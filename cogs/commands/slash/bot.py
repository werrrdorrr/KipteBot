from disnake.ext import commands
import disnake
import aiohttp

dACI = disnake.ApplicationCommandInteraction

class SlashBotCommand(commands.Cog):

    def __init__(
        self, 
        bot: commands.Bot
    ):
        self.bot = bot

    @commands.slash_command()
    async def bot(
        self,
        ctx
    ):
        pass

def setup(
    bot: commands.Bot
):
    bot.add_cog(SlashBotCommand(bot))