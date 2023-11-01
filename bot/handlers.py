import shlex
import requests

import docker
import bot.helpers as helpers
import numpy as np
import sys

client = docker.from_env()

def pong(args=None):
    return "Pong!"

def get_servers(args=None):

    result_string: str = "## IP: \nInternal: 192.168.86.62\n"

    result = requests.get("https://ifconfig.me/ip")

    if result.status_code == 200:
        result_string = "External: %s" % result.text.strip()
    else:
        result_string = "Error retrieving: [%d] %s" % (result.status_code, result.reason)


    docker_info = helpers.get_docker_port_info(client)

    return "%s\n%s" % (result_string, docker_info)

def random(*args):

    rands = helpers.rng(args).tolist()


    output = "\n".join([", ".join([str(n) for n in rng]) for rng in helpers.chunks(rands, 5)] )

    return output

def dice(*args):
    output = ""

    running_total = 0

    for arg in args:

        splits = arg.split("d") or arg.split("D")

        amount = splits[0]
        sides = splits[1]

        outcomes = np.array([outcome + 1 for outcome in helpers.rng("--max", sides, "--amount", amount)])

        total = outcomes.sum()

        running_total += total

        for i, outcome in enumerate(outcomes):
            output += f"d{sides} #{i+1}: {outcome}\n"

        output += f"d{sides} Total: {total}\n"

        output += "\n"
    
    output += f"Overall total: {running_total}"

    return output


def coin(*args):

    outcome = str(np.random.choice(["heads", "tails"])) 

    return "Outcome was %s.\nYou %s" % (outcome, "win!" if outcome.upper() == args[0].upper() else "lose.")

def help(*args):
    return """
    help: Displays this text

    servers: List of servers and their ports

    ping: Pings the bot and responds with 'Pong!'

    coin: <prediction>
          Simulates a coin flip and tells you if you won or lost based off your prediction
          example: `!coin Heads`

    rng or random: ( --digits <num_of_digits> or --min <min number> --max <max number> ) --amount <amount of #'s to generate>
                   examples: `!rng --digits 5`, `!random --min 0 --max 5 --amount 2`
                   
    dice: <list of dice combinations>
          Simulates dice rolls based off of listed dice
          examples: `!dice 1d6`, `!dice 1d4 1d6`
    """

def get_pattern_mappings():
    mappings = dict()

    mappings["ping"] = pong
    mappings["servers"] = get_servers
    mappings["random"] = random
    mappings["rng"] = random
    mappings["coin"] = coin
    mappings["help"] = help

    return mappings