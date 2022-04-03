import heapq as hq

class QueueNode:
    # Constructor
    def __init__(self):
        self.queue = []
        # ubah queue menjadi min-heap
        hq.heapify(self.queue)

    # Method untuk menambahkan node ke dalam queue
    def push(self, node):
        hq.heappush(self.queue, node)

    # Method untuk mengambil node dengan cost paling minimum
    def pop(self):
        return hq.heappop(self.queue)
    
    # Method untuk menghitung panjang dari queue
    def length(self):
        return len(self.queue)

    # Method untuk mengecek apakah queue kosong
    def isEmpty(self):
        return self.length() == 0

    # Method untuk menghapus node yang memiliki cost yang lebih besar dengan cost node yang diberikan
    def kill(self, cost):
        i = 0
        while (i < self.length()):
            if (self.queue[i].cost > cost):
                self.queue.pop(i)
            else:
                i += 1
        hq.heapify(self.queue)

    # Method untuk mencetak queue
    def print(self):
        for node in self.queue:
            node.print()
