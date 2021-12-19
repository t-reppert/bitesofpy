import os
from pathlib import Path
import string
import sys
from urllib.request import urlretrieve
from zipfile import ZipFile
import re

import pandas as pd

TMP = Path(os.getenv("TMP", "/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"


def _setup():
    data_zipfile = '311-data.zip'
    urlretrieve(f'{S3}/{data_zipfile}', TMP / data_zipfile)
    ZipFile(TMP / data_zipfile).extractall(TMP)
    sys.path.append(str(TMP))

_setup()

from stop_words import stop_words
from tf_idf import TFIDF


def load_data():
    # Load the text and populate a Pandas Dataframe
    # The order of the sample text strings should not be changed
    # Return the Dataframe with the index and 'text' column
    return pd.read_csv('/tmp/samples.txt')


def strip_url_email(x_df):
    # Strip all URLs (http://...) and Emails (somename@email.address)
    # The 'text' column should be modified to remove
    #   all URls and Emails
    x_df['text'] = x_df['text'].replace(to_replace='[a-zA-Z0-9\_\-\.]+@[a-zA-Z0-9\_\-\.]+ ', value=' ', regex=True)
    x_df['text'] = x_df['text'].replace(to_replace='(http|HTTP)[sS]*\:\/\/[a-zA-Z\-\_\.\/]+ ', value=' ', regex=True)
    return x_df


def to_lowercase(x_df):
    # Convert the contents of the 'text' column to lower case
    # Return the Dataframe with the 'text' as lower case
    x_df['text'] = x_df['text'].str.lower()
    return x_df


def strip_stopwords(x_df):
    # Drop all stop words from the 'text' column
    # Return the Dataframe with the 'text' stripped of stop words
    def remove_stopwords(words):
        new_words = []
        for word in words.split():
            if word.lower() not in stop_words:
                new_words.append(word)
        return ' '.join(new_words)
    x_df['text'] = x_df['text'].apply(remove_stopwords)
    return x_df


def strip_non_ascii(x_df):
    # Remove all non-ascii characters from the 'text' column
    # Return the Dataframe with the 'text' column
    #   stripped of non-ascii characters
    x_df['text'] = x_df['text'].replace(to_replace='[^\x00-\x7F]+', value='', regex=True)
    return x_df


def strip_digits_punctuation(x_df):
    # Remove all digits and punctuation characters from the 'text' column
    # Return the Dataframe with the 'text' column
    #   stripped of all digit and punctuation characters
    x_df['text'] = x_df['text'].replace(to_replace='[^\w\s]', value='', regex=True)
    x_df['text'] = x_df['text'].replace(to_replace='[0-9\_]', value='', regex=True)
    return x_df


def calculate_tfidf(x_df):
    # Calculate the 'tf-idf' matrix of the 'text' column
    # Return the 'tf-idf' Dataframe
    tfidf_obj = TFIDF(x_df["text"])
    return tfidf_obj()


def sort_columns(x_df):
    # Depending on how the earlier functions are implemented
    #   it's possible that the order of the columns may be different
    # Sort the 'tf-idf' Dataframe columns
    #   This ensure the tests are compatible
    cols = x_df.columns.tolist()
    cols = sorted(cols)
    x_df = x_df[cols]
    return x_df


def get_tdidf():
    # Pandas’ pipeline feature allows you to string together
    #   Python functions in order to build a pipeline of data processing.
    # Complete the functions above in order to produce a 'tf-idf' Dataframe
    # Return the 'tf-idf' Dataframe
    df = (
        load_data()
        .pipe(strip_url_email)
        .pipe(to_lowercase)
        .pipe(strip_stopwords)
        .pipe(strip_non_ascii)
        .pipe(strip_digits_punctuation)
        .pipe(calculate_tfidf)
        .pipe(sort_columns)
    )
    return df
