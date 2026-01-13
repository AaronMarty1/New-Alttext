# OpenAI API Key Setup Guide

## Step 1: Get Your OpenAI API Key

1. **Go to OpenAI Platform**: Visit https://platform.openai.com/
2. **Sign up or Log in**: Create an account or log in if you already have one
3. **Navigate to API Keys**: 
   - Click on your profile icon (top right)
   - Select "API keys" from the menu
   - Or go directly to: https://platform.openai.com/account/api-keys
4. **Create a New API Key**:
   - Click "Create new secret key"
   - Give it a name (e.g., "AltText Generator")
   - Click "Create secret key"
   - **IMPORTANT**: Copy the key immediately - you won't be able to see it again!

## Step 2: Set Up the API Key in Your Project

You have two options:

### Option A: Using .env file (Recommended)

1. **Create a `.env` file** in your project root (`/Users/mac21/Downloads/alttext-1/`):
   ```bash
   cd /Users/mac21/Downloads/alttext-1
   touch .env
   ```

2. **Add your API key** to the `.env` file:
   ```bash
   echo "OPENAI_API_KEY=sk-your-actual-api-key-here" > .env
   ```
   
   Or edit the file manually:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

3. **Make sure `.env` is in `.gitignore`** (to keep your key secure):
   ```bash
   echo ".env" >> .gitignore
   ```

### Option B: Export as Environment Variable

**For current session:**
```bash
export OPENAI_API_KEY="sk-your-actual-api-key-here"
```

**For permanent setup (add to your shell profile):**
```bash
# For zsh (default on macOS)
echo 'export OPENAI_API_KEY="sk-your-actual-api-key-here"' >> ~/.zshrc
source ~/.zshrc

# For bash
echo 'export OPENAI_API_KEY="sk-your-actual-api-key-here"' >> ~/.bash_profile
source ~/.bash_profile
```

## Step 3: Verify the Setup

1. **Restart your Django server** (if it's running):
   ```bash
   # Stop the server (Ctrl+C or kill the process)
   # Then restart:
   cd /Users/mac21/Downloads/alttext-1
   source venv/bin/activate
   python manage.py runserver
   ```

2. **Test the API key**:
   - Upload a PDF
   - Extract images
   - Try generating alt text
   - It should work without the 401 error!

## Important Notes

- **API Key Format**: Your key should start with `sk-` (e.g., `sk-proj-...`)
- **Security**: Never commit your `.env` file or API key to version control
- **Costs**: OpenAI API usage is billed per request. Check pricing at: https://openai.com/pricing
- **Rate Limits**: Free tier has rate limits. Paid accounts have higher limits.

## Troubleshooting

### Still getting 401 error?
1. Make sure the API key starts with `sk-`
2. Check for extra spaces or quotes in the `.env` file
3. Restart the Django server after setting the key
4. Verify the key is active in your OpenAI account

### Check if the key is loaded:
```bash
cd /Users/mac21/Downloads/alttext-1
source venv/bin/activate
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('Key found:', bool(os.getenv('OPENAI_API_KEY')))"
```

## Need Help?

- OpenAI API Documentation: https://platform.openai.com/docs
- OpenAI Support: https://help.openai.com/

