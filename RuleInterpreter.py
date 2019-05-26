class RuleInterpreter:
    ruleKeys = ['DDoS','DoS']


    def isRule(self, rule):
        for key in self.ruleKeys:
            if rule in key:
                return True

        return False