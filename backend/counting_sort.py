import json
from datetime import datetime


def get_date(tweet):
    timestamp_string = tweet.get('timestamp')
    
    if not timestamp_string:
        return datetime.min
    
    try:
        if timestamp_string.endswith('Z'):
            return datetime.fromisoformat(timestamp_string.replace('Z', '+00:00'))
        
        return datetime.fromisoformat(timestamp_string)
    
    except ValueError:
        print("can't parse date")
        return datetime.min


def sort_by_date(data):
    if isinstance(data, str):
        with open(data, 'r') as file:
            twitter_data = json.load(file)
    else:
        twitter_data = data.copy()
    

    date_buckets = {}
    
    for tweet in twitter_data:
        tweet_date = get_date(tweet)
        
        if tweet_date not in date_buckets:
            date_buckets[tweet_date] = []
        
        date_buckets[tweet_date].append(tweet)
    

    if not date_buckets:
        return twitter_data
    

    sorted_results = []
    sorted_dates = sorted(date_buckets.keys())
    
    for single_date in sorted_dates:
        tweets_on_date = date_buckets[single_date]
        
        for tweet in tweets_on_date:
            sorted_results.append(tweet)
    
    return sorted_results



def get_string(user_data):
    return user_data.get('name', '').lower()


def sort_by_string(data):
    if isinstance(data, str):
        with open(data, 'r') as file:
            user_records = json.load(file)
    else:
        user_records = data.copy()
    

    alphabet_buckets = {}
    
    for user in user_records:
        name_value = get_string(user)
        first_letter = name_value[0] if name_value else ''
        sorted_results = []
    
        if first_letter not in alphabet_buckets:
            alphabet_buckets[first_letter] = []
            
        alphabet_buckets[first_letter].append(user)
    

    sorted_letters = sorted(alphabet_buckets.keys())
    
    for letter in sorted_letters:
        users_with_letter = alphabet_buckets[letter]
        users_with_letter.sort(key=get_string)
        
        for user in users_with_letter:
            sorted_results.append(user)
    
    return sorted_results


def sort_by_number(data, key_name):
    if isinstance(data, str):
        with open(data, 'r') as file:
            numerical_data = json.load(file)
    else:
        numerical_data = data.copy()
    

    def get_number(item_data):
        try:
            return int(item_data.get(key_name, 0))
        
        except (ValueError, TypeError):
            return 0
    

    if not numerical_data:
        return []
        

    smallest_value = float('inf')
    largest_value = float('-inf')
    
    for data_item in numerical_data:
        numerical_value = get_number(data_item)
        smallest_value = min(smallest_value, numerical_value)
        largest_value = max(largest_value, numerical_value)
    

    range_too_large = largest_value - smallest_value > 1_000_000
    
    if range_too_large:
        return sorted(numerical_data, key=get_number)
    

    count_array = []
    
    for i in range(largest_value - smallest_value + 1):
        count_array.append(0)
    

    for data_item in numerical_data:
        numerical_value = get_number(data_item)
        adjusted_index = numerical_value - smallest_value
        count_array[adjusted_index] += 1
    

    value_buckets = []
    
    for i in range(largest_value - smallest_value + 1):
        value_buckets.append([])
        

    for data_item in numerical_data:
        numerical_value = get_number(data_item)
        adjusted_index = numerical_value - smallest_value
        value_buckets[adjusted_index].append(data_item)
    

    sorted_results = []
    
    for bucket_index in range(len(value_buckets)):
        current_bucket = value_buckets[bucket_index]
        
        for data_item in current_bucket:
            sorted_results.append(data_item)
    
    return sorted_results