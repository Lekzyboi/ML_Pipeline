import os
import yaml
from src.mlproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file read successfully from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Invalid YAML file format at {path_to_yaml}")
    except Exception as e:
        raise e
    
    
@ensure_annotations

def create_directories(path_to_dirs: list, verbose=True):
    """
    Creates directories if they do not exist.
    
    Args:
        path_to_dirs (list): List of directory paths to create.
    """
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at {path}")
        

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves data to a JSON file.
    
    Args:
        path_to_json (Path): Path to the JSON file.
        data (Any): Data to save in the JSON file.
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        logger.info(f"Data saved to JSON file at {path}")
        
        
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads data from a JSON file.
    
    Args:
        path_to_json (Path): Path to the JSON file.
        
    Returns:
        dict: Data loaded from the JSON file.
    """
    with open(path) as f:
        content = json.load(f)
        
    logger.info(f"Data loaded from JSON file at {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(path: Path, data: Any):
    """
    Saves data to a joblib file.
    
    Args:
        path (Path): Path to the joblib file.
        data (Any): Data to save in the joblib file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Data saved to joblib file at {path}")
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a joblib file.
    
    Args:
        path (Path): Path to the joblib file.
        
    Returns:
        Any: Data loaded from the joblib file.
    """
    data = joblib.load(path)
    logger.info(f"Data loaded from joblib file at {path}")
    return data
