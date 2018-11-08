# MARIE.py
A simple Assembler and Emulator(kind of) for MARIE (Machine Architecture that is Really Intuitive and Easy)
Yes, emulator not simulator. This is because this implementation lacks a lot of the visualisation tools and other features that come in the MARIE.js simulator. Additionally code needs to be "assembled" by an assembler which is more like the functionality of an emulator even though this project isn't technically an emulator either.

Why did I make this?
  
  Two Reasons
  
  1.  Because during the FIT1047 assignment at monash I was frustrated being stuck with a web editor. Plus the 
      actual text editor only makes a small portion of the website making it harder and harder to see the 
      full perspective of my code as my project got more complicated.
  
  2. Because I thought this would be a fun learning exercise
  
Dependancies:
  - Python3.X
  - numpy
  
That's it!
  
DISCLAIMERS:

In case you couldn't tell. I did not originally develop MARIE. This project was inspired by https://github.com/MARIE-js/MARIE.js all credit goes to it's original developers.

I am not in any way associated with the developers of MARIE.js and I am certainly not an expert when it comes to writing compilers and/or understanding hardware architectures.

I will not take any legal or other responsibility for ANY issues with this software. If you decide to use this for your assignment or anything else of importance then you do so at your own risk. Make sure you regularly back up your work and every so often you should check your assignment still works with MARIE.js (that is what you'll be assessed with after all)

All that being said, please feel free to report bugs though.  ;)

TLDR:
  Don't be stupid, make sure your assignment works in MARIE.js before submission. Use this software at your own risk.
  
  
  
TODO:
  
  - Add better error handling and reporting (the assembler current just crashes with invalid code)
  - I still cant run my original assignment so theres some more bugs in there somewhere..
  - Better internal documentation is needed and perhaps some external documentation one day.
  - Better Debugging tools, (although there won't be anything too fancy it would be nice to atleast look at whats in memory after a system halt.
  
  


