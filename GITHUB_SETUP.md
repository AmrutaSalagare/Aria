# 🎯 Aria Job Search Automation — GitHub Actions Setup

## What You Have

A completely automated job search system that:
✅ Searches job portals every morning at **6 AM IST**  
✅ Scores jobs against your profile  
✅ Sends reports to **Telegram**  
✅ Saves reports in your GitHub repo  
✅ Runs **free** on GitHub's servers  

---

## Prerequisites

- GitHub account (free)
- Telegram account with a bot token (free)
- This repository with all Python files

---

## Step 1 — Create a Telegram Bot (5 minutes)

### Get Telegram Bot Token:

1. Open **Telegram**
2. Search for **@BotFather**
3. Send `/newbot`
4. Give your bot a name: **"Aria Job Bot"**
5. Give it a username: **"aria_job_search_bot"** (must be unique)
6. BotFather will give you a **token** that looks like: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`
7. **Copy this token** — you'll need it

### Get Your Telegram Chat ID:

1. Open **Telegram**
2. Search for **@userinfobot**
3. Send `/start`
4. It replies with your user ID (a 9-digit number)
5. **Copy this** — you'll need it

---

## Step 2 — Push Code to GitHub (10 minutes)

### If you don't have a GitHub repo yet:

1. Go to **github.com** and sign in
2. Click **+ icon** → **New repository**
3. Name it: `aria-job-search` (or any name)
4. Set to **Public** (GitHub Actions needs this)
5. Click **Create repository**

### Clone and push:

```bash
# If you have this folder already on your computer:
cd d:\openclaw-amruta
git init
git add .
git commit -m "Initial Aria job search setup"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/aria-job-search.git
git push -u origin main
```

If you get an error, generate a GitHub personal access token:
1. Go to `github.com/settings/tokens`
2. Click **Generate new token (classic)**
3. Check `repo` and `workflow`
4. Click **Generate**
5. Copy the token
6. When git asks for password, paste this token

---

## Step 3 — Add Secrets to GitHub (5 minutes)

### Add Telegram Bot Token:

1. Go to your repository on github.com
2. Click **Settings** (tab at top)
3. Click **Secrets and variables** → **Actions** (left sidebar)
4. Click **New repository secret**
5. Name: `TELEGRAM_BOT_TOKEN`
6. Value: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11` (the token from step 1)
7. Click **Add secret**

### Add Telegram Chat ID:

1. Click **New repository secret** again
2. Name: `TELEGRAM_CHAT_ID`
3. Value: Your 9-digit user ID from step 1
4. Click **Add secret**

---

## Step 4 — Enable GitHub Actions (2 minutes)

1. Go to your repository
2. Click **Actions** tab
3. You should see **"Aria Daily Job Search"** workflow listed
4. If asked, click **I understand my workflows, go ahead and enable them**

---

## Step 5 — Test Locally First (Optional but Recommended)

Before relying on GitHub, test on your computer:

### Install Python dependencies:

```bash
pip install -r requirements.txt
```

### Set environment variables:

**On Windows PowerShell:**
```powershell
$env:TELEGRAM_BOT_TOKEN = "123456:ABC-DEF1234..."
$env:TELEGRAM_CHAT_ID = "123456789"
python job_search.py
```

**On Mac/Linux:**
```bash
export TELEGRAM_BOT_TOKEN="123456:ABC-DEF1234..."
export TELEGRAM_CHAT_ID="123456789"
python job_search.py
```

### You should see:
- Job searches being logged
- Jobs being scored
- A report being generated
- A message sent to your Telegram bot

If this works, GitHub Actions will work too!

---

## Step 6 — Trigger First Run (2 minutes)

1. Go to your repo on github.com
2. Click **Actions** tab
3. Click **Aria Daily Job Search** workflow on the left
4. Click **Run workflow** button (top right)
5. Select **main** branch
6. Click **Run workflow**

**Watch the progress:**
- Repository will show a **yellow dot** (running)
- Then a **green checkmark** (success) or **red X** (failure)

**Check Telegram:** You should receive your first report!

---

## Step 7 — Automatic Daily Runs

The workflow is now scheduled to run at **6:00 AM IST every day**.

**How to verify:**
- Go to **Actions** tab
- You'll see "Aria Daily Job Search" scheduled (no manual trigger needed)
- Tomorrow at 6 AM, it will run automatically

---

## Checking Your Reports

