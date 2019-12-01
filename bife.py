from PIL import Image
import sys
import numpy

brailleDict = {
    1 : "⠁", 2 : "⠂", 3 : "⠃", 
    4 : "⠄", 5 : "⠅", 6 : "⠆", 7 : "⠇", 
    8 : "⠈", 9 : "⠉", 10 : "⠊", 11 : "⠋", 
    12 : "⠌", 13 : "⠍", 14 : "⠎", 15 : "⠏", 
    16 : "⠐", 17 : "⠑", 18 : "⠒", 19 : "⠓", 
    20 : "⠔", 21 : "⠕", 22 : "⠖", 23 : "⠗", 
    24 : "⠘", 25 : "⠙", 26 : "⠚", 27 : "⠛", 
    28 : "⠜", 29 : "⠝", 30 : "⠞", 31 : "⠟", 
    32 : "⠠", 33 : "⠡", 34 : "⠢", 35 : "⠣", 
    36 : "⠤", 37 : "⠥", 38 : "⠦", 39 : "⠧", 
    40 : "⠨", 41 : "⠩", 42 : "⠪", 43 : "⠫", 
    44 : "⠬", 45 : "⠭", 46 : "⠮", 47 : "⠯", 
    48 : "⠰", 49 : "⠱", 50 : "⠲", 51 : "⠳", 
    52 : "⠴", 53 : "⠵", 54 : "⠶", 55 : "⠷", 
    56 : "⠸", 57 : "⠹", 58 : "⠺", 59 : "⠻", 
    60 : "⠼", 61 : "⠽", 62 : "⠾", 63 : "⠿", 
    64 : "⡀", 65 : "⡁", 66 : "⡂", 67 : "⡃", 
    68 : "⡄", 69 : "⡅", 70 : "⡆", 71 : "⡇", 
    72 : "⡈", 73 : "⡉", 74 : "⡊", 75 : "⡋", 
    76 : "⡌", 77 : "⡍", 78 : "⡎", 79 : "⡏", 
    80 : "⡐", 81 : "⡑", 82 : "⡒", 83 : "⡓", 
    84 : "⡔", 85 : "⡕", 86 : "⡖", 87 : "⡗", 
    88 : "⡘", 89 : "⡙", 90 : "⡚", 91 : "⡛", 
    92 : "⡜", 93 : "⡝", 94 : "⡞", 95 : "⡟", 
    96 : "⡠", 97 : "⡡", 98 : "⡢", 99 : "⡣", 
    100 : "⡤", 101 : "⡥", 102 : "⡦", 103 : "⡧", 
    104 : "⡨", 105 : "⡩", 106 : "⡪", 107 : "⡫", 
    108 : "⡬", 109 : "⡭", 110 : "⡮", 111 : "⡯", 
    112 : "⡰", 113 : "⡱", 114 : "⡲", 115 : "⡳", 
    116 : "⡴", 117 : "⡵", 118 : "⡶", 119 : "⡷", 
    120 : "⡸", 121 : "⡹", 122 : "⡺", 123 : "⡻", 
    124 : "⡼", 125 : "⡽", 126 : "⡾", 127 : "⡿", 
    128 : "⢀", 129 : "⢁", 130 : "⢂", 131 : "⢃", 
    132 : "⢄", 133 : "⢅", 134 : "⢆", 135 : "⢇", 
    136 : "⢈", 137 : "⢉", 138 : "⢊", 139 : "⢋", 
    140 : "⢌", 141 : "⢍", 142 : "⢎", 143 : "⢏", 
    144 : "⢐", 145 : "⢑", 146 : "⢒", 147 : "⢓", 
    148 : "⢔", 149 : "⢕", 150 : "⢖", 151 : "⢗", 
    152 : "⢘", 153 : "⢙", 154 : "⢚", 155 : "⢛", 
    156 : "⢜", 157 : "⢝", 158 : "⢞", 159 : "⢟", 
    160 : "⢠", 161 : "⢡", 162 : "⢢", 163 : "⢣", 
    164 : "⢤", 165 : "⢥", 166 : "⢦", 167 : "⢧", 
    168 : "⢨", 169 : "⢩", 170 : "⢪", 171 : "⢫", 
    172 : "⢬", 173 : "⢭", 174 : "⢮", 175 : "⢯", 
    176 : "⢰", 177 : "⢱", 178 : "⢲", 179 : "⢳", 
    180 : "⢴", 181 : "⢵", 182 : "⢶", 183 : "⢷", 
    184 : "⢸", 185 : "⢹", 186 : "⢺", 187 : "⢻", 
    188 : "⢼", 189 : "⢽", 190 : "⢾", 191 : "⢿", 
    192 : "⣀", 193 : "⣁", 194 : "⣂", 195 : "⣃", 
    196 : "⣄", 197 : "⣅", 198 : "⣆", 199 : "⣇", 
    200 : "⣈", 201 : "⣉", 202 : "⣊", 203 : "⣋", 
    204 : "⣌", 205 : "⣍", 206 : "⣎", 207 : "⣏", 
    208 : "⣐", 209 : "⣑", 210 : "⣒", 211 : "⣓", 
    212 : "⣔", 213 : "⣕", 214 : "⣖", 215 : "⣗", 
    216 : "⣘", 217 : "⣙", 218 : "⣚", 219 : "⣛", 
    220 : "⣜", 221 : "⣝", 222 : "⣞", 223 : "⣟", 
    224 : "⣠", 225 : "⣡", 226 : "⣢", 227 : "⣣", 
    228 : "⣤", 229 : "⣥", 230 : "⣦", 231 : "⣧", 
    232 : "⣨", 233 : "⣩", 234 : "⣪", 235 : "⣫", 
    236 : "⣬", 237 : "⣭", 238 : "⣮", 239 : "⣯", 
    240 : "⣰", 241 : "⣱", 242 : "⣲", 243 : "⣳", 
    244 : "⣴", 245 : "⣵", 246 : "⣶", 247 : "⣷", 
    248 : "⣸", 249 : "⣹", 250 : "⣺", 251 : "⣻", 
    252 : "⣼", 253 : "⣽", 254 : "⣾", 255 : "⣿"
}

