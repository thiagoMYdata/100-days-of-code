from art import logo

# calculator
# Add
def add(n1,n2):
    return n1 + n2

# Subtract
def subtract(n1,n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1,n2):
    return n1 / n2



def calculator():
    print(logo)
    
    operation_action = {'+': add, '-':subtract, '*':multiply, '/':divide }

    continue_playing = None

    while  not continue_playing != 'y' or continue_playing == None:
        if continue_playing == None:
            num_1 = float(input('What\'s the next number?: '))
        num_2 = float(input('What\'s the next number?: '))

        for i in operation_action.keys(): print(i)
        operation_symbol = input('Pick an operation from the line above: ')

        answer = operation_action[operation_symbol](num_1,num_2)
        print(f'{num_1} {operation_symbol} {num_2} = {answer}')
        num_1 = answer
        
        continue_playing = input(f'Type \'y\' to continue calculating with {answer}. Or \'n\' to start a new calculator.: ')
        if continue_playing == 'n':
            calculator()
        
calculator()




# for i in calculator.keys(): print(i)

