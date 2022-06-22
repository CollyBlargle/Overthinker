import json
import datetime
from datetime import timedelta
from dateutil import parser
from collections import Counter
from statistics import mean

# Questions I want answered:
# Who usually texts first?
# Who usually is the conversation ender?
# Average response time?
# Average amount of characters per message?
# Total characters per block?
# Total amount of characters sent?

def main(filePath, timeInput = 8):
    #Validity checks
    try:
        with open(filePath, encoding= "utf8") as f:
            chatLog = json.load(f)
    except:
        return "Invalid file."

    # A "text block" is defined as a group of consecutive messages sent by a single author.
    # A "conversation" is defined as a group of consecutive blocks in which each block's messages 
    # has a response time less than conversationTimeThreshold. 

    # Convert messages to blocks

    result = {}

    blocks = []
    conversations = [[]]
    
    try:
        conversationTimeThreshold = delta = timedelta(hours=int(timeInput))
    except ValueError:
        return "Invalid hours (Are you sure you inputted an integer amount?)."
    except OverflowError:
        return "Too many hours."
    if int(timeInput) < 0:
        return "Did you input negative hours?"
    
    previousMessageTimestamp = None
    currentMessageAuthor = None
    previousMessageAuthor = None

    responseTimes = {}
    charactersPerBlock = {}
    totalCharacters = {}

    try:
        for message in chatLog["messages"]:
            currentMessageAuthor = message["author"]["id"]
            
            if not previousMessageTimestamp is None:
                responseTime = parser.parse(message["timestamp"]) - previousMessageTimestamp
            if currentMessageAuthor == previousMessageAuthor and responseTime < conversationTimeThreshold:
                blocks[len(blocks) - 1].append(message)
            else:
                blocks.append([message])
            previousMessageAuthor = currentMessageAuthor
            previousMessageTimestamp = parser.parse(message["timestamp"])
    except KeyError:
        return "Improperly formatted chat log."

    lastMessagePreviousBlock = None
    firstMessageCurrentBlock = None


    # Convert blocks to conversations

    for block in blocks:
        firstMessageCurrentBlock = block[0]

        # Get characters of message
        charactersInBlock = 0
        for message in block:
            charactersInBlock += len(message["content"])
        
        if not message["author"]["name"] in totalCharacters:
            totalCharacters[message["author"]["name"]] = charactersInBlock
        else:
            totalCharacters[message["author"]["name"]] += charactersInBlock
        
        if not message["author"]["name"] in charactersPerBlock:
            charactersPerBlock[message["author"]["name"]] = [charactersInBlock]
        else:
            charactersPerBlock[message["author"]["name"]].append(charactersInBlock)
        
        if not lastMessagePreviousBlock is None:
            responseTime = parser.parse(firstMessageCurrentBlock["timestamp"]) - parser.parse(lastMessagePreviousBlock["timestamp"])
            if responseTime < conversationTimeThreshold:
                # Get response time of each chatter
                if not firstMessageCurrentBlock["author"]["name"] in responseTimes:
                    responseTimes[firstMessageCurrentBlock["author"]["name"]] = [responseTime.total_seconds()]
                else:
                    responseTimes[firstMessageCurrentBlock["author"]["name"]].append(responseTime.total_seconds())
                
                # Append to conversations
                conversations[len(conversations) - 1].append(block)
            else:
                conversations.append([block])
        else:
            conversations[0].append(block)
        lastMessagePreviousBlock = block[len(block) - 1]
    
    for chatter in responseTimes:
        responseTimes[chatter] = str(datetime.timedelta(seconds=round(mean(responseTimes[chatter]), 1))).split(".")[0]
    
    for chatter in charactersPerBlock:
        charactersPerBlock[chatter] = round(mean(charactersPerBlock[chatter]), 1)

    # Find amount of times texted first and last
    textFirst = []
    textLast = []
    for conversation in conversations:
        textFirst.append(conversation[0][0]["author"]["name"])
        textLast.append(conversation[len(conversation)- 1][0]["author"]["name"])
    textFirst = dict(Counter(textFirst))
    textLast = dict(Counter(textLast))

    result["textFirst"] = textFirst
    result["textLast"] = textLast
    result["responseTimes"] = responseTimes
    result["charactersPerBlock"] = charactersPerBlock
    result["totalCharacters"] = totalCharacters

    # print(result["textFirst"],
    #     result["textLast"],
    #     result["responseTimes"],
    #     result["charactersPerBlock"],
    #     result["totalCharacters"])
    return result

#defaultdict is probably better than constantly checking if a key exists..

if __name__ == "__main__":
    main()