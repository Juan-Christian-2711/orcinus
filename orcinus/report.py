import json

class Report:
    def __init__(self, data) -> None:
        self.data = data
    def printReport(self, option) -> None:
        if (option == "reportCveCount"):
            print(self.data['totalResults'])
        if (option == "reportCveIds"):
            for i in self.data['vulnerabilities']:
                for key, value in i.items():
                    print(value.keys())
                    print(value['id'])
