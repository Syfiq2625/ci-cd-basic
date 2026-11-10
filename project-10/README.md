# Project 10 - Pengenalan CD (Continuous Deployment) & CLI Tool

Proyek ini adalah aplikasi Command Line Interface (CLI) sederhana yang dibangun menggunakan library **Typer** (dibuat oleh kreator FastAPI). Proyek ini juga dilengkapi dengan generator dokumentasi statis, yaitu **MkDocs**.

## Tantangan CI/CD (`ci-project-10.yml`):

Ini adalah simulasi transisi dari sekadar CI (Integration) menuju **CD (Continuous Deployment)**. Buatlah workflow dengan struktur berikut:

1. **Job: Code Quality (`quality`)**
   - Gabungkan langkah `ruff`, `bandit`, dan `pip-audit` ke dalam satu job ini.
   
2. **Job: Testing (`test`)**
   - *Needs*: `quality`
   - Gunakan *Matrix Strategy* (misal Python 3.11, 3.12).
   - Jalankan `pytest --cov=src/sys_cli tests/ --cov-report=xml`.
   - **Tantangan Tertunda**: Kali ini, wajibkan dirimu untuk mencoba fitur **Artifacts** dengan mengunggah file `coverage.xml` menggunakan action `actions/upload-artifact@v4`.

3. **Job: Build Package (`build`)**
   - *Needs*: `test`
   - Sama seperti sebelumnya, jalankan `python -m build` dan validasi menggunakan `twine`.

4. **Job: Build & "Deploy" Documentation (`docs`)**
   - *Needs*: `test` (Berjalan paralel dengan job `build`, tidak perlu menunggu build selesai).
   - Install dependencies.
   - Jalankan perintah `mkdocs build`. Perintah ini akan menghasilkan folder baru bernama `site/` yang berisi file HTML statis dokumentasimu.
   - **Tantangan CD**: Unggah seluruh isi folder `site/` tersebut sebagai Artifact menggunakan `actions/upload-artifact@v4` dengan nama artifact `documentation-site`. 
   - *Catatan: Mengunggah folder `site/` ini mensimulasikan proses men-deploy website statis (seperti GitHub Pages).*
