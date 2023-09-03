
from pyfiglet import figlet_format

from rich.progress import track,Progress, SpinnerColumn, BarColumn, TextColumn, TransferSpeedColumn
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich import box
from rich.align import Align
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.syntax import Syntax
from rich.live import Live

from time import sleep
from datetime import datetime
import secrets
from yaspin import yaspin

spinner = yaspin()


def drawlayout(here):
       console = Console()
       layout = Layout(name='base')

       layout.split(
              Layout(name='header',ratio = 1),
              Layout(name='body',ratio=4),
              Layout(Panel(here,title='[green]Footer'), ratio=1)
       )
       layout['body'].split_row(
              Layout(name='left'),
              Layout(Panel('mid',title='playground'), ratio=2),
              Layout(name='right')
       )
       layout['left'].split_column(
              Layout(name='leftTop'),
              Layout(name='leftBottom'),
        )
    #    layout['footer'].update('this be footer so make we see wosop')
       console.print(layout)
       console.print(Panel('Hello, [red]Azay!'))
       console.print(Panel.fit('Hello, [green]Azay!'))
       console.print(Panel('Hello, [white]Azay!',title='akwaaba',subtitle='ayekoo'))

def newformat(t):
     console=Console(width=25)
     style = 'bold white on blue'
     console.print(t,style=style,justify='center')


def hac(t):
     for i in t:
             print(i,end="",flush=True)
             sleep(0.1)
     print('\n')

def ascianim(t):
       text = figlet_format(t,font='standard')
       for i in text:
              print(i,end="",flush=True)
              sleep(0.02)

def savetofile(t):
       with open('save.txt','a') as file:
              textToSave = figlet_format(t,font='standard')
              file.write(textToSave)


def main():
     fresh = True
     while True:
             if(fresh):
                co = Prompt.ask('where is the target?')
            
             else: co = Prompt.ask('new target to hack or exit?')
             level = Prompt.ask('level of penetration',choices=['hardcore','quick'])
             
             if(co=='exit.now'):
                     break
             gen = secrets.token_bytes(128)
             for i in track(range(50),'penetrating firewalls...',show_speed=False):
                     sleep(0.3)
             hac(gen)
             display = co + ' ' + 'hacking about to begin'
             newformat(display)
             for q in track(range(50),'stealing files...'):
                     sleep(0.2)
             ascianim('HACKED')
             finaldisplay = co + ' ' + 'haching DONE !!!'
             for q in track(range(20),'saving to disk...'):
                     sleep(0.1)
             ascianim('DONE')
             savetofile(finaldisplay)
             newformat(finaldisplay)
             fresh = False

             


if __name__ == "__main__":
       pass
#     with Live(drawlayout('start'),auto_refresh=False,screen=True) as live:
#            for i in range(50):
#                 sleep(0.000000001)
                
    