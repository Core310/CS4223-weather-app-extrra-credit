import configparser
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import threading
import requests
import datetime
import pytz
from timezonefinder import TimezoneFinder
import os
from io import BytesIO

# Get the absolute path of the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

WEATHER_THEMES = {
    "Clear": {"bg": "#FFD700", "suggestion": "It's a sunny day! Perfect for a walk."},
    "Clouds": {"bg": "#B0C4DE", "suggestion": "A bit cloudy, but still a good day."},
    "Rain": {"bg": "#4682B4", "suggestion": "Don't forget your umbrella!"},
    "Drizzle": {"bg": "#778899", "suggestion": "Light rain, a jacket would be nice."},
    "Snow": {"bg": "#FFFAFA", "suggestion": "Snowfall! Time to build a snowman."},
    "Thunderstorm": {"bg": "#2F4F4F", "suggestion": "Stormy weather, stay indoors if possible."},
    "Haze": {"bg": "#F0E68C", "suggestion": "Hazy day, take care."},
    "Mist": {"bg": "#E6E6FA", "suggestion": "Misty morning, drive safe."},
    "Night": {"bg": "#2C3E50", "suggestion": "Clear night sky. Have a restful evening."},
    "default": {"bg": "#FFFFFF", "suggestion": ""}
}

'''Author: prathamesh Dhande
If you find any error in this code then you can contact me prathameshdhande534@gmail.com'''  

class Weather(Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry("800x600")
        try:
            icon_path = os.path.join(BASE_DIR, "Images/weather_icon.ico")
            self.icon_img = ImageTk.PhotoImage(Image.open(icon_path))
            self.iconphoto(False, self.icon_img)
        except Exception as e:
            print(f"Warning: Could not load icon: {e}")
        self.resizable(False,False)
        self.config(bg=WEATHER_THEMES["default"]["bg"])
        self.forecast_items = [] # Store forecast labels for clearing
        self.__gui()
        
    def __gui(self):
       # ... (rest of search bar and existing UI) ...
       # (I will use a larger replacement below for the full __gui update)

       # placing the black border for search
       self.img=Image.open(os.path.join(BASE_DIR, "Images/black_border.png"))
       self.resizeimg=self.img.resize((275,35))
       self.finalimg=ImageTk.PhotoImage(self.resizeimg)
       Label(self, image=self.finalimg, bg=self.cget("bg")).place(x=20,y=20)
       
       # creating the search button
       self.img1=Image.open(os.path.join(BASE_DIR, "Images/search_btn.png"))
       self.resizeim1=self.img1.resize((29,29))
       self.finalimg1=ImageTk.PhotoImage(self.resizeim1)
       self.b1=Button(self, image=self.finalimg1,bg="black",command=self.threading)
       self.b1.place(x=297,y=22)
       self.bind("<Return>",self.threading)
     
       # creating the search textbox
       self.search=StringVar()
       self.search_textbox=Entry(self, textvariable=self.search,font=("Segoe UI",14,'bold'),width=24,justify="center",relief="flat")
       self.search_textbox.place(x=25,y=25)

       # creating the current weather label to display the city name and city time
       Label(self, text="Current Weather :",font='Arial 14 bold',fg="red", bg=self.cget("bg")).place(x=590,y=7)

       # location image logo
       self.img2=Image.open(os.path.join(BASE_DIR, 'Images/location.png'))
       self.resizeimg2=self.img2.resize((20,20))
       self.finalimg2=ImageTk.PhotoImage(self.resizeimg2)
       Label(self, image=self.finalimg2, bg=self.cget("bg")).place(x=595,y=36)

       # location label 
       self.location=Label(self, text='',font='Calibri 15', bg=self.cget("bg"))
       self.location.place(x=620,y=34)

       # time label for the searched city
       self.timelbl=Label(self, text="",font=("Cambria",16), bg=self.cget("bg"))
       self.timelbl.place(x=590,y=60)

       # creating the label for the logo according to main
       self.icons = Label(self, bg=self.cget("bg"))
       self.icons.place(x=70,y=110)
       self.set_image("main.png")

       # creating the label to display the temperature
       self.temperature=Label(self, text="",font=("Cambria",75,'bold'), bg=self.cget("bg"))
       self.temperature.place(x=270,y=140)
       self.degree=Label(self, text="",font="Cambria 40 bold", bg=self.cget("bg"))
       self.degree.place(x=390,y=135)

       # feels like label and sunny or fog like labels
       self.feel=Label(self, text="",font=("Nirmala UI",16,"bold"), bg=self.cget("bg"))
       self.feel.place(x=280,y=245)

       # suggestion label
       self.suggestion = Label(self, text="", font=("Nirmala UI", 12, "italic"), bg=self.cget("bg"))
       self.suggestion.place(x=280, y=280)
       
       # sunrise logo
       self.img4=Image.open(os.path.join(BASE_DIR, "Images/sunrise.png")).resize((40,40))
       self.finalimg4=ImageTk.PhotoImage(self.img4)
       Label(self, image=self.finalimg4, bg=self.cget("bg")).place(x=560,y=150)
       self.sunrise=Label(self, text="Sunrise : ",font=("Segoe UI",14,'bold'), bg=self.cget("bg"))
       self.sunrise.place(x=603,y=155)

       #sunset logo
       self.img5=Image.open(os.path.join(BASE_DIR, "Images/sunset.png")).resize((40,30))
       self.finalimg5=ImageTk.PhotoImage(self.img5)
       Label(self, image=self.finalimg5, bg=self.cget("bg")).place(x=560,y=215)
       self.sunset=Label(self, text="Sunset : ",font=("Segoe UI",14,'bold'), bg=self.cget("bg"))
       self.sunset.place(x=603,y=210)

       # bottom bar
       self.img6=Image.open(os.path.join(BASE_DIR, 'Images/bottom_bar.png')).resize((770,70))
       self.finalimg6=ImageTk.PhotoImage(self.img6)
       Label(self, image=self.finalimg6,bg='#00b7ff').place(x=5,y=330)

       # placing the labels
       Label(self, text="Humidity",font="Calibri 15 bold",bg='#00b7ff',fg='white').place(x=35,y=335)
       Label(self, text="Pressure",font="Calibri 15 bold",bg='#00b7ff',fg='white').place(x=210,y=335)
       Label(self, text="Description",font="Calibri 15 bold",bg='#00b7ff',fg='white').place(x=400,y=335)
       Label(self, text="Visibility",font="Calibri 15 bold",bg='#00b7ff',fg='white').place(x=600,y=335)

       # humidity label
       self.humidity=Label(self, text="",font=("Calibri",15,'bold'),bg='#00b7ff',fg='black')
       self.humidity.place(x=50,y=361)

       # pressure label
       self.pressure=Label(self, text="",font=("Calibri",15,'bold'),bg='#00b7ff',fg='black')
       self.pressure.place(x=203,y=361)

       # description label
       self.des=Label(self, text="",font=("Calibri",15,'bold'),bg='#00b7ff',fg='black')
       self.des.place(x=405,y=361)

       # visibility label
       self.vis=Label(self, text="",font=("Calibri",15,'bold'),bg='#00b7ff',fg='black')
       self.vis.place(x=610,y=361)

       # exit and reset button
       Button(self, text='Exit',font=("Georgia",16,"bold"),bg='orange',fg='black',width=7,relief='groove',command=self.exit).place(x=680,y=540)
       Button(self, text='Reset',font=("Georgia",16,"bold"),bg='orange',fg='black',width=7,relief='groove',activebackground="blue",activeforeground='white',command=self.clear).place(x=560,y=540)

       # Forecast Frame
       self.forecast_frame = Frame(self, bg=self.cget("bg"))
       self.forecast_frame.place(x=20, y=410, width=760, height=120)

    def __get_weather(self):
        try:
            # getting the weather information
            city=self.search.get()
            config_file=configparser.ConfigParser()
            config_file.read(os.path.join(BASE_DIR, "config.ini"))
            api=config_file['Openweather']['api']
            
            # Current Weather
            data=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
            weather=requests.get(data).json()
            self.__set_information(weather=weather)

            # 5-Day Forecast
            if weather.get('cod') == 200 or str(weather.get('cod')) == '200':
                self.__get_forecast(city, api)

        except requests.exceptions.ConnectionError:
            messagebox.showwarning('Connect',"Connect to The internet")
        except Exception as e:
            print(f"Error in __get_weather: {e}")
            messagebox.showerror('Error', f"An unexpected error occurred:\n{e}")

    def __get_forecast(self, city, api):
        try:
            url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api}&units=metric'
            response = requests.get(url).json()
            if response.get('cod') == "200":
                forecast_data = self.__process_forecast(response)
                self.update_forecast_ui(forecast_data)
            else:
                print(f"Forecast Error: {response.get('message')}")
        except Exception as e:
            print(f"Error fetching forecast: {e}")

    def __process_forecast(self, data):
        daily_summaries = []
        forecast_list = data.get('list', [])
        
        # Group by day
        by_day = {}
        for item in forecast_list:
            dt = datetime.datetime.fromtimestamp(item['dt'])
            day = dt.strftime('%Y-%m-%d')
            if day not in by_day:
                by_day[day] = []
            by_day[day].append(item)

        # Process first 5 future days (skipping today if needed, or including next 5 entries)
        sorted_days = sorted(by_day.keys())
        for i in range(1, 6): # Next 5 days
            if i >= len(sorted_days):
                break
            day = sorted_days[i]
            day_data = by_day[day]
            
            # Get max/min temp and most frequent weather icon
            max_temp = max(item['main']['temp_max'] for item in day_data)
            min_temp = min(item['main']['temp_min'] for item in day_data)
            icon = day_data[len(day_data)//2]['weather'][0]['icon'] # Take middle-of-day icon
            day_name = datetime.datetime.strptime(day, '%Y-%m-%d').strftime('%a')
            
            daily_summaries.append({
                'day': day_name,
                'temp_max': int(max_temp),
                'temp_min': int(min_temp),
                'icon': icon
            })
        return daily_summaries

    def update_forecast_ui(self, forecast_data):
        # Clear existing forecast UI
        for widget in self.forecast_frame.winfo_children():
            widget.destroy()

        for i, day in enumerate(forecast_data):
            f_frame = Frame(self.forecast_frame, bg=self.cget("bg"))
            f_frame.pack(side=LEFT, padx=15, expand=True)

            Label(f_frame, text=day['day'], font=("Segoe UI", 12, "bold"), bg=self.cget("bg")).pack()
            
            # Icon (fetch from OpenWeather CDN for simplicity or reuse local if mapped)
            try:
                icon_url = f"https://openweathermap.org/img/wn/{day['icon']}@2x.png"
                img_data = requests.get(icon_url).content
                icon_img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)).resize((40, 40)))
                lbl = Label(f_frame, image=icon_img, bg=self.cget("bg"))
                lbl.image = icon_img # keep reference
                lbl.pack()
            except:
                Label(f_frame, text="N/A", bg=self.cget("bg")).pack()

            Label(f_frame, text=f"{day['temp_max']}° / {day['temp_min']}°", font=("Segoe UI", 10), bg=self.cget("bg")).pack()

    def __set_information(self,weather):
        # print(weather)
        if weather.get('cod') == '404' and weather.get('message') == 'city not found':
            messagebox.showerror("Error","Entered City Not Found")
            self.search.set("")
        elif weather.get('cod') == '400' and weather.get('message') == 'Nothing to geocode':
            messagebox.showinfo("Warning",'Enter The city name')
            self.search.set('')
        elif weather.get('cod') == '401':
            messagebox.showerror("API Error", "Invalid API Key in config.ini. Please check your credentials.")
            self.search.set('')
        elif str(weather.get('cod')) != '200':
            messagebox.showerror("Error", f"Error from OpenWeather: {weather.get('message', 'Unknown Error')}")
            self.search.set('')
        else:
            # getting time according to timezone
            lon=weather['coord']['lon']  # longitutde
            lat=weather['coord']['lat']  # latitude
            tf=TimezoneFinder()
            result=tf.timezone_at(lng=lon,lat=lat)
            home=pytz.timezone(result)
            local=datetime.datetime.now(home).strftime("%d/%m/%y  %I:%M %p")
            self.timelbl['text']=local
            self.des['text']=weather['weather'][0]['description']
            self.feel['text']=f"Feels Like {int(weather['main']['feels_like']-273)}° | {weather['weather'][0]['main']}"
            type=weather['weather'][0]['main']
            self.place_image(type)
            
            # sets the temperature and degree label
            temp=int(weather['main']['temp']-273)
            self.degree['text']="°C"
            if temp>=100:
                self.degree.place(x=450,y=135)
            elif temp<=9 and temp>=0:
                self.degree.place(x=340,y=135)
            elif temp<=99 and temp>=10:
                self.degree.place(x=390,y=135)
            elif temp<0 and temp>=-9:
                self.degree.place(x=358,y=135)
            elif temp<=-10 and temp>=-99:
                self.degree.place(x=419,y=135)
            self.temperature['text']=temp
            self.humidity['text']=f"{weather['main']['humidity']}%"
            self.pressure['text']=f"{weather['main']['pressure']} mBar"
            self.location.config(text=weather['name'])
            self.vis['text']=f"{int(weather['visibility']/1000)} km"
            self.sunrise['text']=f"Sunrise : \n{datetime.datetime.fromtimestamp(int(weather['sys']['sunrise'])).strftime('%d/%m/%y  %I:%M %p')}"
            self.sunset['text']=f"Sunset : \n{datetime.datetime.fromtimestamp(int(weather['sys']['sunset'])).strftime('%d/%m/%y   %I:%M %p')}"

            # Update theme and suggestion
            main_weather = weather['weather'][0]['main']
            icon_code = weather['weather'][0]['icon']
            
            # Prioritize Night theme if icon indicates night ('n' suffix)
            if icon_code.endswith('n') and main_weather == 'Clear':
                theme = WEATHER_THEMES["Night"]
            else:
                theme = WEATHER_THEMES.get(main_weather, WEATHER_THEMES["default"])
            
            color = theme["bg"]
            suggestion_text = theme["suggestion"]

            if temp < 10:
                suggestion_text = "It's quite cold! Wear something warm."
            elif temp > 30:
                suggestion_text = "It's hot outside! Stay hydrated."

            self.update_theme(color)
            self.suggestion['text'] = suggestion_text


    def update_theme(self, color):
        self.config(bg=color)
        if hasattr(self, 'forecast_frame'):
            self.forecast_frame.config(bg=color)
            for child in self.forecast_frame.winfo_children():
                if isinstance(child, (Frame, Label)):
                    child.config(bg=color)
                    for gchild in child.winfo_children():
                        if isinstance(gchild, (Frame, Label)):
                            gchild.config(bg=color)
        
        for widget in self.winfo_children():
            if isinstance(widget, Label) and widget.cget("bg") != '#00b7ff':
                widget.config(bg=color)
            if isinstance(widget, Frame) and widget != getattr(self, 'forecast_frame', None):
                widget.config(bg=color)

    def place_image(self,type):
        if type=="Clear":
            img="clear.png"
            self.set_image(img)
        elif type=="Clouds":
            img='clouds.png'
            self.set_image(img)
        elif type=="Rain":
            img='rain.png'
            self.set_image(img)
        elif type=='Haze':
            img='Haze.png' # Fixed casing
            self.set_image(img)
        else:
            img='main.png'
            self.set_image(img)
    
    def set_image(self,img):
       try:
           self.img3=Image.open(os.path.join(BASE_DIR, "Icons", img))
           self.resizeimg3=self.img3.resize((190,190))
           self.finalimg3=ImageTk.PhotoImage(self.resizeimg3)
           self.icons.config(image=self.finalimg3, bg=self.cget('bg'))
       except Exception as e:
           print(f"Error loading image {img}: {e}")
           # Fallback to main.png if it exists and we're not already trying to load it
           if img != "main.png":
               self.set_image("main.png")
    
    def clear(self):
        self.des.config(text="")
        self.vis.config(text="")
        self.pressure.config(text="")
        self.humidity.config(text="")
        self.sunset.config(text="Sunset :")
        self.sunrise.config(text="Sunrise :")
        self.feel.config(text="")
        self.degree.config(text="")
        self.temperature.config(text="")
        self.timelbl.config(text="")
        self.location.config(text="")
        self.search.set("")
        self.suggestion.config(text="")
        if hasattr(self, 'forecast_frame'):
            for widget in self.forecast_frame.winfo_children():
                widget.destroy()
        self.update_theme(WEATHER_THEMES["default"]["bg"])
        img='main.png'
        self.set_image(img)

    def exit(self):
        a=messagebox.askyesno('Confirmation',"Are You sure You Want To Exit !")
        if a==True:
            self.destroy()

    def threading(self,event=0):
        t1=threading.Thread(target=self.__get_weather)
        t1.start()



if __name__=="__main__":
    c=Weather()
    c.mainloop()
