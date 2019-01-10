# CS342 Design Patterns
## Fall 2018
### PROJECT 4 README FILE

## DESIGN OVERVIEW:
- State each design pattern used (if any)
- Brief (< 5 sentences) description of your overall design
- Description of your search algorithm

## KNOWN BUGS AND INCOMPLETE PARTS:
- What parts of the project you were not able to complete

## REFERENCES:
- List any outside resources used

## MISCELLANEOUS COMMENTS:
- Anything you would like the grader to know

## Assignment Description
-In this assignment Baris Aran and Mehmet Kardan work as a member of Tito's Team. The design of the code is explained in following paragraph;
    - Gladiator class is created as observable and hold a list of audience that observes itself. Gladiator objects are created by reading json file
    within the class. Every time its state changed by Arena class, it updates the Audience states.
    
    - Audience class is observing the Gladiator class. The audiences are created in Arena class and attached to the Gladiator each turn.
    
    - Response class is holding 3 Strategies that implemented with the Strategy pattern. The strategies are the positive, which support its
    gladiator if something positive happen, negative, which the audiences only yells when something bad happen and the hybrid one which is mixed.
    Class also has two list of responses that audiences are selecting a response from that list whenever a state changed.
    
    - In arena class we built a fight system. Each turn 2 gladiator fight between each other. The possible outcome events are hit, critical hit
    dodge and lose the fight. If the lose the fight event is happen, the gladiator is asked to be stay alive to the audiences, the thumbs up method.
    Each time the state changes the other classes are updated.
***
# Project 4 - Bread and Circus
### Due Date: 11:59 p.m., Dec 7th, 2018

*All programs will be tested on the machines in the Q22 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files
* gladiators.json

### Grading Rubric
**Total: 40 points**
* Gladiator Class Requirements:
    * (2 pts) Gladiators are read in from json file
    * (4 pts) Each Gladiator is an observable class by implementing the observer pattern
* Audience Class Requirements:
    * (2 pts) has an update method that takes a event type as a parameter
    * (3 pts) has a method that sets the audience response type
    * (3 pts) Audience responds to events using the current response type
    * (3 pts) Audience response strategy changes with each match
* Response Class Requirements:
    * (6 pts) At least 3 different response strategies respond to an event type
* Arena
    * (2 pts) At least 100 Audience objects are created
    * (2 pts) Response types are randomly assigned to audience members
    * (3 pts) All audience members register as observers of gladiator
    * (2 pts) All audience member deregister from gladiator after the match
    * (2 pts) Two gladiators are selected from the pool of gladiators each round
    * (2 pts) battle between gladiators produces events until one reach zero health
    * (4 pts) Audience indicates thumbs up or down after match complete
* Submission:
    * Follows requested project structure and submission format (-5 points)
    * No global variables (-5 points)
    * Meets the commit requirement of having 3 significant commits 24 hours apart

### Guidelines
This is a pair programming assignment. You and a partner can divide up the work. Although both of you may not work on all parts of the program you should understand and be able to fully explain every portion of the code. Outside of your team, it is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically to solve the problem you have been given, and you may not have anyone else help you or your partner write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

If you or your partner are found to have plagiarized any part of the assignment, both will receive a 0 and be reported.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

__In this project, you will learn to__:

* Use the Observer and Strategy patterns to simulate a Colosseum experience

***


## Description

For our final assignment we are going to simulate the gladiatorial contests in the Colosseum in Rome. The game will begin with you reading a json file that contains a list of competitors. Each competitor will compete in the arena in a tournament style battle until there is only one left. An audience will boo, cheer, and ultimately decide the fate of each contender.

## Part A - Creating your participants

### Gladiator

The gladiator data will consists of name (string), age (int), birthplace (string), and health (int 0-100). The data will be stored in a json file in the following format:
[
        {name: ‘ceasar’, age: 56, birthplace: ‘Rome’, health: 50}
...
]
The outcome of the gladiatorial tests should be based on an algorithm of your choosing with 2 requirements:
* The result should not be entirely random. You can factor in previous wins, the health attribute, or whatever else you want, but there should be some weighted factor.
* Matches should produce several events that determine the outcome of the match.

