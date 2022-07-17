from disnake.ext import commands
import disnake

dACI = disnake.ApplicationCommandInteraction

class SlashPartyCommand(commands.Cog):

    def __init__(
        self, 
        bot: commands.Bot
    ):
        self.bot = bot

    @commands.slash_command()
    async def party(
        self,
        ctx
    ):
        pass

def setup(
    bot: commands.Bot
):
    bot.add_cog(SlashPartyCommand(bot))
    