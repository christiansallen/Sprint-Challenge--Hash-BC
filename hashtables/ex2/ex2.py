#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)

    current_location = "NONE"
    for i in range(length):
        next_location = hash_table_retrieve(hashtable, current_location)
        route[i] = next_location
        current_location = next_location

    return route

    # def hash_table_retrieve(hash_table, key):
    # index = hash(key, len(hash_table.storage))

    # current_pair = hash_table.storage[index]

    # while current_pair is not None:
    #     if(current_pair.key == key):
    #         return current_pair.value
    #     current_pair = current_pair.next

    return route
