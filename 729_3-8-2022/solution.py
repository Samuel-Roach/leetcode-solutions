class MyCalendar:

    def __init__(self):
        self.timetable = []

    def book(self, start: int, end: int) -> bool:
        for booking_s, booking_e in self.timetable:
            if booking_s < end and start < booking_e:
                return False
        self.timetable.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)