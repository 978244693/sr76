import os
from PyPDF2 import PdfFileReader,PdfFileMerger,PdfFileWriter

# 拆分pdf
def split_pdf(a, b):

    pdf_open = open(a, 'rb')
    read_pdf = PdfFileReader(pdf_open)
    n1 = read_pdf.getNumPages()  # 计算此PDF文件中的页数
    print("文档共有%s页" % n1)
    writer = PdfFileWriter()
    x = int(input("宝宝输入需要截取PDF文档的起始页（数字）："))    #起始页数
    y = int(input("宝宝输入需要截取PDF文档的的终止页（数字）："))      # 终止页数
    start = x -1   # 起始页数  range 从0开始，所以需要-1，才能与偏移量对应。 如range(0,3)，实际打印结果是0,1,2。
    end = y   # 终止页数   终止页数这里不用-1，如range(0,3)，实际是0,1,2 因此用户输入3，实际结果是2，其实也是对应的第3页。

    for i in range(start, end):
        writer.addPage(read_pdf.getPage(i))
    pdf_write = open(b, "wb")
    writer.write(pdf_write)
    pdf_open.close()
    pdf_write.close()
    print("切分完毕！提取源文档第{}-{}页".format(x, y))
    print()
    print('切分好的文件名字默认为split.pdf，宝宝可以查看下')
    print()
    shuru = input("是否继续使用？继续输入y，输入其它键退出：")
    if shuru == 'y':
        path = 'D:\\chaifenpdf'
        for i in os.listdir(path):
            lujing = os.path.join(path, i)  # 拼接路径,i为遍历的文件名。
            print('要拆分的文件为：' + lujing)  # 带路径的文件名
            # print(path)    文件所在路径
            a = lujing
            # a = input('请输入文件名字（如 D:\\laopo\\pdf\\try.pdf）：')
            b = 'split.pdf'
            split_pdf(a, b)
    else:
        exit()

# 合并PDF
def hebing():

    # path =input('手动输入需要合并的PDF文件夹地址：如：D:\laopo\pdf  ：')
    path = 'D:\\readpdf'
    result_pdf = PdfFileMerger()    #依次读取每个文件的内容，并进行合并。
    n1_list =[]  # 存放pdf文档页数

    for i in os.listdir(path):
        lujing = os.path.join(path,i)  #拼接路径,i为遍历的文件名。
        print(lujing)  #  带路径的文件名
        # print(path)    文件所在路径
        pdf_file = lujing

        with open(pdf_file,'rb') as f:
            pdf_reader = PdfFileReader(f)
            n1 = pdf_reader.getNumPages()  # 计算此PDF文件中的页数
            n1_list.append(n1)
            print(pdf_file+"文档共有%s页" % n1)
            result_pdf.append(pdf_reader,import_bookmarks=True)

    result_pdf.write('Merge.pdf')
    print('合并完成,文件名字为Merge.pdf','合并总页数为：'+str(sum(n1_list)))
    result_pdf.close()
    print()
    a = input("是否继续？输入y继续，输入其他任意字符退出：")
    if a == 'y':
        hebing()
    else:
        exit()

if __name__ == '__main__':
    try:
        qun = input("然然PDF专用小工具，1=拆分PDF，2=合并PDF，只能输入1或者2：")
        if qun == "1":
            print('注意：')
            print('1，需要在D盘创建一个名为：chaifenpdf的文件夹。\n'
                  '2.并把需要拆分的单独一个pdf文档放在里面。\n'
                  '3.切记，每次只能放入一个需要拆分的PDF，不支持多个'
                  )
            h = input('看完说明后，在D盘创建好chaifenpdf文件夹放入要拆分的pdf文档，再按j键继续程序。')
            if h == 'j':
                path ='D:\\chaifenpdf'
                for i in os.listdir(path):
                    lujing = os.path.join(path, i)  # 拼接路径,i为遍历的文件名。
                    print('要拆分的文件为：'+lujing)  # 带路径的文件名
                    # print(path)    文件所在路径
                    a = lujing
                    # a = input('请输入文件名字（如 D:\\laopo\\pdf\\try.pdf）：')
                    b = 'split.pdf'
                    split_pdf(a, b)
        elif qun == '2':
            print('注意：')
            print('1，需要在D盘创建一个名为：readpdf的文件夹。\n'
                  '2.并把需要合并的pdf文档都一起放在readpdf文件夹下。\n'
                  )
            h = input('看完说明后，创建好对应的文件夹放入pdf文档，再按j键继续程序。')
            if h == 'j':
                hebing()
    except:
        exit()