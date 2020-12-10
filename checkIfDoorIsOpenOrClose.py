#Given n doors and n persons. The doors are numbered 1 to n and persons are given id’s numbered 1 to n. Each door can have only 2 status open and closed. Initially all the doors 
#have status closed. Find the final status of all the doors if a person changes the current status of all the doors, i.e. if status open then change to status closed and vice 
#versa, for which he is authorized. A person with id ‘i’ is authorized to change the status of door numbered ‘j’ if ‘j’ is a multiple of ‘i’.

#Approach:
#Check if count of divisors is odd or even.

def hasEvenNumberOfFactors(n):
  sqrt = math.sqrt(n)
  if sqrt * sqrt == n:
    return False
  return True
  
def printStatusOfDoors(n): 
  
    for i in range(1, n + 1): 
        if (hasEvenNumberOfFactors(i) == True): 
            print("closed", end =" ")  
        else: 
            print("open", end =" ") 
 
