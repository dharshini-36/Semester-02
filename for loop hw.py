
for d in range(0,32,4):  
    print(f"{d}",end=" ")

    
row=int(input())
col=int(input())
for x in range(row):
    for y in range(col):
        print("@",end="  ")
    print()
           
scores = [85, 90, -5, 76, 92, -1, 88, 79, 55]
for score in scores:
    if score == -1:
        print("Encountered missing data. Stopping processing.")
        break
    elif score < 0:
        print(f"Invalid score {score} encountered. Skipping.")
        continue
    else:
        print("Score:", score)


