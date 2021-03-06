#importing os and csv files 

import os 
import csv

#Set the path for the files in use
#csvpath = os.path.join('..','03-Python','PyBank Resources.csv') use when multi users 
csvpath = 'C:/Users/12104/OneDrive/Data-Bootcamp/Week 3/03-Python/PyBank Resources.csv'

with open (csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#identify header section 
    
    csv_header = next(csvreader)
    
    #List out data in file
    
    date = []
    
    profit = []
    
    monthly_changes = []
    
    
    #List variables in data
       
    count_months = 0
    
    net_profit = 0
    
    total_change_profits = 0
    
    starting_profit = 0

#Begin calculating 

    for row in csvreader:    
    
        #count the total number of months in the dataset
        
        count_months = count_months + 1 
    
    
    
          # Will need it when collecting the greatest increase and decrease in profits
    
        date.append(row[0])
    
    
    
          # Append the profit information & calculate the total profit
    
        profit.append(row[1])
    
        net_profit = net_profit + int(row[1])
    
    
    
          #Calculate the average change in profits from month to month. Then calulate the average change in profits
    
        final_profit = int(row[1])
    
        monthly_change_profits = final_profit - starting_profit
    
    
    
          #Store these monthly changes in a list
    
        monthly_changes.append(monthly_change_profits)
    
    
    
        total_change_profits = total_change_profits + monthly_change_profits
    
        starting_profit = final_profit
    
    
    
     #Calculate average change in profits
    
        average_profit_change = (total_change_profits/count_months)
    
          
    #Find point of highest and lowest profit 
    
        greatest_increase_profits = max(monthly_changes)
    
        greatest_decrease_profits = min(monthly_changes)
    
    
    #Determine when the points occured; index searches for element in ()
        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
    
#print layout
    print("---------------------------------------------")
    print("Financial Analysis")
    print("---------------------------------------------")
    print("Total Months: " + str(count_months))
    
    print("Total Profits: " + "$" + str(net_profit))
    
    print("Average Change: " + "$" + str(int(average_profit_change)))
    
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    
    print("----------------------------------------------")


with open('financial_analysis.txt', 'w') as text:

    text.write("----------------------------------------------------------\n")
    
    text.write("  Financial Analysis"+ "\n")
    
    text.write("----------------------------------------------------------\n\n")
    
    text.write("    Total Months: " + str(count_months) + "\n")
    
    text.write("    Total Profits: " + "$" + str(net_profit) +"\n")
    
    text.write("    Average Change: " + '$' + str(int(average_profit_change)) + "\n")
    
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    
    text.write("----------------------------------------------------------\n")

