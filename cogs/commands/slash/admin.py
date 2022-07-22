from disnake.ext import commands
import disnake

dACI = disnake.ApplicationCommandInteraction

class SlashAdminCommand(commands.Cog):

    def __init__(
        self, 
        bot: commands.Bot
    ):
        self.bot = bot

    @commands.slash_command(description = 'Purge messages')
    @commands.default_member_permissions(manage_messages = True)
    async def purge(
        self, 
        inter: dACI, 
        number: int = commands.Param(
            description = 'How many messages do you want to delete?',
            min_value = 1
        )
    ):
        await inter.response.defer(ephemeral = True)
        await inter.channel.purge(limit = number)
        emb = disnake.Embed(
            title = f'✅ Done, I deleted {number} messages',
            color = 0x1d9e00
        )
        await inter.edit_original_message(embed = emb)

def setup(
    bot: commands.Bot
):
    bot.add_cog(SlashAdminCommand(bot))