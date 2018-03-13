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
                
                
    def hash_function(self,key):
        return (key%self.length)
    
    def rehash_function(self,oldhash):
        return (oldhash+1)%self.size
