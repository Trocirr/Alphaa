#______________________IMPORT______________________#

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
    await client.change_presence(game=discord.Game(name='use macro or be richt | -help'))
	
#Info Commands Down Down Down#
#Info Commands Down Down Down#
#Info Commands Down Down Down#

#______________________CREDITS______________________#

@client.command(pass_context=True)
async def credits(ctx):
    embed = discord.Embed(title="LejentBot", description="© 2019 Lilith Macro All Rights Reserved", color=0x00EEEEE)
    embed.add_field(name="Original Creator", value="Trocir#9999")
    embed.add_field(name="Server count", value=str(len(client.servers)))
    embed.add_field(name="Date of creation", value="2/20/2019")
    embed.add_field(name="User count", value=str(len(list(client.get_all_members()))))
    embed.add_field(name="Channel count",value=str(len(list(client.get_all_channels()))))
    embed.add_field(name="API", value="discord.py")
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/547775699268927489/548181296145367040/depositphotos_117303114-stock-illustration-letter-l-logo-with-red.png?width=298&height=298')
    utc_dt = datetime.now(timezone.utc)
    p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
    utc = str(p)    
    a=ctx.message.author
    txt= str(a) + " | " + str(utc)
    embed.set_footer(text=txt, icon_url=ctx.message.author.avatar_url) 
    await client.say(embed=embed)

#______________________USER-INFO______________________#

@client.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="", description=user.mention, color=0x9B8DC2)
    embed.add_field(name="Nick", value=user.nick, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Bot?", value=user.bot)
    embed.add_field(name="Game", value=user.game)
    embed.add_field(name="Color", value=user.color)
    embed.add_field(name="Top Role", value=user.top_role.mention)
    embed.add_field(name="Joined", value=user.joined_at.__format__('%d. %B %Y %H:%M:%S'))
    embed.add_field(name="Registered", value=user.created_at.__format__('%d. %B %Y %H:%M:%S'))
    embed.set_thumbnail(url = user.avatar_url)
    a = ctx.message.author
    embed.set_author(name=a, icon_url = ctx.message.author.avatar_url)
    txt = user.id
    embed.set_footer(text="User ID: "+txt)
    await client.say(embed=embed)

#______________________ROLE-INFO______________________#

@client.command(pass_context=True)
async def roleinfo(ctx, role: discord.Role):
    embed = discord.Embed(title="", description="", color=0x9B8DC2)
    embed.add_field(name="ID", value=role.id)
    embed.add_field(name="Name", value=role.name)
    embed.add_field(name="Color", value=role.color)
    embed.add_field(name="Mention", value=role.mention)
    embed.add_field(name="Mentionable", value=role.mentionable)
    embed.add_field(name="Hoisted", value=role.hoist)
    embed.add_field(name="Position", value=role.position)
    embed.add_field(name="Managed", value=role.managed)
    embed.add_field(name="Role Created", value=role.created_at.__format__('%d. %B %Y'))
    embed.set_thumbnail(url= ctx.message.author.avatar_url)
    embed.set_author(name="Here's what I could find:")
    utc_dt = datetime.now(timezone.utc)
    p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
    utc = str(p)    
    a=ctx.message.author
    txt= str(a) + " | " + str(utc)
    embed.set_footer(text=txt, icon_url=ctx.message.author.avatar_url) 
    await client.say(embed=embed)

#______________________CHANNEL-INFO______________________#

@client.command(pass_context=True)
async def channel(ctx, channel: discord.Channel):
    embed = discord.Embed(title="", description="", color=0x9B8DC2)
    embed.add_field(name="ID", value=channel.id)
    embed.add_field(name="Name", value=channel.name)
    embed.add_field(name="Private", value=channel.is_private)
    embed.add_field(name="Position", value=channel.position)
    embed.add_field(name="Channel Type", value=channel.type)
    embed.add_field(name="Default", value=channel.is_default)
    embed.add_field(name="Mention", value=channel.mention)
    embed.add_field(name="Channel Created", value=channel.created_at.__format__('%d. %B %Y'))
    embed.set_thumbnail(url= ctx.message.author.avatar_url)
    embed.set_author(name="Here's what I could find:")
    utc_dt = datetime.now(timezone.utc)
    p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
    utc = str(p)    
    a=ctx.message.author
    txt= str(a) + " | " + str(utc)
    embed.set_footer(text=txt, icon_url=ctx.message.author.avatar_url)
    await client.say(embed=embed)

#______________________SERVER-INFO______________________#

@client.command(pass_context=True, description='Shows the server info.')
async def serverinfo(ctx):
    embed = discord.Embed(title="", description="", color=0x6A7A94)
    embed.add_field(name="Owner", value=ctx.message.server.owner)
    embed.add_field(name="Region", value=ctx.message.server.region)
    embed.add_field(name="Channels", value=len(ctx.message.server.channels))
    embed.add_field(name="Afk Channel", value=str(ctx.message.server.afk_channel))
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name="Roles", value=len(ctx.message.server.roles))
    embed.add_field(name="Emotes", value=len(ctx.message.server.emojis))
    embed.add_field(name="Verification", value=str(ctx.message.server.verification_level))
    embed.add_field(name="Default Role", value=ctx.message.server.default_role)
    embed.add_field(name="Default Channel", value=ctx.message.server.default_channel)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    xd = ctx.message.server.name
    embed.set_author(name=xd, icon_url = ctx.message.server.icon_url)
    txt = ctx.message.server.id
    oh = ctx.message.server.created_at.__format__('%d. %B %Y')
    hehe = " | Server Created: "
    embed.set_footer(text="ID: "+txt +hehe +oh)
    await client.say(embed=embed)

