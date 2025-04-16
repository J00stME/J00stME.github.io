# <center>Alex Frankel's E-Portfolio</center>

## A not-so-brief Professional Self-Assessment
My tumultuous journey towards a degree in Software Engineering has taken me to places I never imagined before.  The best description of what I’ve experienced at SNHU is “a little bit of everything”.  I’ve learned multiple programming languages, multiple front-end development libraries, SQL and NoSQL databases, the software development lifecycle, architectural program design, and even software reverse engineering and secure coding practices.<br>
To break things down just a little bit, here are all my course-specific competencies and related skills: <br>

### **Collaborating in a team environment**
I have been trained in industry-standard communications for creating readable and reusable code.  In-line commenting, encapsulation and modular design, and language-specific naming conventions, and the core Object Oriented Programming principles to name a few of the most basal tenets of coding.  CS320 introduced robust software testing techniques.  My philosophy when it comes to soundness in code is as follows- leave no stone unturned.  This is one great example of why test coverage is so important in a professional setting.  It tells you what you have and have not tested, leaving little room for error in terms of the overall scope.  This contributes to a culture of solidarity among co-developers by covering each other’s tracks.  Other courses such as CS250, a course in the Agile Software Development Lifecycle, culminated in me assuming each role in the ‘Scrum’ framework.  It is important to understand every team member’s role and associated responsibilities in order to best work with them.  This segue’s into the next category… <br>

### **Communicating with stakeholders AND Security**
There were many times in my coursework where I was required to organize and present my findings for several different applications.  This is especially apparent when I discussed code security reviews or strategy plans.  My experiences with cybersecurity are inextricably linked to my experiences compiling in-depth security policies/demonstrations for stakeholders.  CS405, Secure Coding, had me prepare a presentation on a Security Policy for a potential client.  This included compiling security standards to address memory overflow protections for both integers and strings and even chimes in on input validation (especially to prevent SQL Injection attacks).  Professing the various attack vectors a system may have constitutes the “Defense in Depth” cybersecurity strategy.  CS305 Software Security also ended with a Secure Software Practices report.  It included communicating principles such as deploying Algorithm Cyphers for encrypting data and generating security certificates.  Something both of these presentations utilized was static analysis tools such as Maven Dependency Check queries OWASP known vulnerabilities based on the versions of libraries used or CPPCheck which detects various types of errors or bad conventions based on the aforementioned security standards.  Being able to communicate these concepts to a professional audience of stakeholders is incredibly helpful as it builds trust! <br>

I have also in some ways become a stakeholder myself in the software I use every day.  Working in the E-Commerce Department at Whole Foods has granted me the credibility of the ‘product owner’ , or rather the software I use to fulfill orders is familiar to me with all its faults and features.  My time at SNHU has fostered a sense of ownership for the software I interact with and allows me to codify any sort of requests for the betterment of the application and therefore the company at large! <br>

### **Data Structures and Algorithms**
I have been introduced to various data structures and algorithms and have proficiency in their implementations in multiple programming languages.  Vectors, Hash tables, and Binary search trees, and various sorting algorithms (mergesort, bubblesort, fastsort) were introduced in CS300 Data Structures and Algorithms.  Some of the more interesting applications of this involved Q-Learning and Deep Neural Networks as demonstrated in Artifact 2. <br>

### **Software Engineering and Databases**
Various applications of software engineering were explored in my coursework.  CS 330 was an introduction to the principles behind computer graphics.  CS 340, my first Artifact, introduced client/server configurations and full-stack development, data manipulation, and visualization.  CS 465 introduced me to full-stack engineering as well.  CS 360 introduced Android mobile development.  CS 410 introduced me to the intricacies of assembly language and the process of Reverse Engineering different decompiled C++ programs.  I have been instructed in UI and UX design and have software architectural diagrams for a number of programs.  When it comes to Databases, I have experience in designing and administrating SQL (in DAD220) and MongoDB (CS340) databases and have demonstrable skill in writing complex queries for both of them.  Finally, I made use of a localized SQLite server for my Android app to save local user data. <br><br>


## <center>Code Review</center>
<center><iframe width="800" height="600" 
    src="https://www.youtube.com/embed/zYmI5PXftYI" 
    frameborder="0" allowfullscreen></iframe></center><br>
<center>My code review is a walkthrough of my artifacts originally produced as coursework at SNHU.  In this review I go through each project line-by-line and discuss my enhancement plan for this portfolio.</center><br>


## Artifact One: Software Engineering and Design | Databases

The first of my two projects is the Friend Finder application.  It spans both categories as it is the union of both Database administration and design as well as implementing a User Interface and data visualiser.  In my enhancement I run the MongoDB server on my own machine and import the CSV file to the database (database enhancement).  I also updated deprecated methods from the old version of Dash and then swap out the hard-coded database login info in favor of a simple authentication prompt.  Finally, I added various new data visualizations to the project dashboard which granted a new insight on the raw data (software engineering/design enhancements). <br>

<center><a href="https://github.com/J00stME/J00stME.github.io/tree/main/Artifact%201%20Friend%20Finder">Access the Friend Finder files and development narrative here!</a><br></center>

The following screenshot shows the Dashboard up and running

<center>
    <img src="CS499FriendFinder.png" height="800"><br>
    <img src="CS499FriendFinder2.png" height="800">
</center><br>


## Artifact Two: Data Structures and Algorithms

The second project is a Q-Learning, Deep Neural Network trained to solve a simple maze.  Utilizing the Q "reinforcement learning" algorithm, my enhancement is a juxtaposition of different learning parameters for the model and documenting their success (or failure).  I also made use of an Anaconda Virtual Environment so that the original (now deprecated) code could run on my system. <br>

<center><a href="https://github.com/J00stME/J00stME.github.io/tree/main/Artifact%202%20Maze%20Game">Access the Maze Game files and development narrative here!</a><br></center>

The following screenshot shows a completed training session and the path the AI Agent took

<center><img src="CS499QLearning.png" height="800" width="800"></center><br>


