from python_smartmetertx import MeterReader
import plotly.express as px
import os
from datetime import date,timedelta

USER = os.environ['USER']
PASS = os.environ['PASS']
ESSID = os.environ['ESSID']
OUTFILE = os.environ['OUTFILE']
NUMDAYS = int(os.environ['NUMDAYS'])

td = timedelta(days=NUMDAYS + 1)
endDate = (date.today() - timedelta(days=1)).strftime("%m/%d/%Y")
startDate = (date.today() - td).strftime("%m/%d/%Y")

print(f"Date Range: {startDate} through {endDate}")

tx = MeterReader()

r = tx.login(USER, PASS)

j = tx.get_daily_read(ESSID, startDate, endDate)

print("Creating Bar Chart...")
rd = j['data']['registeredReads']


labels = {
    "readDate" : "Date",
    "energyDataKwh": "KwH"
}

fig = px.bar(data_frame=rd, x="readDate", y ="energyDataKwh", labels=labels)

fig.write_html(OUTFILE)

print("Done.")