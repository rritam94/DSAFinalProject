from backend.countingSort import countingSort
from backend.countingSort import countingSort_tup
from data_files.read_files import read_fruit_prices
import random
import time






def generate_random_integers(count, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(count)]




if __name__ == '__main__':
    random_integers = generate_random_integers(100000, -100, 100)

    start_countingSort = time.time()
    countingSort_result = countingSort(random_integers)
    end_countingSort = time.time()
    countingSort_time = end_countingSort - start_countingSort

    start_sorted = time.time()
    sort_result = sorted(random_integers)
    end_sorted = time.time()
    sorted_time = end_sorted - start_sorted


    print(f"CountingSort Time: " + str(countingSort_time))
    print(f"Built-in Sorted Time: " + str(sorted_time))
    print("Results match: " + str(countingSort_result == sort_result))


    ok = read_fruit_prices()


    # try:
    #     print(countingSort_tup(ok, 1))
    # except Exception as e:
    #     print(e)

    # try:
    #     print(countingSort(['cab', 'cba', 'ass', 'abc','abb', 'bc', 'ba', 'bbc', 'bda', 'bea', 'bf']))
    #     words = ["apple", "banana", "grape", "cherry", "date"]
    #     print(countingSort(words))
    #     words = ["apple", "banana", " grape", ",cherry", "date"]
    #     print(countingSort(words))
    # except Exception as e:
    #     print(e)

    # try:
    #
    #
    #     result = countingSort([42, 17, 99, 1, 78, 56, 32, 8, 21, 5, 89, 63, 14, 92, 31, 77, 46])
    #     print(result)
    #
    #
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