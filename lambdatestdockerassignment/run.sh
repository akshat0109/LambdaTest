#!/bin/sh
read -p "Your link here: "
echo "$REPLY" > output.txt
cp output.txt chromexecutiondocker
cp output.txt firefoxexecutiondocker

cd chromexecutiondocker
sudo docker build -t my-chromecode .
cd ..
cd firefoxexecutiondocker
sudo docker build -t my-firefoxcode .
cd ..
sudo docker run -d my-chromecode
CONTAINER_ID1=$(docker ps -alq)
sudo docker run -d my-firefoxcode
CONTAINER_ID2=$(docker ps -alq)
sudo docker cp $CONTAINER_ID1:/resultchrome .
sudo docker cp $CONTAINER_ID2:/resultfirefox .
head resultchrome resultfirefox

