#-*-coding:utf8;-*-
#qpy:3
#qpy:console

pressure=float(input("Enter the pressure:-"))

print(pressure,"Bar")

Tc=62.35*pressure-21.89

print(Tc,"Degree Centigrade")

Tk=273+Tc


print(Tk,"Degree Kelvin")

Tf=32+1.8*Tc

print(Tf,"Degree farenheit")

