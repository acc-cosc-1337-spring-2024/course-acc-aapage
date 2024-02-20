import value_return as vr

# define variables
hour = vr.get_hour(3800)
minutes = vr.get_minutes(3800)
seconds = vr.get_seconds(3800)

# leading 0's
if hour < 10:
    hour = f'0{hour}'
if minutes < 10:
    minutes = f'0{minutes}'
if seconds < 10:
    seconds = f'0{seconds}'

# final output construction
time = f'{hour}:{minutes}:{seconds}'

# output
print(time)