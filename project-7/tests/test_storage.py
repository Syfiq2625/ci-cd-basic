from pathlib import Path

import pytest

from taskcli.storage import TaskNotFoundError, TaskStore


@pytest.fixture
def store(tmp_path: Path) -> TaskStore:
    return TaskStore(tmp_path / "tasks.json")


def test_load_returns_empty_when_file_missing(store: TaskStore) -> None:
    assert store.load() == []


def test_add_assigns_incrementing_ids(store: TaskStore) -> None:
    first = store.add("Satu")
    second = store.add("Dua")
    assert (first.id, second.id) == (1, 2)


def test_add_strips_whitespace(store: TaskStore) -> None:
    assert store.add("  Rapikan  ").title == "Rapikan"


def test_add_rejects_empty_title(store: TaskStore) -> None:
    with pytest.raises(ValueError):
        store.add("   ")


def test_complete_marks_task_done(store: TaskStore) -> None:
    task = store.add("Selesaikan")
    store.complete(task.id)
    assert store.load()[0].done is True


def test_complete_unknown_id_raises(store: TaskStore) -> None:
    with pytest.raises(TaskNotFoundError):
        store.complete(99)


def test_remove_deletes_task(store: TaskStore) -> None:
    task = store.add("Hapus aku")
    store.remove(task.id)
    assert store.load() == []


def test_remove_unknown_id_raises(store: TaskStore) -> None:
    with pytest.raises(TaskNotFoundError):
        store.remove(99)
