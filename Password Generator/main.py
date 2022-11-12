import random

#Options for passwords
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#WelcomeMsg
print("Welcome to the Password Generator! ")

#UserInputs
nr_letters = int(input(f"Type the required amount of letters. \n"))
nr_numbers = int(input(f"Type the required amount of numbers. \n"))
nr_symbols = int(input(f"Type the required amount of symbols. \n"))

#RangeMax for input validaiton on respective character sets
rangeMaxLtr = len(letters)
rangeMaxNum = len(numbers) 
rangeMaxSymbl = len(symbols)
1
if nr_letters >= rangeMaxLtr + 1 or nr_letters <= 0 :
    print("You have selected too few or too many letters")
elif nr_numbers >= rangeMaxNum + 1 or nr_numbers <= 0  :
    print("You have selected too few or too many numbers")
elif nr_symbols >= rangeMaxSymbl + 1 or nr_symbols <= 0  :
    print("You have selected too few or too many symbols")
else:
    
    #RangeMax for which numbers to select from list
    rangeMaxLtr = len(letters) - 1
    rangeMaxNum = len(numbers) - 1 
    rangeMaxSymbl = len(symbols) - 1
    
    #Creating list for 'letters' list indexes
    ltr_index_list = []
    for ltr in range(0, nr_letters):
        ltrIndex = random.randint(0, int(rangeMaxLtr))
        ltr_index_list.append(ltrIndex)
        
    #Using created index list to chose 'letter' options for passwords
    letters_choosen = []
    for index in ltr_index_list:
        choosen = letters[index]
        letters_choosen.append(choosen)
    
    #Creating list for 'numbers' list indexes
    num_index_list = []
    for num in range(0, nr_numbers):
        numIndex = random.randint(0, int(rangeMaxNum))
        num_index_list.append(numIndex)
    
    #Using created index list to chose 'number' options for passwords
    numbers_choosen = []
    for index in num_index_list:
        choosen = numbers[index]
        numbers_choosen.append(choosen)
    
    #Creating list for 'symbols' list indexes
    symbl_index_list = []
    for symb in range(0, nr_symbols):
        symbIndex = random.randint(0, int(rangeMaxSymbl))
        symbl_index_list.append(symbIndex)
    
    #Using created index list to chose 'symbol' options for passwords
    symbols_choosen = []
    for index in symbl_index_list:
        choosen = symbols[index]
        symbols_choosen.append(choosen)
    
    #Final List for Password Characters
    total_characaters = letters_choosen + numbers_choosen + symbols_choosen
   
    #Randomnizing and concating 
    passwordRandomnized = random.sample(total_characaters, len(total_characaters))
    
    password = ''
    for i in passwordRandomnized:
        password += i
    #Output Visual
    print(f"Your new password is : {password}")