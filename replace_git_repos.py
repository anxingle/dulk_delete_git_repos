import re
import lake

# 正则表达式匹配相关信息
replace = re.compile(r'https://github.com/anxingle/')
with open("./save_tap_list.txt", "r") as f:
    lines = f.readlines()
    urls = []
    for line in lines:
        # repos = re.findall(r'le/\w+\s|', line)
        repos = replace.sub(r'', line)
        print repos
        lake.file.add_txt(repos, "./github_repos.txt")
        urls += line
# print urls
replace2 = re.compile(r'\s.+')
with open("./github_repos.txt", "r") as f:
    lines = f.readlines()
    urls = []
    for line in lines:
        # repos = re.findall(r'le/\w+\s|', line)
        repos = replace2.sub(r'', line)
        print repos
        lake.file.add_txt(repos, "./dulk_delete_repos.txt")
        urls += line
