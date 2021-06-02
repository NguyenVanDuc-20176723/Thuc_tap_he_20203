import random
import re


class ProcessNumber:
    def create_five_number(self):
        list_five_num = []
        while len(list_five_num) < 5:
            element = random.randrange(100, 200)
            if (element % 3) == 0:
                list_five_num.append(element)
        return list_five_num

    def create_list_number_from_str(self, string=""):
        return [int(x) for x in re.findall('\d+', string)]


obj = ProcessNumber()
print(obj.create_five_number())
str_list = "Tôi từng tự ý bán cả danh mục 20-30 mã cổ phiếu của " \
           "một chị khách rất thân quen trong năm 2007 và bị cằn nhằn " \
           "không dứt, may là tình chị em vẫn còn sau đợt khủng hoảng đó."
print(obj.create_list_number_from_str(str_list))
