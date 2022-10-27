token = 'MTAxNzUxNTE4NjgwODE2MDQyNw.Gd4hep.QW-usTcqAxRPsYZbsbkRBgxdVT12Vv6JL12K7M'
YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True',
               'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

flags = ["🇦🇫", "🇦🇽", "🇦🇱", "🇩🇿", "🇦🇸", "🇦🇩", "🇦🇴", "🇦🇮", "🇦🇶", "🇦🇬", "🇦🇷", "🇦🇲", "🇦🇼", "🇦🇺",
         "🇦🇹", "🇦🇿", "🇧🇸", "🇧🇭", "🇧🇩", "🇧🇧", "🇧🇾",
         "🇧🇪", "🇧🇿", "🇧🇲", "🇧🇹", "🇧🇴", "🇧🇦", "🇧🇼", "🇧🇷", "🇮🇴", "🇻🇬", "🇧🇳", "🇧🇬", "🇧🇫", "🇧🇮",
         "🇰🇭", "🇨🇲", "🇨🇦", "🇮🇨",
         "🇨🇻", "🇧🇶", "🇰🇾", "🇨🇫", "🇹🇩", "🇨🇱", "🇨🇳", "🇨🇽", "🇨🇨", "🇨🇴", "🇰🇲", "🇨🇬", "🇨🇩", "🇨🇰",
         "🇨🇷", "🇨🇮", "🇭🇷", "🇨🇺", "🇨🇼", "🇨🇾",
         "🇨🇿", "🇩🇰", "🇩🇯", "🇩🇲", "🇩🇴", "🇪🇨", "🇪🇬", "🇸🇻", "🇬🇶", "🇪🇷", "🇪🇪", "🇪🇹", "🇪🇺", "🇫🇰",
         "🇫🇴", "🇫🇯", "🇫🇮", "🇫🇷", "🇬🇫", "🇵🇫", "🇹🇫",
         "🇬🇦", "🇬🇲", "🇬🇪", "🇩🇪", "🇬🇭", "🇬🇮", "🇬🇷", "🇬🇱", "🇬🇩", "🇬🇵", "🇬🇺", "🇬🇹", "🇬🇬", "🇬🇳",
         "🇬🇼", "🇬🇾", "🇭🇹", "🇭🇳", "🇭🇰", "🇭🇺", "🇮🇸", "🇮🇳",
         "🇮🇩", "🇮🇷", "🇮🇶", "🇮🇪", "🇮🇲", "🇮🇱", "🇮🇹", "🇯🇲", "🇯🇵", "🇯🇪", "🇯🇴", "🇰🇿", "🇰🇪", "🇰🇮",
         "🇽🇰", "🇰🇼", "🇰🇬", "🇱🇦", "🇱🇻", "🇱🇧", "🇱🇸", "🇱🇷", "🇱🇾", "🇱🇮",
         "🇱🇹", "🇱🇺", "🇲🇴", "🇲🇰", "🇲🇬", "🇲🇼", "🇲🇾", "🇲🇻", "🇲🇱", "🇲🇹", "🇲🇭", "🇲🇶", "🇲🇷", "🇲🇺",
         "🇾🇹", "🇲🇽", "🇫🇲", "🇲🇩", "🇲🇨", "🇲🇳", "🇲🇪",
         "🇲🇸", "🇲🇦", "🇲🇿", "🇲🇲", "🇳🇦", "🇳🇷", "🇳🇵", "🇳🇱", "🇳🇨", "🇳🇿", "🇳🇮", "🇳🇪", "🇳🇬", "🇳🇺",
         "🇳🇫", "🇰🇵", "🇲🇵", "🇳🇴", "🇴🇲", "🇵🇰", "🇵🇼", "🇵🇸",
         "🇵🇦", "🇵🇬", "🇵🇾", "🇵🇪", "🇵🇭", "🇵🇳", "🇵🇱", "🇵🇹", "🇵🇷", "🇶🇦", "🇷🇪", "🇷🇴",
         "🇷🇺", "🇷🇼", "🇼🇸", "🇸🇲", "🇸🇹", "🇸🇦", "🇸🇳", "🇷🇸", "🇸🇨",
         "🇸🇱", "🇸🇬", "🇸🇽", "🇸🇰", "🇸🇮", "🇬🇸", "🇸🇧", "🇸🇴", "🇿🇦", "🇰🇷", "🇸🇸", "🇪🇸", "🇱🇰", "🇧🇱",
         "🇸🇭", "🇰🇳", "🇱🇨", "🇵🇲", "🇻🇨", "🇸🇩", "🇸🇷", "🇸🇿", "🇸🇪", "🇨🇭",
         "🇸🇾", "🇹🇼", "🇹🇯", "🇹🇿", "🇹🇭", "🇹🇱", "🇹🇬", "🇹🇴", "🇹🇹", "🇹🇳", "🇹🇷", "🇹🇲", "🇹🇨", "🇹🇻",
         "🇻🇮", "🇺🇬", "🇺🇦", "🇦🇪", "🇬🇧", "🇺🇸", "🇺🇳", "🇺🇾", "🇺🇿",
         "🇻🇺", "🇻🇦", "🇻🇪", "🇻🇳", "🇼🇫", "🇪🇭", "🇾🇪", "🇿🇲", "🇿🇼"]

