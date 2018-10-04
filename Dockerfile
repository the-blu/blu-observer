FROM bluelens/chrome-headless:dev

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/

RUN pip3 install --user --upgrade pip
RUN pip3 install --user --no-cache-dir -r requirements.txt
RUN npm install -g chrome-har-capturer

COPY . /usr/src/app
ENV LANG en_US.UTF-8
EXPOSE 8080

CMD python3 run.py