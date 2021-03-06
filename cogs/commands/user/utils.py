from disnake.ext import commands
import disnake
from dotenv import load_dotenv

load_dotenv()

dACI = disnake.ApplicationCommandInteraction

class UserUtilsCommand(commands.Cog):
    
    def __init__(
        self, 
        bot: commands.Bot
    ):
        self.bot = bot

    @commands.user_command(name = 'Avatar')
    async def avatar(
        self,
        inter: dACI,
        member: disnake.Member
    ):
        await inter.response.defer(ephemeral = True)
        emb = disnake.Embed(
            title = f'{member}',
            color = 0x81A1C1
        )
        emb.set_image(
            url = member.display_avatar
        )
        await inter.edit_original_message(embed = emb)

def setup(
    bot: commands.Bot
):
    bot.add_cog(UserUtilsCommand(bot))