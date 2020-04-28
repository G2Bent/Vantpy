## <center> **Vantpy2.0**</center>

#### 关于更新1.21
Vantpy更新的内容：
1. 兼容Linux系统，mac系统，跨系统使用，多人协作
2. 删除绝对路径的读取，改为相对路径的读取
3. 加入接口测试模块
4. 集成Jenkins，测试报告采用Allure测试报告
5. 添加随机生成器，使测试用例更灵活
6. 对selenium二次开发添加新的操作
7. 实现有界面与无界面之间的切换

 ![](/screenshots/vantpy2.0.jpg) 
--------------------------------------- 


---
#### 关于框架：
Vantpy框架基于Selenium+Yaml+Unittest搭建的WebUI自动化测试框架

#### 特点：
- 使用POM（页面对象模式）设计，使代码更加有逻辑性，测试脚本更加规范，后期更加容易维护以及复用性更高
- 支持多种定位方式，包括（xpath/css/ID/text/link_text/name）
- 框架集成了Selenium的常用定位方法，使元素定位更加方便
- 使用HTMLTestRunner作为自动生成测试报告，报告更加美观，更加详细，内容更丰富
- Logging日志输出，可以看到每一步做的操作
- Yaml作为数据管理，实现代码，数据分离，使框架的使用起来更加简单

#### 部署环境：
- Python 3.6+：https://www.python.org/

#### 使用到的package：

> pip install requirements.txt

#### 支持的浏览器及驱动：
基于Selenium支持的所有浏览器

```
browser == "Chrome"
browser == "firefox"
browser == "IE"
browser == "phantomjs"
browser == "opera"
browser == "edge"
```
geckodriver(Firefox):https://github.com/mozilla/geckodriver/releases

Chromedriver(Chrome):https://sites.google.com/a/chromium.org/chromedriver/home

IEDriverServer(IE):http://selenium-release.storage.googleapis.com/index.html

operadriver(Opera):https://github.com/operasoftware/operachromiumdriver/releases

MicrosoftWebDriver(Edge):https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver

#### 定位元素方式：

```
class BaiduPage(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    search_loc =(By.XPATH,'//*[@id="kw"]')#定位百度文本框

    def input_baidu_text(self,text):
        self.send_key(self.search_loc,text)
```

#### 读取yaml数据

```
brwserType:
  browserName : Chrome

testUrl:
  URL : https://www.baidu.com
```

#### 日志输出

```
2018-06-02 14:58:13,521  - INFO - You had select Chrome browser.
2018-06-02 14:58:13,524  - INFO - The test url is: https://www.baidu.com
2018-06-02 14:58:19,629  - INFO - Starting Chrome browser.
2018-06-02 14:58:20,456  - INFO - Open url: https://www.baidu.com
2018-06-02 14:58:21,607  - INFO - Maximize the current window.
2018-06-02 14:58:21,609  - INFO - Set implicitly wait 5 seconds.
2018-06-02 14:58:21,609  - INFO - Clear input-box: //*[@id="kw"]...
2018-06-02 14:58:22,723  - INFO - Input element by xpath: //*[@id="kw"]...
2018-06-02 14:58:22,723  - INFO - Input: selenium
```

#### 生成测试报告

```
def report():
    if len(sys.argv) > 1:
        report_name = os.path.dirname(os.getcwd()) + '\\report\\' + sys.argv[1] + '_result.html'
    else:
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        # 需要查看每段时间的测试报告，可以这样写：
        # report_name = os.getcwd() + '\\report\\'+now+'result.html'
        report_name = os.path.dirname(os.getcwd()) + '\\report\\result.html'
    return report_name
    
fp = open(report(), 'wb')
Runner = HTMLTestRunner(
    stream=fp,
    title='测试报告',
    description='测试用例执行情况'
)
```
#### 测试报告
![自动化测试报告](https://upload-images.jianshu.io/upload_images/3404835-b27828973a200528.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


