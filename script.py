import markdown2
tmp= markdown2.markdown("**-markdown2 up and running!**")

file=open("index.html","r")
myData= file.read().replace("</body>",f"{tmp}\n</body>")
file.close()

file=open("index.html","w")
file.write(myData)
file.close()
print("Done!")
