import json
from datetime import datetime

# function to get the date from the tweet
def get_date(tweet):
    timestamp_string = tweet.get('timestamp')
    
    if not timestamp_string:
        return datetime.min
    
    try:
        if timestamp_string.endswith('Z'):
            return datetime.fromisoformat(timestamp_string.replace('Z', '+00:00'))
        
        return datetime.fromisoformat(timestamp_string)
    
    except ValueError:
        print('cant parse date')


# function to heapify the tweets by date
def heapify_by_date(tweets_array, size, root_index):
    largest_index = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2
    
    if left_child < size and get_date(tweets_array[left_child]) > get_date(tweets_array[largest_index]):
        largest_index = left_child
            
    if right_child < size and get_date(tweets_array[right_child]) > get_date(tweets_array[largest_index]):
        largest_index = right_child
        
    if largest_index != root_index:
        tweets_array[root_index], tweets_array[largest_index] = tweets_array[largest_index], tweets_array[root_index]
        heapify_by_date(tweets_array, size, largest_index)


# function to sort the tweets by date
def heap_sort_by_date(tweets_array):
    array_length = len(tweets_array)
    
    for index in range(array_length // 2 - 1, -1, -1):
        heapify_by_date(tweets_array, array_length, index)
        
    for index in range(array_length - 1, 0, -1):
        tweets_array[0], tweets_array[index] = tweets_array[index], tweets_array[0]
        heapify_by_date(tweets_array, index, 0)
    
    return tweets_array


# function to sort the tweets by user
def get_string(user_data):
    return user_data.get('name', '').lower()    


# function to heapify the tweets by user    
def sort_by_date(data):
    if isinstance(data, str):
        with open(data, 'r') as file:
            twitter_data = json.load(file)
    else:
        twitter_data = data
    
    return heap_sort_by_date(twitter_data)


# function to heapify the tweets by string
def heapify(array, size, root_index):
    largest_index = root_index 
    left_child = 2 * root_index + 1 
    right_child = 2 * root_index + 2  

    if left_child < size and array[left_child] > array[largest_index]:
        largest_index = left_child

    if right_child < size and array[right_child] > array[largest_index]:
        largest_index = right_child
        
    if largest_index != root_index:
        array[root_index], array[largest_index] = array[largest_index], array[root_index]
        heapify(array, size, largest_index)


# function to sort the tweets by string
def heapSort(array):
    array_length = len(array) 
    
    for index in range(array_length // 2 - 1, -1, -1):
        heapify(array, array_length, index)

    for index in range(array_length - 1, 0, -1):
        array[0], array[index] = array[index], array[0] 
        heapify(array, index, 0)

    return array


# function to get the string from the tweet
def get_string(user_data):
    return user_data.get('name', '').lower()


# function to heapify the tweets by string
def heapify_by_string(users_array, size, root_index):
    largest_index = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2
    
    if left_child < size and get_string(users_array[left_child]) > get_string(users_array[largest_index]):
        largest_index = left_child
        
    if right_child < size and get_string(users_array[right_child]) > get_string(users_array[largest_index]):
        largest_index = right_child
        
    if largest_index != root_index:
        users_array[root_index], users_array[largest_index] = users_array[largest_index], users_array[root_index]
        heapify_by_string(users_array, size, largest_index)


# function to sort the tweets by string
def heap_sort_by_string(users_array):
    array_length = len(users_array)
    
    for index in range(array_length // 2 - 1, -1, -1):
        heapify_by_string(users_array, array_length, index)
        
    for index in range(array_length - 1, 0, -1):
        users_array[0], users_array[index] = users_array[index], users_array[0]
        heapify_by_string(users_array, index, 0)
    
    return users_array


# function to sort the tweets by string
def sort_by_string(data):
    if isinstance(data, str):
        with open(data, 'r') as file:
            user_records = json.load(file)
    else:
        user_records = data
    
    return heap_sort_by_string(user_records)


# function to get the number from the tweet
def get_number(item_data, key_name):
    try:
        return int(item_data.get(key_name, 0))
    
    except (ValueError, TypeError):
        return 0


# function to heapify the tweets by number
def heapify_by_number(data_array, size, root_index, key_name):
    largest_index = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2
    
    if left_child < size and get_number(data_array[left_child], key_name) > get_number(data_array[largest_index], key_name):
        largest_index = left_child
        
    if right_child < size and get_number(data_array[right_child], key_name) > get_number(data_array[largest_index], key_name):
        largest_index = right_child
        
    if largest_index != root_index:
        data_array[root_index], data_array[largest_index] = data_array[largest_index], data_array[root_index]
        heapify_by_number(data_array, size, largest_index, key_name)


# function to sort the tweets by number
def heap_sort_by_number(data_array, key_name):
    array_length = len(data_array)
    
    for index in range(array_length // 2 - 1, -1, -1):
        heapify_by_number(data_array, array_length, index, key_name)
        
    for index in range(array_length - 1, 0, -1):
        data_array[0], data_array[index] = data_array[index], data_array[0]
        heapify_by_number(data_array, index, 0, key_name)
    
    return data_array


# function to sort the tweets by number (likes, retweets, replies, id)
def sort_by_number(data, key_name):
    if isinstance(data, str):
        with open(data, 'r') as file:
            numerical_data = json.load(file)
    else:
        numerical_data = data
    
    return heap_sort_by_number(numerical_data, key_name)