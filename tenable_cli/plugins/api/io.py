from pprint import pprint
import click, json


@click.group()
@click.pass_context
def io(ctx):
    '''
    Tenable.io Raw API Interaction commandset
    '''
    pass


@io.command()
@click.argument('path')
@click.option('--params', '-p',
    help='Pass a Query Parameter to the API')
@click.pass_context
def get(ctx, path, params):
    '''
    GET Call
    '''
    # ensuring that the params were passed as a JSON object:
    params = json.loads(params) if params else None

    # Fetching the TenableIO object
    tio = ctx.obj['tio']

    # Making the call and printing the output w/ pprint
    pprint(tio.get(path, params=params).json())


@io.command()
@click.argument('path')
@click.option('--params', '-p',
    help='Pass a Query Parameter to the API')
@click.option('--data', '-d',
    help='Pass a JSON Object to the API in the body')
@click.pass_context
def post(ctx, path, params, data):
    '''
    POST Call
    '''
    # ensuring that params and data were passed as JSON objects:
    params = json.loads(params) if params else None
    data = json.loads(data) if params else None

    # Fetching the TenableIO object
    tio = ctx.obj['tio']

    # Making the call and printing the output w/ pprint
    pprint(tio.post(path, params=params, json=data).json())


@io.command()
@click.argument('path')
@click.option('--params', '-p',
    help='Pass a Query Parameter to the API')
@click.option('--data', '-d',
    help='Pass a JSON Object to the API in the body')
@click.pass_context
def put(ctx, path, params, data):
    '''
    PUT Call
    '''
    # ensuring that params and data were passed as JSON objects:
    params = json.loads(params) if params else None
    data = json.loads(data) if params else None

    # Fetching the TenableIO object
    tio = ctx.obj['tio']

    # Making the call and printing the output w/ pprint
    pprint(tio.put(path, params=params, json=data).json())


@io.command()
@click.argument('path')
@click.option('--params', '-p',
    help='Pass a Query Parameter to the API')
@click.option('--data', '-d',
    help='Pass a JSON Object to the API in the body')
@click.pass_context
def delete(ctx, path, params, data):
    '''
    DELETE Call
    '''
    # ensuring that params and data were passed as JSON objects:
    params = json.loads(params) if params else None
    data = json.loads(data) if params else None

    # Fetching the TenableIO object
    tio = ctx.obj['tio']

    # Making the call and printing the output w/ pprint
    pprint(tio.delete(path, params=params, json=data).json())