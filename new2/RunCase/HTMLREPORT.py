import unittest
from Tools.HTMLTestRunner import HTMLTestRunner
import time
discover=unittest.defaultTestLoader.discover("../case",pattern="test*.py")
if __name__ == '__main__':
    # 定义报告生成的路径-文件夹
    report_dir="../Report/"
    # 定义时间戳
    nowtime=time.strftime("%Y.%m.%d %H.%M.%S")
    # 组装完整的报告地址+文件名
    report_name=report_dir+nowtime+"Reprt.html"
    with open(report_name,"wb") as f:
        runner=HTMLTestRunner(stream=f,title="HBV项目自动化执行结果！",description="HBV项目自动化测试报告")
        runner.run(discover)