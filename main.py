import asyncio

import handmade_crypto
import sqlite3
import quizGames
from help import HelpCog
import discord
from discord_buttons_plugin import *
import qrcode
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from youtube_dl import YoutubeDL
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import pafy
import config
from music import MusicCog
from schoolTimetable import SchoolTimetableCog
from utils import UtilsCog

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)
bot.remove_command("help")
buttons = ButtonsClient(bot)

playlist = {}

'''internal settings'''


async def antiSpam(ctx, arg, content):
    await ctx.message.delete()
    if arg is not None:
        msg = await ctx.send(f"{content}\n Сообщение пропадет через: {arg}")
        for i in range(0, int(arg)):
            await msg.edit(content=f"{content}\n Сообщение пропадет через: {int(arg) - i}")
            await asyncio.sleep(1)
        await msg.delete()
    else:
        await ctx.author.send(f"{content}")


async def timerEmbed(ctx, arg, emb):
    await ctx.message.delete()
    if arg is not None:
        msg = await ctx.send(embed=emb)
        if arg != "stay":
            for i in range(0, int(arg)):
                new_emb = emb
                if i != 0:
                    new_emb.remove_field(index=len(emb.fields) - 1)
                new_emb.add_field(name="Время до удаления", value=f"{int(arg) - i}s")
                await msg.edit(embed=new_emb)
                await asyncio.sleep(1)
            await msg.delete()
    else:
        await ctx.author.send(embed=emb)


def retry(func, retries=3):
    def retry_wrapper(*args, **kwargs):
        attempts = 0
        while attempts < retries:
            try:
                return func(*args, **kwargs)
            except:
                time.sleep(2)
                attempts += 1

    return retry_wrapper


def addEmbedField(emb, name, value):
    emb.add_field(name=name, value=value)
    return emb


server, server_id, name_channel = None, None, None

allGuilds = []


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            embed=discord.Embed(description=f'** {ctx.author.name}, данной команды не существует.**', color=0x0c0c0c))


@bot.event
async def on_ready():
    global allGuilds
    global playlist
    print('bot is ready')
    for guild in bot.guilds:
        allGuilds.append(guild.id)
        playlist = {guild.id: []}
        print(guild.id)
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game("Бот разрабатывается. Version Severe 1.0.0"))


@bot.event
async def on_message(ctx):
    print('new_message')
    await bot.process_commands(ctx)


@bot.command()
async def say_hello(ctx):
    await ctx.send('hello')


'''music'''

playingVoiceChat = False


@retry
@slash.slash(
    name="play",
    description="Just plays a song from youtube",
    guild_ids=allGuilds,
    options=[
        create_option(
            name="ytlink",
            description="Write link from youtube video",
            required=True,
            option_type=3
        )
    ]
)
@bot.command()
async def play(ctx, *, ytlink: str):
    global playingVoiceChat
    if playingVoiceChat:
        await ctx.voice_client.disconnect()
        playingVoiceChat = False
    if ctx.author.voice is None:
        return await ctx.send("You are not connected to a voice channel")
    await ctx.send('Music will start soon')
    vc = await ctx.author.voice.channel.connect()
    with YoutubeDL(config.YDL_OPTIONS) as ydl:
        if 'https://' or 'http://' in ytlink:
            info = ydl.extract_info(ytlink, download=False)
        else:
            info = ydl.extract_info(f"ytsearch:{ytlink}", download=False)['entries'][0]
    url = info['formats'][0]['url']
    vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source=url, **config.FFMPEG_OPTIONS))
    playingVoiceChat = True


@slash.slash(
    name="queue",
    description="Adds music in queue",
    guild_ids=allGuilds,
    options=[
        create_option(name="link",
                      description="Link for music",
                      required=True,
                      option_type=3)
    ]
)
async def addinqueue(ctx, link: str):
    playlist[ctx.guild.id] = playlist.get(ctx.guild.id, []) + [link]
    await ctx.send('Music added in queue')


@slash.slash(
    name="night",
    description="Nightcore songs",
    guild_ids=allGuilds
)
async def nightcore(ctx: SlashContext):
    emb = discord.Embed(title="Музыка Nightcore", color=discord.Color.random())
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    emb.set_thumbnail(url='https://img.youtube.com/vi/KlNHoCcDAUE/hqdefault.jpg')
    emb = addEmbedField(emb, "Nightcore - FRIENDS", 'https://www.youtube.com/watch?v=Aba7gEvAfB4')
    emb = addEmbedField(emb, "Nightcore - Solo", 'https://www.youtube.com/watch?v=KlNHoCcDAUE')
    emb = addEmbedField(emb, "Nightcore - Bad Boy", 'https://www.youtube.com/watch?v=jVZxfy_awus')
    emb = addEmbedField(emb, "Nightcore - Discord", 'https://www.youtube.com/watch?v=UJnFD9Koy0Q')
    emb = addEmbedField(emb, "Nightcore - Teeth", 'https://www.youtube.com/watch?v=XPK2HP8bn68')
    await ctx.send(embed=emb)


