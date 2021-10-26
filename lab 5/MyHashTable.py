class MyHashTable:

    def __init__(self, table_size = 11):
        # initialize hash table using a list (most likely linked)
        # returns a MyHashTable object
        # instance variables num_items, num_collisions
        self.items_hashed = 0
        self.num_collisions = 0
        self.hashtable = [[] for x in range(table_size)]
        self.capacity = table_size

    def hash_function(self, key):
        return key % self.capacity

    def insert(self, key, item):
        if self.load_factor(1) >= 1.5:
            self.helper_rehash()
       # check for duplicate
       # if self.get_duplicate(key):
       #     pass #handle duplicates
       # else:
       #     pass # append key and value to its hash and check if the location it is appended to already has another tuple, if so collision + 1

        item_pair = [key, item]
        for x in self.hashtable[self.hash_function(key)]:
            i = 0
            if x[0] == key:
                self.hashtable[self.hash_function(key)][i] = item_pair
                self.num_collisions += 1
                return
            i += 1
        self.hashtable[self.hash_function(key)].append(item_pair)
        self.items_hashed += 1

    def helper_rehash(self):
        # new_size = 2*old_size + 1 to AVOID collisions
        self.capacity = (2*self.capacity + 1)
        self.num_collisions = 0
        new_size = [[] for x in range(self.capacity)]
        for x in self.hashtable:
            for h in x:
                if len(new_size[self.hash_function(h[0])]) != 0:
                    self.num_collisions += 1
                    new_size[self.hash_function(h[0])].append(h)
        self.hashtable = new_size

    def get(self, key, boolean=False):
        # takes a key and returns the item pair
        # watch out for LookupError exception if no key-item pair is associated with the key
        for x in self.hashtable[self.hash_function(key)]:
            if key == x[0]:
                if boolean is False:
                    return key, x[1]
                else:
                    return x, self.hash_function(key)
    ''' might need LookupError here'''

    def get_duplicate(self, key, boolean=False):
        for x in self.hashtable[self.hash_function(key)]:
            if key == x[0]:
                if boolean is False:
                    return True
                else:
                    return x, self.hash_function(key)
        return False

    def remove(self, key):
        # takes a key, removes key-item pair & returns key-item pair
        # watch out for LookupError exception if no key-item pair is associated with the key
        get_key = self.get(key, True)
        self.hashtable[get_key[1]].remove(get_key[0])
        self.items_hashed -= 1
        return get_key[0]

    def size(self):
        # returns the number of key-item pairs currently stored
        return self.items_hashed

    def load_factor(self, position = 0):
        # function returns the current load factor of the hash table
        # if load_factor is above 50% then we need to resize the table
        if self.items_hashed != 0:
        # size/capacity = load_factor (how many elements divided by maximum number of elements) using float
            return float(float(self.items_hashed + self.num_collisions))/float(self.capacity)
        else:
            return float(0)

    def collisions(self):
        # returns the number of collisions (integer) that have occured during insertions into the hash table
        # occurs when item inserted into hash table at a location where one or more key-item pairs has already been inserted
        return self.num_collisions


'''
    def insert(self, key, item):
        hash key to get to an index, 1. modulus 2. use hash value as index 3. check if key exists, and override item if theres 2, if key doesn't exist there is a collision
        inserts a key-item pair based on hash value via Modulus
        needs to check for duplication (if statement)
        algorithm... new_size = 2*old_size + 1
        rehash
        
        
        if self.load_factor(1) >= 1.5:
            self.helper_rehash()

        item_pair = [key, item]
            i = 0
        if (len(self.hashtable[self.hash_function]) == 0):
            self.hashtable[self.hash_function(key)].append(item_pair)
            self.items_hashed += 1
        else:
            self.hashtable[self.hash_function(key)].append(item_pair)
            self.num_collisions += 1
            self.items_hashed += 1
        
        hash key to get to an index, 1. modulus 2. use hash value as index 3. check if key exists, and override item if theres 2, if key doesn't exist there is a collision
        
        
    item_pair = [key, item]
        for x in self.hashtable[self.hash_function(key)]:
            i = 0
            if x[0] == key:
                self.hashtable[self.hash_function(key)][i] = item_pair
                self.num_collisions += 1
                return
        if len(self.hashtables[hashindex] != 1

          if get.key:
            checks if key exists, if duplicate just replace it
         i += 1
      self.hashtable[self.hash_function(key)].append(item_pair)
       self.items_hashed += 1
        use append function to add a single item to the end of a existing list
      self.hashtable[self.hash_function(key)].append(item_pair)
       if len(self.hashtables[item_pair] != 1:
        self.items_hashed += 1
        
        
      def insert(self, key, item):                                                   
        if self.load_factor(1) >= 1.5:                                               
            self.helper_rehash()

        item_pair = [key, item]                                                                                                                                   # Traverse the list through to test if any of the values have the same key
        for x in self.hashtable[self.hash_function(key)]:
            i = 0
            if x[0] == key:                                                           
                self.hashtables[self.hash_function(key)][i] = item_pair
                self.num_collisions += 1
                return
            i += 1                                                                   
        self.hashtables[self.hash_function(key)].append(item_pair)  # append to list
        self.items_hashed += 1

'''
''' def insert(self, key, item):
        self.items_hashed += 1
        hashindex = key % self.capacity
        if self.load_factor(1) >= 1.5:
            self.helper_rehash()

        item_pair = [key, item]

        for x in self.hashtable[self.hash_function(key)]:
            i = 0
            print(self.hashtable[self.hash_function(key)])
            if len(self.hashtable[self.hash_function(key)] == 0):
                self.hashtable[self.hash_function(key)][i] = item_pair
                self.hashtable[self.hash_function(key)].append(item_pair)
                self.items_hashed += 1
                return
            i += 1
        else:
            self.hashtable[self.hash_function(key)].append(item_pair)
            self.num_collisions += 1
            self.items_hashed += 1'''