from tfx.orchestration.pipeline import Pipeline
from configs.config import *
from pipeline.components.data_ingestion import DataIngestionComp
from tfx.orchestration.local.local_dag_runner import LocalDagRunner

ingestion_comp = DataIngestionComp().getComp()
#pipeline = Pipeline(
#        pipeline_name="name",
#        pipeline_root="/home/yasiru/Documents/",
#        components=[ingestion_comp],
#        enable_cache=True
#    )
#LocalDagRunner().run(pipeline)