nameOfEveryCountryFlag = ["Афганистан", "Аландские острова", "Албания", "Алжир", "Американское Самоа",
                          "Андорра", "Ангола", "Ангилья", "Антарктика",
                          "Антигуа и Барбуда", "Аргентина",
                          "Армения", "Аруба", "Австралия",
                          "Австрия", "Азербайджан", "Багамские Острова", "Бахрейн", "Бангладеш", "Барбадос", "Беларусь",
                          "Бельгия", "Белиз", "Бермуды", "Бутан", "Боливия", "Босния и Герцеговина",
                          "Ботсвана", "Бразилия",
                          "Британская территория в Индийском океане", "Виргинские Острова (Великобритания)", "Бруней",
                          "Болгария", "Буркина-Фасо", "Бурунди",
                          "Камбоджа", "Камерун", "Канада", "🇮🇨",
                          "Кабо-Верде", "Бонайре, Синт-Эстатиус и Саба", "Острова Кайман", "ЦАР", "Чад",
                          "Чили", "Китай", "Остров Рождества", "Кокосовые острова", "Колумбия", "Коморы",
                          "Республика Конго", "ДР Конго", "Острова Кука",
                          "Коста-Рика", "Кот-д’Ивуар", "Хорватия", "Куба", "Кюрасао", "Кипр",
                          "Чехия", "Дания", "Джибути", "Доминика", "Доминиканская Республика",
                          "Эквадор", "Египет", "Сальвадор", "Экваториальная Гвинея",
                          "Эритрея", "Эстония",
                          "Эфиопия", "Европейский союз", "Фолклендские острова",
                          "Фарерские острова", "Фиджи", "Финляндия", "Франция", "Гвиана", "Французская Полинезия",
                          "Французские Южные и Антарктические территории",
                          "Габон", "Гамбия", "Грузия", "Германия", "Гана", "Гибралтар", "Греция", "Гренландия",
                          "Гренада", "Гваделупа", "Гуам",
                          "Гватемала", "Гернси", "Гвинея",
                          "Гвинея-Бисау", "Гайана", "Гаити", "Гондурас", "Гонконг", "Венгрия", "Исландия", "Индия",
                          "Индонезия", "Иран", "Ирак", "Ирландия", "Остров Мэн", "Израиль", "Италия",
                          "Ямайка", "Япония", "Джерси", "Иордания",
                          "Казахстан", "Кения", "Кирибати",
                          "Косово", "Кувейт", "Киргизия", "Лаос", "Латвия", "Ливан",
                          "Лесото", "Либерия", "Ливия", "Лихтенштейн",
                          "Литва", "Люксембург", "Макао", "Северная Македония", "Мадагаскар",
                          "Малави", "Малайзия", "Мальдивы", "Мали", "Мальта", "Маршалловы Острова",
                          "Мартиника", "Мавритания", "Маврикий",
                          "Майотта", "Мексика", "Микронезия", "Молдавия", "Монако", "Монголия", "Черногория",
                          "Монтсеррат", "Марокко", "Мозамбик", "Мьянма", "Намибия",
                          "Науру", "Непал", "Нидерланды", "Новая Каледония", "Новая Зеландия", "Никарагуа",
                          "Нигер", "Нигерия", "Ниуэ",
                          "Остров Норфолк", "КНДР (Корейская Народно-Демократическая Республика)",
                          "Северные Марианские Острова", "Норвегия",
                          "Оман", "Пакистан", "Палау", "Государство Палестина",
                          "Панама", "Папуа — Новая Гвинея", "Парагвай", "Перу", "Филиппины",
                          "Острова Питкэрн", "Польша", "Португалия", "Пуэрто-Рико",
                          "Катар", "Реюньон", "Румыния",
                          "Россия", "Руанда", "Самоа", "Сан-Марино",
                          "Сан-Томе и Принсипи", "Саудовская Аравия", "Сенегал", "Сербия", "Сейшельские Острова",
                          "Сьерра-Леоне", "Сингапур", "Синт-Мартен", "Словакия", "Словения",
                          "Южная Георгия и Южные Сандвичевы Острова",
                          "Соломоновы Острова", "Сомали", "ЮАР", "Республика Корея", "Южный Судан",
                          "Испания", "Шри-Ланка", "Сен-Бартелеми",
                          "Острова Святой Елены, Вознесения и Тристан-да-Кунья",
                          "Сент-Китс и Невис", "Сент-Люсия", "Сен-Пьер и Микелон", "Сент-Винсент и Гренадины",
                          "Судан", "Суринам", "Эсватини", "Швеция", "Швейцария",
                          "Сирия", "Китайская Республика", "Таджикистан", "Танзания", "Таиланд",
                          "Восточный Тимор", "Того", "Тонга", "Тринидад и Тобаго", "Тунис", "Турция",
                          "Туркмения", "Теркс и Кайкос", "Тувалу",
                          "Виргинские Острова", "Уганда", "Украина",
                          "ОАЭ", "Великобритания", "США", "🇺🇳", "Уругвай", "Узбекистан",
                          "Вануату", "Ватикан", "Венесуэла", "Вьетнам",
                          "🇼🇫", "САДР", "Йемен", "Замбия", "Зимбабве"]

