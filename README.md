# Python-Telegram-Bot

This is a python discord  bot made with discord.py framework. Discord is greatly enhanced by its versatile bots, which allow seamless integration with external platforms and offer users an immersive and interactive experience. 


## Bot Commands

| Commands    	| Function                              	| User Input              	|
|-------------	|------------------------------------------	|------------------------	|
| ?ping      	| checking if the bot is online             | None                    	|
| ?status      	| provide the latency ms of the bot         | None                    	|
| ?list      	| provide the list of all commands          | None                    	|
| ?apod       	| provide the astronomy picture of the day  | <YYYY-MM-DD> format     	|
| ?generateqr 	| sends a qr code to the given text         | text                    	|
| ?ufact      	| sends a useless fact                      | None                    	|
| ?qoute      	| provide a random qoute with author        | None                    	|
| ?define      	| provide the simple definition of the word | text                    	|


## Installing modules

- [discord.py](https://github.com/Rapptz/discord.py)
  - Framework
```python
    pip install -U discord.py
```
-  [dotenv](https://github.com/theskumar/python-dotenv)
    - environment variables
```python
    pip install python-dotenv
```
-  [pytz](https://pypi.org/project/pytz/)
    - for timezones
```python
    pip install pytz
```

## APIs

- Generating QR Code --> [goqr](https://goqr.me/api/)
- Astronomy Picture of the Day by NASA --> [NASA](https://api.nasa.gov/)
- Useless Facts --> [useless](https://uselessfacts.jsph.pl/)
- Random Qoutes --> [zenqoutes](https://my.zenquotes.io/)