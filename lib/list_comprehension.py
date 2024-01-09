def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]

# Examples
evens_result = return_evens([0, 1, 3, 5, 7, 8, 9])
exclamation_result = make_exclamation(["Hello", "I'm doing great", "Python is fun"])

print(evens_result)          
print(exclamation_result)    
