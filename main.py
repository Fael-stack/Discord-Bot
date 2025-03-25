import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event()
async def on_member_join(membro:discord.member):

@bot.command()
async def ola(ctx:commands.Context, *,texto):
    nome = ctx.author.name
    await ctx.reply(f"Olá, {nome}! Tudo bem?")

@bot.command()
async def ola(ctx:commands.Context, texto):
    await ctx.send(texto)

@bot.command()
async def somar(ctx:commands.Context, num1:float, num2:float):
    resultado = num1 + num2
    await ctx.send(f"a soma entre {num1} e {num2} é igual a {resultado}")    



bot.run(TOKEN)
