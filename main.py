#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import re
import time


def getCpuSpeed():
    command = "lscpu"
    clock_speed_strings = []
    clock_speed = ""

    cpu_all_info = subprocess.check_output(command, shell=True).strip()
    for line in cpu_all_info.split("\n"):
        if "Vitesse du processeur en MHz :" in line:
            # print(line)

            for i in line:
                if i.isdigit():
                    clock_speed_strings.append(i)

    clock_speed = clock_speed.join(clock_speed_strings)
    clock_speed = int(clock_speed) / 1000

    print(str(clock_speed) + " MHz")
    time.sleep(0.5)


def main():
    try:
        while True:
            getCpuSpeed()
    except KeyboardInterrupt:
        print("\nProgram interrupted.")


main()
