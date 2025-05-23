def palindrome(user_string):
    """"
    A function to check whether a string is a palindrome.
    After google research I decide to keep common convention about palindrome:
    - empty string is palindrome
    - ignore case: "Madam" → valid palindrome
    - ignore spaces: "nurses run" → valid palindrome
    - ignore punctuation: "A man, a plan, a canal: Panama" → valid palindrome
    """
    # edge case is None or True/False is sent as parameter
    if not isinstance(user_string, str):
        print(f"Input ({user_string}) is not a string, cannot check palindrome")
        return
    # create an array to keep filtered chars
    if not user_string or user_string.isspace():
        print("Empty or only whitespace string, still considered palindrome")
        return
    # create an array to keep filtered chars
    user_string_filtered = []

    # 1. keep only lower case letters and digits
    for char in user_string:
        if char.isalnum():
            user_string_filtered.append(char.lower())

    # 2. Iterate through half of array and compare char in front
    # with corresponding char in the back
    length = len(user_string_filtered)
    for i in range(length//2):
        if user_string_filtered[i] != user_string_filtered[- (i + 1)]:
            print(f"entered string ({user_string})  is not palindrome")
            return   # fail-fast principe, no need to continue
    print(f"entered string ({user_string})  is palindrome")


if __name__ == "__main__":
    # flow of program: prompt user for input as long as
    # user don't type q, run test cases after, then end program

    user_string = input("Enter a string you want to check for palindrome, "
                        "q for quit: ")
    while user_string != "q":
        palindrome(user_string)
        user_string = input("Enter a string you want to check for palindrome, "
                            "q for quit: ")

    print()
    print("Now running testcases:")

    test_cases = [
        "taco Cat",     # True
        "1010",           # False (as string '1010' reversed is '0101')
        "Was it a car or a cat I saw?",  # True
        {"a": "b", "b": "a"},  # True (dict to string)
        None,           # False
        False,          # False (bool to string 'False')
        ""              # True (empty string is palindrome)
    ]

    for case in test_cases:
        palindrome(case)