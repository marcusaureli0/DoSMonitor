import xml.etree.ElementTree as et
import RuleInterpreter as ri
import RuleModel as rm

class FileWiter:

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

    def checkRule(self, ruleChildren):
        for children in ruleChildren:
            # comparar ruleModel com children.text
            print (children.text)
        return True

    def writeRule(self, ruleModel):
        print('Writing rule in ', self.configFileWithPath)
        with open (self.configFileWithPath , "r+") as f:
            print('reading lines of ', self.configFileWithPath)
            print('parsing xml file...', self.configFileWithPath)
            try:
                tree = et.parse(self.configFileWithPath)
                root = tree.getroot()

                # utilizar esse trecho de código para verificar se a regra que
                # será adicionada já se encontra no arquivo config.xml 
                for rules in root.findall(".//filter"):
                    for rule in rules.getchildren():
                        if self.checkRule(rule):
                            print('Adding rule in config.xml file')
                        else:
                            print('Rule exists. Not added.')
                return True
            except:
                print('error on parsing xml file')     
                return False