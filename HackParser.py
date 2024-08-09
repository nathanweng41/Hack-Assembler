class Parser(object):
    def __init__(self, filePath):
        content = []
        with open(filePath, 'r') as file:
            for line in file:
                line = line.split("//",1)[0]
                cleanedLine = line.strip()
                #if '//' in cleanedLine:
                #continue
                if cleanedLine:
                    content.append(cleanedLine)
        self.content = content
        self.currentCommand = None
        self.value = 0
        self.hasMoreLinestoParse = True
        self.currentCommandType = None
    def reset(self):
        self.currentCommand = None
        self.value = 0
        self.hasMoreLinestoParse = True
        self.currentCommandType = None
    def hasMoreCommands(self):
        return self.value < len(self.content) - 1
    def InstructionType(self):
        if self.currentCommand == ' ':
            self.currentCommandType = "Empty Line"
        elif self.currentCommand[0] == "@":
            self.currentCommandType = "A_INSTRUCTION"
        elif self.currentCommand[0] == "(":
            self.currentCommandType = "L_INSTRUCTION"
        elif '=' in self.currentCommand or ';' in self.currentCommand:
            self.currentCommandType = "C_INSTRUCTION"
        else:
            raise TypeError("Not A Command")
    def advance(self):
        if(self.currentCommand == None):
            self.currentCommand = self.content[self.value]
            self.currentCurrentCommandType = Parser.InstructionType(self)
        else:
            if(Parser.hasMoreCommands(self)):
                self.value += 1
                self.currentCommand = self.content[self.value]
                self.currentCurrentCommandType = Parser.InstructionType(self)
            else:
                self.hasMoreLinestoParse = False
                print("No more commands!")
    def getCurrentCommand(self):
        return self.currentCommand
    def getCurrentCommandType(self):
        return self.currentCommandType
    def getCurrentSymbol(self):
        if Parser.getCurrentCommandType(self) == "A_INSTRUCTION":
            return self.content[self.value][1:]
        if Parser.getCurrentCommandType(self) == "L_INSTRUCTION":
            return self.content[self.value][1:len(self.content[self.value])-1]
    def getDest(self):
        if Parser.getCurrentCommandType(self) != "C_INSTRUCTION":
            raise TypeError("Not a C_INSTRUCTION")
        if "=" in self.content[self.value]:
            destLetters = self.content[self.value][0:self.content[self.value].index("=")] 
            return destLetters
        else:
            return ''
    def getComp(self):
        if Parser.getCurrentCommandType(self) != "C_INSTRUCTION":
            raise TypeError("Not a C_INSTRUCTION")
        if "=" in self.content[self.value]:
            compLetters = self.content[self.value][self.content[self.value].index("=")+1:] 
            return compLetters
        if ";" in self.content[self.value]:
            compLetters = self.content[self.value][:self.content[self.value].index(";")]
        return compLetters
    def getJump(self):
        if Parser.getCurrentCommandType(self) != "C_INSTRUCTION":
            raise TypeError("Not a C_INSTRUCTION")
        if ";" in self.content[self.value]:
            jmpLetters = self.content[self.value][self.content[self.value].index(";")+1:] 
            return jmpLetters
        else:
            return ''
    def __str__(self) -> str:
        output = ''
        for item in self.content:
            output += item + '\n'
        #optional: remove comment to remove last backspace
        #output = output.rstrip("\n")
        return output
p = Parser('Rect.asm')
print(p)