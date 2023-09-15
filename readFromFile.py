#read from file
#the variable we use to handle a file is called file handel

#f = open('example.txt','r') # r =read, w=write, a=append, x=create
#print(f.read())
#print(f.read(10)) #to read 1st 10 characters
#print(f.readline())
#iterating every line
'''
for x in f:
    print(x)'''

#write mode
'''
f = open('example.txt','w')
f.write('Writing using Python')'''
#it has removed all the data from the past and write the new data only
#the solution is append mode
'''
f = open('example.txt','a') #for opening in append mode
f.write("Yes! We did it!\n")
print("Operation Done!")
'''
'''
f = open('example.txt','r')
print(f.read())
f = open('example.txt','a')
f.write("I am now enjoying doing this."+"\n")
print("DOne!")
f.close()
'''
#handeling files professionally
#context manager use kori cause eta auto file close kore dey

with open('example.txt','r') as f:
    size = 10
    while (f.read() != ''):
        print(f.read(size))


    #print(f.read()) #if we use read it will the wole file to the ram and for big files it's troublesum so we can use readline function. readline function reads one line at a time and for next iteration it starts reading exactly where it sopped last time
    #print(f.readline())
   # print(f.readline())
    '''
    for x in f:
        print(x)
'''
    #print(f.read(10)) #for handeling big files we can load in a certain size
    #print(f.read(10))






