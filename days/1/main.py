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

def get_position_of_first_digit(string):
    for i in range(0, len(string)):
        character = string[i]
        if character.isdigit():
            return i

    return None

def get_position_of_last_digit(string):
    for i in range(len(string) - 1, -1, -1):
        character = string[i]
        if character.isdigit():
            return i

    return None

def find_numbers(string):
    for n in numbers_df['number']:
        # get first index of number
        first = string.find(n)
        # get last index of number
        last = string.rfind(n)

        # if > -1 set the data in the numbers_df
        if first > -1:
            numbers_df.loc[numbers_df['number'] == n, 'first'] = first
        if last > -1:
            numbers_df.loc[numbers_df['number'] == n, 'last'] = last

if __name__ == '__main__':
    # Read input.txt into a pandas DataFrame
    input_data = read_input()

    # Now you can use the input_data DataFrame in the rest of your code
    if input_data is not None:
        sum = 0
        # for each row in the input data
        for index, row in input_data.iterrows():
            # print (row[0])
            first_digit_position = get_position_of_first_digit(row[0])
            last_digit_position = get_position_of_last_digit(row[0])
            # print("first digit position: " + str(first_digit_position))
            # print("last digit position: " + str(last_digit_position))

            numbers_df = pd.DataFrame(columns=['number', 'value', 'first', 'last'])
            numbers_df.loc[0] = ['one', 1, None, None]
            numbers_df.loc[1] = ['two', 2, None, None]
            numbers_df.loc[2] = ['three', 3, None, None]
            numbers_df.loc[3] = ['four', 4, None, None]
            numbers_df.loc[4] = ['five', 5, None, None]
            numbers_df.loc[5] = ['six', 6, None, None]
            numbers_df.loc[6] = ['seven', 7, None, None]
            numbers_df.loc[7] = ['eight', 8, None, None]
            numbers_df.loc[8] = ['nine', 9, None, None]

            find_numbers(row[0])
            # if first and last are None, drop it
            numbers_df = numbers_df.dropna(subset=['first', 'last'])
            # print the numbers_df
            # for index, row in numbers_df.iterrows():
            #     print(row['number'] + ": " + str(row['first']) + ", " + str(row['last']))

            # if the numbers_df is empty, use the digits
            if numbers_df.empty:
                # get the char at the first digit position and last digit position
                number = row[0][first_digit_position] + row[0][last_digit_position]
            else:
                # get the rows from the numbers_df representing the first and last numbers (one, two, three, etc.)
                first_number = numbers_df.loc[numbers_df['first'].idxmin()]
                last_number = numbers_df.loc[numbers_df['last'].idxmax()]

                # set the first and last values base on whether a digit or number word appears first
                if first_number['first'] < first_digit_position:
                    # get the value from the numbers_df
                    first = first_number['value']
                else:
                    # get the char at the first_number first position
                    first = row[0][first_digit_position]

                # set the first and last values base on whether a digit or number word appears last
                if last_number['last'] > last_digit_position:
                    # get the char at the last digit position
                    last = last_number['value']
                else:
                    # get the char at the last_number last position
                    last = row[0][last_digit_position]

                number = str(first) + str(last)

            # print("first number: " + str(first_number['number']) + ", " + str(first_number['value']))
            # print("last number: " + str(last_number['number']) + ", " + str(last_number['value']))

            # add the number to the sum
            sum += int(number)

            # print(number)
            # print()

        # print the sum
        print(sum)

