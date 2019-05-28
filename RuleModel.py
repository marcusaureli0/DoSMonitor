import time

class RuleModel:

    def __init__(self, rule):
        self.rule = rule
        timeEpoch = time.time()
        self.tracker = timeEpoch
        self.createdTime = timeEpoch
        self.updatedTime = timeEpoch
        self.type = 'reject'
        self.interface = 'lan'
        self.ipprotocol = 'inet'
        self.protocol = 'udp'
        self.updatedByUser = 'SpfManager'
        self.createdUserName = 'SpfManager'
        self.destinationIP = ''
        self.sourceAddress = ''
        self.sourcePort = ''
        self.destinationPort = ''
        self.updateInfo()

    # preenche as informações do objeto
    # Interpretar a seguinte mensagem:
    # 05/27-02:30:42.070886 [**] [1:321:3] DoS [**] [Priority: 0] 
    # {UDP} 192.168.1.102:5060 -> 192.168.1.1:5060
    def updateInfo(self):
        splited = self.rule.split(' ')
        count = 0
        print('splited rule: ', splited)
        for key in splited:
            if key == '->':
                destIpWithPort = splited[count + 1].split(':')
                sourceIpWithPort = splited[count-1].split(':')
                self.destinationIP = destIpWithPort[0]
                self.destinationPort = destIpWithPort[1]
                self.sourceAddress = sourceIpWithPort[0]
                self.sourcePort = sourceIpWithPort[1]
                print('found destinationIP: ', self.destinationIP, ', source: ', self.sourceAddress)
                break
            count = count + 1

        return self.destinationIP != '' and self.sourceAddress != ''

    def toXML(self):
        return '''
        <rule>
        <id></id>
        <tracker>%s</tracker>
        <type>%s</type>
        <interface>%s</interface>
        <ipprotocol>%s</ipprotocol>
        <tag></tag>
        <tagged></tagged>
        <max></max>
        <max-src-nodes></max-src-nodes>
        <max-src-conn></max-src-conn>
        <max-src-states></max-src-states>
        <statetimeout></statetimeout>
        <statetype><![CDATA[keep state]]></statetype>
        <os></os>
        <protocol>%s</protocol>
        <source>
            <address>%s</address>
        </source>
        <destination>
            <any></any>
        </destination>
        <descr></descr>
        <updated>
            <time>%s</time>
            <username>%s</username>
        </updated>
        <created>
            <time>%s</time>
            <username>%s</username>
        </created>
        <rule>
        ''' % (self.tracker, self.type, self.interface, self.ipprotocol, self.protocol,
                self.sourceAddress, self.updatedTime, self.updatedByUser,
                self.createdTime, self.createdUserName)

    

