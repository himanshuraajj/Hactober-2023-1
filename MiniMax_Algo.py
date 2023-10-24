import math

def minimax_with_path(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if curDepth == targetDepth:
        return nodeIndex, scores[nodeIndex]

    if maxTurn:
        left_index = nodeIndex * 2
        right_index = nodeIndex * 2 + 1

        left_path, left_value = minimax_with_path(curDepth + 1, left_index, False, scores, targetDepth)
        right_path, right_value = minimax_with_path(curDepth + 1, right_index, False, scores, targetDepth)

        if left_value > right_value:
            return left_path, left_value
        else:
            return right_path, right_value
    else:
        left_index = nodeIndex * 2
        right_index = nodeIndex * 2 + 1

        left_path, left_value = minimax_with_path(curDepth + 1, left_index, True, scores, targetDepth)
        right_path, right_value = minimax_with_path(curDepth + 1, right_index, True, scores, targetDepth)

        if left_value < right_value:
            return left_path, left_value
        else:
            return right_path, right_value

# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = int(math.log(len(scores), 2))

root_path, root_value = minimax_with_path(0, 0, True, scores, treeDepth)

print("The optimal value at the root node is:", root_value)
print("The path to reach the root node is:", root_path)
