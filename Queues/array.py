# Array Implementation of Queue
capacity = 10**6
queue_arr = [None] * capacity

size = 0 #stores the current size of queue
front = -1 #stores index of last element which was just removed
rear = -1 #stores index of last element which was just inserted 
# print(f"front = {front}\nrear = {rear}")

# enqueue
def eq(x):
    if size == capacity:
        print("Queue is full")
        return
    rear = (rear + 1)%capacity
    queue_arr[rear] = x
    size += 1

# dequeue
def dq(x):
    if size == 0:
        print("Queue is empty already")
        return    
    front = (front + 1)%capacity
    queue_arr[front] = None
    size -= 1

# front
def front():
    if size == 0:
        print("Queue is empty already")
        return
    return queue_arr[(front+1)%capacity]