# project-7: taskcli

CLI Python sederhana untuk mengelola daftar tugas (disimpan di file JSON).
Project ini dibuat sebagai bahan latihan membuat CI di GitHub Actions.

## Menjalankan secara lokal

```bash
cd project-7
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pip install -e .
```

Contoh pemakaian:

```bash
taskcli add "Belajar CI"
taskcli list
taskcli done 1
taskcli remove 1
```

Lokasi penyimpanan default `~/.taskcli.json`, bisa diganti dengan `--file`
atau variabel environment `TASKCLI_FILE`.

## Perintah yang dipakai di CI

| Tujuan | Perintah |
| --- | --- |
| Lint | `ruff check .` |
| Cek format | `ruff format --check .` |
| Type check | `mypy` |
| Test + coverage | `pytest` |
| Build package | `python -m build` |

Semua perintah dijalankan dari dalam folder `project-7`.

## Ide latihan CI

1. Workflow dasar: checkout, setup-python, install dependency, jalankan pytest.
2. Matrix: uji di Python 3.10, 3.11, 3.12, dan 3.13.
3. Cache pip dengan `actions/setup-python` (`cache: pip`).
4. Pisahkan job lint, type check, dan test, lalu atur dengan `needs`.
5. Hanya jalan saat folder ini berubah (`paths: ["project-7/**"]`).
6. Upload hasil coverage atau hasil build sebagai artifact.
7. Tambahkan `workflow_dispatch` dan jadwal dengan `schedule`.
8. Tambahkan status badge di README.
