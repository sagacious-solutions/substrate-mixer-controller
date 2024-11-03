### Initial Setup

```
python -m venv .venv
pip install -r requirements.txt
```

# Hardware Functionality

### LCD

LCD is a 4x20 Char display with a PCF8574 i2c GPIO backpack

### Motor Control

Motors controlled with PWM via a D4184 Mosfet.

### Coding and Running
```
source .venv/bin/activate
python main.py
```


### Troubleshooting

Checking the LCD is detected correctly

```
sudo i2cdetect -y 1
```

Issues with LCD Updating too slowly. 

Initially it was writing very slow for me because I had previously lowered my i2c baud
rate as low as possible to accomodate some unusually long pathing to a sensor device.
This caused the LCD to write too slow for real time updates. After increasing the baud
rate from 10,000 up to 400,000 it began writting more or less instantly.

https://gist.github.com/ribasco/c22ab6b791e681800df47dd0a46c7c3a