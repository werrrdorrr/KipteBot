from disnake.ext import commands
import disnake
import requests
from dotenv import load_dotenv
import os

load_dotenv()

dACI = 'disnake.ApplicationCommandInteraction'

class SlashFunCommand(commands.Cog):


    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def fun(self,ctx):
        pass

    @fun.sub_command(description='Bot latency check')
    async def ping(
        self, 
        ctx: dACI
        ):
        await ctx.response.send_message(f"🏓 Pong! {round(self.bot.latency * 1000)}ms", ephemeral=True)
    
    @fun.sub_command(description='About bot')
    async def about(
        self,
        ctx: dACI
        ):
        await ctx.response.send_message("Hi, I'm KipteBot, written on the Disnake library (https://github.com/DisnakeDev/disnake). Bot repository: https://github.com/werrrdorrr/KipteBot")

    @fun.sub_command(description='Shows photos of cats')
    async def cat(
        self,
        ctx:dACI
        ):
        url = f"https://some-random-api.ml/animal/cat"
        stats = requests.get(url)
        json_stats = stats.json()
        caturl = json_stats["image"]
        factcat = json_stats["fact"]
        emb = disnake.Embed(title='Photos of cats 😺',color=0xf7e645)
        emb.add_field(name='Fact: ',value=f'*{factcat}*',inline=False)
        emb.set_image(url=caturl)
        await ctx.response.send_message(embed=emb,ephemeral=True)

    @fun.sub_command(description='Send an anonymous message')
    async def msg(
        self,
        ctx,
        user: disnake.Member = commands.Param(description='Who do you want to write to?'),content: str = commands.Param(description='What do you want to write?')
        ):
        
        embmsg = disnake.Embed(title='📨 You got a message from an anonymous user',color=0x021f4f)
        embmsg.add_field(name="Here's what it said: ",value=f'{content}')
        await user.send(embed=embmsg)
        await ctx.response.send_message('Done!',ephemeral=True)
    @msg.error
    async def msg_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.response.send_message("⚠️ Cannot send messages to this user", ephemeral=True)

    @fun.sub_command(description='Checking the weather')
    async def weather(
        self,
        ctx,
        city: str = commands.Param(description='City name')
        ):
        
        api_key = os.getenv('OW_TOKEN')
        base_url = "http://api.openweathermap.org/data/2.5/weather?lang=en&units=metric&appid="
        complete_url = base_url + api_key + "&q=" + city
        response = requests.get(complete_url)
        x = response.json()
        code = x["cod"]
        badcode = [500,502,503,504]

        if code == 200:
            y = x["main"]
            w = x["wind"]
            s = x["sys"]
            fullname = x["name"]
            current_temperature = y["temp"]
            current_humidity = y["humidity"]
            current_feelslike = y["feels_like"]
            current_speed = w["speed"]
            z = x["weather"]
            weather_description = z[0]["description"]
            icon = z[0]["icon"]
            icon_url = f'https://openweathermap.org/img/wn/{icon}@4x.png'
            embed = disnake.Embed(title=f"🌡️ Weather in {fullname}",color=0x0094FF)
            embed.add_field(name="Temperature now:", value=f"**{current_temperature}°C**", inline=True)
            embed.add_field(name="Feels like:", value=f"**{current_feelslike}°C**", inline=True)
            embed.add_field(name="Description:", value=f"**{weather_description.title()}**", inline=False)
            embed.add_field(name="Humidity:", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Wind speed:", value=f"**{current_speed} m/s**", inline=False)
            embed.set_thumbnail(url=icon_url)
            embed.set_footer(text="Source: OpenWeather") 
            await ctx.response.send_message(embed=embed,ephemeral=True)
        elif code == "404":
            emb_404 = disnake.Embed(title=f'⚠️ City of "{city}" not found!',description='Check for a typo in the name of your city and try again.',color=0xe36f02)
            await ctx.response.send_message(embed=emb_404,ephemeral=True)
        elif code == 401:
            emb_401 = disnake.Embed(title='⚠️ API key error!',description='The error has been reported to the developer.',color=0xe36f02)
            await ctx.response.send_message(embed=emb_401,ephemeral=True)
            print(f'⚠️⚠️⚠️ OpenWeather error: 401')
        elif code == 429:
            emb_429 = disnake.Embed(title='⚠️ Too many requests!',description='Try again later.',color=0xe36f02)
            await ctx.response.send_message(embed=emb_429,ephemeral=True)
        elif code in badcode:
            emb_5xx = disnake.Embed(title='⚠️ Unknown error!',description='The error has been reported to the developer.',color=0xe36f02)
            await ctx.response.send_message(embed=emb_5xx,ephemeral=True)
            print(f'⚠️⚠️⚠️ OpenWeather 5xx error: {code}')
        else:
            emb_unknown = disnake.Embed(title='⚠️ Unknown error!',description='The error has been reported to the developer.',color=0xe36f02)
            await ctx.response.send_message(embed=emb_unknown,ephemeral=True)
            print(f'⚠️⚠️⚠️ OpenWeather unknown error: {code}')

def setup(bot: commands.Bot):
    bot.add_cog(SlashFunCommand(bot))