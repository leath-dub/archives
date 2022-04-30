class Meeting(object):

    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        return "{:02d}:{:02d} ({} minutes)".format(
            self.hour, self.minute, self.duration)

class Schedule(object):

    def __init__(self):
        self.meetings = {}

    def add(self, instance):
        time = instance.minute + (instance.hour * 60)
        self.meetings[time] = "{}".format(instance)

    def __str__(self):
        rlist = []
        rlist.append("Schedule\n--------")
        for k, v in sorted(self.meetings.items()):
            rlist.append(v)
        rlist.append(
            "Meetings today: {}".format(len(rlist) - 1))
        return "\n".join(rlist)
