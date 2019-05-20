from collections import OrderedDict

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def get_belt(user_score):
    belt_achieved = ""
    if user_score == 0 or user_score < 10:
        return None
    elif user_score > 1000:
        return 'red'
    for i in range(10,user_score+1):
        for k,v in HONORS.items():
            if i >= k:
                belt_achieved = v
    return belt_achieved