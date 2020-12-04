# -*- coding: utf-8 -*-
import wx
import basewin
from window_info import *
from window_update_info import *
import calendar
import time
# 首先，咱们从刚刚源文件中将主窗体继承下来.就是修改过name属性的主窗体咯。
class MainWindow(basewin.baseMainWindow):
    # 咱们给个初始化函数，将文本框初始填有‘主窗口测试’几个字
    # 不能直接覆盖原有__ini__方法，这样会导致窗体启动失败。咱们新建一个，然后再调用
    def init_main_window(self):
        #初始化一些参数
        self.weekdays = {'周日':'0','周一':'1','周二':'2','周三':'3','周四':'4','周五':'5','周六':'6'}
        self.weekdays_convert = {k:i for i,k in self.weekdays.items()}
        self.days = list(range(1,43))
        self.month = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31,
                      '01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30}
        self.days = [str(i) for i in self.days]
        #第一次初始化，以防无效输入
        t = time.localtime()
        t = time.strftime("%Y-%m-%d-%a-%H-%M-%S", t)
        time_str = t.split('-')
        self.today_year, self.today_month, self.today = time_str[0],time_str[1],time_str[2]
        self.deal_times(t)
        self.bind_menu_items()


    def bind_menu_items(self):
        self.Bind(wx.EVT_MENU, self.bind_menu_info, self.menuItem_info)
        self.Bind(wx.EVT_MENU, self.bind_menu_update_info,self.menu_updateinfo)
        # self.menuItem_info.
        return

    def bind_menu_info(self,event):
        app = wx.App()
        window_Infomation = window_info(None)
        window_Infomation.Show()
        # main_win.Show()
        app.MainLoop()
        return

    def bind_menu_update_info(self,event):
        app = wx.App()
        window_update = window_update_info(None)
        window_update.Show()
        app.MainLoop()
        return



    def main_button_click(self, event):
        # print(self.text_year.Value,self.text_month.Value,self.text_day.Value)
        text_year_Value = self.text_year.Value.lstrip('0')
        text_month_Value = self.text_month.Value.lstrip('0')
        text_day_Value = self.text_day.Value.lstrip('0')

        year = eval(text_year_Value)
        if not isinstance(year,int) or year <= 1969 or year >= 2099:
            print("year error")
            self.text_year.SetValue(self.today_year)
            text_year_Value = self.today_year
            try:
                year = eval(text_year_Value)
            except:
                year = eval(text_year_Value.lstrip('0'))

        month = eval(text_month_Value)
        if not isinstance(month, int) or month <= 0 or month > 12:
            print("month error")
            self.text_month.SetValue(self.today_month)
            text_month_Value = self.today_month
            try:
                month = eval(text_month_Value)
            except:
                month = eval(text_month_Value.lstrip('0'))

        month_str = str(month)
        day = eval(text_day_Value)
        if not isinstance(day, int) or day <= 0 or day > self.month[month_str]:
            print("day error")
            self.text_day.SetValue(self.today)
            text_day_Value =self.today
            try:
                day = eval(text_day_Value)
            except:
                day = eval(text_year_Value.lstrip('0'))

        date = (year, month,day,0,0,0)
        # print(date)
        month_date = calendar.timegm(date)

        t = time.strftime("%Y-%m-%d-%a-%H-%M-%S",time.localtime(month_date))

        self.deal_times(t)
        return
        # self.text_main.Clear()
        # self.days_5.SetLabel("asdaasd")
        # self.OnTimer(event)

    def deal_times(self,t):
        # 获取时间并且打印在static_text上
        # print
        mark = "self.days_"
        for i in range(1,43):
            eval(mark+str(i)).SetLabel(" ")
            eval(mark+str(i)).SetFont(wx.Font( 20, 70, 93, 90, False, "宋体" ))
        time_str = t.split('-')
        year, month, today, weekday, hour, minute, sec = time_str[0],time_str[1],time_str[2],time_str[3],time_str[4],time_str[5],time_str[6]
        days = self.month[month]
        mark = 'self.days_'

        begin_weekday = self.convert_days(today,time_str)
        #注意begin_weekday是0-6而月份上的30多个日期是1-42
        self.text_year.SetValue(year)
        self.text_month.SetValue(month)
        self.text_day.SetValue(today)
        today = int(today.lstrip('0'))
        for i in range(1,days+1):
            mark_day = mark+str(i+begin_weekday)
            eval(mark_day).SetLabel(str(i))
            if i == today:
                eval(mark_day).SetFont(wx.Font( 20, 70, 93, 92, True, "宋体" ))


    def convert_days(self,today,time_str):
        # 获得该月第一天对应星期几
        today = int(today)
        days_difference = today - 1
        today_weekday = int(self.weekdays[time_str[3]])
        while days_difference > 7 :
            days_difference -= 7
        days_difference = today_weekday + 7 -days_difference
        days_difference %= 7

        begin_weekday = days_difference
        #begin_weekday是一个整数属于0-6
        return begin_weekday


    def Draw(self, dc):  # 绘制当前时间
        t = time.localtime(time.time())
        st = time.strftime("%I:%M:%S", t)
        w, h = self.GetClientSize()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
        tw, th = dc.GetTextExtent(st)
        print(w,h,tw,th)
        dc.DrawText(st, (w - tw) / 2, (h) / 2 - th / 2)

    def OnTimer(self, evt):  # 显示时间事件处理函数
        dc = wx.BufferedDC(wx.ClientDC(self))
        self.Draw(dc)

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        self.Draw(dc)

if __name__ == '__main__':
    app = wx.App()
    # None表示的是此窗口没有上级父窗体。如果有，就直接在父窗体代码调用的时候填入‘self’就好了。
    main_win = MainWindow(None)
    main_win.init_main_window()
    main_win.Show()
    app.MainLoop()