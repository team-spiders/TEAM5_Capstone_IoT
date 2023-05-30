# TEAM5_Capstone_IoT

## Why baby monitoring?? ( Choosing idea for product)
In today's time, the need for a baby monitoring device is crucial. Without it, caregivers face several problems. The absence of a monitoring device means caregivers cannot promptly respond to the baby's needs or monitor their well-being. This can lead to increased risks and safety concerns. Furthermore, caregivers experience heightened stress and anxiety due to the constant worry about the baby's safety. The lack of a monitoring device also limits caregivers' flexibility and freedom to tend to other tasks or have personal time. Overall, not having a baby monitoring device compromises the caregivers' ability to provide timely care and attention, posing risks to the baby's safety and the well-being of the caregivers themselves.

The solution for these problems is to build a proper monitoring device ensuring safety of the baby.

## Challenges (software and product design)
1) OS was pre-installed. I just had to configure some settings

2) However, I had problems while installing opencv. I don't exactly remember what was the error. I installed all the packages but after cmake part, an error emerged

3) Made research on how the actual product could look like before we were given the device. Picked a bunch of similar existing products for submission

4) After we were given the device I had to change the design model since the actual device was different from what was expected. So another research was made to make the actual 3D design

## Challenges of the Project (Engineering Aspect)
Here are some challenges we faced while working with Baby Monitoring System.

  1) Power Management: Raspberry Pi and the connected peripherals require a stable power supply. Ensuring sufficient power is always a challenge considering the need for continuous monitoring.

  2)  Hardware Integration: While connecting sensors to raspberry pi, careful attention was needed as correct wiring is necessary.

  3)  Real-time processing: Due to Raspberry Pi's processing power and memory limitations pose challenges in achieving smooth and responsive video processing. Therefore, for our product, we initially plan to snapshot the frame when motion is detected and send the image using a telegram bot, reducing the processing burden.

  4)  Network Connectivity: Enabling remote access and monitoring requires configuring network settings and handling potential network interruptions and ensuring secure data transmission. 
  
  ## Setup for own Telegram-Bot
  1) First step would be to get the telegram app and search for "BotFather" bot in telegram searching for "@BotFather"

  2) Then, started a chat with BotFather by clicking on it and then clicking the "Start" button.

  3) To create a new bot, I typed "/newbot" in the chat with BotFather and followed the instructions. I provided a name for my bot and a username that ended with "bot". For example, I used "Telebot" as the name and "Alert_bot" as the username. (Draft name and bot username)

  4) Once I provided the necessary information, BotFather generated an API token for my bot. This token was required for accessing the Telegram Bot API and interacting with my bot programmatically. I made sure to copy and securely store the API token.

  5) After that, these libraries were installed within raspberry pi to have full access:  python-telegram-bot , pip install python-telegram-bot in my terminal.

Since API token is used to gain full access of the bot, it is important to keep that confidential.

![image](https://github.com/team-spiders/TEAM5_Capstone_IoT/assets/115747921/1205b22d-5f35-4d3c-ae05-1b0b17457a1d)

## Research on possible App-Integration / Web Interface
Remote monitoring is one of the critical features in collaboration with other features: Such as Motion Detection, Temperature Sensor, etc. I did some research on this topic and found some conclusions as follow:
To make remote monitoring possible, there are some steps we need to work on: 

a. Streaming Service

b. Web-Interface or Mobile App

Developing a Web-interface or Mobile App would be a complete project in itself. Hence, it would be a challenge for us to carry out in short time frame with limited sources. 
However, the steps below for Mobile App integration based on the web research can be our potential future project. 

a. Selecting a programming language and interface

b. Designing the user interface

c. Setup a development environment

d. Implementing video streaming

e. Integrating audio streaming 

f. User authenticity and security
