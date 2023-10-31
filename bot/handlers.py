import requests

import docker
import bot.helpers as helpers

client = docker.from_env()

async def pong(message):
    await message.channel.send("Pong!")

async def get_servers(message):

    result_string: str = "## IP: \nInternal: 192.168.86.62\n"

    result = requests.get("https://ifconfig.me/ip")

    if result.status_code == 200:
        result_string = "External: %s" % result.text.strip()
    else:
        result_string = "Error retrieving: [%d] %s" % (result.status_code, result.reason)


    docker_info = helpers.get_docker_port_info(client)

    await message.channel.send("%s\n%s" % (result_string, docker_info))

def get_pattern_mappings():
    mappings = dict()

    mappings["ping"] = pong
    mappings["servers"] = get_servers

    return mappings