from disnake.ext import commands
import disnake
from dotenv import load_dotenv
import os
import aiohttp

load_dotenv()

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

    @utils.sub_command(description = 'Show member avatar')
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

    @utils.sub_command(description = 'Checking the weather')
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
    bot.add_cog(SlashUtilsCommand(bot))