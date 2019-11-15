import click, logging
from tenable.io import TenableIO
from tenable.sc import TenableSC
from .plugins import plugin_loader
from . import __version__

@click.group()
@click.option('--tio-access-key',
    envvar='TIO_ACCESS_KEY', help='Tenable.io Access Key')
@click.option('--tio-secret-key',
    envvar='TIO_SECRET_KEY', help='Tenable.io Secret Key')
@click.option('--tsc-host',
    envvar='TSC_ADDRESS', help='Tenable.sc Address')
@click.option('--tsc-port', default=443,
    envvar='TSC_ADDRESS', help='Tenable.sc Port')
@click.option('--tsc-username', help='Tenable.sc Username')
@click.option('--tsc-password', help='Tenable.sc Password')
@click.option('--tsc-access-key',
    envvar='TSC_ACCESS_KEY', help='Tenable.sc Access Key')
@click.option('--tsc-secret-key',
    envvar='TSC_SECRET_KEY', help='Tenable.sc Secret Key')
@click.option('--verbose', '-v', envvar='VERBOSITY', default=0,
    count=True, help='Logging Verbosity')
@click.pass_context
def cli(ctx, verbose, tio_access_key, tio_secret_key, tsc_host, tsc_port,
        tsc_username, tsc_password, tsc_access_key, tsc_secret_key):
    '''
    Tenable Command-Line Interface (Tenable-CLI)
    '''
    # Setup the logging verbosity.
    log_fmt = '%(asctime)-15s %(message)s'
    if verbose == 0:
        logging.basicConfig(level=logging.WARNING, format=log_fmt)
    if verbose == 1:
        logging.basicConfig(level=logging.INFO, format=log_fmt)
    if verbose > 1:
        logging.basicConfig(level=logging.DEBUG, format=log_fmt)

    # Setup the context object
    ctx.ensure_object(dict)
    ctx.obj['tio'] = None
    ctx.obj['tsc'] = None

    # If the Tenable.io Secret Keys and Access Keys are passed, we will then
    # instantiate the TenableIO object
    if tio_access_key and tio_secret_key:
        ctx.obj['tio'] = TenableIO(
            access_key=tio_access_key,
            secret_key=tio_secret_key,
            vendor='Tenable',
            product='TenableCLI',
            build=__version__
        )

    # If the Tenable.sc parameters are specified with User Auth, then we will
    # instantiate the TenableSC object and login using user-auth.
    if tsc_host and tsc_port and tsc_username and tsc_password:
        ctx.obj['tsc'] = TenableSC(
            address=tsc_host,
            port=tsc_port,
            vendor='Tenable',
            product='TenableCLI',
            build=__version__
        )
        ctx.obj['tsc'].login(tsc_username, tsc_password)

    # if the Tenable.sc parameters are specified with API keys, then we will
    # instantiate the TenableSC object and use the API keys for keyed auth.
    elif tsc_host and tsc_port and tsc_access_key and tsc_secret_key:
        ctx.obj['tsc'] = TenableSC(
            address=tsc_host,
            port=tsc_port,
            access_key=tsc_access_key,
            secret_key=tsc_secret_key,
            vendor='Tenable',
            product='TenableCLI',
            build=__version__
        )

# Run the plugin-loader to link in all of the plugin commands into the
# commandline interface.
plugin_loader(cli)