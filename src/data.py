# src/data.py
from multiearth_challenge.prediction_dataset import ImagePredictionDataset

def load_prediction_dataset(netcdf_file_path, num_history_images=5):
    """
    Load the prediction dataset from a NetCDF file.

    Args:
        netcdf_file_path (str): Path to the NetCDF file
        num_history_images (int): Number of historical images to use

    Returns:
        dataset: ImagePredictionDataset instance
    """
    return ImagePredictionDataset(
        netcdf_file_path,
        num_history_images=num_history_images
    )
