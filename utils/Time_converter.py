def convert_days(today, time_str):
    # 获得该月第一天对应星期几
    weekdays = {'周日': '0', '周一': '1', '周二': '2', '周三': '3', '周四': '4', '周五': '5', '周六': '6'}
    today = int(today)
    days_difference = today - 1
    today_weekday = int(weekdays[time_str[3]])
    while days_difference > 7:
        days_difference -= 7
    days_difference = today_weekday + 7 - days_difference
    days_difference %= 7

    begin_weekday = days_difference
    # begin_weekday是一个整数属于0-6
    return begin_weekday