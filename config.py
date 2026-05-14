import os
from dotenv import load_dotenv

load_dotenv()

# Discord Bot Token
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Flask Config
FLASK_ENV = os.getenv("FLASK_ENV", "development")
DEBUG = FLASK_ENV == "development"
PORT = int(os.getenv("PORT", 5000))

# Bot Config
BOT_PREFIX = "!"
BOT_STATUS = "🔐 Protecting your Lua code"

# Obfuscation Config
OBFUSCATION_LEVELS = {
    "light": {
        "remove_comments": True,
        "minify": True,
        "rename_vars": False,
        "encrypt_strings": False
    },
    "medium": {
        "remove_comments": True,
        "minify": True,
        "rename_vars": True,
        "encrypt_strings": False
    },
    "heavy": {
        "remove_comments": True,
        "minify": True,
        "rename_vars": True,
        "encrypt_strings": True,
        "add_junk_code": True
    }
}

# Limits
MAX_CODE_LENGTH = 50000  # 50KB
MAX_FILE_SIZE = 25 * 1024 * 1024  # 25MB

# Colors for Discord embeds
COLORS = {
    "primary": 0x5865F2,    # Discord Blurple
    "success": 0x57AB5E,    # Green
    "error": 0xED4245,      # Red
    "warning": 0xFEA92F     # Orange
}
