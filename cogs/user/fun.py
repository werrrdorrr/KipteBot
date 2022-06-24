from disnake.ext import commands
import disnake
from dotenv import load_dotenv

load_dotenv()

dACI = 'disnake.ApplicationCommandInteraction'

class UserFunCommand(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.user_command(name='Avatar')
    async def avatar(
        self,
        ctx: dACI,
        member: disnake.Member
        ):
        emb = disnake.Embed(title=f'{member}',color=0xf7e645)
        emb.set_image(url=member.display_avatar)
        await ctx.response.send_message(embed=emb,ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(UserFunCommand(bot))