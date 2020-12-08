import wx

def bind_menus(self):
    self.Bind(wx.EVT_MENU, self.bind_menu_info, self.menuItem_info)
    self.Bind(wx.EVT_MENU, self.bind_menu_update_info, self.menu_updateinfo)
    self.Bind(wx.EVT_MENU, self.bind_menu_exit, self.menu_exit)
    return