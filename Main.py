import FileMonitor as fm
## test
xmlFileWithPath = r"/cf/conf/config.xml"
snortLogPath = r"/var/log/snort/alert"    

fileMonitor = fm.FileMonitor(xmlFileWithPath, snortLogPath)
fileMonitor.start()
