from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from room import Room
from tkinter import messagebox


class Cust_win():
    def __init__(self, root):
        self.root = root
        self.root.title("Office room booking system")
        self.root.geometry("1295x550+230+220")
        ########### variables ############################
        self.var_name = StringVar()
        self.var_surname = StringVar()
        self.var_email = StringVar()
        self.var_number = StringVar()
        self.var_address = StringVar()

        # title
        lbl_title = Label(
            self.root,
            text="ADD ORDERER DETAILS",
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
        img2 = Image.open(r"img_5.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbling = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbling.place(x=5, y=2, width=100, height=40)
        # frame
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
        #label and entry
        lbl_cus_name = Label(
            label_frame, text="ORDERER NAME", font=(
                "arial", 12, 'bold'))
        lbl_cus_name.grid(row=0, column=0, sticky=W)
        entry_name = Entry(
            label_frame,
            textvariable=self.var_name,
            font=(
                "times new roman",
                12,
                'bold'))
        entry_name.grid(row=0, column=1)
        ####
        lbl_cus_surname = Label(
            label_frame, text="ORDERER SURNAME", font=(
                "arial", 12, 'bold'))
        lbl_cus_surname.grid(row=1, column=0, sticky=W)
        entry_surname = Entry(
            label_frame, textvariable=self.var_surname, font=(
                "times new roman", 12, 'bold'))
        entry_surname.grid(row=1, column=1)
        ####
        lbl_cus_email = Label(
            label_frame, text="EMAIL", font=(
                "arial", 12, 'bold'))
        lbl_cus_email.grid(row=2, column=0, sticky=W)
        entry_email = Entry(
            label_frame, textvariable=self.var_email, font=(
                "times new roman", 12, 'bold'))
        entry_email.grid(row=2, column=1)
        ####
        lbl_cus_number = Label(
            label_frame, text="TELEPHONE NUMBER", font=(
                "arial", 12, 'bold'))
        lbl_cus_number.grid(row=3, column=0, sticky=W)
        entry_number = Entry(
            label_frame, textvariable=self.var_number, font=(
                "times new roman", 12, 'bold'))
        entry_number.grid(row=3, column=1)
        ####
        lbl_cus_address = Label(
            label_frame, text="ADDRESS", font=(
                "arial", 12, 'bold'))
        lbl_cus_address.grid(row=4, column=0, sticky=W)
        entry_address = Entry(
            label_frame, textvariable=self.var_address, font=(
                "times new roman", 12, 'bold'))
        entry_address.grid(row=4, column=1)
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
            fg="gold",
            bd=0,
            cursor="hand1",
            command=self.add_data,
            width=9,
            relief=RIDGE)
        add_btn.grid(row=0, column=0, padx=1)

        delete_btn = Button(
            buttonframe,
            text="DELETE",
            font=(
                "times new roman",
                14,
                'bold'),
            bg="black",
            fg="gold",
            bd=0,
            cursor="hand1",
            command=self.mdelete,
            width=9,
            relief=RIDGE)
        delete_btn.grid(row=0, column=1, padx=1)

        reset_btn = Button(
            buttonframe,
            text="RESET",
            font=(
                "times new roman",
                14,
                'bold'),
            bg="black",
            fg="gold",
            bd=0,
            cursor="hand1",
            command=self.reset,
            width=9,
            relief=RIDGE)
        reset_btn.grid(row=0, column=2, padx=1)

        next_btn = Button(
            buttonframe,
            text="NEXT",
            font=(
                "times new roman",
                14,
                'bold'),
            bg="black",
            fg="gold",
            bd=0,
            cursor="hand1",
            command=self.next_room,
            width=8,
            relief=RIDGE)
        next_btn.grid(row=0, column=3)
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
        tableframe.place(x=435, y=50, width=860, height=490)
        IbSearchBy = Label(
            tableframe,
            font=(
                "arial",
                12,
                "bold"),
            text="Search by: ",
            bg='red',
            fg="white")
        IbSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_Serach = ttk.Combobox(
            tableframe, textvariable=self.search_var, font=(
                "arial", 12, "bold"), width=24, state="readonly")
        combo_Serach["value"] = ("Name", "Number")
        combo_Serach.current(0)
        combo_Serach.grid(row=0, column=1, padx=2)

        self.txtsearch_var = StringVar()
        txtSearch = ttk.Entry(
            tableframe, textvariable=self.txtsearch_var, font=(
                "arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(
            tableframe,
            text="Search",
            command=self.search,
            font=(
                "arial",
                11,
                "bold"),
            bg="black",
            fg="gold",
            width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(
            tableframe,
            text="Show All",
            command=self.fetch_data,
            font=(
                "arial",
                11,
                "bold"),
            bg="black",
            fg="gold",
            width=10,
        )
        btnShowAll.grid(row=0, column=4, padx=1)
        #####Show###
        details_table = Frame(tableframe, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(
            details_table, column=(
                "name", "surname", "email", "number", "address"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("surname", text="Surname")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("number", text="Number")
        self.Cust_Details_Table.heading("address", text="address")
        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("surname", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("number", width=100)
        self.Cust_Details_Table.column("address", width=100)
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_number.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "All fileds are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    port='3306',
                    password="ksr2022704",
                    database="world")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into costumer value(%s,%s,%s,%s,%s)",
                    (self.var_name.get(),
                     self.var_surname.get(),
                     self.var_email.get(),
                     self.var_number.get(),
                     self.var_address.get(),
                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Succes", "orderer has been added")
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
        my_cursor.execute("select * from world.costumer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]
        self.var_name.set(row[0])
        self.var_surname.set(row[1])
        self.var_email.set(row[2])
        self.var_number.set(row[3])
        self.var_address.set(row[4])

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
            query = "delete from costumer where name=%s"
            value = (self.var_name.get(),)
            my_cursor.execute(query, value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_name.set(""),
        self.var_surname.set(""),
        self.var_email.set(""),
        self.var_number.set(""),
        self.var_address.set(""),

    def search(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            port='3306',
            password="ksr2022704",
            database="world")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from costumer where " +
                          str(self.search_var.get()) +
                          "LIKE'%" +
                          str(self.txtsearch_var.get()) +
                          "%s'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def next_room(self):
        self.new_window = Toplevel(self.root)
        self.app = Room(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Cust_win(root)
    root.mainloop()
