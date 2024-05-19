print("九宫格导航页面")

# 定义九宫格导航菜单
menu = {
    "首页": "/home",
    "新闻": "/news",
    "视频": "/videos",
    "图片": "/photos",
    "论坛": "/forum",
    "博客": "/blog",
    "购物": "/shop",
    "音乐": "/music",
    "设置": "/settings"
}

# 打印九宫格导航菜单
for key, value in menu.items():
    print(f"{key}: {value}")
