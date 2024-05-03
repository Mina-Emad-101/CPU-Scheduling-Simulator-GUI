class Process:
    def __init__(self, pid: int, arrivalTime: int, burstTime: int, priority: int):
        self.pid = pid
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.priority = priority
        self.startTime = 0

    def start(self):
        pass

    def stop(self):
        pass

    def split(self, time: int):
        burstTimeLeft = self.burstTime - (time - self.arrivalTime)
        burstTimeDone = self.burstTime - burstTimeLeft
        self.burstTime = burstTimeDone
        remainingProcess = Process(self.pid, self.arrivalTime, burstTimeLeft, self.priority)
        return remainingProcess
