# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class window_update_info
###########################################################################

class window_update_info(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"更新说明", pos=wx.DefaultPosition, size=wx.Size(610, 446),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(15, 70, 90, 90, False, "宋体"))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        gSizer3 = wx.GridSizer(0, 1, 0, 0)

        self.m_staticText58 = wx.StaticText(self, wx.ID_ANY, u"此次更新优化了：\n1.缩放窗口的不一致问题\n2.年份的限定提示\n3.查询的日期当天会用下划线以及粗体标注",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText58.Wrap(-1)
        self.m_staticText58.SetFont(wx.Font(16, 70, 90, 92, False, "宋体"))
        self.m_staticText58.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.m_staticText58.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        gSizer3.Add(self.m_staticText58, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(gSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


