"""
380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150


Implement "RandomizedSet". 
bool insert(int val) Inserts an item val into the set if not present. 
Returns true if the item was not present, false otherwise.

bool remove(int val) Removes an item val from the set if present. 
Returns true if the item was present, false otherwise.

int getRandom() Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.
This one would mean we may have to use dict since its insert, get, remove are O(1).
Aside from dict, we will have to use array and random.


Insert & Delete are great on dict since it's a key & value pair.
Random is great on array since we can get random integer from 0 to len(array) - 1 and use it as an index.
However, there's a problem with how to delete an item from an array in O(1) time because
both array.index and array.remove take O(n).

What we could do is instead of directly removing the requested value from an array, 
we could put the array[index of requested value] = last item of the array and remove the last item instead.
Then, we replace the dict[last item] to the removed index and delete the value from the dictionary.
Do the removal from dictionary after setting dict[last_value] = removed index.
Why? cos if we only have one item and removal first, it will end up putting the value and index back into the dict.
"""
class RandomizedSet:

    def __init__(self):
        self.a = []
        self.d = {} 
        

    def insert(self, val: int) -> bool:
        if val in self.d: return False
        self.a.append(val)
        self.d[val] = len(self.a) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.d: return False
        last_item = self.a[-1]
        last_item_idx = self.d[last_item]
        # array[ index of val ] = last item from array
        self.a[ self.d[val] ] = last_item
        del self.a[-1]
        # put the index of val to the index of last item
        self.d[last_item] = self.d[val]
        del self.d[val]
        return True
        

    def getRandom(self) -> int:
        import random
        return self.a[ random.randint(0, len(self.a)-1) ]