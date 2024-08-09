class Code(object):
    jmpCodes = ['','JGT','JEQ','JGE','JLT','JNE','JLE','JMP']
    destCodes = ['','M','D','MD','A','AM','AD','AMD']
    compCodes = {'0':'0101010','1':'0111111','-1':'0111010','D':'0001100','A':'0110000','M':'1110000','!D':'0001101','!A':'0110011','!M':'1110001','-D':'0001111','-A':'0110011',
                 '-M':'1110011','D+1':'0011111','A+1':'0110111','M+1':'1110111','D-1':'0001110','A-1':'0110010','M-1':'1110010','D+A':'0000010','D+M':'1000010','D-A':'0010011',
                 'D-M':'1010011','A-D':'0000111','M-D':'1000111','D&A':'0000000','D&M':'1000000','D|A':'0010101','D|M':'1010101'}

    def convertAtoBin(self,integer):
        integer = format(integer,'015b')
        return integer
    def getAInstruction(self,aIns):
        return '0'+ Code.convertAtoBin(self,aIns)
    def getCInstruction(self,comp,dest,jump):
        return '111'+ Code.getBinComp(self, comp) + Code.getBinDest(self, dest) + Code.getBinJump(self, jump)
    def getBinJump(self,jump):
        a = self.jmpCodes.index(jump)
        return format(a,'003b')
    def getBinDest(self,dest):
        a = self.destCodes.index(dest)
        return format(a,'003b') 
    def getBinComp(self,comp):
        a = self.compCodes[comp]
        return a

