import os
import discord
# from google.cloud import texttospeech


intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')


@client.event
async def on_message(message):
    print()
    print(message.author.name)
    print(message.content)
    print()
    if message.content.startswith('/ratchet'):
        # Extrait le texte après la commande
        text = message.content[len('/ratchet'):].strip()

        # Utilise ici l'API de synthèse vocale pour générer le fichier audio
        # Exemple avec Google TTS (faudra configurer l'authentification et tout)

        # Envoie le fichier audio généré
        await message.channel.send(file=discord.File('Fart with reverb sound effect.mp3'))

token_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'HIMBOT_token.txt')
token = ''
with open(token_path, 'r') as file:
    token = file.read()
client.run(token)
