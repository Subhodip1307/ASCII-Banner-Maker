import degine
import argparse
import sys,os
import pandas as pb
from colorama import Fore
current_path=os.getcwd()
all_color_list={"DEEP COLORS":["RED","GREEN","BLUE","WHITE","YELLOW","MAGENTA","CYAN","BLACK"],"LIGHT COLORS":["LIGHTRED","LIGHTGREEN","LIGHTBLUE","LIGHTWHITE","LIGHTYELLOW","LIGHTMAGENTA","LIGHTCYAN","LIGHTBLACK"]}
series=pb.DataFrame(all_color_list)
banner_color=[]
class Custom_banner:
    def __init__(self,colors,name,file_name):
        self.name=name
        self.colors=colors
        self.file=file_name
    def code_writter(self,colors):
        os.chdir(current_path)
        with open(f"{self.file}.py","w") as codefile:
            codefile.write(f"""
import pyfiglet
from colorama import Fore ,Back,Style
name="{self.name}"
colord_lines=[]
colors={colors}"""+
r"""
asii_banner=pyfiglet.figlet_format(name)
lines=asii_banner.split("\n")
for i ,line in enumerate(lines):
    color=colors[i % len(colors)]
    colord_line="{}{}{}".format(color,line,Style.RESET_ALL)
    colord_lines.append(colord_line)
colord_banner="\n".join(colord_lines)
print(colord_banner)     
            """)
            return f"Code has been saved in {self.file}"
    def color(self):
        color_list=[]
        for i in range(len(self.colors)):
            if self.colors[i][0]=="d" or self.colors[i][0]=="D" :
                if self.colors[i][1:]=="0":
                    color_list.append(Fore.RED)
                elif self.colors[i][1:]=="1":
                    color_list.append(Fore.GREEN)
                elif self.colors[i][1:]=="2":
                    color_list.append(Fore.BLUE)
                elif self.colors[i][1:]=="3":
                    color_list.append(Fore.WHITE)
                elif self.colors[i][1:]=="4":
                    color_list.append(Fore.YELLOW)
                elif self.colors[i][1:]=="5":
                    color_list.append(Fore.MAGENTA)
                elif self.colors[i][1:]=="6":
                    color_list.append(Fore.CYAN)
                elif self.colors[i][1:]=="7":
                    color_list.append(Fore.BLACK)
                else:
                    print("You have provided out of the range values")
                    return self.colors[i]
            elif self.colors[i][0]=="l" or self.colors[i][0]=="L":
                if self.colors[i][1:]=="0":
                    color_list.append(Fore.LIGHTRED_EX)
                elif self.colors[i][1:]=="1":
                    color_list.append(Fore.LIGHTGREEN_EX)
                elif self.colors[i][1:]=="2":
                    color_list.append(Fore.LIGHTBLUE_EX)
                elif self.colors[i][1:]=="3":
                    color_list.append(Fore.LIGHTWHITE_EX)
                elif self.colors[i][1:]=="4":
                    color_list.append(Fore.LIGHTYELLOW_EX)
                elif self.colors[i][1:]=="5":
                    color_list.append(Fore.LIGHTMAGENTA_EX)
                elif self.colors[i][1:]=="6":
                    color_list.append(Fore.LIGHTCYAN_EX)
                elif self.colors[i][1:]=="7":
                    color_list.append(Fore.BLACK)
                else:
                    print("You have provided out of the range values")
                    return self.colors[i]
            else:
                print("You have given wrong attributes, kindly read documentation/Readme file")
                exit()
        return color_list
    @staticmethod
    def genators(requirments):
        Banner_name=""
        Banner_name=requirments.n
        print("Available color options are:")
        print(series)
        print()
        print(f"You have for request for {requirments.c} color combination")
        for i in range(requirments.c):
            print(f"enter required color index, example: for deep-red color type- d0 or D0, for light red color type- l0 or L0")
            color=input(f"Enter no-{i+1} color:- ")
            color=color.lower()
            banner_color.append(color)
        test=Custom_banner(banner_color,Banner_name,requirments.f)
        # c=test.color()
        try:
            print(test.code_writter(test.color()))
        except:
            print("Something happened wrong please read Documentation and try again")
        return " "
if __name__ == '__main__':
    collect=argparse.ArgumentParser()
    collect.add_argument("-n",type=str,help="Enter the name to create a custom banner with it")
    collect.add_argument("-c",type=int,help="Number's of colors you want in your Banner")
    collect.add_argument("-f",type=str,default="banner",help="Type your required file name don't provide extension")
    require=collect.parse_args()
    sys.stdout.write(str(Custom_banner.genators(require)))

