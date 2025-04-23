from flask import Flask, request, jsonify
from flask_cors import CORS
import time
from datetime import datetime

from heap_sort import sort_by_date as heap_sort_by_date, sort_by_string as heap_sort_by_string, sort_by_number as heap_sort_by_number
from counting_sort import sort_by_date as counting_sort_by_date, sort_by_string as counting_sort_by_string, sort_by_number as counting_sort_by_number


# function to get the date from the tweet
def get_date_key(tweet_data):
    timestamp_string = tweet_data.get('timestamp')
    
    if not timestamp_string: 
        return None
    
    try:
        return datetime.fromisoformat(timestamp_string)
    
    except ValueError:
        print("couldn't parse date")
        return None


# function to get the user from the tweet
def get_user_key(tweet_data):
    username = tweet_data.get('username')
    
    return username.lower() if username else ''


# function to get the likes from the tweet
def get_likes_key(tweet_data):
    try:
        return int(tweet_data.get('likes', 0))
    
    except (ValueError, TypeError):
        return 0


# function to get the retweets from the tweet
def get_retweets_key(tweet_data):
    try:
        return int(tweet_data.get('retweets', 0))
    
    except (ValueError, TypeError):
        return 0


# function to get the replies from the tweet
def get_replies_key(tweet_data):
    try:
        return int(tweet_data.get('replies', 0))
    
    except (ValueError, TypeError):
        return 0


# function to get the id from the tweet
def get_id_key(tweet_data):
    try:
        return int(float(tweet_data.get('id', 0)))
    
    except (ValueError, TypeError):
         return 0


app = Flask(__name__)
CORS(app)


# route to sort the tweets
@app.route('/sort', methods=['POST'])
def sort_tweets():
    try:
        request_data = request.get_json()
        tweets = request_data.get('tweets')
        sort_criteria = request_data.get('criteria')
        sort_algorithm = request_data.get('algorithm')

        start_time = time.time()
        sorted_tweets = []
        error_message = None

        if sort_algorithm == 'heap':
            print(f"Attempting heap sort by {sort_criteria}")
            
            try:
                if sort_criteria == 'date':
                    sorted_tweets = heap_sort_by_date(list(tweets))
                
                elif sort_criteria == 'user':
                    for tweet in tweets:
                        tweet['name'] = tweet.get('username', '')
                    
                    sorted_tweets = heap_sort_by_string(list(tweets))
                    
                    for tweet in sorted_tweets:
                        if 'name' in tweet:
                            del tweet['name']
                
                elif sort_criteria == 'likes':
                    sorted_tweets = heap_sort_by_number(list(tweets), 'likes')
                
                elif sort_criteria == 'retweets':
                    sorted_tweets = heap_sort_by_number(list(tweets), 'retweets')
                
                elif sort_criteria == 'replies':
                    sorted_tweets = heap_sort_by_number(list(tweets), 'replies')
                
                elif sort_criteria == 'id':
                    sorted_tweets = heap_sort_by_number(list(tweets), 'id')
            
            except Exception as e:
                x = 2
        
        elif sort_algorithm == 'counting':
            try:
                if sort_criteria == 'date':
                    sorted_tweets = counting_sort_by_date(list(tweets))
                
                elif sort_criteria == 'user':
                    for tweet in tweets:
                        tweet['name'] = tweet.get('username', '')
                    
                    sorted_tweets = counting_sort_by_string(list(tweets))
                    
                    for tweet in sorted_tweets:
                        if 'name' in tweet:
                            del tweet['name']
                
                elif sort_criteria == 'likes':
                    sorted_tweets = counting_sort_by_number(list(tweets), 'likes')
                
                elif sort_criteria == 'retweets':
                    sorted_tweets = counting_sort_by_number(list(tweets), 'retweets')
                
                elif sort_criteria == 'replies':
                    sorted_tweets = counting_sort_by_number(list(tweets), 'replies')
                
                elif sort_criteria == 'id':
                    sorted_tweets = counting_sort_by_number(list(tweets), 'id')

            except Exception as e:
                x = 2
            
        else:
            error_message = "Invalid algorithm specified"

        end_time = time.time()
        sort_duration = (end_time - start_time) * 1000

        if error_message:
             print(f"Error during sorting: {error_message}")
             return jsonify({"error": error_message}), 400 


        return jsonify({
            "sorted_tweets": sorted_tweets,
            "sort_time_ms": sort_duration
        })

    except Exception as e:
        return jsonify({"error": f"An internal server error occurred: {e}"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5001) 