#______________________INVITE-CODE______________________#

@client.command(pass_context=True)
async def invitecode(ctx, invite: discord.Invite):
    embed = discord.Embed(title="", description="", color=0x6A7A94)
    embed.add_field(name="Server", value=invite.server)
    embed.add_field(name="Inviter", value=invite.inviter)
    embed.add_field(name="Code", value=invite.id)
    embed.add_field(name="Edited", value=invite.revoked)
    embed.add_field(name="Channel", value=invite.channel)
    embed.add_field(name="Link", value=invite.url)
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    embed.set_author(name="Here's what I could find:")
    utc_dt = datetime.now(timezone.utc)
    p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
    utc = str(    p)    
    a=ctx.message.author
    txt= str(a) + " | " + str(utc)
    embed.set_footer(text=txt, icon_url=ctx.message.author.avatar_url)
    await client.say(embed=embed)

#______________________EMOJI-INFO______________________#

@client.command(pass_context=True)
async def emojiinfo(ctx, emoji: discord.Emoji):
    embed = discord.Embed(title="", description="", color=0x6A7A94)
    embed.add_field(name="ID", value=emoji.id)
    embed.add_field(name="Name", value=emoji.name)
    embed.add_field(name="Colons", value=emoji.require_colons)
    embed.add_field(name="Managed", value=emoji.managed)
    embed.add_field(name="Roles", value=emoji.roles)
    embed.add_field(name="Emoji Created", value=emoji.created_at.__format__('%d. %B %Y'))
    embed.set_thumbnail(url=emoji.url)
    embed.set_author(name="Here's what I could find:")
    utc_dt = datetime.now(timezone.utc)
    p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
    utc = str(    p)    
    a=ctx.message.author
    txt= str(a) + " | " + str(utc)
    embed.set_footer(text=txt, icon_url=ctx.message.author.avatar_url)
    await client.say(embed=embed)

#______________________HUGE-EMOJI______________________#

@client.command(pass_context=True)
async def hugeemoji(ctx, emoji: discord.Emoji):
    await client.say(emoji.url)

#______________________CUSTOM-COMMAND______________________#

@client.command(pass_context=True)
async def macro(ctx):
    embed=discord.Embed(title="", description="", color=0x6a7a94)
    embed.add_field(name="Best macro user", value="Lilith")
    embed.add_field(name="second best", value="tuxedo")
    xd = ctx.message.server.name
    embed.set_author(name=xd, icon_url = ctx.message.server.icon_url)
    embed.set_footer(text="Official macro list")
    embed.set_image(url=ctx.message.server.icon_url)
    await client.say(embed=embed)

#Moderator Commands Down Down Down#
#Moderator Commands Down Down Down#
#Moderator Commands Down Down Down#

#______________________PURGE______________________#

