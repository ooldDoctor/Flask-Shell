#!/bin/bash
currentTime=$(date +"%T")
#echo "Current time : $currentTime"
cd static
var=$(</home/wiki/ab/app/hungry)
#echo "$green"
let var="$var + 1"
streamer -f jpeg -o $var-$currentTime.jpeg
#scp your_username@remotehost.edu:foobar.txt /some/local/directory 
#cp -u $currentTime.jpeg /home/robotic/app/static

value(){

src="/static/$currentTime.jpeg"
echo $src




}
destdir=/home/wiki/ab/app/hungry

if [ -f "$destdir" ]
then 
    echo "$var" > "$destdir"
fi

