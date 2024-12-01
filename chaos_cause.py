import pandas as pd
import folium,os
from cProfile import label
from cgitb import text
from logging import root
from tkinter import  *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import requests
import tkinter.messagebox
import tkinter as tk
from tkinter.font import Font
import tkinter.messagebox as msg
import pickle
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import numpy as np
import matplotlib.pyplot  as plot
import pandas as pa
import csv
import tkinter.messagebox as tkMessageBox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

show = "all"

class Node:
    def __init__(self, data=None):
        self.head = data
        self.id = 0
        self.next = None
        self.prev = None

class Doubly_linklist:     #class to store data 
    def __init__(self):
       self.head = None
       self.tail = None
       self.id = 0  
    def append(self,data):

        new_node = Node(data)
        self.id = self.id + 1        
        new_node.id = self.id
        if self.head is None:

            self.head = new_node
            self.tail = new_node
            return      
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node    
    def delete(self,data):
        if(self.head is None):
            print("List is empty")
            return    
        if(self.head.value[0] == data):
            self.head = self.head.next
            self.id = self.id - 1
            return
        if(self.tail.value[0] == data):
            self.tail = self.tail.prev
            self.tail.next = None
            self.id = self.id - 1
            return
        temp_1= self.head  
        prev = None
        while(temp_1 is not None):
            if(temp_1.value[0] == data):
                temp_1.next.prev = prev
                prev.next = temp_1.next
                self.id = self.id - 1
                print("Deleted Successfuly")
                return
            prev = temp_1
            temp_1 = temp_1.next
        print("Sorry not found ")    
    def display(self):
        temp = self.head
        while(temp is not None):
            print(temp.value)
            temp = temp.next
L = Doubly_linklist()



root=Tk()
my_img=ImageTk.PhotoImage(Image.open("proposal.jpg"))  #image insertion for home page
my_label=Label(image=my_img)
my_label.pack()
    

def main_page():      #function for dispalying home page
   
   def tab2():        #nested function  for page at back of home page
   
      button_get_started.destroy() # destroying button of home page
      my_label.destroy()           #destroying image of main page so that page defuned in nested functon could be displayed
      data_entry()                 #this will displat data entry page 
   root.title('Tourism Disaster Managment System')
   root.geometry('1000x500')
   
    

   button_get_started=Button(root,text="Get Started",height=3,width=15,bg="white",fg="black",activebackground="grey",font="Ariel",command=tab2)
   button_get_started.place(x=200,y=520,)
    
main_page()








def data_entry():      # this function will take input from user about situation of location 
    root.maxsize(width=700,height=360)
    root.minsize(width=700,height=360)
    frame_header = ttk.Frame(root)
    frame_header.pack()
    
    global entry_name
    global entry_number
    global entry_contact
    global entry_conditions
    global entry_aid
    global entry_road
    global entry_damage
    global entry_weather
    

    headerlabel = ttk.Label(frame_header, text= 'Disaster Management System', foreground='black',font=('Times New Roman', 22))
    
    headerlabel.grid(row=0, column=2)
    messagelabel = ttk.Label(frame_header,text='PLEASE TELL US ABOUT THE INCIDENT ',foreground='purple', font=('Arial', 12))
    
    messagelabel.grid(row=1, column=2)
    
    frame_content = ttk.Frame(root)
    frame_content.pack()
    
    name = StringVar()
    contact = StringVar()
    number_cas= StringVar()
    conditions= StringVar()
    aid= StringVar()
    road= StringVar()
    damage= StringVar()
    weather= StringVar()
    
    namelabel = ttk.Label(frame_content, text='Name')
    namelabel.grid(row=0, column=0, padx=5, sticky='sw')
    entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 12), textvariable=name)
    entry_name.grid(row=1, column=0)
    
    namelabel = ttk.Label(frame_content, text='Number Of Casualties')
    namelabel.grid(row=2, column=0, padx=6, sticky='sw')
    entry_number = ttk.Entry(frame_content, width=18, font=('Arial', 12), textvariable=contact)
    entry_number.grid(row=3, column=0)
    
    emaillabel = ttk.Label(frame_content, text='Contact')
    emaillabel.grid(row=0, column=1, sticky='sw')
    entry_contact = ttk.Entry(frame_content, width=18, font=('Arial', 12), textvariable=number_cas)
    entry_contact.grid(row=1, column=1)
    
    emaillabel = ttk.Label(frame_content, text='Medical Conditions')
    emaillabel.grid(row=2, column=1, sticky='sw')
    entry_conditions = ttk.Entry(frame_content, width=18, font=('Arial', 12), textvariable=conditions)
    entry_conditions.grid(row=3, column=1)
    
    namelabel = ttk.Label(frame_content, text='Transporation Aid')
    namelabel.grid(row=4, column=0, padx=6, sticky='sw')
    entry_aid = ttk.Entry(frame_content, width=18, font=('Arial', 12), textvariable=aid)
    entry_aid.grid(row=5, column=0)
    
    emaillabel = ttk.Label(frame_content, text='Condition Of Roads')
    emaillabel.grid(row=4, column=1, sticky='sw')
    entry_road = ttk.Entry(frame_content, width=18, font=('Arial', 12), textvariable=road)
    entry_road.grid(row=5, column=1)
    
    namelabel = ttk.Label(frame_content, text='Damaged Properties')
    namelabel.grid(row=6, column=0, padx=6, sticky='sw')
    entry_damage = ttk.Entry(frame_content, width=18, font=('Arial', 12), textvariable=damage)
    entry_damage.grid(row=7, column=0)
    
    emaillabel = ttk.Label(frame_content, text='Weather Conditions')
    emaillabel.grid(row=6, column=1, sticky='sw')
    entry_weather = ttk.Entry(frame_content, width=18, font=('Arial', 12), textvariable=weather)
    entry_weather.grid(row=7, column=1)

 
    
    def clear():    #function to clear data entered by user

        messagebox.showinfo(title='clear', message='Do you want to clear?')
        name.set("")
        contact.set("")
        number_cas.set("")
        conditions.set("")
        aid.set("")
        road.set("")
        damage.set("")
        weather.set("")

    def submit():      #dunction to submit data entered by user about the location
        global L
        entry_name1=entry_name.get()
        entry_number1=entry_number.get()
        entry_contact1=entry_contact.get()
        entry_conditions1=entry_conditions.get()
        entry_aid1=entry_aid.get()
        entry_road1=entry_road.get()
        entry_damage1=entry_damage.get()
        entry_weather1=entry_weather.get()

        if entry_name1=='' or entry_number1==''or entry_contact1=='' or entry_conditions1==''or entry_aid1=='':
            tkMessageBox.showinfo("Warning","fill the empty field!!!")
        else:  # appending data to linked list and then storing that data from linked_list to csvfile
        
            data = (entry_name1,entry_contact1,entry_number1,entry_conditions1,entry_aid1, entry_road1, entry_damage1, entry_weather1)
            L.append(data)
            header=("name", "contact", "number_cas", "conditions","aid","road", "damage", "weather")
            with open('linked_list.csv', 'w', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow(data)

            tkMessageBox.showinfo("Message","Stored successfully")
         
            messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
            clear()



    submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=11, column=0, sticky='e')
    clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=11, column=1, sticky='w')
    Hazardbutton = ttk.Button(frame_content, text='Hazard', command=map1).grid(row=16, column=4, sticky='w')
    Hazardbutton = ttk.Button(frame_content, text='Regression',command=regression).grid(row=17, column=4, sticky='w')


def regression():        # regression module which actually gives the graphical representation of hazards of entered locations

   from scipy import stats

   pd = pa.read_csv("locations.csv")
   features = pd["latitude"]
   labels = pd["longitude"]

    # r - relationship
   slope, intercept, r, p, std_err = stats.linregress(features, labels)

   def lineFunc(x):
      return slope * x + intercept
   x=map(lineFunc, features)
   #lineY = list(map(lineFunc, features))
   lineY = list(x)
   print(lineY)

   plot.scatter(features,labels)
   plot.plot(features,lineY)
   plot.show()

   speedY = lineFunc(6)
   print(speedY)



