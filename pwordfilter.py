import sys, os

class main:

    def mergeString(self,ch):
        st = ""
        for c in ch:
            st += c
        return st

    def removeNewLine(self,ch):
        index = 0
        newCH = []
        while index < len(ch)-1:
            newCH.append(ch[index])
            index += 1
        if ch[index] == '\n':
            return newCH
        return ch
    
    def Characters(self,line):
        ch = self.removeNewLine(list(line))
        for c in ch:
            i = ord(c)
            if i > 126 or i < 33:
                return False
        return True

    def correctSize(self,line,s):
        if s == -1:
            return True
        if len(line)-1 == s:
            return True
        return False

    def correctNumbers(self,line,n):
        if n == -1:
            return True
        ch = self.removeNewLine(list(line))
        for c in ch:
            i = ord(c)
            if n == 0:
                if i > 47 and i < 58:
                    return False
            elif n == 1:
                if i > 47 and i < 58:
                    return True
        return True

    def correctLower(self,line,l):
        if l == -1:
            return True
        ch = self.removeNewLine(list(line))
        for c in ch:
            i = ord(c)
            if l == 0:
                if i > 96 and i < 123:
                    return False
            elif l == 1:
                if i > 96 and i < 123:
                    return True
        return True

    def correctUpper(self,line,u):
        if u == -1:
            return True
        ch = self.removeNewLine(list(line))
        for c in ch:
            i = ord(c)
            if u == 0:
                if i > 64 and i < 91:
                    return False
            elif u == 1:
                if i > 64 and i < 91:
                    return True
        return True

    def correctSymbols(self,line,x):
        if x == -1:
            return True
        ch = self.removeNewLine(list(line))
        for c in ch:
            i = ord(c)
            if x == 0:
                if (i > 32 and i < 48) or (i > 57 and i < 65) or (i > 90 and i < 97) or (i > 122 and i < 127):
                    return False
            elif x == 1:
                if (i > 32 and i < 48) or (i > 57 and i < 65) or (i > 90 and i < 97) or (i > 122 and i < 127):
                    return True
        return True
            

    def meetsCriteria(self,line,s,n,l,u,x):
        if self.Characters(line) == False:
            return False
        if self.correctSize(line,s) == False:
            return False
        if self.correctNumbers(line,n) == False:
            return False
        if self.correctLower(line,l) == False:
            return False
        if self.correctUpper(line,u) == False:
            return False
        if self.correctSymbols(line,x) == False:
            return False
        return True

    def readCont(self):
        contInfo = []
        with open("continue.txt",'r') as r:
            for line in r:
                contInfo.append(self.mergeString(self.removeNewLine(line)))
            r.close()
        print(contInfo)
        return contInfo

    def __init__(self, args):
        nSize = nInput = nOutput = nNumbers = nLower = nUpper = nSymbols = cont = Help = False
        size = numbers = lower = upper = symbols = -1
        Input = Output = ""
        for arg in args:
            if nSize:
                size = int(arg)
                nSize = False
            elif nInput:
                Input = arg
                nInput = False
            elif nOutput:
                Output = arg
                nOutput = False
            elif nNumbers:
                numbers = int(arg)
                nNumbers = False
            elif nLower:
                lower = int(arg)
                nLower = False
            elif nUpper:
                upper = int(arg)
                nUpper = False
            elif nSymbols:
                symbols = int(arg)
                nSymbols = False
            if arg == "--help" or arg == "-h":
                Help = True
                print("Python Script to filter a list of passwords that meet criteria.")
                print("Arguments:")
                print("--help or -h = help")
                print("-c = continue last session")
                print("-s [size] = defines length of password")
                print("-i [input file] = defines input file of passwords")
                print("-o [output file] = defines output file of filtered passwords")
                print("Criteria: (if absent, it will assume there is no preference)")
                print("-n [0/1] = (no numbers/has numbers)")
                print("-l [0/1] = (no lowercase letters/has lowercase letters)")
                print("-u [0/1] = (no uppercase letters/has uppercase letters)")
                print("-x [0/1] = (no symbols/has symbols)")
            elif arg == "-c":
                cont = True
            elif arg == "-s":
                nSize = True
            elif arg == "-i":
                nInput = True
            elif arg == "-o":
                nOutput = True
            elif arg == "-n":
                nNumbers = True
            elif arg == "-l":
                nLower = True
            elif arg == "-u":
                nUpper = True
            elif arg == "-x":
                nSymbols = True

        if Input != "" and Output != "" and Help == False:
            if os.path.isfile(Input) == False:
                print("\n\nInput does not exist.")
                sys.exit()
            if os.path.isfile(Output):
                answer = raw_input("\nOutput file exists.\nDo you want to overwrite [0], append [1], cancel [2]?")
                if int(answer) == 0:
                    with open(Output,'w') as w:
                        with open(Input,'r') as r:
                            index = 0
                            try:
                                for line in r:
                                    if self.meetsCriteria(line,size,numbers,lower,upper,symbols):
                                        w.write(line)
                                    if index % 100000 == 0:
                                        print(str(index))
                                    index += 1
                            except KeyboardInterrupt:
                                r.close()
                                w.close()
                                print("\nIf you would like to continue this session, use -c on next run.")
                                with open("continue.txt","w") as c:
                                    c.write(str(index) + "\n" + Input + "\n" + Output + "\n" + str(size) + "\n" + str(numbers) + "\n" + str(lower) + "\n" + str(upper) + "\n" + str(symbols))
                                c.close()
                                sys.exit()
                        r.close()
                    w.close()
                elif int(answer) == 1:
                    with open(Output,'a') as w:
                        with open(Input,'r') as r:
                            index = 0
                            try:
                                for line in r:
                                    if self.meetsCriteria(line,size,numbers,lower,upper,symbols):
                                        w.write(line)
                                    if index % 100000 == 0:
                                        print(str(index))
                                    index += 1
                            except KeyboardInterrupt:
                                r.close()
                                w.close()
                                print("\nIf you would like to continue this session, use -c on next run.")
                                with open("continue.txt","w") as c:
                                    c.write(str(index) + "\n" + Input + "\n" + Output + "\n" + str(size) + "\n" + str(numbers) + "\n" + str(lower) + "\n" + str(upper) + "\n" + str(symbols))
                                c.close()
                                sys.exit()
                        r.close()
                    w.close()
                elif int(answer) == 2:
                    sys.exit()
            else:
                with open(Output,'a') as w:
                    with open(Input,'r') as r:
                        index = 0
                        try:
                            for line in r:
                                if self.meetsCriteria(line,size,numbers,lower,upper,symbols):
                                    w.write(line)
                                if index % 100000 == 0:
                                    print(str(index))
                                index += 1
                        except KeyboardInterrupt:
                            r.close()
                            w.close()
                            print("\nIf you would like to continue this session, use -c on next run.")
                            with open("continue.txt","w") as c:
                                c.write(str(index) + "\n" + Input + "\n" + Output + "\n" + str(size) + "\n" + str(numbers) + "\n" + str(lower) + "\n" + str(upper) + "\n" + str(symbols))
                            c.close()
                            sys.exit()
                    r.close()
                w.close()
        elif cont:
            contInfo = self.readCont()
            index = int(contInfo[0])
            Input = contInfo[1]
            Output = contInfo[2]
            size = int(contInfo[3])
            numbers = int(contInfo[4])
            lower = int(contInfo[5])
            upper = int(contInfo[6])
            symbols = int(contInfo[7])
            with open(Output,'a') as w:
                with open(Input,'r') as r:
                    try:
                        r.seek(index)
                        for line in r:
                            if self.meetsCriteria(line,size,numbers,lower,upper,symbols):
                                w.write(line)
                            if index % 100000 == 0:
                                print(str(index))
                            index += 1
                    except KeyboardInterrupt:
                        r.close()
                        w.close()
                        print("\nIf you would like to continue this session, use -c on next run.")
                        with open("continue.txt","w") as c:
                            c.write(str(index) + "\n" + Input + "\n" + Output + "\n" + str(size) + "\n" + str(numbers) + "\n" + str(lower) + "\n" + str(upper) + "\n" + str(symbols))
                        c.close()
                        sys.exit()
                r.close()
            w.close()
            

main(sys.argv)
