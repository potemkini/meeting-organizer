'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''


def find_max(t,z):
    #Write your alghoritm here.
    first_input_length = len(t)
    second_input_length = len(z)

    first_input_substrings = generate_substrings(t, first_input_length)
    second_input_substrings = generate_substrings(z, second_input_length)

    repetitions_substrings_array = []
    
    for item in first_input_substrings: # count how many times each substring occurs in the second input
        if item in second_input_substrings:
            repetitions_substrings_array.append(dict(substring=item, count=second_input_substrings.count(item)))

    # i've multiplied the length of the substring with the number of times it occurs in the second input)
    all_possible_results_array = [ len(item['substring']) * item['count'] for item in repetitions_substrings_array]
    maximum_value = max(all_possible_results_array) ## i've found the maximum result
  
    return -1

def generate_substrings(input, length_of_input):
    substring_list = []
    for starting_letter in range(length_of_input): # i've created a for loop that goes through all possible substrings of the input
        for target_letter in range(starting_letter + 1, length_of_input + 1): # each substring has a target letter that defines how long it should be
            substring_list.append(input[starting_letter: target_letter]) # i've appended each substring to a list

    return substring_list


if __name__ == '__main__':
    find_max("acldm1labcdhsnd","shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")