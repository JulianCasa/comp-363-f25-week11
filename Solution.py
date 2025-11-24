little_dictionary = [
    "a",
    "afternoon",
    "airport",
    "an",
    "and",
    "anywhere",
    "at",
    "because",
    "become",
    "before",
    "behind",
    "beside",
    "between",
    "breakfast",
    "broadcast",
    "but",
    "daylight",
    "deadline",
    "everywhere",
    "for",
    "forecast",
    "handbook",
    "hardware",
    "he",
    "headline",
    "her",
    "him",
    "homework",
    "i",
    "in",
    "income",
    "inside",
    "into",
    "it",
    "keyboard",
    "me",
    "midnight",
    "network",
    "notebook",
    "of",
    "offline",
    "on",
    "online",
    "or",
    "outcome",
    "outline",
    "outside",
    "overcome",
    "oversee",
    "password",
    "saturn",
    "she",
    "software",
    "somewhere",
    "suitcase",
    "sunlight",
    "takeover",
    "textbook",
    "the",
    "them",
    "therefore",
    "they",
    "to",
    "understand",
    "undertake",
    "upon",
    "us",
    "we",
    "whatever",
    "whenever",
    "wherever",
    "whoever",
    "within",
    "without",
    "you",
]

import random


def generate_random_string(
        from_words: list[str],
        number_of_words: int,
        distortion_probability: float = 0.0) -> str:
    """Produce a string with randomly selected strings from a list of strings. Then,
    distort the string by removing characters from it with the given probability."""
    # Select words at random from the input list. The number of words to select
    # is specified by the int:number_of_words in the arguments.
    random_string: str = ""
    # Guard statement
    if (distortion_probability >= 0.0
        and number_of_words > 0
            and number_of_words <= len(from_words)):
        random_string = "".join(random.sample(from_words, number_of_words))
        # Distort the string only if the distortion probability is not zero.
        if distortion_probability > 0.0:
            distorted_chars = [
                ch for ch in random_string
                if random.random() >= distortion_probability
            ]
            random_string = "".join(distorted_chars)
    return random_string

def binary_search(word_list: list[str], target: str) -> int:
    """Performs binary search on a sorted list of words.
    Returns the index of target if found, otherwise -1.
    To preserve memory, this implementation is iterative."""
    low: int = 0
    high: int = len(word_list) - 1

    while low <= high:
        mid: int = (low + high) // 2
        guess: str = word_list[mid]

        if guess == target:
            return mid  # Target found
        if guess > target:
            high = mid - 1  # Search in the lower half
        else:
            low = mid + 1  # Search in the upper half

    return -1  # Target not found


def is_word(word_list: list[str], word: str) -> bool:
    """Boolean helper for binary searchReturns True if word is in 
    word_list, False otherwise."""
    return binary_search(word_list, word) != -1

def can_segment_dp(A: str) -> list:
    """Determine (using dynamic programming) if A can be segmented into
    valid tokens from little_dictionary."""
    # Shortuct
    n: int = len(A)
    # Initialize the dp array
    dp: list[bool] = [False] * (n + 1)
    #Creates a list to store where each segment starts
    previous = [None] * (n + 1)
    # Base case
    dp[0] = True

    # Consider every prefix A[:i] for i in 1..n
    for i in range(1, n + 1):
        j = 0
        # we continue until we either find a valid split or exhaust j
        while j < i and not dp[i]:
            if dp[j] and is_word(little_dictionary, A[j:i]):
                dp[i] = True
                #Assigns the start value of the segment
                previous[i] = j
            j += 1

    #Checks to see if it is even segementable
    if not dp[n]:
        words = None
    else:
        #If it is segemntable it creates a list to return them and 
        # creates index to be used as a stop point
        wordsBack = []
        index = n

        #Loops through the list of start points
        while index > 0:
            #Y is assigned the value of the index and travels from back to front
            y = previous[index]
            #The segemented word is appended to the list
            wordsBack.append(A[y:index])
            #Index is then set as the old start point and the loop resets
            index = y

        N = len(wordsBack)

        #It then runs another loop to fix the order of the words
        words = ["0"] * N

        for i in range(N):
            words[i] = wordsBack[N-1-i]

        
    

    return words


# test
number_of_trials = 10
current_trial = 0
distortion_probability = 0.01
while current_trial < number_of_trials:
    current_trial += 1
    A = generate_random_string(
        little_dictionary, number_of_trials, distortion_probability)
    result: bool = can_segment_dp(A)
    # report
    print(f"{str(result):>8}: {A}")
