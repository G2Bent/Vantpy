import os,unittest,time
from report.Runner.HTMLTestRunner3 import HTMLTestRunner

def create_suite():
    TestSuite = unittest.TestSuite()#测试集
    # test_dir = os.getcwd()+'\\TestCase\\'
    test_dir = os.path.realpath('TestCase')

    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='test_*.py',
        top_level_dir=None
    )

    # print (discover)

    for test_case in discover:
        TestSuite.addTests(test_case)
    return TestSuite

def report():
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # report_name = os.getcwd()+'\\Report\\result.html'
    report_name = os.path.join(os.path.realpath("report"), 'result.html')
    return report_name


if __name__ == '__main__':

    fp = open(report(), 'wb')

    TestSuite = create_suite()
    Runner = HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='测试用例执行情况'
    )
    Runner.run(TestSuite)

    fp.close()