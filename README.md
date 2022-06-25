# Overthinker
 Python-based JSON parser of chatlogs converted from DiscordChatExporter (https://github.com/Tyrrrz/DiscordChatExporter) 

# Input
 File: Produce a JSON file from DiscordChatExporter (https://github.com/Tyrrrz/DiscordChatExporter) and feed it into this program.
 
 Hours: This is the amount of hours until a conversation is declared finished. A conversation is defined as the set of messages exchanged between the chatters until the hour threshold is reached. This is used to determine when a conversation is started or ended by a chatter.

# Statistics
 Times chatter texted first: If a new conversation is started by a chatter, that respective chatter increments this statistic.
 
 Times chatter texted last: If a conversation ends with a message by a chatter, that respective chatter increments this statistic.
 
 Average response time: The average amount of time a chatter takes until responding, given a conversation has started. This excludes time between conversations.
 
 Average characters per block: A block of text is a group of consecutive messages sent by a single chatter. Each message is within the timeframe of the hour threshold defined by input. Thus, three messages sent by a single chatter in quick succession would be grouped up as one "block".
 
 Total amount of characters: The total amount of characters sent by each chatter.
 
 Total edits: The total amount of messages that were edited by each chatter.

# Notes
This program is incredibly inefficient. It churns through 10000 messages in about 5 seconds for my lower-end computer. It iterates through the messages to create the blocks, and then to create the conversations from the blocks, and finally parses through the conversations to generate the results. I feel like this could be done in one iteration given some cleverness. I tried this method, but it became rather unwieldy and less readable.

Perhaps an implementation with .csv files could be good since the filetype was designed for stuff like this I believe.. I'm rather unfamiliar with R and other data-science languages though..

This was my first GUI. I was hoping to get a modal window for the result window, and working icons but I decided I didn't care.

I'm not sure if the numbers are completely accurate. I wasn't very diligent with my test-cases. I really only wrote this program for myself.

Some other statistics I might want implemented are the amount of memes sent by each chatter, and removing those characters from the total character count.

I struggle a lot with overthinking. I thought this program would help. I'd get concrete numbers on statistics I constantly speculated about. But now that I have the numbers, I realize their invalidity. Really, there are more factors to simple messaging than how one feels about the other. Some people just.. don't feel like talking. That doesn't mean they hate you. So.. Try not to think too hard. If you want to know how your friend feels about you, just ask. you guys are friends, yeah?
