
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
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        votes.append(row[2])
        
total_votes = len(votes)

for name in votes:
   if name not in candidates:
        candidates.append(name)
        x = name

# Candidate
candidate = votes[0]
# Counter (count)
vote_count = 0
# Set last count
last_count = 0

# print(f'Candidates: {candidates}')
# print("Election Results")
# print('-------------------------')
# print(f"Total Votes: {total_votes}")
# print('-------------------------')

for candidate in candidates:
    for vote in votes:
        if candidate == vote:
            vote_count += 1
    percentage = vote_count / len(votes)
    percent_vote.append(percentage)
    candidate_count.append(vote_count)

    if last_count < vote_count:
        Winner = candidate
    # print(f"{candidate}: {percentage:.3%} ({vote_count})")
    # reset vote count to zero
    last_count = vote_count
    vote_count = 0

Winner = candidate

# print(f'Candidates: {candidates}')
print("Election Results")
print('-------------------------')
print(f"Total Votes: {total_votes}")
print('-------------------------')
# for candidate in candidates:
#     index = candidates.index(candidate)
#     print(f'{candidate} : {percent_vote}% ({vote_count})')
for candidate in candidates:
    index = candidates.index(candidate)
    print(f'{candidate} : {percent_vote}% ({vote_count})')
# for candidate in candidates:
#     index = candidates.index(candidate)
print('-------------------------')
# print(f"{candidates}: {percent_vote:.3%} ({vote_count})")
print(f"Winner: {Winner}")
print('-------------------------')

stdoutOrigin=sys.stdout 
text_path = os.path.join('Analysis', 'PyBank_analysis.txt')
sys.stdout = open(text_path, "w")

print("Election Results")
print('-------------------------')
print(f"Total Votes: {total_votes}")
print('-------------------------')
for candidate in candidates:
    index = candidates.index(candidates)
    print(f"{candidates}: {percent_vote[index]:.3%} ({vote_count[index]})")
print(f"Winner: {last_count}")
print('-------------------------')

sys.stdout.close()
sys.stdout=stdoutOrigin
