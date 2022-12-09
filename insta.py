#!/usr/bin/env python3
import argparse
from os import getenv
from instagrapi import Client

def get_insta_bot(settings_file=".settings"):
    username = getenv('INSTA_USERNAME')
    password = getenv('INSTA_PASSWORD')
    print(f"Authenticating in Instagram with {username}")
    api = Client()
    api.login(username, password)
    return api

def post_story_to_insta(image_path):
    insta_bot = get_insta_bot()
    insta_bot.photo_upload_to_story(image_path)

def parse_args():
    parser=argparse.ArgumentParser(
        add_help=True,
        description="This script asks for a topic and retrieves a meaninful sentence for this topic from ChatGPT and then creates an images which is uploaded to instagram")
    parser.add_argument("-image", type=str, help="enter an image to upload it to instagram")
    args=parser.parse_args()
    return args

def main():
    inputs=parse_args()
    image_path = inputs.image
    post_story_to_insta(image_path)

if __name__ == '__main__':
    main()
