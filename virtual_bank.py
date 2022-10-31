import discord
import banklib
from discord.ext import commands


class BankCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.account = banklib.Account()

    @commands.command()
    async def balance(self, ctx, user: str):
        await ctx.send(self.account.returnAmount(user))

    @commands.command()
    async def register(self, ctx):
        await ctx.send(self.account.register(str(ctx.author.id)))

    @commands.command()
    async def daily(self, ctx):
        await ctx.send(self.account.dailyCommand(str(ctx.author.id)))

    @commands.command()
    async def transaction(self, ctx, user2, amount):
        await ctx.send(self.account.transfer(str(ctx.author.id), user2[2:][:-1], int(amount)))
