#!/bin/bash

#something usefull for bash scripting assignment
clear

echo "Mission Planner for IL2: Sturmovick missions"


echo "Select Aircraft: "
echo "1: 109"
echo "2: 111"
echo "3: Ju88"
read sel

sleep 1

clear

echo "Total distance needed to travel in km: "
read dis

clear

case $sel in
1 | 109)
maxF=401
(( ReqF = $dis / 3))
#(( ReqF = $conv1 / 100))

if [[ $dis -gt 1259 ]]
then
echo "To great a distance"
else
echo "$ReqF liters of fuel is required to make the travel of $dis km."
fi

;;
2 | 111)
maxF=8570
#(( conv1 = $dis * 9))
(( ReqF = $dis * 4))

if [[ $dis -gt 2200 ]]
then
echo "To great a distance"
else
echo "$ReqF liters of fuel is required to make the travel of $dis km."
fi

;;

3 | Ju88)
maxF=3000
(( conv1 = $dis * 9))
(( ReqF = $conv1 / 10))

if [[ $dis -gt 3000 ]]
then
echo "To great a distance"
else
echo "$ReqF liters of fuel is required to make the travel of $dis km."
fi

;;
*)
echo "Invalid selection"
;;
esac
