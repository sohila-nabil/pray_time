import requests
import tkinter as tk
from tkinter import ttk, messagebox

app = tk.Tk()
app.title('pray time')
app.geometry('360x300')


def pray(city, country):
    url = f'http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=8'
    
    try:
        response = requests.get(url)
        info = response.json()
        if 'data' in info:
            time = info['data']['timings']
            return time
        else:
            None
    except Exception as e:
        return f'un expected error {e}'
    
def gui_pray():
    city = city_entry.get()
    country = country_entry.get()

    if city and country:
       pray_timing = pray(city,country)
       for name, time in pray_timing.items():
           times.insert(tk.END, f'{name}:{time}')
    else:
        messagebox.showerror('error','enter correct city and country')


   


city_label = tk.Label(app, text='city')
city_label.grid(row=0, column=1)

city_entry = tk.Entry(app, text='city')
city_entry.grid(row=0, column=2, columnspan=2)

country_label = tk.Label(app, text='country')
country_label.grid(row=1, column=1, pady=5)

country_entry = tk.Entry(app)
country_entry.grid(row=1, column=2, pady=5, columnspan=2)

btn = tk.Button(app, text='pray time', bg='#6d6875', command=gui_pray)
btn.grid(row=2, column=2, columnspan=2)

times = tk.Listbox(app, height=15, width=45)
times.grid(row=3, column=2,columnspan=2, pady=5)





app.mainloop()




    
# city = input('enter the city')
# country = input('enter the country')

