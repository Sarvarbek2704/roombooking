import os
import smtplib
from datetime import *
from email.message import EmailMessage
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from PIL import Image, ImageTk
from twilio.rest import Client


class Room():
    def __init__(self, root):
        self.root = root
        self.root.title("Office room booking system")
        self.root.geometry("1130x500+230+220")
        ########### variables ############################
        self.var_name = StringVar()
        self.var_bookdate = StringVar()
        self.var_roomnumber = StringVar()
        self.var_email = StringVar()
        self.var_number = StringVar()
        self.var_fromhour = StringVar()
        self.var_tohour = StringVar()

        # title
        lbl_title = Label(
            self.root,
            text="ADD ROOM DETAILS",
            font=(
                "times new roman",
                18,
                'bold'),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # logo
        img2 = Image.open(r"img_6.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)

        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbling = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbling.place(x=5, y=2, width=100, height=40)
        label_frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Orderer details",
            padx=2,
            font=(
                "times new roman",
                12,
                'bold'))
        label_frame.place(x=5, y=50, width=425, height=490)

        # label and entry
        lbl_cus_name = Label(
            label_frame, text="NAME ORDERER", font=(
                "arial", 12, 'bold'))
        lbl_cus_name.grid(row=0, column=0, sticky=W)
        entry_name = Entry(
            label_frame,
            textvariable=self.var_name,
            font=(
                "times new roman",
                12,
                'bold'))
        entry_name.grid(row=0, column=1, sticky=W)

        ####
        lbl_cus_date = Label(
            label_frame,
            text="BOOKING DATE(yyyy-mm-dd)",
            font=(
                "arial",
                12,
                'bold'))
        lbl_cus_date.grid(row=1, column=0, sticky=W)
        entry_date = Entry(
            label_frame,
            textvariable=self.var_bookdate,
            font=(
                "times new roman",
                12,
                'bold'))
        entry_date.grid(row=1, column=1, sticky=W)
        warning = Label(
            label_frame,
            font=(
                "arial",
                12,
                "bold"),
            text="Enter date correct(not past)!",
            bg='red',
            fg="white")
        warning.grid(row=8, column=0, sticky=W, padx=2)
        ####
        lbl_cus_surname = Label(
            label_frame, text="ORDER ROOM (1 to 5)", font=(
                "arial", 12, 'bold'))
        lbl_cus_surname.grid(row=2, column=0, sticky=W)
        combo_room = ttk.Combobox(
            label_frame, textvariable=self.var_roomnumber, font=(
                "arial", 12, 'bold'), state="readonly", width=16)
        combo_room["value"] = ("1", "2", "3", "4", "5",)
        combo_room.current(0)
        combo_room.grid(row=2, column=1, sticky=W)

        ####
        lbl_cus_time = Label(
            label_frame, text="TODAY:", font=(
                "arial", 12, 'bold'))
        lbl_cus_time.grid(row=7, column=0, sticky=W)
        entry_address = Label(
            label_frame,
            text=f"{datetime.now():%a, %b %d %Y}",
            fg="black",
            font=(
                "helvetica",
                15))
        entry_address.grid(row=7, column=1, sticky=W)

        ####
        lbl_cus_email = Label(
            label_frame, text="EMAIL", font=(
                "arial", 12, 'bold'))
        lbl_cus_email.grid(row=3, column=0, sticky=W)
        entry_email = Entry(
            label_frame, textvariable=self.var_email, font=(
                "times new roman", 12, 'bold'))
        entry_email.grid(row=3, column=1, sticky=W)

        ####
        lbl_cus_number = Label(
            label_frame, text="TELEPHONE NUMBER", font=(
                "arial", 12, 'bold'))
        lbl_cus_number.grid(row=4, column=0, sticky=W)
        entry_number = Entry(
            label_frame, textvariable=self.var_number, font=(
                "times new roman", 12, 'bold'))
        entry_number.grid(row=4, column=1, sticky=W)
        #####clock from#####
        clocklabelfrom = Label(
            label_frame,
            font=(
                "arial",
                12,
                "bold"),
            text="START FROM(9:30)")
        clocklabelfrom.grid(row=5, column=0, sticky=W)
        fromclock = Entry(
            label_frame,
            textvariable=self.var_fromhour,
            font=(
                "times new roman",
                12,
                'bold'))
        fromclock.grid(row=5, column=1, padx=1, sticky=W)

        #####clock to#####
        clocklabelfrom = Label(
            label_frame,
            font=(
                "arial",
                12,
                "bold"),
            text="UNTIL TO(23:30)")
        clocklabelfrom.grid(row=6, column=0, sticky=W)
        fromclock = Entry(
            label_frame,
            textvariable=self.var_tohour,
            font=(
                "times new roman",
                12,
                'bold'))
        fromclock.grid(row=6, column=1, padx=1, sticky=W)

        #### button #####
        buttonframe = Frame(self.root, bd=2, relief=RIDGE)
        buttonframe.place(x=0, y=400, width=412, height=40)

        add_btn = Button(
            buttonframe,
            text="ADD",
            font=(
                "times new roman",
                14,
                'bold'),
            bg="black",
            command=self.add_data,
            fg="gold",
            bd=0,
            cursor="hand1",
            width=12,
            relief=RIDGE)
        add_btn.grid(row=0, column=0, padx=1)

        delete_btn = Button(
            buttonframe,
            text="DELETE",
            command=self.mdelete,
            font=(
                "times new roman",
                14,
                'bold'),
            bg="black",
            fg="gold",
            bd=0,
            cursor="hand1",
            width=13,
            relief=RIDGE)
        delete_btn.grid(row=0, column=1, padx=1)

        reset_btn = Button(
            buttonframe,
            text="RESET",
            command=self.reset,
            font=(
                "times new roman",
                14,
                'bold'),
            bg="black",
            fg="gold",
            bd=0,
            cursor="hand1",
            width=12,
            relief=RIDGE)
        reset_btn.grid(row=0, column=2, padx=1)

        #### tabel frame ###
        tableframe = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="View details",
            padx=2,
            font=(
                "times new roman",
                12,
                'bold'))
        tableframe.place(x=435, y=50, width=750, height=490)

        details_table = Frame(tableframe, bd=2, relief=RIDGE)
        details_table.place(x=0, y=0, width=650, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_room_Table = ttk.Treeview(
            details_table,
            column=(
                "name",
                "date",
                "rnumber",
                "email",
                "number",
                "fromhour",
                "tohour"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.cust_room_Table.xview)
        scroll_y.config(command=self.cust_room_Table.yview)
        self.cust_room_Table.heading("name", text="Name")
        self.cust_room_Table.heading("date", text="Book date")
        self.cust_room_Table.heading("rnumber", text="Room number")
        self.cust_room_Table.heading("email", text="Email")
        self.cust_room_Table.heading("number", text="Number")
        self.cust_room_Table.heading("fromhour", text="Start from hour")
        self.cust_room_Table.heading("tohour", text="Until hour")
        self.cust_room_Table["show"] = "headings"

        self.cust_room_Table.column("name", width=100)
        self.cust_room_Table.column("date", width=100)
        self.cust_room_Table.column("rnumber", width=100)
        self.cust_room_Table.column("email", width=100)
        self.cust_room_Table.column("number", width=100)
        self.cust_room_Table.column("fromhour", width=100)
        self.cust_room_Table.column("tohour", width=100)
        self.cust_room_Table.pack(fill=BOTH, expand=1)
        self.cust_room_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def email_alert(subject, body, to):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to

        user = "roombooking@gmail.com"
        msg['from'] = user
        password = "qwertyuiop12345"

        server = smtplib.SMTP("smpt.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()

    def add_data(self):
        if self.var_bookdate.get() == "" or self.var_roomnumber.get() == "":
            messagebox.showerror(
                "Error", "All fileds are required or booking date is incorrect")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    port='3306',
                    password="ksr2022704",
                    database="world")
                my_empty = conn.cursor()
                my_empty.execute("Select bookdate from world.room")
                date = my_empty.fetchall()
                if date is None:
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "insert into room value(%s,%s,%s,%s,%s,%s,%s)",
                        (self.var_name.get(),
                         self.var_bookdate.get(),
                         self.var_roomnumber.get(),
                         self.var_email.get(),
                            self.var_number.get(),
                            self.var_fromhour.get(),
                            self.var_tohour.get(),
                         ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo(
                        "Succes",
                        "Booking room  has been added. Wait our email and telephone notification")
                    # send email
                    self.email_alert("You ordered N" +
                                     str(self.var_roomnumber.get()) +
                                     " room from " +
                                     str(self.var_fromhour.get()) +
                                     " until " +
                                     str(self.var_tohour.get()) +
                                     " clock on " +
                                     str(self.var_bookdate.get()) +
                                     " date.Thank you for your attention", "" +
                                     str(self.var_email.get()) +
                                     "")
                    # send message
                    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
                    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
                    client = Client(account_sid, auth_token)
                    client.messages.create(to=os.environ["" +
                                                         str(self.var_number) +
                                                         ""], from_="+123456789", body="You ordered N" +
                                           str(self.var_roomnumber.get()) +
                                           " room from " +
                                           str(self.var_fromhour.get()) +
                                           " until " +
                                           str(self.var_tohour.get()) +
                                           " clock on " +
                                           str(self.var_bookdate.get()) +
                                           " date.Thank you for your attention")
                else:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        port='3306',
                        password="ksr2022704",
                        database="world")
                    my_date = conn.cursor()
                    my_date.execute("select * from world.room where roomnumber='" +
                                    str(self.var_roomnumber.get()) +
                                    "' and bookdate='" +
                                    str(self.var_bookdate.get()) +
                                    "' and ((CAST('" +
                                    str(self.var_fromhour.get()) +
                                    "' as time) between timefrom and timeto) or "
                                    "CAST('" +
                                    str(self.var_tohour.get()) +
                                    "' as time) between timefrom and timeto or "
                                    "(CAST(timefrom as time) between '" +
                                    str(self.var_fromhour.get()) +
                                    "' and '" +
                                    str(self.var_tohour.get()) +
                                    "') or "
                                    "(CAST(timeto as time) between '" +
                                    str(self.var_fromhour.get()) +
                                    "' and '" +
                                    str(self.var_tohour.get()) +
                                    "'))")
                    result = my_date.fetchone()
                    if result is None:
                        my_cursor = conn.cursor()
                        my_cursor.execute(
                            "insert into room value(%s,%s,%s,%s,%s,%s,%s)",
                            (self.var_name.get(),
                             self.var_bookdate.get(),
                                self.var_roomnumber.get(),
                                self.var_email.get(),
                                self.var_number.get(),
                                self.var_fromhour.get(),
                                self.var_tohour.get(),
                             ))
                        conn.commit()
                        conn.close()
                        messagebox.showinfo(
                            "Succes",
                            "Booking room  has been added. Wait our email and telephone notification")
                        # send email
                        self.email_alert("You ordered N" +
                                         str(self.var_roomnumber.get()) +
                                         " room from " +
                                         str(self.var_fromhour.get()) +
                                         " until " +
                                         str(self.var_tohour.get()) +
                                         " clock on " +
                                         str(self.var_bookdate.get()) +
                                         " date.Thank you for your attention", "" +
                                         str(self.var_email.get()) +
                                         "")
                        # send message
                        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
                        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
                        client = Client(account_sid, auth_token)
                        client.messages.create(to=os.environ["" +
                                                             str(self.var_number) +
                                                             ""], from_="+123456789", body="You ordered N" +
                                               str(self.var_roomnumber.get()) +
                                               " room from " +
                                               str(self.var_fromhour.get()) +
                                               " until " +
                                               str(self.var_tohour.get()) +
                                               " clock on " +
                                               str(self.var_bookdate.get()) +
                                               " date.Thank you for your attention")
                    else:
                        messagebox.showinfo(
                            "Booking room has been added by other orderer ", result)
            except Exception as es:
                messagebox.showwarning("Warning", f"smt went wrong:{str(es)}")

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            port='3306',
            password="ksr2022704",
            database="world")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from world.room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_room_Table.delete(*self.cust_room_Table.get_children())
            for i in rows:
                self.cust_room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.cust_room_Table.focus()
        content = self.cust_room_Table.item(cursor_row)
        row = content["values"]
        self.var_name.set(row[0])
        self.var_bookdate.set(row[1])
        self.var_roomnumber.set(row[2])
        self.var_email.set(row[3])
        self.var_number.set(row[4])
        self.var_fromhour.set(row[5])
        self.var_tohour.set(row[6])

    def mdelete(self):
        mdelete = messagebox.askyesno(
            "?", "Do you want to delete this costumer?", parent=self.root)
        if mdelete > 0:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                port='3306',
                password="ksr2022704",
                database="world")
            my_cursor = conn.cursor()
            query = "delete from room where bookdate=%s"
            value = (self.var_bookdate.get(),)
            my_cursor.execute(query, value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_name.set(""),
        self.var_bookdate.set(""),
        self.var_roomnumber.set(""),
        self.var_email.set(""),
        self.var_number.set(""),
        self.var_fromhour.set(""),
        self.var_tohour.set(""),


if __name__ == "__main__":
    root = Tk()
    obj = Room(root)
    root.mainloop()
