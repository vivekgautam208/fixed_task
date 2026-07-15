import json
from pathlib import Path
from typing import Any


REPORT_PATH = Path("/app/report.json")
REQUIRED_KEYS = {"total_requests", "unique_ips", "top_path"}


def _read_report() -> Any:
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def test_report_format_and_schema() -> None:
    """
    Verifies instruction.md success criterion 1: /app/report.json exists as
    valid UTF-8 JSON, contains a JSON object, and has exactly the three
    required keys with no additional keys.
    """
    assert REPORT_PATH.is_file(), "/app/report.json was not created"

    try:
        report = _read_report()
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise AssertionError(
            "/app/report.json must be valid UTF-8 JSON"
        ) from exc

    assert isinstance(report, dict), (
        "/app/report.json must contain a JSON object"
    )
    assert set(report) == REQUIRED_KEYS, (
        "/app/report.json must contain exactly total_requests, "
        "unique_ips, and top_path"
    )


def test_total_requests() -> None:
    """
    Verifies instruction.md success criterion 2: total_requests is an integer
    equal to the number of non-empty request lines in /app/access.log.
    """
    report = _read_report()

    assert type(report["total_requests"]) is int, (
        "total_requests must be an integer"
    )
    assert report["total_requests"] == 6, (
        "total_requests must equal 6"
    )


def test_unique_ips() -> None:
    """
    Verifies instruction.md success criterion 3: unique_ips is an integer equal
    to the number of distinct first-field client IP addresses in /app/access.log.
    """
    report = _read_report()

    assert type(report["unique_ips"]) is int, (
        "unique_ips must be an integer"
    )
    assert report["unique_ips"] == 3, (
        "unique_ips must equal 3"
    )


def test_top_path() -> None:
    """
    Verifies instruction.md success criterion 4: top_path is a string equal to
    the uniquely most frequent request target in /app/access.log.
    """
    report = _read_report()

    assert isinstance(report["top_path"], str), (
        "top_path must be a string"
    )
    assert report["top_path"] == "/index.html", (
        "top_path must equal /index.html"
    )
