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

class Hand():
    # define the Hand class
    # each hand will have 5 cards
    # each hand will have a type
    # types are five of a kind, four of a kind, full house, three of a kind, two pair, one pair, high card
    # each type will have a score equal to the first card in the hand
    # the cards are A, K, Q, J, t, 9, 8, 7, 6, 5, 4, 3, and 2

    def identify_cards(self):
        # identify the type of hand
        # create dictionary of counts per card face
        card_counts = {}
        for character in self.cards:
            # increment the count for the respective card type
            if character in card_counts:
                card_counts[character] += 1
            else:
                card_counts[character] = 1

            # print(character, card_counts)
        return card_counts

    def identify_hand_type(self):
        # if there are 5 of a kind, the type is 6
        # if there are 4 of a kind, the type is 5
        # if there are 3 of a kind, and 2 of another kind, the type is 4
        # if there are 3 of a kind, the type is 3
        # if there are 2 of a kind, and 2 of another kind, the type is 2
        # if there are 2 of a kind, the type is 1
        # if there are no pairs, the type is 0

        if 5 in self.card_counts.values():
            return 6
        elif 4 in self.card_counts.values():
            return 5
        elif 3 in self.card_counts.values():
            if 2 in self.card_counts.values():
                return 4
            else:
                return 3
        elif 2 in self.card_counts.values():
            if 2 in self.card_counts.values():
                return 2
            else:
                return 1
        else:
            return 0

    def get_card_value(self, card):
        # if it is a number, return the number
        if card.isdigit():
            return int(card)
        elif card == 'T':
            return 10
        elif card == 'J':
            return 11
        elif card == 'Q':
            return 12
        elif card == 'K':
            return 13
        elif card == 'A':
            return 14
        else:
            print(f"Error: {card} is not a valid card")
            return 0

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        # identify the type of hand
        self.card_counts = self.identify_cards()
        self.hand_type = self.identify_hand_type()

    def __lt__(self, other):
        # if the hand type is different, return the hand type with the higher value
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        # if the hand type is the same, determine the winner by comparing the cards
        else:
            for index, card in enumerate(self.cards):
                # we're not looking for the higest overall card, but comparing the cards in order
                # if the cards are the same, continue
                if card == other.cards[index]:
                    continue
                # if the cards are different, return the card with the lower value
                else:
                    print(f"comparing {card} to {other.cards[index]} in {self.cards} and {other.cards}")
                    return self.get_card_value(card) < self.get_card_value(other.cards[index])

        # Q: Why is 2 getting ranked higher than Q in this example?
        #   11	QQQJA	31   	   341	      1218
        #   12	Q2Q2Q	19   	   228	      1446
        # A: When looking at the second character, 2 is higher than Q
        #    This is because the get_card_value function returns 0 for Q


if __name__ == '__main__':
    # Read input.txt into a pandas DataFrame
    input_data = read_input()

    # Now you can use the input_data DataFrame in the rest of your code
    if input_data is not None:

        # make a list of hands
        hands = []
        # for each row in the input data
        for index, row in input_data.iterrows():
            # split on ' '
            split = row['input'].split(' ')
            hand = Hand(split[0], split[-1])
            # add the hand to the list of hands
            hands.append(hand)

        # sort the list of hands descending
        hands.sort()

        sum = 0
        # print all the hands
        for hand in hands:
            # winnings is bid * index + 1
            winnings = int(hand.bid) * (hands.index(hand) + 1)
            sum += winnings
            # fixed width formatting sufficient for 1000	23KAT	418	418000	247691671
            print(f"{hands.index(hand) + 1:4}\t{hand.cards:5}\t{hand.bid:5}\t{winnings:6}\t{sum:10}")


