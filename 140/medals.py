import pandas as pd

data = "http://projects.bobbelderbos.com/data/summer.csv"


def athletes_most_medals():
    df = pd.read_csv(data)
    top_man = dict(df[df['Gender']=='Men']['Athlete'].value_counts().head(1))
    top_woman = dict(df[df['Gender']=='Women']['Athlete'].value_counts().head(1))
    return {**top_man,**top_woman}