from pathlib import Path

import pytest

from taskcli.cli import main


def run(tmp_path: Path, *args: str) -> int:
    return main(["--file", str(tmp_path / "tasks.json"), *args])


def test_add_and_list(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert run(tmp_path, "add", "Belajar GitHub Actions") == 0
    assert run(tmp_path, "list") == 0
    out = capsys.readouterr().out
    assert "Ditambahkan #1" in out
    assert "[ ] 1. Belajar GitHub Actions" in out


def test_list_empty(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert run(tmp_path, "list") == 0
    assert "Belum ada tugas." in capsys.readouterr().out


def test_done_marks_task(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    run(tmp_path, "add", "Tugas")
    assert run(tmp_path, "done", "1") == 0
    run(tmp_path, "list")
    assert "[x] 1. Tugas" in capsys.readouterr().out


def test_done_unknown_id_returns_error(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    assert run(tmp_path, "done", "42") == 1
    assert "Error" in capsys.readouterr().out


def test_remove_task(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    run(tmp_path, "add", "Sementara")
    assert run(tmp_path, "remove", "1") == 0
    run(tmp_path, "list")
    assert "Belum ada tugas." in capsys.readouterr().out


def test_add_empty_title_returns_error(tmp_path: Path) -> None:
    assert run(tmp_path, "add", "  ") == 1
