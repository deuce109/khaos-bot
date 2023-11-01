import shlex
import numpy as np

def get_docker_port_info(client):
    containers = client.containers.list()

    container_info = ""

    for container in containers:

        name = container.attrs.get("Config").get("Labels").get("SERVER_NAME")
        type = container.attrs.get("Config").get("Labels").get("SERVER_TYPE")
        port = container.attrs.get("Config").get("Labels").get("CONNECTION_PORT")

        if not name:
            continue

        if type:
            type = "Type: " + type

        if port:
            port = "Port: " + port
    
        container_info += "## %s\n%s\n%s\n" % (name, type, port)

    return container_info.strip()

def chunks(data, chunk_size=5):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def rng(*args):

    if args:
        
        if "--digits" in args:
            digits = int(args[args.index("--digits") + 1])

            min = int("-%s" % "".join(["9" for i in range(digits)]))
            max = int("%s" % "".join(["9" for i in range(digits)]))

        else:

            if "--min" in args:
                min = int(args[args.index("--min") + 1])
            else:
                min = 0
            
            if "--max" in args:
                max = int(args[args.index("--max") + 1])
            else:
                max = 100


        if "--amount" in args:
            amount = int(args[args.index("--amount") + 1])
        else:
            amount = 1

    else:
        min = 0
        max = 100
        amount = 1

    return np.random.randint( min, max, size=amount)
