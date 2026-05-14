# 📚 Detailed Deployment Guide

## Complete Step-by-Step Instructions

### 🟦 Phase 1: Discord Bot Setup (5 minutes)

#### 1.1 Create Discord Application
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application**
3. Give it a name: `Lua Obfuscator` (or your choice)
4. Accept the ToS and click **Create**

#### 1.2 Create Bot User
1. Click **Bot** on the left sidebar
2. Click **Add Bot**
3. Under USERNAME, set the bot name (e.g., "Lua Obfuscator")
4. **COPY THE TOKEN** - You'll need this! ⚠️

#### 1.3 Enable Required Intents
1. Scroll down to **GATEWAY INTENTS**
2. **ENABLE** these intents:
   - ✅ Message Content Intent (REQUIRED!)
   - ✅ Server Members Intent
3. Click **Save Changes**

#### 1.4 Get Bot Invite Link
1. Click **OAuth2** on the left
2. Click **URL Generator**
3. Select these **SCOPES**:
   - ✅ `bot`
   - ✅ `applications.commands`
4. Select these **PERMISSIONS**:
   - ✅ Send Messages
   - ✅ Embed Links
   - ✅ Attach Files
   - ✅ Read Message History
5. **COPY THE GENERATED URL** at the bottom

#### 1.5 Invite Bot to Discord Server
1. Open the URL from 1.4 in your browser
2. Select a server (you need admin rights)
3. Authorize the bot
4. Check if bot appears in your server! ✅

---

### 🟪 Phase 2: Render Deployment (10 minutes)

#### 2.1 Prepare GitHub Repository
1. Make sure all files are in your GitHub repo:
   - `bot.py`
   - `app.py`
   - `obfuscator.py`
   - `config.py`
   - `requirements.txt`
   - `Procfile`
   - `templates/index.html`
   - `README.md`

2. Push all changes to GitHub:
```bash
git add .
git commit -m "Deploy bot to Render"
git push origin main
```

#### 2.2 Create Render Account
1. Go to [render.com](https://render.com)
2. Click **Sign up** (use GitHub for easiest option)
3. Authorize Render to access your GitHub

#### 2.3 Create Web Service
1. Click **New** in dashboard
2. Select **Web Service**
3. Click **Connect Repository**
4. Find and select `discord-lua-obfuscator`
5. Click **Connect**

#### 2.4 Configure Service
Fill in these fields:

| Field | Value |
|-------|-------|
| **Name** | `discord-lua-obfuscator` |
| **Environment** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `python bot.py` |
| **Instance Type** | `Free` (to start) |

#### 2.5 Add Environment Variables
1. Click **Advanced** (if collapsed)
2. Click **Add Environment Variable** for each:

**Variable 1:**
- Key: `DISCORD_TOKEN`
- Value: (Paste your Discord bot token from step 1.2)

**Variable 2:**
- Key: `FLASK_ENV`
- Value: `production`

**Variable 3:**
- Key: `PORT`
- Value: `5000`

#### 2.6 Deploy!
1. Click **Create Web Service**
2. Wait for deployment (usually 3-5 minutes)
3. You'll see logs appearing - watch for "✅ Bot logged in"

#### 2.7 Get Your Bot URL
1. At the top, find your service URL (e.g., `https://discord-lua-obfuscator-xxxxx.onrender.com`)
2. **SAVE THIS URL** - This is your web dashboard!

---

### ✅ Phase 3: Testing (5 minutes)

#### 3.1 Test Discord Bot
1. Go to your Discord server
2. Type: `/help`
3. You should see a beautiful help embed! ✅

#### 3.2 Test Obfuscation Command
1. Type: `/obfuscate code:print("test") level:heavy`
2. Bot should respond with obfuscated code ✅

#### 3.3 Test Web Dashboard
1. Open your Render URL in browser (from 2.7)
2. You should see the web interface
3. Try obfuscating code there ✅

#### 3.4 Test File Upload
1. Create a test file: `test.lua`
2. Add some Lua code
3. Use `/obfuscate file:test.lua level:medium`
4. Bot should download the obfuscated file ✅

---

## 🔧 Troubleshooting

### ❌ Bot not responding to commands
**Solution:**
- Check Message Content Intent is enabled in Developer Portal
- Make sure bot has permissions in the server
- Restart bot in Render dashboard (click disconnect/connect)
- Wait up to 1 hour for slash commands to appear

### ❌ "Obfuscation failed" error
**Solution:**
- Check Render logs for detailed error
- Verify `obfuscator.py` is in repository
- Check code doesn't exceed 50KB limit

### ❌ Web dashboard shows "Connection refused"
**Solution:**
- Wait a bit - Render needs time to start Flask
- Check bot.py is running (check Render logs)
- Verify PORT environment variable is set to 5000

### ❌ "Invalid interaction token"
**Solution:**
- This is usually temporary
- Restart bot in Render
- Or create a new test command

### ❌ File won't upload
**Solution:**
- Check file is `.lua` or `.txt` format
- Ensure file is under 25MB
- Verify bot has "Attach Files" permission

---

## 📊 Monitoring

### Check Bot Status
1. Go to Render dashboard
2. Click your service name
3. Look at **Logs** for:
   - ✅ "Bot logged in as..."
   - ✅ "Synced X command(s)"

### Check Bot Activity
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click your app
3. Check **Usage** tab for activity

### Monitor Render Resource Usage
1. Render dashboard → your service
2. Check CPU/RAM usage
3. Free tier has 0.5 CPU and limited memory

---

## 🚀 After Deployment

### Optional: Upgrade to Paid Render Plan
- Free tier goes to sleep after 15 min inactivity
- Upgrade to keep bot always running
- Starting at $7/month

### Optional: Set Custom Status
Edit `config.py` line 14:
```python
BOT_STATUS = "🔐 Your custom status here"
```

### Optional: Add to More Servers
1. Go back to Discord Developer Portal
2. Get the invite URL (from earlier)
3. Share with friends!

---

## 🎉 You're Done!

Your bot is now:
- ✅ Running on Render (24/7 hosting)
- ✅ Available on Discord
- ✅ Ready to obfuscate Lua code
- ✅ Has a beautiful web dashboard

**Happy scripting! 🔐**

---

## 💡 Pro Tips

1. **Always keep your Discord token secret** - Never share it!
2. **Test locally first** - Before deploying to Render
3. **Monitor logs regularly** - Catch issues early
4. **Update code** - Push to GitHub to auto-deploy
5. **Backup your token** - Save it somewhere safe

---

## 📞 Need Help?

Check these resources:
- [Discord.py Docs](https://discordpy.readthedocs.io/)
- [Render Docs](https://render.com/docs)
- [Flask Docs](https://flask.palletsprojects.com/)
- [GitHub Issues](https://github.com/sttaralbiola123/discord-lua-obfuscator/issues)
