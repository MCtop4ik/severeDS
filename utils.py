import discord
from discord.ext import commands


def addEmbedField(emb, name, value):
    emb.add_field(name=name, value=value)
    return emb


class UtilsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def status(self, ctx, statusbot: str):
        if statusbot == "dnd":
            await self.bot.change_presence(status=discord.Status.dnd,
                                           activity=discord.Game("Бот разрабатывается. Version Severe 1.0.0"))
            await ctx.send('Status do not disturb activated')
        elif statusbot == "sleep":
            await self.bot.change_presence(status=discord.Status.idle,
                                           activity=discord.Game("Бот разрабатывается. Version Severe 1.0.0"))
            await ctx.send('Status sleep activated')
        else:
            await self.bot.change_presence(status=discord.Status.online,
                                           activity=discord.Game("Бот разрабатывается. Version Severe 1.0.0"))
            await ctx.send('Status online activated')

    @commands.command()
    async def memberAvatar(self, ctx, *, avamember: discord.Member = None):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'Аватарка {avamember}')
        userAvatarUrl = avamember.avatar_url
        await ctx.send(userAvatarUrl)

    @commands.command()
    async def clear(self, ctx, amount=None):
        if amount is not None:
            await ctx.channel.purge(limit=int(amount))
        else:
            await ctx.channel.purge(limit=1000)
