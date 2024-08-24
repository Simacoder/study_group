# 2037 TIME NEEDED TO BUY TICKETS
from collections import deque 

def time_needed_to_buy_tickets(tickets, k):
    queue = deque([(tickets[i], i) for i in range(len(tickets))])
    time = 0

    while queue:
        tickets_left, index = queue.popleft()
        time += 1 # Each person takes one turn to buy a tickect

        if tickets_left - 1 > 0:
            queue.append((tickets_left - 1, index))

        # if the person at index k has no ticket left, return time
        if index == k and tickets_left -1 == 0:
            return time
        

# example 
tickets = [2, 3, 2]
k = 2
print(time_needed_to_buy_tickets(tickets, k))