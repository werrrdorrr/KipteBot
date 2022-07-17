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

    @party.sub_command(description = 'Watch together YouTube')
    async def youtube(
        self,
        ctx,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await ctx.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.watch_together,
            max_age = 300
        )
        await ctx.edit_original_message(f'[Click me]({invite}) (The link is valid for 5 minutes)')

    @party.sub_command(description = 'Poker Night game (Requires Boost Level 1)')
    async def poker(
        self,
        ctx,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await ctx.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.poker,
            max_age = 300
        )
        await ctx.edit_original_message(f'[Click me]({invite}) (The link is valid for 5 minutes)')

    @party.sub_command(description = 'Word Snacks game')
    async def word_snack(
        self,
        ctx,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await ctx.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.word_snack,
            max_age = 300
        )
        await ctx.edit_original_message(f'[Click me]({invite}) (The link is valid for 5 minutes)')
    
    @party.sub_command(description = 'SpellCast game (Requires Boost Level 1)')
    async def spellcast(
        self,
        ctx,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await ctx.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.spellcast,
            max_age = 300
        )
        await ctx.edit_original_message(f'[Click me]({invite}) (The link is valid for 5 minutes)')

    @party.sub_command(description = 'Sketch Heads game')
    async def sketch_heads(
        self,
        ctx,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await ctx.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.sketch_heads,
            max_age = 300
        )
        await ctx.edit_original_message(f'[Click me]({invite}) (The link is valid for 5 minutes)')

    @party.sub_command(description = 'Ocho game (Requires Boost Level 1)')
    async def ocho(
        self,
        ctx,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await ctx.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.ocho,
            max_age = 300
        )
        await ctx.edit_original_message(f'[Click me]({invite}) (The link is valid for 5 minutes)')
    
    @party.sub_command(description = 'Chess In The Park game (Requires Boost Level 1)')
    async def chess(
        self,
        ctx,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await ctx.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.chess,
            max_age = 300
        )
        await ctx.edit_original_message(f'[Click me]({invite}) (The link is valid for 5 minutes)')

    @party.sub_command(description = 'Fishington.io game')
    async def fishing(
        self,
        ctx,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await ctx.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.fishing,
            max_age = 300
        )
        await ctx.edit_original_message(f'[Click me]({invite}) (The link is valid for 5 minutes)')

    @party.sub_command(description = 'Betrayal.io game')
    async def betrayal(
        self,
        ctx,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await ctx.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.betrayal,
            max_age = 300
        )
        await ctx.edit_original_message(f'[Click me]({invite}) (The link is valid for 5 minutes)')

    @party.sub_command(description = 'Letter Tile game (Requires Boost Level 1)')
    async def letter_tile(
        self,
        ctx,
        voice: disnake.VoiceChannel = commands.Param(
            description = 'Select the voice channel you want'
        )
    ):
        await ctx.response.defer()
        invite = await voice.create_invite(
            target_type = disnake.InviteTarget.embedded_application, 
            target_application = disnake.PartyType.letter_tile,
            max_age = 300
        )
        await ctx.edit_original_message(f'[Click me]({invite}) (The link is valid for 5 minutes)')

def setup(
    bot: commands.Bot
):
    bot.add_cog(SlashPartyCommand(bot))
    