def map1():    #module to display locations marked as disaster place or not

   try:
      os.remove('world_empty.html')
   except:
      print("A1")

   locations=pd.read_csv('locations.csv')
   print(locations.head())
   print(locations.shape)
   def select_marker_color(row):
      if row['Hazard'] == 'yes':   #Red loction marker tells that disaster occurred at that location
         return 'red'
      elif row['Hazard'] == 'no':    #green loction marker tells that location is not in danger
         return 'green'
      return 'blue'
   locations['colors'] = locations.apply(select_marker_color, axis=1)


   file = folium.Map(
      zoom_start=2,
      location=[33.6844, 73.0479])
   for _, city in locations.iterrows():
      folium.Marker(
      location=[city['latitude'], city['longitude']],
      popup=city['name'],
      tooltip=city['name'],
      icon=folium.Icon(color=city['colors'], prefix='fa', icon='circle')).add_to(file)




   file.save('world_empty.html')
   print(locations.head)

   os.startfile('world_empty.html')

def weather_cond():     # moudle tells about weather conditions of any city/place of disaster you wan to check
   def weatherofthecity(weather):


      try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = int(weather['main']['temp'] - 273)  

        display_str = 'City: %s \nConditions: %s \nTemperature(‎°C): %s ' % (name, desc, temp)  
      except:
        display_str = '''Sorry!
        The city could not be found, Please try again or enter correct spellings!'''  
      return display_str
      def displayweatherofthecity(city):

         weather_key = '14ed2a78adcbcbfe1ac9d1ffb8c5eea6'  # api key we generated
         url = 'https://api.openweathermap.org/data/2.5/weather'  # opening url calling api
         params = {'APPID': weather_key, 'q': city}
         weather_response = requests.get(url, params=params)
         weather = weather_response.json()
         label['text'] = weatherofthecity(weather)
   def closethedisplaywindow():

      closeapp = tkinter.messagebox.askyesno("Chaos Cause", "Do you want to exit?")
      if closeapp > 0:

         base.destroy()
         return
   def functionforstructure():


      functionforstructure = tkinter.messagebox.showinfo(title="DSA Project-CHAOS CAUSE")
      HEIGHT, WIDTH = 500, 500
      canvas = Canvas(base, height=HEIGHT, width=WIDTH)
      canvas.pack()
      menubar = Menu(base)
      base.configure(menu=menubar)
      submenu1 = Menu(menubar)
      submenu2 = Menu(menubar)
      menubar.add_cascade(label="File", menu=submenu1)
      submenu1.add_command(label="Exit", command=closethedisplaywindow)
      frame = Frame(base, bg='green', bd=5)
      frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
      entry = Entry(frame, font=('Times new roman', 15))
      entry.place(relwidth=0.65, relheight=1)
      button = Button(frame, text="See Weather", font=('Times new roman', 12), command=lambda: displayweatherofthecity(entry.get()))
      button.place(relx=0.7, relwidth=0.3, relheight=1)
      lower_frame = Frame(base, bg='green', bd=10)
      lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
      label = Label(lower_frame, background="white", font=('Times New Roman', 18))
      label.place(relwidth=1, relheight=1)   

