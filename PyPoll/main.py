
# import dependencies
import os
import csv
import sys

votes = []
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

for name in candidates:
   if name not in candidates:
        candidates.append(name)
        x = name

candidate = votes[0]
count = 0
last_count = 0

for candidate in candidates:
    for vote in votes:
        if candidate == vote:
            total_votes += 1
    percent_vote = total_votes / len(votes)
    percent_vote.append(percent_vote)
    vote_count.append(vote_count)

    if last_count < total_votes:
        Winner = candidates
    print(f"{candidate}: {percent_vote:.3%} ({vote_count})")

    # reset vote count to zero
    last_count = total_votes
    total_votes = 0

print("Election Results")
print('-------------------------')
print(f"Total Votes: {total_votes}")
print('-------------------------')
# for candidate in candidates:
#     index = candidates.index(candidate)
# print(f"{candidates}: {percent_vote:.3%} ({vote_count})")
print(f"Winner: {Winner}")
print('-------------------------')

