# Weather-App-Using-python-Tkinter

![weather](https://img.shields.io/badge/GUI-Tkinter-orange?style=flat-square&logo=python) 
![weather](https://img.shields.io/badge/API-openweather-blue?style=flat-square&logo=api)

## About:
This app uses the Open weather Api to get the data of the weather. </br>
It generates the data in the form of json.</br>

## Technologies Used:
- OpenWeather Api
- Pytz python Module
- Timezonefinder Python Module
- Tkinter 
- Python 3.9.1
- Requests Python Module
</br>

**Pytz Module** - This Module is all about the timezone so using this module we extracted the timezone of specified longitude and latitude generated from openweather api</br>

**Timezonefinder** - As the name suggests it is used to find the timezone only so using timezone we can show the current time of that searched city.</br>

Visit [Open Weather](https://openweathermap.org/) </br>
Create Your account in this and get the api key and refer the documentation</br>

used the thread module to click on the search button so smootly so that the app does'nt Crashes.</br>

To get the Timezone and time i have used the pytz module and timezonefinder module to get the timezone of the searched city.</br>

## Sample Video:
![weather app](https://user-images.githubusercontent.com/87264935/163821347-f988efc2-79ea-40cd-acae-e6e4d780e49e.gif)

## Screenshots:
![Empty Gui](https://user-images.githubusercontent.com/87264935/163683668-f659b80e-2ef2-4553-99d2-6f0728c7a968.png)
![Output](https://user-images.githubusercontent.com/87264935/163683683-1b0c70c1-0c52-46d2-b7a9-962626c15238.png)

## How to Run the Application

### 1. Install Dependencies
 **Python 3** needs to be installed.  
Then install the required packages:

```bash
pip install pytz
pip install threading
pip install requests
pip install datetime
pip install timezonefinder
```



### 2. Create an OpenWeather Account
Go to: https://openweathermap.org/  
Create an account.

### 3. Confirm Your Email
OpenWeather will send a verification link to your email.  
After confirming, you will receive an **API key** via email, as well as on the dashboard.

### 4. Obtain Your API Key
Go to the **API Keys** section on your OpenWeather dashboard and copy your key.

### 5. Configure the Application
Open the `config.ini` file in the project directory and paste your API key:

```ini
api = YOUR_API_KEY_HERE
```

### 6. Run the Application
Start the app using:

```bash
python3 app.py
```

After the app launches, type any city into the search bar and press **Enter**.

## Feature to Implement: 

Implement a favorites dropdown that will save cities the user has previously searched for and saved as favorites. 

Also, implement the ability to toggle between Celsius and Farenheiht. 

### Author:
**Prathamesh Dhande**

