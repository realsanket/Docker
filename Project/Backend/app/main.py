#https://www.w3schools.com/colors/colors_picker.asp
#start=>ff3333
#end=>b30000
from typing import Union
import uvicorn
from fastapi import FastAPI
import webcolors
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "sasss"}




@app.get("/colorname/{rgb}")
def read_color(rgb: str):
    is_red = is_color_red(rgb)
    return {"is_red":is_red }


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#').upper()
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_distance(color1, color2):
    return sum((a - b) ** 2 for a, b in zip(color1, color2)) ** 0.5

def is_color_red(hex_color):
    red_rgb = hex_to_rgb("#FF0000")
    #add # to hex_color
    hex_color = "#" + hex_color
    target_rgb = hex_to_rgb(hex_color)
    distance = rgb_distance(red_rgb, target_rgb)
    if distance < 100:
        return True
    else:
        return False

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
