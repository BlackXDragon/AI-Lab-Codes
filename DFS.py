class Graph:
	def __init__(self, g = {}):
		self.g = g
	
	def addEdge(self, n1, n2):
		if not n1 in self.g.keys():
			g[n1] = []
		self.g[n1].append(v)
	
	def DFS(self, s, g):
		visited = {i : False for i in self.g.keys()}
		q = []
		q.append(s)
		visited[s] = True
		retStr = ''
		while q:
			print(q)
			s = q.pop(0)
			visited[s] = True
			retStr += '{0}, '.format(s)
			if s == g:
				break
			q = [i for i in self.g[s] if not visited[i]] + q
		return retStr[:-2]

if __name__ == '__main__':
	graph={'A':['B','C'],
	  'B':['D','E'],
	  'C':['D','G'],
	  'D':['B','C','F'],
	  'E':[],
	  'F':['G','H'],
	  'G':[],
	  'H':[]}

	g = Graph(graph)

	print("DFS traversal is as follows:\n{0}".format(g.DFS('A', 'G')), end='')
