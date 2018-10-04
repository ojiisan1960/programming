#!/bin/bash
#
# an example using gdialog
# From Beginning Linux Programming 4th Ed

gdialog --title "Questionnaire" --msgbox "Welcome to my simple survey" 9 18

gdialog --title "Confirm" --yesno "Would like to take part?" 9 18

if [ $? != 0 ];then
	gdialog --infobox "Thank you anyway" 5 20
	sleep 2
	gdialog --clear
	exit 0
	else
	gdialog --title "Questionnaire" --inputbox "Please enter your name" 9 30 2>_1.txt
	Q_NAME=$(cat _1.txt)

	gdialog --menu "$Q_NAME, what music do you like best?" 15 30 4 1 "Classical" 2 "Jazz" 3 "Country" 4 "Other" 2>_1.txt
	Q_MUSIC=$(cat _1.txt)

	if [ "$Q_MUSIC" = "1" ]; then
		gdialog --title "Likes Classical" --msgbox "Good choice!" 12 25
	else
		gdialog --title "Doesn’t like Classical" --msgbox "Shame" 12 25
	fi
	gdialog --infobox "Thanks for playing!" 5 25
	sleep 2
	gdialog --clear
	exit 0
fi

