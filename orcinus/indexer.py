# import json
import yaml

class Indexer:
    def __init__(self):
        self.file_path = ""
        self.compose_index = {}
        
    def parse_docker_compose(self):
        with open(self.file_path, 'r') as f:
            self.compose_index = yaml.safe_load(f)
