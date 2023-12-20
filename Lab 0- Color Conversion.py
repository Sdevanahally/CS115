#Sandya Devanahally - Color Conversion Lab:
#I Pledge my honor that I have abided by the Stevens Honor Code

r_input = int(input("Enter r input:"))
g_input = int(input("Enter g input:"))
b_input = int(input("Enter b input:"))

w= max((r_input/255), (g_input/255), (b_input/255))
c=(w-(r_input/255))/w
m=(w-(g_input/255))/w
y=(w-(b_input/255))/w
k=1-w
cmyk_output = (c+m+y+k)
print(cmyk_output)