@client.command(pass_context=True)
async def purge(ctx, amount=100):
    id_list = ['562000458181246982']
    if ctx.message.author.id in id_list or ctx.message.author.server_permissions.administrator:
         channel = ctx.message.channel
         messages = []
         async for message in client.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
         await client.delete_messages(messages)
         await client.say("<:alphaSuccess:569179017664790528> Successfully deleted message(s).")
    else:
        await client.say("<:alphaError:569178991349465088> You do not have permissions to use this command.")

#______________________BAN______________________#

@client.command(pass_context = True)
async def ban(ctx, user: discord.User,*, bugs: str = None):
    if bugs is None:
        bugs = "Unspecified"
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '562000458181246982':
        embed = discord.Embed(title="", description="{} has been banned.".format(user.name), color=0x0072ff)
        embed.add_field(name="Reason", value=bugs)
        embed.set_author(name="Alpha Moderation", icon_url="https://media.discordapp.net/attachments/562005351353024525/569168417857208320/RealAlpha.png?width=355&height=356")
        utc_dt = datetime.now(timezone.utc)
        p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
        utc = str(    p)    
        txt=str(utc)
        embed.set_footer(text=txt)
        await client.say(embed=embed)
        xd = ctx.message.server.name
        embed = discord.Embed(title="", description="You have been banned from: " +xd, color=0x495c66)
        embed.add_field(name="Action", value="Ban")
        embed.add_field(name="Reason", value=bugs)
        embed.set_author(name="Alpha Moderation", icon_url="https://media.discordapp.net/attachments/562005351353024525/569168417857208320/RealAlpha.png?width=355&height=356")
        utc_dt = datetime.now(timezone.utc)
        p = utc_dt.strftime('       %H:%M:%S • %d/%m/%Y  ')
        utc = str(    p)    
        a=ctx.message.author
        txt= str(a) + " | " + str(utc)
        embed.set_footer(text="Banned by: " +txt)
        await client.send_message(user, embed=embed)
        await client.ban(user)
    else:
        embed=discord.Embed(title="Permission Denied.", description="<:alphaError:569178991349465088> You don't have permission to use this command.", color=0xEA1025)
        await client.say(embed=embed)

#______________________KICK______________________#

@client.command(pass_context = True)
async def kick(ctx, user: discord.User,*, bugs: str = None):
    if bugs is None:
        bugs = "Unspecified"
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '562000458181246982':
        embed = discord.Embed(title="", description="{} has been kicked.".format(user.name), color=0x0072ff)
        embed.add_field(name="Reason", value=bugs)
        embed.set_author(name="Alpha Moderation", icon_url="https://media.discordapp.net/attachments/562005351353024525/569168417857208320/RealAlpha.png?width=355&height=356")
        utc_dt = datetime.now(timezone.utc)
        p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
        utc = str(    p)    
        txt=str(utc)
        embed.set_footer(text=txt)
        await client.say(embed=embed)
        xd = ctx.message.server.name
        embed = discord.Embed(title="", description="You have been kicked from: " +xd, color=0x495c66)
        embed.add_field(name="Action", value="Kick")
        embed.add_field(name="Reason", value=bugs)
        embed.set_author(name="Alpha Moderation", icon_url="https://media.discordapp.net/attachments/562005351353024525/569168417857208320/RealAlpha.png?width=355&height=356")
        utc_dt = datetime.now(timezone.utc)
        p = utc_dt.strftime('       %H:%M:%S • %d/%m/%Y  ')
        utc = str(    p)    
        a=ctx.message.author
        txt= str(a) + " | " + str(utc)
        embed.set_footer(text="Kicked by: " +txt)
        await client.send_message(user, embed=embed)
        await client.kick(user)
    else:
        embed=discord.Embed(title="Permission Denied.", description="<:alphaError:569178991349465088> You don't have permission to use this command.", color=0xEA1025)
        await client.say(embed=embed)

#______________________MUTE______________________#

