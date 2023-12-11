#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    bestkey = None
    max_score = float('-inf')
    
    for key, score in a_dictionary.items():
        if isinstance(score, int) and score > max_score:
            bestkey = key
            max_score = score
    
    return bestkey
    
if __name__ == '__main__':
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
