def find_longest_string(lst): #Finds the Longest String in a list
    longest_so_far=""
    for s in lst:
        if len(s)>len(longest_so_far):
            longest_so_far=s
    return longest_so_far

list_of_words = {"He","Lo", "Thumb"}
print(find_longest_string(list_of_words))
