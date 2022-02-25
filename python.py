def match_restOf(mainStr, patternStr):

    for indx in range(len(mainStr)):  # loop to itarate
        if mainStr[indx] != patternStr[indx]:  # if any  character not matched.
            return 0  # if not matched, any of the character then return 0

    return 1  # if match complete the return 1


def match_count(mainStr, patternStr):  # receiving two string as parameters
    # using this variable to count number of time matches the pattern.
    countMatch = 0

    for indx in range(len(mainStr)):

        # iterating through the main string and matching with the first character of pattern string
        if patternStr[0] == mainStr[indx]:

            # checking the number of character left in main string to match. if there is sufficient enough to match then need to call the function
            if (indx+len(patternStr)) <= len(mainStr):

                # Now calling the function to match rest of the pattern character, of match complete the it returns 1, other wise 0
                countMatch += match_restOf(
                    mainStr[indx+1:indx+len(patternStr)], patternStr[1:len(patternStr)])

    return countMatch  # returning the tottal match count


# main function starts()

# taking input ## calling this string as main string
input_String = input("Please enter the sample string: ")

# taking input  ## calling this string as pattern string
pattern_string = input("Enter the pattern string: ")

# calling the function and printing the number of match (return value).
print(match_count(input_String, pattern_string))

# sample input:
# main string: tadadattaetadadadafa
# pattern string: dada

# output: 3
