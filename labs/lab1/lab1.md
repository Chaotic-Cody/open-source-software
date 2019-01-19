### Lab1.md

## Open Source Definition
This strict criteria for is important for writing and maintaining open source projects, with proper licensing being a high priority.

## Answering Questions in a Helpful Way
1. Don't simply give them the answer to a bad question. Giving someone free code will condition them to continue making bad questions in the future. Give them a gentle nudge in the right direction, and have them come back later when they've research the topic more.
2. Provide step-by-step instructions that are general enough to help more than just the asker. This increases the utility of your answer, and allows it to be useful to more than a single person.

## Free Culture Chapter 3
First, I would like to say that what the RIAA has done is completely bull, and that the American legal system is pretty broken. Jesse built upon the open source content of an older search engine as a pet project. He fixed a bug that caused searches that queried powered down machines to crash the user's system by allowing the user to manually check if the system in question was still actively on the network. To be clear, Jesse continued work on a search engine that he didn't build from the ground up, made it successful, and then proceeded to be sued by the RIAA for files found on other user's local machines that were linked via the search engine. After severe strongarming, Jesse's only remaining options were to fight the case and go bankrupt, or settle and lose all of his savings, along with the placement of severe technological restrictions for the rest of his life. 

## Tree
![Tree](images/Tree.png)

## Regex
![Problem 1](images/RegexOneP1.png)
![Problem 2](images/RegexOneP2.png)
![Problem 3](images/RegexOneP3.png)
![Problem 4](images/RegexOneP4.png)
![Problem 5](images/RegexOneP5.png)
![Problem 6](images/RegexOneP6.png)
![Problem 7](images/RegexOneP7.png)

## Regex Crossword
![Problem 1](images/CrosswordP1.png)
![Problem 2](images/CrosswordP2.png)
![Problem 3](images/CrosswordP3.png)
![Problem 4](images/CrosswordP4.png)

## Blockly
![Maze Level 10](images/BlocklyMaze10.png)

## Reflection
Open Source Project: [Aurora](https://github.com/evaera/Aurora)
I am a hobby game developer, and frequently use Roblox for rapid prototyping and concept work. Making games in Roblox is currently very unstructured, with every developer coming up with their own tools and workflows on the platform. I believe that it would make it easier for all game developers on Roblox if there were more open source toolkits to provide a foundation for organization and good coding practices. Since the demographic consists predominantly of younger people, I believe it is especially important to encourage good coding practices through the use of frameworks and modules. 

Aurora is an open source project run by my friend Eryn. Aurora aims to tackle the common game development problem of stacking effects and status tracking in multiplayer online games. For example, say you get a 10% damage buff and a 5% damage debuff, you would normally have to manually decide how to handle these interactions, and to ensure that they are secure along the client<->server boundary. With Aurora, you can define Agents for each player, and create any number of Auras for each agent. In this case, we would define an Aura for the 10% damage buff, and another for the 5% damage debuff, and then Aurora would handle the number crunching. The default behaviour is to simply return the smallest value, but custom parameters can be passed in to override the defaults. 