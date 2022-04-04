def add_time(start, add, day=None):
    days_later = 0
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    clock_format = start.split(" ")[1]

    # convert start to minutes from 00:00
    if clock_format == "PM":
        # 12:00 PM = 12:00
        if start.split(" ")[0].split(":")[0] == "12":
            start = int(start.split(" ")[0].split(":")[0]) * 60 + int(start.split(" ")[0].split(":")[1])

        else:
            # hours * 60 minutes + 12 hours * 60 minutes + minutes
            start = int(start.split(" ")[0].split(":")[0]) * 60 + 12 * 60 + int(start.split(" ")[0].split(":")[1])
    else:

        if start.split(" ")[0].split(":")[0] == "12":
            # 12:00 AM = 00:00
            start = int(start.split(" ")[0].split(":")[0]) * 60 - 12 * 60 + int(start.split(" ")[0].split(":")[1])
        else:
            # hours * 60 minutes + minutes
            start = int(start.split(" ")[0].split(":")[0]) * 60 + int(start.split(" ")[0].split(":")[1])

    # convert add to minutes
    add = int(add.split(":")[0]) * 60 + int(add.split(":")[1])

    finish = start + add

    while finish > 24 * 60:
        days_later = days_later + 1
        finish = finish - (24 * 60)

    if finish <= 59: # finish from 00:00 to 00:59
        if finish % 60 < 10:
            finish = str(finish // 60 + 12) + ":0" + str(finish % 60) + " AM"
        else:
            finish = str(finish // 60 + 12) + ":" + str(finish % 60) + " AM"

    elif 719 >= finish > 59:  # finish from 1:00 to 11:59
        if finish % 60 < 10:
            finish = str(finish // 60) + ":0" + str(finish % 60) + " AM"
        else:
            finish = str(finish // 60) + ":" + str(finish % 60) + " AM"
    elif 779 >= finish > 719:  # finish from 12:00 to 12:59
        if finish % 60 < 10:
            finish = str(finish // 60) + ":0" + str(finish % 60) + " PM"

        else:
            finish = str(finish // 60) + ":" + str(finish % 60) + " PM"

    else:
        if finish % 60 < 10:
            finish = str(finish // 60 - 12) + ":0" + str(finish % 60) + " PM"
        else:
            finish = str(finish // 60 - 12) + ":" + str(finish % 60) + " PM"

    if day is None:
        if days_later == 0:
            return finish
        elif days_later == 1:
            return finish + " (next day)"
        else:
            return finish + " (" + str(days_later) + " days later)"

    if day is not None:
        day = day.title()
        if days_later == 0:
            return finish + ", " + day
        elif days_later == 1:
            if (days_of_week.index(day) + days_later) % 7 > 6:
                index = (days_of_week.index(day) + days_later) % 7 - 6

            else:
                index = (days_of_week.index(day) + days_later) % 7
            return finish + ", " + days_of_week[index] + " (next day)"
        else:
            if (days_of_week.index(day) + days_later) % 7 > 6:
                index = (days_of_week.index(day) + days_later) % 7 - 6

            else:
                index = (days_of_week.index(day) + days_later) % 7
            return finish + ", " + days_of_week[index] + " (" + str(days_later) + " days later)"