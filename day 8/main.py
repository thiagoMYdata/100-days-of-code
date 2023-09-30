from art import logo

# print(logo)

def caesar_cipher(command:str, message:str, shift_num:int):
    from string import ascii_lowercase
    abc = ascii_lowercase
    abc_shifted = abc[shift_num:] + abc[:shift_num]

    memory = {}
    
    if command == 'encode':
        for index ,letter in enumerate(message):
            key_dic = letter
            if key_dic in memory:
                memory[key_dic].append(index)
            else:
                memory[key_dic] = [index]

        for index, letter in enumerate(abc):
            if letter in memory:
                memory[letter].append([index])

        for keys in memory.keys():
            for i in memory[keys][:-1]:
                message = message[:i] + abc_shifted[memory[keys][-1][0]] + message[i+1:]
        return message

    if command ==  'decode':

        for index ,letter in enumerate(message):
            key_dic = letter
            if key_dic in memory:
                memory[key_dic].append(index)
            else:
                memory[key_dic] = [index]

        for index, letter in enumerate(abc_shifted):
            if letter in memory:
                memory[letter].append([index])

        
        for keys in memory.keys():
            for i in memory[keys][:-1]:
                message = message[:i] + abc[memory[keys][-1][0]] + message[i+1:]
        return message
            
        









while True:

    user_command = input('Type \'encode\' to encrypt, type \'decode\' to decrypt: ')
    user_message = input('Type your message: ')
    user_shift_num = int(input('Type the shift number: '))


    extract =  caesar_cipher(user_command, user_message, user_shift_num)
    print(extract)
    restart = input('Do u wanna restart the program[Y/N]:').upper()
    if restart == 'N': break








# memory = []



#  #[['c',[0],[2]],    ['a',[1,3],[0]],    ['s'[2],[18]]]

# for i in range(len(user_message)):
#     for j in range(len(abc)):
#         if abc[j] == menssage[i]:

#             memory.key('a') += j



# word = 'home'






