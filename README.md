# Daily AI Report

An automated system to fetch and email the top 3 most important AI development news stories every morning at 9 AM.

## Features

✅ **Automated Daily Emails** - Sends top 3 AI news stories at 9 AM UTC  
✅ **No Manual Setup Required** - Configure once, runs forever  
✅ **Beautiful Email Format** - Clean, professional HTML emails  
✅ **Multiple News Sources** - Pulls from Hacker News and more  
✅ **Customizable** - Easy to modify keywords, time, and recipients  

## Quick Start

### Step 1: Add Email Configuration Secrets

Go to your repository: **Settings → Secrets and variables → Actions**

Add the following secrets:

#### Using Mailgun (Recommended - Free tier available)
```
RECIPIENT_EMAIL = linshu.simon@gmail.com
MAILGUN_DOMAIN = your-domain.mailgun.org
MAILGUN_API_KEY = your-mailgun-api-key
```

1. Sign up at [mailgun.com](https://www.mailgun.com)
2. Create an account and verify your domain
3. Find your API key in the dashboard
4. Copy domain and API key to GitHub secrets above

### Step 2: Verify Workflow is Active

- Go to your repository's **Actions** tab
- Confirm the workflow "Daily AI News Report" is listed and enabled

### Step 3: Test It (Optional)

1. Click on "Daily AI News Report" workflow
2. Click "Run workflow" → "Run workflow"
3. Watch it execute in real-time
4. Check your email inbox in a few seconds

## How It Works

```
GitHub Actions Scheduler (9 AM UTC daily)
         ↓
   Run Python Script
         ↓
   Fetch AI News from Hacker News
         ↓
   Filter for AI Keywords
         ↓
   Generate HTML Email
         ↓
   Send via Mailgun API
         ↓
   📧 Email in your inbox!
```

## Customization

### Change Schedule Time

Edit `.github/workflows/daily-ai-news.yml` and modify the cron expression:

```yaml
on:
  schedule:
    - cron: '0 14 * * *'  # 2 PM UTC instead of 9 AM
```

**Cron Format:** `'minute hour day month day-of-week'`
- `0 9 * * *` = 9 AM UTC every day
- `0 14 * * *` = 2 PM UTC every day
- `30 7 * * 1-5` = 7:30 AM UTC Monday-Friday only

### Add Different AI Keywords

Edit `scripts/fetch_ai_news.py`:

```python
keywords = ['ai', 'machine learning', 'neural network', 'transformer', 'gpt', 'llm', 'deep learning']
```

### Change Recipients

Modify the `RECIPIENT_EMAIL` secret in GitHub Settings.

## Troubleshooting

### Emails not arriving?

1. **Check Actions logs**: Go to Actions tab → Latest workflow run → Check "Send email with news" step
2. **Verify secrets**: Ensure `RECIPIENT_EMAIL`, `MAILGUN_DOMAIN`, and `MAILGUN_API_KEY` are all set
3. **Check spam folder**: Email might be filtered
4. **Test manually**: Click "Run workflow" in Actions tab to test immediately

### "Missing required environment variables" error?

- Go to **Settings → Secrets and variables → Actions**
- Verify all three secrets are present and correctly named:
  - `RECIPIENT_EMAIL`
  - `MAILGUN_DOMAIN`
  - `MAILGUN_API_KEY`

### No news found?

- The script filters for AI-related keywords
- Try running manually to see debug output
- Adjust keywords in `scripts/fetch_ai_news.py`

## Files

- `.github/workflows/daily-ai-news.yml` - GitHub Actions workflow configuration
- `scripts/fetch_ai_news.py` - Python script to fetch and format news
- `README.md` - This file

## Support

For issues:
1. Check the troubleshooting section above
2. Review the GitHub Actions workflow logs
3. Verify API keys are correct in secrets
4. Test with manual workflow run

## License

MIT License - Feel free to modify and share!

---

**Happy reading!** 📰🤖
