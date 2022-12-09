#!/usr/bin/env python
import argparse
from chat import get_sentence
from genimage import gen_img_with_text
from insta import post_story_to_insta
from stable_diffussion import get_image_from_stable_diffussion

import logging
logging.basicConfig(level=logging.INFO)

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
    logging.info(f"Calling ChatGPT to retrieve a sentence for the topic {topic}")
    sentence = get_sentence(topic)
    logging.info(f"""Sentence retrieved: "{sentence}" """)
    logging.info(f"Calling Replicate to generate an image for the previously generated sentence")
    # This is an example prompt to have a common style for all the generated photos
    # feel free to replace it
    suffix=",hyper realistic, 8k, epic composition, cinematic, octane render, artstation vista photography by Carr Clifton & Galen Rowell,"\
        "16K resolution, veduta photo by Dustin Lefevre & tdraw, 8k resolution, detailed painting by Ivan Shishkin, DeviantArt, Flickr,"\
        "rendered in Enscape, Miyazaki, Nausicaa Ghibli, Breath of The Wild, 4k detailed post processing, artstation, rendering by octane, unreal engine —ar 16:9"
    logging.info(f"Generating an image with Stable Diffussion for the retrieved sentence")
    background_image = get_image_from_stable_diffussion(sentence, suffix)
    full_topic = f"Topic of the day: {topic}"
    logging.info(f"Invoking apitemplate to add the topic and the generated sentence to the generated image.")    
    gen_img_with_text(background_image, full_topic, sentence)
    logging.info(f"Uploading final image to Instagram")
    post_story_to_insta("output.jpg")
    
if __name__ == '__main__':
    main()
