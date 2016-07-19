#!/bin/bash
cd static

value(){
for entry in *
do
if expr "$(file -b $entry)" : 'JPEG ' >/dev/null; 
then
    #echo -e "$entry"
    echo "/static/$entry" 	
fi	
  
  
done
}
value



#ls -R *.jpeg


