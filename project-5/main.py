import csv
from validator import (
    validate_columns,
    validate_name,
    validate_email,
    validate_age
)


def validate_csv(file_path):
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            # Validasi kolom
            if not validate_columns(reader.fieldnames or []):
                print("ERROR: CSV memiliki kolom yang tidak lengkap.")
                return False

            has_error = False

            # Validasi setiap baris
            for row_number, row in enumerate(reader, start=2):
                errors = []

                if not validate_name(row["name"]):
                    errors.append("Nama tidak boleh kosong")

                if not validate_email(row["email"]):
                    errors.append("Format email tidak valid")

                if not validate_age(row["age"]):
                    errors.append("Usia harus berupa angka dan minimal 18")

                if errors:
                    has_error = True
                    print(f"Baris {row_number}: INVALID")
                    for error in errors:
                        print(f"  - {error}")
                else:
                    print(f"Baris {row_number}: VALID")

            if has_error:
                print("\nCSV memiliki data yang tidak valid.")
                return False

            print("\nSemua data CSV valid.")
            return True

    except FileNotFoundError:
        print(f"ERROR: File '{file_path}' tidak ditemukan.")
        return False


if __name__ == "__main__":
    validate_csv("data/users.csv")