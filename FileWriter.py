import xml.etree.ElementTree as et
import RuleInterpreter as ri
import RuleModel as rm

class FileWriter:

    def __init__(self, configFileWithPath):
        self.configFileWithPath = configFileWithPath
        self.ruleInterpreter = ri.RuleInterpreter()
    
    def writeRuleStr(self, rule):
        if self.ruleInterpreter.isRule(rule):
            # escreve a regra no arquivo de configuração
            #  config.xml do pfSense 
            print('Rule detected: ', rule)
            ruleModel = rm.RuleModel(rule)
            return self.writeRule(ruleModel)
        return False

    
    # Verifica se as regras existentes no config.xml do pfSense
    # são as mesmas definidas no obejto ruleModel
    def ruleNotExist(self, ruleModel, ruleChild):
        sameIP = False
        sameInterface = False
        for rule in ruleChild:
            for item in rule:
                if item.tag == 'source':
                    for sourceChild in item:
                        if sourceChild.tag == 'address' and sourceChild.text == ruleModel.sourceAddress:
                            sameIP = True
                        elif sourceChild == 'interface' and sourceChild.text == ruleModel.interface:
                            sameInterface = True
                
        return not sameIP or not sameInterface

    def writeRule(self, ruleModel):
        print('Writing rule in ', self.configFileWithPath)
        with open (self.configFileWithPath , "r+") as f:
            print('reading lines of ', self.configFileWithPath)
            print('parsing xml file...', self.configFileWithPath)
            print('rule: ', ruleModel.toXML())

            try:
                tree = et.parse(self.configFileWithPath)
                root = tree.getroot()
                
                for ruleChild in root.findall(".//filter"):
                    if self.ruleNotExist(ruleModel, ruleChild):
                        # escrever RuleModel no config.xml
                        print('rule added successfully')
                        return True
                    else:
                        print('not added. Rule exists on config.xml')
                        break
            except:
                print('error on parsing xml file')     
            
            return False