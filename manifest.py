from indexer import Indexer
class Manifest:
    def __init__(self) -> None:
        self.compose = ""
        self.indexer = Indexer()
       
    def index(self): 
        self.indexer = Indexer()
        self.indexer.file_path = "../dockerTest/docker-compose.yml"
        self.indexer.parse_docker_compose()
        return self.indexer.compose_index
