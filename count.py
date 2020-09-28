def main():
    # Ask user input a string

    string = input('Enter a sentence: ')

    strings = string.lower()
    # create counter & total counter function
    counter = 0
    total_counter = 0

    most_frequent_character = ''
    # let i is the most frequent character, if it appear, count +1
    for i in strings:
        for j in strings:
            if j == i:

                counter += 1
        if counter > total_counter:
            total_counter = counter
            most_frequent_character = i
        counter = 0

    print("The most frequent character is", most_frequent_character, "and it appears", total_counter, "times.")


main()
