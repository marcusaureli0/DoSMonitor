import FileMonitor as fm

xmlFileWithPath = r"C:\Users\Marcus\Documents\config.xml"
snortLogPath = r"C:\Users\Marcus\Documents\test.txt"    

fileMonitor = fm.FileMonitor(xmlFileWithPath, snortLogPath)
fileMonitor.start()