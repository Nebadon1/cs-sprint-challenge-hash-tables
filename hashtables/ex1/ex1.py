cache = {}

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    for i in range(len(weights)):
        cache[weights[i]] = i
    for j in range(len(weights)):
        a = limit - weights[j]
        if a in cache:
            return (max(j, cache[a]), min(j, cache[a]))

    return None
