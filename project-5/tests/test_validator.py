import pytest

from validator import (
    validate_columns,
    validate_name,
    validate_email,
    validate_age
)


# Test validate_columns
def test_validate_columns_valid():
    assert validate_columns(["name", "email", "age"]) is True


def test_validate_columns_missing():
    assert validate_columns(["name", "email"]) is False


# Test validate_name
def test_validate_name_valid():
    assert validate_name("Andi") is True


def test_validate_name_empty():
    assert validate_name("") is False


def test_validate_name_whitespace():
    assert validate_name("   ") is False


# Test validate_email
def test_validate_email_valid():
    assert validate_email("andi@example.com") is True


def test_validate_email_missing_at():
    assert validate_email("andi-example.com") is False


def test_validate_email_missing_domain():
    assert validate_email("andi@") is False


def test_validate_email_with_space():
    assert validate_email("andi @example.com") is False


# Test validate_age
def test_validate_age_valid():
    assert validate_age("21") is True


def test_validate_age_below_minimum():
    assert validate_age("17") is False


def test_validate_age_invalid():
    assert validate_age("abc") is False