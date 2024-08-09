import HackCode
import HackParser
import SymbolTable

class HackAssembler(object):
    def __init__(self,input_File):
        self.parser = HackParser.Parser(input_File)
        self.file_name = "result.hack"
        self.hackCode = HackCode.Code()
        self.table = SymbolTable.SymbolTable()
    def parseForLabels(self):
        line = 0
        while self.parser.hasMoreCommands():
            self.parser.advance()
            if(self.parser.getCurrentCommandType() == 'L_INSTRUCTION'):
                if self.parser.getCurrentSymbol() in self.table.getSymbolTable():
                    raise KeyError("Key already exists in dictionary")
                else:
                    self.table.addEntry(self.parser.getCurrentSymbol(),line)
            else:
                line+=1
    def translate(self):
        file = open(self.file_name,"w")
        self.parser.reset()
        start = 16
        while self.parser.hasMoreCommands():
            self.parser.advance()
            if self.parser.getCurrentCommandType() == "A_INSTRUCTION":
                try:
                    file.write(self.hackCode.getAInstruction(int(self.parser.getCurrentSymbol())))
                    file.write("\n")
                except ValueError:
                    if self.table.contains(self.parser.getCurrentSymbol()):
                        regNum = self.table.getAddress(self.parser.getCurrentSymbol())
                        file.write(self.hackCode.getAInstruction(int(regNum)))
                        file.write("\n")
                    else:
                        self.table.addEntry(self.parser.getCurrentSymbol(),start)
                        regNum = self.table.getAddress(self.parser.getCurrentSymbol())
                        file.write(self.hackCode.getAInstruction(int(regNum)))
                        file.write("\n")
                        start+=1
            if self.parser.getCurrentCommandType() == "C_INSTRUCTION":
                dest = self.parser.getDest()
                comp = self.parser.getComp()
                jump = self.parser.getJump()
                file.write(self.hackCode.getCInstruction(comp,dest,jump))
                file.write("\n")
        file.close()
        return self.file_name
p = HackAssembler("Pong.asm")
p.parseForLabels()
p.translate()

