def error_date(MainWindow):
    MainWindow.combo_box_year.SetValue(MainWindow.today_year)
    MainWindow.combo_box_day.SetValue(MainWindow.today)
    MainWindow.combo_box_month.SetValue(MainWindow.today_month)
    text_year_Value, text_month_Value, text_day_Value = MainWindow.today_year, MainWindow.today_month, MainWindow.today
    return eval(text_year_Value.lstrip('0')), eval(text_month_Value.lstrip('0')), eval(text_day_Value.lstrip('0'))
