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

# strip year from readDates
read_dates_short = [data['readDate'][:-5] for data in rd]

fig = px.bar(data_frame=rd, x=read_dates_short, y ="energyDataKwh", text='energyDataKwh', labels=labels)
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))

fig.write_html(OUTFILE, full_html=False)

print("Done.")
