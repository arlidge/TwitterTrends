# TwitterTrends
Monitor trends on twitter with python
 _                                          ___       _ _     _
| |                                        / _ \     | (_)   | |
| |     __ _ _   _ _ __ ___ _ __   ___ ___/ /_\ \_ __| |_  __| | __ _  ___
| |    / _` | | | | '__/ _ \ '_ \ / __/ _ \  _  | '__| | |/ _` |/ _` |/ _ \
| |___| (_| | |_| | | |  __/ | | | (_|  __/ | | | |  | | | (_| | (_| |  __/
\_____/\__,_|\__,_|_|  \___|_| |_|\___\___\_| |_/_|  |_|_|\__,_|\__, |\___|
                                                                __/  |
                                                               |___/


You will need python 3.6

I suggest making a virtualenv

https://docs.python-guide.org/dev/virtualenvs/ follow this link if you do not already know how.

cd into this folder then try:

virtualenv -p /usr/local/bin/python3.6 venv && source venv/bin/activate

pip3 install requirements.txt

First you must edit the file credentials.py and add your twitter api auth credentials

There are two scripts trendy.py and trends.py

I suggest running trendy.py first

python3 trendy.py

It gathers the "WOEID" for all major cities with trending twitter data. This script will print
the data to the console first and then save it as a json file "data.json". Why do we need this?
The twitter api needs a WOEID as input as we will see in the next script.


Now you can run python3 trends.py

You should be asked for a WOEID which you can select from your data.json file.
You will then be asked the name to save the data as for the WOEID you selected, it will hint you use a name ending in .json
It can be anything you like. Now you will have yourName.json with all the trending twitter topics for the WOEID you
selected. We value "tweet_volume" in the data as this tells us the trending power.

The twitter trend endpoints are rate limited, you can call new WOEID's but don't go calling the same data over and over, twitter gets mad.

What next? Now, you could run trends.py on a remote server once an hour and have the saved json output to say /var/www/html/data

We could then use the json data in another app.
