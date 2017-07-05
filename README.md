# Automatic Gate Opener rpy

If you are tired to spend a lot of money in automatic gate controller this project can help you!

**Automatic Gate Opener rpy** is a [Raspberry Pi](https://www.raspberrypi.org/) solution to control an automatic gate by a mobile phone using a broken automatic gate controller.

![alt text](https://github.com/sdrabb/automatic-gate-opener-rpy/blob/master/img/circuit.JPG)


###  Work in progress   :hourglass_flowing_sand:

## Installation

go in your raspberry pi and paste the following commands: 

update the package lists for upgrades for packages that need upgrading

```
sudo apt-get update
```
fetch new versions of packages existing on the machine if APT knows about these new versions

```
sudo apt-get upgrade
```
install all necessary library

```
sudo apt-get install libreadline-dev libconfig-dev libssl-dev lua5.2 liblua5.2-dev libevent-dev make libjansson-dev
```

copy the Command-line interface for Telegram in the directory where you want install it

```
git clone --recursive https://github.com/vysheng/tg.git 
```

go in the tg folder, configure all and enter into installation of de Telegram cli

```
cd tg
sudo ./configure
sudo make
```
enter into the guided installation

```
./bin/telegram-cli
```

now enter mobile phone with the prefix of your country, your name and surname of the people who are allowed to control the gate with the following command

'''
add_contact [countryPrefix_phone_number] [name] [surname]
ex: add_contact 39xxxxxxxxx Alan Turing
'''

Copyright © 2017 sdrabb
