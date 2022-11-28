from calculation import init, r_devision, r_addition, r_multiplication, r_substraction
from logger import general_log
from view import get_mode, get_r_value, get_c_value, return_result, get_system
from comp_calculation import c_devision, c_addition, c_multiplication, c_substraction, init_c


def launch_rocket():
    sort=get_system()
   
    if sort ==2:
        num1, num2 = get_r_value()
        init(num1, num2)
        action = get_mode()
        if action ==1:
            result = r_devision()
        if action ==3:
            result = r_addition()
        if action ==4:
            result = r_multiplication()
        if action ==2:
            result = r_substraction()
    if sort==1:
        num1, num2 = get_c_value()
        init_c(num1, num2)
        action = get_mode()
        if action ==1:
            result = c_devision()
        if action ==3:
            result = c_addition()
        if action ==4:
            result = c_multiplication()
        if action ==2:
            result = c_substraction()
    
 
   
    print(return_result(result, action))
    general_log(num1, num2, action, result)





