# start from base
FROM ubuntu:18.04

MAINTAINER akshatgarg <ag>

COPY dockerchromeexecution.py dockerchromeexecution.py
COPY output.txt output.txt
RUN apt-get -yqq update
RUN apt-get -yqq install wget
RUN apt-get -yqq install python3-pip python3-dev curl gnupg
RUN apt-get install python3-pip
RUN pip3 install --upgrade pip
COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -yqq update
RUN apt-get -yqq install google-chrome-stable
COPY chromedriver /bin/chromedriver
RUN chmod +x /bin/chromedriver
RUN export PATH=$PATH:/
RUN python3 dockerchromeexecution.py > resultchrome
