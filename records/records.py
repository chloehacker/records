class records:
    
    def __init__(self, q=None, interval=None):        
        
        self.q = q
        self.interval = interval
        self.params = {}
        self.df = pd.DataFrame()
    
    def _get_all_records(self):     
        "this will iterate until the end of records"
        start = 0
        data = []
    
        gbif_interval = str(self.interval[0]) + "," + str(self.interval[1])
         
        self.params = {
          "q": self.q , 
          "year" : gbif_interval , 
        "basisOfRecord": "PRESERVED_SPECIMEN",
        "hasCoordinate": "true",
        "hasGeospatialIssue": "false",
        "country": "US",
        "offset": "0",
        "limit": "300"
        }
        
        while 1: 
            res = requests.get(
                url="http://api.gbif.org/v1/occurrence/search?", 
                params=self.params,
            )
        # increment counter
            self.params["offset"] = str(int(self.params["offset"]) + 300)
        
        # concatenate data 
            idata = res.json()
            data += idata["results"]
        
        # stop when end of record is reached
            if idata["endOfRecords"]:
                break
        
        self.df = pd.DataFrame(data)
        return self.df
    
    def all_records(self):
        return self._get_all_records()