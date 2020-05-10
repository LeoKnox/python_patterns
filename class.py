class Attendee:
    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def displayAttendee(self):
        print(f"Name: {self.name}, Tickets:{self.tickets}")
    
    def addTicket(self):
        self.tickets += 1
        print(f"{self.name} tickets increased to {self.tickets}")