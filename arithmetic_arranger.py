def main():
    print("Enter test values: ")
    testvals = input().split(',')
    print("Find answers? (True/False)")
    answers = input()
    results = arithmetic_arranger(testvals, answers)
    print(results)


def arithmetic_arranger(problems, getAnswers=False):
    #Var Initialisation
    arranged_problems = ""
    lineOne = ""
    lineTwo = ""
    lineThree = ""
    lineFour = ""

    #Number of problems is not allowed to exceed 5 as per the test cases
    if(len(problems) > 5):
        return "Error: Too many problems."
    
    #Main loop, loops through all the arithmetic problems and contributes their outputs to the "lines"
    for problem in problems:
        #If symbol is found, returns index position. If not found, returns -1
        addIndex = problem.find('+')
        subIndex = problem.find('-')
        quotIndex = problem.find('\'')

        firstStart = 0
        firstEnd = 0
        secondStart = 0
        secondEnd = 0

        #If the current problem involves addition ->
        if(addIndex != -1):
            answer = 0
            firstStart = quotIndex + 1 #Finds the start index of first number
            firstEnd = addIndex - 1 #Finds last character index of first number
            num1 = problem[firstStart:firstEnd]

            if(num1.isnumeric() == False):
                return "Error: Numbers must only contain digits."
            elif(len(num1) > 4):
                return "Error: Numbers cannot be more than four digits."

            secondStart = addIndex + 2 #Finds the start index of second number
            secondEnd = len(problem) - 1 #Finds last character index of second number
            num2 = problem[secondStart:secondEnd]
            if(num2.isnumeric() == False):
                return "Error: Numbers must only contain digits."
            elif(len(num2) > 4):
                return "Error: Numbers cannot be more than four digits."
            totalWidth = len(str(max(int(num1), int(num2)))) + 2 #How many characters wide the current "block" is
            line1spaces = totalWidth - len(num1)

            # Output construction
            lineOne += ' ' * line1spaces
            lineOne += num1
            if(problems.index(problem) != len(problems) - 1):
                lineOne += "    "
            lineTwo += '+'
            lineTwo += ' ' * (totalWidth - (len(num2) + 1))
            lineTwo += num2
            if(problems.index(problem) != len(problems) - 1):
                lineTwo += "    "
            lineThree += '-' * totalWidth
            if(problems.index(problem) != len(problems) - 1):
                lineThree += "    "

            #This section calculates the arithmetic answer and adds it as an extra line to the block
            if(getAnswers == True):
                answer = int(num1) + int(num2)
                line4spaces = totalWidth - len(str(answer))
                lineFour += ' ' * line4spaces
                lineFour += str(answer)
                if(problems.index(problem) != len(problems) - 1):
                    lineFour += "    "

        #If the current problem involves subtraction ->
        elif(subIndex != -1):
            answer = 0
            firstStart = quotIndex + 1 #Finds the start index of first number
            firstEnd = subIndex - 1 #Finds last character index of first number
            num1 = problem[firstStart:firstEnd]
            if(num1.isnumeric() == False):
                return "Error: Numbers must only contain digits."
            elif(len(num1) > 4):
                return "Error: Numbers cannot be more than four digits."
            secondStart = subIndex + 2 #Finds the start index of second number
            secondEnd = len(problem) - 1 #Finds last character index of second number
            num2 = problem[secondStart:secondEnd]
            if(num2.isnumeric() == False):
                return "Error: Numbers must only contain digits."
            elif(len(num2) > 4):
                return "Error: Numbers cannot be more than four digits."
            totalWidth = len(str(max(int(num1), int(num2)))) + 2 #How many characters wide the current "block" is
            line1spaces = totalWidth - len(num1)

            # Output construction
            lineOne += ' ' * line1spaces
            lineOne += num1
            if(problems.index(problem) != len(problems) - 1):
                lineOne += "    "
            lineTwo += '-'
            lineTwo += ' ' * (totalWidth - (len(num2) + 1))
            lineTwo += num2
            if(problems.index(problem) != len(problems) - 1):
                lineTwo += "    "
            lineThree += '-' * totalWidth
            if(problems.index(problem) != len(problems) - 1):
                lineThree += "    "

            #This section calculates the arithmetic answer and adds it as an extra line to the block
            if(getAnswers == True):
                answer = int(num1) - int(num2)
                line4spaces = totalWidth - len(str(answer))
                lineFour += ' ' * line4spaces
                lineFour += str(answer)
                if(problems.index(problem) != len(problems) - 1):
                    lineFour += "    "

        else:
            return "Error: Operator must be '+' or '-'."
    
    #Final output construction
    arranged_problems += lineOne
    arranged_problems += "\n"
    arranged_problems += lineTwo
    arranged_problems += "\n"
    arranged_problems += lineThree

    #Only adds line 4 for "answers" if required, otherwise output only has 3 lines
    if(getAnswers == True):
        arranged_problems += "\n"
        arranged_problems += lineFour
    return arranged_problems

main()
