import os
import csv

election_data = "/Users/lucasludwig/Desktop/Python_Challenge/PyPoll/Resources/election_data.csv"

# Open and read csv
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Create lists to store data
    voter_id = []
    county = []
    candidate = []

    # Read through each row of data after the header
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    # The total number of votes cast
    total_votes = len(voter_id)

    # A complete list of candidates who received votes
    candidates = list(set(candidate))

    # The total number of votes each candidate won
    stockham_votes = candidate.count("Charles Casper Stockham")
    degette_votes = candidate.count("Diana DeGette")
    doane_votes = candidate.count("Raymon Anthony Doane")

    # The percentage of votes each candidate won
    stockham_percent = round((stockham_votes / total_votes) * 100, 3)
    degette_percent = round((degette_votes / total_votes) * 100, 3)
    li_percent = round((doane_votes / total_votes) * 100, 3)

    # The winner of the election based on popular vote.
    winner = max(stockham_votes, degette_votes, doane_votes)

    if winner == stockham_votes:
        winner_name = "Charles Casper Stockham"
    elif winner == degette_votes:
        winner_name = "Diana DeGette"
    elif winner == doane_votes:
        winner_name = "Raymon Anthony Doane"

    # Print the analysis to the terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    print(f"Charles Casper Stockham: {stockham_percent}% ({stockham_votes})")
    print(f"Diana DeGette: {degette_percent}% ({degette_votes})")
    print(f"Raymon Anthony Doane: {li_percent}% ({doane_votes})")
    print("-------------------------")
    print(f"Winner: {winner_name}")
    print("-------------------------")

    # Export a text file with the results
output_file = "/Users/lucasludwig/Desktop/Python_Challenge/PyPoll/Analysis/election_results.txt"

with open(output_file, "w") as txtfile:
    txtfile.write("Election Results")
    txtfile.write("-------------------------")
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write("-------------------------")
    txtfile.write(f"Charles Casper Stockham: {stockham_percent}% ({stockham_votes})")
    txtfile.write(f"Diana DeGette: {degette_percent}% ({degette_votes})")
    txtfile.write(f"Raymon Anthony Doane: {li_percent}% ({doane_votes})")
    txtfile.write("-------------------------")
    txtfile.write(f"Winner: {winner_name}")
    txtfile.write("-------------------------")
    
