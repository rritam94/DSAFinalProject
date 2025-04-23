from countingSortTest import countingSort
from countingSortTest import countingSort_tup
from read_files import read_fruit_prices

if __name__ == '__main__':
    ok = read_fruit_prices()
    words = []
    prices = []

    try:
        print(countingSort(prices))
        print(countingSort_tup(ok, 1))
    except Exception as e:
        print(e)