# Import libraries--------------------------
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
from kivy.core.window import Window

# Set window size --------------------------
Window.size = (600, 400)

# Api URL ----------------------------------
url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

# Layout class -----------------------------
class DataViz(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# App class --------------------------------
class Vizualizer(App):

    #-------------Fetch data to display on the window-(API call)------------------
    response = requests.request("GET", url)
    data = json.loads(response.text)
    yearList = []
    PopulationList = []
    # --------------Loop through response get Year and Population of USA ---------
    for i in data["data"]:
        yearList.append(i["Year"])
        PopulationList.append(i["Population"])
        print(i["Year"], "--", i["Population"])
    # --------------Create a DF to display in tabular format ----------------------
    data = {'Year': yearList,
            'Population': PopulationList
            }
    df = pd.DataFrame(data, columns=['Year', 'Population'])
    Table = str(df)
    Title = "USA Population Data"

    #-------------------- Build App method---------------------------
    def build(self):
        return DataViz()

    #------------------ Method to display bar graph -----------------
    def showBar(self):
        # ----------Call api to get data-----------------------------
        response = requests.request("GET", url)
        data = json.loads(response.text)
        yearList = []
        PopulationList = []
        # ----------Loop through json to get year and population-----
        for i in data["data"]:
            yearList.append(i["Year"])
            PopulationList.append(i["Population"])
            print("USA Population:","\n",i["Year"], "--", i["Population"])
        #-----------Create df to plot the bar graph------------------
        data = {'Year': yearList,
                'Population': PopulationList
                }
        df = pd.DataFrame(data, columns=['Year', 'Population'])
        df.plot(x='Year', y='Population', kind='bar')

        plt.show()
    def showLine(self):
        # ----------Call api to get data-----------------------------
        response = requests.request("GET", url)
        data = json.loads(response.text)
        yearList = []
        PopulationList = []
        # ----------Loop through json to get year and population-----
        for i in data["data"]:
            yearList.append(i["Year"])
            PopulationList.append(i["Population"])
            print("USA Population:", "\n", i["Year"], "--", i["Population"])
        # -----------Create df to plot the line graph------------------
        data = {'Year': yearList,
                'Population': PopulationList
                }
        df = pd.DataFrame(data, columns=['Year', 'Population'])
        df.plot(x='Year', y='Population', kind='line')

        plt.show()
    def showPie(self):
        # ----------Call api to get data-----------------------------
        response = requests.request("GET", url)
        data = json.loads(response.text)
        yearList = []
        PopulationList = []
        # ----------Loop through json to get year and population-----
        for i in data["data"]:
            yearList.append(i["Year"])
            PopulationList.append(i["Population"])
            print("USA Population:", "\n", i["Year"], "--", i["Population"])
        # -----------Create df to plot the pie graph------------------
        data = {'Year': yearList,
                'Population': PopulationList
                }
        df = pd.DataFrame(data, columns=['Year', 'Population'])
        df.plot(x='Year', y='Population', kind='pie')

        plt.show()

window = Vizualizer()
window.run()
