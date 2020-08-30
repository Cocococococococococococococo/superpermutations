from math import factorial
from random import randint

def main():

    num_of_elements = input('Please enter number of elements\n')

    init_test_length = factorial(num_of_elements) + factorial(num_of_elements-1) + factorial(num_of_elements-2) + num_of_elements - 3
    final_test_length = init_test_length + factorial(num_of_elements-3)

    for n in range (init_test_length,final_test_length):



#checks if a given sequence is a superpermutation of numel elements
def is_superperm(num_elements,sequence):

    perm = gen_perm(num_elements)
    #for each permutation, check if it appears in the sequence
    is_superperm_b = True
    for i in range (len(perm)):
        perm_in = False
        for j in range(len(sequence)-num_elements):
            match = True
            for k in range(num_elements):
                match = (sequence[j+k] == perm[k])
                if not match: break
            perm_in = match
            if perm_in: break
        if not perm_in: 
            is_superperm_b = False
            break
    return is_superperm_b


#generates all permutations of a given number of elements
def gen_perm(num_elements):
    