import tkinter
from tkinter import font
from tkinter import ttk
from tkinter import *
import mysql.connector
from tabulate import tabulate
import matplotlib.pyplot as plt
from random import randint, randrange

# Ask for a State name, then run a query to extract actual stats through
# Python-SQL integration w/ GUI(Tkinter)

# Please enter database details at line 197 & 198 with other references in the code.

# Button Function Defintions
def conFirm():
  msg = '''CHOOSE                                 FROM                                 BELOW'''
  text_box = Text(root,height=1,width=50, font=("Bahnschrift SemiLight Condensed",18), bg='#e6ffff', borderwidth=0)
  text_box.pack(expand=True)
  text_box.insert('end', msg)
  text_box.config(state='disabled')
  confirm['state'] = 'disabled' # To avoid duplicate outputs for different inputs.

def showTable():
  # Fetching different columns.
  cursor.execute('SELECT srno FROM stat;')
  query1 = cursor.fetchall()
  srno = [] 
  for i in query1:
          srno.append(i[0])

  cursor.execute('SELECT state_ut FROM stat;')
  query2 = cursor.fetchall()
  name = [] 
  for j in query2:
          name.append(j[0])

  cursor.execute('SELECT confirmed_cases FROM stat;')
  query3 = cursor.fetchall()
  confirmed = [] 
  for k in query3:
          confirmed.append(k[0])

  cursor.execute('SELECT active_cases FROM stat;')
  query4 = cursor.fetchall()
  active = [] 
  for l in query4:
          active.append(l[0])

  cursor.execute('SELECT cured FROM stat;')
  query5 = cursor.fetchall()
  cured = [] 
  for m in query5:
          cured.append(m[0])

  cursor.execute('SELECT death FROM stat;')
  query6 = cursor.fetchall()
  death = [] 
  for n in query6:
          death.append(n[0])

  info = {'SR NO.': srno,
          'State/UT': name, 
          'Confirmed Cases': confirmed,
          'Active Cases' : active,
          'Cured':cured,
          'Deaths':death}

  print(tabulate(info, headers='keys', tablefmt='fancy_grid'))

  #Alert Window
  alert = tkinter.Tk()
  alert.title('Alert✅')
  alert.geometry('310x90')
  alert.configure(bg='white')
  text = "Check the Python Console."
  text1box = Text(alert,height=2,width=70, font=("Calibiri",10), borderwidth=0)
  text1box.pack(expand=True)
  text1box.insert('end', text)
  text1box.config(state='disabled')
  text1box.place(x = 70, y = 10)
  alert.mainloop()

def showGraph():
  # Query components, '%s' used to use python variables in the SQL query.
  query_1 = "SELECT active_cases,cured,death,confirmed_cases FROM stat WHERE state_ut = '%s';"
  query_2 = state_name.get()

  cursor.execute(query_1%(query_2))

  query_result = cursor.fetchone()
  result = list(query_result) #Converting to list for later assignment of the same.
  stats = result

# Graph Code 
  x_axis=['Active','Cured','Casualties','Confirmed Cases']
# Assigning the width and color.
  plt.figure(figsize=(15,4))
  plt.bar(x_axis,stats,width = 0.9, color = ['red', 'green','blue','violet'])
  plt.xticks(rotation=0)
# naming the x-axis
  plt.xlabel('CASES IN %s'%(state_name.get()))
# naming the y-axis
  plt.ylabel('CASE STATS in Lakhs')
# plot title
  plt.title('%s COVID-19 CASES                          *as on Aug 8, 2021'%(state_name.get()))
  plt.show()

def showPie():
  pie_search = "SELECT cured,death,confirmed_cases,active_cases FROM stat WHERE state_ut = '%s';"
  key = state_name.get()

  cursor.execute(pie_search%(key))
  result = cursor.fetchone()

  label_names = ['cured', 'death', 'confirmed', 'active']
  
# portion covered by each label
  slices = list(result)
  
# color for each label
  colors = ['g', 'r', 'b', 'y']
  
# plotting the pie chart
  plt.pie(slices, labels = label_names, colors=colors, 
          startangle=90, shadow = False, explode = (0, 0, 0, 0),
          radius = 1, autopct = '%1.1f%%')
  
# plotting legend
  plt.legend()
#title
  plt.title("%s COVID 19 Stats"%state_name.get())
  
# showing the plot
  plt.show()
#help window
def helpBox():
  helpB = tkinter.Tk()
  helpB.title('Help')
  helpB.geometry('1330x480')
  helpB.configure(bg='white')
  cursor.execute('SELECT state_ut FROM stat;')
  query = cursor.fetchall()
  name = [] 
  for j in query:
          name.append(j[0])
  str = "HOW TO USE THIS APP :\n\n1. Choose a name from from the drop down.\n2. Click on confirm.\n3. Select the desired form of representation.(Graph, Pie Chart, Table)\n4. The result will be displayed in a new window or Python Console depending on your Python distribution.\n"
  text_b = Text(helpB,height=30,width=84, font=("Corbel Light",22), bg='white', borderwidth=0)
  text_b.pack(expand=True)
  text_b.insert('end', str)
  text_b.config(state='disabled')
  text_b.place(x = 10, y = 10)
  helpB.mainloop()

