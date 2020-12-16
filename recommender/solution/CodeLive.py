file =open('ratings-small.txt')
str = file.read()
arr=str.split('\n')
rs =[]
while len(arr) >=3 :
    arr1=[]
    arr1.append(arr[0])
    arr.remove(arr[0])
    arr1.append(arr[0])
    arr.remove(arr[0])
    arr1.append(arr[0])
    arr.remove(arr[0])
    rs.append(arr1)
dict = {}
user = []
book =[]
rate = []
for v in rs:
    dict[v[0]] = v[2]
    user.append(v[0])
    book.append(v[1])
    rate.append(v[2])



book.sort()

print(book)

print(dict)






def main():
    print('Welcome to the CSC110 Book Recommender. Type the word in the left column to do the action on the right.')
    print('recommend: recommend books for a particular user')
    print('averages: output the average ratings of all books in the system')
    print('quit: exit the program')
    print('next task?')

def averages():
    pass