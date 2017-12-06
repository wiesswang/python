# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 10:05:54 2017

@author: 王欢欢(wanghuanhuan)
"""

#定义分子类（Molecule）作为基类
class Molecule:
    def __init__(self):
        self.elements = set()
        self.weight = None
    def show_weight(self):
        print self.weight
    def show_elements(self):
        print self.elements
#定义AminoAcid类
elements_weights = {'C':12, 'H':1, 'O':16, 'N':14, 'S':32} #元素质量
class AminoAcid(Molecule):
    def __init__(self):
        #继承Molecule
        Molecule.__init__(self)
        self.composition = {'C':0,'H':0,'O':0,'N':0,'S':0} #0指个数，氨基酸的元素组成
    def calc_mw(self):
        weights = 0
        for i in self.composition:  #计算分子量
            weights += elements_weights[i]*self.composition[i]
        self.weight = weights      #赋值
    def show_weight(self):
        self.calc_mw()             #调用calc_mw方法
        Molecule.show_weight(self) #调用基类的show_weight方法
    def show_elements(self):
        elements = set()
        for i in self.composition: #用self.composition的非零值的键生成集合
            if self.composition[i]!=0:
                elements.add(i)
        self.elements = elements   #赋值
        print 'Elements are ', self.elements #打印集合
        
#定义亮氨酸（Leucine）、异亮氨酸（Isoleucine）、半胱氨酸（Cysteine）类
class Leucine(AminoAcid):
    def __init__(self):
        AminoAcid.__init__(self)
        self.composition = {'C':6, 'H':13, 'O':2, 'N':1, 'S':0} #Leucine的元素组成赋值
    def show_composition(self):
        print self.composition       #打印Leucine的元素组成
    def is_isoform(self,aa):
        isoform = True
        for i in self.composition:   #判断是否是同分异构体
            if self.composition[i] != aa.composition[i]:
                isoform = False
            return isoform
            
class Isoleucine(AminoAcid):
    def __init__(self):
        AminoAcid.__init__(self)
        self.composition = {'C':6, 'H':13, 'O':2, 'N':1, 'S':0} #Isoleucine的元素组成赋值
    def show_composition(self):
        print self.composition      #打印Isoleucine的元素组成
    def is_isoform(self,aa):
        isoform = True
        for i in self.composition:
            if self.composition[i] != aa.composition[i]:
                isoform = False
            return isoform

class Cysteine(AminoAcid):
    def __init__(self):
        AminoAcid.__init__(self)
        self.composition = {'C':6, 'H':13, 'O':2, 'N':1, 'S':0} #Cysteine的元素组成赋值
    def show_composition(self):
        print self.composition     #打印Cysteine的元素组成
    def is_isoform(self,aa):
        isoform = True
        for i in self.composition:
            if self.composition[i] != aa.composition[i]:
                isoform = False
            return isoform
#生成实例
leu = Leucine()
ile = Isoleucine()
cys = Cysteine()

#调用函数
leu.show_weight()
leu.show_elements()
leu.show_composition()

ile.show_weight()
ile.show_elements()
ile.show_composition()

cys.show_weight()
cys.show_elements()
cys.show_composition()

print leu.is_isoform(ile)
print leu.is_isoform(cys)
