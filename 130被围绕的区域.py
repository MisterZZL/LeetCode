#130. 被围绕的区域
#给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

#思路方法：
#使用BFS从边上开始搜索，如果是'O'，那么搜索'O'周围的元素，并将'O'置换为'D'，这样每条边都DFS或者BFS一遍。而内部的'O'是不会改变的。这样下来，
#没有被围住的'O'全都被置换成了'D'，被围住的'O'还是'O'，没有改变。然后遍历一遍，将'O'置换为'X'，将'D'置换为'O'。
class Solution():
	    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def fill(x, y):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1 or board[x][y] != 'O':
                return
            queue.append((x, y))
            board[x][y] = 'D'

        def bfs(x, y):
            if board[x][y] == 'O':
                fill(x, y)
            while queue:
                cur = queue.pop(0)
                i = cur[0]
                j = cur[1]
                fill(i + 1, j)
                fill(i - 1, j)
                fill(i, j + 1)
                fill(i, j - 1)

        if len(board) == 0:
            return
        m = len(board)
        n = len(board[0])
        queue = []

        for i in range(n):
            bfs(0, i)
            bfs(m - 1, i)
        for j in range(1, m - 1):
            bfs(j, 0)
            bfs(j, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
					
					

#方法二：
#从板的周围出发，从周围的‘O’出发深度搜索，能搜到的‘O’用visit记录他有没有访问过。最后将所有没有visit过的'O'变成‘X’.
 class Solution(object):
     def solve(self, board):
         """
         :type board: List[List[str]]
         :rtype: void Do not return anything, modify board in-place instead.
         """
         m = len(board)
         if m == 0:
             return
         n = len(board[0])
         visit = [[False for i in range(n)] for j in range(m)]
         def dfs(i,j):
             q = []
             q.append([i,j])
             while len(q) != 0:
                 tmp = q[0]
                 #print(tmp,visit[3][1],board[3][1])
                 q.pop(0)
                 #down,up,left,right
                 if tmp[0] - 1 > 0 and board[tmp[0] - 1][tmp[1]] == 'O' and visit[tmp[0]-1][tmp[1]] == False:
                     visit[tmp[0] -1][tmp[1]] = True
                     q.append([tmp[0] - 1,tmp[1]])
                 if tmp[0] + 1 < m and board[tmp[0] + 1][tmp[1]] == 'O' and visit[tmp[0]+1][tmp[1]] == False:
                     visit[tmp[0] +1][tmp[1]] = True
                     q.append([tmp[0] + 1,tmp[1]])
                 if tmp[1] - 1 > 0 and board[tmp[0]][tmp[1] - 1] == 'O' and visit[tmp[0]][tmp[1]-1] == False:
                     visit[tmp[0]][tmp[1] - 1] = True
                     q.append([tmp[0],tmp[1] - 1])
                 if tmp[1] + 1 < n and board[tmp[0]][tmp[1] + 1] == 'O' and visit[tmp[0]][tmp[1]+1] == False:
                     visit[tmp[0]][tmp[1]+1] = True
                     q.append([tmp[0],tmp[1]+1])
         for i in range(n):
             if visit[0][i] == False and board[0][i] == 'O':
                 visit[0][i] = True
                 dfs(0,i)
             if visit[m - 1][i] == False and board[m-1][i] == 'O':
                 visit[m-1][i] = True
                 dfs(m - 1,i)
         for j in range(m):
             if visit[j][0] == False and board[j][0] == 'O':
                 visit[j][0] = True
                 dfs(j,0)
             if visit[j][n - 1] == False and board[j][n - 1] == 'O':
                 visit[j][n - 1] = True
                 dfs(j,n - 1)
         for i in range(m):
             for j in range(n):
                 if board[i][j] == 'O' and not visit[i][j]:
                     board[i][j] = 'X'