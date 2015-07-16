# RailDisplay
Library for displaying UK train times 

This library is designed for displaying UK train times on a raspberry pi with a [Display-O-Tron 3000](http://shop.pimoroni.com/products/displayotron-3000)


## Prerequisite

Do NOT run any of the below commands if you are not sure what they do, especially piping curl requests to bash.
These are the instructions provided on the external projects sites.

### Install Python 2 (The dot3k lib is not compatible with Python 3 at the time of writing)
### Install pip
```bash
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
```
### Install the [nre-darwin package](https://pypi.python.org/pypi/nre-darwin-py)
```bash
# May be needed
sudo easy_install -U setuptools
```

```bash
sudo pip install nre-darwin-py
```

### Install the [dot3k lib](https://github.com/pimoroni/dot3k) (If using Display-O-Tron)
```bash
curl get.pimoroni.com/dot3k | bash
```

### Get your API Key
You can get an API Key from the [NRE Developer Site](http://www.nationalrail.co.uk/46391.aspx)

## Examples

Please see [example.py](example.py) for an example of usage


## Other

![Data powered by National Rail Enquiries ](/NRE_Powered_logo.jpg)
