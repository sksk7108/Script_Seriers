# 淘宝购物脚本
## 1 介绍
这是一个由本人编写用于淘宝抢购的python脚本，主要用于双十一等活动抢购准点发放购物、前n名买一送一...的商品，使用前需要设置抢购时间，获取到所抢购商品的勾选框的xpath，建议在购物活动开始前十分钟开启此脚本最佳。
## 2 教程
### 2.1 环境搭建
- 安装selenium
> pip install selenium==4.1.3 -i https://pypi.tuna.tsinghua.edu.cn/simple

- 查看Chrome浏览器的版本号（只需知道以点分隔的前三个版本号即可）
![image](https://user-images.githubusercontent.com/105795298/230870842-b3a59239-49d3-445e-a440-08427c73f695.png)

- 下载浏览器驱动（Chrome）
> Chrome浏览器驱动下载网址：https://registry.npmmirror.com/binary.html?path=chromedriver/

> 下载前3个版本号相同的驱动

![image](https://user-images.githubusercontent.com/105795298/230871575-21a9134e-a6a9-4ecc-adee-cc7f78c4000a.png)

- 将下载好的驱动放在与python.exe同级的目录内
![image](https://user-images.githubusercontent.com/105795298/230872532-920fc231-ed38-4432-8a06-67110c816b90.png)

### 2.2 运行前准备
- 设置抢购时间

![image](https://user-images.githubusercontent.com/105795298/230873448-10490bc9-6073-40e6-a17c-1e49bee970e4.png)

- 设置需要抢购商品的xpath
> 先提前在电脑端浏览器登录淘宝并进入购物车，请确保你所需抢购的商品已加入购物车中

![image](https://user-images.githubusercontent.com/105795298/230874853-0c7b9bbd-a409-4b15-8fea-a9cac166735a.png)

> 接着按F12按键，点击一下如图中箭头所示按钮（点击后该按钮会变成蓝色）

![image](https://user-images.githubusercontent.com/105795298/230875728-f62f4221-043f-4e54-823e-03f3797e491a.png)

> 再点击一下需要勾选的勾选框，需要勾选哪个框就点哪个框，可以是店铺前面的勾选框，也可以是单个商品的勾选框

![image](https://user-images.githubusercontent.com/105795298/230877244-2203d2b7-4ef5-4879-bf9b-0794ead3a521.png)

> 回到按F12打开的调试页面，上一步操作完后，调试页面会选择到一个标签，右击该标签，复制到该标签的xpath

![image](https://user-images.githubusercontent.com/105795298/230878091-10dacb30-21c1-423b-ad1b-6260476f20a4.png)

> 粘贴到代码中，可重复上面操作粘贴多个，用单引号包裹，用逗号分隔

![image](https://user-images.githubusercontent.com/105795298/230879359-786b0d93-3552-4fe1-a4fe-1298465b80e8.png)

### 2.3 运行
- 建议在抢购时间前十分钟内，运行程序，等待程序自动打开淘宝扫码登录页面，请在两分钟内打开手机淘宝进行扫码登录
- 登录成功后，程序开始准备抢购，当抢购时间到达时，程序立即开始抢购
- 抢购成功后，订单会进行提交，**请及时在手机淘宝的待付款页面进行付款**
