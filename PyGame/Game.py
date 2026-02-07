import pygame
from tkinter import *
from pygame.locals import *
import subprocess
import shlex

app_path_mc = "/Applications/Minecraft.app"

# The command to run in the terminal
cmd_mc = f"open -a '{app_path_mc}'"

# Use shlex.split to handle spaces in the path correctly
cmd_parts_mc = shlex.split(cmd_mc)

app_path_chrome = "/Applications/Google Chrome.app"
url = "chrome://newtab" # Optional: specify a URL to open
yw_url="https://www.youngwonks.com/students_dashboard"

# The command to run in the terminal
cmd_chrome = f"open -a '{app_path_chrome}' {url}"

# Use shlex.split to handle spaces in the path correctly
cmd_parts_chrome = shlex.split(cmd_chrome)
#################################################################################
# The command to run in the terminal
cmd_yw = f"open -a '{app_path_chrome}' {yw_url}"

# Use shlex.split to handle spaces in the path correctly
cmd_parts_yw = shlex.split(cmd_yw)


pygame.init()
screen = pygame.display.set_mode((1920,1030))
pygame.display.set_caption("Game!!")
logo = pygame.image.load("/Users/naom/Downloads/logo.png")
chrome = pygame.image.load("/Users/naom/Downloads/Google_Chrome-Logo.png")
chrome=pygame.transform.scale(chrome, (150,100))
mc = pygame.image.load("/Users/naom/Downloads/erasebg-transformed.webp")
mc=pygame.transform.scale(mc, (130,100))
yw = pygame.image.load("/Users/naom/Downloads/ms.jpg")
bg = pygame.image.load("/Users/naom/Desktop/Waves (1).png")
bg=pygame.transform.scale(bg, (1920,1060))
running=True
while running:
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,(238, 74, 39),(0,980,1920,50))
    screen.blit(logo,(10,985))
    screen.blit(chrome, (0,10))
    screen.blit(mc, (10,105))
    screen.blit(yw, (20,210))
    for event in pygame.event.get():
        if event.type == QUIT:
            running=False
        if event.type == MOUSEBUTTONDOWN:
            x,y=event.pos
            if x>= 0 and x<=106 and y<= 94 and y>=10:
                try:
    # Run the command
                    subprocess.run(cmd_parts_chrome, check=True)
                    print(f"Opened {app_path_chrome}")
                except FileNotFoundError:
                    print(f"Error: Application not found at {app_path_chrome}")
                except subprocess.CalledProcessError as e:
                    print(f"Error running command: {e}")
                except PermissionError as e:
                    # This specific error is less likely with the 'open' command but included for completeness
                    print(f"Permission denied: {e}")
            elif x>=20 and x <=140 and y>=150 and y<=200:
                try:
    # Run the command
                    subprocess.run(cmd_parts_mc, check=True)
                    print(f"Opened {app_path_mc}")
                except FileNotFoundError:
                    print(f"Error: Application not found at {app_path_mc}")
                except subprocess.CalledProcessError as e:
                    print(f"Error running command: {e}")
                except PermissionError as e:
                    # This specific error is less likely with the 'open' command but included for completeness
                    print(f"Permission denied: {e}")
            elif x>=20 and x<=120 and y>=210 and y<=312:
                try:
    # Run the command
                    subprocess.run(cmd_parts_yw, check=True)
                    print(f"Opened {app_path_chrome} and Opened {yw_url}")
                except FileNotFoundError:
                    print(f"Error: Application not found at {app_path_chrome}")
                except subprocess.CalledProcessError as e:
                    print(f"Error running command: {e}")
                except PermissionError as e:
                    # This specific error is less likely with the 'open' command but included for completeness
                    print(f"Permission denied: {e}")
            print(event.pos)
    pygame.display.update()