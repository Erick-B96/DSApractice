"""A project to practice string use.
   Prompt user input,
   count characters with/without spaces,
   split sentence into words,
   calculate word frequency in user input,
   convert letters into all upper or all lower case,
   reverse the sentence,
   check if it is a palindrome.  
"""

def main():
    # Get user input and save as string
    user_input = input(f"Write a sentence: ")
    
    # Count characters in sentence with and without spaces
    character_with_spaces = len(user_input)
    print(f"character count with spaces is: {character_with_spaces}")
    
    character_without_spaces = len(user_input.replace(" ", ""))
    print(f"Character count without spaces is: {character_without_spaces}")
    
    # Split sentence into individual words and count them
    word_count = len(user_input.split())
    print(f"Word count is: {word_count}")
    
    # Word frequency
    wl_chosen = input(f"Give word or you want the frequency of: ")
    
    word_frequency = user_input.count(wl_chosen)
    
    print(f"Frequency of {wl_chosen} is: {word_frequency}")
        
    # Case conversion
    print(f"All uppercase: {user_input.upper()}")
    
    print(f"All lowercase: {user_input.lower()}")
    
    # Reverse sentence
    reverse_words = ''.join(user_input.split()[::-1])
    print(f"Reverse sentence: {reverse_words}")
    
    # Palindrome checker
    if user_input == reverse_words:
        print(f"Is palindrome")
    else:
        print(f"Not palindrome")
    
    
if __name__ == "__main__":
    main()   