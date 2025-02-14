#!/bin/bash


function is_loyal() {
echo " $1 ne mud ke kisko dekha:"

read bandi 


if [[ "$bandi" == "daya bhabhi" ]];
then

	echo " $1 is loyal"
else
	echo " $1  is not loyal"
fi

}

is_loyal "tom"
