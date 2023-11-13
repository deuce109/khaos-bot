import shlex
import discord
import bot.commands as commands


class MyClient(discord.Client):


    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        
        content: str = message.content

        if content.startswith("!"):

            content = content.replace("!", "", 1)
            command = shlex.split(content.strip())
            base_command = command[0]
            args = command[1:]

            def fallback(args=None):

                message_string = "Unknown command: %s" % base_command
                if args:
                    message_string += "\nArguments: " + ", ".join(args)

                return message_string

            mapping = commands.get_command(base_command) or fallback

            message_source = message.channel if message.channel else message.author

            await message_source.send(mapping(args))