# def start():
#     print("Learning data file name?")
#     print("What would you like to do?")
#     print("1: Get the score of a word")
#     print("2: Get the average score of words in a file")
#     print("3: Find the highest/lowest scoring words in a file")
#     print("4: Sort the word in a file into positive.txt and negative.txt")
#     print("5: Exit the program")
#     print("Enter the number 1-5:")


a_file = open("training.txt", "r")
list_of_lists = []
for line in a_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_lists.append(line_list)

a_file.close()
my_dict = {}
for a in list_of_lists:
    my_dict = {a[0]: x for x in a}
    a.remove(a[0])
    for d in my_dict:




