import click

try:
    from geccoi import GeccoiApp
    app = GeccoiApp()
except ModuleNotFoundError as err:
    click.echo(err)


@click.command(help="The Gecco")
@click.option("-s", "--start", "start", is_flag=True, help="Launches the Geccoi user interface")
@click.option("-d", "--debug", "debug", is_flag=True, help="Will turn debug mode on if launched.")
@click.option("--description", is_flag=True, help="Show the description of this interface.")
def cli(start, debug, description):
    if description:
        click.echo("GeCLI for interacting with the GeCCOI application.")
    if start:
        if debug:
            click.echo("GUI Process Started...")

        app.start_gui(debug)

        if debug:
            click.echo("GUI Closed")


if __name__ == '__main__':
    cli()