@client.command(pass_context = True)
async def mute(ctx, user: discord.Member,*,  bugs: str = None):
    if bugs is None:
        bugs = "Unspecified"
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '562000458181246982':
        embed = discord.Embed(title="", description="{} has been muted.".format(user.name) , color=0x0072ff)
        role = discord.utils.get(user.server.roles, name="Muted")
        await client.add_roles(user, role)
        embed.add_field(name="Reason", value=bugs)
        embed.set_author(name="Alpha Moderation", icon_url="https://media.discordapp.net/attachments/562005351353024525/569168417857208320/RealAlpha.png?width=355&height=356")
        utc_dt = datetime.now(timezone.utc)
        p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
        utc = str(    p)    
        txt=str(utc)
        embed.set_footer(text=txt)
        await client.send_message(client.get_channel("562005351353024525"), embed=embed)
        xd = ctx.message.server.name
        embed = discord.Embed(title="", description="You have been muted in: " +xd, color=0x495c66)
        embed.add_field(name="Action", value="Mute")
        embed.add_field(name="Reason", value=bugs)
        embed.set_author(name="Alpha Moderation", icon_url="https://media.discordapp.net/attachments/562005351353024525/569168417857208320/RealAlpha.png?width=355&height=356")
        utc_dt = datetime.now(timezone.utc)
        p = utc_dt.strftime('       %H:%M:%S • %d/%m/%Y  ')
        utc = str(    p)    
        a=ctx.message.author
        txt= str(a) + " | " + str(utc)
        embed.set_footer(text="Muted by: " +txt)
        await client.send_message(user, embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="<:alphaError:569178991349465088> You don't have permission to use this command.", color=0xEA1025)
        await client.say(embed=embed)

#______________________WARN______________________#

@client.command(pass_context = True)
async def warn(ctx, user: discord.Member,*,  bugs: str):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '562000458181246982':
        embed = discord.Embed(title="", description="{} has been warned.".format(user.name) , color=0x0072ff)
        role = discord.utils.get(user.server.roles, name="Muted")
        await client.add_roles(user, role)
        embed.add_field(name="Reason", value=bugs)
        embed.set_author(name="Alpha Moderation", icon_url="https://media.discordapp.net/attachments/562005351353024525/569168417857208320/RealAlpha.png?width=355&height=356")
        utc_dt = datetime.now(timezone.utc)
        p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
        utc = str(    p)    
        txt=str(utc)
        embed.set_footer(text=txt)
        await client.send_message(client.get_channel("562005351353024525"), embed=embed)
        xd = ctx.message.server.name
        embed = discord.Embed(title="", description="You were warned in: " +xd, color=0x495c66)
        embed.add_field(name="Action", value="Warn")
        embed.add_field(name="Reason", value=bugs)
        embed.set_author(name="Alpha Moderation", icon_url="https://media.discordapp.net/attachments/562005351353024525/569168417857208320/RealAlpha.png?width=355&height=356")
        utc_dt = datetime.now(timezone.utc)
        p = utc_dt.strftime('       %H:%M:%S • %d/%m/%Y  ')
        utc = str(    p)    
        a=ctx.message.author
        txt= str(a) + " | " + str(utc)
        embed.set_footer(text="Warned by: " +txt)
        await client.send_message(user, embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="<:alphaError:569178991349465088> You don't have permission to use this command.", color=0xEA1025)
        await client.say(embed=embed)
            
#______________________TIME______________________#
	
@client.command(pass_context=True)
async def time(ctx):
	utc_dt = datetime.now(timezone.utc)
	p = utc_dt.strftime('     Time - %H:%M:%S | Date - %d/%m/%Y')
	utc = str(p)
	embed = discord.Embed(description="", color=0xFF0000)
	embed.add_field(name=":stopwatch: **Current Local Time and Date in the United Kingdom**", value=utc)
	await client.say(embed=embed)	

@client.command(pass_context=True)
async def ping(ctx):
	await client.say("Checking ping..")
	await client.edit_message( "nigger" +random.randint(150,340))
	 
@client.command(pass_context=True)
async def dmm(ctx, member: discord.Member, message: str):
    await client.send_message(member, message)	
	
