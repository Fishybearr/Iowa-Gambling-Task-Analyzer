import pandas as pd


#
#Function to calculate average reaction time in data
#
def CalcAverage(dataFrame):

    # Adds all 100 reaction times recored to timeAmounts list using pandas

    timeAmounts = dataFrame.loc[:,"Time"]

    


   


    # Running total used in average calculation
    total = 0

    # Adds each recorded time to total
    for x in timeAmounts:
        total += x

    # Calculates average in seconds
    total /= 100000

    #Formatted output
    output = "Average Reaction Time: {} seconds".format(total)
    print("--------------------------------------------------")
    print(output)
  
    
#
# Function to calculate % of high and low risk choices in data
#
def CalcRisk(dataFrame):
   
    
    
    
    

    # total of high risk choices
    totalHigh = 0
    
    #total of low risk choices
    totalLow = 0

    # Creates list of choices from data
    choices = dataFrame.loc[:,"Choice"]

    # If a choice is a 1 or 2 it is added to the high risk total (totalHigh)
    for i in choices:
        if(i < 3 ):
            totalHigh +=1



    # Calculates low risk choices by subtracting highRisk from 100
    totalLow = 100 - totalHigh

    #Formatting for output
    totalLowOut = "Low Risk Choices: {}%".format(totalLow)
    totalHighOut = "High Risk Choices: {}%".format(totalHigh)
    
    #Output
    print("--------------------------------------------------")
    print(totalHighOut)
    print(totalLowOut)
   
  


#
# Function to calculate number of times a fee occured in the data
#
def CalcFee(dataFrame):
    
    # Running total of the number of fees in the data
    numOfFees = 0


    # Adds each fee from the data to a list
    fees = dataFrame.loc[:,"Fee"]

    # If a fee is occurs (i == 1), 1 is added to numOfFees
    for i in fees:
        if(i == 1):
            numOfFees +=1
    

    #Output Formatting
    numOfFeesOut = "Percentage of time a fee was paid: {}%".format(numOfFees)
    
    #Output
    print("--------------------------------------------------")
    print(numOfFeesOut)
   
    

#
# Function to calculate:
#   1) Win Percentage
#   2) Loss Percentage
#   3) Total Amount Won
#   4) Total Amount Lost
#
def CalcWinLoss(dataFrame):
    
    # Reads prizes from data
    prize = dataFrame.loc[:,"Prize"]

    #Reads fees from data
    fee = dataFrame.loc[:,"FeeAmnt"]
    #Opens file for reading
    

   

    # Total amount lost
    totalLost = 0

    #total amount won
    totalwon = 0

    #Percentage of time user lost money (win/loss ratio)
    losePercent = 0

    # calculates totalWon, totalLost, and win/loss ratio
    for (i,x) in zip(prize,fee):
        totalwon += i
        totalLost += i -x

        if(i < x) :
            losePercent += 1

   

    
    
    
    #Output Formatting
    totalwonOut = "Total Amount Won: {}".format(totalwon)
    totalLostOut = "Total Amount Lost: {}".format(totalLost)

    winPercentOut = "Win Percentage: {}%".format(100 - losePercent)
    losePercentOut = "Loss Percentage: {}%".format(losePercent)
    
    #Output
    print("--------------------------------------------------")
    print(totalwonOut)
    print(totalLostOut)
    print("--------------------------------------------------")
    print(winPercentOut)
    print(losePercentOut)
    print("--------------------------------------------------")
    


#
# Function to take filePath of data from user
#
def ReadSpreadSheet():
    
    # Bool to check if user has entered a valid path
    validPath = False

    # while a valid path has not been entered, the program will keep asking user for a valid path
    while validPath == False :

        #Asks user for filepath
        filepath = input("Enter File Path: ")

        # Used for debugging, if user enters -1, program uses test filepath
        if(filepath == "-1") :
            filepath = "G:/IowaGamblingTask/Iowa_Gambling_Data.xlsx"
            print(filepath)

        #Attemps to open file, continues with exectution if it is sucessful
        try:
            df1 = pd.read_excel(filepath)
            validPath = True
    
        # If file cannot be opened, loop is executed again
        except:
            print("Error: File could not be accessed/located")
            
        

    # Returns filepath
    return df1
    

    
#Calls each function
df = ReadSpreadSheet()
CalcAverage(df)
CalcRisk(df)
CalcFee(df)
CalcWinLoss(df)
