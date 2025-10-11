import time

########################################################################################################################
# Static Priority Queue Module
# Author: Barry Hykes Jr, bhykes@gmail.com
# version 1.0.0
########################################################################################################################


class PriorityQueue:
    """
    Priority queue that assigns higher input integer priority value and
    then by timestamp - higher priority given to first entered when priority
    value is equal
    """
    __slots__ = ['__queue']
    def __init__(self):
        """Initialize the queue"""
        self.__queue = []

    def get_queue(self):
        return self.__queue

    def enqueue(self, _id, priority):
        """
        Add item to the queue
        :param _id: unique identifier, str
        :param priority: priority of the item added to the queue
        """
        current_timestamp = time.time()
        self.__queue.append({
            '_id': _id,
            'priority': priority,
            'timestamp': current_timestamp
        })
        self.__sort_queue()

    def dequeue(self):
        """Remove and return highest priority item"""
        if not len(self.__queue):
            return None

        item = self.__queue.pop(0)
        return item

    def update_priority(self, target_id, new_priority):
        """
        Update the priority of existing item in queue
        :param target_id: _id of item to update, str
        :param new_priority: new priority to assign to the item, int
        """
        found_index = next((index for index, item in enumerate(self.__queue) if item['_id'] == target_id), None)
        if found_index is not None:
            self.__queue[found_index]['priority'] = new_priority
            self.__sort_queue()

    def __sort_queue(self):
        """private method to sort queue by priority and then by timestamp for equal priorities"""
        self.__queue.sort(key=lambda obj: (obj['priority'], obj['timestamp']))


# if __name__ == "__main__":
#     priority_queue = PriorityQueue()
#     priority_queue.enqueue('item1', 1)
#     priority_queue.enqueue('item2', 0)
#     print(priority_queue.queue)
#     time.sleep(1)
#     priority_queue.enqueue('item3', 1)
#     priority_queue.enqueue('item4', 0)
#     print(priority_queue.queue)
#
#     priority_queue.update_priority('item2', 2)
#     print(priority_queue.queue)
#
#     priority_queue.dequeue()
#     print(priority_queue.queue)