
# %%
def DFS(start_node):
    result = []
    visited = {}
    stack = [start_node]
    while len(stack) > 0:
        node = stack.pop(len(stack) - 1)
        if node.value in visited:
            continue
        visited[node.value] = True 
        result.append(node.value)
        for index in range(len(node.children) - 1, -1, -1):
            if node.children[index] is not None:
                stack.append(node.children[index])
    print(result)

def BFS(start_node):
    result = []
    visited = {}
    queue = [start_node]
    while len(queue) > 0:
        node = queue.pop(0)
        if node.value in visited:
            continue
        visited[node.value] = True        
        result.append(node.value)
        for index in range(0, len(node.children)):
            if node.children[index] is not None:
                queue.append(node.children[index])
    print(result)
