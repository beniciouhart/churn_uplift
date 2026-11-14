import pandas as pd
import openml
def load_dataset(dataset_id: int = 45580) -> pd.DataFrame:
    """ Takes in dataset ID from OpenML's dataset library.

        Returns design matrix (df), categorical column indicator (boolean list), and feature names.
    """
    dataset = openml.datasets.get_dataset(dataset_id,
                                          download_data = True,
                                          download_qualities = False,
                                          download_features_meta_data = False)
    df, _, cat_ind, names = dataset.get_data()
    return df, cat_ind, names