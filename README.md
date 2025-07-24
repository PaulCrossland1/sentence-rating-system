# AI Sentence Rating System

A Python application that uses Google's Gemini AI to rate sentences based on three creative dimensions: **Humor**, **Creativeness**, and **Fun**. The system implements relative scoring with zero-centered mean, ensuring ratings are contextual to the entire input set.

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Google Gemini API key (get one [here](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd sentence-rating-system
   ```

2. **Set up the environment**
   ```bash
   # Create virtual environment
   python3 -m venv .venv
   
   # Activate it
   source .venv/bin/activate  # On Windows: .\.venv\Scripts\Activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Configure your API key**
   ```bash
   # Copy the example file
   cp .env.example .env.local
   
   # Edit .env.local and add your API key
   # Replace "your_actual_api_key_here" with your real key
   ```

4. **Add sentences to rate**
   ```bash
   # Edit sentences.txt - one sentence per line
   nano sentences.txt
   ```

5. **Run the application**
   ```bash
   python rate_sentences.py > output.csv
   ```

## 🎯 Features

- **Relative Scoring**: Ratings are relative to the entire input set
- **Zero-Centered Mean**: Average score across all sentences for each metric is 0
- **CSV Output**: Clean, machine-readable format
- **Secure Configuration**: Environment variable management for API keys
- **Flexible Input**: Rate any number of sentences

## 📊 Understanding the Output

The system generates a CSV file with these columns:

| Column | Description | Range |
|--------|-------------|--------|
| `entrant` | 1-based index for each sentence | 1, 2, 3... |
| `sentence` | Original sentence text | - |
| `humor` | Relative humor rating | -1.000 to 1.000 |
| `creativeness` | Relative creativeness rating | -1.000 to 1.000 |
| `fun` | Relative fun rating | -1.000 to 1.000 |
| `total` | Sum of the three ratings | -3.000 to 3.000 |

### Scoring Examples

**High creativity, low humor**: "The purple banana flew a spaceship to Tuesday."
- humor: 0.333, creativeness: 0.667, fun: 0.667

**Low creativity, low humor**: "The cat sat on the mat."
- humor: -0.667, creativeness: -0.667, fun: -0.667

**High humor, average creativity**: "Why don't scientists trust atoms? Because they make up everything!"
- humor: 0.667, creativeness: -0.333, fun: 0.333

## ⚙️ Configuration

### Environment Variables
Create a `.env.local` file (from `.env.example`):

```bash
GEMINI_API_KEY=your_actual_api_key_here
```

### Input File Format
Create `sentences.txt` with one sentence per line:

```
The cat sat on the mat.
The purple banana flew a spaceship to Tuesday.
Why don't scientists trust atoms? Because they make up everything!
```

## 🔧 Technical Details

### Dependencies
- `google-genai` - Google AI SDK
- `python-dotenv` - Environment variable management

### File Structure
```
sentence-rating-system/
├── .env.example          # Environment variables template
├── .env.local           # Your local environment (git-ignored)
├── .gitignore          # Git ignore rules
├── rate_sentences.py   # Main application
├── requirements.txt    # Python dependencies
├── sentences.txt       # Input sentences
└── output.csv          # Generated output
```

### API Configuration
The system uses Google's Gemini 1.5 Flash model with:
- Temperature: 0.2 (for consistent, structured output)
- Response format: Plain text CSV

## 🛡️ Security Best Practices

- **Never commit API keys** - `.env.local` is in `.gitignore`
- **Use environment variables** - Never hardcode secrets
- **Check configuration** - Always verify `.env.example` for required variables
- **Review permissions** - Ensure your API key has appropriate restrictions

## 🐛 Troubleshooting

### Common Issues

**"GEMINI_API_KEY not found"**
- Ensure `.env.local` exists and contains your API key
- Check file permissions: `ls -la .env.local`

**"Module not found"**
- Activate virtual environment: `source .venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

**"Rate limit exceeded"**
- Check your Google AI Studio quota
- Consider adding delays between large batches

### Debug Mode
Run with verbose output:
```bash
python rate_sentences.py
```

## 📝 Development

### Adding New Features
1. Create a feature branch: `git checkout -b feature-name`
2. Make your changes
3. Test thoroughly
4. Submit a pull request

### Requirements Update
```bash
pip freeze > requirements.txt
```

## 📄 License
MIT License - feel free to use and modify as needed.

## 🤝 Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request with a clear description

## 📞 Support
For issues and questions:
- Check the troubleshooting section above
- Open an issue on GitHub
- Ensure your API key and environment are properly configured