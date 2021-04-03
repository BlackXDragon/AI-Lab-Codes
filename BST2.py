class BST:
	def __init__(self, raw):
		self.tree = []
		self.tree.append([raw[0]])
		for el in raw[1:]:
			self.append(el)

	def append(self, num):
		l = 0
		el = 0
		flag = True
		while flag:
			if num <= self.tree[l][el]:
				if l == len(self.tree) - 1:
					self.tree.append([None]*(2**(l+1)))
					self.tree[l+1][el*2] = num
					flag = False
				elif self.tree[l+1][el*2] == None:
					self.tree[l+1][el*2] = num
					flag = False
				else:
					l = l + 1
					el = 2 * el
			else:
				if l == len(self.tree) - 1:
					self.tree.append([None]*(2**(l+1)))
					self.tree[l+1][el*2+1] = num
					flag = False
				elif self.tree[l+1][el*2+1] == None:
					self.tree[l+1][el*2+1] = num
					flag = False
				else:
					l = l + 1
					el = 2 * el + 1
		return (l,el)

	def __str__(self):
		treeStr = ""
		for i in self.tree:
			treeStr = treeStr + "[" + ", ".join([str( '_' if(j == None) else j ) for j in i]) + "]\n"
		return treeStr

	def dfs(self, l = 0, el = 0):
		prStr = ""
		if l < len(self.tree):
			if self.tree[l][el]:
				prStr = self.dfs(l + 1, el * 2)
				if not prStr:
					prStr = str(self.tree[l][el])
				else:
					prStr = prStr + ', ' + str(self.tree[l][el])
				r = self.dfs(l + 1, el * 2 + 1)
				if r:
					prStr = prStr + ', ' + r
				return prStr
		return None

	def bfs(self):
		bfsList = []
		for i in self.tree:
			for j in i:
				if not j == None:
					bfsList.append(j)
		return ', '.join([str(i) for i in bfsList])

if __name__ == '__main__':
	raw = eval(input('Enter the raw data as a list: '))
	bst = BST(raw)
	print('\nThe BST generated is:')
	print(bst)
	print('DFS: ',bst.dfs())
	print('BFS: ',bst.bfs())