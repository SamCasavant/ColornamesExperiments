import csv
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import mplcursors

fig = plt.figure()
ax = plt.axes(projection='3d')
rdata = np.array([])
gdata = np.array([])
bdata = np.array([])
colors = np.array([])
labels = np.array([])
words = {}

count = 0
with open('colornames.txt', newline = '') as colornames:
    reader = csv.reader(colornames, delimiter = ',', quotechar = '|')
    for row in reader:
        color = row[0]
        for word in row[1].lower().split(" "):
            if word not in ["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"]:
                try:
                    words[word].append((int(color[:2], 16), int(color[2:4], 16), int(color[4:6], 16)))
                except KeyError:
                    try: 
                        words[word] = [(int(color[:2], 16), int(color[2:4], 16), int(color[4:6], 16))]
                    except ValueError:
                        pass
                
                    
        # if 'the' in row[1].lower():
        #     color = row[0]
        #     red = int(color[:2], 16)
        #     green = int(color[2:4], 16)
        #     blue = int(color[4:6], 16)
        #     rdata = np.append(red, rdata)
        #     gdata = np.append(green, gdata)
        #     bdata = np.append(blue, bdata)
        #     colors = np.append("#" + color[:6], colors)
        #     label = row[1:]
        #     labels.append(label)
        #     count +=1

ax.set_xlabel('red')
ax.set_ylabel('green')
ax.set_zlabel('blue')




named_color_count = 0
average_named_color = (0, 0, 0)
for key in words.keys():
    length = len(words[key])
    if length > 30 or key == 'pastel':#key in ['red', 'orange', 'yellow', 'green', 'purple', 'blue', 'brown', 'magenta', 'tan', 'cyan', 'olive', 'maroon', 'navy', 'aquamarine', 'turquoise', 'silver', 'lime', 'teal', 'indigo', 'violet', 'pink', 'black', 'white', 'gray']:
        rtotal = 0
        gtotal = 0
        btotal = 0
        for color in words[key]:
            rtotal = rtotal + color[0]**2
            gtotal = gtotal + color[1]**2
            btotal = btotal + color[2]**2
        named_color_count += length

        r_avg = (rtotal/length)**.5
        g_avg = (gtotal/length)**.5
        b_avg = (btotal/length)**.5
        if r_avg > 220 or g_avg > 220 or b_avg > 220 or r_avg < 50 or g_avg < 50 or b_avg < 50:
            rdata = np.append(r_avg, rdata)
            gdata = np.append(g_avg, gdata)
            bdata = np.append(b_avg, bdata)
            colors = np.append('#%02x%02x%02x' % (round(r_avg), round(g_avg), round(b_avg)), colors)
            labels = np.append(key, labels)
ax.scatter3D(rdata, gdata, bdata, c = colors)

for x, y, z, label, color in zip(rdata, gdata, bdata, labels, colors):
    ax.text(x, y, z, label, color = color, fontsize = 8, ha= 'center', va='top')
#mplcursors.cursor(ax).connect(
#    "add", lambda sel: sel.annotation.set_text(labels[sel.target.index])
#)



plt.show()