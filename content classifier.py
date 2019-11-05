import ourAlgo
import time
# Take the page as an input
with open("page.txt") as page:
    pageContent = page.read().lower().split()
# Remove common words
with open("common-english-words.txt") as com:
    commonWords = com.read().split(",")
    
for word in commonWords:
    i = 0
    while i < len(pageContent):
        if pageContent[i] == word:
            pageContent.pop(i)
        else:
            i += 1
        

# count occurrences of every word 
words_occurrences = {}
for word in pageContent:
    if word in words_occurrences:
        words_occurrences[word] += 1
    else:
        words_occurrences[word] = 1
        
# sort and calculate time
words_occurrences = list(words_occurrences.items())
print("\n\n")
#Bubble sort
beginning = time.time()
sorted_list = ourAlgo.BubbleSort(words_occurrences[:])
t = (time.time()-beginning)*1000

print(f"Results for Bubble sort: {sorted_list[:5]}\nExecution time for bubble sort: {round(t,5)} ms")
print('-'*100)


#insertion sort
beginning = time.time()
sorted_list = ourAlgo.insertionSort(words_occurrences[:])
t = (time.time()-beginning)*1000

print(f"Results for insertion sort: {sorted_list[:5]}\nExecution time for insertion sort: {round(t,5)} ms")
print('-'*100)


#Selection sort
beginning = time.time()
sorted_list = ourAlgo.selectionSort(words_occurrences[:])
t = (time.time()-beginning)*1000

print(f"Results for selection sort: {sorted_list[:5]}\nExecution time for selection sort: {round(t,5)} ms")
print('-'*100)


#merge sort
beginning = time.time()
sorted_list= ourAlgo.mergeSort(words_occurrences[:])
t = (time.time()-beginning)*1000
print(f"Results for merge sort: {sorted_list[:5]}\nExecution time for merge sort: {round(t,5)} ms")
print('-'*100)


#quick sort
beginning = time.time()
sorted_list = ourAlgo.quickSort(words_occurrences)
t = (time.time()-beginning)*1000

print(f"Results for quick sort: {sorted_list[:5]}\nExecution time for quick sort: {round(t,5)} ms")
print('-'*100)


# classify it
words_occurrences = words_occurrences[:20]
with open("sports_wordlist.txt") as f:
    sports = f.read().lower().split()
    
with open("politics_wordlist.txt") as f:
    politics = f.read().lower().split()
    
with open("food_wordlist.txt") as f:
    food = f.read().lower().split()

with open("science_wordlist.txt") as f:
    science = f.read().lower().split()





categories = [["sports", 0], ["politics", 0], ["food", 0], ["science", 0]]
for item in words_occurrences:
    if item[0] in sports:
        categories[0][1] += item[1]
    if item[0] in politics:
        categories[1][1] += item[1]
    if item[0] in food:
        categories[2][1] += item[1]
    if item[0] in science:
        categories[3][1] += item[1]

        
ourAlgo.get_category(categories)
print("\n")