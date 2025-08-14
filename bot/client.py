import shlex
import discord
from bot.discovery import exec_command
import logging



class MyClient(discord.Client):
    
    def __init__(self, intents, secret: str):
        super().__init__(intents=intents)
        self.secret = secret
    
    def start_bot(self):
        
        if self.secret:
            super().run(self.secret)
        else:
            logging.error("No secret provided for the bot. Exiting.")


    async def on_ready(self):
        logging.info('Logged on as %s', self.user)

    async def on_message(self, message: discord.Message):

        
        content: str = message.content
        
        prefix = "!"

        if message.author != self.user and content.startswith(prefix):
            content = content[len(prefix):]

            args = shlex.split(content)
            
            return_message = exec_command(args[0], args[1:])
            
            try:
                await message.reply(return_message)
            except Exception as e:
                logging.error(f"Error replying to message: {e}")
            
            
