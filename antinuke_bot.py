"""
Guardian Anti-Nuke Bot v5.0
Deploy-ready template for Railway
"""

import os
import discord
from discord.ext import commands

TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

# Paste the rest of your big anti-nuke code below this line.

if __name__ == "__main__":
    bot.run(TOKEN)
