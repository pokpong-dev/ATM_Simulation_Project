# modules/account.py

import datetime
import random

from modules import atm_file_handler


#randomตัวเลขธุรกรรม
def transaction_id_generator():
    x = random.randint(100000000000000000,999999999999999999)
    return str(x)

#ฝากเงิน
def add_transaction_deposit(account_number,amount):
    plus_num = 0
    gen_transaction_id = transaction_id_generator()
    try:
        dep = atm_file_handler.read_transaction_file(account_number)
        lol = len(dep)
        for i in range(lol):
            acc_num = dep[i].split(",")[3]
            new_balance = dep[i].split(",")[4]
            deletepoint = acc_num.find(".")
            deletepoint1 = new_balance.find(".")
            cut1 = new_balance[:deletepoint1]
            if i == lol - 1:
                decimal1 = float(cut1)
                plus_num += decimal1
        timestamps = datetime.datetime.now().isoformat()
        atm_file_handler.append_transaction_log_file(
            account_number=account_number,
            transaction_id=gen_transaction_id,
            timestamp=timestamps[0:19],
            type_i="deposit",
            amount=amount,
            balance= amount+plus_num,
            target="")
        return {"status":"success","msg":f"ฝากเงิน {amount} บาท สำเร็จ, {gen_transaction_id}"}
    except FileNotFoundError:
        return {"status":"error","msg":"ไม่พบบัญชีหรืออาจจะทำรายการซ้ำ"}

#เซ็คเลขบัญชีว่ามีอยู่จริงมั้ย
def add_transaction_firstdeposit(account_number,amount):
    gen_transaction_id = transaction_id_generator()
    checkfile = False
    check = False
    num_acc = atm_file_handler.read_accounts_file()
    for i in range(len(num_acc)):
        acc_num = num_acc[i].split(",")[3]
        if acc_num == account_number :
            check = True
            print(check)
            break

    try:
        atm_file_handler.read_transaction_file(account_number)
    except:
        checkfile = True
    if check == True and checkfile == True:
        timestamps = datetime.datetime.now().isoformat()
        atm_file_handler.append_transaction_log_file(
            account_number=account_number,
            transaction_id=gen_transaction_id,
            timestamp=timestamps[0:19],
            type_i="deposit",
            amount=amount,
            balance=amount,
            target="")
        return {"status":"success","msg":f"ฝากเงิน {amount} บาท ครั้งแรกสำเร็จ , {gen_transaction_id} "}
    else:
        return {"status":"error","msg":"ไม่พบบัญชี"}

#ถอนเงิน
def add_transaction_withdrawal(account_number,amount):
    gen_transaction_id = transaction_id_generator()
    plus_num = 0
    try:
        dep = atm_file_handler.read_transaction_file(account_number)
        lol = len(dep)
        for i in range(lol):
            new_balance = dep[i].split(",")[4]
            deletepoint1 = new_balance.find(".")
            cut1 = new_balance[:deletepoint1]
            if i == lol - 1:
                decimal1 = float(cut1)
                plus_num += decimal1
        timestamps = datetime.datetime.now().isoformat()
        if amount > plus_num:
            return {"status":"error","msg":"ยอดเงินไม่เพียง่พอ"}
        atm_file_handler.append_transaction_log_file(
            account_number=account_number,
            transaction_id=gen_transaction_id,
            timestamp=timestamps[0:19],
            type_i="withdrawal",
            amount=-abs(amount),
            balance= plus_num-amount,
            target="")
        return {"status":"success","msg":f"ถอนเงิน {amount} สำเร็จ , {gen_transaction_id} "}
    except FileNotFoundError:
            return {"status":"error","msg":"ไม่พบบัญชี"}
            

#เซ็กยอดเงิน
def check_balance(account_number):
    try:
        dep = atm_file_handler.read_transaction_file(account_number)
        lol = len(dep)
        for i in range(lol):
            acc_num = dep[i].split(",")[4]
            if i == lol - 1:
                return {"status":"success","msg":acc_num}
    except FileNotFoundError:
        return {"status":"error","msg":"ไม่พบบัญชี"}

#โอนเงิน
def add_transaction_transfer(account_number,account_numberv2,amount):
    plus_num = 0
    gen_transaction_id = transaction_id_generator()
    try:
        dep = atm_file_handler.read_transaction_file(account_number)
        lol = len(dep)
        for i in range(lol):
            new_balance = dep[i].split(",")[4]
            deletepoint1 = new_balance.find(".")
            cut1 = new_balance[:deletepoint1]
            if i == lol - 1:
                decimal1 = float(cut1)
                plus_num += decimal1
        timestamps = datetime.datetime.now().isoformat()
        if amount > plus_num:
            return {"status":"error","msg":"ยอดเงินไม่เพียงพอ"}
        atm_file_handler.append_transaction_log_file(
            account_number=account_number,
            transaction_id=gen_transaction_id,
            timestamp=timestamps[0:19],
            type_i="transfer",
            amount=-abs(amount),
            balance= plus_num-amount,
            target=account_numberv2
        )
        add_transaction_firstdeposit(account_numberv2,amount)
        if len(atm_file_handler.read_transaction_file(account_numberv2))>= 2:
            add_transaction_deposit(account_numberv2, amount)
    except FileNotFoundError:
        return {"status":"error","msg":"ไม่พบบัญชี"}
        

def check_transaction_history(account_number):
    history = atm_file_handler.read_transaction_file(account_number)
    if not history:
        return {"status":"error","msg":"ไม่พบบัญชี"}
    return {"status": "success", "msg": history}
#ถอนเงินที่ตู้


#kplus = check_transaction_history("123-4-56789-0")
#print(kplus)
#x = add_transaction_firstdeposit(account_number="123-4-56789-0",amount=20000.0)
#y = add_transaction_deposit("123-4-56789-0",3000.00)
#m = add_transaction_withdrawal("123-4-56789-0",500.00)
#print(m)
#print(x)
# atm_file_handler.append_account_file(
#     "MR", "Pokpong", "Numberone",
#     "123-4-56789-0", "655576",
#     "2025-10-07T21:35:00+07:00"
# )
#c = check_balance("123-4-56789-0")








