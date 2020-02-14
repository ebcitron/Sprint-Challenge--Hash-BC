#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)
    answer = None

    for i in range(len(weights)):
        theRest = limit - weights[i]
        value = weights[i]
        index = i
        correct = hash_table_retrieve(ht, theRest)
        if correct is not None:
            #If there is an answer
            if i > correct:
                answer = (i, correct)
            else:
                answer = (correct, i)
            return answer
    return answer

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


print(get_indices_of_item_weights([4,6,10,15,16],5,21))