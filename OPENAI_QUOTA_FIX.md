# OpenAI Quota/Billing Issue - How to Fix

## Understanding the Error

**Error 429 - Insufficient Quota** means:
- ✅ Your API key is **working correctly** (authentication successful)
- ❌ Your OpenAI account has **no credits** or has **exceeded its quota**

## How to Fix This

### Step 1: Check Your OpenAI Account Billing

1. **Go to OpenAI Platform**: https://platform.openai.com/
2. **Navigate to Billing**:
   - Click your profile icon (top right)
   - Select "Billing" or go to: https://platform.openai.com/account/billing
3. **Check Your Usage**:
   - View your current usage
   - Check if you have any credits remaining
   - See your spending limits

### Step 2: Add Payment Method (Required for API Usage)

**Free Tier Limitations:**
- OpenAI no longer offers free API credits for new accounts
- You need to add a payment method to use the API

**To Add Payment Method:**
1. Go to: https://platform.openai.com/account/billing/payment-methods
2. Click "Add payment method"
3. Enter your credit card details
4. Set up a usage limit if desired (to control costs)

### Step 3: Set Usage Limits (Recommended)

To avoid unexpected charges:
1. Go to: https://platform.openai.com/account/billing/limits
2. Set a **hard limit** (e.g., $10/month)
3. Set a **soft limit** (e.g., $5/month) for notifications

### Step 4: Check Your Plan

1. Go to: https://platform.openai.com/account/usage
2. Check which model you're using:
   - `gpt-4o` - More expensive, higher quality
   - `gpt-4o-mini` - Cheaper, still good quality (fallback in code)
3. Consider switching to `gpt-4o-mini` if cost is a concern

### Step 5: Verify Credits Are Added

After adding payment method:
- Wait a few minutes for the account to update
- Check billing dashboard shows available credits
- Try generating alt text again

## Cost Information

**Current Pricing (as of 2024):**
- **GPT-4o**: ~$2.50-$10 per 1M input tokens, ~$10-$30 per 1M output tokens
- **GPT-4o-mini**: ~$0.15 per 1M input tokens, ~$0.60 per 1M output tokens

**For Alt Text Generation:**
- Each image uses ~1-2 tokens input + ~50-150 tokens output
- **GPT-4o-mini**: ~$0.0001-0.0003 per image (very cheap!)
- **GPT-4o**: ~$0.001-0.003 per image

**Example Costs:**
- 100 images with GPT-4o-mini: ~$0.01-0.03
- 100 images with GPT-4o: ~$0.10-0.30

## Alternative Solutions

### Option 1: Use GPT-4o-mini Only (Cheaper)

The code already falls back to `gpt-4o-mini` if `gpt-4o` fails. You can modify the code to use `gpt-4o-mini` by default to save costs.

### Option 2: Check for Free Alternatives

If you need a free solution, consider:
- Using a different AI service (Claude, Gemini, etc.)
- Using local models (requires more setup)
- Manual alt text generation

### Option 3: Request Credits

If you're a student or researcher:
- Check OpenAI's research/education programs
- Apply for credits: https://openai.com/research

## Verify the Fix

After adding payment method and credits:

1. **Wait 2-3 minutes** for account to update
2. **Restart your Django server** (to ensure fresh connection)
3. **Try generating alt text again**
4. **Check the error** - should be gone!

## Still Having Issues?

1. **Check API Status**: https://status.openai.com/
2. **Contact OpenAI Support**: https://help.openai.com/
3. **Verify API Key**: Make sure the key is active in your account
4. **Check Rate Limits**: You might be hitting rate limits (different from quota)

## Quick Checklist

- [ ] Added payment method to OpenAI account
- [ ] Set usage limits (optional but recommended)
- [ ] Verified credits are available
- [ ] Waited a few minutes for account update
- [ ] Restarted Django server
- [ ] Tried generating alt text again

---

**Note**: The API key is working fine. This is purely a billing/quota issue that needs to be resolved on OpenAI's platform.

