from disnake.ext import commands
from funcs.party import party_button, party_activity, party_invite
from data.commands.slash.party import choices
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
        inter
    ):
        pass

    @party.sub_command(description = 'Create Discord Activity')
    async def activity(
        self,
        inter: dACI,
        activity: str = commands.Param(
            choices = choices
        ),
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await inter.response.defer()
        invite = await party_invite(voice, party_activity(activity))
        view = disnake.ui.View()
        view.add_item(item = party_button(invite))
        await inter.edit_original_message('Click the button below (valid for 5 minutes)', view = view)

def setup(
    bot: commands.Bot
):
    bot.add_cog(SlashPartyCommand(bot))