#!/usr/bin/env python
import argparse
from pychatgpt import Chat, Options
from os import getenv

def get_chatgpt_client():
    """Returns the ChatGPT client object after authenticating"""
    options = Options()
    username = getenv('CHATGPT_USERNAME')
    password = getenv('CHATGPT_PASSWORD')
    print(f"Authenticating in ChatGPT with {username}")
    chat = Chat(email=username, password=password, options=options)
    return chat

def get_sentence(topic):
    """Ask ChatGPT """
    chatgpt_client = get_chatgpt_client()
    sentence = f"tell me a short and meaningful sentence about {topic}"
    answer = chatgpt_client.ask(sentence)
    return answer

def parse_args():
    parser=argparse.ArgumentParser(
        add_help=True, 
        description="This script asks for a topic and retrieves a meaninful sentence for this topic from ChatGPT and then creates an images which is uploaded to instagram")
    parser.add_argument("-topic", type=str, help="enter a topic to generate an image with a sentence about it")
    args=parser.parse_args()
    return args

def main():
    inputs=parse_args()
    topic = inputs.topic
    answer = get_sentence(topic)
    print(answer)
    
if __name__ == '__main__':
    main()
