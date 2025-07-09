import os
import urllib.request as request
from src.mlproject import logger
import zipfile
from src.mlproject.entity.config_entity import (DataIngestionConfig)


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        # Logic to download data from self.config.source_URL
        if not os.path.exists(self.config.local_data_file):
            filename, headers =  request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"File downloaded: {filename} with headers: {headers}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file}")
    
    def extract_zip_file(self):
        # Logic to unzip data to self.config.unzip_dir
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted files to: {unzip_path}")