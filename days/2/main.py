import os
import pandas as pd

def read_input():
    try:
        current_dir = os.path.abspath(os.path.dirname(__file__))
        input_path = os.path.join(current_dir, 'input.txt')

        df = pd.DataFrame(columns=['input'])
        # read rows using python
        with open(input_path, 'r') as f:
            for line in f:
                df = df._append({'input': line.strip()}, ignore_index=True)
        return df
    except FileNotFoundError:
        print("File not found: input.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

    return df

def get_highest(row, color):
    # Split on color
    tokens = row['input'].split(' ' + color)

    occurrences = []
    if len(tokens) > 1:
        # for each token before the last
        for token in tokens[:-1]:
            # get the last number in the token
            occurrences.append(int(token.split(' ')[-1]))
            # print(f"Occurrences: {occurrences}")

    # return the highest number
    return max(occurrences)


if __name__ == '__main__':
    # Read input.txt into a pandas DataFrame
    input_data = read_input()

    # add columns to the DataFrame for red, blue, green
    input_data['red'] = 0
    input_data['blue'] = 0
    input_data['green'] = 0
    # Now you can use the input_data DataFrame in the rest of your code
    if input_data is not None:

        # for each row in the input data
        for index, row in input_data.iterrows():
            # Extract the numbers between the first ' ' and the first ':' using regex
            input_data.loc[index, 'game'] = row['input'].split(' ')[1][:-1]
            # write regex to extract the numbers in '12 red' which may appear multiple times in a row

            # Get the highest occurrence of each color
            input_data.loc[index, 'red'] = get_highest(row, 'red')
            input_data.loc[index, 'blue'] = get_highest(row, 'blue')
            input_data.loc[index, 'green'] = get_highest(row, 'green')

            # print(f"Game: {input_data.loc[index, 'game']}, Red: {input_data.loc[index, 'red']}, Blue: {input_data.loc[index, 'blue']}, Green: {input_data.loc[index, 'green']}")

        # Drop rows where color appears more more than max
        input_data = input_data[input_data['red'] <= 12]
        input_data = input_data[input_data['blue'] <= 14]
        input_data = input_data[input_data['green'] <= 13]

        # print stats about the DataFrame
        print(input_data.describe())

        # print the length of the DataFrame
        print(f"Number of rows: {len(input_data)}")

        sum = 0
        for index, row in input_data.iterrows():
            # print(row['game'])
            sum += int(row['game'])

        print(f"Sum: {sum}")