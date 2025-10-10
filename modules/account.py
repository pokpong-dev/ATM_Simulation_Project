# modules/account.py
# พวกระบบบัญชี (ยังไม่ทำจริง แค่โครง)
#asdwqweqewqwe

from logging import exception
import datetime
import random
import file_handler
from modules.file_handler import read_transaction_file

#randomตัวเลขธุรกรรม
def transaction_id_generator():
    x = random.randint(100000000000000000,999999999999999999)
    return str(x)

#ฝากเงิน
def add_transaction_deposit(account_number,amount):
    plus_num = 0
    dep = file_handler.read_transaction_file(account_number)
    lol = len(dep)
    for i in range(lol):
        acc_num = dep[i].split(",")[3]
        new_balance = dep[i].split(",")[4]
        Deletepoint = acc_num.find(".")
        Deletepoint1 = new_balance.find(".")
        cut = acc_num[:Deletepoint]
        cut1 = new_balance[:Deletepoint1]
        if i == lol - 1:
            decimal = float(cut)
            decimal1 = float(cut1)
            plus_num += decimal1
            print(plus_num)
            print(cut,cut1)
    timestamps = datetime.datetime.now().isoformat()
    file_handler.append_transaction_log_file(
        account_number=account_number,
        transaction_id=transaction_id_generator(),
        timestamp=timestamps[0:19],
        type_i="deposit",
        amount=amount,
        balance= amount+plus_num,
        target="")

#เซ็คเลขบัญชีว่ามีอยู่จริงมั้ย
def add_transaction_firstdeposit(account_number,amount):
    checkfile = False
    check = False
    num_acc = file_handler.read_accounts_file()
    for i in range(len(num_acc)):
        acc_num = num_acc[i].split(",")[3]
        if acc_num == account_number :
            check = True
            print(acc_num)
            break

    try:
        file_handler.read_transaction_file(account_number)
    except:
        checkfile = True
    if check == True and checkfile == True:
        timestamps = datetime.datetime.now().isoformat()
        file_handler.append_transaction_log_file(
            account_number=account_number,
            transaction_id=transaction_id_generator(),
            timestamp=timestamps[0:19],
            type_i="deposit",
            amount=amount,
            balance=amount,
            target="")
        return {"status":"success","msg":"มันไม่มีบัญชี"}
    else:
        return {"status":"error","msg":"มันไม่มีบัญชี"}

#ถอนเงิน
def add_transaction_withdrawal(account_number,amount):
    plus_num = 0
    dep = file_handler.read_transaction_file(account_number)
    lol = len(dep)
    for i in range(lol):
        acc_num = dep[i].split(",")[3]
        new_balance = dep[i].split(",")[4]
        Deletepoint = acc_num.find(".")
        Deletepoint1 = new_balance.find(".")
        cut = acc_num[:Deletepoint]
        cut1 = new_balance[:Deletepoint1]
        if i == lol - 1:
            decimal = float(cut)
            decimal1 = float(cut1)
            plus_num -= decimal1
    timestamps = datetime.datetime.now().isoformat()
    file_handler.append_transaction_log_file(
        account_number=account_number,
        transaction_id=transaction_id_generator(),
        timestamp=timestamps[0:19],
        type_i="withdrawal",
        amount=amount,
        balance= amount-plus_num,
        target="")

#เซ็กยอดเงิน
def check_balance(account_number):
    dep = file_handler.read_transaction_file(account_number)
    lol = len(dep)
    for i in range(lol):
        acc_num = dep[i].split(",")[4]
        if i == lol - 1:
            return acc_num

#โอนเงิน
def add_transaction_transfer(account_number,account_numberv2,amount):
    plus_num = 0
    dep = file_handler.read_transaction_file(account_number)
    lol = len(dep)
    for i in range(lol):
        acc_num = dep[i].split(",")[3]
        new_balance = dep[i].split(",")[4]
        Deletepoint = acc_num.find(".")
        Deletepoint1 = new_balance.find(".")
        cut = acc_num[:Deletepoint]
        cut1 = new_balance[:Deletepoint1]
        if i == lol - 1:
            decimal = float(cut)
            decimal1 = float(cut1)
            plus_num -= decimal1
    timestamps = datetime.datetime.now().isoformat()
    file_handler.append_transaction_log_file(
        account_number=account_number,
        transaction_id=transaction_id_generator(),
        timestamp=timestamps[0:19],
        type_i="transfer",
        amount=amount,
        balance= amount-plus_num,
        target=account_numberv2
    )
    add_transaction_firstdeposit(account_numberv2,abs(amount))
    if len(file_handler.read_transaction_file(account_numberv2))>= 2:
        add_transaction_deposit(account_numberv2, abs(amount))

#ถอนเงินที่ตู้
b1000


# x = add_transaction_firstdeposit(account_number="123-4-56789-1",amount=20000.0)
#y = add_transaction_deposit("123-4-56789-0",3000.00)
#m = add_transaction_withdrawal("123-4-56789-0",-3000.00)
#c = check_balance("123-4-56789-0")
o = add_transaction_transfer("123-4-56789-0","123-4-56789-1",-1000.00)
print(o)







