import bot.handlers as handlers

commands=[]

def get_command(command_string):

    command = find_command(command_string)

    return command.get("handler", None) if command else None

def help(args):
    if len(args) == 0:
        
        help_text = "# Commands \n"
        help_text += "\n".join([command["help_text"] for command in commands if command.get("help_text", "") != ""])
        return help_text
    else:
        command = find_command(args[0])
        if command:
            return command.get("help_text", "").strip()
        else:
            return "Please specify a command for help"

    

def find_command(command_string):
    for command in commands:
        if command_string in command.get('commands', []):
            return command
    return None


commands.append(  {
    "name": "Help",
    "commands":[
        "help"
    ],
    "handler": help,
    "help_text":"   help <command>: Gives help for all commands or specified command"
} )

commands.append(  {
    "name": "Quote",
    "commands":[
        "quote"
    ],
    "handler":handlers.quotes
} )

commands.append(  {
    "name": "Source",
    "commands":[
        "source",
        "src"
    ],
    "handler": handlers.source,
    "help_text":"   source: Gives the github page for this bot"
} )

commands.append(  {
    "name": "Dice",
    "commands":[
        "dice"
    ],
    "handler": handlers.dice,
    "help_text": """   dice: <list of dice combinations>
          Simulates dice rolls based off of listed dice
          examples: `!dice 1d6`, `!dice 1d4 1d6`"""
} )

commands.append( {
    "name": "RNG",
    "commands": [
        "rng",
        "random"
    ],
    "handler": handlers.random,
    "help_text": """   rng or random: ( --digits <num_of_digits> or --min <min number> --max <max number> ) --amount <amount of #'s to generate>
                   examples: `!rng --digits 5`, `!random --min 0 --max 5 --amount 2`"""
})

commands.append(  {
    "name": "Coin",
    "commands":[
        "coin",
        "flip"
    ],
    "handler": handlers.coin,
    "help_text":"""   coin: <prediction>
          Simulates a coin flip and tells you if you won or lost based off your prediction
          example: `!coin Heads`"""
} )

commands.append(  {
    "name": "Ping",
    "commands":[
        "ping"
    ],
    "handler": handlers.ping,
    "help_text":"   ping: Pings the bot and responds with 'Pong!'"
} )

commands.append(  {
    "name": "Servers",
    "commands":[
        "servers"
    ],
    "handler": handlers.get_servers,
    "help_text":"   servers: List of servers and their ports"
} )

commands.append(  {
    "name": "Docker",
    "commands":[
        "docker"
    ],
    "handler": handlers.docker_handler,
} )

