from .api import api

def plugin_loader(group):
    group.add_command(api)