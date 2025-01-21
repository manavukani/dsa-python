# smallest asteroid explodes if it collides with bigger asteroid
# no need to reduce the size of bigger asteroid


class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for incoming_ast in asteroids:
            # same direction / no collision
            if incoming_ast > 0:
                stack.append(incoming_ast)
            else:
                # top asteroid explodes if smaller than incoming
                while stack and stack[-1] > 0 and stack[-1] < abs(incoming_ast):
                    stack.pop()

                # both explodes
                if stack and stack[-1] == abs(incoming_ast):
                    stack.pop()

                # add -ve incoming asteroid, ONLY IF stack empty
                elif not stack or stack[-1] < 0:
                    stack.append(incoming_ast)

        return stack


print(Solution().asteroidCollision([4, 7, 1, 1, 2, -3, -7, 17, 15, -16]))  # [4, 17]
