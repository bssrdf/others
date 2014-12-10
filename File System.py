from datetime import datetime;

class Entry(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.created = str(datetime.now())
        self.lastUpdated = str(datetime.now())
        self.lastAccessed = str(datetime.now())
    def delete(self):
        if self.parent is None: return False
        return self.parent.deleteEntry(self)
    def size(self):pass
    def getFullPath(self):
        if self.parent is None: return self.name
        return self.parent.getFullPath()+"/"+self.name
    def getCreationTime(self): return self.created
    def getLastUpdatedTime(self):return self.lastUpdated
    def getLastAccessedTime(self):return self.lastAccessed
    def changeName(self, name): self.name = name
    def getName(self): return self.name

class File(Entry):
    def __init__(self, name, parent=None, size=None):
        super(File, self).__init__(name, parent)
        self.content = None
        self.size = size
    def size(self): return self.size
    def getContent(self): return self.content
    def setContent(self, content): self.content = content

class Directory(Entry):
    def __init__(self, name, parent=None): 
        super(Directory, self).__init__(name, parent)
        self.contents = []
    def size(self): 
        size = 0
        for c in self.contents: size+=c.size()
        return size
    def numberOfFiles(self): 
        cnt = 0
        for e in self.contents:
            cnt+=1
            if isinstance(e, Directory): cnt += e.numberOfFiles()
        return cnt
    def deleteEntry(self, entry): 
        self.contents.remove(entry)
    def addEntry(self, entry):
        self.contents.append(entry)
    def getContents(self): 
        return self.contents

if __name__ == "__main__":
    root = Directory("root")
    subdir1 = Directory("subdir1", root)
    root.addEntry(subdir1)
    file1 = File("file1.txt", root, 100)
    root.addEntry(file1)
    file2 = File("file2.txt", subdir1, 50)
    subdir1.addEntry(file2)
    print root.numberOfFiles()
    root.delete()
    print root.name
