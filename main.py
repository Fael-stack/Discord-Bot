import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command()
async def ola(ctx:commands.Context):
    await ctx.reply("Olá! Tudo bem?")






























bot.run("MTM1MjQ1NjExNTcwMjQ2ODY4MQ.G_bfSj.m0PcvjmZFZ_PKoE0Zr0g3ItxO4yTEAt7ifLo7M")

