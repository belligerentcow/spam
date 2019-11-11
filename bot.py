import win32api, win32con
import random
import sys

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def keyboard_event(key_to_press):
    win32api.keybd_event(key_to_press, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0) #press
    win32api.Sleep(5)
    win32api.keybd_event(key_to_press, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0) #release

def type_it(msg):
    msg = msg.upper()
    for aletter in msg:
        if aletter == " ":
            keyboard_event(win32con.VK_SPACE)
        else:
            keyboard_event(ord(aletter))
    # enter:
    keyboard_event(win32con.VK_RETURN)

def run_bot(mouse_coord_x, mouse_coord_y, delay_in_milliseconds):
    with open("words/adj.txt", "r") as adj, open("words/noun.txt", "r") as noun:
        adjList = [word for line in adj for word in line.split()]
        nounList = [word for line in noun for word in line.split()]

    click(mouse_coord_x, mouse_coord_y)

    while True:
        randAdj = random.choice(adjList)
        randNoun = random.choice(nounList)
        randMsg = randAdj + " " + randNoun
        type_it(randMsg)
        win32api.Sleep(delay_in_milliseconds)

run_bot(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
