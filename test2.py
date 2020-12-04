# 鼠标事件处理

import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="一对多事件处理", size=(400, 300))
        self.Centre()  # 设置窗口居中

        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_left_up)
        self.Bind(wx.EVT_MOTION, self.on_mouse_move)

    def on_left_down(self, event):
        print('鼠标按下')

    def on_left_up(self, event):
        print('鼠标释放')

    def on_mouse_move(self, event):
        print('鼠标移动')
        if event.Dragging() and event.LeftIsDown():
            # 鼠标正在移动，按左键移动
            pos = event.GetPosition()  # 取出位置
            print(pos)


# 自定义应用程序对象
class App(wx.App):
    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('应用程序退出')
        return 0


if __name__ == '__main__':
    app = App()  # 调用上面函数
    app.MainLoop()  # 进入主事件循环