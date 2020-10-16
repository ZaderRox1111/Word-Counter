
def main():
    # gets the inputs from the user, like the file, how many words to view, and the sort order
    selected_file = input("What text file would you like to run through? ")
    desired_word_count = int(input("How many words do you want to see? "))
    top_bottom = input("Want to see the most used words or the least? (t) (b): ")

    top_bottom = top_bottom.lower()

    # opens and reads the file that is selected
    f = open(selected_file)
    # just to show that it has begun parsing through the text
    print("Processing ...")
    words = f.read()
    f.close()

    # lists out all the characters we want to delete, then removes them from the read file
    unwanted = '\'".,?!()[]{}/=<>;:-+*&^%$#@'

    # does actions to the read file
    words = words.replace("\n", ' ')
    for badchar in unwanted:
        words = words.replace(badchar, '')
    words = words.lower()
    words_list = words.split()

    # creates new list that has each word with the frequency it appears
    counted_list = []
    for word in words_list:
        counter = words_list.count(word)
        if [counter, word] not in counted_list:
            counted_list.append([counter, word])

    # sorts the list by most or least used
    if top_bottom == 't':
        counted_list.sort(reverse = True)
    elif top_bottom == 'b':
        counted_list.sort()

    # prints stats for the amount of words you want
    for i in range(desired_word_count):
        if i < len(counted_list):
            print(f'" {counted_list[i][1]} " appeared {counted_list[i][0]} times. That means this word took up about {counted_list[i][0] * 100 // len(words_list)}% of the text.')


main()
