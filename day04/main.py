# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


from scrapy.cmdline import execute

import sys
import os


if __name__=='__main__':
    # 设置工程的目录，可以在任何路径下运行execute
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    execute(["scrapy", "crawl", "doubanmovie250"])
    pass



# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助