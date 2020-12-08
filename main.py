# -*- coding: utf-8 -*-
import wx
from Windows.window_main import MainWindow

class UI(MainWindow):
    def __init__(self):
        super(UI,self).__init__(None)


if __name__ == '__main__':
    app = wx.App()
    # None表示的是此窗口没有上级父窗体。如果有，就直接在父窗体代码调用的时候填入‘self’就好了。
    main_win = UI()
    main_win.init_main_window()
    main_win.Show()
    app.MainLoop()
