def main():
    print("Enter test values: ")
    testvals = input().split(',')
    print("Find answers? (True/False)")
    answers = input()
    results = arithmetic_arranger(testvals, answers)
    print(results)


def arithmetic_arranger(problems, getAnswers=False):
    arranged_problems = ""
    lineOne = ""
    lineTwo = ""
    lineThree = ""
    lineFour = ""
    if(len(problems) > 5):
        return "Error: Too many problems."
    for problem in problems:
        print(problem)
        original = problem
        addIndex = problem.find('+')
        subIndex = problem.find('-')
        quotIndex = problem.find('\'')

        firstStart = 0
        firstEnd = 0
        secondStart = 0
        secondEnd = 0

        if(addIndex != -1):
            answer = 0
            firstStart = quotIndex + 1
            firstEnd = addIndex - 1
            num1 = problem[firstStart:firstEnd]
            if(num1.isnumeric() == False):
                return "Error: Numbers must only contain digits."
            elif(len(num1) > 4):
                return "Error: Numbers cannot be more than four digits."
            secondStart = addIndex + 2
            secondEnd = len(problem) - 1
            num2 = problem[secondStart:secondEnd]
            if(num2.isnumeric() == False):
                return "Error: Numbers must only contain digits."
            elif(len(num2) > 4):
                return "Error: Numbers cannot be more than four digits."
            totalWidth = len(str(max(int(num1), int(num2)))) + 2
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

            if(getAnswers == True):
                answer = int(num1) + int(num2)
                line4spaces = totalWidth - len(str(answer))
                lineFour += ' ' * line4spaces
                lineFour += str(answer)
                if(problems.index(problem) != len(problems) - 1):
                    lineFour += "    "

        elif(subIndex != -1):
            answer = 0
            firstStart = quotIndex + 1
            firstEnd = subIndex - 1
            num1 = problem[firstStart:firstEnd]
            if(num1.isnumeric() == False):
                return "Error: Numbers must only contain digits."
            elif(len(num1) > 4):
                return "Error: Numbers cannot be more than four digits."
            secondStart = subIndex + 2
            secondEnd = len(problem) - 1
            num2 = problem[secondStart:secondEnd]
            if(num2.isnumeric() == False):
                return "Error: Numbers must only contain digits."
            elif(len(num2) > 4):
                return "Error: Numbers cannot be more than four digits."
            totalWidth = len(str(max(int(num1), int(num2)))) + 2
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

            if(getAnswers == True):
                answer = int(num1) - int(num2)
                line4spaces = totalWidth - len(str(answer))
                lineFour += ' ' * line4spaces
                lineFour += str(answer)
                if(problems.index(problem) != len(problems) - 1):
                    lineFour += "    "

        else:
            return "Error: Operator must be '+' or '-'."
    arranged_problems += lineOne
    arranged_problems += "\n"
    arranged_problems += lineTwo
    arranged_problems += "\n"
    arranged_problems += lineThree
    if(getAnswers == True):
        arranged_problems += "\n"
        arranged_problems += lineFour
    return arranged_problems


main()
