import os
import pandas as pd

if __name__ == '__main__':
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
        print(row['Time'], row['Distance'])
        for seconds in range(0, 100):
            if seconds > row['Time']:
                break
            else:
                speed = seconds
                time_remaining = row['Time'] - seconds
                distance = speed * time_remaining
                if distance > row['Distance']:
                    df.loc[index, seconds] = True
                    print(f"Seconds: {seconds}, Speed: {speed}, Time Remaining: {time_remaining}, Distance: {distance}")
                    options_for_this_game += 1
        options_overall.append(options_for_this_game)

    result = 1
    for item in options_overall:
        result *= item

    print(result)