import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
import config
import functions as func

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.event
async def on_ready():
    DiscordComponents(bot)
    print("Started")


@bot.command()
async def make_button(ctx):
    embed = discord.Embed(title="Присоединяйся к нам",
                          colour=0x87CEEB)
    embed.add_field(name="Описание", value="Привет.Этот бот поможет тебе связаться с руководством этого сервера если "
                                           "ты хочешь быть частью этой команды.", inline=False)
    embed.add_field(name="Инструкции", value="Все очень просто. Ты нажимаешь на кнопку и в отдельной категории "
                                             "создается твой чат с руководством. \n "
                                             "Пока ты будешь ждать собеседования с руководством ты увидешь кнопку "
                                             "заполнить анкету кандидата. \n "
                                             "Нажми на нее и заполни все поля о себе."
                                             "Как только ты закончишь собеседование нажми на кнопку 'закрыть' если "
                                             "уверен, что у тебя не осталось вопросов.", inline=False)
    embed.add_field(name="Готов?", value="Ну что, готов присоединиться", inline=False)
    embed.set_footer(text="При первом нажатии кнопки могут не сработать.Если это произойдет,то попробуйте еще раз.")
    await ctx.send(
        embed=embed,
        components=[
            Button(style=ButtonStyle.blue, label="Создать чат")
        ]
    )


@bot.event
async def on_button_click(ctx):
    guild = ctx.guild
    responce = await bot.wait_for("button_click")
    if responce.channel == ctx.channel:

        if responce.component.label == "закрыть чат":
            if ctx.channel.id != config.main_channel:  # not equal main channel
                author = ctx.author
                channel = ctx.channel
                category_archive = guild.get_channel(config.archive)

                await channel.set_permissions(author, read_messages=False, send_messages=False)
                await responce.send("Вы закрыли канал. Спасибо за участие")
                await channel.edit(category=category_archive)

                print(f"Канал {channel} с участником {author} закрыт")

        if responce.component.label == "заполнить анкету кандидата":
            await responce.send(embed=config.anketa)

        if responce.component.label == "Создать чат":
            author = responce.author

            cat = discord.utils.get(ctx.guild.categories, name=str("кандидаты"))

            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            }
            name = func.getName(str(author))  # Function formats name in to "name-codification"
            text_channel = await guild.create_text_channel(name=name, category=cat,
                                                           overwrites=overwrites)
            channel = bot.get_channel(text_channel.id)
            await channel.send(f"<@{author.id}>, это твой чат с руководством и с <@!{config.admin_id}>",
                               components=[
                                   Button(style=ButtonStyle.red, label="закрыть чат"),
                                   Button(style=ButtonStyle.green, label="заполнить анкету кандидата")
                               ]
                               )

            print(
                f"Канал {text_channel} с id:{text_channel.id} для участника {author} с id:{str(config.admin_id)} создан")


# except:
#     print(f"Канал не создан. Произошла ошибка ")


bot.run(config.TOKEN)
