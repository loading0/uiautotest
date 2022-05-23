# WEB UI自动化回归脚本说明文档
## 本地搭建项目运行环境

1. **进入项目根目录**，创建项目虚拟环境并安装项目依赖包文件就可以跑项目了。
    ```bash
    ### Linux下
    # 创建项目虚拟环境
    python3 -m venv venv
    # 激活虚拟环境
    source venv/bin/activate
    # 先更新pip版本
    pip3 install -i https://pypi.douban.com/simple -U pip
    # 安装项目依赖包文件
    pip3 install -i https://pypi.douban.com/simple -r requirements.txt
    
    ### Windows下
    # 创建项目虚拟环境
    python -m venv venv
    # 激活虚拟环境
    cd venv/Scripts
    activate
    # 先更新pip版本
    pip install -i https://pypi.douban.com/simple -U pip
    # 安装项目依赖包文件
    pip install -i https://pypi.douban.com/simple -r requirements.txt
    ```
## 项目目录结构介绍
* `common`：封装的一些基础常用类。
    * `base.py`对象库层，对selenium基本方法进行二次封装
    * `chromedriver`本地机器上安装了chrome浏览器，这个是对应的chromedriver驱动文件
    * `driver_init.py`web driver初始化的封装，在测试用例类里的`setup`方法里，每次创建页面page的对象时需要传入此driver初始化方法
    
* `configs`：封装一些配置文件相关
    * `config.ini`配置文件，里边包含了`是否无头模式运行测试用例`,`测试地址`,`driver版本`,`测试地址登录的账号和密码信息`,在运行`main.py`文件时会将控制台传入的参数写入到此配置文件中
    * `config.py`配置文件封装的相关方法

* `utils`: 封装一些工具类
    * `assertion.py`断言封装类
    * `log.py`日志文件的封装
* `logs`:存放日志文件
* `pages_locators`: 存放相关页面元素定位
* `pages_actions`: 封装相关页面的基本功能或模块的操作
* `report`: Json文件夹存放allure生成的json格式结果文件，Html文件夹存放生成的html报告，index.html为报告首页
* `testcases`:测试用例文件夹，
     * `mall_manage`:商城管理相关测试用例
* `case_count.py`:计算测试用例数目，用于测试结果看板使用
* `main.py`：测试启动入口
* `requirements.txt`：项目依赖软件包清单文件

### 增加用例
1. **务必在`case_count.py`文件中引入测试用例的类名**
2. `case_count.py`文件中`get_nums`方法是为了计算所有测试用例个数，为UI自动化回归的结果看板提供数据

## jenkins集成
1. jenkins配置好report_path, headless, domain,driverVersion, case_Path
2. 构建，执行shell，python执行main.py并传入上方配置的参数
