# Project 8 - CI Learning

Proyek ini dirancang tanpa database dan Docker, namun memiliki struktur yang cocok untuk melatih pembuatan CI/CD tingkat lanjut di GitHub Actions.

## Tantangan Pembuatan CI untuk Syafiq:

Buatlah `ci-project-8.yml` dengan skenario berikut:

1. **Job 1: Linting**
   - Gunakan `flake8 src tests` untuk mengecek kualitas kode.
2. **Job 2: Testing (Matrix Strategy)**
   - Jalankan `pytest tests/`.
   - Gunakan `strategy.matrix` untuk mengetes di beberapa versi Python sekaligus (misalnya `3.10`, `3.11`, `3.12`) atau bahkan beda OS (`ubuntu-latest`, `windows-latest`).
   - Buat job ini *depends on* (`needs:`) Job Linting.
3. **Job 3: Build**
   - Jalankan perintah `python -m build` untuk mem-build proyek menjadi package `.tar.gz` dan `.whl`.
   - Buat job ini *depends on* (`needs:`) Job Testing.
4. **Caching**
   - Implementasikan *dependency caching* menggunakan `actions/cache` atau fitur cache bawaan dari `actions/setup-python` agar instalasi dari `requirements.txt` lebih cepat pada run berikutnya.
