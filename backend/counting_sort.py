import json
from datetime import datetime

# function to get the date from the tweet
def get_date(tweet_data):
    timestamp = tweet_data.get('timestamp', '')
    
    if not timestamp:
        return datetime.min
    
    try:
        if timestamp.endswith('Z'):
            timestamp = timestamp[:-1] + '+00:00'
            
        return datetime.fromisoformat(timestamp)
    
    except ValueError:
        return datetime.min

# function to sort the records by date
def counting_sort(input_records, key_function, minimum_value, maximum_value):
    array_size = maximum_value - minimum_value + 1
    frequency_counts = [0] * array_size
    
    i = 0
    while i < len(input_records):
        record = input_records[i]
        frequency_counts[key_function(record) - minimum_value] += 1
        i += 1
    
    index = 1
    while index < array_size:
        frequency_counts[index] += frequency_counts[index - 1]
        index += 1
    
    result_array = [None] * len(input_records)
    
    i = len(input_records) - 1
    while i >= 0:
        record = input_records[i]
        key_value = key_function(record) - minimum_value
        frequency_counts[key_value] -= 1
        result_array[frequency_counts[key_value]] = record
        i -= 1
    
    return result_array

# function to sort the tweets by date
def sort_by_date(data):
    if isinstance(data, str):
        with open(data) as file_handle:
            tweets = json.load(file_handle)
    
    else:
        tweets = data.copy()
    
    records = [(tweet, get_date(tweet)) for tweet in tweets]

    records = counting_sort(records, lambda rec: rec[1].second,0,59)
    records = counting_sort(records,lambda rec: rec[1].minute,0,59)
    
    records = counting_sort(records,lambda rec: rec[1].hour,0,23)
    
    records = counting_sort(records,lambda rec: rec[1].day,1,31)
    
    records = counting_sort(records,lambda rec: rec[1].month,1,12)

    years = [date_time.year for _, date_time in records]
    min_year, max_year = min(years), max(years)
    
    records = counting_sort(records,lambda rec: rec[1].year,min_year, max_year)

    return [tweet for tweet, _ in records]

# function to get the string from the user
def get_string(user_data):
    return user_data.get('name', '').lower()

# function to sort the users by string
def sort_by_string(data):
    if isinstance(data, str):
        with open(data, 'r') as file_handle:
            user_records = json.load(file_handle)
    
    else:
        user_records = data.copy()
    
    if not user_records:
        return []
    
    all_names = []
    
    i = 0
    while i < len(user_records):
        user = user_records[i]
        name = get_string(user)
        all_names.append(name)
        i += 1
    
    max_length = 0
    
    i = 0
    while i < len(all_names):
        name = all_names[i]
        if len(name) > max_length:
            max_length = len(name)
        i += 1
    
    sorted_records = user_records.copy()
    
    char_position = max_length - 1
    while char_position >= 0:
        char_counts = [0] * 256
        
        i = 0
        while i < len(sorted_records):
            user = sorted_records[i]
            name = get_string(user)
            char_code = 0
            
            if char_position < len(name):
                char_code = ord(name[char_position])
                
            char_counts[char_code] += 1
            i += 1
        
        i = 1
        while i < 256:
            char_counts[i] += char_counts[i-1]
            i += 1
        
        output_array = [None] * len(sorted_records)
        
        i = len(sorted_records) - 1
        while i >= 0:
            name = get_string(sorted_records[i])
            char_code = 0
            
            if char_position < len(name):
                char_code = ord(name[char_position])
                
            index = char_counts[char_code] - 1
            output_array[index] = sorted_records[i]
            char_counts[char_code] -= 1
            i -= 1
        
        sorted_records = output_array
        char_position -= 1
    
    return sorted_records


# function to sort by number
def sort_by_number(data, key_name):
    if isinstance(data, str):
        with open(data, 'r') as file_handle:
            numerical_data = json.load(file_handle)
    
    else:
        numerical_data = data.copy()
    
    if not numerical_data:
        return []
    
    number_values = []
    
    i = 0
    while i < len(numerical_data):
        item = numerical_data[i]
        try:
            number = int(item.get(key_name, 0))
        
        except (ValueError, TypeError):
            number = 0
            
        number_values.append(number)
        i += 1
    
    min_number = min(number_values)
    max_number = max(number_values)
    range_size = max_number - min_number + 1
    
    frequency_counts = []
    
    i = 0
    while i < range_size:
        frequency_counts.append(0)
        i += 1
    
    i = 0
    while i < len(number_values):
        num = number_values[i]
        index = num - min_number
        frequency_counts[index] += 1
        i += 1
    
    i = 1
    while i < range_size:
        frequency_counts[i] += frequency_counts[i-1]
        i += 1
    
    result_array = []
    
    i = 0
    while i < len(numerical_data):
        result_array.append(None)
        i += 1
    
    i = len(numerical_data) - 1
    while i >= 0:
        try:
            number = int(numerical_data[i].get(key_name, 0))
        
        except (ValueError, TypeError):
            number = 0
            
        index = frequency_counts[number - min_number] - 1
        result_array[index] = numerical_data[i]
        frequency_counts[number - min_number] -= 1
        i -= 1
    
    return result_array