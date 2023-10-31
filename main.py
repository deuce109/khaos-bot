import os
import discord
import bot.client

intents = discord.Intents.default()
intents.message_content = True
client = bot.client.MyClient(intents=intents)
client.run(os.getenv("DISCORD_BOT_SECRET"))