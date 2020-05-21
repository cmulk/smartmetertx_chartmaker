from python_smartmetertx import MeterReader
import plotly.express as px
import os
from datetime import date,timedelta

USER = os.environ['USER']
PASS = os.environ['PASS']
ESIID = os.environ['ESIID']
OUTFILE = os.environ['OUTFILE']
NUMDAYS = int(os.environ['NUMDAYS'])

td = timedelta(days=NUMDAYS + 1)
endDate = (date.today() - timedelta(days=1)).strftime("%m/%d/%Y")
startDate = (date.today() - td).strftime("%m/%d/%Y")

print(f"Date Range: {startDate} through {endDate}")

tx = MeterReader()

r = tx.login(USER, PASS)

j = tx.get_daily_read(ESIID, startDate, endDate)


print("Creating Bar Chart...")
rd = j['dailyData']


labels = {
    "x" : "Date",
    "reading": "KwH"
}

# strip year from readDates
read_dates_short = [data['date'][:-5] for data in rd]

fig = px.bar(data_frame=rd, x=read_dates_short, y ="reading", text='reading', labels=labels)
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))

fig.write_html(OUTFILE, include_plotlyjs='cdn')

print("Done.")