@client.command(pass_context=True)
async def rulesxdxdxd(ctx):
	embed = discord.Embed(title="", description="**Getting Started** \n - If you have any questions about BFL, feel free to ask us in <#535451148090474497> \n - If you want to join the League, contact Trocir#9999. \n - If you have any suggestions or requests, let us know in <#536932821520875530> by typing `-suggest [Your suggestion here]` in <#535451161998917655> \n \n - BFL is launched in November of 2017. This is the official discord server of BFL. You can talk about anything here as long as it isn't disrespectful. \n - The prefix for BFL Bot on this server is `-` which is also the default for the bot. \n - Our aim is to provide best experience possible for playing Bonk.io Football at a competitive level. \n \n **Rules** \n - You can talk about anything here as long as it isn't disrespectful. If you have a problem with anyone or anything in this server, please DM the Admins about it. \n 1. Rudeness, harassment, and immaturity will not be tolerated. \n 2. Porn and otherwise NSFW/NSFL content is prohibited. \n 3. No discussion about highly illegal activity. \n 4. Copyrighted and other unlawful material is prohibited, such as links to illegal content. \n 5. Advertising and promoting is prohibited. Don't even bother posting invite links because the bots will delete them anyway. \n 6. <#535451148090474497> is our main channel. Keep it clean. \n 7. No (random) links in the general chat <#535451148090474497> unless a moderator or higher lets you! \n - **Moderators may mute/kick/ban at their discretion.** \n \n **Links** \n [BFL Website](https://bonkfootballleague.wixsite.com/footballleague) \n [Youtube Channel](https://www.youtube.com/channel/UCYhjjzOPwfLMvQUwjEZi4gw?) \n [Add BFL Bot](https://discordapp.com/oauth2/authorize?client_id=432607914432135169&permissions=8&scope=bot)", color=0x3D59AB)
	embed.add_field(name="Invite to this Server", value="https://discord.gg/wsWMWCA")
	embed.set_author(name="Welcome to the BFL Discord Server!", icon_url="https://images-ext-2.discordapp.net/external/WLXavXaSZmhfV9DuHJFBh0YcNbuUdtWLl1lJScKOqZo/https/cdn.discordapp.com/icons/533422792167915554/a052ef6b337317f7348c50730d8f1010.jpg?width=116&height=116")
	await client.say(embed=embed)	

@client.command(pass_context=True)
async def rebels(ctx):
	embed = discord.Embed(title="", description="Rebels is one of the worst clans right now with a 3-40 record held by the owner low iq xhappyx and the captain richt dickrider aalaaprocks \n \n We are the first team to reach 40 loses in bonk io clan history (Fact) \n \n It has bad players such as aalaaprocks, bartek0458, dadem and more! \n \n  It has a discord server with an inactive community. Dont join Rebels today!", color=0x00EEEE)
	embed.add_field(name="Invite to this Server", value="[No invite because it sucks](https://discord.gg/xg6RGf8)")
	embed.set_image(url="https://media.discordapp.net/attachments/468414226575130637/552957652603240634/Rebels_Partners.PNG?width=299&height=66")
	embed.set_author(name="Rebels", icon_url="https://media.discordapp.net/attachments/468414226575130637/552957652603240634/Rebels_Partners.PNG?width=299&height=66")
	embed.set_footer(text="Partner")
	await client.say(embed=embed)
	
@client.command(pass_context=True)
async def roses(ctx):
	embed = discord.Embed(title="", description=" Roses is one of the dumbest clans currently in Bonk.io Football lead by xSmurf and Alex2810. \n \n It has one of the worst war records currently standing at : 0-30! \n \n It has bad players such as Nub1, Tuccio, xSmurf and more! \n \n It has a discord server with an inactive community \n \n Dont join roses today!", color=0x00EEEE)
	embed.add_field(name="Invite to this Server", value="[Click Here](https://discord.gg/rGfxT3b)")
	embed.set_image(url="https://images-ext-2.discordapp.net/external/M2Cx7oPf1mK4jtQ-Boa-n-Xxfwfz0ZD78lkViHXg2dc/https/discordapp.com/api/guilds/515609188047519744/icons/43d75d5e16516179ce4247d109f917ec.jpg?width=103&height=103")
	embed.set_author(name="Roses", icon_url="https://images-ext-2.discordapp.net/external/M2Cx7oPf1mK4jtQ-Boa-n-Xxfwfz0ZD78lkViHXg2dc/https/discordapp.com/api/guilds/515609188047519744/icons/43d75d5e16516179ce4247d109f917ec.jpg?width=103&height=103")
	embed.set_footer(text="Partner")
	await client.say(embed=embed)	

	
