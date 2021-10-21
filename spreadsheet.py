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

def write(data):
    """Write data to spreadsheet."""
    ws.append(list(data.values()))
    wb.save("data.xlsx")

def error_inputs(var):
    """Check most entries/comboboxes/radiobuttons if it blanks."""
    return var == '' or var.isspace()

def error_numeric(num):
    """Check entry if it's blank/not a number."""
    if num == '':
        return 'blank'
    elif not num.isnumeric():
        return 'num'
    return False

def error_email(email):
    """Check email if it's blank/wrong format."""
    if email == '':
        return 'blank'
    elif email.count('@') != 1 or email.count('.') < 1:
        return 'format'
    return False

def error_date(date):
    """Check dates if blank/wrong format."""
    if date == '':
        return 'blank'
    elif date[2:6:3] != '--':
        return 'format'
    else:
        if not 12 >= int(date[3:5]) >= 1:
            return 'month'
        if int(date[:2]) < 1:
            return 'day'
        elif int(date[3:5]) in [1, 3, 5, 7, 8, 10, 12] and int(date[:2]) > 31:
            return 'day'
        elif int(date[3:5]) in [4, 6, 9, 11] and int(date[:2]) > 31:
            return 'day'
        return False

def dupl_name(name):
    """Check for name duplicates."""
    return name in current_data[1]

def dupl_tel(tel):
    """Check for tel duplicates."""
    return tel in current_data[3]

def dupl_email(email):
    """Check for email duplicates."""
    return email in current_data[4]

#0:name_start, 1:name,           2:age,        3:tel,  4:email,
#5:start,      6:start_time,     7:start_date, 8:dest, 9:dest_time,
#10:dest_date, 11:class_airport, 12:seat

def dupl_seat(seat, date, check):
    if check == 'start':
        col = 7
    elif check == 'end':
        col = 10
    used_seats_start = [ #if start_date in sheet == one in data, add seat into this list
        current_data[12][i]
        for i in range(len(current_data[12]))
        if current_data[col][i] == date
    ]
    return seat in used_seats_start

