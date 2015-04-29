#FreshBlookNerd - FBNerd

###Brief
FBNerd is a python script program powered by [Python Facebook SDK](https://github.com/pythonforfacebook/facebook-sdk). 

It's a command line based program to post status, link, and photo post to user's wall only on Facebook platform.

The features are limited and really simple.

The purpose of creating of this program is to avoid the risk of experiencing the depressed state when browsing through the feeds or acidentally see certain post that could cause you depressed.

It acts solely on command line attached with long-lived access token (60 days). When I have a solution or time to add a log-in flow, then it can be used without any worry of re-acquire access token again.

###Installation
Make sure you have python installed on your system.

On Windows, follow steps in this [link](http://www.howtogeek.com/197947/how-to-install-python-on-windows/).

On Mac, and Linux system, normally you can use 

`sudo brew install python` or

`sudo apt-get intall python-pyudev`

Then follow the steps to install facebook-sdk package via this [link](http://facebook-sdk.readthedocs.org/en/latest/install.html).

###Usage
**Status post**

`python fbnerd.py -t status -m "Hello world!"`

or

`python fbnerd.py --type status --message "Hello world!"`

**Link post**

`python fbnerd.py -t link -m "Check out this link!" --attach_link "http://wasin.io" --attach_name "Wasin.io Website" --attach_caption "Caption" --attach_description "Description" --attach_picture "http://wasin.io/wp-content/uploads/2015/01/L-lYrqmV.png"`

: `-m` and `--attach_link` are required. The optional parameters are as follows.

* --attach_name
* --attach_caption
* --attach_description
* --attach_picture (image link)

**Photo post**

`python fbnerd.py -t photo -p "/Users/haxpor/image.jpg" -m "Check out this photo!"` 

or

`python fbnerd.py --type photo --path "/Users/haxpor/image.jpg" --message "Check out this photo!"`

### Contact
Just saying hi is pretty much welcome :)
Tweet me a shoutout [@haxpor](https://twitter.com/haxpor).
