#ColourPix2box
#Python 3.6.2
#script BigБро
#idea Zirum

# example result in "colour".txt
# <spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
#for \AC-Game\data\static_data\spawns\(Npcs or gather)\New\location.xml
#Possible colour npcs
#Red:
#400317	Рубин
#401109	Огромный Рубин
#400107	Красный Мифрил
#400211	Красный Орихалк
#gray:
#400158	Иридий 
#400206	Адамантит
#blue:
#400314	Аквамарин
#401103	Огромный Аквамарин
#green:
#400706	Кестал
#white:
#400320	Алмаз
#401110	Огромный Алмаз
#black:
#700395	Ящик (маленький) 
#brown:
#700326	Ящик со снастями (маленький)
#701016	Ящик суканы (средний)
#yellow:
#218571	Сундук
#409054	Эфир 60ур. 01 (средний)
#409055	Эфир 60ур. 02 (маленький)

from PIL import Image

im = Image.open('faschid_face_29x49.bmp','r')
width, height = im.size
#print(width, height)
pix_val = list(im.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]
#this reads RGB from initial pixels in upper left corner, beginning in second row and second line in .bmp-file
#this RGB values are only information to manual adjust colour values for each colour
#to see this values start this script in IDLE 
print(pix_val_flat[3*1+1*width*3],pix_val_flat[3*1+1*width*3+1],pix_val_flat[3*1+1*width*3+2])
print(pix_val_flat[3*2+1*width*3],pix_val_flat[3*2+1*width*3+1],pix_val_flat[3*2+1*width*3+2])
print(pix_val_flat[3*3+1*width*3],pix_val_flat[3*3+1*width*3+1],pix_val_flat[3*3+1*width*3+2])
print(pix_val_flat[3*4+1*width*3],pix_val_flat[3*4+1*width*3+1],pix_val_flat[3*4+1*width*3+2])
print(pix_val_flat[3*5+1*width*3],pix_val_flat[3*5+1*width*3+1],pix_val_flat[3*5+1*width*3+2])

#insert your game coordinates, starting in bottom left corner
x0=1895.92
y0=1584.91
z0=122
h0 = 0

# Item size
iw = 0.5
ih = 0.5
il = 0.5


file = open ('gray.txt', 'w')
for h in range (0, height-1):
  for w in range (0, width-1):
#RGB (R 51..64, G 51..64, B 64..79) if python dont see this colour adjust here RGB values with values you get from upper part
    color_black = pix_val_flat[(3*w+h*width*3)] > 50 and pix_val_flat[(3*w+h*width*3)] < 65 and \
                  pix_val_flat[(3*w+h*width*3)+1] > 50 and pix_val_flat[(3*w+h*width*3)+1] < 65 and \
                  pix_val_flat[(3*w+h*width*3)+2] > 65 and pix_val_flat[(3*w+h*width*3)+2] < 80
    if color_black:
     x = x0+w*iw 
     y = y0
     z = z0+(height-h)*ih
     file.write('<spot h="{:d}" x="{:.1f}" y="{:.1f}" z="{:.1f}"/>\n'.format(h0, x, y, z))
file.close()

file = open ('black.txt', 'w')
for h in range (0, height-1):
  for w in range (0, width-1):
#RGB (R <25, G <25, B <25) if python dont see this colour adjust here RGB values with values you get from upper part
    color_black = pix_val_flat[(3*w+h*width*3)] < 25 and \
                  pix_val_flat[(3*w+h*width*3)+1] < 25 and \
                  pix_val_flat[(3*w+h*width*3)+2] < 25
    if color_black:
     x = x0+w*iw 
     y = y0
     z = z0+(height-h)*ih
     file.write('<spot h="{:d}" x="{:.1f}" y="{:.1f}" z="{:.1f}"/>\n'.format(h0, x, y, z))
file.close()

file = open ('lime.txt', 'w')
for h in range (0, height-1):
  for w in range (0, width-1):
#RGB (R <20, G >200, B <20) if python dont see this colour adjust here RGB values with values you get from upper part
    color_black = pix_val_flat[(3*w+h*width*3)] < 20 and \
                  pix_val_flat[(3*w+h*width*3)+1] > 200 and \
                  pix_val_flat[(3*w+h*width*3)+2] < 20
    if color_black:
     x = x0+w*iw 
     y = y0
     z = z0+(height-h)*ih
     file.write('<spot h="{:d}" x="{:.1f}" y="{:.1f}" z="{:.1f}"/>\n'.format(h0, x, y, z))
file.close()

file = open ('lightbrown.txt', 'w')
for h in range (0, height-1):
  for w in range (0, width-1):
#RGB (R >200, G 138..156, B 79..109) if python dont see this colour adjust here RGB values with values you get from upper part
    color_black = pix_val_flat[(3*w+h*width*3)] > 200 and \
                  pix_val_flat[(3*w+h*width*3)+1] > 137 and pix_val_flat[(3*w+h*width*3)+1] < 157 and \
                  pix_val_flat[(3*w+h*width*3)+2] > 80 and pix_val_flat[(3*w+h*width*3)+2] < 110
    if color_black:
     x = x0+w*iw 
     y = y0
     z = z0+(height-h)*ih
     file.write('<spot h="{:d}" x="{:.1f}" y="{:.1f}" z="{:.1f}"/>\n'.format(h0, x, y, z))
file.close()

file = open ('darkgreen.txt', 'w')
for h in range (0, height-1):
  for w in range (0, width-1):
#RGB (R 25..43, G 71..89, B 50..68) if python dont see this colour adjust here RGB values with values you get from upper part
    color_black = pix_val_flat[(3*w+h*width*3)] > 24 and pix_val_flat[(3*w+h*width*3)] < 44 and \
                  pix_val_flat[(3*w+h*width*3)+1] > 70 and pix_val_flat[(3*w+h*width*3)+1] < 90 and \
                  pix_val_flat[(3*w+h*width*3)+2] > 49 and pix_val_flat[(3*w+h*width*3)+2] < 69
    if color_black:
     x = x0+w*iw 
     y = y0
     z = z0+(height-h)*ih
     file.write('<spot h="{:d}" x="{:.1f}" y="{:.1f}" z="{:.1f}"/>\n'.format(h0, x, y, z))
file.close()
#if you need more colours copy and paste lines 83 to 95 and adjust txt-file name and RGB values.
