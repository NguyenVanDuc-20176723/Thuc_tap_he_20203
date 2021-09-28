from lxml import html
import requests as rq
import re
import time
from pandas import DataFrame
import csv
import os
from concurrent.futures import ThreadPoolExecutor
import concurrent
import copy

company_num = 0
list_details = []
progress_count = 0


def send_with_thread_executor(max_workers, list_url_details):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for url in list_url_details:
            futures.append(
                executor.submit(
                    get_company_detail, url['link']
                )
            )


def get_category(link=''):
    res = rq.get(link)
    tree = None

    if res.status_code == 200:
        tree = html.fromstring(res.content)
    if tree is not None:
        category_xpath = '//div[@style="height:auto; width:160px; margin-top:28px; float:left"]//a/'
        category_link = tree.xpath(category_xpath + '@href')
        category_name = tree.xpath(category_xpath + 'text()')
        for i in range(len(category_link)):
            yield {
                'name': category_name[i],
                'link': category_link[i]
            }


def get_industry(link=''):
    res = rq.get(link)
    tree = None
    if res.status_code == 200:
        tree = html.fromstring(res.content)
    if tree is not None:
        industry_xpath = '//div[@class="niengiam_bigcategory_box"]//a/'
        industry_link = tree.xpath(industry_xpath + '@href')
        industry_name = tree.xpath(industry_xpath + 'text()')
        for i in range(len(industry_link)):
            yield {
                'name': industry_name[i].strip(),
                'link': industry_link[i]
            }


def max_page(tree):
    xpath = '//div[@id="paging"]//a//text()'
    page_list = tree.xpath(xpath)
    page_int_list = [int(x) for x in page_list if x.isdigit()]
    return max(page_int_list)


def get_company(link):
    if not link or len(link) == 0:
        print('Invalid company detail link')
        return []
    global company_num
    count = 0
    page = 1
    element_num = 0
    page_max = 0
    while True:
        res = rq.get(link + f'?page={page}')
        tree = None
        if res.status_code == 200:
            tree = html.fromstring(res.content)
        if tree is not None:
            company_xpath = '//div[@id="main_listing"]//h2[@class="company_name"]//a/'
            company_name = tree.xpath(company_xpath + 'text()')
            company_link = tree.xpath(company_xpath + '@href')

            if page == 1:
                # search company number
                str_num = tree.xpath('//div[@id="searh_result_span"]//text()')
                company_num = int(re.findall(r'\d+', str_num[0])[0])
                # company default number in a page
                element_num = len(company_link)
                # max page number
                page_max = max_page(tree)

            for i in range(len(company_link)):
                yield {
                    # 'name': company_name[i],
                    'link': company_link[i]
                }
            count += len(company_link)
            # print('page:', page)
            # print('length:', company_num)
            # print('count:', count)
            # print('cong:', len(company_link))
            page += 1
            if count >= company_num or len(company_link) < element_num or page > page_max:
                break

    print('length:', company_num)
    print('count:', count)


