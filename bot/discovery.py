import glob
import os
import importlib
import logging
import sys
from typing import Callable, Optional

plugins: dict[str, Callable[[list[str]], str]] = {
    "help": lambda _: help_exec(),
}

def help_exec() -> str:
    return "Available commands: " + ", ".join(plugins.keys())

def search_for_plugins(path: str = "/etc/ip-bot/plugins") -> list[str]:
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
    for module_name in modules:
        module_path = f"bot.plugins.{module_name}"
        module = sys.modules.get(module_path)
        if module is None:
            logging.warning(f"Module {module_path} not found in sys.modules.")
            continue
        command_string = getattr(module, "COMMAND", None)
        excutable: Optional[Callable[[list[str]], str]] = getattr(module, "exec", None)
        if command_string and excutable and callable(excutable):
            plugins[command_string] = excutable
            logging.info(f"Loaded plugin {module_name} as command {command_string}")
        else:
            logging.warning(f"Plugin {module_name} does not have a valid command or exec function.")
            
def load_plugins():
    modules = search_for_plugins()
    if not modules:
        logging.warning("No plugins found.")
        return
    get_plugins(modules)
    if not plugins:
        logging.warning("No valid plugins found.")
    
    
def exec_command(command: str, args: list[str]) -> str:
    if command in plugins.keys():
        return plugins[command](args)
    else:
        logging.warning(f"Command {command} not found in plugins.")
        return f"Command '{command}' not found. Use '!help' to see available commands."
    
load_plugins()