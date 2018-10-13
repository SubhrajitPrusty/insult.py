import click
import subprocess
from colorama import Fore, Back, Style
from random import choice
import os

@click.command()
@click.argument("pyfile", nargs=1, type=click.Path(dir_okay=False, exists=True))
def cli(pyfile):

	messages = [
					"My cat can type better than you?",
					"buh, buh, buh... Get to it, idiot!",
					"Sigh.",
					"(╯°□°）╯︵ ┻━┻",
					"This is not a search engine.",
					"Why are you doing this to me?!",
					"Perhaps computers is not for you...",
					"ERROR_INCOMPETENT_USER",
					"Incompetence is also a form of competence",
					"error code: 1D10T",
					"The keyboard is not a touch screen!",
					"Commands, random gibberish, who cares!",
					"What do you think you are doing, idiot?",
					"I bet your brain feels as good as new, seeing that you never use it.",
					"If I wanted to kill myself I'd climb your ego and jump to your IQ.",
					"I'd like to see things from your point of view but I can't seem to get my head that far up my ass.",
					"I'm not saying I hate you, but I would unplug your life support to charge my phone.",
					"Are you always this stupid or are you making a special effort today?!",
					"So, I'm just going to go ahead and run rm -rf / for you.",
					"ERROR_INCOMPETENT_USER",
					"Incompetence is also a form of competence",
					"What if... you type an actual command the next time!",
					"What if I told you... it is possible to type valid commands.",
					"Please step away from the keyboard!",
					"I am _seriously_ considering 'rm -rf /'-ing myself...",
					"Try using your brain the next time!",
					"Dropped on your head as a baby, eh?"
				]

	py = "python3" if os.name == "posix" else "python"

	result = subprocess.run([py, pyfile], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	out = result.stdout.decode('utf-8')
	err = result.stderr.decode('utf-8')

	if err:
		print(Fore.RED + choice(messages))
		print(Fore.MAGENTA + err)
	else:
		print(Fore.GREEN+ "What can you say! It finally worked!")
		print(Style.RESET_ALL)
		print(out)
