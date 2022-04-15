# Importaciones
from tkinter import Button, Tk, Canvas, Label, Frame, Entry, Button, W, E, Listbox, END
from django.db import connection
import psycopg2

window = Tk()
window.title("Data Base")

#funcion para guardar datos del usuario
def save_new_user(name, surname, age, email, adress):
	conn = psycopg2.connect(
		dbname="postgres",
		user="postgres",
		password="123456p",
		host="localhost",
		port="5432",
	)
	cursor = conn.cursor()
	query = '''INSERT INTO Usuarios(name, surname, age, email, adress) VALUES (%s, %s, %s, %s, %s)'''
	cursor.execute(query, (name, surname, age, email, adress))
	print("Data saved")
	conn.commit()
	conn.close()
	#refrescar save_new_user
	display_user()

#funcion para mostrar datos del usuario
def display_user():
	conn = psycopg2.connect(
		dbname="postgres",
		user="postgres",
		password="123456p",
		host="localhost",
		port="5432",
	)
	cursor = conn.cursor()
	query = '''SELECT * FROM Usuarios'''
	cursor.execute(query)

	row = cursor.fetchall()

	listbox = Listbox(frame, width = 40, height = 10)
	listbox.grid(row = 10 , columnspan = 4, sticky = W + E)

	for x in row:
		listbox.insert(END, x)

	conn.commit()
	conn.close()

#buscar
def search(id):
	conn = psycopg2.connect(
		dbname="postgres",
		user="postgres",
		password="123456p",
		host="localhost",
		port="5432",
	)
	cursor = conn.cursor()
	query = '''SELECT * FROM Usuarios WHERE id=%s'''
	cursor.execute(query, (id))

	row = cursor.fetchone()

	print(row)

	display_search_result(row)

	conn.commit()
	conn.close()

#Mostrar los resultados de la busqueda
def display_search_result(row):
	listbox = Listbox(frame, width = 20, height = 1)
	listbox.grid(row=9, columnspan=4, sticky=W+E)
	listbox.insert(END, row)

# Canvas
canvas = Canvas(window, height=380, width=400)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text="add a user")
label.grid(row=0, column=1)

# Name
label = Label(frame, text="Name")
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

# Surname
label = Label(frame, text="Surname")
label.grid(row=2, column=0)

entry_surname = Entry(frame)
entry_surname.grid(row=2, column=1)

# Age
label = Label(frame, text="Age")
label.grid(row=3, column=0)

entry_age = Entry(frame)
entry_age.grid(row=3, column=1)

# Email
label = Label(frame, text="Email")
label.grid(row=4, column=0)

entry_email = Entry(frame)
entry_email.grid(row=4, column=1)

# Adress
label = Label(frame, text="Adress")
label.grid(row=5, column=0)

entry_adress = Entry(frame)
entry_adress.grid(row=5, column=1)

button = Button(frame, text="ADD", command=lambda: save_new_user(
	entry_name.get(),
	entry_surname.get(),
	entry_age.get(),
	entry_email.get(),
	entry_adress.get()
))
button.grid(row=6, column=1, sticky=W + E)

#Busqueda
label = Label(frame, text="Search Data")
label.grid(row=7, column=1)

label = Label(frame, text="Search By ID")
label.grid(row=8, column=0)

id_search = Entry(frame)
id_search.grid(row=8, column=1)

button = Button(frame, text="Search", command=lambda:search(id_search.get()))
button.grid(row=8, column=2)

display_user()

window.mainloop()