class RuleModel:
    # def __init__(self, tracker, destinationIP, type, interface, ipprotocol, protocol,
    # sourceAddress, updatedTime, updatedByUser, createdTime, createdUserName):
        
    #     self.id = id 
    #     self.tracker = tracker
    #     self.destinationIP = destinationIP
    #     self.type = type
    #     self.interface = interface
    #     self.ipprotocol = ipprotocol
    #     self.protocol = protocol
    #     self.sourceAddress = sourceAddress
    #     self.updatedTime = updatedTime
    #     self.updatedByUser = updatedByUser
    #     self.createdUserName = createdUserName

    def __init__(self, rule):
        self.rule = rule
        self.id = ""
        self.tracker = ""
        self.destinationIP = ""
        self.type = ""
        self.interface = ""
        self.ipprotocol = ""
        self.protocol = ""
        self.sourceAddress = ""
        self.updatedTime = ""
        self.updatedByUser = ""
        self.createdUserName = ""
        self.updateInfo()

    # preenche as informações do obeto
    def updateInfo(self):
       # for c in self.rule:
       #     print(c)
        return True  

    

