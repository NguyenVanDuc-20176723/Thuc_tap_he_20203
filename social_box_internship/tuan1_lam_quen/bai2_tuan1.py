def process_tag_html(str_tag_html="", prop=""):
    value = ""
    list = str_tag_html.split('=')
    len_prop = len(list) - 1
    for i in range(len_prop):
        item = list[i].split()
        if item[-1] == prop:
            value = list[i + 1].split()[0].strip('">')
            break
    return value


stri = "<meta property=\"og:image\" itemprop=\"thumbnailUrl\" " \
       "content=\"https://s1.vnecdn.net/vnexpress/restruct/i/v341/logo_default.jpg\">"
prop = "content"
result = process_tag_html(stri, prop)
print(result)
