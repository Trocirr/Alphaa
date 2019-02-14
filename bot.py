import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
import requests

from datetime import datetime, timezone



Client = discord.Client()
client = commands.Bot(command_prefix = "-")
client.remove_command('help')



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
	
@client.event
async def on_command_error(error, ctx):
	if isinstance(error, commands.CommandOnCooldown):
		await client.send_message(ctx.message.channel, content='Calm down! You have to wait %.2f seconds before using new command :clock1:' % error.retry_after)
	raise error		
	
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='-help'))
	

	
@client.command(pass_context=True)
async def time(ctx):
	utc_dt = datetime.now(timezone.utc)
	p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
	utc = str(p)
	embed = discord.Embed(description="", color=0xFF0000)
	embed.add_field(name=":stopwatch: **Current Local Time and Date in the United Kingdom**", value=utc)
	await client.say(embed=embed)	

@client.command(pass_context=True)
async def summon(ctx):
	channel = ctx.message.author.voice.voice_channel
	await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
	await vc.disconnect()

@client.command(pass_context = True)
async def mutee(ctx, member: discord.Member, message: str):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '399567243744116738':
          role = discord.utils.get(member.server.roles, name='Muted')
          await client.add_roles(member, role)
          embed=discord.Embed(title="User Muted!", description=("**{0}** was muted by **{1}** : " + message).format(member, ctx.message.author), color=0xff00f6)
          await client.say(embed=embed)
     else:
          embed=discord.Embed(title="Permission Denied.", description=":alphaError: You do not have permissions to use this command.", color=0xff00f6)
          await client.say(embed=embed)


@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '399567243744116738':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="<:alphaError:468832634542227477> You do not have permissions to use this command.", color=0xff00f6)
        await client.say(embed=embed)


@client.command(pass_context=True)
async def randomnumber(ctx):
	await client.say(random.randint(1,101))	

@client.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def kick(ctx, userName: discord.User):
	await client.kick(userName)
	embed=discord.Embed(title="User Kicked!", description="<a:Success:468812983074553876> **{0}** has been kicked by **{1}**!".format(userName, ctx.message.author),  color=0xff00f6)
	await client.say(embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, userName: discord.User):
    await client.ban(userName)
    embed=discord.Embed(title="User Banned!", description="<a:Success:468812983074553876> **{0}** has been banned by **{1}**!".format(userName, ctx.message.author),  color=0xff00f6)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def purge(ctx, *, amount : int):
    id_list = ['399567243744116738']
    if ctx.message.author.id in id_list:
         channel = ctx.message.channel
         messages = []
         async for message in client.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
         await client.delete_messages(messages)
    else:
        await client.say("<:alphaError:468832634542227477> You do not have permissions to use this command.")
	 
@client.command(pass_context=True)
async def dmm(ctx, member: discord.Member, message: str):
    await client.send_message(member, message)	
	
@client.command(pass_context=True)
async def idk2(ctx):
	embed = discord.Embed(title="Welcome to Bonk.io Football League Discord Server!", description="BFL is launched in November of 2017. This is the official discord server of BFL. You can talk about anything here as long as it isn't disrespectful.", color=0xFF8C00)
	await client.say(embed=embed)	
	

@client.command(pass_context=True)
async def exdee(ctx):
    embed = discord.Embed(description="", color=0xC9C9C9)
    embed.add_field(name="Rules", value="You can talk about anything here as long as it isn't disrespectful. If you have a problem with anyone or anything in this server, please DM the Admins about it. \n \n 1. Rudeness, harassment, and immaturity will not be tolerated. \n 2. Porn and otherwise NSFW/NSFL content is prohibited. \n 3. No discussion about highly illegal activity. \n 4. Copyrighted and other unlawful material is prohibited, such as links to illegal content. \n 5. Advertising and promoting is prohibited. Don't even bother posting invite links because the bots will delete them anyway. \n 6. <#535451148090474497> is our main channel. Keep it clean. \n 7. No (random) links in the general chat <#535451148090474497> unless a moderator or higher lets you!")
    await client.say(embed=embed)
		
