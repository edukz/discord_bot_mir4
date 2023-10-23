Sumário:

Este script foi desenvolvido para interagir com os usuários do Discord através de um bot.
Sua principal funcionalidade é informar aos usuários qual missão eles têm em um determinado dia da semana.

Bibliotecas utilizadas:

discord: Usado para interagir com a API do Discord.
json: Usado para manipular e ler arquivos JSON.
datetime: Usado para obter a data e o dia da semana atual.
api_key: Arquivo onde a chave de API do bot é armazenada.

Configuração do Bot

Intents

O bot usa a classe Intents para definir quais tipos de eventos ele deve ouvir. O código abaixo especifica que o bot irá ouvir mensagens:

intents = discord.Intents.default()
intents.message_content = True

Inicialização do Bot
O bot é inicializado com um prefixo de comando ! e os intents definidos anteriormente:

python
Copy code
bot = commands.Bot(command_prefix='!', intents=intents)

Eventos e Comandos

Evento on_ready
Este evento é acionado quando o bot estiver online. Ele imprime no console a mensagem que o bot está online:

python
Copy code
@bot.event
async def on_ready():
    print(f'Bot está online como {bot.user.name}!')


Comando wb

Este comando pode ser acionado por um usuário ao enviar a mensagem !wb em qualquer canal onde o bot esteja presente. A funcionalidade principal deste comando é informar ao usuário qual missão eles têm em um determinado dia da semana:

O ID do usuário é obtido.
O arquivo player.json é lido. Este arquivo contém informações sobre qual missão o usuário tem em cada dia da semana.
Se o ID do usuário for encontrado no arquivo, o script prossegue:
O dia atual da semana é obtido.
A missão correspondente ao dia da semana para esse usuário é recuperada.
O arquivo informacoes.json é lido. Este arquivo contém os apelidos/nicks dos usuários.
O nick do usuário é obtido.
Uma mensagem direta é enviada ao usuário informando-o sobre sua missão do dia.
Se o ID do usuário não for encontrado, uma mensagem de erro é enviada.
python
Copy code
@bot.command()
async def wb(ctx):
    ...

    
Execução do Bot
O bot é executado usando a chave de API obtida do arquivo api_key.py:

python
Copy code
bot.run(API)