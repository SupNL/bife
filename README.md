# bife
###Python script for image to text braille conversion

## Dependecies
-Python 3 or above
-Pillow
-NumPy

Both Pillow and NumPy libraries can be installed through pip install
```
pip install numpy
pip install pillow
```

Runnable through command line
```
python bife.py +file=image.png +t=150
```
Text output will be generated to a file named 'brailleArt.txt'

## Command line arguments
Arguments should be separated by space

### +file=
```
+file=image.png
```
The name of the image to be converted

### +t=
```
+t=120
```
Value between 0 and 255
Image threshold

### +scale=
```
+scale=70
```
Optional argument
Image scale
Values in percentage
In the example above, image will be resized to 70% of its size

### +dotted+
```
+dotted+
```
Optional argument
Use a single point instead of blank space
Useful when image is not proportional on each row

Dotted art
![Dotted](https://github.com/SupNL/bife/images/dotted.png)

Without dot
![Non-Dotted](https://github.com/SupNL/bife/images/non_dotted.png)

### About me
This is actually my first time writing a github readme for a program I've coded
Any criticism is welcome, I'm looking forward in learning more!
Talk to me on discord: nl#5118
