# Simple Snake Game
This game was created by Dang Ngoc Quan after participating in the [MIMPython course](https://mimpython.github.io/pythonSummerCourse/).

You can download game [here](https://drive.google.com/file/d/1mEbSQuIBeyk_tc6ggzzN9LWKi_LFyK83/view?usp=sharing). After downloading, extract the SimpleSnakeGame.zip file, then run the SimpleSnakeGame.exe file to play the game.

## Clone repository
```console
git clone https://github.com/dangngocquan/SimpleSnakeGame.git
```

## Install requirement libraries:
```console
pip install -r requirements.txt
```

# Game Introduction

https://user-images.githubusercontent.com/95365566/197530749-87260d61-d3bd-4a07-a84d-2b98e2c30421.mp4

## 1. Main Menu
Main menu include:
+ 1.1. Play game
+ 1.2. Account
+ 1.3. Options
+ 1.4. Statistics
+ 1.5. History
+ 1.6. About Game
+ 1.7. Quit game

https://user-images.githubusercontent.com/95365566/197693959-5cdd0c94-1988-4652-80c7-5cc7e06afa73.mp4

## 1.1. Play Game Menu
Play Game Menu include:
+ 1.1.1. New game
+ 1.1.2. Continue game
+ 1.1.3. Back

https://user-images.githubusercontent.com/95365566/197698033-248d8002-5776-4517-b3db-c5677aedc7d9.mp4

  ### 1.1.1. New Game
  Play new match game.
  
  https://user-images.githubusercontent.com/95365566/197701272-7b6eca05-b5b4-4283-a9ff-97850122368e.mp4

  https://user-images.githubusercontent.com/95365566/197777971-77505101-d5f2-47ac-914d-f7f5722cac57.mp4

  https://user-images.githubusercontent.com/95365566/197778465-c6538d22-ca5e-4c76-aac3-2a48c77fee2a.mp4

  ### 1.1.2. Continue Game
  You can continue to play the match game which you have not finished before quit game.
  
  https://user-images.githubusercontent.com/95365566/197701541-1aec58e9-40e0-4724-a1e7-070fe2d0c149.mp4
  
  ### Game over
  In game over screen, you can use key `'0', '1', '2', '3', '4', '5', '6'` to move your snake (only for loser - snake that died)
  
  https://user-images.githubusercontent.com/95365566/197777854-f7ac806a-c5b6-46cd-aad0-5e3ad96e3fde.mp4

## 1.2. Account Setting

Account Setting include:
+ 1.2.1. Existing account
+ 1.2.2. Create new account
+ 1.2.3. Back

https://user-images.githubusercontent.com/95365566/197698112-f8aa698e-7bfb-446a-be7e-03b167a81bb1.mp4

  ### 1.2.1. Existing account
  You can see statistics of current account, choose other account to play or delete some account if you want.
  
  Note: Account 'Nobody' is default account, so you can't remove it.
  
  https://user-images.githubusercontent.com/95365566/197702334-f8f94470-6629-4c96-9188-01f72c6ff195.mp4

  ### 1.2.2. Create new account
  You can create a new account if you want.
  
  https://user-images.githubusercontent.com/95365566/197702382-4f18c192-11da-4fab-832f-7181a663aebd.mp4


## 1.3. Options Menu
Options Menu include:
+ 1.3.1. Gamemode setting
+ 1.3.2. Game setting
+ 1.3.3. Sound setting
+ 1.3.4. Map setting
+ 1.3.5. Back

https://user-images.githubusercontent.com/95365566/197698174-02f638ff-ae5e-44f6-a6f6-f768f6ca612f.mp4

  ### 1.3.1. Gamemode setting
  You can setup some mode for game:
  + Number of player:
    + 1: One player control a snake, use `'A', 'W', 'S', 'D'` or `'UP', 'DOWN', 'LEFT', 'RIGHT'` to control the snake.
    + 2: Two player control two snakes, the first player use `'A', 'W', 'S', 'D'` to control the first snake, the second player use `'UP', 'DOWN', 'LEFT', 'RIGHT'` to              control the second snake
  + Auto speed up snake:
    + OFF: The speed of the snake will depend on the setting in `Game Setting Menu --> Snake move speed`
    + ON: The spped of the snake will auto increase when snake eat foods, not depend on the setting in `Game Setting Menu --> Snake move speed`
  + Target score: You wil win if your score greater or equal to Target score.
    + Minium target score is 100.
    + You can use wheel-up to increase Target score.
  + View control:
    + First-person view: Player only use `'A', 'D'` or `'LEFT', 'RIGHT'` to control snake.
    + Third-person view: Player use `'A', 'W', 'S', 'D'` or `'UP', 'DOWN', 'LEFT', 'RIGHT'` to control the snake.
  
  https://user-images.githubusercontent.com/95365566/197702442-4335ca2e-9afd-4edb-8a82-d9f9b2797ab9.mp4

  ### 1.3.2. Game setting
  You can setting the appearance ò the grid, the speed of snake when it move, drop, change color (animation speed), the number of max food in game, the speed of         animation of foods.
  + Grid: 
    + ON: Show grid when you play game.
    + OFF: Don't show grid.
  + Snake:
    + Move speed: 1-60, the speed of snake.
    + Drop speed: 1-60, the speed of snake when it drop (only appear when snake died).
    + Animation speed: 1-60, The change frame speed of snake.
  + Food:
    + Max food: 1-104, the number of maxium food in game.
    + Animation speed: 1-60, the change frame speed of food.
  
  https://user-images.githubusercontent.com/95365566/197702466-0cde0946-f1a5-4cac-bc65-02eb01893cb8.mp4
  
  ### 1.3.3. Sound setting
  You can choose the background music, change volume of music or change volume of sound (sound when press button, change button, sound when snake eat food, when game     over).
  + Music:
    + Music 0: Loafers - BoyWithUke
    + Music 1: Sweden - C418
  + Music volume: 0-100, volume of background music.
  + Sound volume: 0-100, sound when press button, change button, sound when snake eat food, when game over.
  
  https://user-images.githubusercontent.com/95365566/197702484-70cffbe8-8d94-444a-b692-b4a866fc29da.mp4
  
  ### 1.3.4. Map setting
  Map setting menu include:
  + 1.3.4.1. Existing Maps
  + 1.3.4.2. Create new map
  + 1.3.4.3. Back

  https://user-images.githubusercontent.com/95365566/197702523-5e21c204-627a-44fc-badc-f2b636070d21.mp4

   #### 1.3.4.1. Existing maps
   You can choose a map to play.
   
   https://user-images.githubusercontent.com/95365566/197702968-957a54f9-c52e-4666-ae97-12b46b16556a.mp4

   #### 1.3.4.2. Create new map
   If you want to create a new map for yourself, this is a good choice.

   https://user-images.githubusercontent.com/95365566/197702989-6a6b3cf9-bcad-49fd-8cfb-1824007f380d.mp4

## 1.4. Statistics
Show highest score and player's name, total time played in game, total match, ...

https://user-images.githubusercontent.com/95365566/197698242-ddcabe67-a716-4df3-989d-82957d7cf358.mp4


## 1.5. History
History play game.

https://user-images.githubusercontent.com/95365566/197698268-cdf8c8b7-84fc-4f7f-98dc-9a38c2315236.mp4


## 1.6. About Game Menu
Link of music, images, ...
Link of source code if someone need.

https://user-images.githubusercontent.com/95365566/197698284-8c1b6f92-b0dc-4c2c-804b-9ec911a41425.mp4

  ### Source code (if you want)
  
  https://user-images.githubusercontent.com/95365566/197704788-4810f852-e45c-46e8-99a3-a6e739b07adf.mp4

## 1.7. Quit Game
Yah, finally, quit game. Thank for play my game !!!
