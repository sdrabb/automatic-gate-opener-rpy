# Automatic Gate Opener rpy

If you are tired to spend a lot of money in automatic gate controller this project can help you!

**Automatic Gate Opener rpy** is a [Raspberry Pi](https://www.raspberrypi.org/) solution to control an automatic gate by a mobile phone using a broken automatic gate controller.

![alt text](https://github.com/sdrabb/automatic-gate-opener-rpy/blob/master/img/circuit.JPG)

## Requirements
* [Raspberry PI](https://www.raspberrypi.org/) 
* [Relay](https://www.amazon.com/SainSmart-101-70-101-4-Channel-Relay-Module/dp/B0057OC5O8): 
* [broken automatic gate controller](https://www.google.it/search?q=automatic+gate+controller&tbm=isch&source=lnms&sa=X&ved=0ahUKEwjm19Sf6_TUAhXL6RQKHbRvAokQ_AUIPSgB&biw=1855&bih=917#tbm=isch&q=automatic+gate+controller+button)
* [cables](https://www.google.it/search?q=automatic+gate+controller&tbm=isch&source=lnms&sa=X&ved=0ahUKEwjm19Sf6_TUAhXL6RQKHbRvAokQ_AUIPSgB&biw=1855&bih=917#tbm=isch&q=wire)
* [Tin welder](https://www.google.it/search?q=welding+machine+electronic&source=lnms&tbm=isch&sa=X&ved=0ahUKEwikmb2M4fTUAhUhIcAKHQDrC-sQ_AUIBigB&biw=1855&bih=966#tbm=isch&q=Tin+welder)
* [mobile device with Telegram]()
## Circuit Installation

take your broken automatic gate controller and try to close the circuit with a cable. When you found the correct pins weld to each of them a cable and after that follow the images in the [build circuit folder](https://github.com/sdrabb/automatic-gate-opener-rpy/tree/master/build%20the%20circuit)


## SW Installation

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

now enter the mobile phone number with the prefix of your country, your name and surname of the people who are allowed to control the gate with the following command

```
add_contact [countryPrefix_phone_number] [name] [surname]
ex: add_contact 39xxxxxxxxx Alan Turing
```	
at this point add the code prvided by BotFather into the array **id_a** and run the **telegram_server.py** using this command
 ```
python telegram_server.py
```	
now chat with your bot using this command on your telegram app and  the gate will start to opening
 ```
/toggle
```

**note:** if you are using an ssh connection you can keep alive the session using a tool like [tmux](https://github.com/tmux/tmux/wiki)

## boot server at startup using systemd

move to systemd folder of your Raspberry
```
cd lib/systemd/system/
```
create your service
```
sudo nano automatic_gate.service
```
and paste in the new file the following lines
```
[Unit]
Description=Clown server for jessie
After=network.target

[Service]
Type=idle
ExecStart=/usr/bin/python /home/pi/Desktop/projects/automatic-gate-opener-rpy/telegram_server.py >>/home/pi/log.txt 2>&1
Restart=always
StartLimitIntervalSec=1min
StartLimitBurst=500

[Install]
WantedBy=multi-user.target



```
enable your service

```
sudo systemctl enable automatic_gate.service
```
control the status of your service
```
sudo systemctl status automatic_gate

```


## Structure
* [remote_controller.py](https://github.com/sdrabb/automatic-gate-opener-rpy/blob/master/remote_controller.py): contains all the procedures used to control the circuit that open and close the gate
* [telegram_server.py](https://github.com/sdrabb/automatic-gate-opener-rpy/blob/master/telegram_server.py): telegram server implementation

## Build with
* [telepot](https://github.com/nickoala/telepot/): Python framework for Telegram 





Copyright © 2017 sdrabb
