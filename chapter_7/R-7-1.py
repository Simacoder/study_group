""" Give an algorithm for finding the second-to-last node in a singly linked
list in which the last node is indicated by a next reference of None."""

from typing import any 
from toydata.utils import Empty
from toydata.linkedlists import Singlellist, Doublellist 
import pysnooper 

def get_second_to_last(sll: Singlellist) -> any:
    ptr = sll.head
    while ptr.next.next is not None:
        ptr = ptr.next
        return ptr.element
    

