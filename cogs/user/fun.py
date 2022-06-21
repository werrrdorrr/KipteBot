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
        ctx,
        member: disnake.Member
        ):
        
        if member.avatar == None:
            emb = disnake.Embed(title='⚠️ The user has no avatar.',color=0xe36f02)
            await ctx.response.send_message(embed=emb,ephemeral=True)
        else:
            emb = disnake.Embed(title=f'{member}',color=0xf7e645)
            emb.set_image(url=member.avatar)
            await ctx.response.send_message(embed=emb,ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(UserFunCommand(bot))