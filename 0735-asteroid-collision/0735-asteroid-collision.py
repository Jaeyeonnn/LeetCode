class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        i=0
        while i<len(asteroids):
            if len(stack)==0: stack.append(asteroids[i])
                
            #If asteroids on top of stack is moving right and currect asteroids is moving left they will collide
            elif stack[-1]>0 and asteroids[i]<0:
                val=0
            #If the asteroid[i] is bigger then asteroids on top of stack it will keep destroying them until the condition dissatifies
                while len(stack)!=0 and stack[-1]<=abs(asteroids[i]) and stack[-1]>0:
                    val=stack.pop()
                    #If both the asteroid and asteroids on top of stack have same mass, they will destroy each other and the loop should break
                    if val==abs(asteroids[i]): break
            #If the len of stack is not zero and top is stack is also moving to left then asteroid[i] will also be appended as it is also moving left and would not collied with stack top
                if len(stack)!=0 and stack[-1]<0 and abs(val)!=abs(asteroids[i]):
                    stack.append(asteroids[i])
            #If the asteroids[i] has destroyed all asteroids in the stack
                if len(stack)==0 and abs(val)!=abs(asteroids[i]):
                    stack.append(asteroids[i])
            else:
                stack.append(asteroids[i])
            i+=1
        return stack