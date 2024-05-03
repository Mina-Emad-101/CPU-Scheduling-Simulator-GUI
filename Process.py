class Process:
    def __init__(self, pid: int, arrivalTime: int, burstTime: int, priority: int):
        self.pid = pid
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.priority = priority
        self.startTime = 0

    def split(self, time: int):
        burstTimeLeft = self.burstTime - (time - self.arrivalTime)
        burstTimeDone = self.burstTime - burstTimeLeft
        self.burstTime = burstTimeDone
        remainingProcess = Process(self.pid, self.arrivalTime, burstTimeLeft, self.priority)
        return remainingProcess
    
    def toString(self):
        text = ''
        text += f'Pid: {self.pid}\n'
        text += f'Arrival Time: {self.arrivalTime}\n'
        text += f'Burst Time: {self.burstTime}\n'
        text += f'Priority: {self.priority}\n'
        text += f'Start Time: {self.startTime}\n'
        text += f'\n'
        return text
