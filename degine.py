import pyfiglet
from colorama import Fore ,Back,Style
name="Banner"
name2="Generators"
colors=[Fore.BLUE,Fore.BLUE,Fore.MAGENTA,Fore.MAGENTA]
colors2=[Fore.BLUE,Fore.BLUE,Fore.MAGENTA,Fore.MAGENTA]
asii_banner=pyfiglet.figlet_format(name)
asii_banner2=pyfiglet.figlet_format(name2)
lines=asii_banner.split("\n")
lines2=asii_banner2.split("\n")
colord_lines=[]
colord_lines2=[]
for i ,line in enumerate(lines):
    color=colors[i % len(colors)]
    colord_line=f"{color}{line}{Style.RESET_ALL}"
    colord_lines.append(colord_line)
colord_banner="\n".join(colord_lines)

for i2 ,line2 in enumerate(lines2):
    color2=colors2[i2 % len(colors2)]
    colord_line2=f"{color2}{line2}{Style.RESET_ALL}"
    colord_lines2.append(colord_line2)
colord_banner2="\n".join(colord_lines2)

print(colord_banner,
                    "\t",colord_banner2
                        )

