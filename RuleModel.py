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
    # Interpretar a seguinte mensagem:
    # 05/27-02:30:42.070886 [**] [1:321:3] DoS [**] [Priority: 0] 
    # {UDP} 192.168.1.102:5060 -> 192.168.1.1:5060
    def updateInfo(self):
        splited = self.rule.split(' ')
        count = 0
        print('splited rule: ', splited)
        for key in splited:
            if key == '->':
                self.destinationIP = splited[count + 1]
                self.sourceAddress = splited[count-1]
                print('found destinationIP: ', self.destinationIP, ', source: ', self.sourceAddress)
                break
            count = count + 1

        return True  

    

