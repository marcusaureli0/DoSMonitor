import time
import FileWriter as fw
import PfSenseManager as pfm

class FileMonitor:
    def __init__(self, configFileWithPath, snortLogPath):
        self.configFileWithPath = configFileWithPath
        self.snortLogPath = snortLogPath
        self.oldLine = ""
        self.fileWriter = fw.FileWiter(configFileWithPath)
        self.pfSenseManager = pfm.PfSenseManager()

    def start(self):
        print('Starting File monitor. Lisnening path ', self.snortLogPath)    
        while True:
            with open(self.snortLogPath, "r+") as f:
                lines = f.readlines()
                f.truncate(0)

                for line in lines:
                    if line != self.oldLine and line:
                        self.oldLine = line
                        writed = self.fileWriter.writeRuleStr(line)
                        print('rule: ', line, ', writed: ', writed)    
                        if writed:
                            self.pfSenseManager.updateSystemRules()

                time.sleep(2)
                f.close()