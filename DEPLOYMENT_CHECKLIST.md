# 🚀 Deployment Checklist

Your Aria job search automation is ready to deploy! Follow this checklist to get it running.

## ✅ System Status

- ✅ Python scripts created and tested
- ✅ Job scoring engine working (7/10 test score)
- ✅ Configuration complete with your profile
- ✅ GitHub Actions workflow configured
- ✅ All dependencies listed (requirements.txt)

---

## 📋 Pre-Deployment Steps (Do These Now)

### 1. **Get Telegram Bot Credentials** ⏱️ 5 minutes

- [ ] Open Telegram
- [ ] Message [@BotFather](https://t.me/botfather)
- [ ] Send `/newbot`
- [ ] Give bot a name: "Aria Job Bot"
- [ ] Give bot username: "aria_job_search_bot" (must be unique)
- [ ] **COPY BOT TOKEN** → looks like `123456:ABCxyz...`
- [ ] Message [@userinfobot](https://t.me/userinfobot)
- [ ] Send `/start`
- [ ] **COPY YOUR CHAT ID** → 9-digit number

**You now have:**
- Bot Token: `___________________________`
- Chat ID: `___________________________`

---

### 2. **Create GitHub Repository** ⏱️ 5 minutes

- [ ] Go to [github.com/new](https://github.com/new)
- [ ] Repository name: `aria-job-search` (or your preferred name)
- [ ] Description: "Automated daily job search for freshers"
- [ ] Set to **Public** (required for GitHub Actions)
- [ ] Click **Create repository**

**Your GitHub repo URL:**
`https://github.com/YOUR_USERNAME/aria-job-search`

---

### 3. **Push Code to GitHub** ⏱️ 10 minutes

Run these commands in **PowerShell** at `D:\openclaw-amruta`:

```powershell
# Initialize git
git config --global user.email "your.email@gmail.com"
git config --global user.name "Your Name"

# From your project directory
cd d:\openclaw-amruta
git init
git add .
git commit -m "Initial Aria job search setup"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/aria-job-search.git
git push -u origin main
```

**If git asks for password:** Use a GitHub Personal Access Token (see GitHub setup guide)

- [ ] Code pushed to GitHub successfully

---

### 4. **Add Secrets to GitHub** ⏱️ 5 minutes

1. Go to your repo on github.com
2. Click **Settings** (top tab)
3. In left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**

**Add First Secret:**
- [ ] Name: `TELEGRAM_BOT_TOKEN`
- [ ] Value: (paste your bot token)
- [ ] Click **Add secret**

**Add Second Secret:**
- [ ] Click **New repository secret**
- [ ] Name: `TELEGRAM_CHAT_ID`
- [ ] Value: (paste your chat ID)
- [ ] Click **Add secret**

Verify both secrets are listed ✓

---

### 5. **Enable GitHub Actions** ⏱️ 2 minutes

- [ ] Go to your repo
- [ ] Click **Actions** tab
- [ ] If asked, click "I understand, run workflows"
- [ ] You should see "Aria Daily Job Search" workflow listed

---

## 🧪 Testing (Optional but Recommended)

### Test Locally First

```powershell
# Install dependencies
pip install -r requirements.txt

# Set environment variables (Windows PowerShell)
$env:TELEGRAM_BOT_TOKEN = "your_token_here"
$env:TELEGRAM_CHAT_ID = "your_chat_id_here"

# Run the script
python job_search.py
```

**Expected output:**
- `ARIA JOB SEARCH INITIATED`
- Job searches logged
- Jobs scored
- Report generated
- Message sent to Telegram

- [ ] Local test successful

---

### Test on GitHub

1. Go to your repo → **Actions** tab
2. Click **Aria Daily Job Search** (left sidebar)
3. Click blue **Run workflow** button
4. Select `main` branch
5. Click **Run workflow**

**Watch the workflow:**
- Yellow dot = Running
- Green checkmark = Success ✓
- Red X = Failed

- [ ] GitHub Actions test successful
- [ ] Telegram message received

---

## 🎯 Deployment Complete!

When everything above is done:

✅ Your job search automation is **LIVE**

**What happens next:**

📅 **Tomorrow at 6:00 AM IST:**
- GitHub Actions automatically wakes up
- Searches all job portals
- Scores every job
- Sends report to your Telegram
- Saves report to GitHub

☕ **Your next 365 mornings:**
- Wake up → Open Telegram
- Fresh job report waiting ✓
- Read, apply, repeat

---

## 📊 Monitoring

### View Your Reports

**On GitHub:**
- Repository → `workspace/reports/` folder
- You'll see files: `2026-03-19.md`, `2026-03-20.md`, etc.

**On Telegram:**
- Messages arrive automatically every morning
- Formatted in chunks for easy reading

### Check Workflow Status

**On GitHub:**
- Go to **Actions** tab
- See history of all job search runs
- Click any run to see logs

---

## 🔧 Customization After Setup

### Update Your Skills

When you learn something new:
1. Edit `config.py`
2. Find `AMRUTA_PROFILE`
3. Update `languages`, `frameworks`, `specializations`
4. Push to GitHub: `git add . && git commit -m "Update skills" && git push`

### Add More Job Portals

To search additional portals:
1. Edit `job_search.py`
2. Add new `search_portalname()` method
3. Call it in `run_search()`
4. Push to GitHub

---

## ❓ Troubleshooting

| Issue | Fix |
|-------|-----|
| Telegram messages not arriving | Check secrets in GitHub Settings are correct |
| Workflow doesn't run at 6 AM IST | It's scheduled for 00:30 UTC (equals 6 AM IST) |
| No jobs in report | Some portals need login. Update scrapers in `job_search.py` |
| "Command not found: git" | Install Git from [git-scm.com](https://git-scm.com) |
| "ModuleNotFoundError" | Run `pip install -r requirements.txt` |

**For more help:** See `GITHUB_SETUP.md` in the repository.

---

## 📞 Need Help?

**Step 1:** Check the detailed guide: `GITHUB_SETUP.md`  
**Step 2:** Look at GitHub Actions logs: Settings → Actions  
**Step 3:** Run local test: `python job_search.py`  
**Step 4:** Check Telegram bot is valid at [@BotFather](https://t.me/botfather)

---

## 🎉 You're Almost There!

Once you complete all checkboxes above, your automation is **DEPLOYED AND LIVE**.

**Next step:** Go to **GitHub Repository Setup** below and follow the steps.

---

# ⚡ Quick Reference

## Your Credentials
```
Git User: _______________________________
GitHub Repo: https://github.com/________/aria-job-search
Bot Token: [ADDED TO GitHub Secrets]
Chat ID: [ADDED TO GitHub Secrets]
```

## Key Files
- `job_search.py` — Main automation script
- `config.py` — Your profile and preferences
- `scorer.py` — Job scoring engine
- `.github/workflows/daily-job-search.yml` — GitHub Actions schedule
- `workspace/reports/` — Where daily reports are saved

## Useful Commands
```bash
# Test locally
python job_search.py

# Install dependencies
pip install -r requirements.txt

# View latest report
cat workspace/reports/$(date +%Y-%m-%d).md

# Push changes to GitHub
git add . && git commit -m "Update" && git push
```

---

**Aria is ready. Time to find your next job.**

🎯 **Good luck, Amruta!**
