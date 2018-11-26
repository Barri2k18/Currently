import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
import aiohttp
from discord.utils import find
from discord import Game, Embed, Color, Status, ChannelType

# --- xd
owner = ["362672438699622403"]
developer = ["362672438699622403"]

BOT_PREFIX = ("<", "c", "currently", "§")

#timestamp=datetime.datetime.utcfromtimestamp(1541415948)

bot = Bot(description="You are not supposed to see this", command_prefix=BOT_PREFIX, pm_help = True)
bot.remove_command('help')
# --- xd
def is_owner(ctx):
    return ctx.message.author.id == "362672438699622403, 282998342315933707"

async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name='for -help', type=1))
        await asyncio.sleep(5)
        await bot.change_presence(game=discord.Game(name='with '+str(len(set(bot.get_all_members())))+' users', type=1))
        await asyncio.sleep(3)
        await bot.change_presence(game=discord.Game(name='in '+str(len(bot.servers))+' servers',type=1))
        await asyncio.sleep(3)
        await bot.change_presence(game=discord.Game(name='with my you.', type=1))
        await asyncio.sleep(3)
        await bot.change_presence(game=discord.Game(name='XD', type=1))
        await asyncio.sleep(1)
     
         # ------------ Oofy  
         
@bot.event
async def on_ready():
    print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
    print('--------') # -
    print('--------') # --
    print('🕵 Succesfull') # ---
    print('load') # ----
    print('--------') # -----
    print('--------') # ------
    print('Invite link: https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(bot.user.id)) # -------
    bot.loop.create_task(status_task())
    
@bot.command(pass_context=True, hidden=True)
async def setavatar(ctx, url):
	if ctx.message.author.id not in owner:
		return
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as r:
			data = await r.read()
	await bot.edit_profile(avatar=data)
	await bot.say("I changed my avatar.", delete_after=6)
	await bot.delete_message(ctx.message)
  
  bot.run(os.getenv('TOKEN'))
