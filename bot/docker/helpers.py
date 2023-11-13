import docker

client = docker.from_env()

def get_port_info():
    
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