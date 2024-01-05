# PySigil
Wrapper of Sigil for Python

# About
A wrapper of the Sigil multimedia library for the Python programming language. This is for use with Python 3 and above. Sigil is a multimedia library that handles images, audio and text. PySigil is meant to be cross-platform and should run on Windows or GNU/Linux with little or no issues.

(c) Copyright 2024 PySigil

# License

PySigil is provided as-is. There is no warranty for this software. You use this software at your own risk. You may not blame the author for any wrong-doing for using this software. You may use this software to write Python programs using the PySigil wrapper. 

# Example

```Python
sigil.slWindow(800,600,b"Hello World",0)

while not sigil.slShouldClose() :

   if sigil.slGetKey(SL_KEY_ESCAPE) :
       sigil.slClose()
       
   sigil.slRender()

sigil.slClose()
```
