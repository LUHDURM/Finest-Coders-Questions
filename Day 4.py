class Solution(object):
    def exist(self, board, word):
        row=len(board)
        col=len(board[0])
        def dfs(i,j,index):
            if index==len(word):
                return True
            if i<0 or j<0 or i>= row or j>= col or board[i][j]!= word[index]:
                return False
            temp=board[i][j]
            board[i][j]='#'
            dir=[[0,1],[1,0],[-1,0],[0,-1]]
            found=False
            for di,dj in dir:
                ni,nj=i+di,j+dj
                if (dfs(ni,nj,index+1)):
                    found=True
                    break
            board[i][j]=temp
            return found
        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0]:
                    if(dfs(i,j,0)):
                        return True
        return False
