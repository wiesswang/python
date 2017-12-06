# python
第一次python作业

统计下面蛋白序列中20种氨基酸或DNA序列中4种碱基的个数和频率：

         >sp|fa1  MNAPERQPQPDGGDAPGHEPGGSPQDELDFSILFDYEYLNPNEEEPNAHKVASPPSGPAYPDDVLDYGLKPYSPLASLSGEPPGRFGEPDRVGPQKFLSAAKPAGASGLSPRIEITPSHELIQAVGPLRMRDAGLLVEQPPLAGVAASPRFTLPVPGFEGYREPLCLSPASSGSSASFISDTFSPYTSPCVSPNNGGPDDLCPQFQNIPAHYSPRTSPIMSPRTSLAEDSCLGRHSPVPRPASRSSSPGAKRRHSCAEALVALPPGASPQRSRSPSPQPSSHVAPQDHGSPAGYPPVAGSAVIMDALNSLATDSPCGIPPKMWKTSP
         
         >sp|fa2 MSIIGATRLQNDKSDTYSAGPCYAGGCSAFTPRGTCGKDWDLGEQTCASGFCTSQPLCARKTQVCGLRYSSKGKDPLVSAEWDSRGAPYVRCTYDADLIDTQAQVDQFVSMFGESPSLAERYCMRGVKNTAGELVSRVSSDADPAGGWCRKWYSAHRGPDQDAALGSFCIKNPGAADCKCINRASDPVYQKVKTLHAYPDQCWYVPCAADVGELKMGTQRDTPTNCPTQVCQIVFNMLDDGSVTMDDVKNTINCDFSKYVPPPPPPKPTPPTPPTPPTPPTPPTPPTPPTPRPVHNRKVMFFVAGAVLVAILISTVRW

提示和要求：用循环、字典等实现，并将频率输出到名为frq.txt的文本文件中，且文件的第一行必须是标题行，包含20列，每一列为对应氨基酸的单字母符号，列间用Tab键’\t’分割。

homework1为代码；seq.fa.txt为蛋白质序列；frq.txt为结果文件

第二次python作业

定义分子类（Molecule）作为基类，包含集合elements和weight作为其属性，用初始化函数，将elements初始化为空集，weight初始化为None；定义show_weight方法，该方法用print函数打印输出分子量weight；定义show_elements方法，用print函数打印输出元素集合。

定义AminoAcid类，继承Molecule类，包含composition属性，并初始化为下面的元素字典：{‘C’: 0, ‘H’: 0, ‘O’: 0, ‘N’: 0, ‘S’: 0}；定义calc_mw方法，根据根据字典的元素组成，计算其分子量（需要用到每种原子的质量，自己去查），并给继承自父类的weight属性赋值；重载show_weight方法，在其中调用calc_mw方法，计算氨基酸的分子量，再调用父类的show_weight方法，打印输出weight值；重载show_elements方法，用元素字典中的非零值的键生成元素集合，再打印输出元素集合。

分别定义亮氨酸（Leucine）、异亮氨酸（Isoleucine）、半胱氨酸（Cysteine）类，均继承自AminoAcid类，在初始化方法中，根据这三种氨基酸的元素组成（这个要自己去查），为其继承来的元素字典的各元素对应赋值；定义show_composition方法，打印输出氨基酸的元素字典；在Leucine类中定义is_isoform方法，接受一个氨基酸对象作为参数，根据氨基酸的元素组成，判断是否为当前氨基酸的同分异构体，返回布尔值（True或者False）。

分别生成Leucine、Isoleucine、Cysteine类的实例leu、iso、cys，通过该实例，调用其show_weight、show_elements、show_composition等方法，查看当前氨基酸的分子量、元素集合、元素字典；通过leu，调用其is_isoform方法，分别以实例iso和cys为参数，查看各自的返回值，以判定是否同分异构体。



