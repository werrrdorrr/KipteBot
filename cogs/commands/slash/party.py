from disnake.ext import commands
from funcs.party_button import party_button
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

    @party.sub_command(description = 'Watch together YouTube')
    async def youtube(
        self,
        inter: dACI,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await inter.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.watch_together,
            max_age = 300
        )
        view = disnake.ui.View()
        view.add_item(item = party_button(invite))
        await inter.edit_original_message('Click the button below (valid for 5 minutes)', view = view)

    @party.sub_command(description = 'Poker Night game (Requires Boost Level 1)')
    async def poker(
        self,
        inter: dACI,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await inter.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.poker,
            max_age = 300
        )
        view = disnake.ui.View()
        view.add_item(item = party_button(invite))
        await inter.edit_original_message('Click the button below (valid for 5 minutes)', view = view)

    @party.sub_command(description = 'Word Snacks game')
    async def word_snack(
        self,
        inter: dACI,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await inter.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.word_snack,
            max_age = 300
        )
        view = disnake.ui.View()
        view.add_item(item = party_button(invite))
        await inter.edit_original_message('Click the button below (valid for 5 minutes)', view = view)
    
    @party.sub_command(description = 'SpellCast game (Requires Boost Level 1)')
    async def spellcast(
        self,
        inter: dACI,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await inter.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.spellcast,
            max_age = 300
        )
        view = disnake.ui.View()
        view.add_item(item = party_button(invite))
        await inter.edit_original_message('Click the button below (valid for 5 minutes)', view = view)

    @party.sub_command(description = 'Sketch Heads game')
    async def sketch_heads(
        self,
        inter: dACI,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await inter.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.sketch_heads,
            max_age = 300
        )
        view = disnake.ui.View()
        view.add_item(item = party_button(invite))
        await inter.edit_original_message('Click the button below (valid for 5 minutes)', view = view)

    @party.sub_command(description = 'Ocho game (Requires Boost Level 1)')
    async def ocho(
        self,
        inter: dACI,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await inter.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.ocho,
            max_age = 300
        )
        view = disnake.ui.View()
        view.add_item(item = party_button(invite))
        await inter.edit_original_message('Click the button below (valid for 5 minutes)', view = view)
    
    @party.sub_command(description = 'Chess In The Park game (Requires Boost Level 1)')
    async def chess(
        self,
        inter: dACI,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await inter.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.chess,
            max_age = 300
        )
        view = disnake.ui.View()
        view.add_item(item = party_button(invite))
        await inter.edit_original_message('Click the button below (valid for 5 minutes)', view = view)

    @party.sub_command(description = 'Fishington.io game')
    async def fishing(
        self,
        inter: dACI,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await inter.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.fishing,
            max_age = 300
        )
        view = disnake.ui.View()
        view.add_item(item = party_button(invite))
        await inter.edit_original_message('Click the button below (valid for 5 minutes)', view = view)

    @party.sub_command(description = 'Betrayal.io game')
    async def betrayal(
        self,
        inter: dACI,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await inter.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.betrayal,
            max_age = 300
        )
        view = disnake.ui.View()
        view.add_item(item = party_button(invite))
        await inter.edit_original_message('Click the button below (valid for 5 minutes)', view = view)

    @party.sub_command(description = 'Letter Tile game (Requires Boost Level 1)')
    async def letter_tile(
        self,
        inter: dACI,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await inter.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.letter_tile,
            max_age = 300
        )
        view = disnake.ui.View()
        view.add_item(item = party_button(invite))
        await inter.edit_original_message('Click the button below (valid for 5 minutes)', view = view)

    @party.sub_command(description = 'Checkers In The Park game (Requires Boost Level 1)')
    async def checkers(
        self,
        inter: dACI,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await inter.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.checkers,
            max_age = 300
        )
        view = disnake.ui.View()
        view.add_item(item = party_button(invite))
        await inter.edit_original_message('Click the button below (valid for 5 minutes)', view = view)

def setup(
    bot: commands.Bot
):
    bot.add_cog(SlashPartyCommand(bot))