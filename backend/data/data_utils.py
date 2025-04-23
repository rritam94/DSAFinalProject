from datasets import load_dataset
import pandas as pd
import random
import json

def sample_points(num_points):
    ds = load_dataset("enryu43/twitter100m_tweets")
    train_ds = ds["train"]
    random_indices = random.sample(range(len(train_ds)), 100000)
    sampled_data = train_ds.select(random_indices)
    df = pd.DataFrame(sampled_data)
    df.to_csv("twitter_sample_100k.csv", index=False)

def convert_to_json(filepath):
    df = pd.read_csv(filepath)
    records = df.to_dict(orient="records")
    with open("twitter_sample_100k.json", "w") as f:
        json.dump(records, f, indent=4)

convert_to_json("twitter_sample_100k.csv")