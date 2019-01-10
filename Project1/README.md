# CS342 Design Patterns
## Fall 2018
### PROJECT 1 README FILE

## DESIGN OVERVIEW:
- State each design pattern used (if any)
- Brief (< 5 sentences) description of your overall design
- Description of your search algorithm

===============================================
The only thing I have done different from the instructions is creating the "Coordinate" class. The coordinate class is a simple class that stores x,y and z values of either stars or the probe. I thought it would be easier rather than typing 3 values evertime. I have used Factory design pattern. My search algorithm is based on fuel saving. The probe always chooses to go to the closest unvisited star recursively. And if the probe's fuel is not greater than next star's distance plus distance to the starting point, the probe decides to turn back even if 't couldn't find life.
===============================================

## KNOWN BUGS AND INCOMPLETE PARTS:
- What parts of the project you were not able to complete

## REFERENCES:
- List any outside resources used

## MISCELLANEOUS COMMENTS:
- Anything you would like the grader to know

## Assignment Description
***
# Project 1 - Searching the Stars
### Due Date: 11:59 p.m., September 28th, 2018

*All programs will be tested on the machines in the Q22 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files
* project1.py

### Grading Rubric
**Total: 47 points**
* Universe Class Requirements:
   * (2 pts) The __init__ method takes the number of stars to create
   * (2 pts) Contain a print universe method that prints required data
* Star Class Requirements:
   * (2 pts) Star Base Class with unique x, y, z coordinates in the range 2**8..2**64
   * (3 pts) Star SubClasses: DwarfStar, GiantStar, MediumStar
   * (3 pts) Each Star subtype has attributes: chances of life, number of planets (as a range), goldilocks zone, recharge amount
   * (2 pts) Stars generate and save a list of planets using the above attributes
   * (2 pts) Star Coordinates are verifiably unique
   * (2 pts) Instance variables follow python conventions for private data
* Planet Class Requirements:
   * (2 pts) Planet base class that contains distance from star
   * (4 pts) Planet SubClasses: RockyPlanet, GaseousPlanet, HabitablePlanet
   * (4 pts) Each Planet is marked with having or not having intelligent life based on star attributes and distance from star
   * (2 pts) Each planet has a unique identifier as described.
* Probe Class Requirements:
   * (3 pts) Keeps track of the requested information
   * (5 pts) Unique algorithm to determine which Star should be visited next
   * (2 pts) Has a fuel attribute that depletes during the search algorithm, and recharges using the recharge amount for each star
   * (3 pts) A print method that prints the probe’s findings.
* Submission:
   * (2 pts) Follows requested project structure and submission format
   * (2 pts) README sections complete
   * Meets the commit requirement of having 3 significant commits 24 hours apart

### Guidelines
This is an individual assignment. You must do the vast majority of the work on your own. It is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically *to* solve the problem you have been given, and you may not have anyone else help you write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

__In this project, you will learn to__:

* Manage a large programming assignment with many parts
* write memory efficient software

***


## Description

For our first assignment we are going to simulate the universe, and then search it for intelligent life. There will be two parts to this project. In Part A you will build a universe of stars and planets. Each star will have a type, an x, y, and z coordinate, and a random range of planets orbiting the star.


## Part 1

### Part A - The Stars

You should first create a Universe class as a container class for all your stars, with a method to generate your universe. The stars should derive from a base star class, and fall into one of 3 categories. Each Star type will have attributes that will affect its likelihood of intelligent life:

* DwarfStar
   * Chances of life: 0.0006
   * Range of planets: 8-15
   * Goldilocks Zone: 30-90
   * Recharge: 2**20
* GiantStar
   * Chances of life: 0.0005
   * Range of planets: 5-10
   * Goldilocks Zone: 100-250
   * Recharge: 2**30
* MediumStar
   * Chances of life: 0.0009
   * Range of planets: 2-9
   * Goldilocks Zone: 60-140
   * Recharge: 2**25

:bulb: The values above should be hard-coded into your program and adjusted
to suit your design if necessary.

Each star will have an x,y,z coordinate to give it a location in space. No two stars should have the same x, y, z coordinates. You will need to use these coordinates to navigate from star to star, so the coordinates must be readable but should not be writable, using python private variable conventions. You should randomly generate these x,y,z coordinates, each in the range of (2^3..2^64)-1.  

Each star should also have a recharge amount to be used by the probe to refuel. A larger star should have a higher recharge amount. For example, I use 2^20, 2^25, 2^30 for the Dwarf, Medium, and Giant Stars respectively. You can adjust these numbers to suit your program, but it must be *possible* to run out of fuel.

Lastly, each star will randomly generate a list of planets (more information on planets below). It should have num planets, where num is in the range of planets given above (inclusive). When you generate the planets, you will need to also randomly assign the planet’s distance from the star in millions of miles. Multiple planets can have the same distance from a star.

### Part B - Planets


Each star will have multiple planets, each with 3 different types:

* RockyPlanet
* GaseousPlanet
* HabitablePlanet

You should randomly assign planet types as they are created, and each Planet should derive from a base Planet class. The Planet base class should contain the planet’s distance from the star in millions of miles.

For example, One star, which is a Giant, may have 6 planets, 2 Rocky, 3 Gaseous, and 1 Habitable. Another Giant Star might have 8 planets, all of which are Gaseous.

Each planet should also have a unique id, preceded by a letter identifying what kind of planet it is, ‘r’ for Rocky, ‘g’ for Gaseous, and ‘h’ for Habitable.