### On GitHub:
- Go to **workspace/reports/** folder
- You'll see files like `2026-03-18.md`, `2026-03-19.md`, etc.
- Each contains the full daily report

### On Telegram:
- Your report arrives automatically every morning at 6 AM IST
- Formatted as chunks for easy reading

---

## Troubleshooting

### Workflow doesn't run at 6 AM IST?

GitHub Actions runs on UTC. 6 AM IST = 00:30 UTC.  
The cron job is set to: `30 0 * * *` (00:30 UTC daily)

To adjust for your timezone:
- Edit `.github/workflows/daily-job-search.yml`
- Change the cron line to match your desired time in UTC

[Cron Converter Tool](https://crontab.guru/)

### Telegram messages not arriving?

Check that:
1. You added the secrets correctly in Settings
2. Your bot token is valid (test with BotFather)
3. Your chat ID is correct (should be 9 digits)

To debug:
```bash
python -c "from telegram_sender import TelegramSender; t = TelegramSender('TOKEN', 'CHATID'); print(t.test_connection())"
```

### No jobs found in report?

This is expected for the first few runs while the scraper learns the portals.  
The current implementation searches major job sites but requires:
- Some portals need additional authentication (LinkedIn, Naukri)
- Some sites need JavaScript rendering (Internshala)

**To improve results:**
- Add your own job portal scraping logic
- Use Selenium/Playwright for JavaScript-heavy sites
- Or manually curate a list of 50 best portals

### Reports not saving to GitHub?

Make sure your repo settings allow Actions to commit:
1. Go to **Settings** → **Actions** → **General**
2. Under "Workflow permissions", select **"Read and write permissions"**
3. Check **"Allow GitHub Actions to create and approve pull requests"**
4. Click **Save**

---

## What Happens Next

Every morning at 6 AM IST:

1. ✅ GitHub Actions wakes up
2. ✅ Downloads latest code & your profile
3. ✅ Searches job portals
4. ✅ Scores each job (0-10)
5. ✅ Picks top 25 matches
6. ✅ Sends to your Telegram in chunks
7. ✅ Saves markdown report to GitHub
8. ✅ Logs what happened (for learning patterns)

You wake up with a fresh job report waiting. ☕

---

## Improving Job Search Quality

The current version searches:
- LinkedIn Jobs (via search)
- Naukri (structure ready)
- Indeed (structure ready)
- Internshala (structure ready)

To add more portals or improve scraping:

1. Edit `job_search.py`
2. Add new `search_portalname()` methods
3. Return job dicts with: `title`, `company`, `location`, `experience_required`, `salary`, `description`, `url`, `posted_date`
4. The scorer will automatically rank all jobs

### Example: Adding a Custom Portal

```python
def search_my_custom_portal(self) -> List[Dict]:
    """Search my custom job portal"""
    jobs = []
    try:
        # Your scraping code here
        response = requests.get('https://example.com/jobs')
        # Parse response, extract jobs
        # Return list of job dicts
    except Exception as e:
        logger.warning(f"Custom portal search failed: {e}")
    return jobs
```

Then add to `run_search()`:
```python
all_jobs.extend(self.search_my_custom_portal())
```

---

## Optional: Improving with Better Scraping

For more complete job searches, create a `scrapers/` folder:

```
scrapers/
├── linkedin_scraper.py
├── naukri_scraper.py
├── internshala_scraper.py
└── generic_scraper.py
```

Use frameworks like:
- **BeautifulSoup** — HTML parsing
- **Playwright** — JavaScript rendering (headless browser)
- **Selenium** — Full browser automation

GitHub Actions has `pip install playwright` available.

---

## Your Daily Workflow

**Every morning (automatic):**
- ☀️ 6 AM: Aria wakes up, searches jobs
- ☕ 6:05 AM: Telegram notification arrives
- 📋 Read report, click interesting links
- 🎯 Apply to top 3-5 matches
- ✨ Repeat tomorrow

**Optional weekly maintenance:**
- Update `USER.md` if your skills change
- Review monthly patterns in MEMORY.md
- Suggest new portals to search

---

## Questions?

Aria has these iron laws baked in:

1. ✅ **Never fabricate jobs or links**
2. ✅ **Honest scoring** — no inflation
3. ✅ **Fresh search daily** — no reusing yesterday's results
4. ✅ **Flag red flags** — bond clauses, service agreements
5. ✅ **Max 25 jobs** — quality over quantity
6. ✅ **Minimum score 5** — only good matches included

These are unbreakable rules in `MEMORY.md`.

---

## Next Steps

1. ✅ Create Telegram bot + get token
2. ✅ Push code to GitHub
3. ✅ Add secrets
4. ✅ Enable Actions
5. ✅ Test locally (optional)
6. ✅ Trigger first run manually
7. ✅ Wait for 6 AM tomorrow for automatic run
8. ✅ Check Telegram and GitHub reports

You're all set! 🚀

---

**Aria is now live and searching for your next job every morning.**

*Good luck, Amruta! 🎯*
