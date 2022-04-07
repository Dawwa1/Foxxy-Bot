# Foxxy Discord Bot TESTING VERSION

This is the testing version of the official bot. The features here are bugged and broken, and will not work as intented. This is mostly gonna be used for uploading my code for myself, but if you want to pitch in you are more then welcome to!

## Installation

Download the folder, and install everything in the requirments.txt file

```bash
pip install -r requirements.txt
```

Then add your bot token to the .env file in thise format

```py
BOT = "token here"
```

Finally, run the run.py file to start the bot!

## Commands
As this is the testing version, I will not be updating the commands list. These are the core commands that are already polished.

```
1) !ban {member} {reason}
2) !unban {member} {reason}
3) !kick {member} {reason}
4) !lock & !unlock {role id} #Locks or unlocks a channel for a specific role or all roles
5) !mute {member} {length in minutes} {reason}
6) !unmute {member} {reason}
7) !nuke #Deletes all messages in channel
8) !poll {what to poll on}
```

## Contributing
If you want to contribute to this project, be welcome to make a pull request!

## License
MIT License

Copyright (c) 2022 Dawwa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
