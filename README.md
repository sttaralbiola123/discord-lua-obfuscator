# 🔐 Discord Lua Obfuscator Bot

A powerful Discord bot that obfuscates Lua code with support for Discord slash commands and a beautiful web dashboard. Perfect for protecting Lua scripts for Roblox executors like Delta, Synapse X, Oxygen U, and more!

## ✨ Features

- 🤖 **Discord Bot** - Slash commands for easy obfuscation
- 🌐 **Web Dashboard** - Beautiful UI for code obfuscation
- 🔒 **Multiple Protection Levels** - Light, Medium, Heavy
- 📁 **File Support** - Upload and obfuscate Lua files
- 🎯 **Advanced Obfuscation:**
  - Remove comments and whitespace
  - Variable renaming
  - String encryption (Base64)
  - Junk code injection
  - Full minification
- 📊 **Real-time Stats** - See compression ratios and code size
- 🚀 **Ready for Render** - One-click deployment

## 🎯 Discord Commands

```
/obfuscate code <code> level:<light/medium/heavy>  - Obfuscate inline code
/obfuscate file <file.lua> level:<light/medium/heavy> - Obfuscate uploaded file
/help                                                  - Show help message
/invite                                               - Get bot invite link
```

## 🌐 Web Dashboard

Access the web interface at `https://your-render-url.onrender.com`

- 📝 Paste or upload code
- 🎛️ Choose protection level
- 📋 Copy to clipboard
- ⬇️ Download as .lua file
- 📊 View compression stats

## ⚙️ Protection Levels

### 🟢 Light
- Comment removal
- Minification
- Minimal compression
- Best for testing

### 🟡 Medium (Recommended)
- Comment removal
- Minification
- Variable renaming
- Good balance of protection and readability

### 🔴 Heavy
- Everything from Medium, plus:
- String encryption
- Junk code injection
- Maximum obfuscation
- 60%+ compression

## 🚀 Deployment

### Requirements
- Python 3.9+
- Discord Bot Token
- Render account (free)

### Quick Deploy to Render

1. **Get Discord Bot Token:**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create New Application → Add Bot
   - Copy TOKEN
   - Enable Message Content Intent

2. **Push to GitHub:**
   - Create repository
   - Push all files

3. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - New Web Service → Select your repo
   - Build: `pip install -r requirements.txt`
   - Start: `python bot.py`
   - Add environment variables:
     - `DISCORD_TOKEN` = Your bot token
     - `FLASK_ENV` = production
     - `PORT` = 5000
   - Click Create!

4. **Invite Bot:**
   - Developer Portal → OAuth2 → URL Generator
   - Scopes: bot + applications.commands
   - Permissions: Send Messages, Embed Links, Attach Files
   - Copy URL → Invite to server

## 📝 Installation (Local)

```bash
# Clone repository
git clone https://github.com/yourusername/discord-lua-obfuscator.git
cd discord-lua-obfuscator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "DISCORD_TOKEN=your_token_here" > .env
echo "FLASK_ENV=development" >> .env
echo "PORT=5000" >> .env

# Run bot
python bot.py
```

## 🔧 Configuration

Edit `config.py` to customize:
- Bot status
- Protection level defaults
- File size limits
- Code length limits
- Discord embed colors

## 📚 File Structure

```
.
├── bot.py                 # Discord bot with slash commands
├── app.py                 # Flask web server
├── obfuscator.py         # Lua obfuscation engine
├── config.py             # Configuration
├── requirements.txt      # Python dependencies
├── Procfile              # Render deployment config
├── README.md             # This file
├── DEPLOYMENT.md         # Detailed deployment guide
└── templates/
    └── index.html        # Web dashboard UI
```

## 🤝 Usage Examples

### Discord Bot

```
# Simple obfuscation
/obfuscate code:print("Hello World") level:heavy

# File obfuscation
/obfuscate file:myscript.lua level:medium
```

### Web API

```python
import requests

# Obfuscate code
response = requests.post('https://your-bot.onrender.com/api/obfuscate', json={
    'code': 'print("test")',
    'level': 'heavy'
})

result = response.json()
print(result['obfuscated'])
print(result['stats'])
```

## 📊 Performance

- Light Level: ~10ms
- Medium Level: ~50ms
- Heavy Level: ~100ms

## ⚠️ Important Notes

- Keep your Discord token SECRET
- Never commit tokens to GitHub
- Use environment variables for sensitive data
- Test obfuscated code before using in production
- Some complex Lua patterns may not obfuscate perfectly

## 🐛 Troubleshooting

**Bot not responding to commands?**
- Check Message Content Intent is enabled
- Make sure bot has proper permissions
- Restart bot in Render dashboard

**Obfuscation failed?**
- Check code doesn't exceed 50KB
- Verify Lua syntax is correct
- Check Render logs for errors

**Web dashboard not loading?**
- Wait for Flask to start (check logs)
- Verify PORT is set to 5000
- Clear browser cache

## 📞 Support

- Check `DEPLOYMENT.md` for detailed guides
- Review error messages in Render logs
- Test locally before deploying

## 📄 License

MIT License - Feel free to use and modify!

## 🙏 Credits

- Discord.py for the Discord API wrapper
- Flask for web server
- Render for hosting

---

**Made with ❤️ for the Lua scripting community**
