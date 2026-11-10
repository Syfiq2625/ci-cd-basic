from typer.testing import CliRunner
from src.sys_cli.main import app
import platform

runner = CliRunner()

def test_ping_default():
    result = runner.invoke(app, ["ping"])
    assert result.exit_code == 0
    assert "Pong! Halo, Syafiq!" in result.stdout

def test_ping_custom():
    result = runner.invoke(app, ["ping", "--name", "Admin"])
    assert result.exit_code == 0
    assert "Pong! Halo, Admin!" in result.stdout

def test_sysinfo():
    result = runner.invoke(app, ["sysinfo"])
    assert result.exit_code == 0
    assert platform.system() in result.stdout
