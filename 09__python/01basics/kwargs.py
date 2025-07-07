# kward arguments
"""
Input: Multiple values for minutes, key=value pair activity
Output : Return sum of minutes + random minutes spend on an activity
"""

import random


def time_activity(*args, **kvargs):
    # print(args)
    # print(kvargs)
    min = sum(args) + random.randint(0, 80)
    # print(min)
    choice = random.choice(
        list(kvargs.values())
    )  # run tuples thats why convert to list
    # print(choice)
    print(f"Your spend {min} minutes on {choice}.")


time_activity(10, 20, 30, hobby="Anime", sport="Football", fun="driving", work="Devops")
