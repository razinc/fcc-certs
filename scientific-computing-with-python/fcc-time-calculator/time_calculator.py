from datetime import datetime, timedelta
def add_time(start, duration, start_day = False):

    # convert start to 24 hours system
    if "12:" and "AM" in start:
        start = start.replace("12:", "00:").replace(" AM", "")
    elif "AM" in start:
        start = start.replace(" AM", "")
    elif "PM" in start:
        start = start.strip(" PM")
        start = str(int(start.split(":")[0]) + 12) + ":" + start.split(":")[1]

    # convert args to timestamp
    start = datetime.strptime(start, "%H:%M")

    # convert duration to individual hours and minutes
    add_hrs, add_min = duration.split(":")
    if add_hrs == "00":
        add_hrs = 0
    else:
        add_hrs = int(add_hrs)
    if add_min == "00":
        add_min = 0
    else:
        add_min = int(add_min.lstrip("0"))

    # add start with duration
    new_time = start + timedelta(hours = add_hrs)
    new_time = new_time + timedelta(minutes = add_min)

    # calculate day difference
    start_date = start.date()
    end_date = new_time.date()
    days = (end_date - start_date).days
    if days == 0:
        days_diff = ""
    elif days == 1:
        days_diff = " (next day)"
    else:
        days_diff = f" ({days} days later)"

    # if start_day is passed to def
    days_in_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if start_day is False:
        end_day = ""
    else:
        # format days
        start_day = start_day.lower().title()

        # calculate end day
        if days_diff == "":
            end_day = f", {start_day}"
        elif days_diff != "":
            start_day_i = days_in_week.index(start_day)
            end_day_i = start_day_i + days

            # doesn't have to loop days_in_week
            if end_day_i < len(days_in_week):
                end_day = days_in_week[end_day_i]
            # does have to loop days_in_week
            else:
                no_of_weeks = int(end_day_i / len(days_in_week))
                no_of_days = len(days_in_week) * no_of_weeks
                end_day_i = end_day_i - no_of_days
                end_day = days_in_week[end_day_i]
            end_day = f", {end_day}"

    # convert new_time to 12 hours system
    new_time = str(new_time.time())
    hours, minutes, seconds = new_time.split(":")
    if hours == "00":
        hours = 12
        am_or_pm = "AM"
    elif hours == "12":
        am_or_pm = "PM"
    elif int(hours) > 12:
        hours = int(hours) - 12
        am_or_pm = "PM"
    elif int(hours) < 13:
        hours = hours.lstrip("0")
        am_or_pm = "AM"
    new_time = f"{hours}:{minutes} {am_or_pm}{end_day}{days_diff}".strip()

    return new_time