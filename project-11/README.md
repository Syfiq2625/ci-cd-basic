# Project 11 - CI/CD Capstone (Schedule & Release)

Selamat! Ini adalah proyek terakhir sebelum kamu memasuki dunia Docker dan Containerization.

Proyek ini mensimulasikan sebuah *script* otomatis yang bertugas mengumpulkan data dan membuat laporan harian berbentuk JSON (`data_processor`).

## Tantangan Final CI/CD (`ci-project-11.yml`):

Untuk lulus dari tahap CI/CD dasar ini, kamu harus merancang *workflow* dengan dua jenis *trigger* baru: **Schedule (Cron)** dan **Tags**.

### 1. Trigger Tambahan
Selain `push`, `pull_request`, dan `workflow_dispatch`, tambahkan:
- `schedule`: Gunakan cron expression agar workflow berjalan otomatis (misalnya setiap jam 00:00).
- `push tags`: Atur agar workflow juga berjalan jika kamu melakukan push tag yang diawali huruf v (contoh: `v1.0.0`). *Hint: gunakan `tags: - 'v*'` di bagian push*.

### 2. Job 1: Quality & Test (`integrate`)
- Gabungkan pengecekan kode (`ruff`, `mypy`) dan `pytest` dalam satu job ini.
- Wajib menyimpan `coverage.xml` sebagai artifact.

### 3. Job 2: Nightly Report (`report`)
- *Needs*: `integrate`
- Job ini mensimulasikan eksekusi script di server.
- Jalankan perintah: `python src/data_processor/main.py`.
- Script tersebut akan membuat file JSON di dalam folder `data/`.
- Unggah seluruh folder `data/` sebagai Artifact bernama `daily-report`.

### 4. Job 3: GitHub Release (`release`)
- *Needs*: `integrate`
- **PENTING**: Job ini HANYA boleh berjalan jika workflow di-trigger oleh **Tag**. *Hint: gunakan kondisional `if: startsWith(github.ref, 'refs/tags/')` pada level job*.
- Lakukan build package: `python -m build`.
- Gunakan action pihak ketiga (misalnya `softprops/action-gh-release@v2`) untuk membuat **GitHub Release** secara otomatis dan melampirkan file `.whl` serta `.tar.gz` dari folder `dist/` ke dalam halaman *Release* repositorimu.

Semoga sukses! Setelah ini kamu siap menghadapi Docker!
