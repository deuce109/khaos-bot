import glob
import os
import importlib
import logging
import sys
from discord import Attachment
from typing import Callable, Optional

DEFAULT_PLUGINS: dict[str, Callable[[list[str], list[Attachment]], str]] = {
    "help": lambda _, __: help_exec(),
    "reload": lambda _, __: load_plugins()
}


plugins: dict[str, Callable[[list[str], list[Attachment]], str]] = {}

def help_exec() -> str:
    return "Available commands: " + ", ".join(plugins.keys())

def search_for_plugins(path: str = "/app/bot/plugins") -> list[str]:
    modules = []
    
    file_path = os.path.abspath(path)
    
    glob_path = os.path.join(file_path, "*.py")
    
    logging.info(f"Searching for plugins in {glob_path}")
    
    
    for file in glob.glob(glob_path):
        module_name = os.path.basename(file)[:-3]
        if module_name != "__init__":
            try:
                importlib.import_module(f"bot.plugins.{module_name}", "bot.plugins")
                modules.append(module_name)
            except Exception as e:
                logging.warning(f"Could not load plugin {module_name}: {e}")
                
    return modules
            
        
def get_plugins(modules: list[str]):
    global plugins
    plugins = DEFAULT_PLUGINS
    for module_name in modules:
        module_path = f"bot.plugins.{module_name}"
        module = sys.modules.get(module_path)
        if module is None:
            logging.warning(f"Module {module_path} not found in sys.modules.")
            continue
        command_string = getattr(module, "COMMAND", None)
        excutable: Optional[Callable[[list[str], list[Attachment]], str]] = getattr(module, "execute", None)
        if command_string and excutable and callable(excutable):
            plugins[command_string] = excutable
            logging.info(f"Loaded plugin {module_name} as command {command_string}")
        else:
            logging.warning(f"Plugin {module_name} does not have a valid command or execute function.")
            
def load_plugins():
    modules = search_for_plugins()
    if not modules:
        logging.warning("No plugins discovered.")
        return "No plugins discovered."
    get_plugins(modules)
    if plugins:
        return f"Plugins loaded: {'\n'.join(plugins.keys())}"
    else:
        logging.warning("No plugins loaded.")
        return "No plugins loaded."
        
    
    
def exec_command(command: str, args: list[str], attachments: list[Attachment]) -> str:
    if command in plugins.keys():
        return plugins[command](args, attachments)
    else:
        logging.warning(f"Command {command} not found in plugins.")
        return f"Command '{command}' not found. Use '!help' to see available commands."