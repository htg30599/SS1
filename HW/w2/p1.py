def main():
    full_name = input("Enter your full name please:")
    name = full_name.split()
    for string in name:
        print(string[0].upper(), sep="", end="")
        print(" ", sep="", end="")


main()
