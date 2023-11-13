
import bot.docker.handlers as handlers

import docker

client = docker.from_env()

commands = []

def execute_command(command_text, args):
    command = get_command(command_text)
    if command:
        return command(client, args)
    else:
        message_string = "Unknown Docker command: %s" % command_text
        if args:
            message_string += "\nArguments: " + ", ".join(args)
        return message_string


def get_command(command_text):
    command = find_command(command_text)
    return command.get("handler", None)

def find_command(command_string):
    for command in commands:
        if command_string == command.get('subcommand', ""):
            return command
        
# commands.append(
#     {
#         "name": "Compose",
#         "subcommand": "compose",
#         "handler": handlers.compose        
#     }
# )
commands.append(
    {
        "name": "Restart",
        "subcommand": "restart",
        "handler": handlers.restart        
    }
)
commands.append(
    {
        "name": "Start",
        "subcommand": "start",
        "handler": handlers.start        
    }
)
commands.append(
    {
        "name": "Stop",
        "subcommand": "stop",
        "handler": handlers.stop        
    }
)
commands.append(
    {
        "name": "PS",
        "subcommand": "ps",
        "handler": handlers.ps        
    }
)