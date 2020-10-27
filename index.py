import discord
import time
import asyncio
from random import choice
from discord.ext import commands
from config import settings

 
nastea = commands.Bot(command_prefix = settings['prefix'])

@nastea.event
async def on_ready():
    print("eval)")

@nastea.event
async def on_command_error(msg, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Ошибка", color=0xff4500, description="Вы не имеете необходимых разрешений для выполнения этой команды.")
        embed.set_footer(text="Nasty.py. 2020.", icon_url='https://cdn.discordapp.com/avatars/721434688337477632/8fc51ec9395086d149c70cd3a1008d29.png')
        await msg.channel.send(embed=embed)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Ошибка", color=0xff4500, description="Вы предоставили не все необходимые аргументы для выполнения этой команды.")
        embed.set_footer(text="Nasty.py. 2020.", icon_url='https://cdn.discordapp.com/avatars/721434688337477632/8fc51ec9395086d149c70cd3a1008d29.png')
        await msg.channel.send(embed=embed)

@nastea.command()
async def hello(msg):
    author = msg.message.author
    await msg.send(f'привет {author.mention} пошли гулять!!!')

@nastea.command()
async def say(msg, sayphr):
    channel = msg.channel
    if msg.message.author.name == "prizmech" or "ncrvfan2005":
        await channel.send(sayphr)
        await msg.message.delete()
    else:
        await channel.send("вы не имеете права вы малолетка !!!")

@nastea.command()
async def ping(msg):
    peng = round(nastea.latency*1000)
    embed = discord.Embed(title="Задержка (в мс)", color=0xff4500)
    embed.add_field(name="Клиент - сервер",value=peng, inline=False)
    embed.set_footer(text="Nasty.py. 2020.", icon_url='https://cdn.discordapp.com/avatars/721434688337477632/8fc51ec9395086d149c70cd3a1008d29.png')
    await msg.channel.send(embed=embed)

@nastea.command()
async def shutdown(msg):
    await msg.channel.send("всем пака !!!")
    await nastea.close()

@nastea.command()
async def randnitro(msg):
    sub = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
    main = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
    num = ['1','2','3','4','5','6','7','8','9']
    randisc = []
    while len(randisc) < 24:
        rands = choice(sub)
        randm = choice(main)
        randn = choice(num)
        randisc1 = [rands, randm, randn]
        randisc += choice(randisc1)
    randistr = "https://discord.com/gifts/"+''.join(str(e) for e in randisc)
    await msg.channel.send(randistr)

@nastea.command()
async def invite(msg):
    embed = discord.Embed(title="Ссылки", color=0xff4500)
    embed.add_field(name="Приглашение бота на сервер", value='[Ссылка](https://discord.com/api/oauth2/authorize?client_id=721434688337477632&permissions=1081601094&scope=bot)', inline=False)
    embed.add_field(name="Дебаг-сервер бота", value="[Ссылка](https://discord.gg/pjrtRpc)", inline=False)
    embed.set_footer(text="Nasty.py. 2020.", icon_url='https://cdn.discordapp.com/avatars/721434688337477632/8fc51ec9395086d149c70cd3a1008d29.png')
    await msg.channel.send(embed=embed)

@nastea.command()
@commands.has_permissions(ban_members = True)
async def ban(msg, member:discord.User=None, why=None):
    if member == None or member == msg.message.author:
        messega = discord.Embed(title="Ошибка", color=0xff4500, description=f"Самодепортация из сервера не допускается.")
        messega.set_footer(text="Nasty.py. 2020.", icon_url='https://cdn.discordapp.com/avatars/721434688337477632/8fc51ec9395086d149c70cd3a1008d29.png')
        await msg.channel.send(embed=messega)
    else:
        if why == None:
            why = "уебанство!!!"
        messega = discord.Embed(title="Сообщение", color=0xff4500, description=f"ты вые**бан** из интеллигентного клуба имени {msg.guild.name} за {why}!! и больше туда не возвращайся !!!")
        messega.set_footer(text="Nasty.py. 2020.", icon_url='https://cdn.discordapp.com/avatars/721434688337477632/8fc51ec9395086d149c70cd3a1008d29.png')
        await member.send(embed=messega)
        await msg.guild.ban(member, reason=why)
        print(f"{member} выебан отсюда !!!")

@nastea.command()
@commands.has_permissions(kick_members = True)
async def kick(msg, member:discord.User=None, why=None):
    if member == None or member == msg.message.author:
        messega = discord.Embed(title="Ошибка", color=0xff4500, description=f"Самоизгнание из сервера не допускается.")
        messega.set_footer(text="Nasty.py. 2020.", icon_url='https://cdn.discordapp.com/avatars/721434688337477632/8fc51ec9395086d149c70cd3a1008d29.png')
        await msg.channel.send(embed=messega)
    else:
        if why == None:
            why = "уебанство!!!"
        messega = discord.Embed(title="Сообщение", color=0xff4500, description=f"ты изгнан из интеллигентного клуба имени {msg.guild.name} за {why}")
        messega.set_footer(text="Nasty.py. 2020.", icon_url='https://cdn.discordapp.com/avatars/721434688337477632/8fc51ec9395086d149c70cd3a1008d29.png')
        await member.send(embed=messega)
        await msg.guild.kick(member, reason=why)
        print(f"{member} выпизжен отсюда !!!")

@nastea.command()
@commands.has_permissions(ban_members=True)
async def unban(msg, member:discord.User=None):
    if member == None or member == msg.message.author:
       messega = discord.Embed(title="Ошибка", color=0xff4500, description=f"Вы и так не забанены!")
       messega.set_footer(text="Nasty.py. 2020.", icon_url='https://cdn.discordapp.com/avatars/721434688337477632/8fc51ec9395086d149c70cd3a1008d29.png')
       await msg.channel.send(embed=messega)
    else:
        await msg.guild.unban(member)
        messega = discord.Embed(title="Успех", color=0xff4500, description=f"Пользователь {member} разбанен и имеет возможность присоединиться к серверу заново!")
        messega.set_footer(text="Nasty.py. 2020.", icon_url='https://cdn.discordapp.com/avatars/721434688337477632/8fc51ec9395086d149c70cd3a1008d29.png')
        print("хатова !!!")
        await msg.channel.send(embed=messega)
        messega = discord.Embed(title="Сообщение", color=0xff4500, description=f"я успокоился можешь возвращаться")
        messega.set_footer(text="Nasty.py. 2020.", icon_url='https://cdn.discordapp.com/avatars/721434688337477632/8fc51ec9395086d149c70cd3a1008d29.png')
        await member.send(embed=messega)

@nastea.command()
async def avatar(msg, user: discord.Member = None):
    memberb = user or msg.author
    link = memberb.avatar_url_as(size=2048, format='png')
    messega = discord.Embed(title=f"Аватар пользователя **{memberb.name}**", color=0xff4500)
    messega.set_image(url=link)
    messega.set_footer(text="Nasty.py. 2020.", icon_url='https://cdn.discordapp.com/avatars/721434688337477632/8fc51ec9395086d149c70cd3a1008d29.png')
    await msg.channel.send(embed=messega)

nastea.run(settings['token'])