# # import dependencies
# import os
# import csv
# import sys

# # set your variables
# votes = []
# vote_count = 0
# last_count = 0
# candidate_list = []
# candidate_count = 0
# candidate_percentage = 0

# # set csvpath
# csvpath = os.path.join ('Resources','election_data.csv')


# with open(csvpath, "r") as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')

#     # read the header row first (skip this if there is no header)
#     csv_header = next(csvreader)

#     for row in csvreader:
#         votes.append(row[2])

#     total_votes = len(votes)

#     for name in candidate_list:
#         if name not in candidate_list:
#             x = name
#             votes.append(name)     

# candidate = candidate_list[0]


# for candidate in candidate_list:
#     for vote in votes:
#         if candidate == vote:
#             vote_count += 1
    
#     if last_count < count:
#         win = candidate

#     count = 0 
#     last_count = 0
        

# print("Election Results")
# print('-------------------------')
# print(f"Total Votes: {total_votes}")
# print('-------------------------')
# print(f"Winner: {win}")
# print('-------------------------')


# import dependencies
import os
import csv
import sys

# these are the important variables for the election result
votes = []
# the following lists are 1- unique candidates, 2- percentage of their votes, 3- total count of their votes
candidates = []
percent_vote = []
vote_count = []
total_votes = 0
last_count = 0 

# set csvpath
csvpath = os.path.join ('Resources','election_data.csv')

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        votes.append(row[2])
        
total_votes = len(votes)

# find all the candidates and assign their indexes
for name in candidates:
   if name not in candidates:
        candidates.append(name)
        x = name

candidate = votes[0]
count = 0
last_count = 0

for candidate in candidates:
    for vote in votes:
        if candidate == votes:
            total_votes += 1
    percent_vote = total_votes / len(votes)
    percent_vote.append(percent)
    vote_count.append(count)

        if last_count < total_votes:
            winner = candidate    
        print(f"{candidate}: {percent_vote:.3%} ({vote_count})")

    # reset vote count to zero
    last_count = total_votes
    total_votes = 0

print("Election Results")
print('-------------------------')
print(f"Total Votes: {total_votes}")
print('-------------------------')
print(f"Winner: {Winner}")
print('-------------------------')
