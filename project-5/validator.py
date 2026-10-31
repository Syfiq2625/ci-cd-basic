def validate_columns(columns):
    required_columns = ["name", "email", "age"]

    for column in required_columns:
        if column not in columns:
            return False

    return True


def validate_name(name):
    if not name or not name.strip():
        return False

    return True


def validate_email(email):
    if not email or " " in email:
        return False

    if "@" not in email:
        return False

    parts = email.split("@")

    if len(parts) != 2:
        return False

    username, domain = parts

    if not username or not domain:
        return False

    if "." not in domain:
        return False

    return True


def validate_age(age):
    try:
        age = int(age)

        if age < 18:
            return False

        return True

    except ValueError:
        return False