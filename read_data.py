import pandas as pd


def read_train_df():
    return pd.read_csv('input/train.csv')


def read_test_df():
    return pd.read_csv('input/test.csv')
