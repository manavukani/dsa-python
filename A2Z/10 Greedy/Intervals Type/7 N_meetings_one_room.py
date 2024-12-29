# maximum number of meetings that can be accommodated in a single meeting room

def maximumMeetings(start, end):
    meetings = list(zip(start, end))
    meetings.sort(key=lambda x: x[1])  # sort by end time
    last_end_time = -1
    count = 0
    for s, e in meetings:
        if s > last_end_time:
            count += 1
            last_end_time = e

    return count
