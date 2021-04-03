class WeightedGraph:
	def __init__(self, g = {}):
		self.g = g
	
	def addEdge(self, n1, n2, w):
		if not n1 in self.g.keys():
			g[n1] = []
		self.g[n1].append((n2,w))
	
	def UCS(self, s, g):
		q = []
		q.append((s,0))
		retStr = ''
		while q:
			print(q)
			idx = 0
			minDist = 1000
			for i, n in enumerate(q):
				if n[1] < minDist:
					minDist = n[1]
					idx = i
			(s, sDist) = q.pop(idx)
			retStr += '{0}, '.format(s)
			if s == g:
				break
			for i in self.g[s]:
				q.append((i[0],i[1]+sDist))
		return retStr[:-2]

if __name__ == '__main__':
	graph={'S':[('p',1),('d',3),('e',9)],
		'p':[('q',15)],
		'q':[],
		'd':[('b',1),('c',8),('e',2)],
		'b':[('a',2)],
		'c':[('a',2)],
		'a':[],
		'e':[('h',8),('r',2)],
		'h':[('q',4),('p',4)],
		'r':[('f',1)],
		'f':[('c',3),('G',2)],
		'G':[]}

	g = WeightedGraph(graph)

	print("Uniform Cost Search is as follows:\n{0}".format(g.UCS('S','G')), end='')