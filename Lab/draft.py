import numpy as np

a = np.zeros((2, 2))  # T¤o array vîi t§t c£ c¡c ph¦n tû 0
print(a)  # Prints "[[ 0. 0.]
# [ 0. 0.]]"
b = np.ones((1, 2))  # T¤o array vîi c¡c ph¦n tø 1
print(b)  # Prints "[[ 1. 1.]]"
c = np.full((2, 2), 7)  # T¤o array vîi c¡c ph¦n tû 7
print(c)  # Prints "[[ 7. 7.]
# [ 7. 7.]]"
d = np.eye(2)  # T¤o identity matrix k½ch th÷îc 2*2
print(d)  # Prints "[[ 1. 0.]
# [ 0. 1.]]"
e = np.random.random((2, 2))  # T¤o array vîi c¡c ph¦n tû ÷ñc t¤o ng¨u nhi¶n
print(e)  # Might print "[[ 0.91940167 0.08143941]
# [ 0.68744134 0.87236687]]"
