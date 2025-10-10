from modules import atm_file_handler, auth, account
import datetime

def main():
    while True:
        print("""==== ATM Simulation ====
    [1] Login
    [2] Register
    [3] Exit""")
        menu = input("Enter menu number:").strip()
        if menu == "1":
            account_number = input("Enter account number: ").strip()
            pin = input("Enter PIN number: ").strip()
            login_result = auth.login(account_number, pin)
            print(login_result["msg"])
            if login_result["status"] == "success":
                main_menu(account_number)
        elif menu == "2":
            check_title = True
            title = input("Enter title (MR/MS): ").strip()
            if title != "MR" and title != "MS":
                print("Select title MR or MS")
                check_title = False
            if check_title:
                first_name = input("Enter first name: ").strip()
                last_name = input("Enter last name: ").strip()
                pin = input("Enter 6-digit PIN: ").strip()
                register_result = auth.register(title, first_name, last_name, pin)
                print(type(register_result["msg"]))
        elif menu == "3":
            print("Goodbye")
            break
        else:
            print("Invalid menu number, please try again.")

#ใบเสร็จ Receipt
def receipt(account_number,menu_type ,amount , account_numberv2=None):
    #อ่านธุรกรรม
    try:
        transactions = atm_file_handler.read_transaction_file(account_number)
        if not transactions:
            print("ไม่พบบัญชีหรือไม่มีธุรกรรม")
            return
        lol_transaction = transactions[-1].strip().split(",")
        transaction_id = lol_transaction[0]
        timestamp = lol_transaction[1]
        balance = lol_transaction[2]
        account_numberv2_acc = account_numberv2 if account_numberv2 else "None"
        print(f"""==== {menu_type} ====
Time: {timestamp}
Account: {account_number}
Amount: {amount}
Target: {account_numberv2_acc}
Transaction ID: {transaction_id}
Balance: {balance}
        ================""")
    except FileNotFoundError:
        print("ไม่พบไฟล์ธุรกรรมของบัญชีนี้")


#หน้า Main Menu
def main_menu(account_number):
    while True:
        print(f"""==== Main Menu (Account: {account_number}) ====
[1] Check Balance
[2] Deposit
[3] Withdraw
[4] Transfer
[5] Transactions history
[6] Logout""")
        choice = input("Enter menu number:").strip()
        if choice == "1":
            balance = account.check_balance(account_number)
            #if balance is None:
            print(balance)
        elif choice == "2":
            print(type(account_number))
            print(account_number)
            amount = float(input("Enter deposit amount (100, 500, 1000 banknote only): "))
            print(amount)
            result = account.add_transaction_firstdeposit(account_number, amount)
            result = account.add_transaction_deposit(account_number, amount)
            receipt(account_number, "Deposit", amount)
            print(result["msg"])
        elif choice == "3":
            amount = float(input("Enter withdraw amount: "))
            result = account.add_transaction_withdrawal(account_number, amount)
            receipt(account_number, "Withdrawal", amount)
            print(result["msg"])
        elif choice == "4":
            account_numberv2 = input("Enter recipient account number: ").strip()
            amount = float(input("Enter transfer amount: "))
            result = account.add_transaction_transfer(account_number,account_numberv2,amount)
            receipt(account_number, "Transfer", amount, account_numberv2)
            print(result["msg"])
        elif choice == "5":
            transactions = atm_file_handler.read_transaction_file(account_number)
            print("==== Transactions history ====")
            for t in transactions:
                print(t.strip())
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid menu number, please try again.")

main()
#main_menu("123456789")