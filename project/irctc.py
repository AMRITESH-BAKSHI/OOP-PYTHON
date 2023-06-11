import requests

class IRCTC:
    def __init__(self):
        userinput=input(""" 
        enter the choice:
        1--> check live train status
        2--> check pnr
        3--> check train schedule 
        # """)
        if userinput=="1":
            print("live train status")
        elif userinput=="2":
            print("check pnr")
        elif userinput=="3":
            print("train schedule")
            self.train_schedule()
    
    
    def train_schedule(self):
        tno=input("enter train no")
        self.fetchdata(tno)
    
    
    def fetchdata(self,tno):
        url = "https://trains.p.rapidapi.com/"

        payload = { "search": "Rajdhani" }
        headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "f4c2da8fc3mshabe2a7cc6b48369p1c7e0cjsnc030443d9770",
	"X-RapidAPI-Host": "trains.p.rapidapi.com"
                }

        data = requests.post(url, json=payload, headers=headers)
        data=data.json()
        for i in data:
            if i["train_num"]==int(tno):
                print("train name:-->",i["name"])
                print("arrival time:-->",i["data"]["arriveTime"])
                print("departure time:-->",i["data"]["departTime"])
                print("train from:-->",i["train_from"])
                print("train to:-->",i["train_to"])
                
ob=IRCTC()

