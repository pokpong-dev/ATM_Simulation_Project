#  File Handler by pokpong

> Docs นี้ใช้เฉพาะฟังชัน (ชื่อที่ *ไม่มี* `_` นำหน้า) สำหรับจัดการไฟล์บัญชีและไฟล์บันทึกธุรกรรม


---

## `append_account_file(title, first_name, last_name, account_number, pin, balance, created_at)`

เพิ่มข้อมูล **บัญชีผู้ใช้** ลงท้ายไฟล์ `accounts_data.txt`
ถ้าไฟล์ยังไม่มี **จะสร้างไฟล์** และ **เขียน header อัตโนมัติ**

### Parameters

| ชื่อ             | ชนิด    | คำอธิบาย                                           |
|------------------|---------|----------------------------------------------------|
| `title`          | `str`   | คำนำหน้าชื่อ (เช่น `"MR"`)                         |
| `first_name`     | `str`   | ชื่อจริง                                           |
| `last_name`      | `str`   | นามสกุล                                            |
| `account_number` | `str`   | เลขบัญชี (xxx-x-xxxxx-x)                           |
| `pin`            | `str`   | รหัส PIN                                           |
| `created_at`     | `str`   | เวลา (เช่น ISO8601: `"2025-10-07T21:35:00+07:00"`) |

### Returns

* `None`

### process

* เขียน/ต่อท้ายไฟล์ `accounts_data.txt`
* ถ้าไฟล์ยังไม่มี header จะเขียน header:
  `title,first_name,last_name,account_number,pin,balance,created_at`

### Raises

* `TypeError` เมื่อชนิดข้อมูลของพารามิเตอร์ไม่ตรงตามที่กำหนด

### Example

```python
append_account_file(
    "MR", "Pokpong", "Numberone",
    "123-4-56789-0", "655576", 15000.0,
    "2025-10-07T21:35:00+07:00"
)
```

---

## `append_transaction_log_file(account_number, transaction_id, timestamp, type_i, amount, balance, target)`

เพิ่ม **ธุรกรรมของบัญชี** ลงท้ายไฟล์ `transaction_logs/<account_number>.txt`
ถ้าไฟล์ยังไม่มี **จะสร้างไฟล์** และ **เขียน header อัตโนมัติ**

### Parameters

| ชื่อ             | ชนิด    | คำอธิบาย                                                |
|------------------|---------|---------------------------------------------------------|
| `account_number` | `str`   | เลขบัญชี (ใช้กำหนดชื่อไฟล์ปลายทาง)                      |
| `transaction_id` | `str`   | ไอดีธุรกรรม                                             |
| `timestamp`      | `str`   | เวลา (เช่น ISO8601)                                     |
| `type_i`         | `str`   | ประเภท (`"deposit"`, `"withdrawal"`, `"transfer"`)      |
| `amount`         | `float` | จำนวนเงินของธุรกรรม                                     |
| `balance`        | `float` | ยอดคงเหลือหลังธุรกรรม                                   |
| `target`         | `str`   | เป้าหมาย (เช่นเลขบัญชีปลายทางกรณีโอน; ไม่มีให้ใส่ `""`) |

### Returns

* `None`

### Process

* เขียน/ต่อท้ายไฟล์ `transaction_logs/<account_number>.txt`
* ถ้าไฟล์ยังไม่มี header จะเขียน header:
  `transaction_id,timestamp,type,amount,balance,target`

### Raises

* `TypeError` เมื่อชนิดข้อมูลของพารามิเตอร์ไม่ตรงตามที่กำหนด

### Examples

```python
# ฝากเงิน
append_transaction_log_file(
    account_number="123-4-56789-0",
    transaction_id="TXN0001",
    timestamp="2025-10-07T21:35:00+07:00",
    type_i="deposit",
    amount=15000.1,
    balance=655576.1,
    target=""
)

# ถอนเงิน
append_transaction_log_file(
    account_number="123-4-56789-0",
    transaction_id="TXN0002",
    timestamp="2025-10-07T21:40:00+07:00",
    type_i="withdrawal",
    amount=500.0,
    balance=655076.1,
    target=""
)

# โอนเงิน
append_transaction_log_file(
    account_number="123-4-56789-0",
    transaction_id="TXN0003",
    timestamp="2025-10-07T21:45:00+07:00",
    type_i="transfer",
    amount=1000.0,
    balance=654076.1,
    target="983-4-96789-0"
)
```

---

## `read_accounts_file()`

อ่านข้อมูลทั้งหมดจาก `accounts_data.txt`

### Parameters

* (ไม่มี)

### Returns

* `list[str]` — ทุกบรรทัด (รวม header)




### Example

```python
yim_kiw_chain = read_accounts_file()
print(yim_kiw_chain)
```

---

## `read_transaction_file(account_number)`

อ่านข้อมูลธุรกรรมจากไฟล์ `transaction_logs/<account_number>.txt`

### Parameters

| ชื่อ             | ชนิด  | คำอธิบาย               |
|------------------|-------|------------------------|
| `account_number` | `str` | เลขบัญชีที่ต้องการอ่าน |

### Returns

* `list[str]` — รายการบรรทัดทั้งหมดในไฟล์ (รวม header)


### Example

```python
i_love_stat = read_transaction_file("123-4-56789-0")
print(i_love_stat)
```

---
