from node import Node

class QueueNode:
    def __init__(self):
        self.queue = []

    def push(self, node):
        if (self.length() == 0):
            self.queue.append(node)
        else:
            for i in range(self.length()):
                if (node.cost < self.queue[i].cost):
                    self.queue.insert(i, node)
                    break
                elif (i == self.length() - 1):
                    self.queue.append(node)

    def pop(self):
        return self.queue.pop(0)
    
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

    def print(self):
        for node in self.queue:
            node.print()
