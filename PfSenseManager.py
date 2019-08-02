import os
class PfSenseManager:

    def __init__(self):
        print('initializing PfSenseManager')

    def updateSystemRules(self):
        try:
             # clear cache
            os.remove('/tmp/config.cache')

            # sync filters
            os.system('/etc/rc.filter_configure_sync')

            # clear pfsense state
            os.system('pfctl -F state')
            print('rules updated successfully')
        except:
            print('failed, rules not updated')
