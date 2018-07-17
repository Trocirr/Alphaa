import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import urbandict
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
	
@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '399567243744116738':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)	


@client.command(pass_context=True)
async def randomnumber(ctx):
     await client.say(random.randint(1,101))	
	 
@client.command(pass_context=True)
async def lol(ctx):
		await client.say("shut up u retard <a:TrollDance:456805020143190020> <a:Success:456782999607050240> <a:Thinking360:456789181226680331> <a:thinkloading:456846926994997259>")	 
	 
	 

		
	 
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
        await client.say("You don't have permission to use this command.")
	 
@client.command(pass_context=True)
async def dm(ctx, member: discord.Member, message: str):
    await client.send_message(member, message)	
	
@client.command(pass_context=True)
async def idk2(ctx):
	embed = discord.Embed(title="Welcome to **Bonk.io Football League**!", description="BFL is launched in January of 2018. This is the official discord server of Bonk.io Football League. The league does not use any extensions or mods. You can talk about anything here as long as it isn't disrespectful.", color=0xFF8C00)
	await client.say(embed=embed)	
	

@client.command(pass_context=True)
async def exdee(ctx):
    embed = discord.Embed(description="", color=0xC9C9C9)
    embed.add_field(name="Rules", value="You can talk about anything here as long as it isn't disrespectful. If you have a problem with anyone or anything in this server, please DM the Staff about it. \n \n 1. Rudeness, harassment, and immaturity will not be tolerated. \n 2. Porn and otherwise NSFW/NSFL content is prohibited. \n 3. No discussion about highly illegal activity. \n 4. Copyrighted and other unlawful material is prohibited, such as links to illegal content. \n 5. Advertising and promoting is prohibited. Don't even bother posting invite links because the bots will delete them anyway. \n 6. <#443154096787161092> is our main channel. Keep it clean. \n 7. No (random) links in the general chat <#443154096787161092> unless a moderator or higher lets you!")
    await client.say(embed=embed)
	
@client.command(pass_context=True)
async def idk5(ctx):
    embed = discord.Embed(description="", color=0xC9C9C9)
    embed.add_field(name="pro", value="im good in this as serbia in world cup")
    await client.say(embed=embed)	
	
@client.command(pass_context=True)
async def idk(ctx):
    embed = discord.Embed(description="", color=0xC9C9C9)
    embed.add_field(name="Roles", value="<@&443070361450446848> - Staff Team of the league \n <@&443436497350164490> - Referees, tag them if you need referee! \n <@&443074283837718546> - Official BFL Bot \n <@&443070319045902357> - BFL League Players \n <@&443070027743232001> - Default role \n <@&443070606657716234> - Role for our bots")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True, description='Shows the server info.')
async def server(ctx):
    embed = discord.Embed(description="Here's what I could find:", color=0x00ff00)
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
async def xdd(ctx):
	embed = discord.Embed(description="__About Defender__", color=0x00ff00)
	embed.add_field(name=
	
	
@client.command(pass_context=True, description='Shows the info of the mentioned user.')
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find:", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined",value=user.joined_at)
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
    embed = discord.Embed(title="__About BFL__", description="© 2018 BFL Bot All Rights Reserved", color=0x00ff00)
    embed.add_field(name="Original Creators", value="<@399567243744116738> & <@293447483818901504>")
    embed.add_field(name="Server count", value=str(len(client.servers)))
    embed.add_field(name="User count", value=str(len(list(client.get_all_members()))))
    embed.add_field(name="Channel count",value=str(len(list(client.get_all_channels()))))
    embed.add_field(name="API", value="Python")
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/438003912184692738/438306520317427712/Test.png?width=334&height=341')
    utc_dt = datetime.now(timezone.utc)
    p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
    utc = str(p)    
    a=ctx.message.author
    txt= str(a) + " | " + str(utc)
    embed.set_footer(text=txt, icon_url=ctx.message.author.avatar_url) 
    await client.say(embed=embed)
	
	
