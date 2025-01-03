from tfx.components import CsvExampleGen, example_gen
from configs.config import *
from tfx.proto import example_gen_pb2
from tfx.components import CsvExampleGen
from tfx.proto import example_gen_pb2
from tfx.proto.example_gen_pb2 import SplitConfig
from tfx.orchestration.experimental.interactive.interactive_context import InteractiveContext

class DataIngestionComp:
    
    def __init__(self):
        self.data_path =  BBC_DATASET_PATH

    def getComp(self):
        output = self.prepareOutput()
        self.example_gen = CsvExampleGen(input_base=self.data_path, output_config=output)
        context = InteractiveContext()
        context.run(self.example_gen)  
        with open('/home/yasiru/Desktop/new.txt', 'w') as file:
            for artifact in self.example_gen.outputs['examples'].get():
                file.write(artifact.name)
                file.write(artifact.__str__())
        file.close
        return self.example_gen

    def prepareOutput(self):
        output = example_gen_pb2.Output(
            split_config = SplitConfig(splits = [
                SplitConfig.Split(name = 'train', hash_buckets = 3),
                SplitConfig.Split(name = 'eval', hash_buckets = 1)
            ]
            )
        )
        return output
