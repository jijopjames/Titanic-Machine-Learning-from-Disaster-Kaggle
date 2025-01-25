import pandas as pd

# Dataset Path
train = "../data/train.csv"
test = "../data/test.csv"
gender_submission = "../data/gender_submission.csv"

# Load the datasets
train_data = pd.read_csv(train)
train_data.head()

test_data = pd.read_csv(test)
test_data.head()

gender_submission_data = pd.read_csv(gender_submission)
gender_submission_data.head()
