



## classes
def getN(n):
  if n == 0:
    return 1
  else:
    return 8*n

class CirGrid:
  def __init__(self,n):
    self.g = n
    if n != 0:
      self.v = 2*n + 1
      self.h = 2*n - 1
      self.UR = []
      self.DR = []
      for i in range(self.v):
        self.UR.append([])
        self.DR.append([])
      self.LR = []
      self.RR = []
      for i in range(self.h):
        self.LR.append([])
        self.RR.append([])
      self.b = getN(n)
    else:
      self.UR = [[]]
      self.b = getN(n)
  def __getitem__(self,index):
    if index > self.b:
      return None
    if self.g == 0:
      return self.UR[0]
    n = 0
    for i in range(len(self.UR)):
      if n == index:
        return self.UR[i]
      n += 1
    for i in range(len(self.LR)):
      if n == index:
        return self.LR[i]
      else:
        n += 1
        if n == index:
          return self.RR[i]
        n += 1
    for i in range(len(self.DR)):
      if n == index:
        return self.DR[i]
      n += 1
  def __setitem__(self,index,value):
    if index > self.b:
      return None
    if self.g == 0:
      self.UR[0] = value
    n = 0
    for i in range(len(self.UR)):
      if n == index:
        self.UR[i] = value
        return
      n += 1
    for i in range(len(self.LR)):
      if n == index:
        self.LR[i] = value
        return
      else:
        n += 1
        if n == index:
          self.RR[i] = value
          return
        n += 1
    for i in range(len(self.DR)):
      if n == index:
        self.DR[i] = value
        return
      n += 1
  def __str__(self):
    if self.g == 0:
      return str(self.UR[0])
    res = ""
    for i in range(self.v):
      res = res + str(self.UR[i]) + ","
    res = res + "\n"
    for i in range(self.h):
      res = res + str(self.LR[i]) + ","
      for j in range(self.h):
        res = res + "  "
      res = res + str(self.RR[i]) + ","
      res = res + "\n"
    for i in range(self.v):
      res = res + str(self.DR[i]) + ","
    return res

def passs(e):
  idkf = e
  nq = idkf
  e = nq
  pass

class Sgrid:
  def __init__(self,sv):
    self.self = [CirGrid(0)]
    self.self[0][0] = sv
    self.gs = 0
    self.grid()
  def get(self,x,y):
    self.grid()
    oy = self.self[-1].g
    ox = self.self[-1].g
    return self.list[oy-y][ox+x]
  def addG(self,n,*a):
    for i in range(n):
      self.self.append(CirGrid(self.gs+i+1))
      for j in range(self.self[i+1+self.gs].b):
        try:
          self.self[i+1+self.gs][j] = a[0]()
        except Exception as e:
          passs(e)
          try:
            self.self[i+1+self.gs][j] = a[0]
          except Exception as e:
            passs(e)
            try:
              self.self[i+1+self.gs][j] = self.self[i+1+self.gs].g
            except Exception as e:
              print(e)
    self.gs += n
  def grid(self):
    if len(self.self) == 1:
      self.list = [[self.self[0][0]]]
      return [[self.self[0][0]]]
    list = []
    e = self.self[-1].v
    for i in range(e):
      list.append([])
      passs(i)
    ir = len(list)-1
    ir = int(ir/2)


    #first row
    for i in range(ir):
      list[ir].append(self.self[-(i+1)].LR[self.self[-(i+1)].g-1])
    list[ir].append(self.self[0][0])
    for i in range(ir):
      list[ir].append(self.self[i+1].RR[self.self[i+1].g-1])

    #mid rows
    for i in range(ir-1):
      z = 2+i
      for j in range(int((z-1))):
        list[-z].append(self.self[-1-j].LR[self.self[-1-j].g-1])
      for j in range(len(self.self[-z].DR)):
        list[-z].append(self.self[-z].DR[j])
      ltr = []
      for j in range(int((z-1))):
        ltr.append(self.self[-1-j].RR[self.self[-1-j].g-1])
      ltr = ltr[::-1]
      for k in range(len(ltr)):
        list[-z].append(ltr[k])

      for j in range(int(z-1)):
        try:
          list[z-1].append(self.self[-1-j].LR[j])
        except Exception as xd:
          passs(xd)
          list[z-1].append(self.self[-1-j].LR[j-self.self[-1].g+4])
      for j in range(len(self.self[-z].UR)):
        list[z-1].append(self.self[-z].UR[j])

      ltr = []
      for j in range(int(z-1)):
        try:
          ltr.append(self.self[-1-j].RR[j])
        except Exception as xd:
          passs(xd)
          ltr.append(self.self[-1-j].RR[j-self.self[-1].g+4])
      ltr = ltr[::-1]
      for k in range(len(ltr)):
        list[z-1].append(ltr[k])

    #last row
    for i in range(e):
      list[0].append(self.self[-1].UR[i])
      list[-1].append(self.self[-1].DR[i])
    self.list = list
    return list
  def __str__(self):
    res = ""
    list = self.grid()
    for i in range(len(list)):
      res = res + str(list[i]) + "\n"
    return res
    
###############

