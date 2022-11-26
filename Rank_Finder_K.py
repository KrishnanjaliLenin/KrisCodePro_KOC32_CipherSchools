
# Python3 implementation of the approach
 
# Function to print the name of student who
# stood first after updation in rank
def nameRank(names, marks, updates):
     # Number of students
    n = len(names)

    # Array of students
    x = [[0 for j in range(5)] for i in range(n)]
   
    for i in range(n):
        
        # Store the name of the student
        x[i][0] = names[i]
        
        # Store the marks of the student
        x[i][1]= marks[i]

        # Update the marks of the student
        x[i][2]= marks[i] + updates[i]

    x.sort(key=lambda x:x[1], reverse=True)
    for i in range(n):
        # Store the current rank of the student
        x[i][3] = i + 1
    
    x.sort(key=lambda x:x[2], reverse=True)
    for i in range(n):
        # Store the updated rank of the student
        x[i][4] = i + 1

    print("\nThe details of the student with the highest marks")
    print("Name:",x[0][0], ", Previous mark:",x[0][1], ", Current mark:",x[0][2], ", Previous rank:",x[0][3], ", Current rank:",x[0][4])
    
    # Updated rank list
    print("\nUpdated rank list")
    print(x,"\n")    

    # Print the name, previous and current rank
    for i in range(n):
        print("Name:",x[i][0], ", Previous Rank:",x[i][3], 
              ", Current Rank:",x[i][4], ", Jump in Rank:",x[i][4] - x[i][3],"\n")
 
# Driver code
 
# Names of the students
names= ["Tina", "Hina", "Hiran"]
 
# Marks of the students
marks = [80, 79, 75]
 
# Updates that are to be done
updates = [0, 5, -9]

nameRank(names, marks, updates)