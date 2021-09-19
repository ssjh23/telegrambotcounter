from PIL import Image, ImageDraw, ImageFont
import os
from datetime import date
from pathlib import Path
import pyrebase
import fbaseConfig
import classes



def trash_summary():
    
    path_to_file_map = "C:/Users/seans/OneDrive/Documents/GitHub/telegrambotcounter/pictures/map.png"
    path_to_file_green = "C:/Users/seans/OneDrive/Documents/GitHub/telegrambotcounter/pictures/green.png"
    path_to_file_yellow = "C:/Users/seans/OneDrive/Documents/GitHub/telegrambotcounter/pictures/yellow.png"
    path_to_file_red = "C:/Users/seans/OneDrive/Documents/GitHub/telegrambotcounter/pictures/red.png"
    path_to_file_font = "C:/Users/seans/OneDrive/Documents/GitHub/telegrambotcounter/pictures\ARLRDBD.TTF"
    ## image coordinates for trash points - Woodlands
    location = "Woodlands Ave"
    blk728 = (1789,2145)
    blk701 = (1275,2493)
    blk745 = (715,1892)
    blk748 = (412,1386)
    blk759 = (1222,1345)
    blk721 = (2063,1528)
    blk714 = (2329,2108)
    blk789 = (3101,2096)
    blk787 = (2721,1561)
    blk786 = (2435,1050)
    blk769 = (1855,895)
    blk780 = (2729,397)
    blk782 = (3023,777)
    blk784 = (3385,940)
    blk734 = (1238,1827)

    blk_tuple = [blk701,blk714,blk721,blk728,blk734,blk745,blk748,blk759,
                 blk769,blk780,blk782,blk784,blk786,blk787,blk789]

    ### GET DATA FROM DATABASE
    ############################
    ## for one bin
    depth_bin = 22
    depth_kinda_empty = 0.5*depth_bin
    depth_notfull = 0.3*depth_bin

    firebaseConfig = fbaseConfig.firebaseConfig
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    bin = db.child("Bin1").get()
    database_value = None
    for data in bin.each():
        if data.key() == 'distance':
            database_value = float(data.val())

    block_example = ["to be replaced","full","kinda empty","not full","full","kinda empty","not full","full",
                       "kinda empty","not full","full","kinda empty","not full","full","kinda empty"]

    if database_value >= depth_kinda_empty:
            block_example[0] = 'kinda empty'
    elif database_value >= depth_notfull and database_value < depth_kinda_empty:
            block_example[0] = "not full"
    elif database_value >= 0 and database_value < depth_notfull:
            block_example[0] = "full"  

    
    WL_map = Image.open(path_to_file_map)
    edit_stack = WL_map.copy()

    for i in range(len(block_example)):
        if block_example[i] == "kinda empty":
            imgreen = Image.open(path_to_file_green)
            edit_stack.paste(imgreen,blk_tuple[i])
            edit_stack.save("WLpresummary.png")          

        elif block_example[i] == "not full":
            imyellow = Image.open(path_to_file_yellow)
            edit_stack.paste(imyellow,blk_tuple[i])
            edit_stack.save("WLpresummary.png")
            

        elif block_example[i] == "full":
            imred = Image.open(path_to_file_red)
            edit_stack.paste(imred,blk_tuple[i])
            edit_stack.save("WLpresummary.png")    
            

    title_font = ImageFont.truetype(path_to_file_font,150)
    today = date.today()
    d4 = today.strftime("%b-%d-%Y")
    draw = ImageDraw.Draw(edit_stack)
    draw.text((522,472), d4,(0,0,0), font = title_font)
    file_name = "WLsummary_" + d4 + ".png"
    done_im = edit_stack.copy()
    done_im.save(file_name)

    os.remove("WLpresummary.png")
    print("File Removed!")
