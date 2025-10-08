import os


#ฟังชันที่มี _ เราใช้ของเราเองนะจะใช้แค่ไฟล์นี้แหละ
#ฟังชันที่ไม่มี _ อันนนั้น public เลย ใช้ใน main_program หรือ module ได้เบยยย

### PRIVATE GLOBAL VARIABLES ###
_save_as_account_file_name = "accounts_data.txt"
_transactions_folder_name = "transaction_logs"

_current_file_location = os.path.dirname(os.path.dirname(__file__))
accounts_file = os.path.join(_current_file_location, _save_as_account_file_name)

_current_folder = os.path.dirname(__file__) #คืนค่าเป็นตำแหน่งที่ folder อยู่
_root_folder = os.path.dirname(_current_folder) #กลับไป 1 folder

# /home/user/atm_simulation_project/transaction_log
# /home/user/atm_simulation_project

if not os.path.exists(accounts_file):
    open(accounts_file, "w").close()
else:
    pass

_folder_path = os.path.join(_root_folder, _transactions_folder_name) #ต่อ string folder

if not os.path.exists(_folder_path):
    os.makedirs(_folder_path) # สร้าง folder
    pass
else:
    pass

#TEMPLATE#

_account_template = "title,first_name,last_name,account_number,pin,created_at"
_transaction_template = "transaction_id,timestamp,type,amount,balance,target"

_list_account_template = [_account_template]
_list_transaction_template = [_transaction_template]


### PRIVATE HELPERS ###
def _is_header(file_location, find_header_data):
    """
    เช็คว่ามี header มุ้ย
    :param file_location (str):
    :param find_header_data (str):
    :return boolean True/False
    """
    if not isinstance(file_location,str):
        raise TypeError(f"{file_location} ต้องเป็น str นะเพื่อน ไม่ใช่ {type(file_location)}")
    try:
        with open(file_location, "r") as f:
            first_line = f.readline().strip()
            if first_line == find_header_data:
                return True
            else:
                return False
    except FileNotFoundError:
        raise FileNotFoundError(f"หาไฟล์ {file_location} ไม่เจออะเพื่อน")


def _write_header(file_location, template):
    """
    เขียน header ของไฟล์ ด้วย template parameter ที่ส่งเข้ามา
    :param file_location: (str)
    :param template:  (str) _account_template or _transaction_template
    :return boolean True/False
    """
    try:
        with open(file_location, "w") as f:
            if template == "_account_template":
                f.write(_account_template + "\n")
            elif template == "_transaction_template":
                f.write(_transaction_template + "\n")
            else:
                raise FileNotFoundError(f"{template} ที่นายส่งมามันไม่ถูกเพื่อนมันมีแค่ account_template กับ transaction_template")
    except FileNotFoundError:
        raise FileNotFoundError(f"หาไฟล์ {file_location} ไม่เจออะเพื่อน")


### PUBLIC FUNCTIONS ###
def append_account_file(title, first_name, last_name, account_number, pin, created_at):
    """
    เพิ่มข้อมูล account ถ้าไม่มีสร้างใหม่อัตโนมัติ ถ้ามีก็เขียนต่อบรรทัดสุดท้ายของไฟล์นั้นๆ
    :param title: str
    :param first_name: str
    :param last_name: str
    :param account_number: str
    :param pin: str
    :param created_at: str
    :return: None
    """
    _validate_account_parameter = {
        "title": str,
        "first_name": str,
        "last_name": str,
        "account_number": str,
        "pin": str,
        "created_at": str
    }

    for my_friend_parameter, validate_account_paramete in _validate_account_parameter.items():
        value = locals()[my_friend_parameter]
        if not isinstance(value, validate_account_paramete):
            raise TypeError(f"{my_friend_parameter} ต้องเป็น {validate_account_paramete.__name__} นะเพื่อน ไม่ใช่ {type(value).__name__}")


    get_args_account = [title, first_name, last_name, account_number, pin, created_at]
    if not _is_header(accounts_file, _account_template):
        _write_header(accounts_file, _account_template)
    convert_list_to_string = ",".join(str(x) for x in get_args_account)
    with open(accounts_file, "a") as f:
        f.write(convert_list_to_string + "\n")


