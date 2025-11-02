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

#### To install/play:
1. Setup a python environment in your VS code
2. Download py file from my github
3. Save, run, and enjoy!

Otherwise, just copy it into any python IED and run it.

To know more visit my medium page: [medium](https://medium.com/@sofiew0504/cif-projects-week-two-a2a0e84cd4d1)

## Your turn
Now it's your turn to try, ff this sounds intresting to you or someone you know, you can sign up for classes here: [cif sign ups](https://www.itisfun.org/)


