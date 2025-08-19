# Khaos Bot

A Docker based Discord bot that is designed to allow for users to create their own commands via a plugin system.

It is recommended to understand Docker before attempting to set this up.

## Discord Token

You can learn how to get a Discord Bot Token by following guides on the [Discord Developer guide site](https://discord.com/developers)

The Discord token can be passed in one of two ways.

### Secrets

#### Docker Swarm Secrets

- Create a secret using `docker secret create` (see the help for the command on information on how to do this)
- Pass this in using a deploy file for Docker Swarm (see Docker Swarm example at bottom of readme)

#### Environment Variables

- Set the environment variable ` in the docker container to your Discord token
  - Using the Docker CLI that looks like this `docker run -e DISCORD_TOKEN=<your-token-here> deuce109/khaos-bot`
  - See an example using Docker compose at the bottom of this readme

## Volumes

In order to load plugins you will need to mount a Docker volume to the container.

Using the Docker CLI that looks like this `docker run -v ./data:/opt/khaos-bot deuce109/khaos-bot`. This will mount `<your-current-directory>/data` to `/opt/khaos-bot` inside the container.

## Environment Variables

- `BOT_COMMAND_PREFIX` Sets the prefix for the bot to recognize for commands (default: `!`)
- `DISCORD_TOKEN` Set this to pass the Discord Bot Token by environment variable
- `PACKAGE_LIST` Path to extra OS packages in case of necessity for third party libraries (default: `/opt/khaos-bot/plugins/packages.txt`)

## Plugins

### Builtin Plugins

- `help` Lists the available commands
- `reload` Attempts to find new pluings in the specified plugin folder, does not reload libraries or packages

### Installing Plugins

In order to install plugins you will need to add them to `/opt/khaos-bot/plugins`. If using the above command this path will be `./data/plugins`.

After updating any file under the plugins folder you will need to restart the bot in order to get the updates.

### Basic Plugins

Some basic default plugins are available at https://github.com/deuce109/khaos-bot-plugins

### Custom Plugins

Building custom plugins is made to be as simple as possible.

Plugins need to be a Python script that have the following 2 attributes at a minimum:

- `COMMAND` The name of the command for the bot to listen to
- `execute` This should be a function that accepts a list of strings as arguments and returns a string that will be the message the bot will reply with

Some examples can be seen at https://github.com/deuce109/khaos-bot-plugins

If extra third party Python libraries are needed add them to `/opt/khaos-bot/plugins/requirements.txt`

If extra third party OS libraries are needed add them ot `/opt/khaos-bot/plugins/packages.txt`

### Setup Examples

#### Docker Swarm

```yaml
services:
  khaos-bot:
    image: deuce109/khaos-bot:latest
    volumes:
    - ./data:/opt/khaos-bot
    secrets:
      - discord-bot-token

secrets:
  discord-bot-token:
    external: true
```

#### Docker Compose

```yaml
services:
  khaos-bot:
    image: deuce109/khaos-bot:latest
    volumes:
    - ./data:/opt/khaos-bot
    environment:
    - DISCORD_TOKEN=<your-discord-token-here>
    - BOT_COMMAND_PREFIX="#"
```

## Supporting

If you want to support development of this bot you can do so in a few ways

### Donation

Kofi - https://ko-fi.com/deuce109
Patreon - https://www.patreon.com/c/deuce109

### Development

If you would like to contribute to Khaos Bot then you will need the latest version of python available at https://www.python.org/downloads/
