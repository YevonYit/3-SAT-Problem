import random
import time

class SAT:
    def __init__(self):
 
        self.literals = []
        self.literalsValue = {}
        self.literalsValueComplement = {}
        self.formula = ""
        self.s = ""

        
    '''Generate a list of literals according to the number of literals stated by the user'''
    def LiteralListGenerator(self,numOfLiterals):
        for s in range(1,numOfLiterals + 1):
            self.literals.append("s"+str(s))
        for t in range(1, numOfLiterals + 1):
            self.literals.append("¬s"+str(t))


    '''Generate dictionaries by creating key value pair for each literal''' 
    def DictKeyValueGenerator(self,numOfLiterals):
        for s in range(numOfLiterals,0,-1):
            self.literalsValue["s"+str(s)] = 0
            self.literalsValueComplement["¬s"+str(s)] = 1


    '''Set string s'''
    def SetValueS(self,numOfLiterals):
        self.s = "0"*numOfLiterals


    '''Generate problem randomly according to number of clauses stated by the user'''
    def ProblemGenerator(self,numOfClauses):
        checkList = []
        for s in range (numOfClauses):
            while True:
                temp = self.literals.copy()
                tempCheckList = []

                choice1 = random.choice(temp)
                temp.remove(choice1)
                choice2 = random.choice(temp)
                temp.remove(choice2)
                choice3 = random.choice(temp)

                if s == 0:
                    checkList.append([choice1,choice2,choice3])
                    break

                else:     
                    tempCheckList.append([choice1,choice2,choice3])
                    counter = 0

                    for item in checkList:
                        if set(item) != set(tempCheckList[0]):
                            counter += 1
                        else:
                            counter = 0
                            break
                        
                        
                    if counter > 0:
                        checkList.append([choice1,choice2,choice3])
                        break
                    else:
                        continue
                        

            
            if s != 0:
                self.formula = self.formula + " ∧ "
            self.formula = self.formula + "(" + choice1 +" ∨ " + choice2 +" ∨ " + choice3 + ")"

            
        return self.formula


    '''Assign new value to literals inside dictionary by incrementing 1 in binary form'''
    def AssignValueDictionary(self):
        self.s = ('{:0'+str(_input)+'b}').format(1 + int(self.s, 2))

        original = self.s
        original = original[::-1]
        reverse = list(self.s)
        
        for t in range (len(reverse)):
            if reverse[t] == '0':
                reverse[t] = 'a'
            else:
                reverse[t] = 'b'
                
        for u in range (len(reverse)):
            if reverse[u] == 'a':
                reverse[u] = '1'
            else:
                reverse[u] = '0'

        reverse = "".join(reverse)
        reverse = reverse[::-1]
        
        counter = 0
        for i in self.literalsValueComplement:
            self.literalsValueComplement[i] = int(reverse[counter])
            counter += 1

        counter1 = 0
        for i in self.literalsValue:
            self.literalsValue[i] = int(original[counter1])
            counter1 += 1



    '''Substitute the boolean value of each literal into the formula'''
    def AssignValueFormula(self):
        newFormulaWithAssignment = self.formula

        for key in self.literalsValueComplement:
            newFormulaWithAssignment = newFormulaWithAssignment.replace(key,str(self.literalsValueComplement[key]))
        for key in self.literalsValue:
            newFormulaWithAssignment = newFormulaWithAssignment.replace(key,str(self.literalsValue[key]))

        #print(newFormulaWithAssignment)
        return newFormulaWithAssignment


    '''Check each of the clauses to get true or false value'''
    def CheckClauses(self,newFormula):
        stringLength = len(self.formula)
        newClauseFormula = ""
        
        for i in range (0,stringLength,14):
            if newFormula[i:i+11] != "":
                if i != 0:
                    newClauseFormula += " ∧ "
                if "1" in newFormula[i:i+11]:
                    newClauseFormula += "1"
                else:
                    newClauseFormula += "0"
                
        return newClauseFormula
                

    '''Check the entire formula to to determine whether a solution is found'''
    def CheckProblem(self,clauseFormula):
        if "0" in clauseFormula:
            return 0
        else:
            return 1


        
       
if __name__ == '__main__':
    _input = 16 #literals
    a = SAT()
    counter = 0
    search_count = 0
    totalSec = 0
    
    for i in range(30):
            
        start = time.time()
        
        a.LiteralListGenerator(_input)
        a.DictKeyValueGenerator(_input)
        a.SetValueS(_input)
        '''print("Initialized literals list: ", a.literals,"\n")
        print("Initialized dictionary value:")
        print(a.literalsValue)
        print(a.literalsValueComplement)
        print()'''
        print("Problem Generation: " + a.ProblemGenerator(20) + "\n") #clause

        print("Checking for solution...")
        
        while a.s != ("1"*_input):     
            if counter != 0:
                a.AssignValueDictionary()
                #print()
            else:
                '''print(a.literalsValue)
                print(a.literalsValueComplement)
                print()'''
                counter += 1
            b = a.CheckClauses(a.AssignValueFormula())
            '''print(b)
            print()'''
            c = a.CheckProblem(b)
            if c == 1:
                search_count += 1
                
                print("There is/are solution(s) for this 3-SAT problem.\n")
                end = time.time()
                end1 = round(end - start , 4)
                print("Computing Time for search count", search_count, ":", end1 ,"s.")
                '''print(a.literalsValue)
                print(a.literalsValueComplement)
                print(b)
                print(c)'''
                break
            
            if a.s == ("1"*_input) and c == 0:
                search_count += 1
                end = time.time()
                end1 = round(end - start , 4)
                print("There is no solution for this 3-SAT problem.\n")
                print("Computing Time for search count", search_count, ": ", end1 ,"s.")
    
        totalSec += end1
        print("Total Computing Time Taken: ", (round(totalSec,4)) , "s.\n")

    avg = round(totalSec / 50 , 4)
    print("-----------------------------------------------")
    print("Average Computing Time: ", avg, "s.\n")
        
