class TreeMap:
    class Node:
        def _init_(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def _init_(self):
        self.root = None

    def _setitem_(self, key, value):
        self.root = self._insert_node(self.root, key, value)

    def _insert_node(self, node, key, value):
        if node is None:
            return self.Node(key, value)
        if key < node.key:
            node.left = self._insert_node(node.left, key, value)
        else:
            node.right = self._insert_node(node.right, key, value)
        return node