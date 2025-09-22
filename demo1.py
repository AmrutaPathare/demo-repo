def reverse_string(s: str) -> str:
    """
    Return the reversed version of the input string.
    """
    return s[::-1]


# Simple tests
if __name__ == "__main__":
    assert reverse_string("") == ""
    assert reverse_string("abc") == "cba"
    assert reverse_string("racecar") == "racecar"
    assert reverse_string("Hello, world!") == "!dlrow ,olleH"
    print("All tests passed.")