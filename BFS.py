class Graph:
	def __init__(self, g = {}):
		self.g = g
	
	def addEdge(self, n1, n2):
		if not n1 in self.g.keys():
			g[n1] = []
		self.g[n1].append(v)
	
	def BFS(self, s):
		visited = {i : False for i in self.g.keys()}
		q = []
		q.append(s)
		visited[s] = True
		retStr = ''
		while q:
			s = q.pop(0)
			retStr += '{0}, '.format(s)
			for i in self.g[s]:
				if not visited[i]:
					q.append(i)
					visited[i] = True
		return retStr[:-2]

if __name__ == '__main__':
	graph={'A':['F','C','B'],
      'B':['G','C'],
      'C':['F'],
      'D':['C'],
      'E':['D','C','J'],
      'F':['D'],
      'G':['C','E'],
      'J':['D','K'],
      'K':['E','G']}

	g = Graph(graph)

	print("BFS traversal is as follows:\n{0}".format(g.BFS('K')), end='')