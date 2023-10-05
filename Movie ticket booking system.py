# Counting the number of unreserved seats in a movie theatre
# Let us assume the reserved seats are displayed by 1 and unreserved by 0

string=input().split()
n,m=int(string[0]),int(string[1])

# Initializing all seats of theatre with 0
seats=[[0 for j in range(m)] for i in range(n)]

# Reserving the seats randomly
for i in range(n):
    for j in range(m):
        print("Enter the number 0/1: ")
        reserve=int(input())
        if reserve==1:
            seats[i][j]=1
        elif reserve==0:
            continue
        else:
            break

# Counting the number of unreserved seats
count=0
for i in range(n):
    for j in range(m):
        if seats[i][j]==0:
            count=count+1

# Printing the theatre outline
for i in range(n):
    for j in range(m):
        print(seats[i][j],end=" ")
    print()

# Finally depicting number of unreserved seats
print("The number of unreserved seats are {}".format(count))

