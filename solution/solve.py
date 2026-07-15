import json
import re
from collections import Counter
from pathlib import Path


LOG_PATH = Path("/app/access.log")
REPORT_PATH = Path("/app/report.json")
REQUEST_PATTERN = re.compile(r'"\S+\s+(\S+)\s+HTTP/\d+(?:\.\d+)?"')


def main() -> None:
    path_counts: Counter[str] = Counter()
    client_ips: set[str] = set()
    total_requests = 0

    with LOG_PATH.open("r", encoding="utf-8") as log_file:
        for raw_line in log_file:
            line = raw_line.strip()
            if not line:
                continue

            fields = line.split()
            if not fields:
                continue

            match = REQUEST_PATTERN.search(line)
            if match is None:
                raise ValueError(f"Malformed request field: {line}")

            total_requests += 1
            client_ips.add(fields[0])
            path_counts[match.group(1)] += 1

    if not path_counts:
        raise ValueError("The access log contains no request targets")

    top_path, _ = path_counts.most_common(1)[0]
    report = {
        "total_requests": total_requests,
        "unique_ips": len(client_ips),
        "top_path": top_path,
    }

    REPORT_PATH.write_text(
        json.dumps(report, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
