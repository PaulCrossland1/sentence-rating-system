import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env.local
load_dotenv('.env.local')

# --- 1. Prepare the Input ---

# The system prompt that instructs the model.
system_prompt = """You are an expert AI tasked with rating sentences based on specific creative dimensions. Your analysis must be relative to the entire list of sentences provided in a single request.

Your task is to process a list of sentences and rate each one on a scale of -1.000 to 1.000 for the following three metrics: Humour, Creativeness, and Fun.

**CRITICAL SCORING INSTRUCTIONS:**
1.  **Relative Scoring:** The scores are not absolute. They must be relative to the other sentences in the list.
2.  **Zero-Centered Mean:** For each metric (Humour, Creativeness, Fun), the average score across ALL sentences MUST be 0. This means if the entire list is very funny, some sentences will still receive negative humour scores (i.e., they are less funny than the group's average) and some will receive positive scores (i.e., they are funnier than the group's average). A score of 0.000 indicates the sentence is of average creativity/humour/fun compared to the rest of the list.
3.  **Scale:** A score of -1.000 represents the lowest relative value in the set, and 1.000 represents the highest.

**OUTPUT FORMAT:**
- You MUST return the data in a CSV format.
- Do not include any other text, explanations, or summaries before or after the CSV data.
- The CSV header must be exactly: `entrant,sentence,humor,creativeness,fun,total`
- **entrant**: A 1-based index for each sentence.
- **sentence**: The original sentence text.
- **humor, creativeness, fun**: The calculated relative scores, formatted to 3 decimal places.
- **total**: The sum of the humor, creativeness, and fun scores, also formatted to 3 decimal places.

**EXAMPLE:**
If you receive the input:
The cat sat on the mat.
The purple banana flew a spaceship to Tuesday.
Why don't scientists trust atoms? Because they make up everything!

Your output should look like this (values are for illustration):
entrant,sentence,humor,creativeness,fun,total
1,"The cat sat on the mat.",-0.855,-0.950,-0.900,-2.705
2,"The purple banana flew a spaceship to Tuesday.",-0.145,0.950,0.750,1.555
3,"Why don't scientists trust atoms? Because they make up everything!",1.000,0.000,0.150,1.150

Now, process the following sentences and generate the CSV output.
"""

# Read the sentences from your text file.
try:
    with open('sentences.txt', 'r') as f:
        user_sentences = f.read()
except FileNotFoundError:
    print("Error: 'sentences.txt' not found. Please create this file and add sentences to it.")
    exit()

# Combine the system prompt and the user's sentences into the final input.
final_input = f"{system_prompt}\n{user_sentences}"


# --- 2. Call the Gemini API ---

def generate():
    """Generates content using the Gemini API and prints the CSV output."""
    try:
        client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    except Exception:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return

    # Note: The user's original code specified 'gemini-2.0-flash-lite',
    # but the prompt and task might perform better with the standard 'gemini-1.5-flash'.
    # You can experiment with either.
    model = "gemini-1.5-flash-latest"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=final_input),
            ],
        ),
    ]
    
    # Requesting plain text output for easy CSV parsing.
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        temperature=0.2 # Lower temperature for more predictable, structured output
    )

    # Use the correct method for the google-genai library
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config
    )
    
    # Clean up the response by removing markdown code block markers
    output = response.text
    if output.startswith("```csv\n"):
        output = output[7:]  # Remove ```csv\n
    if output.endswith("\n```"):
        output = output[:-4]  # Remove \n```
    
    print(output)


if __name__ == "__main__":
    generate()