# Implements a hash table with open addressing and NO delete functionality

class HashTable:
    def __init__(self,length):
        self.data = [None]*length
        self.keys = [None]*length
        self.length = length
        
    def put(self,key,value):
        hashval = self.hash_function(key)
        if self.keys[hashval] == None:
            self.keys[hashval] = key
            self.data[hashval] = value
            #Note, use something like this for chaining: self.data = [[] for _ in range(capacity)]
        else:
            # if there is data there already, and the key matches
            if self.keys[hashval] == key:
                self.data[hashval] = value
            # if there is no data there and the key doesn't match
            elif self.keys[hashval] != key:
                while self.keys[hashval] != key and self.keys[hashval] != None: # consider including case for when table is full
                    hashval = self.rehash_function(hashval)
                self.keys[hashval] = key
                self.data[hashval] = value
    
    def get(self, key):
        hashval = self.hash_function(key)
        
        # if there's nothing in the hash slot, return None
        if self.keys[hashval] == None:
            return None
        
        # if the hash slot matches the key, return the relevant data
        if self.keys[hashval] == key:
            return self.data[hashval]
        
        # start looking in other slots using open addressing...
        # if the hash slot does NOT match the key... check all rehashes until we return to start
        elif self.keys[hashval] != key:
            
            rehashval = self.rehash_function(hashval)
            while True:
                # if we're back at start position, return None
                if rehashval == hashval:
                    return None
                
                # if we found it, return it!
                elif self.keys[rehashval] == key:
                    return self.data[rehashval]
                
                rehashval = self.rehash_function(rehashval)
    
    # removing is difficult with open addressing! 
    # if you just delete the value found, than any re-hashed values further along will never be searched for.
    # this can be fixed by keeping a counter for the number of items which have been hashed for a particular key
    # def remove(self, key):
        
    
    
    def hash_function(self,key):
        return (key%self.length)
    
    def rehash_function(self,oldhash):
        return (oldhash+3)%self.length
