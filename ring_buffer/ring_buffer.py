class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest_elem_index = 0
        self.buffer = []

    def append(self, item):
        if len(self.buffer) == self.capacity:
            self.buffer.pop(self.oldest_elem_index)
            self.buffer.insert(self.oldest_elem_index, item)
            self.oldest_elem_index += 1

            if self.oldest_elem_index == self.capacity:
                self.oldest_elem_index = 0
        else:
            self.buffer.append(item)

    def get(self):
        return self.buffer
