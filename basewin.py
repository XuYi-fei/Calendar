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
## Class baseMainWindow
###########################################################################

class baseMainWindow(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"万年历_version1", pos=wx.DefaultPosition,
                          size=wx.Size(879, 514), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOTEXT))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer3 = wx.FlexGridSizer(5, 1, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.title = wx.StaticText(self, wx.ID_ANY, u"万年历\n（1970-2099）", wx.Point(-1, -1), wx.DefaultSize,
                                   wx.ALIGN_CENTRE)
        self.title.Wrap(-1)
        self.title.SetFont(wx.Font(23, 70, 90, 90, False, wx.EmptyString))

        fgSizer3.Add(self.title, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.HORIZONTAL)

        self.text_year = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(-1, -1), 0)
        sbSizer1.Add(self.text_year, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText54 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"年", wx.DefaultPosition,
                                            wx.Size(-1, -1), 0)
        self.m_staticText54.Wrap(-1)
        self.m_staticText54.SetFont(wx.Font(20, 70, 93, 90, False, wx.EmptyString))

        sbSizer1.Add(self.m_staticText54, 1, wx.ALL, 5)

        self.text_month = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.Size(-1, -1), 0)
        sbSizer1.Add(self.text_month, 1, wx.ALL, 5)

        self.m_staticText56 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"月", wx.DefaultPosition,
                                            wx.Size(-1, -1), 0)
        self.m_staticText56.Wrap(-1)
        self.m_staticText56.SetFont(wx.Font(20, 70, 93, 90, False, wx.EmptyString))

        sbSizer1.Add(self.m_staticText56, 1, wx.ALL, 5)

        self.text_day = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.Size(-1, -1), 0)
        sbSizer1.Add(self.text_day, 1, wx.ALL, 5)

        self.m_staticText57 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"日", wx.DefaultPosition,
                                            wx.Size(-1, -1), 0)
        self.m_staticText57.Wrap(-1)
        self.m_staticText57.SetFont(wx.Font(20, 70, 93, 90, False, wx.EmptyString))

        sbSizer1.Add(self.m_staticText57, 1, wx.ALL, 5)

        fgSizer3.Add(sbSizer1, 1, wx.EXPAND, 5)

        self.button1 = wx.Button(self, wx.ID_ANY, u"查询", wx.Point(1000, 1000), wx.Size(-1, -1), 0)
        self.button1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer3.Add(self.button1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"label"), wx.HORIZONTAL)

        self.weekday_0 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"周日", wx.DefaultPosition, wx.DefaultSize, 0)
        self.weekday_0.Wrap(-1)
        sbSizer2.Add(self.weekday_0, 1, wx.ALL, 5)

        self.weekday_1 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"周一", wx.DefaultPosition, wx.DefaultSize, 0)
        self.weekday_1.Wrap(-1)
        sbSizer2.Add(self.weekday_1, 1, wx.ALL, 5)

        self.weekday_2 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"周二", wx.DefaultPosition, wx.DefaultSize, 0)
        self.weekday_2.Wrap(-1)
        sbSizer2.Add(self.weekday_2, 1, wx.ALL, 5)

        self.weekday_3 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"周三", wx.DefaultPosition, wx.DefaultSize, 0)
        self.weekday_3.Wrap(-1)
        sbSizer2.Add(self.weekday_3, 1, wx.ALL, 5)

        self.weekday_4 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"周四", wx.DefaultPosition, wx.DefaultSize, 0)
        self.weekday_4.Wrap(-1)
        sbSizer2.Add(self.weekday_4, 1, wx.ALL, 5)

        self.weekday_5 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"周五", wx.DefaultPosition, wx.DefaultSize, 0)
        self.weekday_5.Wrap(-1)
        sbSizer2.Add(self.weekday_5, 1, wx.ALL, 5)

        self.weekday_6 = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"周六", wx.DefaultPosition, wx.DefaultSize, 0)
        self.weekday_6.Wrap(-1)
        sbSizer2.Add(self.weekday_6, 1, wx.ALL, 5)

        fgSizer3.Add(sbSizer2, 1, wx.EXPAND, 5)

        gSizer1 = wx.GridSizer(7, 7, 0, 0)

        gSizer1.SetMinSize(wx.Size(1200, 500))
        self.days_1 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_1.Wrap(-1)
        gSizer1.Add(self.days_1, 0, wx.ALL, 5)

        self.days_2 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_2.Wrap(-1)
        gSizer1.Add(self.days_2, 0, wx.ALL, 5)

        self.days_3 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_3.Wrap(-1)
        gSizer1.Add(self.days_3, 0, wx.ALL, 5)

        self.days_4 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_4.Wrap(-1)
        gSizer1.Add(self.days_4, 0, wx.ALL, 5)

        self.days_5 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_5.Wrap(-1)
        gSizer1.Add(self.days_5, 0, wx.ALL, 5)

        self.days_6 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_6.Wrap(-1)
        gSizer1.Add(self.days_6, 0, wx.ALL, 5)

        self.days_7 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_7.Wrap(-1)
        gSizer1.Add(self.days_7, 0, wx.ALL, 5)

        self.days_8 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_8.Wrap(-1)
        gSizer1.Add(self.days_8, 0, wx.ALL, 5)

        self.days_9 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_9.Wrap(-1)
        gSizer1.Add(self.days_9, 0, wx.ALL, 5)

        self.days_10 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_10.Wrap(-1)
        gSizer1.Add(self.days_10, 0, wx.ALL, 5)

        self.days_11 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_11.Wrap(-1)
        gSizer1.Add(self.days_11, 0, wx.ALL, 5)

        self.days_12 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_12.Wrap(-1)
        gSizer1.Add(self.days_12, 0, wx.ALL, 5)

        self.days_13 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_13.Wrap(-1)
        gSizer1.Add(self.days_13, 0, wx.ALL, 5)

        self.days_14 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_14.Wrap(-1)
        gSizer1.Add(self.days_14, 0, wx.ALL, 5)

        self.days_15 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_15.Wrap(-1)
        gSizer1.Add(self.days_15, 0, wx.ALL, 5)

        self.days_16 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_16.Wrap(-1)
        gSizer1.Add(self.days_16, 0, wx.ALL, 5)

        self.days_17 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_17.Wrap(-1)
        gSizer1.Add(self.days_17, 0, wx.ALL, 5)

        self.days_19 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_19.Wrap(-1)
        gSizer1.Add(self.days_19, 0, wx.ALL, 5)

        self.days_18 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_18.Wrap(-1)
        gSizer1.Add(self.days_18, 0, wx.ALL, 5)

        self.days_20 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_20.Wrap(-1)
        gSizer1.Add(self.days_20, 0, wx.ALL, 5)

        self.days_21 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_21.Wrap(-1)
        gSizer1.Add(self.days_21, 0, wx.ALL, 5)

        self.days_22 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_22.Wrap(-1)
        gSizer1.Add(self.days_22, 0, wx.ALL, 5)

        self.days_23 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_23.Wrap(-1)
        gSizer1.Add(self.days_23, 0, wx.ALL, 5)

        self.days_24 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_24.Wrap(-1)
        gSizer1.Add(self.days_24, 0, wx.ALL, 5)

        self.days_25 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_25.Wrap(-1)
        gSizer1.Add(self.days_25, 0, wx.ALL, 5)

        self.days_26 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_26.Wrap(-1)
        gSizer1.Add(self.days_26, 0, wx.ALL, 5)

        self.days_27 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_27.Wrap(-1)
        gSizer1.Add(self.days_27, 0, wx.ALL, 5)

        self.days_28 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_28.Wrap(-1)
        gSizer1.Add(self.days_28, 0, wx.ALL, 5)

        self.days_29 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_29.Wrap(-1)
        gSizer1.Add(self.days_29, 0, wx.ALL, 5)

        self.days_30 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_30.Wrap(-1)
        gSizer1.Add(self.days_30, 0, wx.ALL, 5)

        self.days_31 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_31.Wrap(-1)
        gSizer1.Add(self.days_31, 0, wx.ALL, 5)

        self.days_32 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_32.Wrap(-1)
        gSizer1.Add(self.days_32, 0, wx.ALL, 5)

        self.days_33 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_33.Wrap(-1)
        gSizer1.Add(self.days_33, 0, wx.ALL, 5)

        self.days_34 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_34.Wrap(-1)
        gSizer1.Add(self.days_34, 0, wx.ALL, 5)

        self.days_35 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_35.Wrap(-1)
        gSizer1.Add(self.days_35, 0, wx.ALL, 5)

        self.days_36 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_36.Wrap(-1)
        gSizer1.Add(self.days_36, 0, wx.ALL, 5)

        self.days_37 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_37.Wrap(-1)
        gSizer1.Add(self.days_37, 0, wx.ALL, 5)

        self.days_38 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_38.Wrap(-1)
        gSizer1.Add(self.days_38, 0, wx.ALL, 5)

        self.days_39 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_39.Wrap(-1)
        gSizer1.Add(self.days_39, 0, wx.ALL, 5)

        self.days_40 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_40.Wrap(-1)
        gSizer1.Add(self.days_40, 0, wx.ALL, 5)

        self.days_41 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_41.Wrap(-1)
        gSizer1.Add(self.days_41, 0, wx.ALL, 5)

        self.days_42 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.days_42.Wrap(-1)
        gSizer1.Add(self.days_42, 0, wx.ALL, 5)

        fgSizer3.Add(gSizer1, 0, wx.EXPAND, 5)

        self.SetSizer(fgSizer3)
        self.Layout()
        self.menubar1 = wx.MenuBar(0)
        self.menu_menu = wx.Menu()
        self.menuItem_info = wx.MenuItem(self.menu_menu, wx.ID_ANY, u"说明", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_menu.Append(self.menuItem_info)

        self.menu_updateinfo = wx.MenuItem(self.menu_menu, wx.ID_ANY, u"更新说明", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_menu.Append(self.menu_updateinfo)

        self.menubar1.Append(self.menu_menu, u"菜单")

        self.SetMenuBar(self.menubar1)

        self.statusBar1 = self.CreateStatusBar(1, 0, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.button1.Bind(wx.EVT_BUTTON, self.main_button_click)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def main_button_click(self, event):
        event.Skip()


