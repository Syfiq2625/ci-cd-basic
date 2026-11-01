from datetime import datetime


def read_logs(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        logs = file.readlines()

    return [log.strip() for log in logs if log.strip()]


def count_logs(logs):
    return len(logs)


def count_by_level(logs, level):
    count = 0

    for log in logs:
        parts = log.split(" ", 3)

        if len(parts) == 4 and parts[2] == level:
            count += 1

    return count


def get_error_logs(logs):
    error_logs = []

    for log in logs:
        parts = log.split(" ", 3)

        if len(parts) == 4 and parts[2] == "ERROR":
            error_logs.append(log)

    return error_logs


def validate_log_format(log):
    parts = log.split(" ", 3)

    if len(parts) != 4:
        return False

    date, time, level, message = parts

    try:
        datetime.strptime(
            f"{date} {time}",
            "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        return False

    if level not in ["INFO", "WARNING", "ERROR"]:
        return False

    if not message.strip():
        return False

    return True