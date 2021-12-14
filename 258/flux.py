import pandas as pd
XYZ = "https://bites-data.s3.us-east-2.amazonaws.com/xyz.csv"
THRESHOLDS = (5000, 0.05)


def calculate_flux(XYZ: str) -> list:
    """Read the data in from xyz.csv
    add two new columns, one to calculate dollar flux,
    and the other to calculate percentage flux
    return as a list of tuples
    """
    df = pd.read_csv(XYZ)
    df['Dollar Flux'] = df['12/31/20'] - df['12/31/19']
    df['Percentage Flux'] = (df['Dollar Flux'] / df['12/31/19']).abs()
    return [tuple(s) for s  in df.to_numpy()]


def identify_flux(xyz: list) -> list:
    """Load the list of tuples, iterate through
    each item and determine if it is above both
    thresholds. if so, add to the list
    """
    flagged_lines = [i for i in xyz if abs(i[3]) > THRESHOLDS[0] and abs(i[4]) > THRESHOLDS[1]]

    return flagged_lines