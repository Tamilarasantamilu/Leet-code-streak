class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        
        # Initialize the DP array with zeros. The array f stores the minimum height
        # of shelves needed to place the first i books.
        f = [0] * (n + 1)

        # Iterate through each book
        for i in range(1, n + 1):
            w, h = books[i - 1]
            
            # Start with the current book alone on a new shelf
            f[i] = f[i - 1] + h
            
            # Try to place as many previous books on the same shelf as possible
            for j in range(i - 1, 0, -1):
                w += books[j - 1][0]
                
                # If the total width exceeds shelf width, stop placing more books on this shelf
                if w > shelfWidth:
                    break
                
                # Update the height of the current shelf to the maximum height of the books on it
                h = max(h, books[j - 1][1])
                
                # Update the minimum height for placing the first i books
                f[i] = min(f[i], f[j - 1] + h)

        return f[n]
