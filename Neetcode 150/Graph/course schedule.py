'''STRIVER APPROACH IS BETTER -- GRAPHS/TOPO SORT'''

# NEETCODE APPROACH
# FOLLOW UP => print order of execution
def print_order(num_nodes, edges):
    # write your code here
    from collections import deque

    nodes, order, queue = {}, [], deque()
    for node_id in range(num_nodes):
        nodes[node_id] = { 'in': 0, 'out': set() }
    for node_id, pre_id in edges:
        nodes[node_id]['in'] += 1
        nodes[pre_id]['out'].add(node_id)
    for node_id in nodes.keys():
        if nodes[node_id]['in'] == 0:
            queue.append(node_id)
    while len(queue):
        node_id = queue.pop()
        for outgoing_id in nodes[node_id]['out']:
            nodes[outgoing_id]['in'] -= 1
            if nodes[outgoing_id]['in'] == 0:
                queue.append(outgoing_id)
        order.append(node_id)
        
    return order if len(order) == num_nodes else None


print(print_order(5, [[0,1],[0,2],[0,3],[1,4]])) # true