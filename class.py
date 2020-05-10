class Attendee:
    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def displayAttendee(self):
        print(f"Name: {self.name}, Tickets:{self.tickets}")
    
    def addTicket(self):
        self.tickets += 1
        print(f"{self.name} tickets increased to {self.tickets}")



att1 = Attendee("Asmodeus", 666)
att2 = Attendee("Bahamat", 7)

att1.displayAttendee()
att2.displayAttendee()

att1.addTicket()
att1.displayAttendee()

att1.addTicket()
att1.displayAttendee()