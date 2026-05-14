import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
from obfuscator import LuaObfuscator
import asyncio

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    print("❌ ERROR: DISCORD_TOKEN not found in environment variables!")
    exit(1)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
obfuscator = LuaObfuscator()

@bot.event
async def on_ready():
    print(f"✅ Bot logged in as {bot.user}")
    print(f"✅ Synced {len(bot.tree.get_commands())} command(s)")
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash command(s) to Discord")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

# HELP Command
@bot.tree.command(name="help", description="Show help and information about the bot")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🔐 Lua Obfuscator Bot",
        description="Protect your Lua scripts for Delta, Synapse X, and other executors!",
        color=0x5865F2
    )
    
    embed.add_field(
        name="📝 Commands",
        value="""
`/obfuscate` - Obfuscate Lua code or files
`/help` - Show this message
`/invite` - Get bot invite link
        """,
        inline=False
    )
    
    embed.add_field(
        name="🎯 Features",
        value="""
✅ Remove Comments & Whitespace
✅ Variable Renaming
✅ String Encryption (Base64)
✅ Add Junk Code
✅ Support for File Uploads
✅ Web Dashboard
        """,
        inline=False
    )
    
    embed.add_field(
        name="⚙️ Protection Levels",
        value="""
🟢 **Light** - Fast, basic minification
🟡 **Medium** - Balanced protection
🔴 **Heavy** - Maximum obfuscation
        """,
        inline=False
    )
    
    embed.add_field(
        name="🌐 Web Dashboard",
        value="Check the bot status/web interface for GUI obfuscation",
        inline=False
    )
    
    embed.set_footer(text="Made with ❤️ | Lua Obfuscator Bot")
    
    await interaction.response.send_message(embed=embed)

# INVITE Command
@bot.tree.command(name="invite", description="Get the bot invite link")
async def invite_command(interaction: discord.Interaction):
    invite_url = f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=2048&scope=bot%20applications.commands"
    
    embed = discord.Embed(
        title="🔗 Invite Bot",
        description=f"[Click here to invite me!]({invite_url})",
        color=0x57AB5E
    )
    
    await interaction.response.send_message(embed=embed, ephemeral=True)

# OBFUSCATE Command
obfuscate_group = app_commands.Group(name="obfuscate", description="Obfuscate Lua code")

@obfuscate_group.command(name="code", description="Obfuscate Lua code directly")
@app_commands.describe(
    code="The Lua code to obfuscate",
    level="Protection level (light/medium/heavy)"
)
async def obfuscate_code(interaction: discord.Interaction, code: str, level: str = "medium"):
    await interaction.response.defer()
    
    if level.lower() not in ["light", "medium", "heavy"]:
        embed = discord.Embed(
            title="❌ Invalid Level",
            description="Please choose: `light`, `medium`, or `heavy`",
            color=0xED4245
        )
        await interaction.followup.send(embed=embed)
        return
    
    if len(code) > 50000:
        embed = discord.Embed(
            title="❌ Code Too Long",
            description="Maximum 50,000 characters allowed",
            color=0xED4245
        )
        await interaction.followup.send(embed=embed)
        return
    
    try:
        obfuscated = obfuscator.obfuscate(code, level.lower())
        
        original_size = len(code.encode('utf-8'))
        obfuscated_size = len(obfuscated.encode('utf-8'))
        compression = ((original_size - obfuscated_size) / original_size * 100) if original_size > 0 else 0
        
        if len(obfuscated) > 2000:
            # Send as file
            import tempfile
            with tempfile.NamedTemporaryFile(mode='w', suffix='.lua', delete=False) as f:
                f.write(obfuscated)
                temp_path = f.name
            
            embed = discord.Embed(
                title="✅ Code Obfuscated!",
                description="File is ready to download",
                color=0x57AB5E
            )
            embed.add_field(name="📊 Stats", value=f"""
**Original:** {original_size:,} bytes
**Obfuscated:** {obfuscated_size:,} bytes
**Compression:** {compression:.1f}%
**Level:** {level.upper()}
            """, inline=False)
            
            await interaction.followup.send(embed=embed, file=discord.File(temp_path, "obfuscated.lua"))
            
            os.remove(temp_path)
        else:
            embed = discord.Embed(
                title="✅ Code Obfuscated!",
                color=0x57AB5E
            )
            embed.add_field(name="📊 Stats", value=f"""
**Original:** {original_size:,} bytes
**Obfuscated:** {obfuscated_size:,} bytes
**Compression:** {compression:.1f}%
**Level:** {level.upper()}
            """, inline=False)
            embed.add_field(name="💻 Code", value=f"```lua\n{obfuscated}\n```", inline=False)
            
            await interaction.followup.send(embed=embed)
    
    except Exception as e:
        embed = discord.Embed(
            title="❌ Obfuscation Failed",
            description=f"Error: {str(e)}",
            color=0xED4245
        )
        await interaction.followup.send(embed=embed)

@obfuscate_group.command(name="file", description="Obfuscate a Lua file")
@app_commands.describe(
    file="The Lua file to obfuscate",
    level="Protection level (light/medium/heavy)"
)
async def obfuscate_file(interaction: discord.Interaction, file: discord.Attachment, level: str = "medium"):
    await interaction.response.defer()
    
    if level.lower() not in ["light", "medium", "heavy"]:
        embed = discord.Embed(
            title="❌ Invalid Level",
            description="Please choose: `light`, `medium`, or `heavy`",
            color=0xED4245
        )
        await interaction.followup.send(embed=embed)
        return
    
    if not file.filename.endswith(('.lua', '.txt')):
        embed = discord.Embed(
            title="❌ Invalid File Type",
            description="Please upload a `.lua` or `.txt` file",
            color=0xED4245
        )
        await interaction.followup.send(embed=embed)
        return
    
    if file.size > 25 * 1024 * 1024:  # 25MB limit
        embed = discord.Embed(
            title="❌ File Too Large",
            description="Maximum 25MB file size allowed",
            color=0xED4245
        )
        await interaction.followup.send(embed=embed)
        return
    
    try:
        code = await file.read()
        code = code.decode('utf-8')
        
        obfuscated = obfuscator.obfuscate(code, level.lower())
        
        original_size = len(code.encode('utf-8'))
        obfuscated_size = len(obfuscated.encode('utf-8'))
        compression = ((original_size - obfuscated_size) / original_size * 100) if original_size > 0 else 0
        
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.lua', delete=False) as f:
            f.write(obfuscated)
            temp_path = f.name
        
        embed = discord.Embed(
            title="✅ File Obfuscated!",
            color=0x57AB5E
        )
        embed.add_field(name="📊 Stats", value=f"""
**Original:** {original_size:,} bytes
**Obfuscated:** {obfuscated_size:,} bytes
**Compression:** {compression:.1f}%
**Level:** {level.upper()}
        """, inline=False)
        
        await interaction.followup.send(embed=embed, file=discord.File(temp_path, "obfuscated.lua"))
        
        os.remove(temp_path)
    
    except Exception as e:
        embed = discord.Embed(
            title="❌ Obfuscation Failed",
            description=f"Error: {str(e)}",
            color=0xED4245
        )
        await interaction.followup.send(embed=embed)

bot.tree.add_command(obfuscate_group)

if __name__ == "__main__":
    bot.run(TOKEN)
