import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def hello():
    console.print("[bold magenta] 🎵 Lofi Station[/bold magenta]")

if __name__ == "__main__":
    app()
