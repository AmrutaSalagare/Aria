# 🚀 GitHub Setup — Final Steps (3 minutes)

Your credentials are received and ready! Here's what to do now.

---

## Step 1: Create GitHub Repository (2 minutes)

### Go to GitHub & Create Repo

1. Go to **https://github.com/new**
2. **Repository name:** `aria-job-search`
3. **Description:** "Automated daily fresher job search for Amruta"
4. **Visibility:** `Public` (required for GitHub Actions free tier)
5. **Initialize with:** Leave everything blank
6. Click **Create repository**

You'll see a screen with code to push. You'll need the repository URL.

---

## Step 2: Add GitHub Secrets (1 minute)

After creating the repository:

1. Go to your repo → **Settings** (top tab)
2. In left sidebar: **Secrets and variables** → **Actions**
3. Click **New repository secret**

### Secret 1:
- **Name:** `TELEGRAM_BOT_TOKEN`
- **Value:** `8649568407` (your bot token from @BotFather)
- Click **Add secret**

### Secret 2:
- Click **New repository secret** again
- **Name:** `TELEGRAM_CHAT_ID`
- **Value:** `5201142003` (your chat ID from @userinfobot)
- Click **Add secret**

**Verify both secrets are now listed** ✓

---

## Step 3: Push Your Code (Run This Command)

Open **PowerShell** and run this command. Replace `GITHUB_USERNAME` with **AmrutaSalagare**:

```powershell
cd d:\openclaw-amruta
git remote add origin https://github.com/AmrutaSalagare/aria-job-search.git
git branch -M main
git push -u origin main
```

**What happens:**
- GitHub may ask for authentication
- If it asks for password: Copy an access token (see below)
- Then press Enter

---

## If GitHub Asks for Password

GitHub will ask for a personal access token instead of password:

1. Go to **https://github.com/settings/tokens**
2. Click **Generate new token** → **Generate new token (classic)**
3. Check box: `repo` (full control of private repositories)
4. Check box: `workflow` (update GitHub Actions and deployment workflows)
5. Scroll to bottom, click **Generate token**
6. **Copy the token** (you'll only see it once)
7. Go back to PowerShell, when it asks for password: **Paste the token** and press Enter

---

## Step 4: Verify It Worked

After `git push` succeeds:

1. Go to your GitHub repo: `https://github.com/AmrutaSalagare/aria-job-search`
2. You should see all your files
3. Click **Actions** tab
4. You should see **"Aria Daily Job Search"** workflow listed

---

## Step 5: Test the Automation (Optional)

### Option A: Test on GitHub (Recommended)
1. Go to repo → **Actions** tab
2. Click **Aria Daily Job Search**
3. Click **Run workflow** button
4. Select `main` branch
5. Click **Run workflow**

**Watch it run:**
- Yellow dot = Running
- Green checkmark = Success ✓
- Check Telegram → you should get a message!

### Option B: Test Locally (Skip if You Did This Already)
```powershell
cd d:\openclaw-amruta
pip install -r requirements.txt
$env:TELEGRAM_BOT_TOKEN = "8649568407"
$env:TELEGRAM_CHAT_ID = "5201142003"
python job_search.py
```

---

## 🎉 You're Done!

**After pushing to GitHub:**

✅ Code is on GitHub  
✅ Telegram secrets are configured  
✅ Automation is ready  
✅ Your repo will auto-run tomorrow at 6 AM IST ⏰  
✅ You'll get Telegram reports automatically  

---

## 📅 What Happens Tomorrow

6:00 AM IST → GitHub Actions runs automatically →Finds job opportunities → Sends report to your Telegram ✓

Then every morning at 6 AM for the next year, Aria will:
- 🔍 Search job portals
- 📊 Score and rank jobs
- 💬 Send Telegram report
- 💾 Save to GitHub

---

## ✋ Need Help?

| Problem | Solution |
|---------|----------|
| Can't create GitHub repo | Go to github.com/new directly |
| Can't add secrets | Go to repo → Settings → Secrets |
| git push fails | Check you have git installed and GitHub username is correct |
| No Telegram message | Check secrets are added correctly in GitHub Settings |

---

## ✨ Commands Summary

```powershell
# Create GitHub secrets first, then:
cd d:\openclaw-amruta

# Add GitHub as remote
git remote add origin https://github.com/AmrutaSalagare/aria-job-search.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## 🎯 Once Code Is Pushed

Your GitHub repo URL will be:
```
https://github.com/AmrutaSalagare/aria-job-search
```

Bookmark it! That's where your daily reports will be saved. 📁

---

## 💡 What's Your Telegram Bot Token Again?

⚠️ **Important:** The bot token you provided is `8649568407` but this looks like it's missing the colon and secret part. 

A complete Telegram bot token looks like:
```
123456:ABCxyz1234567890abcdefghijklmnop
```
(Number, colon, then alphanumeric secret)

**Is `8649568407` your complete token, or did you only provide part of it?**

If you only provided part, please get the FULL token from @BotFather and let me know. The GitHub setup will fail if the token is incomplete.

---

**Ready to push? Let me know if the bot token is complete or if you need to update it!** ✨
