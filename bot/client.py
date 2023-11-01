from bot.handlers import get_pattern_mappings
import shlex
import discord


class MyClient(discord.Client):

    # def __init__(self):
    #     self.pattern_mappings = get_pattern_mappings()


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

            mapping = get_pattern_mappings().get(base_command, fallback)

            await message.channels.send(mapping(args))