'''
Question 4
A company is looking at automating one of their internal processes and wants to determine if automating a process would save labor time this year. The company uses the formula [time_to_automate < (time_to_perform * amount_of_times_done)] to decide whether automation is worthwhile. The process normally takes about 10 minutes every week. The automation process itself will take 40 hours total to complete. Using the formula, how many weeks will it be before the company starts saving time on the process?

'''


def calculation(x,y):
    time_to_automate = x*60
    time_to_perform = y

    amount_of_times_done = time_to_automate / time_to_perform

    #rem that the amount of times done is basically if its done in once a day then that amount wil be counted in days and for ex here it is weeks then the amount will be in weeks

    print(f"The amount of weeks it will take will be: {amount_of_times_done:.0f}")

calculation(40, 10)
calculation(12, 50)
