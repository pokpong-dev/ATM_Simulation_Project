import file_handler
import random
from datetime import datetime

def register(title, first_name, last_name, account_number, pin, created_at):
    #title ถ้าไม่ได้รับ MR หรือ ms
    if title != "MR" and title != "MS":
        return {"status": "Error", "msg": "Select title MR or MS"}

    piset_letter = ['@', '!', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '{', '}', '[', ']', ':', ';', '"',
                     "'", '<', '>', ',', '.', '?', '/', '\\', '|', '`']
    #เช็คพวกตัวอักษรพิเศษ
    for i in piset_letter:
        if i in first_name:
            return {"status": "Error", "msg": "ชื่อจริง ใส่ตัวอักษรพิเศษไม่ได้ กรอกเป็นตัวอักษรภาษาอังกฤษเท่านั้น"}
        if i in last_name:
            return {"status": "Error", "msg": "นามสกุล ใส่ตัวอักษรพิเศษไม่ได้ กรอกเป็นตัวอักษรภาษาอังกฤษเท่านั้น"}

    #เช็คเลขบัญชีว่าเคยสั่งสมัครยัง ในไฟ
    log_login = file_handler.read_accounts_file()
    for i in range(len(log_login)):
        num_accs = log_login[i].split(",")[3]
        if account_number == num_accs:
            return {"status": "Error", "msg": "เลขบัญชีนี้มีอยู่แล้ว"}

    # เช็ค fname กับ Lname ว่าตัวแรกเป็นตัวใหฐ่ไหม กับเชคว่าเปนตัวเลขป่าว
    if first_name.isdigit() or not first_name[0].isupper():
        return {"status": "Error", "msg": "ชื่อจริง กรอกเป็นตัวอักษร และ ตัวแรกต้องเป็นตัวพิมพ์ใหญ่เท่านั้น"}
    if last_name.isdigit() or not last_name[0].isupper():
        return {"status": "Error", "msg": "นามสกุล กรอกเป็นตัวอักษร และ ตัวแรกต้องเป็นตัวพิมพ์ใหญ่เท่านั้น"}

    #ดักพวกกรอก พิน มักง่าย
    easy_pin = ["123456", "111111", "987654", "000000", "123321", "654321", "222222", "333333", "444444", "555555",
                "666666", "777777", "888888", "999999"]
    if pin in easy_pin:
        return {"status": "Error", "msg": "รหัสง่ายเกินไป"}
    if len(pin) != 6:
        return {"status": "Error", "msg": "กรอก PIN 6 ตัว เท่านั้น"}
    if not pin.isdigit():
        return {"status": "Error", "msg": "กรอกเป็นตัวเลขเท่านั้น"}

    #สุ่มเลขบัญชี
    acc_nums1 = random.randint(0, 999)
    acc_nums2 = random.randint(0, 9)
    acc_nums3 = random.randint(0, 99999)
    acc_nums4 = random.randint(0, 9)
    account_number = f"{acc_nums1:03}-{acc_nums2}-{acc_nums3:05}-{acc_nums4}"

    #เวลา
    created_at = datetime.now().strftime("%d-%m-%YT%H:%M:%S+07:00")

    #เพิ่มข้อมูลเข้าไฟ
    file_handler.append_account_file(title, first_name, last_name, account_number, pin, created_at)

    return {"status": "success", "msg": "สมัครบัญชี สำเร็จ"}


def login(account_number, pin,created_at):

    #อ่านข้อมูลจากไฟล์ที่ reg มันเพิ่มเข้า
    log_login = file_handler.read_accounts_file()

    #เวลา
    created_at = datetime.now().strftime("%d-%m-%YT%H:%M:%S+07:00")
    #ค้นหาบัญชีที่ตรงกับ account_number
    for i in range(len(log_login)):
        # ดึงข้อมูลจากแต่ละบรรทัด
        account_data = log_login[i].split(",")
        num_accs = account_data[3]
        stored_pin = account_data[4]

        # ตรวจสอบว่าเลขบัญชีตรงกับที่ป้อน
        if account_number == num_accs:

            if pin == stored_pin:
                return {"status": "success", "msg": "ล็อคอิน สำเร็จ"}
            else:
                return {"status": "failed", "msg": "PIN ไม่ถูกต้อง"}

    #ถ้าไม่เจอเลขบัญชีในไฟ
    return {"status": "Error", "msg": "ไม่พบบัญชี"}


#ทดสอบ สมัคร เฉยๆ
test_registration = register("MR", "W", "K#", "xxx-x-xxxxx-x", "122456", "s")
print(test_registration)

#ทดสอบการล้อคอิน
test_login = login("869-3-52817-0", "122456","")
print(test_login)
