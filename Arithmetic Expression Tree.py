class AENode(object):
    def __init__(self):pass
    def evaluate(self):pass

class AEValueNode(AENode):
    def __init__(self, v):
        self.value = v
    def evaluate(self):return self.value

class AEBinaryOperatorNode(AENode):
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
    def evaluate(self):pass

class AENaryOperatorNode(AENode):
    def __init__(self, children):
        self.children = children
    def evaluate(self):pass

class AEAddNode(AEBinaryOperatorNode):
    def __init__(self, node1, node2):
        super(AEAddNode, self).__init__(node1, node2)
    def evaluate(self):
        if self.node1 and self.node2: return self.node1.evaluate()+self.node2.evaluate()

class AEAverageNode(AENaryOperatorNode):
    def __init__(self, children):
        super(AEAverageNode, self).__init__(children)
    def evaluate(self):
        if self.children:
            sum = 0
            for child in self.children:
                sum+=child.evaluate()
            return sum/len(self.children)

if __name__ == "__main__":
    root = AEAddNode(AEValueNode(3), AEValueNode(4))
    print root.evaluate()
    root = AEAverageNode([AEAddNode(AEValueNode(1), AEValueNode(2)),AEValueNode(3)])
    print root.evaluate()