def append_transaction_log_file(account_number, transaction_id, timestamp, type_i, amount, balance, target):
    """
    เพิ่ม transaction ของแต่ละคน
    :param account_number: str
    :param transaction_id: str
    :param timestamp: str
    :param type_i: str
    :param amount: str
    :param balance: float
    :param target: str
    :return None
    """

    _validate_transaction_parameter = {
        "account_number": str,
        "transaction_id": str,
        "timestamp": str,
        "type_i": str,
        "amount": float,
        "balance": float,
        "target": str
    }

    for my_friend_parameter, validate_transaction_paramete in _validate_transaction_parameter.items():
        value = locals()[my_friend_parameter]
        if not isinstance(value, validate_transaction_paramete):
            raise TypeError(f"{my_friend_parameter} ต้องเป็น {validate_transaction_paramete.__name__} นะเพื่อน ไม่ใช่ {type(value).__name__}")

    merge_account_number_file_with_dot_txt = account_number + ".txt"
    get_transaction_location = os.path.join(_folder_path, merge_account_number_file_with_dot_txt)
    get_args_transaction = [transaction_id, timestamp, type_i, amount, balance, target]
    with open(get_transaction_location, "a") as f:
        if not _is_header(get_transaction_location, _transaction_template):
            _write_header(get_transaction_location, _transaction_template)
        convert_list_to_string = ",".join(str(x) for x in get_args_transaction)
        f.write(convert_list_to_string + "\n")


def read_accounts_file():
    """
    อ่านข้อมูลใน accounts.txt
    :return list of str ออกมา: (ข้อมูลที่เก็บในไฟล์บัญชีทั้งหมด)
    """
    try:
        with open(accounts_file, "r") as f:
            list_accounts = f.readlines()
            return list_accounts
    except FileNotFoundError:
        raise FileNotFoundError(f"หาไฟล์ {_save_as_account_file_name} ไม่เจออะเพื่อน")


def read_transaction_file(account_number):
    """
    :param account_number: str
    :return list of str ออกมา (ข้อมูลที่อยู่ใน folder transaction_log ของเลขบัญชีนั้นๆ)
    """
    if not isinstance(account_number,str):
        raise TypeError(f"{account_number} ต้องเป็น str นะเพื่อน ไม่ใช่ {type(account_number)}")
    edit_file = _folder_path + "/" + account_number + ".txt"
    try:
        with open(edit_file, "r") as f:
            list_transactions = f.readlines()
            return list_transactions
    except FileNotFoundError:
        raise FileNotFoundError(f"หาไฟล์ {account_number}.txt ใน folder {_transactions_folder_name} ไม่เจออะเพื่อน")



# # ตัวอย่างการใช้งาน
# ### auth with file_handler ###
# ##append mode##
# append_account_file("MR", "Pokpong", "Numberone", "123-4-56789-0", "655576", 15000.0, "2025-10-07T21:35:00+07:00")
#
# # ตัวอย่างการใช้งาน
# ### account with file_handler ###
# ##append mode##
# #deposit
# append_transaction_log_file(
#     account_number="123-4-56789-0",
#     transaction_id="TXN0001",
#     timestamp="2025-10-07T21:35:00+07:00",
#     type_i="deposit",
#     amount=15000.1,
#     balance=655576.1,
#     target=""
# )
#
# #withdraw
# append_transaction_log_file(
#     account_number="123-4-56789-0",
#     transaction_id="TXN0001",
#     timestamp="2025-10-07T21:35:00+07:00",
#     type_i="withdrawal",
#     amount=15000.1,
#     balance=655576.1,
#     target=""
# )
#
# #transfer
# append_transaction_log_file(
#     account_number="123-4-56789-0",
#     transaction_id="TXN0001",
#     timestamp="2025-10-07T21:35:00+07:00",
#     type_i="transfer",
#     amount=15000.1,
#     balance=655576.1,
#     target="983-4-96789-0"
# )
#
# x = read_accounts_file()
# y = read_transaction_file("123-4-56789-0")
# print(x)
# print(y)
#
