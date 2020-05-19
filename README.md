# Smart Meter Texas Chartmaker
Uses the python_smartmetertx (github.com/cmulk/python_smartmetertx) api and plotly to build a simple electricity usage chart suitable to be embedded in a HomeAssistant iframe.

## Environment Variables
Required:
- Username -> __USER__
- Password -> __PASS__
- ESIID -> __ESIID__

Optional:
- Output file path (relative to container) - > __OUTFILE__
- Number of days of usage -> __NUMDAYS__

## Build
```
docker build -t smartmetertx_chartmaker:local .
```
or
```
docker build -t smartmetertx_chartmaker:local https://github.com/cmulk/smartmetertx_chartmaker.git
```

## Example run
```
docker run -it --rm -e 'USER=<your_username>' -e 'PASS=<your_password>' -e 'ESIID=<your_esiid>' -v <output_dir>:/out smartmetertx_chartmaker:local
```
HTML file will be saved as `<output_dir>/daily_reads.html` by default.


