import re
import datetime

simple_data = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

class Guard:
    def __init__(self, guard_id):
        self.id = guard_id
        self.asleep_minutes = 0
        self.sleep_calendar = [0] * 60
        self.sleep_start = None
        self.sleep_end = None

    def __repr__(self):
        return f"{self.id}: {self.asleep_minutes} minutes. Most common sleep minute: {self.most_common_sleep_minute()}"

    @staticmethod
    def __to_datetime(time: str):
        return datetime.datetime.strptime(time, "%Y-%m-%d %H:%M")

    def most_common_sleep_minute(self):
        return self.sleep_calendar.index(max(self.sleep_calendar))

    def fall_asleep(self, time: str):
        self.sleep_start =  self.__to_datetime(time)

    def wake_up(self, time: str):
        awake_time = self.__to_datetime(time)
        self.asleep_minutes += (awake_time - self.sleep_start).total_seconds() / 60
        for minute in range(self.sleep_start.minute, awake_time.minute):
            self.sleep_calendar[minute] += 1

with open('input.txt') as indata:
    data = indata.readlines()
data = sorted([item.strip() for item in data])
guard_id_re = re.compile(r"\[(.+)\] Guard #(.+) begins shift")
wake_re = re.compile(r"\[(.+)\] wakes up")
sleep_re = re.compile(r"\[(.+)\] falls asleep")
guards = []
current_guard = None
for item in data:
    matchdata = guard_id_re.match(item)
    if matchdata:
        guard_id = matchdata.group(2)
        try:
            guard = list(filter(lambda _guard: _guard.id == guard_id, guards))[0]
        except IndexError:
            guard = Guard(guard_id)
            guards.append(guard)
    else:
        matchdata = wake_re.match(item)
        if matchdata:
            guard.wake_up(matchdata.group(1))
        else:
            matchdata = sleep_re.match(item)
            if matchdata:
                guard.fall_asleep(matchdata.group(1))

### Question 1
guard = sorted(guards, key=lambda _guard: _guard.asleep_minutes, reverse=True)[0]
print(guard)
print(f"{int(guard.id) * guard.most_common_sleep_minute()}")

### Question 2
guard = sorted(guards, key=lambda _guard: max(_guard.sleep_calendar), reverse=True)[0]
print(guard)
print(f"{int(guard.id) * guard.most_common_sleep_minute()}")
