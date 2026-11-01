import pytest

from log_analyzer import (
    read_logs,
    count_logs,
    count_by_level,
    get_error_logs,
    validate_log_format
)


# Test read_logs
def test_read_logs(tmp_path):
    file = tmp_path / "server.log"
    file.write_text(
        "2026-11-01 08:00:00 INFO Server started\n"
        "2026-11-01 08:05:00 ERROR Connection failed\n",
        encoding="utf-8"
    )

    logs = read_logs(file)

    assert len(logs) == 2
    assert logs[0] == "2026-11-01 08:00:00 INFO Server started"


def test_read_logs_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_logs("data/not_found.log")


# Test count_logs
def test_count_logs():
    logs = [
        "2026-11-01 08:00:00 INFO Server started",
        "2026-11-01 08:05:00 ERROR Connection failed",
        "2026-11-01 08:10:00 WARNING High memory usage"
    ]

    assert count_logs(logs) == 3


def test_count_logs_empty():
    assert count_logs([]) == 0


# Test count_by_level
def test_count_by_level_info():
    logs = [
        "2026-11-01 08:00:00 INFO Server started",
        "2026-11-01 08:05:00 INFO User logged in",
        "2026-11-01 08:10:00 ERROR Connection failed"
    ]

    assert count_by_level(logs, "INFO") == 2


def test_count_by_level_error():
    logs = [
        "2026-11-01 08:00:00 INFO Server started",
        "2026-11-01 08:05:00 ERROR Connection failed",
        "2026-11-01 08:10:00 ERROR Request timeout"
    ]

    assert count_by_level(logs, "ERROR") == 2


def test_count_by_level_not_found():
    logs = [
        "2026-11-01 08:00:00 INFO Server started"
    ]

    assert count_by_level(logs, "ERROR") == 0


# Test get_error_logs
def test_get_error_logs():
    logs = [
        "2026-11-01 08:00:00 INFO Server started",
        "2026-11-01 08:05:00 ERROR Connection failed",
        "2026-11-01 08:10:00 WARNING High memory usage"
    ]

    errors = get_error_logs(logs)

    assert len(errors) == 1
    assert errors[0] == "2026-11-01 08:05:00 ERROR Connection failed"


def test_get_error_logs_empty():
    assert get_error_logs([]) == []


# Test validate_log_format
def test_validate_log_format_valid():
    log = "2026-11-01 08:00:00 INFO Server started"

    assert validate_log_format(log) is True


def test_validate_log_format_invalid_date():
    log = "2026-13-01 08:00:00 INFO Server started"

    assert validate_log_format(log) is False


def test_validate_log_format_invalid_level():
    log = "2026-11-01 08:00:00 DEBUG Server started"

    assert validate_log_format(log) is False


def test_validate_log_format_missing_message():
    log = "2026-11-01 08:00:00 ERROR"

    assert validate_log_format(log) is False


def test_validate_log_format_invalid_structure():
    log = "Server started"

    assert validate_log_format(log) is False