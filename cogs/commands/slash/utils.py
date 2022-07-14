from disnake.ext import commands
import disnake
import os
import aiohttp

dACI = disnake.ApplicationCommandInteraction

class SlashUtilsCommand(commands.Cog):

    def __init__(
        self, 
        bot: commands.Bot
    ):
        self.bot = bot

    @commands.slash_command()
    async def utils(
        self,
        ctx
    ):
        pass

def setup(
    bot: commands.Bot
):
    bot.add_cog(SlashUtilsCommand(bot))