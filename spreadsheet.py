"""Take data from main GUI, check data for errors/duplicates, write data to spreadsheet."""

from openpyxl import load_workbook

#load workbook
wb = load_workbook('data.xlsx')
ws = wb.active

#อ่านข้อมูลใน sheet มาเก็บไว้ใน list เพื่อใช้เปรีบยเทียบดูข้อมูลซ้ำ
#sheet มี 13 columes
#1:name_start, 2:name,           3:age,        4:tel,  5:email,
#6:start,      7:start_time,     8:start_date, 9:dest, 10:dest_time,
#11:dest_date, 12:class_airport, 13:seat
current_data = [
    list(list(ws.iter_cols(min_col=col, max_col=col, values_only=True))[0])
    for col in range(1, 13)
]

def check(data):
    """check for user input errors and duplicates"""
    #USER INPUT ERROR CHECKS
    #ตรวจสอบแต่ละช่อง input ว่าเขียนผิดแบบหรือไม่
    #ทุกช่องตรวจด้วยว่าใส่มาครบไหม
    #Name: เลือกคำนำหน้าหรือยัง
    error_blank_name = not bool(data['name']) or data['name'].isspace()
    error_name_start = data['name_start'] == ''
    #Age: เป็นตัวเลข
    error_blank_age = not bool(data['age']) or data['age'].isspace()
    error_age = not data['age'].isnumeric()
    #Tel: เป็นตัวเลข
    error_blank_tel = not bool(data['tel']) or data['tel'].isspace()
    error_tel = not data['tel'].isnumeric()
    #Email: มี @ .
    error_blank_email = not bool(data['email']) or data['email'].isspace()
    error_email_format = data['email'].count('@') != 1 or data['email'].count('.') < 1
    #วันที: เขียนตามแบบ (นอกจากจะเปลี่ยนเป็น gui เลือกวันที่ให้เลย)
    error_blank_start_date = not bool(data['start_date'])
    error_blank_dest_date = not bool(data['dest_date'])
    error_start_date_format = data['start_date'][2:6:3] != '--'
    error_dest_date_format = data['dest_date'][2:6:3] != '--'
    #combobox ทุกอัน: เลือกให้ครบ
    #start, start_time, dest_dest_time, class_airport, seat
    error_blank_start = not bool(data['start'])
    error_blank_start_time = not bool(data['start_time'])
    error_blank_dest = not bool(data['dest'])
    error_blank_dest_time = not bool(data['dest_time'])
    error_blank_class = not bool(data['class_airport'])
    error_blank_seat = not bool(data['seat'])

    #DUPLICATE CHECKS ==> -1
    #0:name_start, 1:name,           2:age,        3:tel,  4:email,
    #5:start,      6:start_time,     7:start_date, 8:dest, 9:dest_time,
    #10:dest_date, 11:class_airport, 12:seat
    dupl_name = data['name'] in current_data[1]
    dupl_tel = data['tel'] in current_data[3]
    dupl_email = data['email'] in current_data[4]
    used_seats_start = [ #if start_date in sheet == one in data, add seat into this list
        current_data[12][i]
        for i in range(len(current_data[12]))
        if current_data[5][i] == data['start_date']
    ]
    dupl_seat = data['seat'] in used_seats_start

    errors = [error_blank_name, error_name_start, error_blank_age, error_age,
            error_blank_tel, error_tel, error_blank_email, error_email_format,
            error_blank_start_date, error_blank_dest_date, error_start_date_format,
            error_dest_date_format, error_blank_start, error_blank_start_time,
            error_blank_dest, error_blank_dest_time, error_blank_class, error_blank_seat,
            dupl_name, dupl_tel, dupl_email, dupl_seat]

    return sum(errors) > 0 #ถ้ามีอันนึงที่ error จะ return True

def write(data):
    """write data to spreadsheet"""
    ws.append(list(data.values()))
    wb.save("data.xlsx")