@client.command(pass_context=True)
async def top(ctx):
	embed = discord.Embed(title="", description="", color=0x3D59AB)
	embed.add_field(name="Top 30", value="This is the top 30 best players who have ever played bonk.io and ever will judged by Trocir and TLJXEDO. \n \n It is also based on the 1v1 tournament results as well as public opinion. This is not 100% accurate, but it is as close as it can come to. If you have any opinions, feel free to express them. \n \n If you're not here, do not complain or request to be added.")
	embed.set_author(name="Bonk.io - Football League", icon_url="https://images-ext-2.discordapp.net/external/WLXavXaSZmhfV9DuHJFBh0YcNbuUdtWLl1lJScKOqZo/https/cdn.discordapp.com/icons/533422792167915554/a052ef6b337317f7348c50730d8f1010.jpg?width=116&height=116")
	embed.set_footer(text="BFL")
	await client.say(embed=embed)
	
@client.command(pass_context=True)
async def vaga(ctx):
	embed = discord.Embed(title="", description="", color=0x3D59AB)
	embed.add_field(name="Top 30", value="This is the top 30 best players who are currently playing bonk.io judged by Trocir and TLJXEDO. \n \n It is also based on the 1v1 tournament results as well as public opinion. This is not 100% accurate, but it is as close as it can come to. If you have any opinions, feel free to express them. \n \n If you're not here, do not complain or request to be added.")
	embed.set_author(name="Bonk.io - Football League", icon_url="https://images-ext-2.discordapp.net/external/WLXavXaSZmhfV9DuHJFBh0YcNbuUdtWLl1lJScKOqZo/https/cdn.discordapp.com/icons/533422792167915554/a052ef6b337317f7348c50730d8f1010.jpg?width=116&height=116")
	embed.set_footer(text="BFL")
	await client.say(embed=embed)	
	
@client.command(pass_context=True)
async def vagaa(ctx):
	embed = discord.Embed(title="", description="", color=0x3D59AB)
	embed.add_field(name="Rank", value="1. anxiety \n 3. General_Richt \n 5. Trocir \n 7. GSpeku \n 9. zmudx \n \n 11. leftright \n 13. le riz \n 15. Acquah \n 17. aalaaprocks \n 19. mesney \n \n 21. SxC Swish \n 23. alalalaaa07 \n 25. Tuccio \n 27. bartek0458 \n 29. TheAngryBull")
	embed.add_field(name="Rank", value="2. lolwhat5011 \n 4. Nub1 \n 6. TLJXEDO \n 8. Trxior \n 10. selet \n \n 12. Bunniesss \n 14. frozenkiller \n 16. MicroHype \n 18. xSmurf \n 20. bbb86 \n \n 22. Alex2810 \n 24. Sm4cK \n 26. CommandX11 \n 28. Magician 1223 \n 30. scoregod")
	embed.set_author(name="Bonk.io - Football League", icon_url="https://images-ext-2.discordapp.net/external/WLXavXaSZmhfV9DuHJFBh0YcNbuUdtWLl1lJScKOqZo/https/cdn.discordapp.com/icons/533422792167915554/a052ef6b337317f7348c50730d8f1010.jpg?width=116&height=116")
	embed.set_footer(text="All Time")
	await client.say(embed=embed)
	
@client.command(pass_context=True)
async def vagaaa(ctx):
	embed = discord.Embed(title="", description="", color=0x3D59AB)
	embed.add_field(name="Rank", value="1. anxiety \n 3. General_Richt \n 5. Trocir \n 7. GSpeku \n 9. zmudx \n \n 11. leftright \n 13. le riz \n 15. Acquah \n 17. aalaaprocks \n 19. mesney \n \n 21. SxC Swish \n 23. alalalaaa07 \n 25. Tuccio \n 27. bartek0458 \n 29. TheAngryBull")
	embed.add_field(name="Rank", value="2. lolwhat5011 \n 4. Nub1 \n 6. TLJXEDO \n 8. Trxior \n 10. selet \n \n 12. Bunniesss \n 14. frozenkiller \n 16. MicroHype \n 18. xSmurf \n 20. bbb86 \n \n 22. Alex2810 \n 24. Sm4cK \n 26. CommandX11 \n 28. Magician 1223 \n 30. scoregod")
	embed.set_author(name="Bonk.io - Football League", icon_url="https://images-ext-2.discordapp.net/external/WLXavXaSZmhfV9DuHJFBh0YcNbuUdtWLl1lJScKOqZo/https/cdn.discordapp.com/icons/533422792167915554/a052ef6b337317f7348c50730d8f1010.jpg?width=116&height=116")
	embed.set_footer(text="All Time")
	await client.say(embed=embed)	
	
