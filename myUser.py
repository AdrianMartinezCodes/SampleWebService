import json
"""
Creates a user profile with the properties to add tranascations,
spend points, and get total values
"""
class myUser:
    def __init__(self):
        """Constructor:

        Initiates timestamps <Key:string Timestamp, V: string payer>
        Initiates payers <Key:string payer,
                        V:(PayerDict<Key:String Timestamp,V: int points>,int PayerTotal)>
        Initates runningTotal
        """
        self.timestamps = {}
        self.payers = {}
        self.runningTotal = 0
    def transaction(self,data):
        """
        Adds a valid timestamp to timestamps
        Adds a valid timestamp to payers
        Updates running cost

            Paramters:
                data(list): a decompiled json list with values for
                            "payer": string name, "points": int num, "timestamp": string date        
        """
        #parse the decompiled json into payer/points/timestamp
        payer = data["payer"]
        pts = int(data["points"])
        timestamp = data["timestamp"]
        #check for duplicate timestamp
        if timestamp not in self.timestamps:
            #check for negeative points in respective payer tree
            if (self.runningTotal + pts) < 0:
                raise ValueError("Invalid Tranasction. Negative Balance")
            #checks if payerDict exists, else makes one
            if payer in self.payers:
                payerTimeDict = self.payers[payer][0]
                payerTotal = self.payers[payer][1]
                payerTimeDict[timestamp] = pts
                self.payers[payer][1] += pts
            else:
                self.payers[payer] = [{timestamp:pts},pts]
            self.timestamps[timestamp] = payer
            self.runningTotal += pts
        return

    def spendPoints(self,data):
        """
        Spends a users points based on earliest transaction

            Paramters:
                data(list): a decompiled json list with values for
                            "payer": string name, "points": int num, "timestamp": string date
            Returns: json file of total total amounts removed from payers
        """
        #parse the url into points
        pts = int(data["points"])
        removalDict = {}
        #checks that there are enough points to spend
        if self.runningTotal < pts:
            raise ValueError("Not enough points to Redeem!")
        else:
            while pts > 0:
                #grab earliest timestamp and payer/points that correspond to it
                toRemove = min(self.timestamps)
                payer = self.timestamps[toRemove]
                payerDict = self.payers[payer][0]
                pointsToRemove = min(payerDict[toRemove],pts)
                #pop from timestamp dicts
                self.timestamps.pop(toRemove)
                self.payers[payer][0].pop(toRemove)
                #update runningTotal
                self.runningTotal -= pointsToRemove
                #update total in payer points
                payerDict = self.payers[payer][0]
                payerPoints = self.payers[payer][1]
                self.payers[payer] = [payerDict,
                                     payerPoints - pointsToRemove]
                #decriment pts 
                pts -= pointsToRemove
                #log amount removed from payer
                if payer in removalDict:
                    removalDict[payer] += pointsToRemove
                else:
                    removalDict[payer] = pointsToRemove
        #TODO: Fix output
        output = []
        for key in removalDict.keys():
            output.append({"payer":key,"points":removalDict[key] * -1})
        return json.dumps(output)

    def checkBalance(self):
        """
        Checks the balance of each payer

            Returns: json file of payer balance
        """
        payerBalance = {}
        for payer in self.payers.keys():
            payerBalance[payer] = self.payers[payer][1]
        return json.dumps(payerBalance)
    
