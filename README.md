# Welcome to bife!
### Python script for image to text braille conversion
<img src="https://github.com/SupNL/bife/blob/master/images/example_logo_art.png" width="350" height="350" />

## Dependecies
- Python 3 or above
- Pillow
- NumPy

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
Image threshold<br/>
```
+t=120
```
Value between 0 and 255<br/>

### +scale=
Image scale<br/>
```
+scale=70
```
Optional argument<br/>
Values in percentage<br/>
In the example above, image will be resized to 70% of its size<br/>

### +dotted+
```
+dotted+
```
Optional argument<br/>
Use a single point instead of blank space<br/>
Useful when image is not proportional on each row

Dotted art<br/>
![Dotted](https://github.com/SupNL/bife/blob/master/images/dotted.png)

Without dot<br/>
![Non-Dotted](https://github.com/SupNL/bife/blob/master/images/non_dotted.png)

### About me
This is actually my first time writing a github readme for a program I've coded<br/>
Any criticism is welcome, I'm looking forward in learning more!<br/>
Talk to me on discord: nl#5118
