<h1 align="center" style="border-bottom: none">
    <b>PickMeGarb</b>
    <br>
    WhatTheHack 2021
    <br>
</h1>

<p align="center">
   A user-friendly IOT system that aims to boost the efficiencies of the waste-collection process in Singapore 
</p>

<br>

<div align="center">

![Pythontelegramapi](https://img.shields.io/badge/PythonTelegramAPI-%2320232a.svg?style=for-the-badge&logo=Telegram&logoColor=%2361DAFB)
![Firebase](https://img.shields.io/badge/firebase-orange.svg?style=for-the-badge&logo=firebase&logoColor=white)
![Google maps API](https://img.shields.io/badge/GoogleMapsapi-google?style=for-the-badge&logo=google-maps&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
</div>

# Resources
- [DevPost](https://devpost.com/software/pickmegarb)

# File Directories
```
📦backend              # AWS backend lambda functions
 ┣ 📂add-order
 ┣ 📂get-all-orders
 ┣ 📂login
 ┣ 📂publish-photo
 ┣ 📂register 
 ┣ 📂validate-order
 📦frontend 
 ┣ 📂public            # images used for frontend
 ┣ 📂src
 ┃ ┣ 📂api             # custom api function
 ┃ ┣ 📂components      # building blocks for webpage
 ┃ ┣ 📂icons           # icons used for frontend
 ┃ ┣ 📂pages           # main webpages: login, register, dashboard, add order
 ┃ ┣ 📂routes          # routing for logged in / non-logged in users
 ┃ ┗ 📂service         # user authentication function
 📦hardware            # configuration for solonoid lock + keypad
 ┃ ┣ 📂esp32-cam       # esp32 cam code
 ┃ ┣ 📂raspberry-pi    # raspberry pi configuration
 📦postman             # sample postman calls for backend api
 ```



