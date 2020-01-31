PeriodicTable = {"N/A":0, "Na":22.989769, "Cl": 35.453, "H": 1.00784, "C":12.0107, "S":32.065, "O":15.999,"F":18.998403,"Mg":24.305,"Li":6.941, "Br":79.904, "He":4.002602, "K":39.0983} #Very limited table cause I didn't want to go through all 118


#Start of human input

#Equation = [First Element, Number Of First, Second Element, Number of Second, Third Element, Number of Third]
Equation = ["Na",1,"F",1,"N/A",0, "N/A", 0, "N/A", 0, "N/A", 0, "N/A", 0, "N/A", 0] #Enter Formula
#Equation = [First Element, Number Of First, Second Element, Number of Second, Third Element, Number of Third]
Equation2 = ["Mg",1,"F",2,"N/A",0, "N/A", 0, "N/A", 0, "N/A", 0, "N/A", 0, "N/A", 0] #Enter Formula

Grams = 5.5 #Insert grams here

MoleRatio1 = 2 #Enter First Mole Ratio
MoleRatio2 = 1 #Enter Second Mole Ratio

#End of user input





MMofElements = PeriodicTable[Equation[0]]*Equation[1] + PeriodicTable[Equation[2]]*Equation[3] + PeriodicTable[Equation[4]]*Equation[5] + PeriodicTable[Equation[6]]*Equation[7] #Moles per gram of left side
print(MMofElements) #moles per gram 1

SecondMMElements = PeriodicTable[Equation2[0]]*Equation2[1] + PeriodicTable[Equation2[2]]*Equation2[3] + PeriodicTable[Equation2[4]]*Equation2[5] + PeriodicTable[Equation2[6]]*Equation2[7] #Moles per gram of left side
SecondMM = SecondMMElements
print(SecondMM) #Moles per gram 2

FirstMM = Grams/MMofElements

Ratio = float(MoleRatio1)/float(MoleRatio2)

print(((FirstMM/Ratio)*SecondMM))

#All in 14 lines of code :)