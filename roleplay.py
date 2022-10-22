import sqlite3

import discord
from discord.ext import commands


def addEmbedField(emb, name, value):
    emb.add_field(name=name, value=value)
    return emb


class RolePlayCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rp_permission(self, ctx, age: str):
        base = sqlite3.connect('discord.db')
        cur = base.cursor()
        cur.execute('UPDATE servers SET age_permission == ? WHERE id_server == ?', (age, str(ctx.guild.id), ))
        base.commit()
        await ctx.send(age)
