Read the Apache-style access log at `/app/access.log` and create `/app/report.json`.

The output must satisfy these success criteria:

1. `/app/report.json` must exist as valid UTF-8 JSON. Its top-level value must be an object containing exactly the keys `total_requests`, `unique_ips`, and `top_path`, with no additional keys.

2. `total_requests` must be an integer equal to the number of non-empty request lines in `/app/access.log`.

3. `unique_ips` must be an integer equal to the number of distinct client IP addresses. The client IP address is the first whitespace-separated field of each non-empty log line.

4. `top_path` must be a string equal to the uniquely most frequent request target in `/app/access.log`. The request target is the value between the HTTP method and HTTP version inside the quoted request field. The supplied access log has one uniquely most frequent request target.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
