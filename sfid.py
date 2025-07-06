import sys
from sonyflake import SonyFlake
from datetime import datetime, timedelta, timezone

print(SonyFlake(
    start_time=datetime(1998, 3, 27, 13, 56, 00).replace(tzinfo=timezone(timedelta(hours=5, minutes=30))),
    machine_id=lambda: None if len(sys.argv) != 2 else int(sys.argv[1])
).next_id())
