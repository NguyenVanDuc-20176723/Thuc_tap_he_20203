from itertools import combinations


class SumThreeRealIsZero:
    def __init__(self, list_number):
        self.list = list_number

    def sum_three_num_is_zero(self):
        re_list = []
        list_number = self.list
        length = len(list_number)
        for x in range(length - 2):
            for y in range(x + 1, length - 1):
                for z in range(y + 1, length):
                    sum = list_number[x] + list_number[y] + list_number[z]
                    if sum == 0:
                        re_list.append([list_number[x], list_number[y], list_number[z]])
        return re_list

    def three_element_has_sum_is_zero(self):
        re_list = []
        list_number = self.list
        for item in combinations(list_number, 3):
            if sum(item) == 0:
                re_list.append(item)
        return re_list


list = [3, 4.5, -2, 3.5, -1, -5.5, 2, 1]
obj = SumThreeRealIsZero(list)
result1 = obj.sum_three_num_is_zero()
print(result1)
result2 = obj.three_element_has_sum_is_zero()
print(result2)
