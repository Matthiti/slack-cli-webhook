# slack-cli-webhook
Version 0.1.8

A Python package for sending messages to Slack

## Requirements
- Python 3.x
- pip for Python 3.x
- [Incoming webhook](https://api.slack.com/incoming-webhooks) for the Slack app

## Installation
To install with `pip`, run
```bash
pip install slack-cli-webhook
```
or
```bash
pip3 install slack-cli-webhook
```

Alternatively, the package can be installed from source:
```bash
python3 -m pip install --user --upgrade setuptools wheel
git clone https://github.com/Matthiti/slack-cli-webhook.git
cd slack-cli-webhook
python3 setup.py install
```
## Usage
```bash
usage: python -m slack-cli-webhook [-h] -m MESSAGE -w WEBHOOK

optional arguments:
  -h, --help            show this help message and exit
  -m MESSAGE, --message MESSAGE
                        message to send
  -w WEBHOOK, --webhook WEBHOOK
                        webhook to send to
```

### Send a message
A message can be specified with the `-m` or `--message` properties. Note that characters needs to be properly escaped. In addition to the message, a webhook needs to be provided to send the message to using `-w` or `--webhook`.

```bash
python -m slack-cli-webhook -m "Test" -w "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
```
