# CIF Junior


## Introduction
CIF or Coding Is Fun is a public program to help young coders to learn programming via various fun projects, through different coding languages and programs like:

- Python
- Markdown
- Mermaid
- C++
- Html
- Javascrip
- CSS

And much more.

We cover six prjects in 20 units, all of which, the process, flowchart, and code will be uploaded to this repository.
## Projects
### Project 1: Number Guessing Game

#### What it is:
As the name suggests, it's a simple number guessing game, where you would enter a range you would like to guess from. As well as if you would like to limit tries and how many - meaning you choose the difficulty you want. The system randomly generates the number and with hints you would start guessing.

#### How it's created:
1. Simply lay out your basic steps in a flowchart:

``` mermaid
graph TD
  A[start] --> B[generate random number] --> C[ask user to input their guess] --> D{matched?};
  D --> E[print you win] --> G[end];
  D --> F[print you lose] --> G[end];
```

2. Code the simpler ideas, before one by one adding more features and ideas:

#### How to play:
For my game, I added these features:
- Asking for lower and higher boundaries. If user enters a non-integer it'll result an error and loop back to ask again.
- Asking if user would like to limit their tries + how many
  - if user says no, they get infinite tries
<img width="600" height="201.75" alt="image" src="https://github.com/user-attachments/assets/064f9f5a-1253-4989-8d84-5e4952dd08ec" />

- Let user be able to quit when they want
- Give hints comparing the guess to the chosen number
<img width="600" height="174" alt="image" src="https://github.com/user-attachments/assets/2fdb522b-1b5f-4bb5-a24e-4c822bf26401" />


- Let user give a rating of the game
- Option to play another round

To know more visit my medium page: [CIF Projects #1 — Number Guessing Game](https://medium.com/@sofiew0504/cif-projects-week-two-a2a0e84cd4d1)

### Project 2: TBAG

#### What it is:
TBAG stands for a text based adventure game. Meaning, the user interacts with a game through text only, and the outcomes depends on each choice the user makes. It can be a point scoring trivia game, or a choose your own adventure one with a storyline. Which is what I've created here.

#### How it's created:
The main steps we learned about can be concluded to five simple stages:
1. Analyze the flow - as always, start a simple flowchart. Using Lucidchart or draw.io, think the overall pattern of your game/code.
2. Program the flow - now turn your thoughts into codes. Add comments either to remind yourself to add something later or simply for the organization.
3. Define the functions - we learned all about what functions are and how to define them. Here is when you would start thinking which steps of the code you want to make function of and how.
4. Call the functions - after defining it, you'll be able to call/use it later on in the code without having to copy huge blocks of code around.
5. Refine the code - here in the final stage, you would polish it and code any thoughts you added as comments in step two. and tada!

#### How to play:
I created a choose you own adventure typed game.

Backgrounder: You wake up one morning in a magical world. From a owl's scroll, you have been called to save the royal princess from the evil witch! You'll face monsters and magical elements (and bonding with the owl, of course) and hopefully survive this journey!

p.s. you start with nine hearts, each choice end you up with a different number of lives left, good luck adventurer!

<img width="800" height="38" alt="image" src="https://github.com/user-attachments/assets/e85130d3-43c9-4436-a112-1c160155193b" />


<img width="1200" height="121" alt="image" src="https://github.com/user-attachments/assets/da0915a4-d80e-4b54-9bc4-93681fff1a14" />


<img width="1200" height="67" alt="image" src="https://github.com/user-attachments/assets/2e711efe-1484-417d-8fb0-8d621b3e2f71" />
Better luck next time!

To know more visit my medium page: [CIF Projects #2 — Text Based Adventure Game](https://medium.com/@sofiew0504/cif-projects-2-text-based-adventure-game-109e891b54f0)

### Project 3: Turtle Fireworks

#### What it is:
Turtle is built in function in python that creates a digital turtle that'll draw shapes or whatever you code it to. Our project this time is to create a firework scene in the night sky.

#### How it's created:
As this project isn't exactly a game, we didn't need a flowchart. But we did start from the basics by planning out the simple steps for a turtle to draw our vision. Before the actual fireworks, we went through a bunch exercises from a simple polygon to drawing complicated optical illusion like shapes.

<img width="480" height="444" alt="image" src="https://github.com/user-attachments/assets/350cd75e-39bd-4f5c-9e5e-cb6b8cb23c77" />

To know more visit my medium page: [CIF Project #3 - Turtle Fireworks](https://medium.com/@sofiew0504/cif-projects-3-32462f9d358e?postPublishedType=initial)

### Project 4: Pygame
#### What it is:
PyGame is a set of built in Python module that allows you to create and visualze games. By changing the frame every few seconds, you can make it look like things are coming to live and moving around.

#### How it's created:
I first planned out what the basic objective of the game is, which is a platformer game to get to the top of the screen for a prize. I sketched out where things would be and what it would look like on paper to have a better layout, then started coding. It begun with finding pictures and creating this controllable variable of our main character Mr Capybara. Then came ledges or clouds he could jump on to reach his carrot. Then, more ideas started coming, and I added them one by one. For example:
- adding bullets as obstacles
- an instructions screen
etc.

<img width="668" height="1046" alt="Screenshot 2026-01-29 at 5 30 48 PM" src="https://github.com/user-attachments/assets/b76a52e5-89a2-4689-842a-025b24c77832" />

Almost 90% of this program is based on the collision detection function which allow something to happen when two things collide. For example, winning or losing the game by colling with carrots and bullets, or the buttons to start the game that collides with your mouse.

#### How to play:
The goal of the first version is to simply jump on the moving clouds to reach a carrot to win. The second/final version is a never ending climb that keeps track of your highscores. Using arrow keys, you can control Mr Capybara to land on clouds at the right time while avoiding the bullets. The black bullets are harmless other than push you aside a few pixels, the red one however, is deadly.

To know more visit my medium page: [CIF Project #4 - Pygame](https://medium.com/@sofiew0504/cif-projects-4-pygame-c31ee3a5ab4a?postPublishedType=repub)

### Project 5: Physical Computing
#### What it is:
Physical computing bridges the gap between online coding and real-world technologies. Using wires and sensors, you can learn to build your own systems that sends data directly to your devices.

#### How it's created:
With the basic items like jumper wires and bread boards we assemebled it to become a mini dector that senses data around it. Using things like ultrasound and infrared light, it can send data as to how close the nearest object is and if it detects motion within its radar. Then, a website was created using HTML that makes the data easier to read instead of endless scrolling pages.

<img alt="IMG_212" src="https://github.com/user-attachments/assets/5363cae9-acda-48be-9013-927fb92d4b7d" />

### To install/play:
For most of these games, if you want to try yourself: 
1. Setup a python environment in your VS code
2. Download py file from my github
3. Save, run, and enjoy!

Otherwise, just copy it into any python IED and run it.

For special ones like turtle and pygame, you can't run in any python IED as most don't support the modules. For pygame, you'll also need to download the images attached to this github in order to play the game with visuals.

## Your turn
Now it's your turn to try, if this sounds intresting to you or someone you know, you can sign up for classes here: [cif sign ups](https://www.itisfun.org/)
