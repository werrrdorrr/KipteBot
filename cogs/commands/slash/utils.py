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

    @utils.sub_command(description = 'Send an anonymous message')
    async def msg(
        self,
        ctx: dACI,
        user: disnake.Member = commands.Param(
            description = 'Who do you want to write to?'
        ),
        content: str = commands.Param(
            description = 'What do you want to write?'
        ),
        file: disnake.Attachment = commands.Param(
            description = 'Attach a file to your message',
            default = None
        )
    ):
        await ctx.response.defer(ephemeral = True)
        emb_msg = disnake.Embed(
            title = '📨 You got a message from an anonymous user',
            color = 0x028ade
        )
        emb_msg.add_field(
            name = "Here's what it said: ",
            value = content
        )
        if file is not None:
            file_ext = str(file.content_type)
            if file_ext.startswith('image'):
                emb_msg.set_image(
                    url = file
                )
            else:
                emb_msg.add_field(
                    name = 'The file attached to this message:',
                    value = f'[File]({file})',
                    inline = False
                )
        else:
            pass
        await user.send(embed = emb_msg)
        emb_done = disnake.Embed(
            title = '✅ Done!',
            color = 0x1d9e00
        )
        await ctx.edit_original_message(embed = emb_done)

def setup(
    bot: commands.Bot
):
    bot.add_cog(SlashUtilsCommand(bot))