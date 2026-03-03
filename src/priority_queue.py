import heapq
import time
from dataclasses import dataclass


########################################################################################################################
# Static Priority Queue Module
# Author: Barry Hykes Jr, bhykes@gmail.com
# version 1.0.0
########################################################################################################################

@dataclass(order=True)
class QueueItem:
    priority: int
    timestamp: float
    item_id: str

class ModernPriorityQueue:
    """Using heapq to push, peek, pop, update"""
    def __init__(self):
        self._queue = []
        self._entry_finder = {}
        self.REMOVED = '<REMOVED>'

    def remove(self, _id):
        item: QueueItem = self._entry_finder.pop(_id)
        item.item_id = self.REMOVED # updating item in entry finder auto updates the reference in self._queue also

    def enqueue(self, _id, priority):
        timestamp = round(time.time(), 3)
        if _id in self._entry_finder:
            self.remove(_id)

        item = QueueItem(priority, timestamp, _id)
        heapq.heappush(self._queue, item)
        self._entry_finder[_id] = item

    def dequeue(self):
        if not self._queue:
            return None

        while self._queue:
            item: QueueItem = heapq.heappop(self._queue)
            if item.item_id is not self.REMOVED:
                return item

    def peek(self):
        if not self._queue:
            return None

        while self._queue:
            item: QueueItem = self._queue[0]
            if item.item_id is self.REMOVED:
                heapq.heappop(self._queue)
            else:
                return item

    def update_priority(self, _id, priority):
        item: QueueItem = self._entry_finder[_id]
        timestamp = item.timestamp
        updated_item = QueueItem(priority, timestamp, item.item_id)

        self.remove(item.item_id)
        heapq.heappush(self._queue, updated_item)

class PriorityQueue:
    """
    Priority queue that assigns higher input integer priority value and
    then by timestamp - higher priority given to first entered when priority
    value is equal
    """
    __slots__ = ['_queue']
    def __init__(self):
        """Initialize the queue"""
        self._queue = []

    def get_queue(self):
        return self._queue

    def enqueue(self, _id, priority):
        """
        Add item to the queue
        :param _id: unique identifier, str
        :param priority: priority of the item added to the queue
        """
        current_timestamp = time.time()
        self._queue.append({
            '_id': _id,
            'priority': priority,
            'timestamp': current_timestamp
        })
        self._sort_queue()

    def dequeue(self):
        """Remove and return highest priority item"""
        if not len(self._queue):
            return None

        item = self._queue.pop(0)
        return item

    def peek(self):
        if not len(self._queue):
            return None

        return self._queue[0]


    def update_priority(self, target_id, new_priority):
        """
        Update the priority of existing item in queue
        :param target_id: _id of item to update, str
        :param new_priority: new priority to assign to the item, int
        """
        found_index = next((index for index, item in enumerate(self._queue) if item['_id'] == target_id), None)
        if found_index is not None:
            self._queue[found_index]['priority'] = new_priority
            self._sort_queue()

    def _sort_queue(self):
        """private method to sort queue by priority and then by timestamp for equal priorities"""
        self._queue.sort(key=lambda obj: (obj['priority'], obj['timestamp']))


def testing_priority_queue():
    priority_queue = PriorityQueue()
    priority_queue.enqueue('item1', 2)
    priority_queue.enqueue('item2', 1)
    time.sleep(.2)
    print(priority_queue.peek())
    priority_queue.enqueue('item3', 2)
    priority_queue.enqueue('item4', 1)
    time.sleep(.2)

    print(priority_queue.peek())

    priority_queue.update_priority('item2', 3)
    time.sleep(.2)
    print(priority_queue.peek())

    priority_queue.dequeue()
    print(priority_queue.peek())

    print('modern version')

    priority_queue = ModernPriorityQueue()
    priority_queue.enqueue('item1', 2)
    priority_queue.enqueue('item2', 1)
    time.sleep(.2)
    print(priority_queue.peek())
    priority_queue.enqueue('item3', 2)
    priority_queue.enqueue('item4', 1)
    time.sleep(.2)

    print(priority_queue.peek())

    priority_queue.update_priority('item2', 3)
    time.sleep(.2)
    print(priority_queue.peek())

    priority_queue.dequeue()
    print(priority_queue.peek())