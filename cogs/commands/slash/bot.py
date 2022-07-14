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

    @bot.sub_command(description = 'About bot')
    async def about(
        self,
        ctx: dACI
    ):
        await ctx.response.defer(ephemeral = True)
        view = disnake.ui.View()
        item = disnake.ui.Button(
            style = disnake.ButtonStyle.url, 
            label = "Bot repository", 
            url = "https://github.com/werrrdorrr/KipteBot"
        )
        item2 = disnake.ui.Button(
            style = disnake.ButtonStyle.url,
            label = 'Disnake library',
            url = 'https://github.com/DisnakeDev/disnake'
        )
        view.add_item(item = item)
        view.add_item(item = item2)
        await ctx.edit_original_message("Hi, I'm a Discord bot written on the Disnake library.", view = view)

def setup(
    bot: commands.Bot
):
    bot.add_cog(SlashBotCommand(bot))