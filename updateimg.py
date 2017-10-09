# coding=utf-8
import xlrd
import os
import platform
import img

basePath = r"./alimama"
if platform.system() == 'Windows':
    basePath = r"D:/alimama"

for parent, dirnames, filenames in os.walk(basePath):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:  # 输出文件信息
        xlname=os.path.join(parent,filename)
        print r"filename is ",xlname.decode('gbk')
        workbook = xlrd.open_workbook(xlname)
        sheet = workbook.sheet_by_index(0)

        header=sheet.row_values(0)

        cols=sheet.col_values(2)
        for col_inx in xrange(sheet.nrows):
            if (col_inx == 0) :
                continue
            print '---',col_inx,'---',cols[col_inx]
            img.save_url('d:/mamaimg/'+cols[col_inx].split('/')[-1],cols[col_inx])



        for row_index in xrange(sheet.nrows):
            break
            if row_index==0:
                continue
#            if row_index > 10 :
#                break
            rows=sheet.row_values(row_index)
            for inx in xrange(sheet.ncols):
#            for inx in [12,1,2,3,5,20,21]:
                print '---',row_index,'---',header[inx],rows[inx]
            print '-----------------------------------------'

