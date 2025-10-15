rows =5
for i in range(1,rows+1): # outer loop controles the rows
    for j in range(1,i+1):# inner loop prints the stars in each row
        print("*", end="") # print star follwed by the space ,stays on same line
    print() # after the inner loop is finished it prints a new line


    # when i =1 the inner loop prints once one start
    # i=2 inner loop runs twice and prints 2 start


