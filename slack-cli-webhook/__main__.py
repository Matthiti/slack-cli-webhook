# __main__.py
from slack_cli import SlackCLI
from argparse import ArgumentParser
import sys


def main():
    parser = ArgumentParser()
    parser.add_argument("-m", "--message", dest="message", help="message to send", required=True)
    parser.add_argument("-w", "--webhook", dest="webhook", help="webhook to send to", required=True)
    args = parser.parse_args()
    slack_cli = SlackCLI(args.webhook)
    if slack_cli.send_message(args.message):
        print("Message successfully sent.")
        sys.exit(0)
    else:
        print("Sending message failed, please try again later.")
        sys.exit(1)


if __name__ == "__main__":
    main()
