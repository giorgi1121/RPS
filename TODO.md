we have Rock, Paper, Scissor game. user have to input his/her choice from Rock, Paper or Scissor and computer also choose one randomly from them. if computer and user choices will be same then it's tie, but if computer choose scissor and user choose paper or computer choose rock and user choose scissor or computer choose paper and user choose rock then computer gets point, otherwise user gets point. The game continues until 3, 5 or 7. Whoever reaches the required number of points first wins. If user does not want to play anymore he/she can input "Stop game" and he/she loses the game.

# Rock Paper Scissor

## Questions
1. How many points are required to reach?
2. What is users choices?
3. What is computers choices?
4. What is player points?
5. What is computer points?
6. Does player want to play again?

## Technical assignment

we have Rock, Paper, Scissor game. user have to input his/her choice from Rock, Paper or Scissor and computer also choose one randomly from them. if computer and user choises will be same then it's tie, but if computer choose scissor and user choose paper or computer choose rock and user choose scissor or computer choose paper and user choose rock then computer gets point, otherwise user gets point. The game continues until 3, 5 or 7. Whoever reaches the required number of points first wins. If user does not want to play anymore he/she can input "Stop game" and he/she loses the game.
### Inputs, Processes, Outputs
Nouns:
1. required points
2. player choice
3. computer choice
4. win/lose/tie
5. player points
6. computer points
7. win

Verbs:
1. prompts user for required points
2. prompts user for choice
3. randomise computer choice
4. calculate points
5. revealing the winner
6. display points
7. display winner 
8. ask user if wants to play again
 
Inputs: 
1. required points
2. users choice
3. users wish to play again

Processes:
1. randomise computer choice
2. calculate points
3. revealing the winner

Output:
1. computer points
2. player points
3. winner

## Pseudocode
Rock Paper Scissor:

import random module

define main function which prompts user required points, prompts for choice and call "computer_choice" function

1. I have to add functionality which restrict amount of required points
2. I can add functionality which counts points in general according to wins 
3. I can add A function to display the game rules: You could create a function that displays the rules of the game (i.e., which move beats which). 
4. I can add Allow for more than two players: Instead of just a player and a computer, you could allow for multiple human players to play against each other, or even have multiple computer players with different levels of difficulty. 
5. Add more choices: In addition to rock, paper, and scissors, you could add other choices such as lizard and Spock (popularized by the TV show The Big Bang Theory), or create your own custom choices. 
6. Implement different game modes: You could create different game modes with different rules, such as a timed mode where players have to make their choice within a certain amount of time, or a sudden death mode where the first player to win a round wins the game.
7. Add graphics: You could add graphics to your game to make it more visually appealing, such as displaying the player's and computer's choices as images instead of text.
8. Add sound effects and music: Adding sound effects and music can enhance the overall user experience and make the game more engaging.

Multiplayer mode: Allow two players to compete against each other instead of playing against the computer.
Difficulty levels: Allow the user to choose between easy, medium, and hard difficulty levels with varying levels of AI intelligence.
Score tracking: Keep track of the overall win-loss record between the player and the computer.
GUI: Implement a graphical user interface to make the game more visually appealing.
Sound effects: Add sound effects to make the game more immersive.

make separate function for music
