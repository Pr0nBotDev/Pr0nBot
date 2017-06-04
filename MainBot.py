import discord
import os
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='.', description="Oh baby...")

configFile = "config.json"
if os.path.isfile("config.json"):
    file = open("config.json")
    conf = json.load(file)
    discord_token = conf["discord_token"]
else:
    print("RIP no config")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def stop():
    print('------')
    print('Logging out')
    await bot.logout()

@bot.command()
async def play(word:str=None):
    await bot.change_presence(game=discord.Game(name=word))

@bot.command()
async def ping():
    await bot.say("Pong!")

@bot.event
async def on_message(message):   
    await bot.process_commands(message)

# Load cogs here
bot.load_extension("PornHub")

bot.run(discord_token)