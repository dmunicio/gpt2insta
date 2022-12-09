#!/usr/bin/env python3
import replicate
import webbrowser

def get_image_from_stable_diffussion(prompt, suffix=""):
    model = replicate.models.get("stability-ai/stable-diffusion")
    full_prompt=f"{prompt}{suffix}"
    output_url = model.predict(prompt=full_prompt)
    return output_url

def main():
    output_url = get_image_from_stable_diffussion(prompt="electric sheep, neon, synthwave")[0]
    print(output_url)
    webbrowser.open(output_url)

if __name__ == '__main__':
    main()