@client.command(pass_context=True)
async def div1(ctx):
    embed = discord.Embed(description="", color=0xFF8C00)
    embed.add_field(name="__1st Division__", value="1. Alex28102 :flag_ca: \n 2. Acquah :flag_it: \n 3. Dadem :flag_dz: \n 4. Frozenkiller :flag_nl: \n 5. aalaaprocks :flag_ie: \n 6. Shyrix :flag_fr: \n 7. Trocir :flag_rs:")
    await client.say(embed=embed)
	
@client.command(pass_context=True)
async def div3(ctx):
    embed = discord.Embed(description="", color=0xFF8C00)
    embed.add_field(name="__2nd Division__", value="1. Deus_ :flag_us: \n 2. Empirezz :flag_al: \n 3. King181 :flag_us: \n 4. Lxior :flag_us: \n 5. Shaun_ :flag_gb: \n 6. Tuccio :flag_us: \n 7. Warzen Rez :flag_us:")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def idk(ctx):
    embed = discord.Embed(description="", color=0xC9C9C9)
    embed.add_field(name="Roles", value="<@&535449445530075137> - Admins of the league \n <@&535498153378709504> - Referees. Ping them if u need one \n <@&535449391356575762> - The Staff Team \n <@&535449623947378708> Moderators \n <@&535449594491043841> - Bot Creator \n <@&535449576258273302> - Our Official Bot \n <@&535449518007648276> - Special people \n <@&535449546055090177> - League Players \n <@&535449658861027328> - Default role for everyone \n <@&535449699897835520> Role for our bots")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True, description='Shows the server info.')
