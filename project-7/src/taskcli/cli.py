"""Antarmuka command line untuk taskcli."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from taskcli import __version__
from taskcli.storage import TaskNotFoundError, TaskStore


def default_path() -> Path:
    env = os.environ.get("TASKCLI_FILE")
    if env:
        return Path(env)
    return Path.home() / ".taskcli.json"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="taskcli", description="Pengelola daftar tugas sederhana"
    )
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument(
        "--file", type=Path, default=None, help="Lokasi file JSON penyimpanan"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="Tambah tugas baru")
    add.add_argument("title", help="Judul tugas")

    sub.add_parser("list", help="Tampilkan semua tugas")

    done = sub.add_parser("done", help="Tandai tugas selesai")
    done.add_argument("id", type=int, help="ID tugas")

    rm = sub.add_parser("remove", help="Hapus tugas")
    rm.add_argument("id", type=int, help="ID tugas")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    store = TaskStore(args.file or default_path())

    try:
        if args.command == "add":
            task = store.add(args.title)
            print(f"Ditambahkan #{task.id}: {task.title}")
        elif args.command == "list":
            tasks = store.load()
            if not tasks:
                print("Belum ada tugas.")
            for task in tasks:
                mark = "x" if task.done else " "
                print(f"[{mark}] {task.id}. {task.title}")
        elif args.command == "done":
            task = store.complete(args.id)
            print(f"Selesai #{task.id}: {task.title}")
        elif args.command == "remove":
            store.remove(args.id)
            print(f"Dihapus #{args.id}")
    except (TaskNotFoundError, ValueError) as exc:
        print(f"Error: {exc}")
        return 1
    return 0