@slash.slash(
    name="dconnect",
    description="Disconnect from voice chat",
    guild_ids=allGuilds
)
async def disconnect(ctx):
    global playingVoiceChat
    await ctx.voice_client.disconnect()
    await ctx.send('Bot disconnected from server')
    playingVoiceChat = False


@bot.command()
async def disconnect(ctx):
    global playingVoiceChat
    await ctx.voice_client.disconnect()
    await ctx.send('Bot disconnected from server')
    playingVoiceChat = False


'''send email'''


@slash.slash(
    name="mail",
    description="Send an email to user",
    guild_ids=allGuilds,
    options=[
        create_option(
            name="emailaddress",
            description="Email address",
            required=True,
            option_type=3
        ),
        create_option(
            name="topic",
            description="Write your topic",
            required=True,
            option_type=3
        ),
        create_option(
            name="subject",
            description="Write subject of email",
            required=True,
            option_type=3
        )
    ]
)
@bot.command()
async def _mailsmb(ctx, emailaddress: str, topic: str, subject: str):
    await ctx.send('Trying to send an email')
    fromaddr = "noreplytg@mail.ru"
    mypass = "gbZqyVS3bQj9tfZnXenQ"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = emailaddress
    msg['Subject'] = topic

    body = subject
    msg.attach(MIMEText(body, 'plain'))

    serverSMPT = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    serverSMPT.login(fromaddr, mypass)
    text = msg.as_string()
    serverSMPT.sendmail(fromaddr, emailaddress, text)
    serverSMPT.quit()


@bot.command()
async def tournament(ctx, *participants):
    emb = discord.Embed(title="Турнир по круговой системе", color=discord.Color.random())
    emb.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    for i in range(len(participants) - 1):
        emb = addEmbedField(emb, f"Тур {i + 1}", createPairs(list(participants), i))
    await ctx.send(embed=emb)


def createPairs(lst, tur):
    if len(lst) % 2 == 1:
        lst.append('bye')
    main_sym = lst[:1][0]
    lst = lst[1:]
    shift = tur
    lst = lst[-shift:] + lst[:-shift]
    lst.insert(0, main_sym)
    pairs = ""
    for i in range(len(lst) // 2):
        pairs += (str(lst[i]) + "-" + str(lst[len(lst) - i - 1])) + '\n\n'
    return pairs


def createQRFunction(data: str):
    filename = "qr.png"
    img = qrcode.make(data)
    img.save(filename)


@bot.command()
async def phisicsFormulas(ctx, *args):
    letter = args[0]
    if len(args) == 2:
        grade = args[1]
    if len(args) == 3:
        topic = args[2]

    base = sqlite3.connect("discord.db")
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS {}(letter, formula, photoID, description, topic, grade)'
                 .format('formularies'))
    base.commit()
    getFormula = cur.execute('SELECT formula FROM formularies WHERE letter == ?', letter).fetchall()
    getDescription = cur.execute('SELECT description FROM formularies WHERE letter == ?', letter).fetchall()
    getTopic = cur.execute('SELECT grade FROM formularies WHERE letter == ?', letter).fetchall()
    getGrade = cur.execute('SELECT topic FROM formularies WHERE letter == ?', letter).fetchall()

    await ctx.send(f"{getFormula}\n{getDescription}\n{getGrade}\n{getTopic}")


@bot.command()
async def createQR(ctx, *data):
    dataSTR = ''
    for i in range(len(data)):
        dataSTR += data[i] + " "
    createQRFunction(dataSTR)
    await ctx.send("Your QRcode", file=discord.File('qr.png'))


@bot.command()
async def say(ctx, *message):
    await ctx.channel.purge(limit=1)
    mess = ""
    for i in range(len(message)):
        mess += message[i] + " "
    await ctx.send(mess)


@bot.command()
async def XOR_NUM(ctx, number_1: int, number_2: int):
    await ctx.send(number_1 ^ number_2)


@bot.command()
async def XOR_STR(ctx, message_1, message_2):
    message = message_1
    crypto_key = message_2
    cipher = handmade_crypto.xor_fn(message, crypto_key)
    await ctx.send(f"Cipher text is: {cipher}")
    handmade_crypto.write_file("ciphertext.txt", cipher)
    data = handmade_crypto.read_file("ciphertext.txt")
    plain = handmade_crypto.xor_fn(data, crypto_key)
    await ctx.send(f"Decrypted text: {plain}")


