# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class baseMainWindow
###########################################################################

class baseMainWindow ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"万年历_version1", pos = wx.DefaultPosition, size = wx.Size( 1120,740 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		fgSizer3 = wx.FlexGridSizer( 5, 1, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.title = wx.StaticText( self, wx.ID_ANY, u"万年历\n（1970-2099）", wx.Point( -1,-1 ), wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.title.Wrap( -1 )

		self.title.SetFont( wx.Font( 23, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer3.Add( self.title, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		combo_box_yearChoices = [ u"2020", u"2019", u"2018", u"2017", u"2016", u"2015", u"2014", u"2013", u"2012" ]
		self.combo_box_year = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"2020", wx.DefaultPosition, wx.DefaultSize, combo_box_yearChoices, 0 )
		self.combo_box_year.SetSelection( 0 )
		self.combo_box_year.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		self.combo_box_year.SetMinSize( wx.Size( 120,-1 ) )

		sbSizer1.Add( self.combo_box_year, 0, wx.ALL, 5 )

		self.m_staticText54 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"年", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText54.Wrap( -1 )

		self.m_staticText54.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		sbSizer1.Add( self.m_staticText54, 1, wx.ALL, 5 )

		combo_box_monthChoices = [ u"01", u"02", u"03", u"04", u"05", u"06", u"07", u"08", u"09", u"10", u"11", u"12" ]
		self.combo_box_month = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, combo_box_monthChoices, 0 )
		self.combo_box_month.SetSelection( 1 )
		self.combo_box_month.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		self.combo_box_month.SetMinSize( wx.Size( 120,-1 ) )

		sbSizer1.Add( self.combo_box_month, 0, wx.ALL, 5 )

		self.m_staticText56 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"月", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText56.Wrap( -1 )

		self.m_staticText56.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		sbSizer1.Add( self.m_staticText56, 1, wx.ALL, 5 )

		combo_box_dayChoices = [ u"01", u"02", u"03", u"04", u"05", u"06", u"07", u"08", u"09", u"10", u"11", u"12", u"13", u"14", u"15", u"16", u"17", u"18", u"19", u"20", u"21", u"22", u"23", u"24", u"25", u"26", u"27", u"28", u"29", u"30", u"31", wx.EmptyString, wx.EmptyString, wx.EmptyString ]
		self.combo_box_day = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, combo_box_dayChoices, 0 )
		self.combo_box_day.SetSelection( 1 )
		self.combo_box_day.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		self.combo_box_day.SetMinSize( wx.Size( 120,-1 ) )

		sbSizer1.Add( self.combo_box_day, 0, wx.ALL, 5 )

		self.m_staticText57 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"日", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText57.Wrap( -1 )

		self.m_staticText57.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		sbSizer1.Add( self.m_staticText57, 1, wx.ALL, 5 )


		fgSizer3.Add( sbSizer1, 1, wx.EXPAND, 5 )

		self.button1 = wx.Button( self, wx.ID_ANY, u"查询", wx.Point( 1000,1000 ), wx.Size( -1,-1 ), 0 )
		self.button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		fgSizer3.Add( self.button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.weekday_0 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"周日", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.weekday_0.Wrap( -1 )

		sbSizer2.Add( self.weekday_0, 1, wx.ALL, 5 )

		self.weekday_1 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"周一", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.weekday_1.Wrap( -1 )

		sbSizer2.Add( self.weekday_1, 1, wx.ALL, 5 )

		self.weekday_2 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"周二", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.weekday_2.Wrap( -1 )

		sbSizer2.Add( self.weekday_2, 1, wx.ALL, 5 )

		self.weekday_3 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"周三", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.weekday_3.Wrap( -1 )

		sbSizer2.Add( self.weekday_3, 1, wx.ALL, 5 )

		self.weekday_4 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"周四", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.weekday_4.Wrap( -1 )

		sbSizer2.Add( self.weekday_4, 1, wx.ALL, 5 )

		self.weekday_5 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"周五", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.weekday_5.Wrap( -1 )

		sbSizer2.Add( self.weekday_5, 1, wx.ALL, 5 )

		self.weekday_6 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"周六", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.weekday_6.Wrap( -1 )

		sbSizer2.Add( self.weekday_6, 1, wx.ALL, 5 )


		fgSizer3.Add( sbSizer2, 1, wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 7, 7, 0, 0 )

		gSizer1.SetMinSize( wx.Size( 1200,500 ) )
		self.days_1 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_1.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_1, 0, wx.ALL, 5 )

		self.days_2 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_2.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_2, 0, wx.ALL, 5 )

		self.days_3 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_3.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_3, 0, wx.ALL, 5 )

		self.days_4 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_4.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_4, 0, wx.ALL, 5 )

		self.days_5 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_5.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_5, 0, wx.ALL, 5 )

		self.days_6 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_6.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_6, 0, wx.ALL, 5 )

		self.days_7 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_7.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_7, 0, wx.ALL, 5 )

		self.days_8 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_8.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_8, 0, wx.ALL, 5 )

		self.days_9 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_9.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_9, 0, wx.ALL, 5 )

		self.days_10 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_10.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_10, 0, wx.ALL, 5 )

		self.days_11 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_11.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_11, 0, wx.ALL, 5 )

		self.days_12 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_12.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_12, 0, wx.ALL, 5 )

		self.days_13 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_13.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_13, 0, wx.ALL, 5 )

		self.days_14 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_14.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_14, 0, wx.ALL, 5 )

		self.days_15 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_15.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_15, 0, wx.ALL, 5 )

		self.days_16 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_16.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_16, 0, wx.ALL, 5 )

		self.days_17 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_17.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_17, 0, wx.ALL, 5 )

		self.days_18 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_18.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_18, 0, wx.ALL, 5 )

		self.days_19 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_19.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_19, 0, wx.ALL, 5 )

		self.days_20 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_20.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_20, 0, wx.ALL, 5 )

		self.days_21 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_21.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_21, 0, wx.ALL, 5 )

		self.days_22 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_22.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_22, 0, wx.ALL, 5 )

		self.days_23 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_23.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_23, 0, wx.ALL, 5 )

		self.days_24 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_24.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_24, 0, wx.ALL, 5 )

		self.days_25 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_25.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_25, 0, wx.ALL, 5 )

		self.days_26 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_26.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_26, 0, wx.ALL, 5 )

		self.days_27 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_27.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_27, 0, wx.ALL, 5 )

		self.days_28 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_28.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_28, 0, wx.ALL, 5 )

		self.days_29 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_29.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_29, 0, wx.ALL, 5 )

		self.days_30 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_30.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_30, 0, wx.ALL, 5 )

		self.days_31 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_31.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_31, 0, wx.ALL, 5 )

		self.days_32 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_32.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_32, 0, wx.ALL, 5 )

		self.days_33 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_33.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_33, 0, wx.ALL, 5 )

		self.days_34 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_34.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_34, 0, wx.ALL, 5 )

		self.days_35 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_35.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_35, 0, wx.ALL, 5 )

		self.days_36 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_36.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_36, 0, wx.ALL, 5 )

		self.days_37 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_37.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_37, 0, wx.ALL, 5 )

		self.days_38 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_38.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_38, 0, wx.ALL, 5 )

		self.days_39 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_39.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_39, 0, wx.ALL, 5 )

		self.days_40 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_40.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_40, 0, wx.ALL, 5 )

		self.days_41 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_41.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_41, 0, wx.ALL, 5 )

		self.days_42 = wx.Button( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		self.days_42.SetLabelMarkup( u" " )
		gSizer1.Add( self.days_42, 0, wx.ALL, 5 )


		fgSizer3.Add( gSizer1, 0, wx.EXPAND, 5 )


		self.SetSizer( fgSizer3 )
		self.Layout()
		self.menubar1 = wx.MenuBar( 0 )
		self.menu_menu = wx.Menu()
		self.menuItem_info = wx.MenuItem( self.menu_menu, wx.ID_ANY, u"说明"+ u"\t" + u"F11", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_menu.Append( self.menuItem_info )

		self.menu_updateinfo = wx.MenuItem( self.menu_menu, wx.ID_ANY, u"更新说明"+ u"\t" + u"F12", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_menu.Append( self.menu_updateinfo )

		self.menu_exit = wx.MenuItem( self.menu_menu, wx.ID_ANY, u"退出"+ u"\t" + u"ESC", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_menu.Append( self.menu_exit )

		self.menubar1.Append( self.menu_menu, u"菜单" )

		self.SetMenuBar( self.menubar1 )

		self.status_main = self.CreateStatusBar( 2, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.button1.Bind( wx.EVT_BUTTON, self.main_button_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def main_button_click( self, event ):
		event.Skip()


