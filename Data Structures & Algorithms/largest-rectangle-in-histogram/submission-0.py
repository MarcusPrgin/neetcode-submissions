class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stores the maximum rectangle area found so far
        maxArea = 0
        
        # Stack will store pairs: (start_index, height)
        stack = []

        # Traverse through all bars in the histogram
        for i, h in enumerate(heights):
            start = i

            # While current height is smaller than the last height in stack
            # calculate area for bars that cannot extend further
            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                # Calculate area using popped height
                # Width = current index - starting index
                maxArea = max(maxArea, height * (i - index))

                # Update start so the current height can extend left
                start = index

            # Push current bar with its valid starting index
            stack.append((start, h))

        # Process remaining bars in the stack
        for i, h in stack:
            # Width extends to the end of the histogram
            maxArea = max(maxArea, h * (len(heights) - i))

        # Return the largest rectangle area
        return maxArea