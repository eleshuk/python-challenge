
# import dependencies
import os
import csv
import sys

votes = []
candidates = []
candidate_count = []
percent_vote = []
total_votes = 0
last_count = 0 

# set csvpath
csvpath = os.path.join ('Resources','election_data.csv')

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # print header
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    # append votes column
    for row in csvreader:
        votes.append(row[2])
# calculate total number of votes for all candidates        
total_votes = len(votes)

# append candidates list
for name in votes:
   if name not in candidates:
        candidates.append(name)
        x = name

# set candidate list of votes
candidate = votes[0]
# set vote counter
vote_count = 0
# set last count
last_count = 0

# print election results and total votes
print("Election Results")
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')

# create for loop to calculate percentage of votes per candidate
for candidate in candidates:
    for vote in votes:
        # if the candidate has a vote towards them
        if candidate == vote:
            # increase vote count by 1
            vote_count += 1
    # calculate percent of votes per candidate
    percentage = vote_count / len(votes)
    # append the percent vote list
    percent_vote.append(percentage)
    # append the candidate count list
    candidate_count.append(vote_count)

    # if the vote count is greater th
    if last_count < vote_count:
        Winner = candidate
    print(f'{candidate}: {percentage:.3%} ({vote_count})')
    # reset last count to new vote count
    last_count = vote_count
    # reset vote count to zero
    vote_count = 0

# Winner = candidate

print('-------------------------')
print(f'Winner: {Winner}')
print('-------------------------')

stdoutOrigin=sys.stdout 
text_path = os.path.join('Analysis', 'PyPoll_analysis.txt')
sys.stdout = open(text_path, "w")

# print election results and total votes
print("Election Results")
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')

# create for loop to calculate percentage of votes per candidate
for candidate in candidates:
    for vote in votes:
        if candidate == vote:
            vote_count += 1
    percentage = vote_count / len(votes)
    percent_vote.append(percentage)
    candidate_count.append(vote_count)

    if last_count < vote_count:
        Winner = candidate
    print(f'{candidate}: {percentage:.3%} ({vote_count})')
    last_count = vote_count
    vote_count = 0

print('-------------------------')
print(f'Winner: {Winner}')
print('-------------------------')

sys.stdout.close()
sys.stdout=stdoutOrigin
