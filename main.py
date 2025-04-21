from countingSort import countingSort
from countingSort import countingSort_tup
from data_files.read_files import read_fruit_prices

if __name__ == '__main__':

    ok = read_fruit_prices()
    words = []
    prices = []
    for tup in ok:
        words.append(tup[0])
        prices.append(tup[1])


    try:
        print(countingSort(prices))
        print(countingSort_tup(ok, 1))
    except Exception as e:
        print(e)

    # try:
    #     print(countingSort(['cab', 'cba', 'ass', 'abc','abb', 'bc', 'ba', 'bbc', 'bda', 'bea', 'bf']))
    #     words = ["apple", "banana", "grape", "cherry", "date"]
    #     print(countingSort(words))
    #     words = ["apple", "banana", " grape", ",cherry", "date"]
    #     print(countingSort(words))
    # except Exception as e:
    #     print(e)

    # try:
    #     result = countingSort([4, 9, 20, 3, 7, 4, 8])  # Valid
    #     print(result)
    #     # Large random sequence
    #
    #
    #     result = countingSort([42, 17, 99, 1, 78, 56, 32, 8, 21, 5, 89, 63, 14, 92, 31, 77, 46])
    #     print(result)
    #
    #     # Reverse-sorted list
    #     result = countingSort([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])
    #     print(result)
    #
    #     # Already sorted list
    #     result = countingSort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    #     print(result)
    #
    #     # List with duplicates
    #     result = countingSort([5, 3, 9, 5, 3, 9, 2, 8, 8, 1, 4, 4])
    #     print(result)
    #
    #     # Negative and positive values
    #     result = countingSort([-10, -1, -5, 0, 3, 7, -2, 6])
    #     print(result)
    #
    #     # Large range of numbers
    #     result = countingSort(list(range(1000, 0, -1)))  # Sorting from 1000 down to 1
    #     print(result)
    #
    #
    #     #sort(["a", "b", 3])  # Raises TypeError
    # except Exception as e:
    #     print(e)
    #
    #
    #
    #
    # try:
    #     countingSort([3, "hello", 7.5, None])  # Raises TypeError
    # except Exception as e:
    #     print(e)
    #
    # try:
    #     countingSort(["apple", "orange", "banana", 10])  # Raises TypeError
    # except Exception as e:
    #     print(e)