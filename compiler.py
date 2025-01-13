#Reformats each instrucitons into a list of tokens. Also removes comments and empty line
def format (instructions):
    formattedInstructions =  []

    #Will format each instruction properly
    for x in range(len(instructions)):
        #Prevents going out of bounds
        if (x == len(instructions)):
            break

        #If the instruction is empty, remove it
        if (instructions[x] == "\n" or instructions[x][0] == "/"):
            instructions = instructions[0:x] + instructions[x:]
            x -= 1
        else:
            #Makes it uppercase
            instructions[x] = instructions[x].upper()

            #Remove the \n
            if (x != len(instructions)-1):
                instructions[x] = instructions[x][0:-1]

            #Remove all spaces
            instructions[x] = instructions[x].replace(" ", "")


            #If the instruction has a comment, remove it
            if ("//" in instructions[x]):
                instructions[x] = instructions[x][0:instructions[x].find("//")]

            #Extracts the first three chars from instruction (The instruction name)
            name = instructions[x][0:3]
            instructions[x] = instructions[x][3:]

            #Splits the instructions into each token
            instructions[x] = [name] + instructions[x].split(",")

            formattedInstructions += [instructions[x]]
    
    return formattedInstructions

#Returns the binary code of a register
def binCode (register):
    if (register == "X0"):
        return "00"
    if (register == "X1"):
        return "01"
    if (register == "X2"):
        return "10"
    return "11"

#Converts immediate number to a 4-bit binary string
def decToBin (immediate):
    return bin(int(immediate))[2:].zfill(4)

#Sets a given index to a new char
def setChar (string, index, char):
    return string[0:index] + char + string[index+1:]

#Returns the hex code of a given instruction
def toHex (instruction):
    #The binary string to represent the function (THis is just opcodes to start)
    binString = "100000"

    #ADD
    if (instruction[0] == "ADD"):
        #Check if immediate number
        if (instruction[2].isdigit()):
            binString = setChar(binString, 3, "1")
            binString += decToBin(instruction[2])

            binString += binCode(instruction[1])
            binString += "00"
            binString += binCode(instruction[3])
        else:
            binString += "0000"
            binString += binCode(instruction[1])
            binString += binCode(instruction[2])
            binString += binCode(instruction[3])

    #SUB
    if (instruction[0] == "SUB"):
        binString = setChar(binString, 5, "1")

        #Check if immediate number
        if (instruction[2].isdigit()):
            binString = setChar(binString, 3, "1")
            binString += decToBin(instruction[2])

            binString += binCode(instruction[1])
            binString += "00"
            binString += binCode(instruction[3])
        else:
            binString += "0000"
            binString += binCode(instruction[1])
            binString += binCode(instruction[2])
            binString += binCode(instruction[3])
    
    #LDR
    if (instruction[0] == "LDR"):
        binString = setChar(binString, 4, "1")

        #Check if immediate number
        if (instruction[2].isdigit()):
            binString = setChar(binString, 3, "1")
            binString += decToBin(instruction[2])

            binString += binCode(instruction[1])
            binString += "00"
            binString += binCode(instruction[3])
        else:
            binString += "0000"
            binString += binCode(instruction[1])
            binString += binCode(instruction[2])
            binString += binCode(instruction[3])

    #STR
    if (instruction[0] == "STR"):
        binString = setChar(binString, 4, "1")
        binString = setChar(binString, 5, "1")

        #Check if immediate number
        if (instruction[2].isdigit()):
            binString = setChar(binString, 3, "1")
            binString += decToBin(instruction[2])

            binString += binCode(instruction[1])
            binString += "00"
            binString += binCode(instruction[3])
        else:
            binString += "0000"
            binString += binCode(instruction[1])
            binString += binCode(instruction[2])
            binString += binCode(instruction[3])
    
    #SET
    if (instruction[0] == "SET"):
        binString = setChar(binString, 2, "1")

        #Check if immediate number
        if (instruction[1].isdigit()):
            binString = setChar(binString, 3, "1")
            binString += decToBin(instruction[1])

            binString += "00"
            binString += "00"
            binString += binCode(instruction[2])
        else:
            binString += "0000"
            binString += "00"
            binString += binCode(instruction[1])
            binString += binCode(instruction[2])
    
    #DIS
    if (instruction[0] == "DIS"):
        binString = setChar(binString, 1, "1")
        binString = setChar(binString, 4, "1")

        #Check if immediate number
        if (instruction[1].isdigit()):
            binString = setChar(binString, 2, "1")
            binString = setChar(binString, 3, "1")
            binString += decToBin(instruction[1])

            binString += "00"
            binString += "00"
            binString += "00"
        else:
            binString += "0000"
            binString += "00"
            binString += "00"
            binString += binCode(instruction[1])
    
    binString = "0b" + binString

    return [str(hex(int(binString, base=2)))[2:]]

#Writes the hex code instructions into a RAM image
def makeImage (hexCodes):
    imageString = "v3.0 hex words plain\n"

    index = 0

    for x in range(16):
        for y in range(16):
            if (index < len(hexCodes)):
                imageString += hexCodes[index] + " "
                index += 1
            else:
                imageString += "0000 "
        imageString = imageString[:-1] + "\n"
    
    return imageString


fileName = input("Enter the name of the file (.barb) to be compiled: ")

program = open(fileName, "r")

instructions = program.readlines()

instructionImage = open(fileName.split(".")[0]+".txt", "w")

instructions = format(instructions)


hexCodes = []
for instruction in instructions:
    hexCodes += toHex(instruction)

instructionImage.write(makeImage(hexCodes))

program.close()
instructionImage.close()