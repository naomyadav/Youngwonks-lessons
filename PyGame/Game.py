import pygame
from tkinter import *
from pygame.locals import *
import subprocess
import shlex
import pyglet
from pyglet.window import mouse



import datetime
import calendar
print(calendar.month(2026,2))
if True:
    app_path_mc = "/Applications/Minecraft.app"
    # The command to run in the terminal
    cmd_mc = f"open -a '{app_path_mc}'"
    # Use shlex.split to handle spaces in the path correctly
    cmd_parts_mc = shlex.split(cmd_mc)
    print(cmd_parts_mc)

    app_path_chrome = "/Applications/Google Chrome.app"
    url = "chrome://newtab" # Optional: specify a URL to open
    yw_url="https://www.youngwonks.com/students_dashboard"
    logo_url="https://www.google.com/search?q=The+Lab+City&stick=H4sIAAAAAAAA_-NgU1I1qLAwsEhLMk00TkpNNU9KNEmxMqhITDOwTEs1MDVPMTYyNjAwXcTKE5KRquCTmKTgnFlSCQCzzMefOAAAAA&hl=en&mat=CaLPhkNNBkALElcBTVDHnvSK6KH3cgKejyzy6OZmgyJ7YXME7T4W3Vmsma9nb1jd_BABeM4FQYlTP3h6r5_LTwgDZ3irUchqlpmMEpFg8Cp6CrQXpt6ic4lcS_nomILm9n4&authuser=1&ved=2ahUKEwj67eC-7MiSAxVRx-YEHWnoIoAQ-MgIegQILBAf"
    # The command to run in the terminal
    cmd_chrome = f"open -a '{app_path_chrome}' {url}"
    # Use shlex.split to handle spaces in the path correctly
    cmd_parts_chrome = shlex.split(cmd_chrome)
    print(cmd_parts_chrome)

    # The command to run in the terminal
    cmd_yw = f"open -a '{app_path_chrome}' {yw_url}"
    # Use shlex.split to handle spaces in the path correctly
    cmd_parts_yw = shlex.split(cmd_yw)
    print(cmd_parts_yw)
    # The command to run in the terminal
    cmd_logo = f"open -a '{app_path_chrome}' {logo_url}"
    # Use shlex.split to handle spaces in the path correctly
    cmd_parts_logo = shlex.split(cmd_logo)
    print(cmd_parts_logo)

    # The command to run in the terminal
    cmd_yw = f"open -a '{app_path_chrome}' {yw_url}"
    # Use shlex.split to handle spaces in the path correctly
    cmd_parts_yw = shlex.split(cmd_yw)
    print(cmd_parts_yw)

pygame.init()



# Get current month
today = datetime.date.today()
year = today.year
month = today.month


cal_text = calendar.month(year, month)
cal_lines = cal_text.split("\n")
WIDTH,HEIGHT=1920,1030
screen = pygame.display.set_mode((WIDTH,HEIGHT),)
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
#display text on window def show_text(mig.x.y.color):
def show_text(msg, x, y, color, size):
    fontobj= pygame.font.SysFont("freesans", size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))

font = pygame.font.SysFont("comfortaa", 24)
title_font = pygame.font.SysFont("comfortaa", 36, bold=True)

def draw_calendar(surface, year, month, x_offset, y_offset):
    """
    surface: The Pygame screen or surface to draw on.
    x_offset, y_offset: The top-left starting position for the calendar.
    """
    # 1. Draw Header (Month and Year)
    month_name = calendar.month_name[month]
    title = title_font.render(f"{month_name} {year}", True, (0, 0, 0))
    # Place title centered relative to the calendar width (~525px)
    surface.blit(title, (x_offset + 180, y_offset))
    
    # 2. Draw Weekday Labels
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, day in enumerate(days):
        txt = font.render(day, True, (100, 100, 100))
        surface.blit(txt, (x_offset + i * 75, y_offset + 50))

    # 3. Draw the Days Grid
    cal = calendar.monthcalendar(year, month)
    for row_idx, week in enumerate(cal):
        for col_idx, day in enumerate(week):
            if day != 0:
                # Add x_offset and y_offset to the rectangle position
                rect_x = x_offset + (col_idx * 75)
                rect_y = y_offset + 80 + (row_idx * 60)
                
                rect = pygame.Rect(rect_x, rect_y, 60, 50)
                pygame.draw.rect(surface, (230, 230, 230), rect)
                
                date_txt = font.render(str(day), True, (0, 0, 0))
                surface.blit(date_txt, (rect.x + 10, rect.y + 10))
