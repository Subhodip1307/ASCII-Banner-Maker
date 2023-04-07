# ASCII-Banner-Maker
ASCII Art Banner Maker is a Python program that allows users to input any text they like and convert it into a colorful ASCII art banner. The program asks the user for input a text and convert it to a colorful eye-catching ASCII banner. It can be use to increase the attractiveness  of any CLI based programs

## Author
- [@Subhodip1307](https://github.com/Subhodip1307)

## Tested OS
```bash
    Windows
    Linux(Debain based)
```
  
## Requirments
```bash
    Python 3
```
## Use
>First Git clone the repo in your systeam
```bash
    git clone https://github.com/Subhodip1307/ASCII-Banner-Maker.git
```
Now run the setup.py to download the required packages to run

Step 1
> now open it in your terminal
```bash
 cd ASCII-Banner-Maker
```
Step 2
> for windows
```bash
  python setup.py
```
>for Linux
```bash
  python3 setup.py
```
Now lets Run the Main file

> for windows
```bash
  python Code_genatros.py -n <text for banner> -c <Number's fo colors you want to use> -f <give a file name without extention to save the code> 
```
>for Linux
```bash
   python3 Code_genatros.py -n <text for banner> -c <Number's fo colors you want to use> -f <give a file name without extention to save the code> 
```

## Explanation of Commands of the code

> -h/--help       For help

> -n              Type text which you want to convert into a Banner

> -c               Number's of colors you want to use here

> -f              (it's optional command) type here the file name where you want to save the code if you don't give any name it will save as banner.p


## Color Codes

Available color options are:

Index    DEEP COLORS     |   LIGHT COLORS

0         RED   |   LIGHTRED

1       GREEN   |  LIGHTGREEN

2        BLUE   |  LIGHTBLUE

3       WHITE   |  LIGHTWHITE

4      YELLOW   |  LIGHTYELLOW

5     MAGENTA   |  LIGHTMAGENTA

6        CYAN   |  LIGHTCYAN

7       BLACK   | LIGHTBLACK

- There are two types of color combinations deep color and light color and Indexes also provied 

- suppose you want to use deep Red , Deep Yellow and Light Red in your banner, to do that

>d0 

d, stands for deep color and then 0 shows the index, mean deep Red

>d4 

(d, stands for deep color, you can also use "D" insated of "d" and then 4 shows the index, mean deep yellow)

>l0 

(l, stands for light color, you can also use "L" insated of "l"  and then 0 shows the index, mean light red)

## Examples
> The Example will be shown in windows but you can use it in linux in the same way just replace python to python3

-After running setup.py file

```bash
  python Code_genatros.py -n example -c 2 -f myfile 
```
- So here we are creating a banner of "example" with 2 colors and the code result will store in myfile.py

![image](https://user-images.githubusercontent.com/111901004/230647500-c34e7179-07e7-4ca0-a253-6493114de1ea.png)

- So it's askfor selecting 2 colorcodes , in this case we will use Deep red and light Green so the color code will be

> D0

> L1

- After putting two values one by one now the code will save in myfile.py

![image](https://user-images.githubusercontent.com/111901004/230648834-f9cf5b07-d9bf-4e85-9993-141e1931709a.png)

- now we just have to run myfile.py to check the results

```bash
    python myfile.py
```
