from disnake.ext import commands
import disnake
import os
import aiohttp
from simpledemotivators import *
import random

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
        inter
    ):
        pass

    @fun.sub_command(name = '8ball', description = 'Magic 8 ball')
    async def ball(
        self,
        inter: dACI,
        question: str = commands.Param(
            description = 'What do you want to ask?'
        ),
        ephemeral: bool = commands.Param(
            description = 'Make the message visible only to you? (The default value is True)',
            default = True
        )
    ):
        from data.commands.slash.fun import ball_answers
        await inter.response.defer(ephemeral = ephemeral)
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
        await inter.edit_original_message(embed = emb)
    
    @fun.sub_command(description = 'Make a demotivator')
    async def demotivator(
        self,
        inter: dACI,
        image: disnake.Attachment = commands.Param(
            description = 'Image'
        ),
        top: str = commands.Param(
            description = 'Top text'
        ),
        bottom: str = commands.Param(
            description = 'Bottom text',
            default = ''
        ),
        ephemeral: bool = commands.Param(
            description = 'Make the message visible only to you? (The default value is True)',
            default = True
        )
    ):
        await inter.response.defer(ephemeral = ephemeral)
        img_ext = str(image.content_type)
        if img_ext.startswith('image'):
            dem = Demotivator(
                top,
                bottom
            )
            dem.create(
                image,
                use_url = True,
                font_name = 'fonts/PTSerif-Regular.ttf',
                result_filename = f'dem_{inter.id}.png',
                delete_file = True
            )
            file = disnake.File(fp = f'dem_{inter.id}.png')
            emb = disnake.Embed(
                title = inter.author,
                color = 0x028ade
            )
            emb.set_footer(
                text = 'Made with: https://github.com/Infqq/simpledemotivators'
            )
            emb.set_image(
                file = file
            )
            await inter.edit_original_message(embed = emb)
            os.remove(f'dem_{inter.id}.png')
        else:
            emb = disnake.Embed(
                title = "⚠️ The file is not an image",
                color = 0xe36f02
            )
            await inter.edit_original_message(embed = emb)

    @fun.sub_command(description = 'Create a quote of great men')
    async def quote(
        self,
        inter: dACI,
        text: str = commands.Param(
            description = 'Quote text'
        ),
        ephemeral: bool = commands.Param(
            description = 'Make the message visible only to you? (The default value is True)',
            default = True
        )
    ):
        await inter.response.defer(ephemeral = ephemeral)
        quote = Quote(
            text, 
            inter.author.name
        )
        quote.create(
            inter.author.display_avatar,
            use_url = True,
            quote_text_font = 'fonts/PTSerif-Italic.ttf',
            author_name_font = 'fonts/PTSerif-Italic.ttf',
            headline_text_font = 'fonts/PTSerif-Regular.ttf',
            result_filename = f'quote_{inter.id}.png',
            headline_text = 'Quotes of great men'
        )
        file = disnake.File(fp = f'quote_{inter.id}.png')
        emb = disnake.Embed(
            title = inter.author,
            color = 0x028ade
        )
        emb.set_footer(
            text = 'Made with: https://github.com/Infqq/simpledemotivators'
        )
        emb.set_image(
            file = file
        )
        await inter.edit_original_message(embed = emb)
        os.remove(f'quote_{inter.id}.png')

    @fun.sub_command(description = 'Shows photos of cats')
    async def cat(
        self,
        inter: dACI,
        ephemeral: bool = commands.Param(
            description = 'Make the message visible only to you? (The default value is True)',
            default = True
        )
    ):
        await inter.response.defer(ephemeral = ephemeral)
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
                await inter.edit_original_message(embed = emb)

def setup(
    bot: commands.Bot
):
    bot.add_cog(SlashFunCommand(bot))