from tfx.orchestration.pipeline import Pipeline
from configs.config import *
from pipeline.components.data_ingestion import DataIngestionComp
from tfx.orchestration.local.local_dag_runner import LocalDagRunner
from tfx.orchestration import metadata

pipeline_root = os.path.join(os.getcwd(), 'tfx_output')
metadata_connection_config = metadata.sqlite_metadata_connection_config(
    os.path.join(pipeline_root, 'metadata.sqlite')
)
ingestion_comp = DataIngestionComp().getComp()
def create_pipeline(pipeline_name: str, pipeline_root: str) -> Pipeline:
    return Pipeline(
        pipeline_name=pipeline_name,
        metadata_connection_config = metadata_connection_config,
        components=[
            ingestion_comp,
        ],
        enable_cache=True
    )

# Run the pipeline
if __name__ == '__main__':
    pipeline_name = 'minimal_pipeline'
    data_root = os.path.join(os.getcwd(), 'data')
    pipeline = create_pipeline(pipeline_name=pipeline_name, pipeline_root=pipeline_root)
    LocalDagRunner().run(pipeline)

