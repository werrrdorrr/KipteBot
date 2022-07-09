from disnake.ext import commands
import disnake
from data.error.error import *

class ErrorCommand(commands.Cog):

    def __init__(
        self, 
        bot: commands.Bot
    ):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_slash_command_error(
        self, 
        ctx, 
        error
    ):
        if isinstance(error, commands.CommandInvokeError):
            if CannotSendMsgUser in str(error):
                emb = disnake.Embed(
                    title = '⚠️ Cannot send messages to this user',
                    color = 0xe36f02
                )
                await ctx.edit_original_message(embed = emb)
            elif InvalidFormBody in str(error): 
                emb = disnake.Embed(
                    title = '⚠️ Invalid form body',
                    color = 0xe36f02
                )
                emb.add_field(
                    name = 'Possible reasons:', 
                    value = 'You may have entered too many characters\nCannot create an embed'
                )
                await ctx.edit_original_message(embed = emb)
            elif UnidentifiedImageError in str(error):
                emb = disnake.Embed(
                    title = '⚠️ Unidentified image error',
                    description = 'Please try another image',
                    color = 0xe36f02
                )
                emb.add_field(
                    name = 'Possible reasons:',
                    value = 'The image is damaged'
                )
                await ctx.edit_original_message(embed = emb)
            elif ContentTypeError in str(error):
                emb = disnake.Embed(
                    title = '⚠️ Invalid content type',
                    color = 0xe36f02
                )
                emb.add_field(
                    name = 'Possible reasons:', 
                    value = 'You may have entered too many characters\nCannot create an embed'
                )
                await ctx.edit_original_message(embed = emb)
            else:
                emb = disnake.Embed(
                    title = '⚠️ Command invoke error',
                    description = f'Error:\n```{error}```',
                    color = 0xe36f02
                )
                await ctx.edit_original_message(embed = emb)

def setup(
    bot: commands.Bot
):
    bot.add_cog(ErrorCommand(bot))