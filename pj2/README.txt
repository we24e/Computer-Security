0. Xuyang Wang     netid:xw313

1. Basically, my client program first reads a line in the HNS text file, and send it to RS first. 
When received a message from RS, my client program will first check whether ' - NS' is in the message or not. 
If it is in, extract the TS hostname and send the message to TS. 
If not, write the message into the RESOLVED file. 
After receiving message from TS, write whatever message that is from TS into the RESOLVED file. 
After receiving all messages and sent all messages, the client program will end. 

2. I haven't found any errors through my tests, as all the functionalities seem to be working fine. 

3. There are many problems that i faced, such as how to get the ip address of the server, how to create an array with text messages, etc. 
The biggest problem is that it is really difficult to implement the function in the second announcement. 
I really can't find a way to rewrite just a line by searching " - NS" and replace the line, as this is what needed
in the DNSRS file, so i can only rewrite the whole file to update just the TS ip address and it took me LOTS of time. 

4. I learned more about python, as well as how can one client program connect to a server program remotely. 
Most importantly, I learned how can one client connect to multiple servers, as well as a bit more infor 
about how sockets work. 