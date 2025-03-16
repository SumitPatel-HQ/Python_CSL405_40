import re

def extract_critical_errors(log_data: str) -> list[tuple]:
    pattern = re.compile(
        r"""
        ^\[(?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\]\s+
        \[ERROR\]\s+
        \[(?P<module>[A-Za-z0-9_]+)\]\s+
        (?P<msg>
            (?=.*\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)(?:\.
            (?:25[0-5]|2[0-4]\d|[01]?\d\d?)){3})\b)
            (?=.*\b0x[A-F0-9]{8}\b)
            .+
        )
        """, re.VERBOSE | re.MULTILINE
    )

    results = []
    
    for match in pattern.finditer(log_data):
        results.append((match.group("timestamp"), match.group("module"), match.group("msg").strip()))
        
    return results


log_data = """
[2025-02-10 14:23:01] [INFO] [Auth_Module] User login successful.
[2025-02-10 15:45:32] [ERROR] [Net_Module] Connection timeout from 192.168.1.10. Error Code: 0xAB12CD34
[2025-02-10 16:01:10] [WARN] [Disk_Module] Low disk space warning.
[2025-02-10 17:12:05] [ERROR] [Security_Module] Unauthorized access detected from 10.0.0.5. Error Code: 0xDEADBEEF
"""


extracted = extract_critical_errors(log_data)

print("$$$ Advanced Concept of Python $$$")
print("\nExtracted Critical Errors:")
for item in extracted:
    print(item)
