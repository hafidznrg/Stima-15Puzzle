import heapq as hq

class QueueNode:
    def __init__(self):
        self.queue = []
        hq.heapify(self.queue)

    def push(self, node):
        hq.heappush(self.queue, node)

    def pop(self):
        return hq.heappop(self.queue)
    
    def length(self):
        return len(self.queue)

    def isEmpty(self):
        return self.length() == 0

    def kill(self, cost):
        i = 0
        while (i < self.length()):
            if (self.queue[i].cost > cost):
                self.queue.pop(i)
            else:
                i += 1
        hq.heapify(self.queue)

    def print(self):
        for node in self.queue:
            node.print()
