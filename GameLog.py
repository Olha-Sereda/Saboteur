from datetime import datetime

class GameLog:
    def __init__(self):
        self.log_entries = []

    def cleanLog(self):
        self.log_entries = []

    def addLog(self, username: str, message: str):
        current_time = datetime.now()
        log_entry = {"userName": username, "message": message, "time": current_time}
        self.log_entries.append(log_entry)

    def addGameLog(self, message: str):
        current_time = datetime.now()       #.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {"userName": "Game", "message": message, "time": current_time}
        self.log_entries.append(log_entry)

    def getLastMessages(self, number=0):
        if len(self.log_entries) < number:
            number = len(self.log_entries)

        if number == 0:
            return self.log_entries
        else:
            return self.log_entries[-number:]