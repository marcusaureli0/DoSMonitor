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
    def checkRule(self, ruleChildren, ruleModel):
        for children in ruleChildren:
            # comparar ruleModel com children.text
            print (children.text)
        return True

    def writeRule(self, ruleModel):
        print('Writing rule in ', self.configFileWithPath)
        with open (self.configFileWithPath , "r+") as f:
            print('reading lines of ', self.configFileWithPath)
            print('parsing xml file...', self.configFileWithPath)
            print('rule: ', ruleModel.toXML())
            
            try:
                tree = et.parse(self.configFileWithPath)
                root = tree.getroot()

                for rules in root.findall(".//filter"):
                    rules = filterNode.getChildren()
                
                if self.ruleNotExist(ruleModel, rules):    
                    #filterNode.append(ruleModel.toXML())
                    print('rule added successfully')
                else:
                            print('Rule exists. Not added.')
                return True
            except:
                print('error on parsing xml file')     
                return False