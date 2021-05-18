file=open("index.html","r")
myData= file.read().replace("</body>","<p>Oh a new Line, added via GitHub actions</p>\n</body>")
file.close()

file=open("index.html","w")
file.write(myData)
file.close()
print("Done!")
