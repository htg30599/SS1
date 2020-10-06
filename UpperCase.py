def to_sentence_case(string):
    ending = []
    for i in range(len(string)):
        if string[i] == '.':
            ending.append('.')
        elif string[i] == '?':
            ending.append('?')
        elif string[i] == '!':
            ending.append('!')

    string = string.replace('.', '?').replace('.', '!')
    sentence = string.split('.')
    while '' in sentence:
        sentence.remove('')



    for i in range(len(sentence)):
        sentence[i] = sentence[i].lstrip(' ')
        sentence[i] = sentence[0]

    new_string = ' '
    for i in range(len(sentence)):
        new_string += sentence[i]
        new_string += ending[i] + ' '
    new_string = new_string[:-1]
    return new_string
    return sentence


user_string = input("Enter string with lowcase:")
print("In sentence case, your sentences look like:")
print(to_sentence_case(user_string))
