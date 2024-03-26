import os
import discord
# from google.cloud import texttospeech


parent_folder = os.path.dirname(__file__)
root_folder = os.path.dirname(parent_folder)

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')


@client.event
async def on_message(message):
    if message.content.startswith('/ratchet'):
        # Extrait le texte après la commande
        text = message.content[len('/ratchet'):].strip()

        # Utilise ici l'API de synthèse vocale pour générer le fichier audio
        # Exemple avec Google TTS (faudra configurer l'authentification et tout)

        # Envoie le fichier audio généré
        # file_path = os.path.join(parent_folder, 'Fart with reverb sound effect.mp3')
        file_path = os.path.join(parent_folder, 'ratchetunreal.mp3')
        await message.channel.send(file=discord.File(file_path), reference=message)


token_path = os.path.join(root_folder, 'HIMBOT_token.txt')
token = ''
with open(token_path, 'r') as file:
    token = file.read()
client.run(token)
