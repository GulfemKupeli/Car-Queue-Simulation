# QUEUE IMPLEMENTATION BASED PARKING SIMULATION
import random


# I used Node structure for constructing FIFO Queue.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, car):
        newNode = Node(car)
        if not self.front:
            self.front = newNode
            self.rear = newNode
        else:
            if not self.rear:
                self.rear = self.front
            self.rear.next = newNode
            self.rear = newNode
        # This part iterates through a queue and calculates the total waiting time for each car.
        current = self.front
        totalProcessTime = 0
        while current:
            current.data.totalWaitTime = totalProcessTime
            totalProcessTime += current.data.processTime
            current = current.next

    def dequeue(self):
        if not self.front:
            print("Queue is empty")
            return None
        else:
            data = self.front.data
            self.front = self.front.next
            if not self.front:
                self.rear = None
            return data

    def isEmpty(self):
        return self.front is None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, car):
        newNode = Node(car)
        if self.head is None or car.processTime < self.head.data.processTime:
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            while current.next is not None and current.next.data.processTime <= car.processTime:
                current = current.next
            newNode.next = current.next
            current.next = newNode
        current = self.head
        # This part iterates through a queue and calculates the total waiting time for each car.
        totalProcessTime = 0
        while current:
            current.data.totalWaitTime = totalProcessTime
            totalProcessTime += current.data.processTime
            current = current.next

    def dequeue(self):
        if not self.isEmpty():
            removedCar = self.head.data
            self.head = self.head.next
            return removedCar
        else:
            print("Queue is empty")
            return None

    def isEmpty(self):
        return self.head is None


# I created a car class for keeping track of car number and processing time.
class Car:
    def __init__(self, carNumber):
        self.carNumber = carNumber
        self.processTime = random.randint(10, 300)
        self.totalWaitTime = 0
        self.completedProcessTime = 0


if __name__ == "__main__":
    N = random.randint(1, 20)  # Queue size may change between 1 and 20.

    stdQueue = Queue()  # standard queue
    priQueue = PriorityQueue()  # priority queue

    totalProcessingTimeStd = 0
    totalProcessingTimePri = 0
    # I created two for loops for assigning car numbers to incoming cars.
    # I assumed that the different cars are coming in for priority queue but the same amount as our standard queue.
    for i in range(1, N + 1):
        # There is a system here for queuing the cars and recording the process times.
        carStd = Car(i)
        totalProcessingTimeStd += carStd.processTime
        stdQueue.enqueue(carStd)
    for j in range(1, N + 1):
        carPri = Car(j)
        totalProcessingTimePri += carPri.processTime
        priQueue.enqueue(carPri)

    print("STANDARD QUEUE: ")
    totalTimeStd = 0
    # This part  processes all cars in the standard queue, calculates their waiting and completed process times,
    # and displays detailed information for each car.
    while not stdQueue.isEmpty():
        car = stdQueue.dequeue()
        car.totalWaitTime = totalTimeStd
        totalTimeStd += car.processTime
        car.completedProcessTime = totalTimeStd
        print(
            f"Car {car.carNumber} |  Process Time: {car.processTime} seconds, Wait Time: {car.totalWaitTime} seconds, "
            f"Completed Process Time: {car.completedProcessTime} seconds")
    #It calculates and prints the average transaction completion time for the entire queue.
    averageTimeStd = totalProcessingTimeStd / N
    print(f"\nAverage Transaction Completion Time for {N} Cars in Standard Queue: {averageTimeStd:.2f} seconds")

    print("\nPRIORITY QUEUE:")
    totalTimePri = 0
    while not priQueue.isEmpty():
        car = priQueue.dequeue()
        car.totalWaitTime = totalTimePri
        totalTimePri += car.processTime
        car.completedProcessTime = totalTimePri
        print(
            f"Car {car.carNumber} |  Process Time: {car.processTime} seconds, Wait Time: {car.totalWaitTime} seconds, "
            f"Completed Process Time: {car.completedProcessTime} seconds")

    averageTimePri = totalProcessingTimePri / N
    print(f"\nAverage Transaction Completion Time for {N} Cars in Priority Queue: {averageTimePri:.2f} seconds")

    gain = ((averageTimeStd - averageTimePri) / averageTimeStd) * 100
    print(f"\nGain: {gain:.2f}%")