'''@slash.slash(
    name="messageme",
    description="Just sends a message",
    guild_ids=[1017363542397157406]
)
async def _messageme(ctx: SlashContext):
    await ctx.author.send("Hello World!")


@slash.slash(
    name="helloinchat",
    description="Just sends a message",
    guild_ids=[1017363542397157406],
    options=[
        create_option(
            name="option",
            description="Choose your word",
            required=True,
            option_type=3,
            choices=[
                create_choice(
                    name="World",
                    value="world"
                ),
                create_choice(
                    name="You!",
                    value="you"
                )
            ]
        )
    ]
)
async def _message(ctx: SlashContext, option: str):
    await ctx.send(option)


@slash.slash(
    name="getuser",
    description="Get user",
    guild_ids=[1017363542397157406],
    options=[
        create_option(
            name="user",
            description="Select a user",
            required=True,
            option_type=6
        )
    ]
)
async def _getuser(ctx: SlashContext, user: str):
    await ctx.send(str(user))


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None, amount=1):
    await ctx.channel.purge(limit=int(amount))
    await member.kick(reason=reason)
    await ctx.send(f"Kicked user {member.mention}")


@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None, amount=1):
    await ctx.channel.purge(limit=int(amount))
    await member.ban(reason=reason)
    await ctx.send(f"Banned user {member.mention}")


@bot.command()
async def unban(ctx, member: discord.Member, *, reason=None, amount=1):
    await ctx.channel.purge(limit=int(amount))
    await member.unban(reason=reason)
    await ctx.send(f"Unbanned user {member.mention}")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            embed=discord.Embed(description=f'** {ctx.author.name}, данной команды не существует.**', color=0x0c0c0c))
@slash.slash(
    name="dconnect",
    description="Disconnect from voice chat",
    guild_ids=allGuilds
)
@bot.command()
async def disconnect(ctx):
    global playingVoiceChat
    await ctx.voice_client.disconnect()
    await ctx.send('Bot disconnected from server')
    playingVoiceChat = False
    

'''
