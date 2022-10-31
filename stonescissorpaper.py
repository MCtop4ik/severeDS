import discord
from discord.ext import commands


class GameCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dictionary = {
            "stone": ["acid", "paper"],
            "paper": ["scissors", "lamp"],
            "scissors": ["acid", "stone"],
            "lamp": ["scissors", "stone"],
            "acid": ["lamp", "paper"]
        }
        self.save = {}

    @commands.command()
    async def playpss(self, ctx, first: str, opponent: str):
        print(self.save)
        print(opponent)
        if opponent in self.save.keys():
            await ctx.send(self.winner(first, self.save[opponent]))
            self.save.pop(opponent, None)
        else:
            self.save[ctx.author.mention] = first

    def winner(self, first: str, second: str):
        if first == second:
            return "draw"
        else:
            if first in self.dictionary[second]:
                return "second"
            else:
                return "first"
