import json
import subprocess
import docker
import bot.helpers as helpers
import pandas as pd
from io import StringIO

def from_env():
    return docker.from_env()

def ps(client, _):
    containers = client.containers.list(all=True)

    data = '"Container Name",Image,Created,Status\n'

    for container in containers:
        name = container.attrs.get("Name").replace("/", "", 1)
        image = container.attrs.get("Config").get("Image")

        created_time_string = container.attrs.get("Created")[:-3] + "+0000"

        created = created_time_string
        status = container.attrs.get("State").get("Status")
        data += f'"{name}","{image}","{created}","{status}"\n'

    string_reader = StringIO(data)

    return "# Docker Ouput\n"+pd.read_csv(string_reader).to_string(index=False, )

def start(client: docker.DockerClient, args):

    container = client.containers.get(args[1])
    container.start()

def stop(client: docker.DockerClient, args):

    container = client.containers.get(args[1])
    container.stop()

def restart(client: docker.DockerClient, args):

    container = client.containers.get(args[1])
    container.restart()

def compose_register(args):
    with open('./data/docker_registry.json', "r+") as registry:

        json_string = registry.read()

        if json_string != "":
            registry_list = json.loads(json_string)
        else:
            registry_list = []

        if args[0] not in [item["name"] for item in registry_list]:

            registry_list.append({
                "name": args[0],
                "path": args[1]
            })

            json.dump(registry_list, registry)

    return f"Successfully registered {args[0]}"

def compose_up(args):
    with open('data/docker_registry.json') as registry:
        registry_listing = [item for item in json.load(registry) if item["name"] == args[0]][0]
    
    command_output = subprocess.check_output(['docker','compose','--file', registry_listing['path'], 'up', '-d'])

    return command_output

def compose_down(args):
    with open('data/docker_registry.json') as registry:
        registry_listing = [item for item in json.load(registry) if item["name"] == args[0]][0]
    
    command_output = subprocess.check_output(['docker','compose','--file', registry_listing['path'], 'down'])

    return command_output

def compose_restart(args):
    with open('data/docker_registry.json') as registry:
        registry_listing = [item for item in json.load(registry) if item["name"] == args[0]][0]
    
    command_output = subprocess.check_output(['docker','compose','--file', registry_listing['path'], 'restart'])

    return command_output

def compose(_, args):

    if args[1] == 'up':
        compose_up(args[2:])
    elif args[1] == 'down':
        compose_down(args[2:])
    elif args[1] == 'register':
        compose_register(args[2:])
    elif args[1] == 'restart':
        compose_restart(args[2:])
    