custom_cursor = pygame.image.load("/Users/naom/Downloads/Rainbow Arrow & Hand 3D/Rainbow Arrow & Hand 3D--cursor--SweezyCursors.png") 
pygame.mouse.set_visible(False)
custom_cursor = pygame.transform.scale(custom_cursor,(50,50))

while running:
    now = datetime.datetime.now()
    curr_year, curr_month = now.year, now.month
    
    
    
    datetime_text = now.strftime("%A, %B %d %m/%d/%Y %I:%M:%S:%f %p")
    date_text = now.strftime("%D")
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,(255,255,255),(1273, 493, 10000,10000000),0,-1,-1,-1,-1,-1)
    draw_calendar(screen, curr_year, curr_month, 1312, 524)
    pygame.draw.rect(screen,(238, 74, 39),(0,980,1920,50))
    
    screen.blit(logo,(10,985))
    screen.blit(chrome, (0,10))
    screen.blit(mc, (10,105))
    screen.blit(yw, (20,210))
    show_text (datetime_text,1070, 991,(255,255,255),32)
    for event in pygame.event.get():
        if event.type == QUIT:
            running=False
        if event.type == MOUSEBUTTONDOWN:
            x,y=event.pos
            if x>= 0 and x<=106 and y<= 94 and y>=10:
                try:
                    subprocess.run(cmd_parts_chrome, check=True)
                    print(f"Opened {app_path_chrome}")
                except FileNotFoundError:
                    print(f"Error: Application not found at {app_path_chrome}")
                except subprocess.CalledProcessError as e:
                    print(f"Error running command: {e}")
                except PermissionError as e:
                    # This specific error is less likely with the 'open' command but included for completeness
                    print(f"Permission denied: {e}")
            elif x>=38 and x <=109 and y>=113 and y<=202:
                try:
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
                    subprocess.run(cmd_parts_yw, check=True)
                    print(f"Opened {app_path_chrome} and Opened {yw_url}")
                except FileNotFoundError:
                    print(f"Error: Application not found at {app_path_chrome}")
                except subprocess.CalledProcessError as e:
                    print(f"Error running command: {e}")
                except PermissionError as e:
                    # This specific error is less likely with the 'open' command but included for completeness
                    print(f"Permission denied: {e}")
            elif x>=10 and x<=50 and y>=985 and y<=1026:
                try:
                    subprocess.run(cmd_parts_logo, check=True)
                    print(f"Opened {app_path_chrome} and Opened {logo_url}")
                except FileNotFoundError:
                    print(f"Error: Application not found at {app_path_chrome}")
                except subprocess.CalledProcessError as e:
                    print(f"Error running command: {e}")
                except PermissionError as e:
                    # This specific error is less likely with the 'open' command but included for completeness
                    print(f"Permission denied: {e}")
              
            if event.type==MOUSEMOTION:
                x,y = pygame.mouse.get_pos()
                if x>= 0 and x<=106 and y<= 94 and y>=10:
                    custom_cursor = pygame.image.load("/Users/naom/Downloads/Rainbow Arrow & Hand 3D/Rainbow Arrow & Hand 3D--pointer--SweezyCursors.png") 
                    pygame.mouse.set_visible(False)
                    custom_cursor = pygame.transform.scale(custom_cursor,(50,50))
            print(event.pos)
    show_text(f"{date_text}",1389, 911,(0,0,0),50)

    screen.blit(custom_cursor, (pygame.mouse.get_pos()))
    pygame.display.update()