from manifest import Manifest
from api import Api
class Main:
    def __init__(self):
        # Constructor
        pass
    def run(self):
        manifest = Manifest()
        index = manifest.index()
        service = list(index["services"].keys())[0]
        version = index["version"]
        cpe_name = "cpe:2.3:a:{}:{}:{}:*:*:*:-:*:*:*".format(service,service, version)
        api_url = "https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName={}".format(cpe_name)
        api = Api()
        data = api.connect_to_api(api_url)
        print(data)

if __name__ == "__main__":
    main_instance = Main()
    main_instance.run()
