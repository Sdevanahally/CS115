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


#so basically first you take the RGB input and then
#then you solve for w using the formula w= max((r_input/255), (g_input/255), (b_input/255))
#then you put it into the formula for cmyk -- c= (((w-(r/255))/w), m= (((w-(g/255))/w), y= (((w-(b/255))/w), k= (1-w)
#return CYMK
