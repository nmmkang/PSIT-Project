"""print ตั๋ว"""

from pathlib import Path
from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from PIL import Image, ImageTk, ImageFont, ImageDraw

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def booking():
    '''func หลัก'''

    #window หลัก
    window = Tk()
    window.geometry("1152x700")
    window.configure(bg = "#FFFFFF")
    window.title('Booking Airline-Ticket')

    #canvas หลัก
    canvas = Canvas(window, bg = "#FFFFFF", height = 700, width = 1152, bd = 0, highlightthickness = 0, relief = "ridge")
    canvas.place(x = 0, y = 0)

    #พื้นหลัง
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(576.0, 350.0,image=image_image_1)

    #พื้นหลัง ช่องกรอกข้อมูล
    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(357.0, 350.0,image=image_image_2)

    #พื้นหลัง รูปเครื่องบินก่อนสร้างตั๋ว
    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(872.0,351.0,image=image_image_3)

    #พื้นหลังตั๋วก่อนใส่ข้อมูล
    image_image_4 = Image.open('image_4.png')

    #list_combobox
    list_airport = ['Suvarnabhumi', 'Don Mueang', 'Chiang Mai']
    list_class = ['First Class', 'Business Class', 'Economy Class']
    list_time = ['07:00 AM', '11:00 AM', '04:00 PM', '08:00 PM']
    list_seat_chr = ['A', 'B', 'C', 'D', 'E', 'F']
    list_seat_num = [i for i in range(1,11)]


    #Name
    entry_name = StringVar()
    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(285.0, 236.0, image=entry_image_2)
    entry_2 = Entry(bd=0, bg="#FFFFFF", textvariable=entry_name, highlightthickness=0)
    entry_2.place(x=130.0, y=224.0, width=320.0, height=25.0)

    #Tel
    entry_tel = StringVar()
    entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(225.0, 313.0, image=entry_image_5)
    entry_5 = Entry(bd=0, bg="#FFFFFF", textvariable=entry_tel, highlightthickness=0)
    entry_5.place(x=130.0, y=302.0, width=198.0, height=25.0)

    #Email
    entry_email = StringVar()
    entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(473.0, 313.0, image=entry_image_6)
    entry_6 = Entry(bd=0, bg="#FFFFFF", textvariable=entry_email, highlightthickness=0)
    entry_6.place(x=358.0, y=302.0, width=236.0, height=25.0)

    #คำนำหน้าชื่อ
    radio_name_start = StringVar()
    mr = Radiobutton(window, text='Mr.', variable=radio_name_start, value="MR.")
    mr.place(x=175.0, y=188)
    ms = Radiobutton(window, text='Ms.', variable=radio_name_start, value="MS.")
    ms.place(x=235.0, y=188)
    miss = Radiobutton(window, text='Miss.', variable=radio_name_start, value="MISS.")
    miss.place(x=298.0, y=188)

    #Age
    entry_age = StringVar()
    entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(532.0, 236.0, image=entry_image_3)
    entry_3 = Entry(bd=0, bg="#FFFFFF", textvariable=entry_age, highlightthickness=0)
    entry_3.place(x=482.0, y=225.0, width=100.0,height=25.0)

    #Departure date
    entry_date_departure = StringVar()
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(497.0, 323+65, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#FFFFFF", textvariable=entry_date_departure, highlightthickness=0)
    entry_1.place( x=410.0, y=311+65, width=180.0, height=25.0)

    #Return date
    entry_date_return = StringVar()
    entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(497.0, 410+65, image=entry_image_4)
    entry_4 = Entry(bd=0, bg="#FFFFFF", textvariable=entry_date_return, highlightthickness=0)
    entry_4.place(x=410.0, y=399+65, width=180.0, height=25.0)

    #Time
    combo_time_start = StringVar()
    canvas.create_text(255.0, 279+65, anchor="nw", text="Time 🕒", fill="#000000",font=("Manrope Regular", 16 * -1))
    time = ttk.Combobox(window, textvariable=combo_time_start, values=list_time)
    time.current()
    time.place(x=250.0, y=311+65, width=117)

    combo_time_return = StringVar()
    canvas.create_text(255.0, 366+65, anchor="nw", text="Time 🕘", fill="#000000", font=("Manrope Regular", 16 * -1))
    time_return = ttk.Combobox(window, textvariable=combo_time_return, values=list_time)
    time_return.current()
    time_return.place(x=250.0, y=394+65, width=117)

    #Entry text
    canvas.create_text(122.0, 191.0, anchor="nw", text="Name️", fill="#000000", font=("Manrope Regular", 16 * -1))
    canvas.create_text(122.0, 270.0, anchor="nw", text="Tel.", fill="#000000", font=("Manrope Regular", 16 * -1))
    canvas.create_text(351.0, 270.0, anchor="nw", text="Email", fill="#000000", font=("Manrope Regular", 16 * -1))
    canvas.create_text(476.0, 191.0, anchor="nw", text="Age", fill="#000000", font=("Manrope Regular", 16 * -1))
    canvas.create_text(401.0, 279+65, anchor="nw", text="Departure date ", fill="#000000", font=("Manrope Regular", 16 * -1))
    canvas.create_text(515.0, 281+65, anchor="nw", text="( dd-mm-yyyy )", fill="#919191", font=("Manrope Regular", 12 * -1))
    canvas.create_text(401.0, 366+65, anchor="nw", text="Return date", fill="#000000", font=("Manrope Regular", 16 * -1))
    canvas.create_text(490.0, 368+65, anchor="nw", text="( dd-mm-yyyy )", fill="#919191", font=("Manrope Regular", 12 * -1))

    #Origin
    combo_origin = StringVar()
    canvas.create_text(122.0, 279+65, anchor="nw", text="Origin", fill="#000000", font=("Manrope Regular", 16 * -1))
    origin = ttk.Combobox(window, textvariable=combo_origin, values=list_airport)
    origin.current()
    origin.place(x=117.0, y=311+65, width=117)

    #Destination
    combo_destination = StringVar()
    canvas.create_text(122.0, 366+65, anchor="nw", text="Destination", fill="#000000", font=("Manrope Regular", 16 * -1))
    destination = ttk.Combobox(window, textvariable=combo_destination)
    destination.current()
    destination.place(x=117.0, y=394+65, width=117)

    #Class
    combo_class = StringVar()
    canvas.create_text(122.0, 449+65, anchor="nw", text="Class 💵", fill="#000000", font=("Manrope Regular", 16 * -1))
    class_airport = ttk.Combobox(window, textvariable=combo_class, values=list_class)
    class_airport.current()
    class_airport.place(x=117.0, y=477+65, width=117)

    #Seat
    combo_seat_chr = StringVar()
    canvas.create_text(255.0, 449+65, anchor="nw", text="Seat number", fill="#000000", font=("Manrope Regular", 16 * -1))
    seat_chr = ttk.Combobox(window, textvariable=combo_seat_chr)
    seat_chr.current()
    seat_chr.place(x=250.0, y=477+65, width=55)

    combo_seat_num = StringVar()
    seat_num = ttk.Combobox(window, textvariable=combo_seat_num, values=list_seat_num)
    seat_num.current()
    seat_num.place(x=250+55+7, y=477+65, width=55)

    #text fight booking
    canvas.create_text(108.0, 126.0, anchor="nw", text="Flight Booking", fill="#FFFFFF", font=("Manrope Regular", 16 * -1))


    #function ยอ่ย
    def check():
        '''ตรวจสอบข้อมูล และราคา'''
        # get data from inputs
        name_start = radio_name_start.get()
        name = entry_name.get()
        tel = entry_tel.get()
        email = entry_email.get()
        age = entry_age.get()
        date_departure = entry_date_departure.get()
        date_departure = date_departure.split('-')
        d_departure = "%02d.%02d.%s" %(int(date_departure[0]), int(date_departure[1]), date_departure[2][2:])
        date_return = entry_date_return.get()
        date_return = date_return.split('-')
        d_return = "%02d.%02d.%s" %(int(date_return[0]), int(date_return[1]), date_return[2][2:])
        origin = combo_origin.get()
        destination = combo_destination.get()
        seat_chr = combo_seat_chr.get()
        seat_num = combo_seat_num.get()
        seat = "%s%02d" %(seat_chr, int(seat_num))
        time_start = combo_time_start.get()
        time_return = combo_time_return.get()
        class_seat = combo_class.get()

        check_data = Tk()
        check_data.title('Check Information')

        def create_ticket():
            '''สร้างตั๋ว'''
            check_data.destroy()
            # draw images
            draw=ImageDraw.Draw(image_image_4)
            draw.text((703.0-673, 283.0-106), text="JKF", fill="#000000", font=ImageFont.truetype("Manrope-ExtraBold.ttf", 64))
            draw.text((920.0-673, 283.0-106), text="ROM", fill="#000000", font=ImageFont.truetype("Manrope-ExtraBold.ttf", 64 ))
            draw.text((715.0-673, 381.0-106), text="DATE", fill="#000000", font=ImageFont.truetype("Manrope-ExtraBold.ttf", 24))
            draw.text((801.0-673, 380.0-106), text="%s         %s" %(d_departure, d_return), fill="#0284B9", font=ImageFont.truetype("Manrope-Medium.ttf", 24))
            draw.text((801.0-673, 380.0-106), text="                       |", fill="#000000", font=ImageFont.truetype("Manrope-Medium.ttf", 24))
            draw.text((801.0-673, 423.0-106), text="%s       %s" %(time_start, time_return), fill="#0284B9", font=ImageFont.truetype("Manrope-Medium.ttf", 24)) # time
            draw.text((801.0-673, 423.0-106), text="                       |", fill="#000000", font=ImageFont.truetype("Manrope-Medium.ttf", 24))
            draw.text((716.0-673, 426.0-106), text="TIME", fill="#000000", font=ImageFont.truetype("Manrope-ExtraBold.ttf", 24))
            draw.text((715.0-673, 191.0-106), text="PASSENGER NAME", fill="#000000", font=ImageFont.truetype("Manrope-Regular.ttf", 10))
            draw.text((715.0-673, 210.0-106), text=name_start + " " + name.upper(), fill="#0284B9", font=ImageFont.truetype("Manrope-Regular.ttf", 16)) # passenger name
            draw.text((715.0-673, 237.0-106), text="FROM", fill="#000000", font=ImageFont.truetype("Manrope-Regular.ttf", 10))
            draw.text((716.0-673, 256.0-106), text=origin,fill="#0284B9",font=ImageFont.truetype("Manrope-Regular.ttf", 16)) # origin
            draw.text((898.0-673, 237.0-106), text="TO",fill="#000000",font=ImageFont.truetype("Manrope-Regular.ttf", 10))
            draw.text((898.0-673, 256.0-106), text=destination,fill="#0284B9",font=ImageFont.truetype("Manrope-Regular.ttf", 16)) # destination
            draw.text((727.0-673, 511.0-106), text="JR1103",fill="#FFFFFF",font=ImageFont.truetype("Manrope-ExtraBold.ttf", 24))
            draw.text((857.0-673, 511.0-106), text="R3",fill="#FFFFFF",font=ImageFont.truetype("Manrope-ExtraBold.ttf", 24))
            draw.text((955.0-673, 511.0-106), text=seat,fill="#FFFFFF",font=ImageFont.truetype("Manrope-ExtraBold.ttf", 24)) # seat 1
            draw.text((727.0-673, 541.0-106), text="RJ1503",fill="#FFFFFF",font=ImageFont.truetype("Manrope-ExtraBold.ttf", 24))
            draw.text((857.0-673, 541.0-106), text="J3",fill="#FFFFFF",font=ImageFont.truetype("Manrope-ExtraBold.ttf", 24))
            draw.text((955.0-673, 541.0-106), text=seat,fill="#FFFFFF",font=ImageFont.truetype("Manrope-ExtraBold.ttf", 24)) # seat 2
            draw.text((740.0-673, 483.0-106), text="FLIGHT",fill="#FFFFFF",font=ImageFont.truetype("Manrope-ExtraBold.ttf", 16))
            draw.text((853.0-673, 483.0-106), text="GATE",fill="#FFFFFF",font=ImageFont.truetype("Manrope-ExtraBold.ttf", 16))
            draw.text((958.0-673, 483.0-106), text="SEAT",fill="#FFFFFF",font=ImageFont.truetype("Manrope-ExtraBold.ttf", 16))
            draw.text((806.0-673, 124.0-106), text="PSIT Airline",fill="#FFFFFF",font=ImageFont.truetype("Manrope-ExtraBold.ttf", 24))
            #image_image_4.show()
            photo = ImageTk.PhotoImage(image_image_4)
            canvas.create_image(872.0,351.0,image=photo)
            canvas.create_image(x=670,y=100,image=photo)

        #เฟรมตรวจสอบข้อมูลที่กรอกมา
        labelframe = LabelFrame(check_data, text='Please check your information')
        labelprice = LabelFrame(check_data, text='Please check your flight')

        Label(labelframe, text='   Name').grid(row=1, column=0, pady=3, sticky=W)
        Label(labelframe, text=name_start+' '+name.upper()).grid(row=1, column=1, columnspan=2, pady=3, sticky=W)

        Label(labelframe, text='   Age').grid(row=2, column=0, pady=3, sticky=W)
        Label(labelframe, text=age+' years').grid(row=2, column=1, pady=3, sticky=W)

        Label(labelframe, text='   Tel').grid(row=3, column=0, pady=3, sticky=W)
        Label(labelframe, text=tel).grid(row=3, column=1, pady=3, sticky=W)

        Label(labelframe, text='   Email').grid(row=4, column=0, pady=3, sticky=W)
        Label(labelframe, text=email).grid(row=4, column=1, pady=3, sticky=W)

        Label(labelprice, text='   From').grid(row=0, column=0, pady=3, sticky=W)
        Label(labelprice, text=origin+' | '+time_start+' | '+d_departure).grid(row=0, column=1, pady=3, sticky=W)
        Label(labelprice, text='   To').grid(row=1, column=0, pady=3, sticky=W)
        Label(labelprice, text=destination+' | '+time_return+' | '+d_return).grid(row=1, column=1, pady=3,sticky=W)

        Label(labelprice, text='   Class').grid(row=2, column=0, pady=3, sticky=W)
        Label(labelprice, text=class_seat).grid(row=2, column=1, pady=3, sticky=W)

        Label(labelprice, text='   Seat').grid(row=3, column=0, pady=3, sticky=W)
        Label(labelprice, text=seat).grid(row=3, column=1, pady=3, sticky=W)

        labelframe.grid(row=0, column=0, padx=10, pady=5, ipadx=5, ipady=5)
        labelprice.grid(row=0, column=1, padx=10, pady=5, ipadx=5, ipady=5)

        Label(check_data, text='THB 1,250', font=("Manrope Blod", 46)).grid(sticky='news',row=1, column=0 , columnspan=2)
        label_button = Label(check_data)
        Button(label_button, text='Confirm', command=lambda: create_ticket()).grid(row=0, column=1, pady=5)
        Button(label_button, text='Cancel', command=lambda: check_data.destroy()).grid(row=0, column=0, pady=5)
        label_button.grid(row=2, column=0 , columnspan=2)

        check_data.resizable(False, False)
        check_data.mainloop()


    #change destination
    def change_dest(var, indx, mode):
        destination.set("")
        list_airport2 = list_airport[:]
        list_airport2.remove(combo_origin.get())
        destination.config(values=list_airport2)
    combo_origin.trace_add("write", change_dest)


    #change seat_char by class
    #list_class = ['First Class', 'Business Class', 'Economy Class']
    def change_seat(var, indx, mode):
        seat_chr.set("")
        if combo_class.get() == "First Class":
            seat_chr.config(values=list_seat_chr[:2])
        elif combo_class.get() == "Business Class":
            seat_chr.config(values=list_seat_chr[2:4])
        elif combo_class.get() == "Economy Class":
            seat_chr.config(values=list_seat_chr[4:])
    combo_class.trace_add("write", change_seat)

    #Button เอาไว้ล่างสุดเพราะมีการเรียกใช้ func ข้างบน
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_save = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: image_image_4.save('img3.png'), relief="flat")
    button_save.place(x=948.0, y=617.0, width=124.0, height=46.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_clear = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat")
    button_clear.place(x=363.0, y=617.0, width=124.0, height=46.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_check = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=check, relief="flat")
    button_check.place(x=511.0, y=617.0, width=124.0, height=46.0)

    window.resizable(False, False)
    window.mainloop()

booking()
