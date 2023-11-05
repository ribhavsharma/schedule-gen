

day=[hour for hour in range(0,24)] #hours in a day
unavailableTimes=[]
numActivities=int(input("Enter the number of activities you have today: "))
for i in range(0,numActivities):
    start=int(input("Enter the start time of the activity: "))
    end=int(input("Enter the end time of the activity: "))
    unavailableTimes.append((start,end))
availableTimes=day.copy()

conflicts = [] #list of hours with conflicts
for start,end in unavailableTimes:
    for hour in range(start,end):
        if hour in availableTimes:
            if hour not in conflicts:
                conflicts.append(hour) #add hour to conflicts
            availableTimes.remove(hour) #remove hour from availableTimes as the user is not free

if conflicts:
    print("You have conflicts at the following times:")
    for hour in conflicts:
        print(f"{hour}:00 - {hour+1}:00")
else:
    print("You have no conflicts.") #list of conflicts and available times are printed. 

print("Your free times are:")
for hour in availableTimes:
    print(f"{hour}:00 - {hour+1}:00")