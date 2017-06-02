class Techcon(object):
    def __init__(self, mon, tue, wed, thu, fri, sat, sun):
        self.monday = mon
        self.tuesday = tue
        self.wednesday = wed
        self.thursday = thu
        self.friday = fri
        self.saturday = sat
        self.sunday = sun


def generate_base_schedule():
    hours = {
        'monday': {
            '08:00': [],
            '08:30': [],
            '09:00': [],
            '09:30': [],
            '10:00': [],
            '10:30': [],
            '11:00': [],
            '11:30': [],
            '12:00': [],
            '12:30': [],
            '13:00': [],
            '13:30': [],
            '14:00': [],
            '14:30': [],
            '15:00': [],
            '15:30': [],
            '16:00': [],
            '16:30': []
        },
        'tuesday': {
        },
        'wednesday': {
        },
        'thursday': {
        },
        'friday': {
        }
    }
    return hours


def generate_schedule(techcons, start_hour, end_hour, max_hours):
    for x in techcons:
        pass


def produce_schedule(techcons, start_hour, end_hour, max_hours):
    pass
