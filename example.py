#!/usr/bin/env python3

import pandas as pd

# Do some basic data from ops.

df = pd.DataFrame([list(range(i, i + 3)) for i in range(1, 10)], columns=['A', 'B', 'C'])
print(df)
for c in df.columns:
    print(f"mean({c}): " + str(df[c].mean()))

df = pd.read_csv('test.csv', index_col=False)
df['ts'] = pd.to_datetime(df['ts'])
print(df)