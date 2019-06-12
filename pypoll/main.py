#Dependencies 
import os
import csv

#Creating the pathway for the file to be read through
csv_file = os.path.join('election_data.csv')

# Declaring some variables, out of habit
Votes=0 
Candidates = []
CandidateA=0
CandidateB=0
CandidateC=0
CandidateD=0

# Used to open the file, so it is being read
with open(csv_file,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter =',')

# For loop to read into the file, finding the number of votes,
# and using a If, not in, to collect the names of the candidates
    csvheader=next(csvreader)
    for rows in csvreader:
        Votes=Votes+1
        if rows[2] not in Candidates:
            Candidates.append(rows[2])
        if Candidates[0] == rows[2]:
            CandidateA=CandidateA+1
        elif Candidates[1] == rows[2]:
            CandidateB=CandidateB+1
        elif Candidates[2] == rows[2]:
            CandidateC=CandidateC+1
        elif Candidates[3]==rows[2]:
            CandidateD=CandidateD+1
                
# For Statement to compare which candidate did better than the other
for candidates in Candidates:
    if CandidateA> CandidateB and CandidateC and CandidateD:
        Winner = Candidates[0]
    elif CandidateB > CandidateC and CandidateD:
        Winner = Candidates[1]
    elif CandidateC > CandidateD:
        Winner = Candidates[2]
    else:
        Winner = Candidates[3]

# Calculating the Percent Shares
CandidateA_PercentShare = CandidateA/Votes
CandidateB_PercentShare = CandidateB/Votes
CandidateC_PercentShare = CandidateC/Votes
CandidateD_PercentShare = CandidateD/Votes


# Printing the Results
print('Election Results')
print('-----------------------')
print(f'Total Votes: {Votes}')
print('-----------------------')
print(f'{Candidates[0]}: {CandidateA_PercentShare *100}% ({CandidateA})')
print(f'{Candidates[1]}: {CandidateB_PercentShare *100}% ({CandidateB})')
print(f'{Candidates[2]}: {CandidateC_PercentShare *100}% ({CandidateC})')
print(f'{Candidates[3]}: {CandidateD_PercentShare *100}% ({CandidateD})')
print('-----------------------')
print(f'Winner: {Winner}')
print('-----------------------')