base = Tk()   # new window to input needs on the loction of disaster
base.title("DSA Group Project- Weather Conditions ")
def weatherofthecity(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = int(weather['main']['temp'] - 273)  

        display_str = 'City: %s \nConditions: %s \nTemperature(‎°C): %s ' % (name, desc, temp)  
    except:
        display_str = '''Sorry!
        The city could not be found, Please try again or enter correct spellings!'''  
    return display_str
def displayweatherofthecity(city):
    weather_key = '14ed2a78adcbcbfe1ac9d1ffb8c5eea6'  # api key we generated
    url = 'https://api.openweathermap.org/data/2.5/weather'  # opening url calling api
    params = {'APPID': weather_key, 'q': city}
    weather_response = requests.get(url, params=params)
    weather = weather_response.json()
    label['text'] = weatherofthecity(weather)
def closethedisplaywindow():
    closeapp = tkinter.messagebox.askyesno("Chaos Cause", "Do you want to exit?")
    if closeapp > 0:
        base.destroy()
        return
def functionforstructure():
    functionforstructure = tkinter.messagebox.showinfo(title="DSA Project-CHAOS CAUSE")
HEIGHT, WIDTH = 500, 500
canvas = Canvas(base, height=HEIGHT, width=WIDTH)
canvas.pack()
menubar = Menu(base)
base.configure(menu=menubar)
submenu1 = Menu(menubar)
submenu2 = Menu(menubar)
menubar.add_cascade(label="File", menu=submenu1)
submenu1.add_command(label="Exit", command=closethedisplaywindow)
frame = Frame(base, bg='green', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
entry = Entry(frame, font=('Times new roman', 15))
entry.place(relwidth=0.65, relheight=1)
button = Button(frame, text="See Weather", font=('Times new roman', 12), command=lambda: displayweatherofthecity(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)
lower_frame = Frame(base, bg='green', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
label = Label(lower_frame, background="white", font=('Times New Roman', 18))
label.place(relwidth=1, relheight=1)
base.mainloop()






def add_item():  

	item_to_add = add_item_variable.get()
	if item_to_add:
		listbox.insert(tk.END, item_to_add)
		add_item_input.delete(0, tk.END)
	else:
		msg.showwarning("Warning", "Please enter a item that you require in emergency!")

def delete_item():
	try:
		item_to_delete = listbox.curselection()[0]
		listbox.delete(item_to_delete)
	except IndexError:
		msg.showwarning("Warning", "Please select a item to delete")


def save_items():
	items = listbox.get(0, listbox.size())
	if items:
		pickle.dump(items, open("item.dat", 'wb'))
	else:
		msg.showwarning("Warning", "no item to save!")


def load_item():
	try:
		items = pickle.load(open("item.dat", 'rb'))
		if items:
			for item in items:
				listbox.insert(tk.END, item)
		else:	
			msg.showwarning("Warning", "no item to load!")
	except:
		msg.showwarning("Warning", "item.dat does not exist")




window = tk.Tk()
window.title("Emergency Items List")

my_font = Font(
    weight="bold",
    family="monospace",
    size=15
)

listbox = tk.Listbox(window, height=20, width=50, selectbackground="green", font=my_font)
listbox.pack(fill=tk.BOTH, expand=True)

entry_frame = tk.Frame(window)
entry_frame.pack(expand=True, fill=tk.BOTH)

add_item_variable = tk.StringVar()

add_item_input = tk.Entry(entry_frame, width=39, textvariable=add_item_variable, font=my_font)
add_item_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
add_item_input.focus()

add_item_btn = tk.Button(entry_frame, text="add item", bg="green", command=add_item)
add_item_btn.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

del_item_btn = tk.Button(window, width=48, text="delete item", bg="green", command=delete_item)
del_item_btn.pack(expand=True, fill=tk.BOTH)

save_items_btn = tk.Button(window, width=48, text="save item", bg="green", command=save_items)
save_items_btn.pack(expand=True, fill=tk.BOTH)

window.mainloop()




root = Tk()
root.maxsize(width=900,height=700)
root.minsize(width=700,height=500)
frame_header = ttk.Frame(root)
frame_header.pack()
headerlabel = ttk.Label(frame_header, text= 'Emergency Contacts', foreground='black',font=('Times New Roman', 22))
headerlabel.grid(row=0, column=2)

messagelabel = ttk.Label(frame_header,text="",foreground='purple', font=('Arial', 10))
messagelabel.grid(row=1, column=2)
frame_content = ttk.Frame(root)
frame_content.pack()
def Hospital():

    v1 = pdf.ShowPdf()

 

    v2 = v1.pdf_view(root,

                 pdf_location = r"C:\Users\USER\Desktop\DSA project\Hospital-List-05-09-2017 (1).pdf",  

                 width = 75, height = 60)

 

 

    v2.pack()

def Emergency():

    v3 = pdf.ShowPdf()

 

    v4 = v3.pdf_view(root,

                 pdf_location = r"C:\Users\USER\Desktop\DSA project\contacts.pdf",

                 width = 75, height = 60)

 

    v4.pack()

   

   

Hospitalbutton = ttk.Button(frame_content, text='Hospital List', command=Hospital).grid(row=11, column=0, sticky='e')
Emergencybutton = ttk.Button(frame_content, text='Landlines', command=Emergency).grid(row=11, column=1, sticky='w')



mainloop()


root.mainloop()