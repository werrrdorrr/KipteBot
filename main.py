import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
bot = commands.Bot(guild_ids=[986294560365903933],reload=True,sync_commands_debug=True)

print('Connecting to Discord servers...')

@bot.event
async def on_ready():
    print("The bot is ready!")

for ext in ['cogs.slash.fun','cogs.slash.admin','cogs.user.fun']:  
    bot.load_extension(ext)


bot.run(os.getenv('TOKEN'))