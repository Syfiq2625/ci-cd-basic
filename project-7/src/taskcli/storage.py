"""Penyimpanan tugas ke file JSON."""

from __future__ import annotations

import json
from pathlib import Path

from taskcli.models import Task


class TaskNotFoundError(Exception):
    """Dilempar saat id tugas tidak ditemukan."""


class TaskStore:
    """Membaca dan menulis daftar tugas dari/ke file JSON."""

    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> list[Task]:
        if not self.path.exists():
            return []
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        return [Task.from_dict(item) for item in raw]

    def save(self, tasks: list[Task]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = [task.to_dict() for task in tasks]
        self.path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def add(self, title: str) -> Task:
        title = title.strip()
        if not title:
            raise ValueError("Judul tugas tidak boleh kosong")
        tasks = self.load()
        next_id = max((task.id for task in tasks), default=0) + 1
        task = Task(id=next_id, title=title)
        tasks.append(task)
        self.save(tasks)
        return task

    def complete(self, task_id: int) -> Task:
        tasks = self.load()
        for task in tasks:
            if task.id == task_id:
                task.done = True
                self.save(tasks)
                return task
        raise TaskNotFoundError(f"Tugas dengan id {task_id} tidak ditemukan")

    def remove(self, task_id: int) -> None:
        tasks = self.load()
        remaining = [task for task in tasks if task.id != task_id]
        if len(remaining) == len(tasks):
            raise TaskNotFoundError(f"Tugas dengan id {task_id} tidak ditemukan")
        self.save(remaining)
