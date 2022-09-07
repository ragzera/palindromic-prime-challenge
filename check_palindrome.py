def palindrome_check(stringInput):
    if stringInput == stringInput[::-1]:
        return True
    else:
        return False


def main():
    while True:
        stringInput = input("Enter a string: ")
        if palindrome_check(stringInput):
            print(stringInput, "is a palindrome.")
        else:
            print(stringInput, "is not a palindrome.")

if __name__ == "__main__":
    main()