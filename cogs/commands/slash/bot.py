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
        inter
    ):
        pass

    @bot.sub_command(description = 'About bot')
    async def about(
        self,
        inter: dACI
    ):
        await inter.response.defer(ephemeral = True)
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
        await inter.edit_original_message("Hi, I'm a Discord bot written on the Disnake library.", view = view)

    @bot.sub_command(description = 'Bot latency check')
    async def ping(
        self, 
        inter: dACI
    ):
        await inter.response.defer(ephemeral = True)
        async with aiohttp.ClientSession() as session:
            async with session.get("https://discordstatus.com/api/v2/status.json") as r:
                x = await r.json()
                y = x["status"]
                description = y["description"]
                emb = disnake.Embed(
                    title = "Bot status",
                    color = 0x81A1C1
                )
                emb.add_field(
                    name = "Bot latency: ",
                    value = f"{round(self.bot.latency * 1000)}ms"
                )
                emb.add_field(
                    name = "Discord status: ",
                    value = description
                )
                await inter.edit_original_message(embed = emb)

def setup(
    bot: commands.Bot
):
    bot.add_cog(SlashBotCommand(bot))