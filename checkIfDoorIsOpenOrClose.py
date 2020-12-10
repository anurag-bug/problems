#Given n doors and n persons. The doors are numbered 1 to n and persons are given id’s numbered 1 to n. Each door can have only 2 status open and closed. Initially all the doors 
#have status closed. Find the final status of all the doors if a person changes the current status of all the doors, i.e. if status open then change to status closed and vice 
#versa, for which he is authorized. A person with id ‘i’ is authorized to change the status of door numbered ‘j’ if ‘j’ is a multiple of ‘i’.

#Approach:
#Check if count of divisors is odd or even.

def hasEvenNumberOfFactors(n):
  #Factors appear in pairs but in case of perfect squares they are odd. Ex
  #5 = 1,5
  #4 = 1,2,4
  #25 = 1,5,25
  #36 = 1,2,3,4,6,9,12,18,36
  #12 = 1,2,3,4,6,12
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
 
