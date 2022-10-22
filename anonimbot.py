import sqlite3

import discord
from discord.ext import commands


def addEmbedField(emb, name, value):
    emb.add_field(name=name, value=value)
    return emb


class AnonBCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def startAB(self, ctx):
        base = sqlite3.connect("discord.db")
        cur = base.cursor()

        cur.execute('INSERT INTO anonbotq(id_user) VALUES (?)', (str(ctx.message.author.id),))
        base.commit()
        await ctx.send("Поиск начат")

        isUsers = cur.execute('SELECT * FROM anonbotq').fetchall()
        base.commit()
        if isUsers[1][1] is not None:
            cur.execute('INSERT INTO anonbotpairs(id_1, id_2) VALUES (?, ?)', (str(isUsers[0][1]),
                                                                               str(isUsers[1][1]), ))
            base.commit()
            cur.execute('DELETE FROM anonbotq')
            base.commit()
            await ctx.send("Собеседник найден. Общайтесь")

    @commands.command()
    async def next(self, ctx):
        base = sqlite3.connect("discord.db")
        cur = base.cursor()

        cur.execute('DELETE FROM anonbotpairs WHERE (id_1 == ? or id_2 == ?)', (str(ctx.message.author.id),
                                                                                str(ctx.message.author.id),))

        cur.execute('INSERT INTO anonbotq(id_user) VALUES (?)', (str(ctx.message.author.id),))
        base.commit()
        await ctx.send("Поиск начат")

        isUsers = cur.execute('SELECT * FROM anonbotq').fetchall()
        base.commit()
        if isUsers[1][1] is not None:
            cur.execute('INSERT INTO anonbotpairs(id_1, id_2) VALUES (?, ?)', (str(isUsers[0][1]),
                                                                               str(isUsers[1][1]),))
            base.commit()
            cur.execute('DELETE FROM anonbotq')
            base.commit()
            await ctx.send("Собеседник найден. Общайтесь")

    @commands.command()
    async def stop(self, ctx):
        base = sqlite3.connect("discord.db")
        cur = base.cursor()

        cur.execute('DELETE FROM anonbotpairs WHERE (id_1 == ? or id_2 == ?)', (str(ctx.message.author.id),
                                                                                str(ctx.message.author.id),))
