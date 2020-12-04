import wx
# from PIL import Image
# # app = wx.App()  # 创建应用程序对象
# #
# # win = wx.Frame(None, -1, 'install test')  # 创建窗体
# #
# # btn = wx.Button(win, label='Button')  # 创建Button
# #
# # win.Show()  # 显示窗体
# #
# # app.MainLoop()
#
#
# import wx
#
# class HelloFrame(wx.Frame):
#     """
#     A Frame that says Hello World
#     """
#
#     def __init__(self, *args, **kw):
#         # ensure the parent's __init__ is called
#         super(HelloFrame, self).__init__(*args, **kw)
#
#         # create a panel in the frame
#         pnl = wx.Panel(self)
#
#         # put some text with a larger bold font on it
#         st = wx.StaticText(pnl, label="Hello World!")
#         font = st.GetFont()
#         font.PointSize += 10
#         font = font.Bold()
#         st.SetFont(font)
#
#         # and create a sizer to manage the layout of child widgets
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
#         pnl.SetSizer(sizer)
#
#         # create a menu bar
#         self.makeMenuBar()
#
#         # and a status bar
#         self.CreateStatusBar()
#         self.SetStatusText("Welcome to wxPython!")
#
#
#     def makeMenuBar(self):
#         """
#         A menu bar is composed of menus, which are composed of menu items.
#         This method builds a set of menus and binds handlers to be called
#         when the menu item is selected.
#         """
#
#         # Make a file menu with Hello and Exit items
#         fileMenu = wx.Menu()
#         # The "\t..." syntax defines an accelerator key that also triggers
#         # the same event
#         helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
#                 "Help string shown in status bar for this menu item")
#         fileMenu.AppendSeparator()
#         # When using a stock ID we don't need to specify the menu item's
#         # label
#         exitItem = fileMenu.Append(wx.ID_EXIT)
#
#         # Now a help menu for the about item
#         helpMenu = wx.Menu()
#         aboutItem = helpMenu.Append(wx.ID_ABOUT)
#
#         # Make the menu bar and add the two menus to it. The '&' defines
#         # that the next letter is the "mnemonic" for the menu item. On the
#         # platforms that support it those letters are underlined and can be
#         # triggered from the keyboard.
#         menuBar = wx.MenuBar()
#         menuBar.Append(fileMenu, "&File")
#         menuBar.Append(helpMenu, "&Help")
#
#         # Give the menu bar to the frame
#         self.SetMenuBar(menuBar)
#
#         # Finally, associate a handler function with the EVT_MENU event for
#         # each of the menu items. That means that when that menu item is
#         # activated then the associated handler function will be called.
#         self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
#         self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
#         self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
#
#
#     def OnExit(self, event):
#         """Close the frame, terminating the application."""
#         self.Close(True)
#
#
#     def OnHello(self, event):
#         """Say hello to the user."""
#         wx.MessageBox("Hello again from wxPython")
#
#
#     def OnAbout(self, event):
#         """Display an About Dialog"""
#         wx.MessageBox("This is a wxPython Hello World sample",
#                       "About Hello World 2",
#                       wx.OK|wx.ICON_INFORMATION)
#
#
# if __name__ == '__main__':
#     # When this module is run (not imported) then create the app, the
#     # frame, show it, and start the event loop.
#     app = wx.App()
#     frm = HelloFrame(None, title='Hello World 2')
#     frm.Show()
#     app.MainLoop()
import wx
import time


class ClockWindow(wx.Window):
    def __init__(self, parent):
        wx.Window.__init__(self, parent)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.timer = wx.Timer(self)  # 创建定时器
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)  # 绑定一个定时器事件
        self.timer.Start(1000)  # 设定时间间隔

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


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="wx.Timer")
        ClockWindow(self)


app = wx.PySimpleApp()
frm = MyFrame()
frm.Show()
app.MainLoop()
