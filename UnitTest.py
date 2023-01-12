import DataHandler



def test1():
    print(DataHandler.SplitStr("[INFO    ]2022-08-11 22:24:00 | W get 12.50 Pt(6,125) by A- done","get "," Pt"))
    print(DataHandler.SplitStrAsFloat("[INFO    ]2022-08-11 22:24:00 | W get 12.50 Pt(6,125) by A- done","get "," Pt"))



test1();