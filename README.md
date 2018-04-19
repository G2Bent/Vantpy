## **Vantpy**

---
#### 关于框架：
Vantpy框架基于Selenium3+unittest搭建的WebUI自动化测试框架

#### 特点：
- 使用POM（页面对象模式）设计，使我们写的代码更加简单，后期更加容易维护以及复用性更高
- 支持多种定位方式，包括（xpath/css/ID/text/link_text/name）
- 框架集成了Selenium的常用定位方法，也是在我们经常使用到的方法
- 使用HTMLTestRunner框架自动生成测试报告，使我们更直观查看报告的内容
- 集成断言一层验证，截图二层验证的方法，使我们的定位问题精准性更高

#### 部署环境：
- Python 3.6+：https://www.python.org/
- Selenium3.8.0+：https://pypi.python.org/pypi/selenium

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
search_loc = (By.XPATH,'//*[@id="kw"]')

def input_baidu_text(self,text):
    self.find_element(*self.search_loc).send_keys(text)
```

```
By.NAME,'百度'  
By.ID,'ID'   
By.LINK_TEXT,'Link_text'   
By.CSS_SELECTOR,'CSS'   
By.CLASS_NAME,'Class_name'   
...
```
#### 自动化测试报告

![enter image description here](http://images.gitbook.cn/8af0c470-ff2f-11e7-806c-257f5e05f705)
