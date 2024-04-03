import argparse
from manifest import Manifest
from api import Api
from report import Report

class Orcinus:
    def __init__(self):
        # Constructor
        pass
    def run(self, options):
        manifest = Manifest()
        index = manifest.index()
        
        service = list(index["services"].keys())[0]
        version = index["version"]
        
        cpe_name = f"cpe:2.3:a:{service}:{service}:{version}:*:*:*:-:*:*:*"         
        api_url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName={cpe_name}"
        
        api = Api()
        data = api.connect_to_api(api_url)
        
        api_report = Report(data)
        api_report.printReport(options.reportType)

if __name__ == "__main__":     
    parser = argparse.ArgumentParser(description='Static analysis tool for docker containers.')     
    parser.add_argument('reportType', choices=['reportCveCount', 'reportCveIds'], help='Select report type')     

    args = parser.parse_args()      
    main_instance = Orcinus()     
    main_instance.run(args)

