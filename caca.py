# @title Clone repository and install dependencies
# @markdown This first step will download the latest version of Voice Changer and install the dependencies. **It can take some time to complete.**
%cd /content/

!pip install colorama --quiet
from colorama import Fore, Style
import os

print(f"{Fore.CYAN}> Cloning the repository...{Style.RESET_ALL}")
!git clone https://github.com/w-okada/voice-changer.git --quiet
print(f"{Fore.GREEN}> Successfully cloned the repository!{Style.RESET_ALL}")
%cd voice-changer/server/

print(f"{Fore.CYAN}> Installing libportaudio2...{Style.RESET_ALL}")
!apt-get -y install libportaudio2 -qq

print(f"{Fore.CYAN}> Installing pre-dependencies...{Style.RESET_ALL}")
# Install dependencies that are missing from requirements.txt and pyngrok
!pip install faiss-gpu fairseq pyngrok --quiet
!pip install pyworld --no-build-isolation --quiet
print(f"{Fore.CYAN}> Installing dependencies from requirements.txt...{Style.RESET_ALL}")
!pip install -r requirements.txt --quiet

print(f"{Fore.GREEN}> Successfully installed all packages!{Style.RESET_ALL}")
