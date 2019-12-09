#!/bin/bash

python3.5 mp3_regrade.py input/mp31.csv "GDT Loading [0;1]" "Exception Handlers [0;1]"
python3.5 mp3_regrade.py input/mp32.csv "RTC Open/Close [0;1]" "Read Directory [0;1]"
python3.5 mp3_regrade.py input/mp33.csv "Shell runs and prompt shows up [0;2]" "Shell auto relaunched or preventing halt on root shell [0,1]"
python3.5 mp3_regrade.py input/mp34.csv "Multiple shells can run [0;2]" "all programs halt properly [0;2]"
python3.5 mp3_regrade.py input/mp35.csv "At Least 3 Terminals [0;1]" "While pingpong runs other shells can be exited [0;1]"
