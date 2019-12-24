# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(msg):
    arg = msg.content[0]
    args = msg.content[1:].split(" ")
    if arg == "!"
        if args[0] == "hs":
            if not args[1]:
                pass
            else:


        elif args[0] == "update":
            break

        elif 'help':
            msg1 = 'Examples:\n !hs (Admin only)\n !hs KalphiteQueen\n !update IronRok KalphiteQueen 100 (Admin only)\n!save\n!clear n (Admin only)'
            msg.channel.send(msg1)
            break



    print(msg.content)


client.run(token)
