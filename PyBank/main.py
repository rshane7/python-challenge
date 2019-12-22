import os
import csv

# Files to load (Remember to change these)
budget_file = "Resources/budget_data.csv"

# Read the csv and convert it into a list of dictionaries
with open(budget_file) as budget_data:
    reader = csv.reader(budget_data)

    # use of next to skip first title row in csv file
    next(reader) 
    budget = []
    date = []
    budget_diff = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in reader:
        budget.append(int(row[1]))
        date.append(row[0])

    # print result set
    print("Financial Analysis")
    print("-------------------------------------------------------")
    print("Total Months:", len(date))
    print("Total: $", sum(budget))
    
    #Loop through the budget column to find total budget, min/max and average differences in the budget. 
    for i in range(1,len(budget)):
        budget_diff.append(budget[i] - budget[i-1])   
        avg_budget_diff = sum(budget_diff)/len(budget_diff)
        max_budget_diff = max(budget_diff)
        min_budget_diff = min(budget_diff)
        max_budget_diff_date = str(date[budget_diff.index(max(budget_diff))])
        min_budget_diff_date = str(date[budget_diff.index(min(budget_diff))])
    
    # print results for the differences min/max and average
    print("Average Difference: $", round(avg_budget_diff))
    print("Greatest Increase in Profits:", max_budget_diff_date,"($", max_budget_diff,")")
    print("Greatest Decrease in Profits:", min_budget_diff_date,"($", min_budget_diff,")")

# Zip lists together
bank_budget_analysis_csv = zip()

# Set variable for output file
output_file = os.path.join("Resources","bank_budget_analysis.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Financial_Analysis"])
    writer.writerow(["------------------------------------"])
    writer.writerow(["Total Months:", len(date)])
    writer.writerow(["Total: ","$", sum(budget)])
    writer.writerow(["Average Difference: ","$", round(avg_budget_diff)])
    writer.writerow(["Greatest Increase in Profits:", max_budget_diff_date,"($",max_budget_diff,")"])
    writer.writerow(["Greatest Decrease in Profits:", min_budget_diff_date,"($",min_budget_diff,")"])

    # Write in zipped rows
    writer.writerows(bank_budget_analysis_csv)