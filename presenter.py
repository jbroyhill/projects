# Import packages necessary
import sumy, wikipedia, pyttsx3
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

converter = pyttsx3.init()
converter.setProperty('rate', 160)
converter.setProperty('volume', .09)
def summarize_the_research(): # Our primary function
    print("_" * 100, "\n")
    print("\n\n\t\t*** The Library of Alexandria ***\n")
    print("\n\nWelcome to the library. Please input three topics for research.")
    while True:
        search1 = input("\nPlease select your first topic.\n")
        print("Input received. Please specify your research topic.\n")
        print(wikipedia.search(search1))
        topic1 = input("Input a research topic.\n")
        research1 = wikipedia.page(topic1) # Sets our first research topic
        search2 = input("\nPlease select your second topic.\n")
        print("Input received. Please specify your research topic.\n")
        print(wikipedia.search(search2))
        topic2 = input("Input a research topic.\n")
        research2 = wikipedia.page(topic2) # Sets our second research topic
        search1 = input("\nPlease select your third topic.\n")
        print("Input received. Please specify your research topic.\n")
        print(wikipedia.search(search1))
        topic3 = input("Input a research topic.\n")
        research3 = wikipedia.page(topic3) # Sets our third research topic
        print("You have chosen these three topics:")
        print(topic1)
        print(topic2)
        print(topic3)
        print("Would you like to proceed with your research or reset and choose three different topics?")
        userChoice = input("1. Continue Research. 2. Choose 3 different topics\n")
        if userChoice == "1":
            print("Please wait...")
            break
        elif userChoice == "2":
            print("Returning to the beginning...")
    f = open('research_results.txt', 'w', encoding='utf8')  # Creates txt file to save output

    data1 = research1.content # Creates variable for content to summarize
    data2 = research2.content # Creates variable for content to summarize
    data3 = research3.content # Creates variable for content to summarize
    parser1 = PlaintextParser.from_string(data1, Tokenizer("english")) # Creates variable to parse data
    parser2 = PlaintextParser.from_string(data2, Tokenizer("english")) # Creates variable to parse data
    parser3 = PlaintextParser.from_string(data3, Tokenizer("english")) # Creates variable to parse data
    summarizer = LexRankSummarizer() # Creates variable to utilize algorithim to summarize data
    number_of_sentences_in_summary = 10 # Number of sentences to output as summary
    summary1 = summarizer(parser1.document, number_of_sentences_in_summary) # Summarizes data per parser and sentence number
    summary2 = summarizer(parser2.document, number_of_sentences_in_summary) # Summarizes data per parser and sentence number
    summary3 = summarizer(parser3.document, number_of_sentences_in_summary) # Summarizes data per parser and sentence number

    # now print out our result summary
    print("\n\n\n\n\t *** Summary of the research ***\n\n")
    print("\t*** Summary of the research ***\n\n", file=f)
    print("\n\n\n ", str(topic1), "Information!")
    print("\n\n\n", str(topic1), "Information!", file=f)
    for sentence in summary1: # Loop that summarizes information, outputting one sentence at a time
        print(sentence) # Prints out one sentence of summar
        converter.say(sentence)
        file_output1 = str(sentence) # Turns sentence into a string so we can output it to a file
        print(file_output1.encode("utf-8"), file=f) # Outputs summary to file
    print("\n\n\n", topic2, " Information!")
    print("\n\n\n", topic2, " Information!", file=f)
    for sentence in summary2: # Loop that summarizes information, outputting one sentence at a time
        print(sentence) # Prints out one sentence of summary
        converter.say(sentence)
        file_output2 = str(sentence) # Turns sentence into a string so we can output it to a file
        print(file_output2.encode("utf-8"), file=f) # Outputs summary to file
    print("\n\n\n", topic3, " Information!")
    print("\n\n\n", topic3, " Information!", file=f)
    for sentence in summary3: # Loop that summarizes information, outputting one sentence at a time
        print(sentence) # Prints out one sentence of summary
        converter.say(sentence)
        file_output3 = str(sentence) # Turns sentence into a string so we can output it to a file
        print(file_output3.encode("utf-8"), file=f) # Outputs summary to file
    print("\n\n\n\t *** Finished! Check research_results.txt for a saved version of this output *** ")
    converter.runAndWait()


# Start of program is main

def main(): # Our main function
    # Program driver which controls memeory flow
    print("\n\n\n\n\n\t*** This AI summarizes research! Please be patient, it may take a moment to gather your information. ***\n\n")
    summarize_the_research() # Calling our summarization function


# If the main function exists, call it!
if __name__ == "__main__":
    main() # Calls main function