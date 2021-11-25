class Schedule():
    def __init__(self, date, time, subject):
        self.date = date
        self.time = time
        self.subject = subject
        self.adjacencylist = []
        self.visited = False

    def bfs(self):
        queue = []
        queue.append(self)
        filledspots = []
        self.visited = True

        while queue:
            currentSchedule = queue.pop(0)

            if currentSchedule.time >= 11:
                filledspots.append(currentSchedule.date)

            for n in currentSchedule.adjacencylist:
                if not n.visited:
                    n.visited = True
                    queue.append(n)

        return filledspots


November = Schedule('November', 0, '0')
Week1 = Schedule('First week', 0, '0')
Week2 = Schedule('Second week', 0, '0')
Week3 = Schedule('Third week', 0, '0')
Week4 = Schedule('Fourth week', 0, '0')

option1 = Schedule('Tuesday 2nd', 10, 'Marketing')
option2 = Schedule('Thursday 4th', 15, 'Programming')
option3 = Schedule('Friday 5th', 9, 'Algorithms and Data Structures')

option4 = Schedule('Wednesday 9th', 13, 'Math')
option5 = Schedule('Monday 7th', 10, 'Entrepreneurship')
option6 = Schedule('Sunday 14th', 17, 'Marketing')

option7 = Schedule('Tuesday 16th', 9, 'Algorithms and Data Structures')
option8 = Schedule('Wednesday 17th', 16, 'Math')
option9 = Schedule('Saturday 20th', 11, 'Programming')

option10 = Schedule('Monday 22nd', 14, 'Marketing')
option11 = Schedule('Thursday 25th', 17, 'Entrepreneurship')
option12 = Schedule('Sunday 28th', 9, 'Algorithms and Data Structures')


November.adjacencylist = [Week1, Week2, Week3, Week4]
Week1.adjacencylist.extend([option1, option2, option3])
Week1.adjacencylist.extend([option4, option5, option6])
Week1.adjacencylist.extend([option7, option8, option9])
Week1.adjacencylist.extend([option10, option11, option12])

November.bfs()

