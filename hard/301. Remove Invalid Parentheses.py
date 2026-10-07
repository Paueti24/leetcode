class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        res = []
        minRemovals = float('inf')

        
        def dfs(i, open, string):
            nonlocal res, minRemovals
            crides_recursives += 1
            if i >= n:
                if open == 0:
                    removals = n - len(string)
                    if removals < minRemovals:
                        minRemovals = removals
                        res = [string]
                    elif removals == minRemovals:
                        res.append(string)
                    # if removed > minRemovals -> discard it
                return

            if s[i] != '(' and s[i] != ')':
                dfs(i+1, open, string + s[i])
                return

            # use bracket
            if s[i] == '(':
                dfs(i+1, open+1, string + s[i])
            elif open > 0: #')'
                dfs(i+1, open-1, string + s[i])
            # if ')' and open == 0 -> cannot be removed
                
            # remove bracket (if previos used is different)
            # do not remove this one, if it means removing more than minRemovals
            if ((not string or string[-1] != s[i])
                and i - len(string) < minRemovals):
                dfs(i+1, open, string)



        dfs(0,0,"")
        return res