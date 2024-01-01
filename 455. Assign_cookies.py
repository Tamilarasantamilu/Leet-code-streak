class Solution:
    def findContentChildren(self, child: List[int], cookie: List[int]) -> int:
        '''
        i= desired cookie size 
        j= the size of a cookie
        if j >= i , i (children) will be content!!!  -> maximize the number of content children
        output= the number of content children
        '''
        # 1. order each lists in numerical order to compare easily and to ensure the cookies are offered in order of ascending size -> greedy algorithm
        child.sort()
        cookie.sort()

        # 2. define the variables
        content_children = 0
        cookie_index = 0

        # 3. find the maximum number from the cookie list
        while cookie_index < len(cookie) and content_children < len(child):
            if cookie[cookie_index] >= child[content_children]:
                content_children += 1
            cookie_index += 1

        return content_children
