import requests, json

class Wu:
    def __init__(self):
        self.project = ""
        self.run = ""
        self.clone = ""
        self.gen = ""
        self.unit = ""
        self.code = ""
        self.credit = ""
        self.credit_time = ""
        self.days = ""
        self.cpuid = ""

    def populate_apiInfo(self, user):
        try:
            uri = f"https://api.foldingathome.org/project/{self.project}/run/{self.run}/clone/{self.clone}/gen/{self.gen}"
            response = requests.get(uri)
            apiWus = json.loads(response.content)
            
            for apiWu in apiWus:
                if apiWu.get('user') == user:
                    self.code = apiWu.get('code')
                    self.credit = apiWu.get('credit')
                    self.credit_time = apiWu.get('credit_time')
                    self.days = apiWu.get('days')
                    self.cpuid = apiWu.get('cpuid')
        
        except Exception as e:
            print("ERROR: cannot get info from API")
            print(e)

    def __str__(self):
        return f"{self.project},{self.run},{self.clone},{self.gen},{self.unit},{self.code},{self.credit},{self.credit_time},{self.days},{self.cpuid}"