import typer
from src.commands import Initialise
from src.commands.exceptions import WorkingDirNotExists

app = typer.Typer(no_args_is_help=True)


@app.command()
def init(
    working_directory: str,
    create_wd: bool = typer.Option(
        False,
        "--create-wd",
        help="Create the working directory if it doesn't exist"
    )
):
    """Initialize a new project"""
    process = Initialise(working_directory, create_wd)

    try:
        process.run()
    except WorkingDirNotExists as e:
        typer.echo(
            f"Error: {e}\n"
            "Use --create-wd to create it",
            err=True
        )
        raise typer.Exit(code=1)


@app.command()
def generate(name: str):
    """Generate a new MVC stack for `name`"""
    print(name)