@client.command(pass_context=True)
async def oko(ctx):
	embed = discord.Embed(title="", description="", color=0x3D59AB)
	embed.add_field(name="Top 30", value="This is the top 16 best players who have competed in the 1v1 tournaments in this server judged by their scoring and performance by Trocir and TLJXEDO. Only players who have competed in the tournaments will be added here. \n \n Do not ask to be added or for your position to be changed.")
	embed.set_author(name="Bonk.io - Football League", icon_url="https://images-ext-2.discordapp.net/external/WLXavXaSZmhfV9DuHJFBh0YcNbuUdtWLl1lJScKOqZo/https/cdn.discordapp.com/icons/533422792167915554/a052ef6b337317f7348c50730d8f1010.jpg?width=116&height=116")
	embed.set_footer(text="BFL")
	await client.say(embed=embed)
		

@client.command(pass_context=True)
@commands.cooldown(1, 3, commands.BucketType.user)
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
@commands.cooldown(1, 3, commands.BucketType.user)
async def multi(ctx, a,b):
	c=int(a) * int(b)
	s=str(c)
	await client.say(a + " * " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
@commands.cooldown(1, 3, commands.BucketType.user)
async def sub(ctx, a,b):
	c=int(a) - int(b)
	s=str(c)
	await client.say(a + " - " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
@commands.cooldown(1, 3, commands.BucketType.user)
async def add(ctx, a,b):
	c=int(a) + int(b)
	s=str(c)
	await client.say(a + " + " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
@commands.cooldown(1, 3, commands.BucketType.user)
async def div(ctx, a,b):
	c=int(a) / int(b)
	s=str(c)
	await client.say(a + " / " + b + " = " + s)
	
	
	
@client.command(pass_context=True)
@commands.cooldown(1, 3, commands.BucketType.user)
async def choose(ctx,message):
	x=message.split("/")
	await client.say(":thinking:  |  I choose: "+ "**"+ random.choice(x) +"**!")



@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def meme(ctx):
	list=['http://i0.kym-cdn.com/photos/images/facebook/001/217/729/f9a.jpg','http://mojly.com/wp-content/uploads/2017/10/Hilarious-Meme-humor-pictures-images-fun-thug-life-funny-meme.jpg','http://cdn.ebaumsworld.com/mediaFiles/picture/2407036/84822802.jpg','http://images.memes.com/meme/29838.jpg','http://images.memes.com/meme/9076.jpg','http://images.memes.com/meme/14834.jpg','http://images.memes.com/meme/10828.jpg','http://images.memes.com/meme/25719.jpg','http://images.memes.com/meme/20837.jpg','http://images.memes.com/meme/27526.jpg','https://i.redd.it/3n3lixsq5vq01.jpg','https://i.redd.it/xovz0z5mewq01.jpg','https://i.redd.it/kqsotjgj0yq01.jpg','http://images.memes.com/meme/868122','http://images.memes.com/meme/1452777','http://images.memes.com/meme/19242.jpg','http://images.memes.com/meme/1111179','https://i.redd.it/cva9tb3r1wq01.png','https://imgur.com/2hlsj7Q','https://i.redd.it/f5l79kk17yq01.jpg','https://i.redd.it/ii9w5dpqyxq01.jpg','https://imgur.com/UH6DABG','https://i.redd.it/5zo511n7bxq01.jpg','https://i.redd.it/dxefclltiyq01.jpg']
	secure_random = random.SystemRandom()
	m=secure_random.choice(list)
	embed = discord.Embed(description="Random Meme", color=0x00BFFF)
	embed.set_image(url=m)
	await client.say(embed=embed)


client.run(str(os.environ.get('BOT_TOKEN')))
