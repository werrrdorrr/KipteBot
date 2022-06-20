from disnake.ext import commands
import disnake

dACI = 'disnake.ApplicationCommandInteraction'

class SlashFunCommand(commands.Cog):


    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def fun(self,ctx):
        pass

    @fun.sub_command(description='Bot latency check')
    async def ping(self, ctx: dACI):

        await ctx.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(SlashFunCommand(bot))