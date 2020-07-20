# 明日方舟AirTest自助刷图器

###  5秒钟看懂这是个啥：  
#### 1. 在第三方网站上获得的刷图规划计划  
![在第三方网站上获得的刷图规划计划](blog/penguin.png)
#### 2. 在刷图器中书写规划代码
```
run('主线'， '3'， '3-4'， 4)
run('主线'， '5'， '5-10'， 7)
run('主线'， '2'， '2-5'， 10)
```
---
## 1. 使用方法
### 1. PC安装 `Airtest IDE`
访问[`Airtest IDE`官网](http://airtest.netease.com/)，安装相应版本

### 2. 连接设备或模拟器
1. [Android真机连接](https://airtest.doc.io.netease.com/IDEdocs/device_connection/1_android_phone_connection/)  
> [Android连接常见问题](https://airtest.doc.io.netease.com/IDEdocs/device_connection/2_android_faq/)
2. [Android模拟器连接](https://airtest.doc.io.netease.com/IDEdocs/device_connection/3_emulator_connection/)
3. [IOS设备连接](https://airtest.doc.io.netease.com/IDEdocs/device_connection/4_ios_connection/)

### 3. 使用Airtest IDE运行脚本
[下载脚本地址](https://github.com/newsekaes/auto-arknights/releases/)  

1. 下载`.zip`文件
2. 解压缩
3. 使用`Airtest IDE` -> 【文件】-> 【打开脚本】-> 选择打开`arknight.air`文件夹
4. 连接设备或模拟器
5. 在脚本下方输入你想按顺序刷图的代码（参见示例）
6. 点击【运行】-> 【运行脚本】

### 2. 目前支持的关卡及其代码名称
```
主线：
    1：
        1-7
    2：
        2-5
        2-10
    3：
        3-1
        3-2
        3-3
        3-4
    4：
        4-2
        4-4
        4-6
        4-7
        4-8
        4-9
        s4-1
    5：
        s5-7
        5-10
    6：
        6-16
    7：
        7-16
        7-10
        7-12
        7-15
        7-16
物资筹备：
    ls:
        ls-5
    ap:
        ap-5
```
### 3. 如果想刷的关不在上述列表，且只是想对某一关刷到天荒地老
直接在`刷图配置`里保留唯一一行代码
```
# ======刷图配置=======
fight(999)
# ===================
```
当然`999`表示次数，你可以自定义自己想刷多少次

### 4. 不想自动碎石嗑体力怎么办
在脚本上方有这么一部分
```
# ================刷图相关的配置在这里=================
# 是否使用理智补给：'none'不用，'potion'仅使用药剂，'rock'使用药剂+源石
USE_SUPPLY = 'rock'

# ===================================================

```
如果不想嗑药不想碎石，就改成 `'none'`; 如果只想使用药剂，改为`'potion'`
