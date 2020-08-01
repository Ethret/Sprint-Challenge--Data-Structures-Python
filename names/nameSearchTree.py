class nameSearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if  self.value > value:
            if self.left == None:
                 self.left = nameSearchTree(value)
            else:
                self.left.insert(value)

        if  self.value <= value:
            if self.right == None:
                self.right = nameSearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if self.right != None:
                return self.right.contains(target)
            else:
                    return False

        elif target < self.value:
            if self.left != None:
                return self.left.contains(target)
            else:
                return False

    def get_max(self):
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
