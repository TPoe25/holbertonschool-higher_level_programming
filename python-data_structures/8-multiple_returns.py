#!/usr/bin/python3

def multiple_returns(sentance):
    if not sentance:
        return (0, None)
    else:
        return (len(sentance), sentance[0])
    
if __name__ == "__main__":
    sentance = "At school, I learnt C!"
    length, first = multiple_returns(sentance)
    print("Length: {:d} - First character: {}".format(length, first))
