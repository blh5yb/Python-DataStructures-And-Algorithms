
import pytest
from unittest.mock import patch
from src.priority_queue import *

queue_one_raw = [
    {'_id': 'id1', 'priority': 3, 'timestamp': 10.1},
    {'_id': 'id2', 'priority': 3, 'timestamp': 10.21},
    {'_id': 'id3', 'priority': 3, 'timestamp': 10.6},
    {'_id': 'id4', 'priority': 3, 'timestamp': 10.2},
    {'_id': 'id5', 'priority': 3, 'timestamp': 9.12},
]
queue_one_sorted = [
    {'_id': 'id5', 'priority': 3, 'timestamp': 9.12},
    {'_id': 'id1', 'priority': 3, 'timestamp': 10.1},
    {'_id': 'id4', 'priority': 3, 'timestamp': 10.2},
    {'_id': 'id2', 'priority': 3, 'timestamp': 10.21},
    {'_id': 'id3', 'priority': 3, 'timestamp': 10.6},
]

queue_two_raw = [
    {'_id': 'id1', 'priority': 4, 'timestamp': 10.1},
    {'_id': 'id2', 'priority': 1, 'timestamp': 10.21},
    {'_id': 'id3', 'priority': 3, 'timestamp': 10.6},
    {'_id': 'id4', 'priority': 4, 'timestamp': 10.2},
    {'_id': 'id5', 'priority': 1, 'timestamp': 9.12},
]
queue_two_sorted = [
    {'_id': 'id5', 'priority': 1, 'timestamp': 9.12},
    {'_id': 'id2', 'priority': 1, 'timestamp': 10.21},
    {'_id': 'id3', 'priority': 3, 'timestamp': 10.6},
    {'_id': 'id1', 'priority': 4, 'timestamp': 10.1},
    {'_id': 'id4', 'priority': 4, 'timestamp': 10.2},
]

queue_three_sorted = [
    {'_id': 'id5', 'priority': 1, 'timestamp': 9.12},
    {'_id': 'id2', 'priority': 1, 'timestamp': 10.21},
]

queue_three_updated = [
    {'_id': 'id2', 'priority': 1, 'timestamp': 10.21},
    {'_id': 'id5', 'priority': 2, 'timestamp': 9.12},
]

@pytest.fixture(scope="function")
def time_fixture():
    with patch('time.time') as time_mock:
        yield time_mock

class TestPriorityQueue:
    def test_constructor(self, time_fixture):
        """
        Test the constructor value of self.queue variable is updated correctly
        """
        queue = PriorityQueue()
        time_fixture.return_value = 10.1
        queue.enqueue('id1', 4)
        result = queue.get_queue()

        assert result == [{'_id': 'id1', 'priority': 4, 'timestamp': 10.1}]

    @pytest.mark.parametrize(
        'queue_items, sorted_queue',
        [
            (queue_one_raw, queue_one_sorted),
            (queue_two_raw, queue_two_sorted)
        ]
    )
    def test_enqueue(self, queue_items, sorted_queue, time_fixture):
        """
        Test the constructor value of self.queue variable is updated correctly by enqueue function
        """
        queue = PriorityQueue()
        for item in queue_items[:4]:
            time_fixture.return_value = item['timestamp']
            queue.enqueue(item['_id'], item['priority'])
        time_fixture.return_value = queue_items[-1]['timestamp']
        queue.enqueue(queue_items[-1]['_id'], queue_items[-1]['priority'])
        result = queue.get_queue()

        assert result == sorted_queue

    @pytest.mark.parametrize(
        'queue_items, dequed_item, updated_queue',
        [
            (queue_one_sorted, queue_one_sorted[0], queue_one_sorted[1:]),
            (queue_two_sorted, queue_two_sorted[0], queue_two_sorted[1:]),
            ([], None, [])
        ]
    )
    def test_dequeue(self, queue_items, dequed_item, updated_queue, time_fixture):
        """Test dequeue'ing first item or return None if queue is empty"""
        queue = PriorityQueue()
        for item in queue_items:
            time_fixture.return_value = item['timestamp']
            queue.enqueue(item['_id'], item['priority'])

        result = queue.dequeue()
        assert result == dequed_item # first item from the queue
        assert queue.get_queue() == updated_queue # queue[1:] or None

    @pytest.mark.parametrize(
        'queue_items, updated_queue, target_id, new_priority',
        [
            (queue_three_sorted, queue_three_updated, queue_three_sorted[0]['_id'], 2),
            (queue_three_sorted, queue_three_sorted, 'not_found_id', 2) # not updated
        ]
    )
    def test_priority_update(self, queue_items, updated_queue, target_id, new_priority, time_fixture):
        queue = PriorityQueue()
        for item in queue_items:
            time_fixture.return_value = item['timestamp']
            queue.enqueue(item['_id'], item['priority'])
        queue.update_priority(target_id, new_priority)
        assert queue.get_queue() == updated_queue