swim_time = int(input("What was your swimming time in minutes?\n"))
cycle_time = int(input("What was your cycling time in minutes?\n"))
run_time = int(input("What was your running time in minutes?\n"))

total_time = swim_time + cycle_time + run_time
print(f"Your total time was {total_time} minutes.")

if total_time < 100:
    print("Your award is the Provincial Colours")
elif total_time < 105:
    print("Your award is the Provincial Half Colours")
elif total_time < 110:
    print("Your award is the Provincial Scroll")
else:
    print("Valiant effort but No Award")