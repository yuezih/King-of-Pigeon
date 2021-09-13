import operator

class Std(object):
    def __init__(self):
        self.name = ''
        self.offerNum = 0
        self.offers = []

stds = []
stdsDict = {}
index = 0

def readStd(name,camper):
    global stds
    global stdsDict
    global index
    if name not in stdsDict:
        newStd = Std()
        newStd.name = name
        stds.append(newStd)
        stdsDict[name] = index
        index += 1
    if camper not in stds[stdsDict[name]].offers:
        stds[stdsDict[name]].offers.append(camper)
        stds[stdsDict[name]].offerNum += 1

if __name__ == "__main__":
    campers = ['PKUxk','THUsz_ai','THUsz_cs','THUsz_data','USTC_cs']
    for camper in campers:
        filename = camper + '.txt'
        with open('data/%s'%(filename), "r") as f:
            data = f.readlines()
            for std in data:
                readStd(std,camper)

    cmpfun = operator.attrgetter('offerNum','name')
    stds.sort(key = cmpfun,reverse = True)

    for std in stds:
        if std.name[-1] == '\n':
            std.name = std.name[:-1]
        print(f'{std.name} 拿了 {std.offerNum} 个 offer: ',end = '')
        print(std.offers)