### Audience

Next you will need to create an audience. The audience class observes the Gladiators as they go through the gladiatorial games, giving cheers, boos, or gasps as events occur in each match. You should create an audience of at least 100 audience objects that register as observers of the gladiator. The gladiator then ‘notifies’ the audience whenever an event occurs. There are 3 possible event types:
* The gladiator is harmed (loses health)
* The gladiator wins a match
* The gladiator loses a match

### Response

In addition to the audience class, you should create at least 3 audience member response strategies which will determine how different audience members respond to an event. For example, a negative response type would produce the following results:
* The gladiator is harmed (loses health) produces cheers
* The gladiator completes a task produces boos
* The gladiator fails a task produces cheers

Another response type, for example positive:
* The gladiator is harmed (loses health) produces boos
* The gladiator completes a task produces cheers
* The gladiator fails a task produces gasps

The response strategies should be contained in their own classes and should be assigned randomly to each audience object.

Each audience member randomly chooses one of the gladiators during the match to observe and respond to. The response strategy for each audience member should be updated with a new response strategy for each match.

## Part B - The Arena
Once you have your gladiators and your audience set up, the gladiatorial tournament can begin.

### Arena
The Arena class will hold all the audience members, gladiators, and battle logic.

Your gladiators will be put into the arena and compete in battle. Your logic will be to retrieve the next two gladiators from the pool of gladiators and have them battle until one reaches zero health. Then the audience will decide if the loser should have another chance with a thumbs up or thumbs down vote.

Each audience member will choose thumbs up or thumbs down based on any algorithm of your choosing.
* If the majority of audience members give the thumbs up, the gladiator will be placed back in the pool of gladiators and live to fight another round. :bulb: You will need to reset the gladiator's health.
* Otherwise, the gladiator is deleted.

## Project Requirements
In this assignment, you will use the Strategy and Observer Patterns. How each pattern will be used is explained below.
* Observer
   * The gladiator class should follow the design pattern requirements in the observer pattern for the subject.
   * The audience members should follow the observer pattern and must have an update method that takes an event type as a parameter.
* Strategy
   * You may use either classes or functions, but you should implement at least 3 different response types that can be passed to the audience members. All should share the same interface for responding with slightly different results.

## Part C: Submission

Required code organization:
* project4.py
    * this contains your main driver code
* Gladiator.py
* Audience.py
* Responses.py
    * You maybe put all your response types into a single file if you wish
* Arena.py
    * Each Arena subclass should go into its own file
* Include any additional files

### Git

You must commit your changes throughout the development of your project. You do not necessarily need to push the commits to Github, but we will look at your repository commit history to ensure you have **3 significant commits 24 hours apart**. If you do not meet the commit requirements, we will not accept your project and you will receive a 0.

These are a reminder of the git commands you will need to submit your project.

:warning: *These commands all presume that your current working directory is within the directory tracked by `git`.*

```shell
git status
git add info.txt
git commit -a -m "final commit message"
git push
```
:warning: *You* __must__ *add any new files you create to the repository with the `git add` command or they will not upload to the repo, and your code will not work.*

To find your most recent commit hash, use the following command:

```shell
git rev-parse HEAD
```

To complete your submission, you must copy and paste this number into mycourses. Go to MyCourses, select cs342, and **Assignment Hash Submission**. Select Project 4, and where it says text submission, paste your commit hash. The TAs will only grade your submission that corresponds to the hash you submitted. You can update this as often as you like until the deadline.

I strongly recommend making a submission early on, even if your assignment is not 100% working, to avoid late penalties. You can resubmit as many times as you like.

:warning: You __MUST__ submit the commit hash on mycourses before the deadline to be considered on time **even if your project is completely working before the deadline**. :warning:
