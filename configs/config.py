import os
from absl import logging

#dataset info
BBC_DATASET_PATH = os.path.join(os.getcwd(), 'datasets', 'raw') 

#pipeline info
PIPELINE_NAME = "news-classifier-ml-piepline"
PIPELINE_ROOT = os.path.join('..' , 'pipeline')
METADATA_PATH = os.path.join('..', 'metadata', 'metadata.db')
SERVING_MODEL_DIR = os.path.join('..','model', 'serving_model')

logging.set_verbosity(logging.DEBUG)
