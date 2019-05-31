import FileMonitor as fm

xmlFileWithPath = r"/cf/conf/config.xml"
snortLogPath = r"/var/log/snort/snort.log"    

fileMonitor = fm.FileMonitor(xmlFileWithPath, snortLogPath)
fileMonitor.start()