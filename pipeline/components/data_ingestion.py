import os
from tfx.components import CsvExampleGen
from tfx.orchestration.pipeline import Pipeline
from tfx.orchestration.local.local_dag_runner import LocalDagRunner
from configs.config import *

data_path =  BBC_DATASET_PATH

example_gen = CsvExampleGen(input_base=data_path)
pipeline = Pipeline(
    pipeline_name=PIPELINE_NAME,
    pipeline_root=PIPELINE_ROOT,
    components=[example_gen],
    enable_cache=True
)

LocalDagRunner().run(pipeline=pipeline)
