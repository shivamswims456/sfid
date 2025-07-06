import sys
from sonyflake import SonyFlake
from datetime import datetime, timezone

print(SonyFlake(
    start_time=datetime(1970, 1, 1, 0, 0, 0).replace(tzinfo=timezone.utc),
    machine_id=lambda: None if len(sys.argv) != 2 else int(sys.argv[1])
).next_id())
