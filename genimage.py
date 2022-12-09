#!/usr/bin/env python
import argparse
from apitemplate import APITemplateIO
from os import getenv

def get_apitemplate():
    apikey = getenv('APITEMPLATE_APIKEY')
    apitemplate = APITemplateIO(apikey)
    return apitemplate

def gen_img_with_text(image, topic, sentence, template_id=None, output_filename="output"):
    if template_id is None:
        template_id = getenv('APITEMPLATE_ID')
    apitemplate = get_apitemplate()
    data = {
        "overrides": [
            {
                "name": "background-image",
                "src": image
            },
            {
                "name": "topic",
                "text": f"*{topic}*"
            },
            {
                "name": "sentence",
                "text": sentence
             }
        ]
    }
    apitemplate.create_image(template_id, data, f"{output_filename}.jpg", f"{output_filename}.png")

def parse_args():
    parser=argparse.ArgumentParser(
        add_help=True,
        description="This script asks for a topic, description and image and generate an image with overprinted text by calling apitemplate.io")
    parser.add_argument("-topic", type=str, help="enter a topic")
    parser.add_argument("-sentence", type=str, help="enter a sentence")
    parser.add_argument("-image", type=str, help="enter a topic to generate an image with a sentence about it")
    args=parser.parse_args()
    return args

def main():
    inputs=parse_args()
    image = inputs.image
    topic = inputs.topic
    sentence = inputs.sentence
    gen_img_with_text(image=image, topic=topic, sentence=sentence)

if __name__ == '__main__':
    main()
