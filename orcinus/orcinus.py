from manifest import Manifest
from api import Api
from report import Report

class orcinus:
    def __init__(self):
        # Constructor
        pass
    def run(self):
        manifest = Manifest()
        index = manifest.index()
        
        service = list(index["services"].keys())[0]
        version = index["version"]
        
        cpe_name = f"cpe:2.3:a:{service}:{service}:{version}:*:*:*:-:*:*:*"         
        api_url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName={cpe_name}"
        
        api = Api()
        data = api.connect_to_api(api_url)
        
        api_report = Report(data)
        api_report.printReport()

if __name__ == "__main__":
    main_instance = orcinus()
    main_instance.run()
