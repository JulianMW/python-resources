def reverse_SLL_k_recursive(head, k):
    curr_node = head 
    next_node  = None
    prev_node = None
    count = 0

    # Reverse first k nodes of the linked list
    while(curr_node is not None and count < k):
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
        count += 1

    # next is now a pointer to (k+1)th node
    # recursively call for the list starting
    # from current . And make rest of the list as
    # next of first node
    if next_node is not None:
        head.next = reverse_SLL_k_recursive(next_node, k)

    # prev is new head of the input list
    return prev_node
