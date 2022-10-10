import sqlite3

import discord
from discord.ext import commands


def addEmbedField(emb, name, value):
    emb.add_field(name=name, value=value)
    return emb


class SchoolTimetableCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def schoolTimetableCreate(self, ctx, name):
        base = sqlite3.connect("discord.db")
        base.execute('CREATE TABLE IF NOT EXISTS {}(name, guildid,'
                     'monday_1, monday_2, monday_3, monday_4, monday_5, monday_6, monday_7, monday_8,'
                     'tuesday_1, tuesday_2, tuesday_3, tuesday_4, tuesday_5, tuesday_6, tuesday_7, tuesday_8,'
                     'wednesday_1, wednesday_2, wednesday_3, wednesday_4, wednesday_5, wednesday_6, wednesday_7, '
                     'wednesday_8,'
                     'thursday_1 ,thursday_2, thursday_3, thursday_4, thursday_5, thursday_6, thursday_7, thursday_8,'
                     'friday_1, friday_2, friday_3, friday_4, friday_5, friday_6, friday_7, friday_8,'
                     'saturday_1, saturday_2, saturday_3, saturday_4, saturday_5, saturday_6, saturday_7,'
                     'saturday_8)'.format('timetable'))
        base.commit()

        cur = base.cursor()
        cur.execute('INSERT INTO timetable(name, guildid, monday_1, tuesday_1, wednesday_1, thursday_1, friday_1,'
                    'saturday_1) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (name, ctx.message.guild.id, '-', '-', '-',
                                                                    '-', '-', '-'))
        base.commit()
        await ctx.send('Timetable created successfully')

    @commands.command()
    async def editSchoolTimetable(self, ctx, timetable, day, lesson, name, room="", lessontime=""):
        base = sqlite3.connect("discord.db")
        cur = base.cursor()
        day_table = day + "_" + lesson
        dbinfo = name + " " + room + " " + lessontime
        cur.execute(f'UPDATE timetable SET {day_table} == ? WHERE name == ?', (dbinfo, timetable))
        base.commit()
        await ctx.send("Информация добавлена в расписание")

    @commands.command()
    async def schoolTimetable(self, ctx, name):
        emb = discord.Embed(title=f"Расписание {name}", color=discord.Color.random())
        emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        base = sqlite3.connect("discord.db")
        cur = base.cursor()

        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        days_ru = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
        for i in range(6):
            info = ""
            for j in range(1, 9):
                column = f"{days[i]}_{str(j)}"
                getLesson = cur.execute(f"SELECT {column} FROM timetable WHERE name == '{name}'").fetchone()
                if str(getLesson[0]) != "None":
                    info += str(j) + '. ' + str(getLesson[0]) + '\n'
            emb = addEmbedField(emb, days_ru[i], info)
        await ctx.send(embed=emb)
