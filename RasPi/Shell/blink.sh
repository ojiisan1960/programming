#!/bin/bash
# Blink the ACT on the pi 5 times


LED_0='/sys/class/leds/led0'

echo none > $LED_0/trigger

for (( i=1; i <= 5; i++))
do
    echo 1 > $LED_0/brightness
    sleep 1s
    echo 0 > $LED_0/brightness
    sleep 1s
done

echo mmc0 > $LED_0/trigger
