class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def avl_insert(root, key):
    if not root:
        return AVLNode(key)
    elif key < root.key:
        root.left = avl_insert(root.left, key)
    else:
        root.right = avl_insert(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # Left Left Case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Right Right Case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Left Right Case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right Left Case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def get_height(root):
    if not root:
        return 0
    return root.height

def get_balance(root):
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)

def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y




def find_max_value_avl(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.key

def find_min_value_avl(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.key

def sum_tree_avl(root):
    if root is None:
        return 0
    return root.key + sum_tree_avl(root.left) + sum_tree_avl(root.right)


# Приклад використання
avl_root = None
avl_root = avl_insert(avl_root, 20)
avl_root = avl_insert(avl_root, 8)
avl_root = avl_insert(avl_root, 22)
avl_root = avl_insert(avl_root, 4)
avl_root = avl_insert(avl_root, 12)
avl_root = avl_insert(avl_root, 10)
avl_root = avl_insert(avl_root, 14)

print(f"Найменше значення у AVL-дереві: {find_min_value_avl(avl_root)}")
print(f"Найбільше значення у AVL-дереві: {find_max_value_avl(avl_root)}")
print(f"Сума всіх значень у AVL-дереві: {sum_tree_avl(avl_root)}")