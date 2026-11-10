import typer
import platform

app = typer.Typer(help="System Utility CLI")

@app.command()
def ping(name: str = "Syafiq"):
    """Sapa pengguna dan pastikan CLI berjalan."""
    typer.echo(f"Pong! Halo, {name}!")

@app.command()
def sysinfo():
    """Tampilkan informasi sistem operasi dasar."""
    sys_name = platform.system()
    release = platform.release()
    typer.echo(f"OS: {sys_name}")
    typer.echo(f"Release: {release}")

if __name__ == "__main__":
    app()
