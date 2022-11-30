from ui import get_action, get_info_3, get_info_1, get_info_2
from csv_append import append_user, reading_csv



def start_engine():
    act = get_action()
    if act == 3:
        append_user(get_info_3())
    if act == 1:
        reading_csv(get_info_1())
    if act == 2:
        reading_csv(get_info_2())