""" BRAILLE PATTERNS """
def getBraillePattern(array):
    # expects arg of [[x, x], [x, x], [x, x], [x, x]]
    res = 0
    if not array[0][0]:
        res += 1
    if not array[1][0]:
        res += 2
    if not array[2][0]:
        res += 4
    if not array[0][1]:
        res += 8
    if not array[1][1]:
        res += 16
    if not array[2][1]:
        res += 32
    if not array[3][0]:
        res += 64
    if not array[3][1]:
        res += 128
    return brailleDict[res]

def preparePixelArray(pixelArray):
    rowsCount = len(pixelArray)
    colsCount = len(pixelArray[0])
    fakeRow = [True] * colsCount

    # must at least be divisible by 4
    while rowsCount % 4 != 0:
        pixelArray.append(fakeRow)
        rowsCount += 1
    
    # cols must be even
    if colsCount % 2 != 0:
        for i in pixelArray:
            i.append(True)
        colsCount += 1
    
    return int((rowsCount * colsCount) / 8), colsCount
    

def generateBrailleArt(pixelArray, totalChar, colsCount):
    # generate braille art here
    fileArt = open("brailleArt.txt", "w", encoding="utf8")

    rowSkip = 0
    colSkip = 0

    for count in range(0, totalChar):

        braille = getBraillePattern([
            [pixelArray[(rowSkip * 4)    ][(colSkip * 2)], pixelArray[(rowSkip * 4)    ][(colSkip * 2) + 1]],
            [pixelArray[(rowSkip * 4) + 1][(colSkip * 2)], pixelArray[(rowSkip * 4) + 1][(colSkip * 2) + 1]],
            [pixelArray[(rowSkip * 4) + 2][(colSkip * 2)], pixelArray[(rowSkip * 4) + 2][(colSkip * 2) + 1]],
            [pixelArray[(rowSkip * 4) + 3][(colSkip * 2)], pixelArray[(rowSkip * 4) + 3][(colSkip * 2) + 1]]
        ])
        fileArt.write(braille)

        colSkip += 1
        
        # After each "end of line"
        if int(colsCount/2) == colSkip:
            fileArt.write("\n")
            rowSkip += 1
            colSkip  = 0

    fileArt.close()


def applyTreshold(threshold, image):
    fn = lambda x : 255 if x > threshold else 0
    return image.convert('L').point(fn, mode='1')


def getArgumentValue(string, args):
    string = "+" + string + "="
    for i, argument in enumerate(args):
        if string in argument:
            value = argument.split("=")
            value = value[1]
            value.split("'")
            value.split('"')
            args.pop(i)
            return value
    return None

def findArgument(string, args):
    for i, argument in enumerate(args):
        if string == argument:
            args.pop(i)
            return True
    return False

# Args without python file
sys.argv.pop(0)
args = sys.argv

# Open the file
filename = getArgumentValue("file", args)
if filename is not None:
    img = Image.open(filename)
else:
    raise ValueError("No file defined")

# Threshold argument
threshold = getArgumentValue("t", args)
if threshold is not None:
    threshold = int(threshold)
else:
    raise ValueError("No value for threshold")

# Percentage to be reduced
percentage = getArgumentValue("scale", args)
if percentage is not None:
    percentage = int(percentage)
    width  = int(round(img.size[0] * (percentage / 100)))
    height = int(round(img.size[1] * (percentage / 100)))
    # Resize image
    img = img.resize((width, height), Image.ANTIALIAS)

# Point instead of blank space
space = findArgument("+dotted+", args)
if space == True:
    brailleDict[0] = "⠄"
else:
    brailleDict[0] = " "

# Apply treshold
newImg = applyTreshold(threshold, img)

# Create an array of pixels
pixelArray = numpy.array(newImg).tolist()

# Prepare array
totalChar, colsCount = preparePixelArray(pixelArray)

# Generate txt file
generateBrailleArt(pixelArray, totalChar, colsCount)

print("Succesful!")