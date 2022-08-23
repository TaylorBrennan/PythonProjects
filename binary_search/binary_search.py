#pylint: disable=R1705
"Simple Binary Search based on a number array and user entered number."

import sys

def main():
    "Main Function."
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("[Error] Invalid input")
        sys.exit(1)
    index = binary_search(array, number)
    if index is None:
        print("Number not found.")
    else:
        print(f"Number found at index: {index}")

def binary_search(array, number):
    "Binary Search Algorithm."
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == number:
            return mid
        elif array[mid] < number:
            low = mid + 1
        else:
            high = mid - 1
    return None


if __name__ == "__main__":
    main()
    