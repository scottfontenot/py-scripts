# Return the day of the week it will be on birthday_day, given that the day of
# the week is current_weekday and the day of the year is current_day.

# current_weekday is the current day of the week and is in the range 1-7
# (Sunday-Saturday). current_day and birthday_day are both in the range 1-365.

# use days_difference to figure out how many days there are between two days.
# use get_weekday to figure out what day of the week it will be given the
# current day of the week and the number of days away.

#  days_diff = days_difference(current_day, birthday_day)
#  return get_weekday(current_weekday, days_diff)
# now put it all together:

def get_birthday_weekday(current_weekday: int, current_day: int,
                         birthday_day: int)->int:
