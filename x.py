def sentence():
    test = list(string)

    for i in range(len(test)):

        # convert to lowercase if its an uppercase character
        if 'A' <= test[i] <= 'Z':
            test[i] = chr(ord(test[i]) + 32)
            # Print space before the uppercase character
            if i != 0:
                print("", end="")
            # print character
            print(test[i], end="")
        # if it lower character, just print.
        else:
            print(test, end="")


if __name__ == "__main__":
    string = "HelpMe"
    sentence()
