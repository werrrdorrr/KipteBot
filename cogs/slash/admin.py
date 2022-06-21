from disnake.ext import commands
import disnake





dACI = 'disnake.ApplicationCommandInteraction'

class SlashAdminCommand(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description='Purge messages')
    @commands.default_member_permissions(manage_messages=True)
    async def purge(
        self, 
        ctx: dACI, 
        msg_count: int = commands.Param(description='How many messages do you want to delete?',min_value=1)
        ):
        
        await ctx.channel.purge(limit=int(msg_count))
        await ctx.response.send_message('Done!', ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(SlashAdminCommand(bot))