#Easter Egg
def easterEgg():
  #Button Function Definition
  def jk():
    text_box = Text(eastegg,height=1,width=55, font=("Bahnschrift SemiLight Condensed",18), bg='#e6ffff', borderwidth=0)
    text_box.pack(expand=True, side=BOTTOM, anchor=SE)
    text_box.insert('end', "PS : Alexa had nothing to do with this, we made this app ourselves !")
    text_box.config(state='disabled')
    #Jokes
    bundle = [
      'Mother: “How Was School Today, Patrick?”\nPatrick: “It Was Really Great Mum! Today We Made Explosives!”\nMother: “Ooh, They Do Very Fancy Stuff With You These Days. And What Will You Do At School Tomorrow?”\nPatrick: “What School?”',
      'A potato was interrogated by cops. After 3 hours of torture, it gave in and said\n"Main batata hun, main batata hun"',
      'Did you know that you can cool yourself to -273.15˚C and still be 0K !',
      'Do not trust atoms,\nthey make up everything','Two chemists go into a restaurant.\nThe first one says "I think I will have an H2O."\nThe second one says "I think I will have an H2O too" -- and he died',
      'Q: What did the scientist say when he found 2 isotopes of helium?\nA: HeHe',
      'Lata: Is it right to punish someone for something they have not done?\nTeacher: Of course, not!\nLata: I have not done my homework.',
      '“I hate audio correct.”',
      'Did you hear about the college professor who was involved in a terrible car wreck?\nHe was grading papers on a curve',
      'Never lend money to a friend.\nIt is dangerous. It could damage his memory.',
      'God: You are going to power cars in the future\nDinosaurs: Cool! We are goin to drive!\nGod: Well no, you are going to be the fuel... ',
      'Friends pay restaurant bills on a de-tu-de basis.',
      'A photon checks into a hotel, where a bellhop asks where its suitcase is.\nThe photon replies, “I didn’t bring any luggage. I’m traveling light.”'] 

    jokeline = Text(eastegg, height=7,width=63, font=("Bahnschrift SemiLight Condensed",18), bg='#e6ffff', borderwidth=0)
    jokeline.pack(expand=True)
    jokeline.place(x=370,y=180)
    jokeline.insert('end', bundle[randrange(0,len(bundle))])
    joke['state'] = 'disabled'
  
  eastegg = tkinter.Tk()
  eastegg.title('Easter Egg')
  eastegg.configure(bg = '#e6ffff')
  eastegg.geometry('1330x480')
  joke = tkinter.Button(eastegg, text="Alexa 😜, Tell Me a Joke!",height = 2, width = 30, font=("Bahnschrift Condensed",16), bg='white', borderwidth=1, command = jk)
  joke.place(x=530,y=20)
  eastegg.mainloop()

# SQL Connection Code
# Connecting to the Database, where the records are stored.
cases_DB = mysql.connector.connect(
  host="localhost",
  user="root",
  password="", #Enter your Password, if applicable.
  database="csproj" #Enter the name of database.
)

cursor = cases_DB.cursor()

# GUI Code
root = tkinter.Tk()
root.title('REAL TIME COVID 19 STATS ~DEVELOPED by OM ARYAN and AMIT SIROHI')
root.geometry('1280x720')
root.configure(bg = '#e6ffff')

msg = "🩺💉 REAL TIME COVID 19 STATS 💉🩺"
text_box = Text(root,height=2,width=70, font=("Bahnschrift Condensed",26), bg='#e6ffff', borderwidth=0)
text_box.pack(expand=True)
text_box.insert('end', msg)
text_box.config(state='disabled')
text_box.place(x = 380, y = 90)

#Fetching data from DB for a function.
cursor.execute('SELECT state_ut FROM stat;')
query = cursor.fetchall()
name = [] 
for j in query:
          name.append(j[0])

# Taking Input
state_name = ttk.Combobox(root, values=name, font=("Calibiri",16))
state_name.place(x=440,y=200,width=310,height=55)

# Button Configurations
confirm = tkinter.Button(root, text="CONFIRM",height = 3, width = 20, bg='white',borderwidth=1,command = conFirm)
confirm.place(x=750, y=200)

help = tkinter.Button(root, text="Help",height = 1, width = 7, bg='#e6ffff', borderwidth=1, command = helpBox)
help.pack(side=TOP, anchor=NE)

easteregg = tkinter.Button(root, text="Don't Click Me",height = 1, width = 13, bg='#e6ffff', borderwidth=1, command=easterEgg)
easteregg.place(x=1130,y=0)

graph = tkinter.Button(root, text="Graph",height = 3, width = 20, bg='white', command = showGraph)
graph.place(x=80, y=550)

pie = tkinter.Button(root, text="Pie Chart",height = 3, width = 20, bg='white', command = showPie)
pie.place(x=550, y=550)

table = tkinter.Button(root, text="Tabular Stats",height = 3, width = 20, bg='white', command = showTable)
table.place(x=1000, y=550)

root.mainloop()
cases_DB.close() #Closing the SQL Connection
