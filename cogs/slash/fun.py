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

        await ctx.response.send_message(f"🏓 Pong! {round(self.bot.latency * 1000)}ms", ephemeral=True)
    @fun.sub_command(description='About bot')
    async def about(self,ctx: dACI):
        await ctx.response.send_message("Hi, I'm KipteBot, written on the Disnake library (https://github.com/DisnakeDev/disnake). Bot repository: https://github.com/werrrdorrr/KipteBot")


def setup(bot: commands.Bot):
    bot.add_cog(SlashFunCommand(bot))