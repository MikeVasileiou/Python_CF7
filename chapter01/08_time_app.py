# constants

SECONDS_IN_A_MINUTE = 60
SECONDS_IN_A_HOUR = 3600
SECONDS_IN_A_DAY = 86400


#prompt

total_seconds = int(input("Enter the number of seconds: "))

#calculations

# / returns float, // return int
days = total_seconds // SECONDS_IN_A_DAY
seconds_remaining = total_seconds % SECONDS_IN_A_DAY

hours = seconds_remaining // SECONDS_IN_A_HOUR
seconds_remaining %=SECONDS_IN_A_HOUR

minutes = seconds_remaining // SECONDS_IN_A_MINUTE
seconds_remaining %=SECONDS_IN_A_MINUTE

seconds = seconds_remaining

print(f"{total_seconds} senconds is equal to :")
print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")