@bot.command(pass_context=True)
async def nick(ctx, member: discord.Member, nickname):
    await member.edit(nick=nickname)
    await ctx.send(f"Ник {discord.member} изменен")


@bot.command()
async def unicode(ctx, text, num=False):
    if num:
        await ctx.send(chr(int(text)))
    else:
        await ctx.send(ord(text))


@bot.command()
async def createQuiz(ctx, message, *emojis):
    if len(emojis) == 0:
        await buttons.send(
            content=message,
            channel=ctx.channel.id,
            components=[
                ActionRow([
                    Button(
                        label="👍",
                        style=ButtonType().Primary,
                        custom_id="one_emoji"
                    ), Button(
                        label="👎",
                        style=ButtonType().Secondary,
                        custom_id="two_emoji"
                    )
                ])])
    else:
        print('works')
        print(emojis)
        await buttons.send(
            content=message,
            channel=ctx.channel.id,
            components=[
                ActionRow([
                    Button(
                        label=emojis[0],
                        style=ButtonType().Primary,
                        custom_id="one_emoji"
                    ), Button(
                        label=emojis[1],
                        style=ButtonType().Secondary,
                        custom_id="two_emoji"
                    )
                ])])


@buttons.click
async def one_emoji(ctx):
    await ctx.reply('Вы проголосовали успешно за первое эмоджи')


@buttons.click
async def two_emoji(ctx):
    await ctx.reply('Вы проголосовали успешно за второе эмоджи')


'mini games'


@buttons.click
async def firstVariation(ctx):
    await ctx.channel.purge(limit=1)
    if flagGame.returnRndArray()[0] == flagGame.returnRightAnswer():
        await ctx.reply("Answer is correct")
    else:
        await ctx.reply("Answer is incorrect")


@buttons.click
async def secondVariation(ctx):
    await ctx.channel.purge(limit=1)
    if flagGame.returnRndArray()[1] == flagGame.returnRightAnswer():
        await ctx.reply("Answer is correct")
    else:
        await ctx.reply("Answer is incorrect")


@buttons.click
async def thirdVariation(ctx):
    await ctx.channel.purge(limit=1)
    if flagGame.returnRndArray()[2] == flagGame.returnRightAnswer():
        await ctx.reply("Answer is correct")
    else:
        await ctx.reply("Answer is incorrect")


@buttons.click
async def forthVariation(ctx):
    await ctx.channel.purge(limit=1)
    if flagGame.returnRndArray()[3] == flagGame.returnRightAnswer():
        await ctx.reply("Answer is correct")
    else:
        await ctx.reply("Answer is incorrect")


@bot.command()
async def guessCountry(ctx):
    await ctx.message.delete()
    global flagGame
    flagGame = quizGames.flagQuizes()
    flagGame.flagToName()
    content = ""
    content += f"What's country is this flag {config.flags[flagGame.returnRightAnswer()]}!\n" \
               f"{config.nameOfEveryCountryFlag[flagGame.returnRndArray()[0]]}\n" \
               f"{config.nameOfEveryCountryFlag[flagGame.returnRndArray()[1]]}" \
               f"{config.nameOfEveryCountryFlag[flagGame.returnRndArray()[2]]}" \
               f"{config.nameOfEveryCountryFlag[flagGame.returnRndArray()[3]]}"
    await buttons.send(
        content=f"What's country is this flag {config.flags[flagGame.returnRightAnswer()]}!",
        channel=ctx.channel.id,
        components=[
            ActionRow([
                Button(
                    label=config.nameOfEveryCountryFlag[flagGame.returnRndArray()[0]],
                    style=ButtonType().Primary,
                    custom_id="firstVariation"
                ), Button(
                    label=config.nameOfEveryCountryFlag[flagGame.returnRndArray()[1]],
                    style=ButtonType().Secondary,
                    custom_id="secondVariation"
                )
            ]), ActionRow([
                Button(
                    label=config.nameOfEveryCountryFlag[flagGame.returnRndArray()[2]],
                    style=ButtonType().Success,
                    custom_id="thirdVariation"
                ), Button(
                    label=config.nameOfEveryCountryFlag[flagGame.returnRndArray()[3]],
                    style=ButtonType().Danger,
                    custom_id="forthVariation"
                )
            ])
        ]
    )


bot.add_cog(HelpCog(bot))
bot.add_cog(MusicCog(bot))
bot.add_cog(SchoolTimetableCog(bot))
bot.add_cog(UtilsCog(bot))
bot.run(config.token)
