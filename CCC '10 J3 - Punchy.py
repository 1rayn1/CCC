'''
1 defines a variable
2 prints it out
3 adds the two and stores it in the first variable mentioned
4 multiplies the two and stores it in the first variable mentioned
5 subtracts the two and stores it in the first variable mentioned
6 divides the two and stores it in the first variable mentioned
7 ends the program
'''

variables = {"A": 0, "B": 0}

while True:
    choice = input().split()
    key = choice[0]
    
    if key == "7":
        break

    elif key == "1":
        variables[choice[1]] = int(choice[2])
        
    elif key == "2":
        print(variables[choice[1]])
        
    elif key == "3":
        variables[choice[1]] += variables[choice[2]]
        
    elif key == "4":
        variables[choice[1]] *= variables[choice[2]]
        
    elif key == "5":
        variables[choice[1]] -= variables[choice[2]]
        
    elif key == "6":
        variables[choice[1]] //= variables[choice[2]]