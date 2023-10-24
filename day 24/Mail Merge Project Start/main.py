#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r'100 days of code\day 24\Mail Merge Project Start\Input\Names\invited_names.txt') as names:

    names =  names.readlines()
    names_size = len(names)
    for i in range(names_size):
        names[i] = names[i].strip('\n')
    print(names)

for name in range(names_size):
    with open(r'100 days of code\day 24\Mail Merge Project Start\Input\Letters\starting_letter.txt') as letter:
        letter = letter.readlines()
        letter[0] = letter[0].replace('[name]', names[name])

    with open(rf'100 days of code\day 24\Mail Merge Project Start\Output\{names[name]}.txt', mode='w') as edit_txt:
        for i in range(len(letter)):
            edit_txt.write(letter[i])


