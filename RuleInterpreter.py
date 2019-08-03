class RuleInterpreter:
    ruleKeys = ['->']


    def isRule(self, rule):
        for key in self.ruleKeys:
            if key in rule:
                return True

        return False