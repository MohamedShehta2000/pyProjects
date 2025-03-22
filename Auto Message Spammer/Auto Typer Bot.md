# Auto Typer Bot

## Description
This Python script automates typing a specific message multiple times using the `pyautogui` module. After a short delay, it writes "hello" and presses Enter repeatedly.

## How It Works
1. The script waits for 5 seconds to allow the user to focus on the desired text input field.
2. It then enters "hello" and presses Enter 200 times using a loop.

## Prerequisites
Ensure you have Python installed on your system along with the required module:

```sh
pip install pyautogui
```

## Usage
Run the script and quickly switch to the text field where you want the messages to be typed.

```sh
python script.py
```

## Code Example
```python
import time
import pyautogui as pg

time.sleep(5)  # Delay to allow the user to switch windows

for i in range(200):
    pg.write("hello")
    pg.press("Enter")
```

## Notes
- Be careful when using automation scripts, as excessive spamming may violate platform rules.
- You can modify the script to send different messages or adjust the delay time.

## License
This project is open-source and available for modification and distribution.

