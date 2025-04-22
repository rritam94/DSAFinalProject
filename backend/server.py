from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import json
import os
from datetime import datetime
import traceback

from heap_sort import sort_by_date, sort_by_string
from countingSort import countingSort, countingSort_tup

def get_date_key(item):
    timestamp_str = item.get('timestamp')
    if not timestamp_str: return None
    try:
        return datetime.fromisoformat(timestamp_str)
    except ValueError:
        print(f"Warning: Could not parse date: {timestamp_str}")
        return None

def get_user_key(item):
    user = item.get('username')
    return user.lower() if user else ''

def get_likes_key(item):
    try:
        return int(item.get('likes', 0))
    except (ValueError, TypeError):
        return 0

def get_retweets_key(item):
    try:
        return int(item.get('retweets', 0))
    except (ValueError, TypeError):
        return 0

def get_replies_key(item):
    try:
        return int(item.get('replies', 0))
    except (ValueError, TypeError):
        return 0

def get_id_key(item):
    try:
        return int(float(item.get('id', 0)))
    except (ValueError, TypeError):
         return 0

app = Flask(__name__)
CORS(app)

@app.route('/sort', methods=['POST'])
def sort_tweets():
    try:
        data = request.get_json()
        tweets = data.get('tweets')
        criteria = data.get('criteria')
        algorithm = data.get('algorithm')

        if not tweets:
             return jsonify({"sorted_tweets": [], "sort_time_ms": 0})
        if not criteria or not algorithm:
            return jsonify({"error": "Missing required parameters: criteria or algorithm"}), 400

        print(f"Received request to sort {len(tweets)} tweets by '{criteria}' using '{algorithm}' sort.")

        start_time = time.time()
        sorted_tweets = []
        error_message = None

        if algorithm == 'heap':
            print(f"Attempting heap sort by {criteria}")
            try:
                if criteria == 'date':
                    sorted_tweets = sort_by_date(list(tweets))
                elif criteria == 'user':
                    for tweet in tweets:
                        tweet['name'] = tweet.get('username', '')
                    sorted_tweets = sort_by_string(list(tweets))
                    for tweet in sorted_tweets:
                        if 'name' in tweet:
                            del tweet['name']
                else:
                    tweet_tuples = []
                    
                    if criteria == 'likes':
                        for tweet in tweets:
                            tweet_tuples.append((tweet, get_likes_key(tweet)))
                    elif criteria == 'retweets':
                        for tweet in tweets:
                            tweet_tuples.append((tweet, get_retweets_key(tweet)))
                    elif criteria == 'replies':
                        for tweet in tweets:
                            tweet_tuples.append((tweet, get_replies_key(tweet)))
                    elif criteria == 'id':
                        for tweet in tweets:
                            tweet_tuples.append((tweet, get_id_key(tweet)))
                    
                    sorted_tuples = countingSort_tup(tweet_tuples, 1)
                    sorted_tweets = [t[0] for t in sorted_tuples]
                    
                    if criteria in ['likes', 'retweets', 'replies']:
                        sorted_tweets.reverse()
                    
            except Exception as e:
                traceback.print_exc()
                error_message = f"Error during heap sort: {e}"

        elif algorithm == 'counting':
            print(f"Attempting counting sort by {criteria}")
            try:
                tweet_tuples = []
                
                if criteria == 'likes':
                    for tweet in tweets:
                        tweet_tuples.append((tweet, get_likes_key(tweet)))
                elif criteria == 'retweets':
                    for tweet in tweets:
                        tweet_tuples.append((tweet, get_retweets_key(tweet)))
                elif criteria == 'replies':
                    for tweet in tweets:
                        tweet_tuples.append((tweet, get_replies_key(tweet)))
                elif criteria == 'id':
                    for tweet in tweets:
                        tweet_tuples.append((tweet, get_id_key(tweet)))
                elif criteria == 'user':
                    for tweet in tweets:
                        tweet_tuples.append((tweet, get_user_key(tweet)))
                elif criteria == 'date':
                    for tweet in tweets:
                        timestamp = tweet.get('timestamp', '')
                        if timestamp is None:
                            timestamp = ''
                        else:
                            timestamp = timestamp.lower().replace('t', ' ')
                        tweet_tuples.append((tweet, timestamp))
                
                sorted_tuples = countingSort_tup(tweet_tuples, 1)
                sorted_tweets = [t[0] for t in sorted_tuples]

                if criteria in ['likes', 'retweets', 'replies', 'date']:
                    sorted_tweets.reverse()
                
            except Exception as e:
                traceback.print_exc()
                error_message = f"Error during counting sort: {e}"
            
        else:
            error_message = "Invalid algorithm specified"

        end_time = time.time()
        sort_duration = (end_time - start_time) * 1000

        if error_message:
             print(f"Error during sorting: {error_message}")
             return jsonify({"error": error_message}), 400 

        print(f"Sorting finished in {sort_duration:.2f} ms. Returning {len(sorted_tweets)} sorted tweets.")

        return jsonify({
            "sorted_tweets": sorted_tweets,
            "sort_time_ms": sort_duration
        })

    except Exception as e:
        print(f"An error occurred in /sort endpoint: {e}")
        traceback.print_exc()
        return jsonify({"error": f"An internal server error occurred: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001) 