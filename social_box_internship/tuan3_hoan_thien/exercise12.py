import re


class RegularExpression:
    def phone_number(self, str):
        return [x.strip() for x in re.findall(r'[\d|-|.|\s]{10,}', str)]

    def string_in_tag(self, str):
        #return [x for x in re.findall('[^(<|</)em>]+', str)]
        return [x for x in re.findall(r'[^</em>]+', str)]

str_phone = """ĐƠN VỊ CHỦ QUẢN:
Địa chỉ: Toà nhà Skyline, Nguyễn Khuyến, Văn Quán, Hà Đông, Hà Nội

SĐT: 0944 328.989 - Email: cskh@biluxury.vn

Mã số thuế / Mã số doanh nghiệp: 0107273793

Đăng ký lần đầu : 30/12/2015, Sở KHĐTHN - Đăng ký thay đổi lần thứ 4, ngày 05/07/2019, Sở KHĐTHN"""

str = "Xin chào <em>đồng chí</em>, đồng chí <em>yếu đuối</em> quá"

regex = RegularExpression()
result_phone = regex.phone_number(str_phone)
print(str_phone)
print("\nSDT:", result_phone)
result_str = regex.string_in_tag(str)

print(result_str)
