import json
import datetime
from datetime import timedelta
from dateutil import parser
from collections import Counter
from statistics import mean

# Questions I want answered:
# Who usually texts first?
# Average response time?
# Average amount of characters per message?
# Total characters per block?
# Total amount of characters sent?
# Who usually is the conversation ender?

def main(filePath):
    result = {}

    with open(filePath, encoding= "utf8") as f:
        chatLog = json.load(f)

    # A "text block" is defined as a group of conseccutive messages sent by a single author.
    # A "conversation" is defined as a group of conseccutive blocks in which each block's messages 
    # has a response time less than conversationTimeThreshold. 

    # Convert messages to blocks

    blocks = []
    conversations = [[]]
    conversationTimeThreshold = delta = timedelta(hours=8)

    previousMessageTimestamp = None
    currentMessageAuthor = None
    previousMessageAuthor = None

    responseTimes = {}
    charactersPerBlock = {}
    totalCharacters = {}

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
        responseTimes[chatter] = round(mean(responseTimes[chatter]), 1)
    
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

    print(result["textFirst"],
        result["textLast"],
        result["responseTimes"],
        result["charactersPerBlock"],
        result["totalCharacters"])
    return result

if __name__ == "__main__":
    main()