import csv
import os
import wx
def get_csv(self):
    if not os.path.exists("festivals.csv"):
        # app = wx.App
        csv_error = wx.MessageDialog(None, u"  节日列表拉取失败  \n是否创建 list.csv 新文件?", u" 创建文件",
                                     wx.YES | wx.NO |wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL)
        csv_error.Show()
        t = csv_error.ShowModal()
        if t == wx.ID_NO:
            csv_error.Destroy()
        elif t == wx.ID_YES:
            with open("list.csv",'a') as f:
                f.close()
            csv_error.Destroy()
    return


def rear_csv():
    return



def write_csv():
    return