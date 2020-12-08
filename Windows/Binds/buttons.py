import wx

def bind_buttons(self):
    for i in range(1,43):
        mark = "self.days_"
        eval(mark+str(i)).Bind(wx.EVT_LEFT_DCLICK,self.set_text)
    return

