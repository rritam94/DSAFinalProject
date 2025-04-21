from datasets import load_dataset
import pandas as pd
import random

ds = load_dataset("enryu43/twitter100m_tweets")
train_ds = ds["train"]
random_indices = random.sample(range(len(train_ds)), 100000)
sampled_data = train_ds.select(random_indices)
df = pd.DataFrame(sampled_data)
df.to_csv("twitter_sample_100k.csv", index=False)