async def server(ctx):
    embed = discord.Embed(description="<:Members:468729005273776128> Here's what I could find:", color=0x00ff00)
    embed.add_field(name="Name", value=ctx.message.server.name)
    embed.add_field(name="Owner", value=ctx.message.server.owner)
    embed.add_field(name="Region", value=ctx.message.server.region)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles))
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name="Channels", value=len(ctx.message.server.channels))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    utc_dt = datetime.now(timezone.utc)
    p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
    utc = str(p)    
    a=ctx.message.author
    txt= str(a) + " | " + str(utc)
    embed.set_footer(text=txt, icon_url=ctx.message.author.avatar_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def test123(ctx):
	msg = await client.say("no")
	await client.edit_message(msg, "hi")

@client.command(pass_context=True, description='Shows the server info.')
async def link(ctx):
    embed = discord.Embed(description="[disc](https://discordapp.com)", color=0x00ff00)
    await client.say(embed=embed)

@client.command(pass_context=True, description='Shows the server info.')
async def trocir(ctx):
    embed = discord.Embed(description="__**Trocir's stats :flag_rs:**__", color=0x00ff00)
    embed.add_field(name="Team", value="-")
    embed.add_field(name="Goals", value="-")
    embed.add_field(name="Assists", value="-")
    embed.add_field(name="Matches played", value="-")
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/532692198114721822.png?v=1')
    await client.say(embed=embed)


@client.command(pass_context=True, description='Shows the server info.')
async def nub1(ctx):
    embed = discord.Embed(description="__**Nub1's stats :flag_lb:**__", color=0x00ff00)
    embed.add_field(name="Team", value="Requiem")
    embed.add_field(name="Goals", value="4")
    embed.add_field(name="Matches played", value="1")
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/536202285131235358.png?v=1')
    await client.say(embed=embed)

@client.command(pass_context=True, description='Shows the server info.')
async def lyhnx(ctx):
    embed = discord.Embed(description="__**Lyhnx's stats :flag_gb:**__", color=0x00ff00)
    embed.add_field(name="Team", value="Requiem")
    embed.add_field(name="Goals", value="3")
    embed.add_field(name="Matches played", value="1")
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/536202285131235358.png?v=1')
    await client.say(embed=embed)

@client.command(pass_context=True, description='Shows the server info.')
async def llj(ctx):
    embed = discord.Embed(description="__**LLJ's stats :flag_gb:**__", color=0x00ff00)
    embed.add_field(name="Team", value="Violets")
    embed.add_field(name="Goals", value="3")
    embed.add_field(name="Matches played", value="1")
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/536239388720627715.png?v=1')
    await client.say(embed=embed)


@client.command(pass_context=True, description='Shows the server info.')
async def acquah(ctx):
    embed = discord.Embed(description="__**Acquah's stats :flag_it:**__", color=0x00ff00)
    embed.add_field(name="Team", value="Atletico Zero")
    embed.add_field(name="Goals", value="3")
    embed.add_field(name="Matches played", value="1")
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/532692198114721822.png?v=1')
    await client.say(embed=embed)

@client.command(pass_context=True, description='Shows the server info.')
async def nub0(ctx):
    embed = discord.Embed(description="__**Nub 0's stats :flag_dz:**__", color=0x00ff00)
    embed.add_field(name="Team", value="Legends")
    embed.add_field(name="Goals", value="1")
    embed.add_field(name="Matches played", value="1")
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/534051996303622145.png?v=1')
    await client.say(embed=embed)

@client.command(pass_context=True, description='Shows the server info.')
async def aalaaprocks(ctx):
    embed = discord.Embed(description="__**aalaaprocks's stats :flag_ie:**__", color=0x00ff00)
    embed.add_field(name="Team", value="Blaugrana")
    embed.add_field(name="Goals", value="14")
    embed.add_field(name="Matches played", value="2")
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/534048933631229962.png?v=1')
    await client.say(embed=embed)


@client.command(pass_context=True, description='Shows the server info.')
async def atleticozero(ctx):
    embed = discord.Embed(description="__**Atletico Zero**__", color=0x00ff00)
    embed.add_field(name="Captain", value="Acquah")
    embed.add_field(name="Trophies", value="0")
    embed.add_field(name="Wins", value="0")
    embed.add_field(name="Loss", value="1")
    embed.add_field(name="Draws", value="0")
    embed.add_field(name="Matches played", value="1")
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/532692198114721822.png?v=1')
    await client.say(embed=embed)
	
@client.command(pass_context=True, description='Shows the server info.')
async def blaugrana(ctx):
    embed = discord.Embed(description="__**Blaugrana**__", color=0x00ff00)
    embed.add_field(name="Captain", value="aalaaprocks")
    embed.add_field(name="Trophies", value="1")
    embed.add_field(name="Wins", value="2")
    embed.add_field(name="Loss", value="0")
    embed.add_field(name="Draws", value="0")
    embed.add_field(name="Matches played", value="2")
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/534048933631229962.png?v=1')
    await client.say(embed=embed)

@client.command(pass_context=True, description='Shows the server info.')
async def legends(ctx):
    embed = discord.Embed(description="__**Legends**__", color=0x00ff00)
    embed.add_field(name="Captain", value="Nub 0")
    embed.add_field(name="Trophies", value="0")
    embed.add_field(name="Wins", value="0")
    embed.add_field(name="Loss", value="1")
    embed.add_field(name="Draws", value="0")
    embed.add_field(name="Matches played", value="1")
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/534051996303622145.png?v=1')
    await client.say(embed=embed)

@client.command(pass_context=True, description='Shows the server info.')
async def violets(ctx):
    embed = discord.Embed(description="__**Violets**__", color=0x00ff00)
    embed.add_field(name="Captain", value="LLJ")
    embed.add_field(name="Trophies", value="0")
    embed.add_field(name="Wins", value="0")
    embed.add_field(name="Loss", value="1")
    embed.add_field(name="Draws", value="0")
    embed.add_field(name="Matches played", value="1")
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/536239388720627715.png?v=1')
    await client.say(embed=embed)	

@client.command(pass_context=True, description='Shows the server info.')
async def requiem(ctx):
    embed = discord.Embed(description="__**Requiem**__", color=0x00ff00)
    embed.add_field(name="Captain", value="Lyhnx")
    embed.add_field(name="Trophies", value="1")
    embed.add_field(name="Wins", value="1")
    embed.add_field(name="Loss", value="0")
    embed.add_field(name="Draws", value="0")
    embed.add_field(name="Matches played", value="1")
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/536202285131235358.png?v=1')
    await client.say(embed=embed)


@client.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find:", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Top Role", value=user.top_role.mention)
    embed.add_field(name="Joined at",value=user.joined_at)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.set_thumbnail(url = user.avatar_url)
    utc_dt = datetime.now(timezone.utc)
    p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
    utc = str(p)    
    a=ctx.message.author
    txt= str(a) + " | " + str(utc)
    embed.set_footer(text=txt, icon_url=ctx.message.author.avatar_url)    
    await client.say(embed=embed)
	
	