def get_company_detail(link):
    if not link or len(link) == 0:
        print('Invalid company detail link')
        return None
    try:

        contact_info = {}
        res = rq.get(link)
        tree = None
        if res.status_code == 200:
            tree = html.fromstring(res.content)
        else:
            print(f'Error: status_code = {res.status_code}')

        if tree is not None:
            name_xpath = '//h1[@id="company_name_h1"]'
            address_xpath = '//div[@id="detail_diachi_box"]//span[@style="line-height:20px"]'
            industry_xpath = '//div[@class="detail_nganhnghe"]//a'
            web_xpath = '//div[@id="detail_diachi_box"]//p[@class="diachi_box_p"]/a[@rel="nofollow"]'
            contact_info_key_xpath = '//div[@id="listings_right"]//div[@class="contact_div"]//div[@class="contact_left"]'
            contact_info_value_xpath = '//div[@id="listings_right"]//div[@class="contact_div"]//div[@class="contact_right"]'
            phone_xpath = '//div[@id="detail_diachi_box"]//span[@class="span_mathoai"]'

            name = tree.xpath(name_xpath + '/text()')
            address = tree.xpath(address_xpath + '/text()')
            industry = [ind.strip() for ind in tree.xpath(industry_xpath + '/text()')]
            website = tree.xpath(web_xpath + '/text()')
            contact_info_key = tree.xpath(contact_info_key_xpath + '/text()')
            contact_info_value = [value.strip() for value in tree.xpath(contact_info_value_xpath + '//text()')]
            phone = tree.xpath(phone_xpath + '/text()')

            phone_num = set()
            for p in re.findall(r'[^,\-:a-zA-Z]+', phone[0]):
                sub_phone = re.sub(r'[^\d]+', '', p)
                if len(sub_phone) >= 10 and sub_phone[0] == '0':
                    phone_num.add(sub_phone)

            contact_info['company'] = name[0]
            contact_info['address'] = address[0]
            contact_info['industry'] = list(set(industry))
            website = [web.strip() for web in website]
            contact_info['website'] = list(set(website))

            contact_info['phone'] = phone_num
            contact_info['contact_person'] = ''
            contact_info['is_hotline'] = ''
            contact_info['gender'] = ''
            contact_info['position'] = ''
            contact_info['email'] = ''
            for i in range(len(contact_info_key)):
                if contact_info_key[i] == 'Điện thoại:' or contact_info_key[i] == 'Di động:':
                    for p in re.findall(r"[^-,]+", contact_info_value[i]):
                        p = re.sub(r"[^\d]+", '', p)
                        if len(p) >= 10 and p[0] == '0':
                            contact_info['phone'].add(p)
                elif contact_info_key[i] == 'Người liên hệ:':
                    contact_info['contact_person'] = contact_info_value[i]
                elif contact_info_key[i] == 'Chức vụ:':
                    contact_info['position'] = contact_info_value[i]
                elif contact_info_key[i] == 'Email:':
                    contact_info['email'] = contact_info_value[i]
            contact_info['phone'] = list(contact_info['phone'])

            if contact_info['position'].lower() == 'Hotline'.lower():
                contact_info['is_hotline'] = 'X'

            if contact_info['contact_person'].lower() == 'Hotline'.lower():
                contact_info['is_hotline'] = 'X'
            elif len(contact_info['contact_person']) > 0:
                str_gender = re.findall(r"\w+", contact_info['contact_person'])[0]
                if str_gender.lower() == 'Mr'.lower() or str_gender.lower() == 'Ông'.lower():
                    contact_info['gender'] = 'male'
                elif str_gender.lower() == 'Ms'.lower() or str_gender.lower() == 'Msr'.lower() or str_gender.lower() == 'Bà'.lower():
                    contact_info['gender'] = 'female'
            # print('----------------------')
            # print('contact information:', contact_info)
            # print('----------------------')
            contact_info['url'] = link
        print(contact_info['company'])

        list_details.append(contact_info)

    except Exception as e:
        print(e)


def process_object(obj):
    re_obj = copy.copy(obj)
    re_obj['industry'] = "__".join(re_obj['industry'])
    if len(re_obj['phone']) == 0:
        re_obj['phone'] = ''
    else:
        re_obj['phone'] = "\'" + "__".join(re_obj['phone']).strip('_') + "\'"

    re_obj['website'] = "__".join(re_obj['website'])
    # print(re_obj)
    return re_obj


def write_csv(file, data, indus):
    global progress_count
    writer = csv.DictWriter(file, fieldnames=list(data[0].keys()))
    if progress_count == 0:
        writer.writeheader()

    progress_count += len(data)
    for item in data:
        item = process_object(item)
        writer.writerow(item)
    print("-----------------")
    print(f"industry: {indus['name']}")
    print(f'Progess [{progress_count}/{company_num}], Save company sucessfully')
    print("-----------------")


def main(dir_path, link):
    global list_details
    global progress_count
    list_company = []
    try:
        os.makedirs(dir_path, exist_ok=True)
    except OSError as e:
        print(e)
    industrys = get_industry(link)
    for industry in industrys:
        companys = get_company(industry['link'])
        progress_count = 0
        file_name = re.sub(r"/", ',', industry['name'])
        with open(f"{dir_path}{file_name}.csv", mode="w+") as f:
            for company in companys:
                try:
                    list_company.append(company)
                    if len(list_company) == 20:
                        send_with_thread_executor(10, list_company)
                        list_company = []
                        write_csv(f, list_details, industry)
                        list_details = []

                except Exception as e:
                    print(e)
            try:
                send_with_thread_executor(10, list_company)
                list_company = []
                write_csv(f, list_details, industry)
                list_details = []
            except Exception as e:
                print(e)
            f.close()


def category_index(index, category):
    for i in range(index - 1):
        next(category)
    return next(category)


url_home = 'https://www.yellowpages.vn/'
categorys = get_category(url_home)

category = category_index(5, categorys)
dir_path = f'./scrawl_data/{category["name"]}/'

url = category['link']
main(dir_path, url)
print("COMPLETED CRAWL")
