import click
import subprocess
from colorama import Fore, Back, Style


@click.command()
@click.argument("pyfile", nargs=1, type=click.Path(dir_okay=False, exists=True))
def cli(pyfile):
    result = subprocess.run(["python3", pyfile], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    out = result.stdout.decode('utf-8')
    err = result.stderr.decode('utf-8')

    if err:
        print(Fore.RED + "What do you think you are doing, idiot?\n")
        print(Fore.MAGENTA + err)
    else:
        print(Fore.GREEN+ "What can you say! It finally worked!")
        print(Style.RESET_ALL)
        print(out)