### Part C - Life

We will be using the Star’s chances of life instance variable to mark if a planet has intelligent life. Even if the planet is marked as possible for intelligent life, it then must be within the so-called goldilocks zone for its star and must be a HabitablePlanet type.

If all of these conditions are met, you should mark the planet as having intelligent life. Otherwise, mark it as without life.

Once you have your universe set up, you should add a method to your Universe class that prints the number of stars of each type and how many planets of each type correspond to each star. (See below for sample output)

## Part 2 - The Search

### Part A - Searching for Life
Once you have generated your universe with stars, planets, and (possibly) life, it’s time to search for life. To do so you will need a ‘probe’ object that will search star to star, using an algorithm of your choosing to select which star to go to next. In this README you must explain your search algorithm, and defend why you chose it.


As you visit each star you will use fuel. Your probe will have an initial fuel amount, and can recharge at each star. The recharge amount depends on the type of star you are visiting. After recharging, your probe will check the Star’s planets, and should mark that star as visited so you don’t revisit already explored stars.  Your search ends when your probe finds a planet with intelligent life. In order for your probe to deliver the information, it must have enough fuel to return to its starting point, which means you have to keep track of the probe’s starting coordinates.

You will need to keep track of some data as you explore your simulated universe.

* The probe's starting coordinates
* How many Stars you have visited
* How many Planets you have explored
* The total distance you have traveled before finding intelligent life
   * You can use the [3 dimensional distance formula](https://www.varsitytutors.com/hotmath/hotmath_help/topics/distance-formula-in-3d) to determine the distance between stars.  

When you finally find life and successfully return to the origin, the probe should print the above information and the unique ID of the planet that contained life.

If no life was found or the probe runs out of fuel, print the above information and a message noting this.

### Part B - Requirements

The following are the basic requirements for your program:

#### Universe Class Requirements:

* The initialize method takes the number of stars to create
    * For testing, you should start out with around 2**10 or less. After you get it working, see how large you can go and still run within a reasonable amount of time.
* Should contain a print universe method that prints:
    * The number of stars in the universe
    * The number of each type of star
    * The number of each type of planet around each type of star
        * See below for example

#### Star Class Requirements:

* Star Base Class with unique x, y, z coordinates in the range 2**3..2**64
* Star SubClasses: DwarfStar, GiantStar, MediumStar
* Each Star subtype has attributes:
    * chances of life
    * number of planets (as a range)
    * goldilocks zone
    * Stars should generate and save a list of planets using the above attributes

#### Planet Class Requirements:

* Planet base class that contains distance from star ranging from 1-300 (in 10 millions of miles)
* Planet SubClasses: RockyPlanet, GaseousPlanet, HabitablePlanet
* Each Planet is marked with having or not having intelligent life
* Each planet should have a unique identifier.
    * implementation is up to you as long as it is guaranteed to be unique and is prefixed with the appropriate letter (i.e. ‘r’, ‘g’, ‘h’)

###Probe Class Requirements:

* Keeps track of the following information
    * starting coordinates
    * id of planet discovered to have intelligent life
    * total distance traveled
    * number of stars visited
    * number of planets explored
* An algorithm to determine which Star you should visit next
* A print method that prints the probe’s findings.


### Additional Requirements

* You must use composition for all HAS-A relationships.
    * For example, the planet class should not inherit from the Star class. You must have a compositional relationship between the Star and the Planet.         
* Each base class must go into a separate file. Subclasses *may* go in the same file as their base class.
* The main driver code should also be in a separate file.
* You should not have any global variables

## Sample Output:

This was run with 2**10 stars:

```
Total number of stars in my universe: 1025
There are 380 Giant Stars with:
        1056 Gaseous Planets
        1092 Rocky Planets
        1082 Habitable Planets
        0 Planets with Intelligent Life

There are 303 Dwarf Stars with:
        1275 Gaseous Planets
        1219 Rocky Planets
        1277 Habitable Planets
        0 Planets with Intelligent Life

There are 342 Medium Stars with:
        715 Gaseous Planets
        747 Rocky Planets
        807 Habitable Planets
        1 Planets with Intelligent Life

==========

Your origin was (4576, 76584476, 46508759)
Traveled 1.6731455226093466e+20 miles
        You have 5.870783888950368e+3 fuel remaining
        Visited 131 stars
        Explored 1223 planets
Found life on planet h8657
```

## Part 3: Submission

Required code organization:
* project1.py
    * this contains your main driver code
* Universe.py
* Star.py
    * You can put your Star subclasses into one file if you wish
* Planet.py
    * You can put your planet subclasses into one file if you wish
* Probe.py
    * The Probe class should be in a file by itself
* Include any additional files

### Git

An additional git requirement for this project is that you commit your changes throughout the development of your project. You do not necessarily need to push the commits to Github, but we will look at your repository commit history to ensure you have **3 significant commits 24 hours apart**. If you do not meet the commit requirements, we will not accept your project and you will receive a 0.

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



To complete your submission, you must copy and paste this number into mycourses. Go to MyCourses, select cs342, and **Assignment Hash Submission**. Select Project 1, and where it says text submission, paste your commit hash. The TAs will only grade your submission that corresponds to the hash you submitted. You can update this as often as you like until the deadline.

I strongly recommend making a submission early on, even if your assignment is not 100% working, to avoid late penalties. You can resubmit as many times as you like.

:warning: You __MUST__ submit the commit hash on mycourses before the deadline to be considered on time **even if your project is completely working before the deadline**. :warning:
