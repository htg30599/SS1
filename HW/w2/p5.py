def main():
    vowels =0
    cons = 0
    get_string = input("Enter a sentence: ")

    vowels = vowel_counter(get_string)

    cons = cons_counter(get_string)

    print('The string you entered includes', vowels, \
          'vowels and', cons, 'consonants.')

def vowel_counter(string):
    count = 0
    vowels ='aeiou'
    for ch in string:
        if vowels.find(ch) >= 0:
            count = count + 1

    return count

def cons_counter(string):
    count = 0
    cons = 'bcdfghjklmnpqrstvwxyz'

    for ch in string:
        if cons.find(ch) >= 0:
            count = count + 1

    return count

main()