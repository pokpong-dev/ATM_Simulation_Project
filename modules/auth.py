# modules/auth.py
# พวกระบบล็อคอิน/เปิดบัญชี (ยังไม่ทำจริง แค่โครง)
# modules/auth.py
# พวกระบบล็อคอิน/เปิดบัญชี (ยังไม่ทำจริง แค่โครง)
import file_handler
import random
import time
#file_handler.append_account_file()
#| ชื่อ             | ชนิด    | คำอธิบาย                                           |
#|------------------|---------|----------------------------------------------------|
#| `title`          | `str`   | คำนำหน้าชื่อ (เช่น `"MR"`)                         |
#| `first_name`     | `str`   | ชื่อจริง                                           |
#| `last_name`      | `str`   | นามสกุล                                            |
#| `account_number` | `str`   | เลขบัญชี (xxx-x-xxxxx-x)                           |
#| `pin`            | `str`   | รหัส PIN                                           |
#| `created_at`     | `str`   | เวลา (เช่น ISO8601: `"2025-10-07T21:35:00+07:00"`) |

##PIN = ต้องไม่เกิน 6 ตัว , ไม่ง่ายเกินไป , กรอกเป็นตัวเลขเท่านั้น
##First_name = ตัวแรกต้องเป็นตัวใหญ่ , กรอกเป็นตัวอักษรเท่านั้น
##Last_name = ตัวแรกต้องเป็นตัวใหญ่, กรอกเป็นตัวอักษรเท่านั้น
##account_number = *random*,เลขบัญชี (xxx-x-xxxxx-x)
def register(title, first_name, last_name, account_number, pin,created_at):
    file_handler.append_account_file("MR","Cht","Kha","xxx-x-xxxxx-x","111111","1/11")
    #check = [title, first_name, last_name, account_number, pin,created_at]
    tf = file_handler.read_accounts_file()#
    easy_pin = ["123456", "111111", "987654", "000000", "123321", "654321", "222222", "333333", "444444", "555555","666666", "777777", "888888", "999999"]
    ####สุ่มเลขบัญชี####
    acc_nums1 = random.randint(000,999)
    acc_nums2 = random.randint(0, 9)
    acc_nums3 = random.randint(00000, 99999)
    acc_nums4 = random.randint(0, 9)
    account_number = f"{acc_nums1}-{acc_nums2}-{acc_nums3}-{acc_nums4}"
    ####เวลา realtime####
    t = time.ctime()
    t1 = t.split(" ")
    del t1[2]
    times = t1[3]
    mount = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
             'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    d, m, y = t1[2], mount[t1[1]], t1[4]
    created_at = f"{d}-{m}-{y}T{times}+07:00"

#ALL    for i in range(len(tf)):
#ALL        print(tf[i].split(","))
    log_login = file_handler.read_accounts_file()
    if title == 1:
        title = "MR"
        return title
    elif title == 2:
        title = "MS"
        return title
    else:
        pass
#FNAME / LNAME
    #บัญชีซ่ำ
    for i in range(len(log_login)):
        num_accs = log_login[i].split(",")[3]
        if account_number == num_accs:
            return {"status": "failed", "msg": "มีเลขบัญชีนี้อยู่แล้ว"}
    #เช็ค fname
    if first_name.isdigit():
        return {"status": "failed", "msg": "Please enter only Charactor"}
    elif first_name[0].islower():
        return {"status": "failed", "msg": "Enter the first letter in capital letters"}
    else:
        pass
    #เช็ค Lname
    if last_name.isdigit():
        return {"status": "failed", "msg": "Please enter only Charactor"}
    elif last_name[0].islower():
        return {"status": "failed", "msg": "Enter the last letter in capital letters"}
#PIN
    if pin in easy_pin:
        return {"status": "failed", "msg": "The pin is too simple"}
    if len(pin) !=6:
        return {"status": "failed", "msg": "Please enter 6 digits"}
    if pin.isalpha():
        return {"status": "failed", "msg": "Please Enter only number"}
    else:
        return {"status": "success", "msg": "OK"}
test = register("1","W","Kha","xxx-x-xxxxx-x","131111","s")
#(test)
print(test)
def login(account_number,pin):
    log_login = file_handler.read_accounts_file()
    for i in range(len(log_login)):
        num_accs = log_login[i].split(",")[3]
        pin_accs = log_login[i].split(",")[4]
        print(num_accs)
        if account_number == num_accs:
            return {"status": "success","msg":"OK"}
        if len(pin) != 6:
            return {"status": "failed", "msg": "Please enter 6 digits"}
        elif pin == pin_accs:
            return {"status": "success", "msg": "OK"}
        elif pin.isalpha():
            return {"status": "failed", "msg": "Please Enter only number"}
        else:
            pass
ta = login("xxx-x-xxxxx-x","123452")
print(ta)





