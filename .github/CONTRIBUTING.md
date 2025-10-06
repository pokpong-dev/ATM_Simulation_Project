# คู่มือ
สำหรับโปรเจกต์: **ATM Simulation Program (CLI)**  
กลุ่ท **Baan Dollar** G01

---

บทบาทแต่ละคน

| บทบาท | หน้าที่หลัก |
|--------|--------------|
| @pokpong-dev | Admin / Reviewer / Merge PR |
| สมาชิกทีม | พัฒนาโมดูลตามที่ได้รับมอบหมาย |
...

**แอดมิน (pokpong-dev)** เราจะเป็นคนตรวจสอบโค้ดให้พวกนายเอง
- Merge Pull Request เข้าสาขา `main`


---



### ขั้นตอนการใช้งาน github เบื้องต้น ###
```bash
git clone https://github.com/pokpong-dev/ATM_Simulation_Project.git
cd ATM_Simulation_Project
git pull origin main
```

จากนั้นเปลี่ยนเป็น branch ของตัวเอง

### ตัวอย่าง ###
- feature/auth
- feature/account
- feature/main_program
- feature/file_handler

### ห้ามแก้ไข main ให้ทำใน branch ตัวเองแล้วเปิด pr เดี๋ยวเราจะ review ให้)

### วิธีเปิด Pull Request (PR) ###
ไปที่หน้า GitHub
จะเห็นปุ่ม Compare & pull request → กด
ตรวจว่า base = main, compare = feature/...
GitHub จะเติม template ให้อัตโนมัติ
เขียนรายละเอียดการเปลี่ยนแปลง
กด Create Pull Request
รอการตรวจโค้ดจากปกป้อง


ถ้ามีการแก้ไข → แก้ใน branch เดิมแล้ว push ใหม่


### วิธีอัปเดตโค้ดจาก main ###

หลัง merge เสร็จ ให้ทุกคนอัปเดต branch ตัวเองด้วย

git checkout main
git pull
git checkout feature/<ชื่อ branch ตัวเอง>
git merge main

กฎที่ต้องปฏิบัติ
push ตรงเข้า main	main ถูกป้องกันไว้
ลบ branch โดยไม่ merge	งานหาย / เทสไม่ครบ
เปิด PR โดยไม่มีคำอธิบาย	Reviewer ตรวจยาก

การทดสอบอัตโนมัติ (GitHub Actions)
ทุก PR จะรัน test workflow อัตโนมัติจาก
ถ้าเทสไม่ผ่าน → PR จะขึ้น “❌ Checks failed” → Merge ไม่ได้
ถ้าเทสผ่านทั้งหมด → “✅ All checks passed” → Reviewer สามารถ merge ได้

ถ้าเจอข้อความ
“You can’t commit to main because it is a protected branch”
แปลว่า main ถูกป้องกันไม่ให้ commit ตรง เราตั้งใจเซ็ตไว้ เพราะว่าให้ทุกคนไปทำ feature/... แยกเป็นของตัวเอง
