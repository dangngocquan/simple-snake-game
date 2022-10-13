from datetime import datetime
import json

##############################   CLASS ACCOUNT   ############################################################
class Account:
    def __init__(self, name="", createdTime="", winMatch=0, loseMatch=0,
                 totalTimePlayed=0):
        self.name = name
        self.createdTime = createdTime
        self.winMatch = winMatch
        self.loseMatch = loseMatch
        self.totalTimePlayed = totalTimePlayed
        

##############################   CLASS ACCOUNT MANAGER  #####################################################      
class AccountManager:
    def __init__(self, listAccount=[]):
        self.listAccount = listAccount
        
    def addNewAccount(self, account):
        if account.name in [acc.name for acc in self.listAccount]:
            return False
        else:
            self.listAccount.append(account)
            return True
        
    def removeAccount(self, indexAccount):
        self.listAccount.pop(indexAccount)
        
        
###########   Load data of Account Manager from json file   ############################################################
def loadData(path='./data/accounts/accounts.json'):
    accounts = []
    data = None
    with open(path, 'r') as file:
        data = json.load(file)
    file.close()
    
    for account in data['ACCOUNTS']:
        accounts.append(Account(
            name=account['NAME'],
            createdTime=account['CREATED_TIME'],
            winMatch=account['WIN_MATCH'],
            loseMatch=account['LOSE_MATCH'],
            totalTimePlayed=account['TOTAL_TIME_PLAYED']
        ))
    return AccountManager(listAccount=accounts)


###########   Save data of Account Manager to json file   ############################################################
def saveData(accountManager=[], path='./data/accounts/accounts.json'):
    data = {
        "ACCOUNTS" : [
            
        ]
    }
    
    for account in accountManager:
        data["ACCOUNTS"].append(
            {
                "NAME" : account.name,
                "CREATED_TIME" : account.createdTime,
                "WIN_MATCH" : account.winMatch,
                "LOSE_MATCH" : account.loseMatch,
                "TOTAL_TIME_PLAYED" : account.totalTimePlayed,
            }
        )
        
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
    file.close()
   

ACCOUNT_MANAGER = loadData()