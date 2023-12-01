import os
import pandas as pd

def read_input():
    try:
        current_dir = os.path.abspath(os.path.dirname(__file__))
        input_path = os.path.join(current_dir, 'input.txt')

        df = pd.read_csv(input_path, header=None)  # Adjust parameters as needed
        return df
    except FileNotFoundError:
        print("File not found: input.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

    return None

if __name__ == '__main__':
    # Read input.txt into a pandas DataFrame
    input_data = read_input()

    # Now you can use the input_data DataFrame in the rest of your code
    if input_data is not None:
        sum = 0
        # for each row
        for index, row in input_data.iterrows():
            first = 0
            last = 0

            # find the first number in the row
            for i in range(0, len(row[0])):
                # get character in position i
                character = row[0][i]
                # is the character a number?
                if character.isdigit():
                    first = character
                    break
                else:
                    continue

            # find the last number in the row
            for i in range(len(row[0]) - 1, -1, -1):
                # get character in position i
                character = row[0][i]
                # is the character a number?
                if character.isdigit():
                    last = character
                    break
                else:
                    continue

            # concatenate the first and last numbers
            number = first + last
            # add the number to the sum
            sum += int(number)

        # print the sum
        print(sum)
