import discord
from discord.ext import commands
import json
import datetime
from api_key import API

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot está online como {bot.user.name}!')

@bot.command()
async def wb(ctx):
    # Obter ID do usuário
    user_id = str(ctx.author.id)
    
    # Ler o arquivo player.json
    with open('player.json', 'r') as file:
        player_data = json.load(file)
    
    # Verificar se o ID do usuário está no arquivo
    if user_id in player_data:
        # Obter o dia da semana
        day_of_week = datetime.datetime.now().strftime('%A')
        
        # Obter a missão do boss para esse dia
        boss = player_data[user_id][day_of_week]
        
        # Ler o arquivo informacoes.json
        with open('informacoes.json', 'r') as file:
            info_data = json.load(file)
        
        # Obter o nick do usuário
        nick = info_data[user_id]
        
        # Enviar a resposta
        await ctx.author.send(f'{nick}, você deve ir ao {boss} hoje!')

    else:
        await ctx.send('Erro: Usuário não encontrado!')

bot.run(API)
