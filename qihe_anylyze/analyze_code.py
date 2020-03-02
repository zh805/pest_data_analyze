#coding:utf-8
import os,re
#代码所在目录
FILE_PATH = './'

def analyze_code(codefilesource):
    total_line = 0
    comment_line = 0
    blank_line = 0
    # with open(codefilesource,encoding='gb18030',errors='ignore') as f:
    with open(codefilesource,'r',encoding='UTF-8') as f:
        lines = f.readlines()
        total_line = len(lines)
        # print(total_line)
        line_index = 0
        #遍历每一行
        while line_index < total_line:
            line = lines[line_index]
            #检查是否为注释
            if line.startswith("#"):
                comment_line += 1
            elif re.match("\s*'''",line) is not None:
                comment_line += 1
                while re.match(".*'''$",line) is None:
                    line = lines[line_index]
                    comment_line += 1
                    line_index += 1
            #检查是否为空行
            elif line =='\n':
                blank_line += 1
            line_index += 1
    print("在%s中:"%codefilesource)
    print("代码行数：",total_line)
    print("注释行数:",comment_line,"占%0.2f%%"%(comment_line*100/total_line))
    print("空行数:", blank_line, "占%0.2f%%"%(blank_line * 100 / total_line))
    return [total_line,comment_line,blank_line]
def run(FILE_PATH):
    os.chdir(FILE_PATH)
    #遍历py文件
    total_lines = 0
    total_comment_lines = 0
    total_blank_lines = 0
    for i in os.listdir(os.getcwd()):
        # print(i)
        if os.path.splitext(i)[-1] == '.py':
            # print(i)
            line = analyze_code(i)
            total_lines,total_comment_lines,total_blank_lines=total_lines+line[0],total_comment_lines+line[1],total_blank_lines+line[2]
    print("总代码行数:",total_lines)
    print("总注释行数:",total_comment_lines,"占%0.2f%%"%(total_comment_lines*100/total_lines))
    print("总空行数:", total_blank_lines, "占%0.2f%%"% (total_blank_lines * 100 / total_lines))

if __name__ == '__main__':
    run(FILE_PATH)