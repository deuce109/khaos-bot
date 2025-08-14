import os
import discord
import bot.client
import bot.discovery as discovery
import logging

FORMAT = '%(asctime)s : %(levelname)s : %(message)s'

logging.basicConfig(format=FORMAT)

def get_secret():
    secret = ""
    try:
        with open("/run/secrets/discord-bot-token") as secret_reader:
            secret = secret_reader.read() 
    except Exception as e:
        logging.warning(f"Could not read secret from file: {e}")
        
    
    return secret if secret else os.getenv('DISCORD_TOKEN', "")

discovery.load_plugins()

intents = discord.Intents.default()
intents.message_content = True
client = bot.client.MyClient(intents=intents, secret=get_secret())
client.start_bot()