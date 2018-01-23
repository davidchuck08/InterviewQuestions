class CheckCapital:
    def __init__(self, s):
        self.s = s
        
    def capitalCheck(self):
        return self.s[1:].islower() or self.s.islower() or self.s.isupper()
    
if __name__ == '__main__':
    c = CheckCapital("Rddsq")
    print c.capitalCheck()