blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new transaction as well as the last blockchain transaction to the blockchain

    Arguments:
        :transaction_amount: The amount that should be added
        :last_transaction: The last blockchain transaction (default [1])
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print("Outputting Block")
        print(block)


def verfiy_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


while True:
    print('Please choose')
    print('a: Add a new transaction value')
    print('o: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == 'a':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == 'o':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('Provide a valid choice')
    if not verfiy_chain():
        print('Invalid blockchain')
        break

print('Done!')
