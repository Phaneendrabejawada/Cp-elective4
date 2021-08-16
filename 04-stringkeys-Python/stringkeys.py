"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = ['']*10000

    def store(self, string):
        
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        x = self.calculate_hash_value(string)
        if(self.table[x]!=None):
            self.table[x]=(string) #updating hash value
        else:
            self.table[x]=[string] #storing hash value if not there
        return x
        
    def lookup(self, string):
        
        # Your code goes here
        x = self.calculate_hash_value(string)
        if(string in self.table[x]):  #checks whether string is there or not in hash value if there return hash value of string
            return x
        return -1

    def calculate_hash_value(self, string):
        
        # Your code goes here
        y=ord(string[0]) * 100 + ord(string[1])
        return y



