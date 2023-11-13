import json
import requests

import bot.helpers as helpers
import bot.docker.commands as docker_commands
import bot.docker.helpers as docker_helpers
import numpy as np

def ping(_):
    return "Pong!"

def get_servers(_):

    result_string: str = "# Servers\n## IP: \nInternal: 192.168.86.62\n"

    result = requests.get("https://ifconfig.me/ip")

    if result.status_code == 200:
        result_string += "External: %s" % result.text.strip()
    else:
        result_string += "Error retrieving: [%d] %s" % (result.status_code, result.reason)


    docker_info = docker_helpers.get_port_info()

    return "%s\n%s" % (result_string, docker_info)

def random(args):

    rands = helpers.rng(args).tolist()


    output = "\n".join([", ".join([str(n) for n in rng]) for rng in helpers.chunks(rands, 5)] )

    return "Results:\n" + output

def dice(args):
    output = "Results:"

    running_total = 0

    for arg in args:

        sep = "d" if "d" in arg else "D"

        splits = arg.split(sep)

        amount = splits[0]
        sides = splits[1]

        outcomes = np.array([outcome + 1 for outcome in helpers.rng(["--max", sides, "--amount", amount])])

        total = outcomes.sum()

        running_total += total

        for i, outcome in enumerate(outcomes):
            output += f"d{sides} #{i+1}: {outcome}\n"

        output += f"d{sides} Total: {total}\n"

        output += "\n"
    
    output += f"Overall total: {running_total}"

    return output


def coin(args):

    valid_predictions = [prediction.casefold() for prediction in ["t", "h", "Tail", "Head", "Tails", "Heads"]]

    if args[0] in valid_predictions:

        prediction = args[0][0].casefold()

        outcome = str(np.random.choice(["h".casefold(), "t".casefold()])) 

        return "Outcome was %s.\nYou %s" % ("heads" if outcome == "h" else "tails", "win!" if outcome == prediction else "lose.")
    
    else:
        return "Please use a valid prediction\nOptions: " + ", ".join(valid_predictions) 

def source(_):
    return "My source code is located at https://github.com/deuce109/ip-bot"

def quotes(args):
    quote_mapping: dict = {}
    with open('data/quotes.json', 'r') as quote_reader:
        quote_mapping = json.load(quote_reader)

    if args[0] == 'add':
        if args[1] == '' or args[2] == '' or len(args) > 3:
            return "Arguments to quote command must be in form '!quote add <name> <quote>"
        else:
            quote_mapping[args[1]] = args[2]
            with open('data/quotes.json', 'w') as quote_writer:
                json.dump(quote_mapping, quote_writer)
            return "Quote sucessfully added"
    elif args[0] == 'delete' or args[0] == "del" or args[0] == "remove" or args[0] == "rm" :
        if args[1] == '' or len(args) > 2:
            return "Arguments to quote command must be in form '!quote remove <name>"
        else: 
            del quote_mapping[args[1]]
            with open('data/quotes.json', 'w') as quote_writer:
                json.dump(quote_mapping, quote_writer)
            return "Quote sucessfully removed"
    elif args[0] == 'random' or args[0] == 'rand' or args[0] == '':
        keys = list(quote_mapping.keys())
        return quote_mapping.get(keys[np.random.randint(0, len(keys))])
    elif args[0] == "list" or args[0] == "ls":
        keys = list(quote_mapping.keys())
        return "\n".join([", ".join([key for key in chunk]) for chunk in helpers.chunks(keys, 5)] )
    else:
        return quote_mapping.get(args[0], "Please specify a quote to show")
    


def docker_handler(args):

    return docker_commands.execute_command(args[0], args[1:])