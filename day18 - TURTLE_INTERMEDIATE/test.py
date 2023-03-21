hours = int(input('how many hours did you work? '))
rate = int(input('what is your hourly rate? '))

if hours >= 40:
  overtimeRate = 2.0 * rate
  overtime = (hours-40) * overtimeRate
  hours = 40
else:
  overtime = 0

print("you earn", (hours + max(hours - 40, 0) * 0.5) * rate)