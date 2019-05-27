class RuleInterpreter:
    ruleKeys = ['DDoS','DoS']


    def isRule(self, rule):
        for key in self.ruleKeys:
            if key in rule:
                return True

        return False