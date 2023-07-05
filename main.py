import os
import csv
with open(r'C:\Users\nicho\OneDrive\Desktop\budget_data.csv') as csvfile:
    datareader = csv.reader(csvfile, delimiter = ",")
    Total_Months = 0
    Dates = []
    Profits = []
    Value = 0
    Total_Pl = 0
    Change = 0

    csv_header = next(datareader)
    First_Row = next(datareader)
    Total_Pl += int(First_Row[1])
    Value = int(First_Row[1])
    Total_Months += 1


    for row in datareader:     
        
        
        Total_Months += 1
        Dates.append(row[0])

     
        Change = int(row[1])-Value
        Profits.append(Change)
        Value = int(row[1])
        Total_Pl = Total_Pl + int(row[1])
        
        
       
        Avg_Change = sum(Profits)/len(Profits)   
       
        
        
        
       
        Greatest_Inc = max(Profits)       
        Greatest_Inc_index = Profits.index(Greatest_Inc)        
        Increase_Date_index = Dates[Greatest_Inc_index]


        Greatest_Dec = min(Profits)       
        Greatest_Dec_index = Profits.index(Greatest_Dec)
        Decrease_Date_index = Dates[Greatest_Dec_index]


        output = open("output.txt", "w")        

    line1 = "Financial Analysis"
    line2 = "----------------------------------"
    line3 = "Total Months: " + " = len(Dates)"
    line4 = "Total: $" + str(Total_Pl)
    line5 = "Average Change: $" + str(round(Avg_Change,2))
    line6 = "Greatest Increase in Profits: " + Increase_Date_index + " ($" + str(Greatest_Inc) + ")"
    line7 = "Greatest Increase in Profits: " + Decrease_Date_index + " ($" + str(Greatest_Dec) + ")"
    output.write("{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(line1,line2,line3,line4,line5,line6,line7))


    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {str(Total_Months)}")
    print(f"Total: ${str(Total_Pl)}")
    print(f"Average Change: ${str(round(Avg_Change,2))}")
    print(f"Greatest Increase in Profits: {Increase_Date_index} (${str(Greatest_Inc)})")
    print(f"Greatest Decrease in Profits: {Decrease_Date_index} (${str(Greatest_Dec)})")




    

