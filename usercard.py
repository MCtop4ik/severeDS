import discord
import requests
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from banklib import Database
import io


class CardCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["я", "карточка"])
    async def card(self, ctx):
        img = Image.new('RGBA', (400, 200), '#0D0033')
        url = str(ctx.author.avatar_url)[:-10]

        response = requests.get(url, stream=True)
        response = Image.open(io.BytesIO(response.content))
        response = response.convert('RGBA')
        response.resize((100, 100), Image.ANTIALIAS)

        img.paste(response, (15, 15))

        idraw = ImageDraw.Draw(img)

        name = ctx.author.name
        tag = ctx.author.discriminator

        headline = ImageFont.truetype('arial.ttf', size=20)
        undertext = ImageFont.truetype('arial.ttf', size=12)
        balance = Database().amount(str(ctx.author.id))

        idraw.text((155, 15), f'{name}#{tag}', font=headline, fill='#ffd700')
        idraw.text((155, 50), f'Balance: {balance}Sev', font=headline)
        idraw.text((240, 180), f'ID: {ctx.author.id}', font=undertext)

        img.save('usercard.png')

        await ctx.send(file=discord.File(fp='usercard.png'))
