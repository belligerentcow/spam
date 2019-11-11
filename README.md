# Python Spam Bot

## How to use:

1. Install the win32api library for python

    ```
    pip install pywin32
    ```

2. Clone the repository and change directories into it

    ```
    git clone https://github.com/belligerentcow/spam.git
    cd spam
    ```

3. The bot takes 3 command line arguments: `[x mouse coordinate of target text box] [y mouse coordinate of target text box] [delay between sending messages in milliseconds]`. You can run the bot by being in the spam repository and running:

    ```
    python bot.py [arg1] [arg2] [arg3]
    ```

4. In order to determine the x and y coordinates for the mouse, open up a python terminal and the application you're trying to spam on the same monitor, and run

    ```
    >>> import win32api
    >>> win32api.SetCursorPos((x, y))
    ```

    Where `x` and `y` are x and y coordinates from the top left of the screen in pixels. Experiment until the mouse ends up over the text box you're attempting to spam.
