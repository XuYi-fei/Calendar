import wx

def bind_combos(self):
    self.Bind(wx.EVT_COMBOBOX, self.bind_combo_box_time, self.combo_box_year)
    self.Bind(wx.EVT_COMBOBOX, self.bind_combo_box_time, self.combo_box_month)
    self.Bind(wx.EVT_COMBOBOX, self.bind_combo_box_time, self.combo_box_day)
    return


