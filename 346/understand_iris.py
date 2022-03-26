__all__ = [
    "IRIS_DATA",
    "get_nr_classes",
    "get_nr_samples",
    "get_dim",
    "get_nr_samples_per_class",
    "get_rel_nr_samples_per_class",
    "get_nr_missing_values",
    "get_stats_per_feature",
    "get_correlation_per_feature",
] # __all__ controls what gets imported if you use from module.py import *.
import pandas as pd
from sklearn.datasets import load_iris

# you can set as_frame to False, but this will complicate the solution
# because you have to work with numpy ndarrays
IRIS_DATA = load_iris(as_frame=True, return_X_y=True)


def get_nr_classes(data: tuple) -> int:
    """Return the number of classes in the Iris data set.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        int: Number of classes (targets) in the data set.
    """
    return len(set(data[1]))


def get_nr_samples(data: tuple) -> int:
    """Return the number of samples in the Iris data set.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        int: Number of samples (instances) in the data set.
    """
    return len(data[0])


def get_dim(data: tuple) -> int:
    """Return the dimensionality of the Iris data set.

    **Warning**: Dimensionality is not meant in the mathematical sense
        (which would be the shape and dim attribute if we would talk about matrices).
        Dimensionality in ML means the number of dimensions in your data,
        that is the number of axes your data span over, which is the number of features we
        have available.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        int: Number of dimensions (features) in the data set.
    """
    return len(data[0].columns)


def get_nr_samples_per_class(data: tuple) -> pd.Series:
    """Return the number of samples for each class of the Iris data set.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        pd.Series: Series with number of samples for each class.
    """
    return get_nr_samples(data) / get_nr_classes(data)


def get_rel_nr_samples_per_class(data: tuple) -> pd.Series:
    """Return the relative number of samples for each class of the Iris data set.

    **Hint**: Try to re-use already defined functions.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        pd.Series: Series with percentage (between 0 and 1) of samples for each class.
    """
    return pd.Series([1 / get_nr_classes(data)] * get_nr_classes(data))


def get_nr_missing_values(data: tuple) -> int:
    """Return the number of missing values in the Iris data set.

    **Hint**: pandas isna() might come in handy.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().

    Returns:
        int: Number of missing values in the data set.
    """
    return sum(data[0].isna().sum())


def get_stats_per_feature(
    data: tuple,
    features: list,
    stats: list,
) -> pd.DataFrame:
    """Return summary statistics for a list of given features.

    **Hint**: Maybe try out pandas.DataFrame.describe() or pandas.DataFrame.agg().

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().
        features (list): A list of features for which to calculate summary statistics.
        stats (list): A list of summary statistics to calculate/extract for the given features.

    Returns:
        pd.DataFrame: A data frame with the requested summary statistics for each feature.
    """
    info = data[0].describe()
    return info.loc[stats, features]


def get_correlation_per_feature(
    data: tuple,
    features: list,
) -> pd.DataFrame:
    """Return feature correlation with target.

    **Hint**: Correlation coefficients can be calculated for each pair of feature with pandas.DataFrame.corr().
        This means you might have to combine the features and the target into a single data frame.

    Arguments:
        data (tuple): The data as returned by sklearn.datasets.load_iris().
        features (list): A list with feature names for which the correlation is returned.

    Returns:
        pd.Series: Value of feature correlation with target.
    """
    new_data = data[0][features]
    return new_data.corrwith(data[1])


if __name__ == "__main__":
    # here you can try out your functions!
    # only called when directly run so no problem when imported from the test file
    print(IRIS_DATA[0].head()) # show the first 5 lines.
    print(get_nr_classes(IRIS_DATA)) # pass the data to the function and return nr classes.