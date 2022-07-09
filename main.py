import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = disnake.Intents.default()
intents.members = True

bot = commands.InteractionBot(
    test_guilds = [986294560365903933],
    reload = True,
    sync_commands_debug = True,
    intents = intents
    )

for ext in [
    'cogs.commands.slash.fun',
    'cogs.commands.slash.admin',
    'cogs.commands.user.fun',
    'cogs.error.error'
    ]:  
    bot.load_extension(ext)

print('Connecting to Discord servers...')

@bot.event
async def on_ready():
    print("The bot is ready!")
    
bot.run(os.getenv('TOKEN'))