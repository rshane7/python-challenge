import os
import csv

# Files to load 
election_file = "Resources/election_data.csv"

# Read the csv and convert it into a list of dictionaries
with open(election_file) as election_data:
    reader = csv.reader(election_data)

    # use of next to skip first title row in csv file
    next(reader) 
    voterid = []
    county = []
    candidate = []
    #ctr = 0
    #rows = 0
    #record = []

    #for record in reader:
    #if 'Khan' in record[0]:
    #    rows += 1
    #    ctr += record[0].count('Khan') 
    #elif "Correy" in record[0]:
    #    rows += 1
    #    ctr += record[0].count("Correy")
    #elif "Li" in record[0]:
    #    rows += 1
    #    ctr += record[0].count("Li")
	#elif "O'Tooley" in record[2]:
    #    rows += 1
	#    ctr += record[2].count("OTooley")

    for row in reader:
        voterid.append(row[0])
    
    # print result set
    print("Election Results")
    print("-------------------------------------------------------")
    print("Total Voters", len(voterid))
    print("-------------------------------------------------------")
    #print('Khan: {}, rows: {}'.format(ctr, rows))
    #print('Correy: {}, rows: {}'.format(ctr, rows))
    #print('Li: {}, rows: {}'.format(ctr, rows))
    #print("O'Tooley : {}, rows: {}".format(ctr, rows))
    print("-------------------------------------------------------")
    print("Winner: "                                               )
    print("-------------------------------------------------------")

# Zip lists together
election_results_csv = zip()

# Set variable for output file
output_file = os.path.join("Resources","election_results.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

# Write the header row
    writer.writerow(["Election Results"])
    writer.writerow(["------------------------------------"])
    writer.writerow(["Total Votes:", len(voterid)])
    writer.writerow(["------------------------------------"])
    writer.writerow(["Winner:                             "])                         
    writer.writerow(["------------------------------------"])

 # Write in zipped rows
    writer.writerows(election_results_csv)