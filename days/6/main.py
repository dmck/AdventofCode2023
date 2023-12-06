import os
import pandas as pd


def part1():
    # make a dataframe with, columns time and distance, and values
    # Time:        44     89     96     91
    # Distance:   277   1136   1890   1768

    df = pd.DataFrame({'Time': [44, 89, 96, 91], 'Distance': [277, 1136, 1890, 1768]})
    # add columns 0-100 with values of False
    for i in range(100):
        df[i] = False

    options_overall = []
    for index, row in df.iterrows():
        options_for_this_game = 0
        # print(row['Time'], row['Distance'])
        for seconds in range(0, 100):
            if seconds > row['Time']:
                break
            else:
                speed = seconds
                time_remaining = row['Time'] - seconds
                distance = speed * time_remaining
                if distance > row['Distance']:
                    df.loc[index, seconds] = True
                    # print(f"Seconds: {seconds}, Speed: {speed}, Time Remaining: {time_remaining}, Distance: {distance}")
                    options_for_this_game += 1
        options_overall.append(options_for_this_game)

    result = 1
    for item in options_overall:
        result *= item

    print(result)


def part2():
    # 44,899,691
    # 277,113,618,901,768

    x = 0
    speed = x
    time_remaining = 44899691 - x
    # 277113618901768 = speed * time_remaining

    # ask ChatGPT...

    # To solve the equation `277113618901768 = x * (44899691 - x)`, we can use the quadratic formula ` x = (-b +-
    # sqrt(b^2 - 4ac)) / 2a`. In this case, the equation can be rewritten in the form of `ax^2 + bx + c = 0` as `x^2
    # - 44899691x + 277113618901768 = 0`. Here, `a = 1`, `b = -44899691`, and `c = 277113618901768`.
    #
    # Here is the Python code to solve this equation:
    #
    # ```python
    import math

    # coefficients
    a = 1
    b = -44899691
    c = 277113618901768

    # calculate the discriminant
    D = b ** 2 - 4 * a * c

    # calculate the two solutions
    x1 = int((-b - math.sqrt(D)) / (2 * a))
    x2 = int((-b + math.sqrt(D)) / (2 * a))

    # print(x1, x2)
    # ```
    #
    # This code first calculates the discriminant `D` and then uses it to find the two solutions `x1` and `x2` of the
    # quadratic equation. The solutions are then printed out.

    # cast to int
    # validate ChatGPT's answer
    speed = x1
    time_remaining = 44899691 - x1
    print(x1, speed * time_remaining)
    speed = x2
    time_remaining = 44899691 - x2
    print(x2, speed * time_remaining)

    print(x2 - x1)


if __name__ == '__main__':
    # part1()
    part2()
