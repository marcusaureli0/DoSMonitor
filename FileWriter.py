import xml.etree.ElementTree as et
import RuleInterpreter as ri
import RuleModel as rm

class FileWriter:

    def __init__(self, configFileWithPath):
        self.configFileWithPath = configFileWithPath
        self.ruleInterpreter = ri.RuleInterpreter()
    
    def writeRuleStr(self, rule):
        if self.ruleInterpreter.isRule(rule):
            # escreve a regra no arquivo de configuracao
            # config.xml do pfSense 
            print('Rule detected: ', rule)
            ruleModel = rm.RuleModel(rule)
            return self.writeRule(ruleModel)
        return False

    
    # Verifica se as regras existentes no config.xml do pfSense
    # sao as mesmas definidas no obejto ruleModel
    def ruleNotExist(self, ruleModel, filterChilds):
        sameIP = False
        sameInterface = False
        for rule in filterChilds:
            for item in rule:
                if item.tag == 'source':
                    for sourceChild in item:
                        if sourceChild.tag == 'address' and sourceChild.text == ruleModel.sourceAddress:
                            sameIP = True
                        elif sourceChild == 'interface' and sourceChild.text == ruleModel.interface:
                            sameInterface = True

            if sameIP and sameInterface:
                break

        return not sameIP or not sameInterface

    def writeRule(self, ruleModel):
        print('Writing rule in ', self.configFileWithPath)
        with open (self.configFileWithPath , "r+") as f:
            print('reading lines of ', self.configFileWithPath)
            print('parsing xml file...', self.configFileWithPath)
        
            try:
                tree = et.parse(self.configFileWithPath)
                root = tree.getroot()
                
                for filterChilds in root.findall(".//filter"):
                    if self.ruleNotExist(ruleModel, filterChilds):
                        # escrever RuleModel no config.xml
                        newRule = et.Element('rule')
                        tracker = et.SubElement(newRule, 'tracker')
                        
                        created = et.SubElement(newRule, 'created')
                        createdTime = et.SubElement(created, 'time')
                        createdUsername = et.SubElement(created, 'username')

                        updated = et.SubElement(newRule, 'updated')
                        updatedTime = et.SubElement(updated, 'time')
                        updatedUsername = et.SubElement(updated, 'username')

                        type = et.SubElement(newRule, 'type')
                        interface = et.SubElement(newRule, 'interface')
                        ipprotocol = et.SubElement(newRule, 'ipprotocol')
                        protocol = et.SubElement(newRule, 'protocol')
                        destination = et.SubElement(newRule, 'destination')
                        destAny = et.SubElement(destination, 'any')

                        source = et.SubElement(newRule, 'source')
                        sourceAddress = et.SubElement(source, 'address')

                        sourceAddress.text = ruleModel.sourceAddress
                        tracker.text = ruleModel.tracker
                        createdTime.text = ruleModel.createdTime
                        createdUsername.text = ruleModel.createdUserName
                        updatedTime.text = ruleModel.updatedTime
                        updatedUsername.text = ruleModel.updatedByUser
                        type.text = ruleModel.type
                        interface.text = ruleModel.interface
                        ipprotocol.text = ruleModel.ipprotocol
                        protocol.text = ruleModel.protocol
                        
                        filterChilds.append(newRule)
                        tree.write(self.configFileWithPath)
                        print('rule added successfully')
                        return True
                    else:
                        print('not added. Rule exists on config.xml')
                        break
            except:
                print('error on parsing xml file')     
            
            return False