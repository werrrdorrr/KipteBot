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

    @fun.sub_command(description = 'Bot latency check')
    async def ping(
        self, 
        ctx: dACI
        await ctx.response.defer(ephemeral=True)
        await ctx.edit_original_message(f"🏓 Pong! {round(self.bot.latency * 1000)}ms")
    ):
    
    @fun.sub_command(description = 'About bot')
    async def about(
        self,
        ctx: dACI
        await ctx.response.defer(ephemeral=True)
    ):
        view = disnake.ui.View()
        item = disnake.ui.Button(
            style = disnake.ButtonStyle.url, 
            label = "Bot repository", 
            url = "https://github.com/werrrdorrr/KipteBot"
        )
        item2 = disnake.ui.Button(
            style = disnake.ButtonStyle.url,
            label = 'Disnake library',
            url = 'https://github.com/DisnakeDev/disnake'
        )
        view.add_item(item = item)
        view.add_item(item = item2)
        await ctx.edit_original_message("Hi, I'm a Discord bot written on the Disnake library.", view = view)

    @fun.sub_command(name = '8ball',description = 'Magic 8 ball')
    async def ball(
        self,
        ball_answers=["It is certain.","It is decidedly so.","Without a doubt.","Yes definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
        ctx: dACI,
        question: str = commands.Param(
            description = 'What do you want to ask?'
        )
    ):
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
        else:
            emb = disnake.Embed(
                title = "⚠️ The attachment is not a image",
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
                await ctx.edit_original_message(embed = emb)

    @fun.sub_command(description = 'Send an anonymous message')
    async def msg(
        self,
        ctx: dACI,
        user: disnake.Member = commands.Param(
            description = 'Who do you want to write to?'
        ),
        content: str = commands.Param(
            description = 'What do you want to write?'
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
        await user.send(embed = emb_msg)
        emb_done = disnake.Embed(
            title = '✅ Done!',
            color = 0x1d9e00
        )
        await ctx.edit_original_message(embed = emb_done)
    
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
    ):
        await ctx.response.defer(ephemeral = True)
        api_key = os.getenv('OW_KEY')
        base_url = "http://api.openweathermap.org/data/2.5/weather?lang=en&units=metric&appid="
        complete_url = f'{base_url}{api_key}&q={city},{country}'
        async with aiohttp.ClientSession() as session:
            async with session.get(complete_url) as r:
                x = await r.json()
                code = x["cod"]
                badcode = [500,502,503,504]
                if code == 200:
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
                elif code == "404":
                    emb_404 = disnake.Embed(title=f'⚠️ The city "{city}" was not found!',description='Check for a typo in the name of your city and try again.',color=0xe36f02)
                    await ctx.edit_original_message(embed=emb_404)
                elif code == 401:
                    emb_401 = disnake.Embed(
                        title = '⚠️ API key error!',
                        description = 'The error has been reported to the developer',
                        color = 0xe36f02
                    )
                    await ctx.edit_original_message(embed = emb_401)
                    print(f'⚠️⚠️⚠️ OpenWeather error: 401')
                elif code == 429:
                    emb_429 = disnake.Embed(
                        title = '⚠️ Too many requests!',
                        description = 'Please try again later',
                        color = 0xe36f02
                    )
                    await ctx.edit_original_message(embed = emb_429)
                elif code in badcode:
                    emb_5xx = disnake.Embed(
                        title = '⚠️ Unknown error!',
                        description = 'The error has been reported to the developer',
                        color = 0xe36f02
                    )
                    await ctx.edit_original_message(embed = emb_5xx)
                    print(f'⚠️⚠️⚠️ OpenWeather 5xx error: {code}')
                else:
                    emb_unknown = disnake.Embed(
                        title = '⚠️ Unknown error!',
                        description = 'The error has been reported to the developer',
                        color = 0xe36f02
                    )
                    await ctx.edit_original_message(embed = emb_unknown)
                    print(f'⚠️⚠️⚠️ OpenWeather unknown error: {code}')

def setup(
    bot: commands.Bot
):
    bot.add_cog(SlashFunCommand(bot))