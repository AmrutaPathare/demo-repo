def reverse_string(s: str) -> str:
    """
    Return the reverse of the input string.
    """
    return s[::-1]
    if __name__ == "__main__":
        user_input = input("Enter a string to reverse: ")
        print("Reversed String:", reverse_string(user_input))
        print(reverse_string(user_input)