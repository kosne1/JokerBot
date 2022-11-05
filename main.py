import discord
from discord.ext import commands

channel_id = 1038053124570624114
TOKEN = 'MTAzNzcxNDYzMTI1NjQ0MDg4Mg.G4RqBj.aLEs-nF1BOEcGT1ARrlM-oD9fUgD-YPErLjfJE'
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    await bot.get_channel(channel_id).send("bot is online")


@bot.event
async def on_message(message):
    try:
        match message.content:
            case '1':
                message_text = "Чем отличается мужская общага от женской? В женской посуду моют после еды, а в мужской - до"
            case '2':
                message_text = "Согласно правилам грузинского этикета, нож нужно держать в правой руке, а русню - в страхе"
            case '3':
                message_text = "Зачем идти к другу на похороны, если он к тебе не придет"
            case '4':
                message_text = "Как называют пожилых анорексичек? Легкие бабки"
            case '5':
                message_text = "Почему денежное дерево такое богатое? У него еврейские корни"
            case '6':
                message_text = "Что будет, если все темнокожие станут карликами? Уровень преступности снизится"
            case '7':
                message_text = "Как англичане называют бутылку виски с двумя горлышками? Двусторонний скотч"
            case '8':
                message_text = "Гроб карлика-пессимиста наполовину пуст."
            case '9':
                message_text = "По заверению сыгравших русская рулетка на 100% безопасна."
            case "10":
                message_text = "Штирлиц бил наверняка. Наверняк сражался как мог. Мог был смелым парнем."
            case _:
                return 0
        await bot.get_channel(message.channel.id).send(message_text)
    except Exception as _ex:
        print(f"ERROR")

bot.run(TOKEN)
