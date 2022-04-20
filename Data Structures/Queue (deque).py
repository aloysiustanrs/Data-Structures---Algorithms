from collections import deque

# Create queue
queue = deque()

# Enqueue
queue.append(4)
queue.append(2)
queue.append(123)
queue.append(3)
queue.append(44)

# Dequeue
queue.popleft()

# Print queue
for i in queue:
    print(i)