@client.command(pass_context=True)
async def trocir(ctx):
    embed = discord.Embed(title="__Trocir's profile__ :flag_rs:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="7th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/446395067373191169/Picture1.png?width=868&height=646")
    await client.say(embed=embed)
	

@client.command(pass_context=True)
async def microhype(ctx):
    embed = discord.Embed(title="__MicroHype's profile__ :flag_gb:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="7th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/446395067373191169/Picture1.png?width=868&height=646")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True)
async def frozenkiller(ctx):
    embed = discord.Embed(title="__frozenkiller's profile__ :flag_nl:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="7th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/446395067373191169/Picture1.png?width=868&height=646")
    await client.say(embed=embed)
	

@client.command(pass_context=True)
async def avenger434(ctx):
    embed = discord.Embed(title="__Avenger434's profile__ :flag_my:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="8th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/446395067373191169/Picture1.png?width=868&height=646")
    await client.say(embed=embed)
	
	
@client.command(pass_context=True)
async def mhmmyeeesss(ctx):
    embed = discord.Embed(title="__MhmmYeeesss's profile__ :flag_us:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="7th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/446395067373191169/Picture1.png?width=868&height=646")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True)
async def acquah(ctx):
    embed = discord.Embed(title="__Acquah's profile__ :flag_it:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="7th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/446395067373191169/Picture1.png?width=868&height=646")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True)
async def reddragon6(ctx):
    embed = discord.Embed(title="__RedDragon6's profile__ :flag_pk:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="8th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/446395067373191169/Picture1.png?width=868&height=646")
    await client.say(embed=embed)
	
	
@client.command(pass_context=True)
async def alex2810(ctx):
    embed = discord.Embed(title="__Alex2810's profile__ :flag_ca:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="8th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/446395067373191169/Picture1.png?width=868&height=646")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True)
async def nahojaa(ctx):
    embed = discord.Embed(title="__Naho jaa's profile__ :flag_br:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="9th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/446395067373191169/Picture1.png?width=868&height=646")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True)
async def numbskullian(ctx):
    embed = discord.Embed(title="__Numb Skullian's profile__ :flag_gb:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="9th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/446395067373191169/Picture1.png?width=868&height=646")
    await client.say(embed=embed)	
	

@client.command(pass_context=True)
async def nasean79(ctx):
    embed = discord.Embed(title="__nasean79's profile__ :flag_us:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="10th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/446395067373191169/Picture1.png?width=868&height=646")
    await client.say(embed=embed)		
		
	
@client.command(pass_context=True)
async def commanderjoash(ctx):
    embed = discord.Embed(title="__CommanderJoash's profile__ :flag_us:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="8th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/446395067373191169/Picture1.png?width=868&height=646")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True)
async def aggthescorer(ctx):
    embed = discord.Embed(title="__AggTheScorer__ :flag_gr:", description="", color=0x2874A6)
    embed.add_field(name="Joined", value="15th May 2018")
    embed.add_field(name="Goals", value="0")
    embed.add_field(name="Assists", value="0")
    embed.add_field(name="Own Goals", value="0")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/446395067373191169/Picture1.png?width=868&height=646")
    await client.say(embed=embed)	
	
	
@client.command(pass_context=True)
async def records(ctx):
    embed = discord.Embed(title="__BFL Records__", description="Our Football Records", color=0x2874A6)
    embed.add_field(name="Biggest Win", value="Team 0-0 Team")
    embed.add_field(name="Most Goals in a match", value="Player - 0", inline = False)
    embed.add_field(name="Most Assists in a match", value="Player - 0", inline = False)
    embed.add_field(name="Most Goals of all time", value="Player - 0", inline = False)
    embed.add_field(name="Most Assists of all time", value="Player - 0", inline = False)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/443418563160571944/443423107215261697/Feed_Me_Bonk_League.png?width=462&height=420")
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
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    embed=discord.Embed(title=None, description=':ping_pong: Pong! `{}ms`'.format(round((t2-t1)*1000)), color=0x2874A6)
    await client.say(embed=embed)

@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def meme(ctx):
	list=['http://i0.kym-cdn.com/photos/images/facebook/001/217/729/f9a.jpg','http://mojly.com/wp-content/uploads/2017/10/Hilarious-Meme-humor-pictures-images-fun-thug-life-funny-meme.jpg','http://cdn.ebaumsworld.com/mediaFiles/picture/2407036/84822802.jpg','http://images.memes.com/meme/29838.jpg','http://images.memes.com/meme/9076.jpg','http://images.memes.com/meme/14834.jpg','http://images.memes.com/meme/10828.jpg','http://images.memes.com/meme/25719.jpg','http://images.memes.com/meme/20837.jpg','http://images.memes.com/meme/27526.jpg','https://i.redd.it/3n3lixsq5vq01.jpg','https://i.redd.it/xovz0z5mewq01.jpg','https://i.redd.it/kqsotjgj0yq01.jpg','http://images.memes.com/meme/868122','http://images.memes.com/meme/1452777','http://images.memes.com/meme/19242.jpg','http://images.memes.com/meme/1111179','https://i.redd.it/cva9tb3r1wq01.png','https://imgur.com/2hlsj7Q','https://i.redd.it/f5l79kk17yq01.jpg','https://i.redd.it/ii9w5dpqyxq01.jpg','https://imgur.com/UH6DABG','https://i.redd.it/5zo511n7bxq01.jpg','https://i.redd.it/dxefclltiyq01.jpg']
	secure_random = random.SystemRandom()
	m=secure_random.choice(list)
	embed = discord.Embed(description="Random Meme", color=0x00BFFF)
	embed.set_image(url=m)
	await client.say(embed=embed)

	
@client.command()
async def urban(*, word: str):
	try:
		defi = urbandict.define(word)
		definition = defi[0]['def']
		example = defi[0]['example']
		embed = discord.Embed(title=word, description=definition, color=0x0062f4)
		embed.add_field(name="Example", value=example, inline=False)
		await client.say(embed=embed)
	except:
		await client.say(":exclamation: Error. No definition found.")
			


client.run(str(os.environ.get('BOT_TOKEN')))
