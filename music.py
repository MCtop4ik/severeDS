import discord
from discord.ext import commands


def addEmbedField(emb, name, value):
    emb.add_field(name=name, value=value)
    return emb


class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nightcore(self, ctx):
        emb = discord.Embed(title="Музыка Nightcore", color=discord.Color.random())
        emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        emb.set_thumbnail(url='https://img.youtube.com/vi/KlNHoCcDAUE/hqdefault.jpg')
        emb = addEmbedField(emb, "Nightcore - FRIENDS", 'https://www.youtube.com/watch?v=Aba7gEvAfB4')
        emb = addEmbedField(emb, "Nightcore - Solo", 'https://www.youtube.com/watch?v=KlNHoCcDAUE')
        emb = addEmbedField(emb, "Nightcore - Bad Boy", 'https://www.youtube.com/watch?v=jVZxfy_awus')
        emb = addEmbedField(emb, "Nightcore - Discord", 'https://www.youtube.com/watch?v=UJnFD9Koy0Q')
        emb = addEmbedField(emb, "Nightcore - Teeth", 'https://www.youtube.com/watch?v=XPK2HP8bn68')
        emb = addEmbedField(emb, "Nightcore - Drag Me Down", 'https://www.youtube.com/watch?v=8Ok2nQl93lM')
        await ctx.send(embed=emb)
