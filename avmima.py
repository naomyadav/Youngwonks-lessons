
temperatures = [[23, 29, 26], [32, 37, 34.5], [33, 37, 35], [30, 39, 34.5], [28, 37, 32.5]]

min_temp = [ temperatures[i][0] for i in range(len(temperatures))]
max_temp = [ temperatures[i][1] for i in range(len(temperatures))]
avg_temp = [ temperatures[i][2] for i in range(len(temperatures))]

avg_min_temp = sum(min_temp)/len(min_temp)
avg_max_temp = sum(max_temp)/len(max_temp)
avg_avg_temp = sum(avg_temp)/len(avg_temp)
print("Avg Min:",avg_min_temp,"Avg Max:",avg_max_temp,"Avg Avg:",avg_avg_temp)
