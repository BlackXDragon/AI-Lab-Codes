class Node:
	def __init__(self, name, c = None, h = None, p = None): # c is cost from root, h is heuristic
		self.name = name
		self.c = c
		self.h = h
		self.p = p

class WeightedGraph:
	def __init__(self, g = {}):
		self.g = g
	
	def addEdge(self, n1, n2, w):
		if not n1 in self.g.keys():
			g[n1] = []
		self.g[n1].append((n2,w))

	def a_star(self, s, g, h):
		S = Node(s, 0, h[s])
		q = [S]
		traversed = []
		goalNode = None
		flag = False

		while q:
			s = q.pop(self.qmin(q))
			traversed.append(s)
			if s.name == g:
				flag = True
				goalNode = s
				break
			for i in self.g[s.name]:
				child = Node(i[0], s.c + i[1], h[i[0]], s)
				if not self.check(child):
					q.append(child)
		
		if flag:
			path = []
			s = goalNode
			while not s == None:
				path.append(s.name)
				s = s.p
			path.reverse()
			print("Path to Goal:")
			print(', '.join(path))
		else:
			print("404! Solution not found.")
	
	def qmin(self, q):
		minH = q[0].h + q[0].c
		minIdx = 0
		for idx, i in enumerate(q):
			if (i.h + i.c) < minH:
				minH = (i.h + i.c)
				minIdx = idx
		return minIdx
	
	def check(self, c):
		a = c.p
		while not (a.p == None):
			if c.name == a.p.name:
				return True
			a = a.p
		return False

if __name__ == '__main__':
	graph={'Hannover':[('Dusseldorf',320),('Bremen',120),('Hamburg',155),('Schwerin',270),('Leipzig',255),('Frankfurt',365)],
		'Dusseldorf':[('Hannover',320),('Frankfurt',240)],
		'Bremen':[('Hannover',120),('Hamburg',110)],
		'Hamburg':[('Bremen',110),('Hannover',155),('Kiel',85)],
		'Schwerin':[('Hannover',270),('Berlin',200),('Rostock',90)],
		'Leipzig':[('Hannover',255),('Berlin',185),('Dresden',140),('Munchen',435)],
		'Frankfurt':[('Hannover',365),('Leipzig',410),('Munchen',410),('Stuttgart',200),('Bonn',180),('Dusseldorf',240)],
		'Kiel':[('Hamburg',85)],
		'Rostock':[('Schwerin',90)],
		'Berlin':[('Schwerin',200),('Leizwig',185)],
		'Dresden':[('Leipzig',140)],
		'Bonn':[('Frankfurt',180)],
		'Stuttgart':[('Frankfurt',200),('Munchen',210)],
		'Munchen':[('Stuttgart',210),('Frankfurt',410),('Leipzig',435)]}

	g = WeightedGraph(graph)

	heuristic = {
		'Stuttgart': 180,
		'Bonn': 480,
		'Dusseldorf': 540,
		'Frankfurt': 380,
		'Bremen': 720,
		'Hannover': 610,
		'Hamburg': 720,
		'Kiel': 750,
		'Schwerin': 680,
		'Rostock': 740,
		'Berlin': 590,
		'Leipzig': 410,
		'Dresden': 400,
		'Munchen': 0
	}

	print("A Star Search from Hannover to Munchen:")
	g.a_star('Hannover','Munchen',heuristic)
