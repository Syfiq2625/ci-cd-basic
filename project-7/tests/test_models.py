from taskcli.models import Task


def test_task_defaults_to_not_done() -> None:
    task = Task(id=1, title="Belajar CI")
    assert task.done is False


def test_task_roundtrip_dict() -> None:
    task = Task(id=2, title="Tulis test", done=True)
    assert Task.from_dict(task.to_dict()) == task


def test_from_dict_without_done_field() -> None:
    task = Task.from_dict({"id": 3, "title": "Tanpa done"})
    assert task.done is False
