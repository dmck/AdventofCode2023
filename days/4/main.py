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


if __name__ == '__main__':
    # Read input.txt into a pandas DataFrame
    input_data = read_input()

    # Now you can use the input_data DataFrame in the rest of your code
    if input_data is not None:

        sum = 0
        # for each row in the input data
        for index, row in input_data.iterrows():

            # winning_numbers = row['input'][10:40]
            # split on the space which may be multiple
            winning_numbers = row['input'][10:40].split(' ')
            print(winning_numbers)
            # sort
            winning_numbers.sort()

            ticket_numbers = row['input'][42:].split(' ')
            print(ticket_numbers)
            # sort
            ticket_numbers.sort()

            # find all the matching numbers
            matching_numbers = []
            for winning_number in winning_numbers:
                if winning_number in ticket_numbers:
                    if winning_number != '':
                        matching_numbers.append(winning_number)
                        # print(f"Found a match: {winning_number}")

            value = 0
            if len(matching_numbers) == 1:
                print(f"Found {len(matching_numbers)} matching numbers: {matching_numbers}")
                value = 1
            elif len(matching_numbers) == 2:
                print(f"Found {len(matching_numbers)} matching numbers: {matching_numbers}")
                value = 2
            elif len(matching_numbers) >= 3:
                print(f"Found {len(matching_numbers)} matching numbers: {matching_numbers}")
                # value should double... 1, 2, 4, 8, 16, 32, 64, 128, 256, 512
                value = 2 ** (len(matching_numbers) - 1)
                print(f"Value: {value}")
            sum += value

        print(f"Sum: {sum}")
