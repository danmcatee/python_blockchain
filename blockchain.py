blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    """ Append a new value as well as the last blockchain value to the blockchain

    Arguments:
        :transaction_amount: The amount that should be added
        :last_transaction: The last blockchain transaction (default [1])
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    return float(input('Your transaction amount please: '))


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print("Outputting Block")
        print(block)


while True:
    print('Please choose')
    print('a: Add a new transaction value')
    print('o: Output the blockchain blocks')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == 'a':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == 'o':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Provide a valid choice')

print("Done!")
