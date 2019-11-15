import click, json
from .io import io
from .sc import sc


@click.group()
@click.pass_context
def api(ctx):
    '''
    Raw API Interaction Commandset
    '''
    pass

api.add_command(io)
api.add_command(sc)