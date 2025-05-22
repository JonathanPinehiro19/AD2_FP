# def sequentialSearch(target, lyst):
    
#     position = 0
#     while position
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def indexOfMin(lyst):
    
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1        
    return minIndex

print(indexOfMin(vetor))


def sequentialSearch(target, lyst):
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1    
    