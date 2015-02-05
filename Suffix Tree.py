class SuffixTree:
    def __init__(self, string):
        self.root = SuffixTreeNode()
        for i in range(len(string)):
            suffix = string[i:]
            self.root.insert(suffix, i)

    def search(self, target):
        return self.root.search(target)

class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.indexes = []

    def insert(self, string, index):
        self.indexes.append(index)
        if string is not None and len(string)!=0:
            value = string[0]
            child = None
            if value in self.children:
                child = self.children[value]
            else:
                child = SuffixTreeNode()
                self.children[value] = child
            remainder = string[1:]
            child.insert(remainder, index)

    def search(self, target):
        if target is None or len(target)==0:
            return self.indexes
        else:
            value = target[0]
            if value in self.children:
                remainder = target[1:]
                return self.children[value].search(remainder)
        return None

if __name__ == "__main__":
    t = SuffixTree("banana")
    print t.search("a")
    print t.root.children, t.root.indexes
    print t.root.children['a'].children, t.root.children['a'].indexes
