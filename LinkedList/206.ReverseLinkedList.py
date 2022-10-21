from locale import currency
from os import preadv


while curr:
    nxt = curr.next
    curr.next = prev 
    prev = curr 
    curr = nxt
return prev