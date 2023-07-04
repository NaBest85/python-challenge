import os
import csv
with open(r'C:\Users\nicho\OneDrive\Desktop\budget_data.csv') as csvfile:
    datareader = csv.reader(csvfile, delimiter = "-")
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
    #print()
    for row in datareader:
        Dates.append(row[0])
        Value = int(row[1])
        Change = int(row[1])-Value
        Profits.append(Change)
        Total_Months += 1

        Total_Pl = Total_Pl + int(row[1])

        Avg_Change = sum(Profits)/len(Profits)
        Greatest_Inc = max(Profits)
        Greatest_Dec = min(Profits)
        Decrease_Date = Dates[Greatest_Dec]
        Increase_Date = Dates[Greatest_Inc]

        output = open("output.txt", "w")

        line1 = "Financial Analysis"
        line2 = "----------------------------------"
        #line3 = str("Total Months: [str(Total_Months)]")
        #line4 = str("Total: $[str(Total_Pl)]")
        #line5 = str("Average Change: $[str(round*(Avg_Change,2))]")
        #line6 = str("Greatest Increase in Profits: [Increase_Date] ($[str(Greatest_Inc)])")
        #line7 = str("Greatest Increase in Profits: [Decrease_Date] ($[str(Greatest_Dec)])")
        #output.write(format(line1,line2,line3,line4,line5,line6,line7))
        #output.write("[]\n[]\n[]\n[]\n[]\n[]\n[]\n".format(line1,line2,line3,line4,line5,line6,line7))

        line1 = "Financial Analysis"
        line2 = "----------------------------------"
        line3 = "Total Months: " + " = len(Dates)"
        line4 = "Total: $" + str(Total_Pl)
        line5 = "Average Change: $" + str(round(Avg_Change,2))
        line6 = "Greatest Increase in Profits: " + Increase_Date + " ($" + str(Greatest_Inc) + ")"
        line7 = "Greatest Increase in Profits: " + Decrease_Date + " ($" + str(Greatest_Dec) + ")"
        output.write("{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(line1,line2,line3,line4,line5,line6,line7))


        print("Financial Analysis")
        print("---------------------")
        print(f"Total Months: {str(Total_Months)}")
        print(f"Total: ${str(Total_Pl)}")
        print(f"Average Change: ${str(round(Avg_Change,2))}")
        print(f"Greatest Increase in Profits: {Increase_Date} (${str(Greatest_Inc)})")
        print(f"Greatest Decrease in Profits: {Decrease_date} (${str(Greatest_Dec)})")




    

