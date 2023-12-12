# rpi-bookcase
Digital e-ink bookcase running on Raspberry Pi

On boot the device pulls the latest commit from this Github repo, and chooses a random book cover to show on the e-ink display

## WittyPi
Power management is dealt with by WittyPi which is at `~/wittypi`.

`sudo ./wittypi.sh` allows you to change schedule scripts etc (which are in `wittypi/schedules`)