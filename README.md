# Aria Job Search — Quick Start

## 🚀 Get Started in 10 Minutes

### 1. Create Telegram Bot (5 min)
- Message [@BotFather](https://t.me/botfather) on Telegram
- Send `/newbot`
- Follow steps → get **BOT TOKEN**
- Message [@userinfobot](https://t.me/userinfobot) → get **CHAT ID**

### 2. Create GitHub Repo (3 min)
```bash
cd d:\openclaw-amruta
git init
git add .
git config user.email "your.email@gmail.com"
git config user.name "Your Name"
git commit -m "Initial Aria setup"
git remote add origin https://github.com/YOUR_USERNAME/aria-job-search.git
git push -u origin main
```

### 3. Add Secrets (2 min)
- Go to repo → **Settings** → **Secrets** → **Actions**
- Add `TELEGRAM_BOT_TOKEN` = your bot token
- Add `TELEGRAM_CHAT_ID` = your chat ID

### 4. Test Locally
```bash
pip install -r requirements.txt
set TELEGRAM_BOT_TOKEN=your_token  # Windows
set TELEGRAM_CHAT_ID=your_id
python job_search.py
```

### 5. Enable Automation
- Go to **Actions** tab on GitHub
- Click **Run workflow** to test
- It will run automatically tomorrow at 6 AM IST

---

## 📁 File Structure

```
aria-job-search/
├── job_search.py              ← Main automation script
├── scorer.py                  ← Job scoring engine
├── config.py                  ← Your profile & settings
├── telegram_sender.py         ← Telegram integration
├── requirements.txt           ← Python dependencies
├── .github/
│   └── workflows/
│       └── daily-job-search.yml  ← GitHub Actions schedule
├── workspace/
│   └── reports/               ← Daily reports saved here
├── GITHUB_SETUP.md           ← Full setup guide
└── README.md                 ← This file
```

---

## 🎯 What It Does

**Every morning at 6 AM IST:**
1. Searches major job portals
2. Scores each job 0-10 based on your profile
3. Keeps top 25 matches
4. Sends report to your Telegram
5. Saves markdown report to GitHub

---

## 🔧 Customization

### Update Your Profile
Edit `config.py` → `AMRUTA_PROFILE` section:
- Add/remove skills
- Change preferred locations
- Update salary expectations
- Adjust job preferences

### Add More Job Portals
Edit `job_search.py`:
```python
def search_my_portal(self) -> List[Dict]:
    # Add your scraping code
    return jobs

# In run_search():
all_jobs.extend(self.search_my_portal())
```

### Adjust Scoring Weights
Edit `scorer.py` → `score_job()` method:
```python
# Increase skills weight
score += self._score_skills_match(job) * 1.5
```

---

## ⚙️ Troubleshooting

| Problem | Solution |
|---------|----------|
| No Telegram messages | Check secrets in GitHub Settings |
| No jobs in report | Job portals might need authentication |
| Workflow not running | Check Actions tab, enable if needed |
| Jobs not scoring high | Update your skills in `config.py` |

---

## 📊 Scoring System

Jobs are scored **0-10** based on:
- **Role match** (0-3): How well title matches your preferences
- **Skills match** (0-4): How many of your skills match requirements
- **Experience** (0-2): Fresher-eligible preferred
- **Location** (0-1): Preferred cities get bonus
- **Salary** (0-0.5): Within your range gets bonus
- **Red flags** (-2): Bond clauses, suspicious sites penalized

**Minimum to include:** 5/10

---

## 🛡️ Iron Laws

These rules are embedded in the system and can't be broken:

1. Never fabricate job links or company names
2. Never inflate match scores
3. Never reuse yesterday's results
4. Always read your profile before searching
5. Always flag bond clauses first
6. Always deliver by 6 AM IST
7. Maximum 25 jobs per report
8. Minimum match score 5.0

---

## 📧 Telegram Message Format

```
Good morning Amruta!

Your job report is ready.
25 fresh opportunities found today.

🏆 Top Match:
Software Engineer @ TechCorp
Score: 8.5/10

[Full job list follows in chunks...]

📋 Your Action Plan:
1. Review top 3
2. Check bond clauses
3. Prepare cover letter
4. Set referral reminders
5. Apply to 3-5

That's today's full list. Go get it! 🚀
```

---

## 💡 Tips

- **Update skills regularly** when you learn something new
- **Save report links** to track where you applied
- **Look for patterns** in reports (which companies hiring, which locations trending)
- **Customize action plan** in `telegram_sender.py` if needed
- **Add more portals** as you discover good job boards

---

## 📞 Support

For issues:
1. Check `GITHUB_SETUP.md` for detailed troubleshooting
2. Look at workflow run logs in GitHub Actions
3. Test locally with `python job_search.py`
4. Check Telegram bot token is valid

---

**Happy job hunting! 🎯**

*Aria runs every morning at 6 AM IST. You've got this.* ✨
