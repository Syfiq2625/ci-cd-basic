# Project 9 - CI/CD Level Up

Proyek ini adalah REST API sederhana menggunakan **FastAPI**, lengkap dengan *TestClient*. Tidak menggunakan database sungguhan (hanya *in-memory list*) dan tanpa Docker. 

Tujuannya adalah untuk melatih pembuatan *pipeline* CI yang lebih kompleks.

## Tantangan CI/CD (`ci-project-9.yml`):

Tugasmu adalah membuat *workflow* dengan **4 Jobs** yang saling berkaitan:

1. **Job 1: Linting (`lint`)**
   - Gunakan `ruff` untuk mengecek dan memformat kode di folder `src` dan `tests`.

2. **Job 2: Security Scan (`security`)**
   - Gunakan tools bernama **Bandit** (`bandit -r src/`).
   - *Bandit* berfungsi untuk mendeteksi celah keamanan pada kode Python.
   - Job ini **tidak** bergantung pada `lint`, jadi bisa berjalan **secara paralel** dengan Job 1.

3. **Job 3: Testing & Coverage (`test`)**
   - Berjalan HANYA JIKA `lint` dan `security` sukses (`needs: [lint, security]`).
   - Gunakan *Matrix Strategy* untuk Python 3.10 dan 3.12.
   - Jalankan *pytest* dengan mengecek *code coverage*: `pytest --cov=src/api tests/ --cov-report=xml`
   - **(Fitur Baru)**: Upload hasil coverage (`coverage.xml`) sebagai *Artifact* menggunakan GitHub Action `actions/upload-artifact@v4`. Ini biasa dipakai agar hasil tes bisa didownload atau dibaca oleh tools lain (seperti SonarQube/Codecov).

4. **Job 4: Build (`build`)**
   - Berjalan HANYA JIKA `test` sukses.
   - Karena `test` menggunakan *matrix*, kamu cukup mem-build pada satu versi Python saja (misal: 3.12).
   - Lakukan `python -m build` untuk memastikan proyek dapat di-paking (*packaged*) dengan baik.
