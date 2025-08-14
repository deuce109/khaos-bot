# Khaos Bot

A Docker based Discord bot that is designed to do nothing by default but allow for users to create their own commands via a plugin system.


## Volumes
In order to load plugins you will need to mount a Docker volume to the container.

Using the Docker CLI that looks like this `docker run -v ./data:/etc/khaos-bot deuce109/khaos-bot`

## Plugins

### Installing Plugins
In order to install plugins you will need to add them to `/etc/khaos-bot/plugins`. If using the above command this path will be `./data/plugins`.

### Basic Plugins
Some basic default plugins are available at https://github.com/deuce109/khaos-bot/plugins

### Custom Plugins
Building custom plugins is made to be as simple as possible.

Plugins need to be a Python script that have the following 2 attributes at a minimum:
- `COMMAND` The name of the command for the bot to listen to
- `exec` This should be a function that accepts a list of strings as arguments and returns a string that will be the message the bot will reply with

Some examples can be seen at https://github.com/deuce109/khaos-bot/plugins
