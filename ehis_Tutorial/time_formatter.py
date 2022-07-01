def time_formatter(time: str):
    new_time = time.split(":")
    hour = int(new_time[0])
    minute = new_time[1]
    seconds = new_time[2]
    sec = seconds[:2]
    meridian = seconds[-2:]

    check_am = 'am' or 'AM'
    check_pm = 'pm' or 'PM'

    if(meridian == check_am and hour == 12):
        hour = 0
    else:
        if(meridian == check_pm and hour < 12):
            hour += 12
    return str(hour) + ":" + minute + ":" + sec


# time = "01:55:22am"
time = input("Enter time (hh:mm:ss): ")
print(time_formatter(time))
