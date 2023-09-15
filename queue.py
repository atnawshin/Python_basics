#queue - FIFO
from collections import deque

bank = deque(["Jhon","Jane","Joye","Chandler"])
print(bank)
bank.popleft()
bank.popleft()
bank.popleft()
bank.popleft()

if not bank:
    print("No person left")