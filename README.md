# Time Logging Bot
Python Discord bot created for recording Discord channels & meetings in channels

## Usage
This bot runs on Python 3.10, along with PyCord v2.0 (last tested to work on [PyCord](https://github.com/Pycord-Development/pycord) v2.0.0b4. Below, you will find the steps for how to setup the bot depending on your specific usage

### Pterodactyl Container
To run this bot via a Pterodactyl container, import the JSON file titled "egg" into your Pterodactyl nest. After that, you should be able to create a server, import these files, and run it. No checks have been done to verify that the requirements.txt will actually work inside of this server. If it doesn't, feel free to reach out to me and I'll adjust the egg as needed for that.

### Windows/Linux CLI
To run this bot via CLI, you need two prerequisites. Firstly, you'll need to have Python v10 installed. That can be done by clicking [this](https://www.python.org/downloads/) link if you're on Windows. If you're on Linux, you will most likely have Python 3.9 installed by default (you can verify by typing in `python3 --version` into your CLI. If you've got Python 3.10 installed, you're good to go. If not, check out [this](https://opensource.com/article/20/4/install-python-linux) guide for installing the latest version of Python. After doing this, and verifying that Python 3.10 has been installed, you can proceed to install [PyCord](https://github.com/Pycord-Development/pycord). If you want, you can visit their repository to see the ways in which you can installed it, however, I'll attach the way in which we will do it in this repository below. Following this, extract the bot into a folder and CD into that folder. Then, run the following command: `python3 -m pip install -r requirements.txt`. Now, with all of the requirements setup, you can follow the configuration below and then run the following command to start the bot: `python3 main.py`

```
git clone https://github.com/Pycord-Development/pycord
cd pycord
python3 -m pip install -U .[voice]
```

### Configuration
The bot comes with an easily configurable config file. However, since some people aren't the best at understanding config files, I've attached comments into the config that explain what everything means and how to use it.

[Hosting Company](https://jakehamblin.com/images/hosturly.png)
### Hosting Company
Are you looking for a reliable and affordable host? Well, with many years of experience working with websites, website hosting, and dedicated server hosting, I can say that I've got a pretty good idea when a host is good. [Hosturly](https://jakehamblin.com/hosturly) is up for the task. Don't trust me? Read their reviews. They've got an almost 5 star rating, and with many years in the industry, they're here to stay. Use code `JAKE` for 10% off your order.
