# start from base
FROM ubuntu:18.04

MAINTAINER akshatgarg <ag>

COPY dockerfirefoxexecution.py dockerfirefoxexecution.py
COPY output.txt output.txt
RUN apt-get -yqq update
RUN apt-get -yqq install python3-pip python3-dev curl gnupg
RUN apt-get install python3-pip
RUN pip3 install --upgrade pip
RUN apt-get -yqq install firefox
COPY requirement.txt requirement.txt
COPY geckodriver /bin/geckodriver
RUN chmod +x /bin/geckodriver
RUN pip3 install -r requirement.txt
RUN python3 dockerfirefoxexecution.py > resultfirefox
