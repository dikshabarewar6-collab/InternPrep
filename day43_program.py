# Mini Heap Tree
import heapq

heap = []

heapq.heappush(heap, 7)
heapq.heappush(heap, 2)
heapq.heappush(heap, 9)
heapq.heappush(heap, 1)

print("Heap:", heap)

print("Min:", heapq.heappop(heap))
print("After pop:", heap)

# Max Heap Tree
import heapq

heap = []

heapq.heappush(heap, -10)
heapq.heappush(heap, -5)
heapq.heappush(heap, -20)

print(-heapq.heappop(heap))