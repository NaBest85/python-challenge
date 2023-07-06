import os
import csv
with open(r"C:\Users\nicho\OneDrive\Desktop\election_data.csv", newline="") as csvfile:
    pollreader = csv.reader(csvfile, delimiter= ",")


    total_votes = 0
    winner_votes = 0
    candidate_votes = {}
    candidates = []
    votes_count = []
    percentage_votes = []    
    candidate_order = []
    winner = ""


    next(pollreader)

   
    for row in pollreader:
        
        total_votes = total_votes + 1
        
        
        candidate_name = row[2]
        
       
        if candidate_name in candidates:
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

       
        else:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 1

    for win, value in candidate_votes.items():
        votes_count.append(value)
        votes = candidate_votes[candidate_name]
        percentage = round((int(value)/ total_votes * 100),2)
        percentage_votes.append(percentage)

        if (value > winner_votes):
            winner_votes = value
            winner= win

    candidate_order = zip(candidates,percentage_votes, votes_count)
    candidate_order = list(candidate_order)


    output_poll = open("output.txt", "w",newline="")




line1 = "Election Results"
line2 = "----------------------"
line3 = ([f'Total Votes :  {total_votes}'])
line4 = "----------------------"
output_poll.write("{}\n{}\n{}\n{}\n".format(line1, line2, line3, line4))
for index in candidate_order:
    linea = ([f'{index[0]} : {index[1]}00% ({index[2]})'])
output_poll.write("{}\n".format(linea))
line6 = "----------------------"
line7 = ([f'Winner : {winner}'])
line8 = "----------------------"
output_poll.write("{}\n{}\n{}\n".format(line6, line7, line8))

print("Election Results")
print("----------------------")
print(f"Total Votes: {str(total_votes)}")
print("----------------------")
for index in candidate_order:
    print([f'{index[0]} : {index[1]}00% ({index[2]})'])
print("----------------------")
print([f'Winner : {winner}'])
print("----------------------")
