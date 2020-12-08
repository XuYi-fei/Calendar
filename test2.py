def createWidgets(self):
    self.listCtrl = wxskinListCtrl(self, ID_LISTCTRL,
                                   style=wx.LC_REPORT | wx.SUNKEN_BORDER | wx.LC_SINGLE_SEL | wx.LC_VRULES | wx.LC_HRULES)
    self.listCtrl.InsertColumn(COL_STATUS, "Status")
    self.listCtrl.InsertColumn(COL_DATE, "Date")
    self.listCtrl.InsertColumn(COL_FROM, "From")
    self.listCtrl.InsertColumn(COL_MESSAGE, "Message")

    ColumnSorterMixin.__init__(self, 4)

    self.currentItem = 0

    wx.EVT_SIZE(self, self.OnSize)
    wx.EVT_LIST_ITEM_SELECTED(self, ID_LISTCTRL, self.OnItemSelected)
    wx.EVT_LIST_ITEM_ACTIVATED(self, ID_LISTCTRL, self.OnItemActivated)
    wx.EVT_RIGHT_DOWN(self.listCtrl, self.OnRightDown)
    wx.EVT_LEFT_DCLICK(self.listCtrl, self.OnPopupEdit)
    wx.EVT_CLOSE(self, self.closeWindow)

    # for wxMSW and wxGTK respectively
    wx.EVT_COMMAND_RIGHT_CLICK(self.listCtrl, ID_LISTCTRL, self.OnRightClick)
    wx.EVT_RIGHT_UP(self.listCtrl, self.OnRightClick)