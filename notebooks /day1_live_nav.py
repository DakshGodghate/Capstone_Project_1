import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine
import requests
import scipy
from scipy import stats
from scipy import optimize
from scipy import signal
from IPython.display import display
import csv


def get_latest_nav(mf125497):
    url = f" https://api.mfapi.in/mf/125497/latest"
    reponse = requests.get(url)
    data=reponse.json()

    fund_name = data['meta']['scheme_name']
    nav = data['data'][0]['nav']
    date = data['data'][0]['date']

    return fund_name,nav,date

name,nav,date = get_latest_nav("125497")
print(f"Fund:{name}")
print(f"NAV:₹{nav}")
print(f"Date:{date}")

def get_latest_nav(mf119551):
    url = f" https://api.mfapi.in/mf/119551/latest"
    reponse = requests.get(url)
    data=reponse.json()

    fund_name = data['meta']['scheme_name']
    nav = data['data'][0]['nav']
    date = data['data'][0]['date']

    return fund_name,nav,date

name,nav,date = get_latest_nav("119551")
print(f"Fund:{name}")
print(f"NAV:₹{nav}")
print(f"Date:{date}")

def get_latest_nav(mf120503):
    url = f" https://api.mfapi.in/mf/120503/latest"
    reponse = requests.get(url)
    data=reponse.json()

    fund_name = data['meta']['scheme_name']
    nav = data['data'][0]['nav']
    date = data['data'][0]['date']

    return fund_name,nav,date

name,nav,date = get_latest_nav("120503")
print(f"Fund:{name}")
print(f"NAV:₹{nav}")
print(f"Date:{date}")

def get_latest_nav(mf118632):
    url = f" https://api.mfapi.in/mf/118632/latest"
    reponse = requests.get(url)
    data=reponse.json()

    fund_name = data['meta']['scheme_name']
    nav = data['data'][0]['nav']
    date = data['data'][0]['date']

    return fund_name,nav,date

name,nav,date = get_latest_nav("118632")
print(f"Fund:{name}")
print(f"NAV:₹{nav}")
print(f"Date:{date}")

def get_latest_nav(mf119092):
    url = f" https://api.mfapi.in/mf/119092/latest"
    reponse = requests.get(url)
    data=reponse.json()

    fund_name = data['meta']['scheme_name']
    nav = data['data'][0]['nav']
    date = data['data'][0]['date']

    return fund_name,nav,date

name,nav,date = get_latest_nav("119092")
print(f"Fund:{name}")
print(f"NAV:₹{nav}")
print(f"Date:{date}")

def get_latest_nav(mf120841):
    url = f" https://api.mfapi.in/mf/120841/latest"
    reponse = requests.get(url)
    data=reponse.json()

    fund_name = data['meta']['scheme_name']
    nav = data['data'][0]['nav']
    date = data['data'][0]['date']

    return fund_name,nav,date

name,nav,date = get_latest_nav("120841")
print(f"Fund:{name}")
print(f"NAV:₹{nav}")
print(f"Date:{date}")

def get_latest_nav(mf119018):
    url = f" https://api.mfapi.in/mf/119018/latest"
    reponse = requests.get(url)
    data=reponse.json()

    fund_name = data['meta']['scheme_name']
    nav = data['data'][0]['nav']
    date = data['data'][0]['date']

    return fund_name,nav,date

name,nav,date = get_latest_nav("119018")
print(f"Fund:{name}")
print(f"NAV:₹{nav}")
print(f"Date:{date}")

def get_latest_nav(mf119598):
    url = f" https://api.mfapi.in/mf/119598/latest"
    reponse = requests.get(url)
    data=reponse.json()

    fund_name = data['meta']['scheme_name']
    nav = data['data'][0]['nav']
    date = data['data'][0]['date']

    return fund_name,nav,date

name,nav,date = get_latest_nav("119598")
print(f"Fund:{name}")
print(f"NAV:₹{nav}")
print(f"Date:{date}")

def get_latest_nav(mf120465):
    url = f" https://api.mfapi.in/mf/120465/latest"
    reponse = requests.get(url)
    data=reponse.json()

    fund_name = data['meta']['scheme_name']
    nav = data['data'][0]['nav']
    date = data['data'][0]['date']

    return fund_name,nav,date

name,nav,date = get_latest_nav("120465")
print(f"Fund:{name}")
print(f"NAV:₹{nav}")
print(f"Date:{date}")

def get_latest_nav(mf120586):
    url = f" https://api.mfapi.in/mf/120586/latest"
    reponse = requests.get(url)
    data=reponse.json()

    fund_name = data['meta']['scheme_name']
    nav = data['data'][0]['nav']
    date = data['data'][0]['date']

    return fund_name,nav,date

name,nav,date = get_latest_nav("120586")
print(f"Fund:{name}")
print(f"NAV:₹{nav}")
print(f"Date:{date}")

def get_latest_nav(mf120152):
    url = f" https://api.mfapi.in/mf/120152/latest"
    reponse = requests.get(url)
    data=reponse.json()

    fund_name = data['meta']['scheme_name']
    nav = data['data'][0]['nav']
    date = data['data'][0]['date']

    return fund_name,nav,date

name,nav,date = get_latest_nav("120152")
print(f"Fund:{name}")
print(f"NAV:₹{nav}")
print(f"Date:{date}")



scheme_codes = ["125497","119551","120503","118632","119092",
                "120841","119018","119598","120465","120586",
                "120152"]
rows = []
for code in scheme_codes:
    data = requests.get(f"https://api.mfapi.in/mf/{code}/latest").json()
    rows.append({
        "scheme_code": data['meta']['scheme_code'],
        "scheme_name": data['meta']['scheme_name'],
        "fund_house" : data['meta']['fund_house'],
        "scheme_type": data['meta']['scheme_type'],
        "scheme_category": data['meta']['scheme_category'],
        "nav":         data['data'][0]['nav'],
        "date":        data['data'][0]['date'],
    })

with open ("nav_data.csv","w",newline="")as f:
    writer = csv.DictWriter(f,fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Saved {len(rows)}funds to nav_data.csv")

