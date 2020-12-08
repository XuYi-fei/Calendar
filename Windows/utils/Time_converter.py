import time,wx
from .Errors.Error_date_error import error_date
import calendar
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

def deal_times(self):
    month_dict = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30,'12': 31,
             '01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30}
    date = get_date(self)

    month_date = calendar.timegm(date)
    t = time.strftime("%Y-%m-%d-%a-%H-%M-%S", time.localtime(month_date))
    # 获取时间并且打印在static_text上
    # 首先重新设置字体
    mark = "self.days_"
    for i in range(1,43):
        eval(mark+str(i)).SetLabel(" ")
        eval(mark+str(i)).SetFont(wx.Font( 20, 70, 93, 90, False, "宋体" ))
    time_str = t.split('-')
    year, month, today, weekday, hour, minute, sec = time_str[0],time_str[1],time_str[2],time_str[3],time_str[4],time_str[5],time_str[6]
    days = month_dict[month]
    mark = 'self.days_'

    begin_weekday = convert_days(today,time_str)
    #注意begin_weekday是0-6而月份上的30多个日期是1-42
    today_number = int(today.lstrip('0'))
    # 打印开始,对于查询的日子换一个字体用来标注
    for i in range(1,days+1):
        mark_day = mark+str(i+begin_weekday)
        eval(mark_day).SetLabel(str(i))
        if i == today_number:
            eval(mark_day).SetFont(wx.Font( 20, 70, 93, 92, True, "宋体" ))

    self.combo_box_year.SetValue(year)
    self.combo_box_month.SetValue(month)
    self.combo_box_day.SetValue(today)
    return

def get_date(self):
    month_dict = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30,
                  '12': 31,
                  '01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30}
    text_year_Value = self.combo_box_year.Value.lstrip('0')
    text_month_Value = self.combo_box_month.Value.lstrip('0')
    text_day_Value = self.combo_box_day.Value.lstrip('0')

    text_availabel = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    flag = False
    if len(text_year_Value) * len(text_month_Value) * len(text_day_Value) == 0:
        flag = True

    for i in [text_year_Value, text_day_Value, text_month_Value]:
        for j in i:
            if j not in text_availabel:
                flag = True

    if not flag:
        year, month, day = eval(text_year_Value), eval(text_month_Value), eval(text_day_Value)
        if year <= 1969 or year >= 2099 or month <= 0 or month > 12:
            flag = True
        month_str = str(month)
        if not flag:
            if day <= 0 or day > month_dict[month_str]:
                flag = True

    if flag:
        # 处理输入错误
        year, month, day = error_date(self)
        self.OnCloseMe()

    date = (year, month, day, 0, 0, 0)


    return date