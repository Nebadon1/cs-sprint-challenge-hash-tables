#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
cache = {}

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = [None] * length
    # fill the dictionary, looping through the tickets
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
        # print(cache)
    next_pointer = cache['NONE']
    for t in range(0, length):
        route[t] = next_pointer
        next_pointer = cache[next_pointer]

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]


print(reconstruct_trip(tickets, 3))


  
