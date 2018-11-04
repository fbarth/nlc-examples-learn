import pandas as pd
import numpy as np

df = pd.read_csv('../data/dataset_original.csv')
msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]

train.to_csv("../data/train.csv", sep=',', encoding='utf-8', index=False, quotechar='"')
test.to_csv("../data/test.csv", sep=',', encoding='utf-8', index=False, quotechar='"')