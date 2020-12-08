# -*- coding: utf-8 -*-
from . import basewin
import csv
from Windows.window_info import *
from Windows.window_update_info import *
from Windows.Binds import *
from Windows.utils import *
from Windows.External_libs import *

import time
# 首先，咱们从刚刚源文件中将主窗体继承下来.就是修改过name属性的主窗体咯。
class MainWindow(basewin.baseMainWindow):
    # 咱们给个初始化函数，将文本框初始填有‘主窗口测试’几个字
    # 不能直接覆盖原有__ini__方法，这样会导致窗体启动失败。咱们新建一个，然后再调用
    def init_main_window(self):
        #初始化一些参数
        self.days = list(range(1,43))
        self.days = [str(i) for i in self.days]
        #第一次初始化，以防无效输入
        t = time.localtime()
        t = time.strftime("%Y-%m-%d-%a-%H-%M-%S", t)
        time_str = t.split('-')
        bind_menus(self)
        bind_combos(self)
        bind_buttons(self)
        self.today_year, self.today_month, self.today = time_str[0],time_str[1],time_str[2]
        self.combo_box_year.SetValue(self.today_year)
        self.combo_box_month.SetValue(self.today_month)
        self.combo_box_day.SetValue(self.today)
        self.status_main.SetStatusText("程序正常运行中")

        deal_times(self)

    def bind_combo_box_time(self,event):
        deal_times(self)
        return

    def bind_menu_info(self,event):
        app = wx.App()
        window_Infomation = window_info(None)
        window_Infomation.Show()
        app.MainLoop()
        return

    def bind_menu_exit(self,event):
        self.Close()
        return

    def bind_menu_update_info(self,event):
        app = wx.App()
        window_update = window_update_info(None)
        window_update.Show()
        app.MainLoop()
        return

    def main_button_click(self, event):
        deal_times(self)

        return

    def set_text(self, event):
        day = int(event.EventObject.Label)
        date = get_date(self)
        get_csv(self)
        return

    def OnCloseMe(self):
        dlg = wx.MessageDialog(None, u"输入日期有误或超出范围", u"报错消息", wx.OK)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
        dlg.Destroy()
        return

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
