"""Decision Tree."""


class TreeNode(Object):
    """Node for the decision tree."""

    def __init__(self, data_idx, column=None, split=None):
        self.column = column
        self.split = split
        self.left = None
        self.right = None
        self.data_idx = data_idx


class DecisionTree(Object):
    """The Tree!"""

    def __init__(self, max_depth=None, min_leaf_size=None):
        self.max_depth = max_depth
        self.min_leaf_size = min_leaf_size
        self.root = None

    def fit(self, columns, labels):
        """Build the decision tree's brain."""
        self.root = TreeNode(data_idx=columns.index)  # flowers.index
        self.columns = columns
        node = self.root
        while True:
            self.split(node)
            node = node.left  # maybe?

    def _split(self, node):
        """Split the values."""
        node.column, node.split = best_split_alg(node)

        left_idx = idx or values in column where value < split
        node.left = TreeNode(data_idx=left_idx)
        if len(node.left.data_idx) <= 1 or len(set(node.left.labels)) <= 1:
            end left

        #repeat for right node

    def best_split_alg(self, node):
        """Find the best column and split point, given a node with a dataset."""
        for val in flowers_data[0]:
            left_list=[labels[idx] for idx in data_idx if flowers_data[0][idx] <= val]
            right_list=[labels[idx] for idx in data_idx if flowers_data[0][idx] > val]
            print(left_list, right_list,
                  left_list.count(1)/len(left_list) * right_list.count(0)/len(right_list), 
                  left_list.count(0)/len(left_list) * right_list.count(1)/len(right_list),
                  right_list.count(0),
                  left_list.count(0),
                  len(right_list),
                  len(left_list))


    def predict(self, columns):
        """Apply model to new datapoints."""
        pass
