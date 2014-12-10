class Hash:
    def __init__(self):
        self.size = 10
        self.array = [[] for i in range(self.size)]

    def hashCodeOfKey(self, key):
        return len(str(key))%self.size

    def put(self, cell):
        hashCode = self.hashCodeOfKey(cell.key)
        self.array[hashCode].append(cell)

    def get(self, key):
        hashCode = self.hashCodeOfKey(key)
        for cell in self.array[hashCode]:
            if cell.key == key: return cell

class Cell:
    def __init__(self, k, v):
        self.key = k
        self.value = v
    
if __name__ == "__main__":
    hashTable = Hash()
    hashTable.put(Cell(2,4))
    hashTable.put(Cell(3,9))
    print hashTable.get(3).value

