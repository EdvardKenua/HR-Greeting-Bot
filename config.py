import discord
TOKEN = "Put yout token"

admin_id = 378570863152463875
archive = 896132845842620507
main_channel = #

anketa = discord.Embed(title="Анкета", colour=0xf1c40f)
anketa.add_field(name="1 вопрос:", value="Как тебя зовут?", inline=False)
anketa.add_field(name="2 вопрос:", value="Сколько тебе лет? (необяз.)", inline=False)
anketa.add_field(name="3 вопрос", value="Занимался/лась ли ты раньше мангой?", inline=False)
anketa.add_field(name="4 вопрос", value="Если да, то как давно и в какой команде? (необяз.)", inline=False)
anketa.add_field(name="5 вопрос", value="Какие нравятся жанры?", inline=False)
anketa.add_field(name="6 вопрос", value="Сколько готов/а уделять времени работе с мангой?", inline=False)
anketa.add_field(name="7 вопрос", value="Надолго ли ты к нам или просто потренироваться?", inline=False)
anketa.add_field(name="8 вопрос", value=" Если ты пришёл к нам в качестве ретушёра/клинера, то есть ли граф. планшет?", inline=False)
anketa.set_footer(text="Пожалуйста, отвечай на вопрос с указание цифры")
