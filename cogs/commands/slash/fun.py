from disnake.ext import commands
import disnake
from dotenv import load_dotenv
import os
import aiohttp
from simpledemotivators import *
import random

load_dotenv()

dACI = disnake.ApplicationCommandInteraction

class SlashFunCommand(commands.Cog):

    def __init__(
        self, 
        bot: commands.Bot
    ):
        self.bot = bot

    @commands.slash_command()
    async def fun(
        self,
        ctx
    ):
        pass

    @fun.sub_command(name = '8ball', description = 'Magic 8 ball')
    async def ball(
        self,
        ctx: dACI,
        question: str = commands.Param(
            description = 'What do you want to ask?'
        )
    ):
        from data.commands.slash.fun import ball_answers
        await ctx.response.defer(ephemeral = True)
        emb = disnake.Embed(
            title = '🔮 8ball',
            color = 0x52038f
        )
        emb.add_field(
            name = 'You asked me:',
            value = f'{question}'
        )
        emb.add_field(
            name = "Here's my answer:",
            value = f'{random.choice(ball_answers)}'
        )
        await ctx.edit_original_message(embed = emb)
    
    @fun.sub_command(description = 'Make a demotivator')
    async def demotivator(
        self,
        ctx: dACI,
        image: disnake.Attachment = commands.Param(
            description = 'Image'
        ),
        top: str = commands.Param(
            description = 'Top text'
        ),
        bottom: str = commands.Param(
            description = 'Bottom text',
            default = ''
        )
    ):
        await ctx.response.defer(ephemeral = True)
        img_ext = str(image.content_type)
        if img_ext.startswith('image'):
            dem = Demotivator(
                top,
                bottom
            )
            dem.create(
                image,
                use_url = True,
                result_filename = f'dem_quote\dem_{ctx.id}.png',
                delete_file = True
            )
            file = disnake.File(fp = f'dem_quote\dem_{ctx.id}.png')
            emb = disnake.Embed(
                title = ctx.author,
                color = 0x028ade
            )
            emb.set_footer(
                text = 'Made with: https://github.com/Infqq/simpledemotivators'
            )
            emb.set_image(
                file = file
            )
            await ctx.edit_original_message(embed = emb)
            os.remove(f'dem_quote\dem_{ctx.id}.png')
        else:
            emb = disnake.Embed(
                title = "⚠️ The file is not an image",
                color = 0xe36f02
            )
            await ctx.edit_original_message(embed = emb)

    @fun.sub_command(description = 'Create a quote of great men')
    async def quote(
        self,
        ctx: dACI,
        text: str = commands.Param(
            description = 'Quote text'
        )
    ):
        await ctx.response.defer(ephemeral = True)
        quote = Quote(
            text, 
            ctx.author.name
        )
        quote.create(
            ctx.author.display_avatar,
            use_url = True,
            result_filename = f'dem_quote\quote_{ctx.id}.png',
            headline_text = 'Quotes of great men'
        )
        file = disnake.File(fp = f'dem_quote\quote_{ctx.id}.png')
        emb = disnake.Embed(
            title = ctx.author,
            color = 0x028ade
        )
        emb.set_footer(
            text = 'Made with: https://github.com/Infqq/simpledemotivators'
        )
        emb.set_image(
            file = file
        )
        await ctx.edit_original_message(embed = emb)
        os.remove(f'dem_quote\quote_{ctx.id}.png')

    @fun.sub_command(description = 'Shows photos of cats')
    async def cat(
        self,
        ctx: dACI
    ):
        await ctx.response.defer(ephemeral = True)
        async with aiohttp.ClientSession() as session:
            async with session.get("https://some-random-api.ml/animal/cat") as r:
                json_stats = await r.json()
                caturl = json_stats["image"]
                factcat = json_stats["fact"]
                emb = disnake.Embed(
                    title = '😺 Photos of cats',
                    color = 0x028ade
                )
                emb.add_field(
                    name = 'Fact: ',
                    value = f'*{factcat}*',
                    inline = False
                )
                emb.set_image(
                    url = caturl
                )
                emb.set_footer(
                    text = 'Made with: https://some-random-api.ml/'
                )
                await ctx.edit_original_message(embed = emb)

    @fun.sub_command(description = 'Show member avatar')
    async def avatar(
        self,
        ctx: dACI,
        member: disnake.Member = commands.Param(
            description = "Whose avatar do you want to show?"
        )
    ):
        await ctx.response.defer(ephemeral = True)
        emb = disnake.Embed(
            title = f'{member}',
            color = 0x028ade
        )
        emb.set_image(
            url = member.display_avatar
        )
        await ctx.edit_original_message(embed = emb)

    @fun.sub_command(description = 'Checking the weather')
    async def weather(
        self,
        ctx: dACI,
        city: str = commands.Param(
            description = 'City name'
        ),
        country: str = commands.Param(
            description = 'The name a country (write the name with two letters only, for example: United States = US, etc.)',
            default = ''
        )
    ):
        await ctx.response.defer(ephemeral = True)
        api_key = os.getenv('OW_KEY')
        base_url = "http://api.openweathermap.org/data/2.5/weather?lang=en&units=metric&appid="
        complete_url = f'{base_url}{api_key}&q={city},{country}'
        async with aiohttp.ClientSession() as session:
            async with session.get(complete_url) as r:
                x = await r.json()
                code = x["cod"]
                match code:
                    case 200:
                        y = x["main"]
                        w = x["wind"]
                        s = x["sys"]
                        z = x["weather"]
                        fullname = x["name"]
                        current_temperature = y["temp"]
                        current_humidity = y["humidity"]
                        current_feelslike = y["feels_like"]
                        current_speed = w["speed"]
                        country = s["country"]
                        weather_description = z[0]["description"]
                        icon = z[0]["icon"]
                        icon_url = f'https://openweathermap.org/img/wn/{icon}@4x.png'
                        emb_200 = disnake.Embed(
                            title = f"🌡️ Weather in {fullname}\nCountry: {country}",
                            color = 0x028ade
                        )
                        emb_200.add_field(
                            name = "Temperature now:", 
                            value = f"**{current_temperature}°C**", 
                            inline = True
                        )
                        emb_200.add_field(
                            name = "Feels like:", 
                            value = f"**{current_feelslike}°C**", 
                            inline = True
                        )
                        emb_200.add_field(
                            name = "Description:", 
                            value = f"**{weather_description.title()}**", 
                            inline = False
                        )
                        emb_200.add_field(
                            name = "Humidity:", 
                            value = f"**{current_humidity}%**", 
                            inline = False
                        )
                        emb_200.add_field(
                            name = "Wind speed:", 
                            value = f"**{current_speed} m/s**", 
                            inline = False
                        )
                        emb_200.set_thumbnail(
                            url = icon_url
                        )
                        emb_200.set_footer(
                            text = "Source: OpenWeather"
                        ) 
                        await ctx.edit_original_message(embed = emb_200)
                    case "404":
                        match country:
                            case '':
                                emb_404 = disnake.Embed(
                                    title = f'⚠️ The city "{city}" was not found!',
                                    description = 'Please check the correct spelling of the city and try again',
                                    color = 0xe36f02
                                )
                                await ctx.edit_original_message(embed = emb_404)
                            case _:
                                emb_404 = disnake.Embed(
                                    title = f'⚠️ The city "{city}" in the country "{country}" was not found!',
                                    description = 'Please check the correct spelling of the city and country and try again',
                                    color = 0xe36f02
                                )
                                await ctx.edit_original_message(embed = emb_404)
                    case 401:
                        emb_401 = disnake.Embed(
                            title = '⚠️ API key error!',
                            description = 'The error has been reported to the developer',
                            color = 0xe36f02
                        )
                        await ctx.edit_original_message(embed = emb_401)
                        print(f'⚠️⚠️⚠️ OpenWeather error: 401')
                    case 429:
                        emb_429 = disnake.Embed(
                            title = '⚠️ Too many requests!',
                            description = 'Please try again later',
                            color = 0xe36f02
                        )
                        await ctx.edit_original_message(embed = emb_429)
                    case 500 | 502 | 503 | 504:
                        emb_5xx = disnake.Embed(
                            title = '⚠️ Unknown error!',
                            description = 'The error has been reported to the developer',
                            color = 0xe36f02
                        )
                        await ctx.edit_original_message(embed = emb_5xx)
                        print(f'⚠️⚠️⚠️ OpenWeather 5xx error: {code}')

def setup(
    bot: commands.Bot
):
    bot.add_cog(SlashFunCommand(bot))