# import glob2
import os
# filenames = glob2.glob('*.txt')  # list of all .txt files in the directory
# filenames=sorted(filenames)
# with open('outfile.txt', 'w') as f:
#     for file in filenames:
#         with open(file) as infile:
#             f.write(infile.read()+'\n')
def concatFiles():
    path = 'Data/Annotation/'
    files = sorted(os.listdir(path))

    for idx, infile in enumerate(files):
        print ("File #" + str(idx) + "  " + infile)
    concat = ''.join([open(path + f).read()+'\n' for f in files])
    with open("Data/Annotation/Annotation.txt", "w") as fo:
        fo.write(concat)

if __name__ == "__main__":
    concatFiles()
