import os
class PfSenseManager:

    def __init__(self):
        print('initializing PfSenseManager')

    def updateSystemRules(self):
        try:
            configCache = '/tmp/config.cache'
            cmd = '/etc/rc.filter_configure_sync'
            os.remove(configCache)
            os.system(cmd)
            print('rules updated successfully')
        except:
            print('failed, rules not updated')