@client.command(pass_context=True)
async def about(ctx):
    embed = discord.Embed(title="__About BFL__", description="© 2019 BFL Bot All Rights Reserved", color=0x00ff00)
    embed.add_field(name="Original Creators", value="Trocir#9999 & Mes#0010")
    embed.add_field(name="Server count", value=str(len(client.servers)))
    embed.add_field(name="User count", value=str(len(list(client.get_all_members()))))
    embed.add_field(name="Channel count",value=str(len(list(client.get_all_channels()))))
    embed.add_field(name="API", value="Python")
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/534665657107611663/535158629230313482/BFL.PNG?width=158&height=176')
    utc_dt = datetime.now(timezone.utc)
    p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
    utc = str(p)    
    a=ctx.message.author
    txt= str(a) + " | " + str(utc)
    embed.set_footer(text=txt, icon_url=ctx.message.author.avatar_url) 
    await client.say(embed=embed)
	

	
@client.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s avatar".format(user.name), color=0x00BFFF)
    embed.set_image(url = user.avatar_url)
    utc_dt = datetime.now(timezone.utc)
    p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
    utc = str(p)    
    a=ctx.message.author
    txt= str(a) + " | " + str(utc)
    embed.set_footer(text=txt, icon_url=ctx.message.author.avatar_url) 
    await client.say(embed=embed)	
	
	
	
@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def multi(ctx, a,b):
	c=int(a) * int(b)
	s=str(c)
	await client.say(a + " * " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def sub(ctx, a,b):
	c=int(a) - int(b)
	s=str(c)
	await client.say(a + " - " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def add(ctx, a,b):
	c=int(a) + int(b)
	s=str(c)
	await client.say(a + " + " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def div(ctx, a,b):
	c=int(a) / int(b)
	s=str(c)
	await client.say(a + " / " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
async def choose(ctx,message):
	x=message.split("/")
	await client.say(":thinking:  |  I choose: "+ "**"+ random.choice(x) +"**!")



@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def meme(ctx):
	list=['http://i0.kym-cdn.com/photos/images/facebook/001/217/729/f9a.jpg','http://mojly.com/wp-content/uploads/2017/10/Hilarious-Meme-humor-pictures-images-fun-thug-life-funny-meme.jpg','http://cdn.ebaumsworld.com/mediaFiles/picture/2407036/84822802.jpg','http://images.memes.com/meme/29838.jpg','http://images.memes.com/meme/9076.jpg','http://images.memes.com/meme/14834.jpg','http://images.memes.com/meme/10828.jpg','http://images.memes.com/meme/25719.jpg','http://images.memes.com/meme/20837.jpg','http://images.memes.com/meme/27526.jpg','https://i.redd.it/3n3lixsq5vq01.jpg','https://i.redd.it/xovz0z5mewq01.jpg','https://i.redd.it/kqsotjgj0yq01.jpg','http://images.memes.com/meme/868122','http://images.memes.com/meme/1452777','http://images.memes.com/meme/19242.jpg','http://images.memes.com/meme/1111179','https://i.redd.it/cva9tb3r1wq01.png','https://imgur.com/2hlsj7Q','https://i.redd.it/f5l79kk17yq01.jpg','https://i.redd.it/ii9w5dpqyxq01.jpg','https://imgur.com/UH6DABG','https://i.redd.it/5zo511n7bxq01.jpg','https://i.redd.it/dxefclltiyq01.jpg']
	secure_random = random.SystemRandom()
	m=secure_random.choice(list)
	embed = discord.Embed(description="Random Meme", color=0x00BFFF)
	embed.set_image(url=m)
	await client.say(embed=embed)


client.run(str(os.environ.get('BOT_TOKEN')))
