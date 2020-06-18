import click, os

try:
    from geccoi import GeccoiApp
    app = GeccoiApp()
    module_required = None

except ModuleNotFoundError as err:
    module_required = str(err).strip("No module named ").strip("'")


@click.group()
@click.option("--name", is_flag=True)
def cli(name):
    if name:
        click.echo("GeCLI for interacting with the GeCCOI application.")


@click.command()
@click.option("-s", "--start", "start", is_flag=True)
@click.option("-q", "--quit", "quit", is_flag=True)
@click.option("-d", "--debug", "debug", is_flag=True)
def ai(start, quit, debug):
    if start is True and quit is True:
        raise ValueError("Option -s/--start cannot be used with -q/--quit")

    if start:
        if debug:
            click.echo("AI Process Started")

    if quit:
        if debug:
            click.echo("AI Process Quit")


@click.command()
@click.option("-s", "--start", "start", is_flag=True)
@click.option("-d", "--debug", "debug", is_flag=True)
def gui(start, debug):
    if start:
        if debug:
            click.echo("GUI Process Started...")

        app.start_gui(debug)

        if debug:
            click.echo("GUI Closed")


cli.add_command(ai)
cli.add_command(gui)


if __name__ == '__main__':
    try:
        cli()
    except NameError:
        for package in ["PySimpleGUI", "keyboard", "mouse", "opencv-python", "numpy", "click"]:
            if package == "opencv-python":
                package = "https://github.com/opencv/opencv/archive/4.3.0.tar.gz"

            os.system("pip install %s" % package)


