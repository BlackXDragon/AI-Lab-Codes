class Graph:
	def __init__(self, g = {}):
		self.g = g
	
	def addEdge(self, n1, n2):
		if not n1 in self.g.keys():
			g[n1] = []
		self.g[n1].append(v)
	
	def DFS(self, s, g, d):
		if s == g:
			return 'Goal ({0})'.format(s)
		retStr = s + ', '
		if d > 1:
			for child in self.g[s]:
				retStr += self.DFS(child, g, d-1) + ', '
		return retStr[:-2]
	
	def IDS(self, s, g, maxDepth):
		retStr = ''
		for d in range(1, maxDepth + 1):
			retStr += 'Depth {0}: '.format(d) + self.DFS(s, g, d) + '\n'
		return retStr

if __name__ == '__main__':
	graph={'A':['B','C'],
	  'B':['D','E'],
	  'C':['F','G'],
	  'D':['H'],
	  'E':['I','J'],
	  'F':['K'],
	  'G':[],
	  'H':[],
	  'I':[],
	  'J':[],
	  'K':[],}

	g = Graph(graph)

	print("IDS traversal for node G with max depth of 3:\n{0}".format(g.IDS('A', 'G', 3)), end='')
