from collections import deque

people = ["Shachi", "Utkarsh", "Cherry", "Pumpkin"]

queue = deque(people)

# enqueue
queue.append("Rainbow")

# dequeue
queue.popleft()

# front or peek
queue[0]

print(f"\n {queue[0]}")