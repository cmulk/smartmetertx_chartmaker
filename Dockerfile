FROM ubuntu

## Replace with your username, password, and ESSID or define at runtime
# ENV USER=<<USERNAME>>
# ENV PASS=<<PASSWORD>>
# ENV ESSID=<<ESSID>>

ENV OUTFILE="/out/daily_reads.html"
ENV NUMDAYS=7
ENV TZ="America/Chicago"

# Install pandas from package since it's too hard to compile on Raspberry Pi
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
   && apt-get -y install --no-install-recommends python3 python3-pip python3-setuptools python3-wheel python3-pandas tzdata \
   #
   # Clean up
   && apt-get autoremove -y \
   && apt-get clean -y \
   && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

WORKDIR /app

COPY python_smartmetertx ./python_smartmetertx
COPY chartmaker.py .


CMD ["python3", "-u", "chartmaker.py"]