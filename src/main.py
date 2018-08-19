# coding=utf-8
import sys
import os
import subprocess

def quiz10(text):
    return len(text.split("\n"))

def quiz11(text):
    return text.replace("\t", " ")

def quiz12(text):
    output = [[], []]
    f1 = open("../tmp/col1.txt", "w", encoding="utf-8")
    f2 = open("../tmp/col2.txt", "w", encoding="utf-8")
    for line in text.split("\n"):
        if len(line.split("\t")) <= 1:
            break
        output[0].append(line.split("\t")[0])
        output[1].append(line.split("\t")[1])
        f1.write(line.split("\t")[0] + "\n")
        f2.write(line.split("\t")[1] + "\n")
    f1.close()
    f2.close()
    # 結果表示用
    res  = "col1.txt\n"
    res += "\n".join(output[0]) + "\n"
    res += "col2.txt\n"
    res += "\n".join(output[1]) + "\n"
    return res

def quiz13(text):
    output = []
    f1 = open("../tmp/col1.txt", "r", encoding="utf-8")
    f2 = open("../tmp/col2.txt", "r", encoding="utf-8")
    fo = open("../tmp/col1and2.txt", "w", encoding="utf-8")
    while True:
        line1 = f1.readline()
        line2 = f2.readline()
        if line1 == "" or line2 == "":
            break
        fo.write("%s\t%s\n" % (line1[:-1], line2[:-1]))
        output.append("%s\t%s\n" % (line1[:-1], line2[:-1]))
    f1.close()
    f2.close()
    return "".join(output)

def quiz14(text, N):
    return "\n".join(text.split("\n")[:N])

def quiz15(text, N):
    return "\n".join(text.split("\n")[-N:])

def quiz16(text, N):
    output = []
    nl    = quiz10(text)
    split = int(float(nl)/N)   
    for n in range(N):
        with open("../tmp/splited%d_%d.txt" % (n, N), "w", encoding="utf-8") as f:
            f.write("\n".join(text.split("\n")[split*n:split*(n+1)])) 
            output.append("\n".join(text.split("\n")[split*n:split*(n+1)]))
            if n == N-1:
                f.write("\n" + text.split("\n")[-1])
                output[-1] += "\n" + text.split("\n")[-1]
    res = ""
    for i in range(len(output)):
        res += "\nsplited%d_%d:\n" % (i, len(output))
        res += output[i]
    return res

def quiz17(text):
    output = [line.split("\t")[0] for line in text.split("\n")]
    # 最終行の空行分を無視するためのフィルタ
    output = [o for o in output if len(o) > 0]
    return set(output)

def quiz18(text):
    output = [tuple(line.split("\t")) for line in text.split("\n")]
    # 最終行の空行分を無視するためのフィルタ
    output = [o for o in output if len(o) == 4]
    # 最高気温で降順ソート
    output = sorted(output, key=lambda x:x[2])[::-1]

    # 出力用に整形
    res = ""
    for o in output:
        res += "%s\t%s\t%s\t%s\n" % o
    return res

def quiz19(text):
    output = {}
    for line in text.split("\n"):
        word = line.split("\t")[0]
        # 空行のフィルタリング
        if len(word) <= 0:
            continue
        if word not in output.keys():
            output[word]  = 1
        else:
            output[word] += 1
    output = [o[0] for o in sorted(output.items(), key=lambda x:x[1])[::-1]]
    return "\n".join(output)

if __name__ == "__main__":
    args = sys.argv
    if len(args) <= 1 or os.path.exists(args[1]) == False:
        print("invalid input")
        exit()
    with open(args[1], "r", encoding="utf-8") as f:
        text = f.read()
    print(text)

    print("---10---")
    print(quiz10(text))

    print("---11---")
    print(quiz11(text))
    
    print("---12---")
    print(quiz12(text))

    print("---13---")
    print(quiz13(text))

    print("---14---")
    print(quiz14(text, 3))

    print("---15---")
    print(quiz15(text, 3))

    print("---16---")
    print(quiz16(text, 3))

    print("---17---")
    print(quiz17(text))
    
    print("---18---")
    print(quiz18(text))

    print("---19---")
    print(quiz19(text))
