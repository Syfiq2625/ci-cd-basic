from log_analyzer import (
    read_logs,
    count_logs,
    count_by_level,
    get_error_logs,
    validate_log_format
)


def main():
    file_path = "data/server.log"

    try:
        logs = read_logs(file_path)

        print("===== SERVER LOG ANALYZER =====\n")

        # Total logs
        print(f"Total Logs: {count_logs(logs)}")

        # Logs by level
        print(f"INFO: {count_by_level(logs, 'INFO')}")
        print(f"WARNING: {count_by_level(logs, 'WARNING')}")
        print(f"ERROR: {count_by_level(logs, 'ERROR')}")

        # Error logs
        print("\n===== ERROR LOGS =====")

        error_logs = get_error_logs(logs)

        if error_logs:
            for log in error_logs:
                print(log)
        else:
            print("No error logs found.")

        # Validate log format
        print("\n===== LOG FORMAT VALIDATION =====")

        valid_count = 0
        invalid_count = 0

        for log in logs:
            if validate_log_format(log):
                valid_count += 1
            else:
                invalid_count += 1

        print(f"Valid Logs: {valid_count}")
        print(f"Invalid Logs: {invalid_count}")

        print("\n===== ANALYSIS COMPLETED =====")

    except FileNotFoundError:
        print(f"ERROR: File '{file_path}' not found.")


if __name__ == "__main__":
    main()