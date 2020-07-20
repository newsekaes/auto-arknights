# -*- encoding=utf8 -*-
__author__ = "Doctor"

# ================刷图相关的配置在这里=================
# 是否使用理智补给：'none'不用，'potion'仅使用药剂，'rock'使用药剂+源石
USE_SUPPLY = 'rock'

# ===================================================


from airtest.core.api import *
# airtest.core.api中包含了一个名为ST的变量，即为全局设置
# 识别图片的阈值
ST.THRESHOLD = 0.95
# exists判断的超时时间
ST.FIND_TIMEOUT_TMP = 3

import random

auto_setup(__file__)

# arknights 关卡数据
series = [
    {
        'name': '主线',
        'template': Template(r"./img/series/main-line.png", record_pos=(-0.446, 0.193), resolution=(2340, 1080)),
        'chapters': [
            {
                'name': '1',
                'template': Template(r"./img/chapters/chapter1.png", record_pos=(0.059, -0.127), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '1-7',
                        'template': Template(r"./img/missions/1-7.png", record_pos=(0.07, -0.088), resolution=(2340, 1080))
                    }
                ]
            },
            {
                'name': '2',
                'template': Template(r"./img/chapters/chapter2.png", record_pos=(0.027, -0.131), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '2-5',
                        'template': Template(r"./img/missions/2-5.png", record_pos=(0.13, 0.043), resolution=(2340, 1080))
                    },
                    {
                        'name': '2-10',
                        'template': Template(r"./img/missions/2-10.png", record_pos=(0.3, 0.044), resolution=(2340, 1080))
                    },
                ],
            },
            {
                'name': '3',
                'template': Template(r"./img/chapters/chapter3.png", record_pos=(0.339, -0.131), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '3-1',
                        'template': Template(r"./img/missions/3-1.png", record_pos=(-0.182, -0.013), resolution=(2340, 1080))
                    },
                    {
                        'name': '3-2',
                        'template': Template(r"./img/missions/3-2.png", record_pos=(0.009, -0.016), resolution=(2340, 1080))
                    },
                    {
                        'name': '3-3',
                        'template': Template(r"./img/missions/3-3.png", record_pos=(-0.258, -0.02), resolution=(2340, 1080))
                    },
                    {
                        'name': '3-4',
                        'template': Template(r"./img/missions/3-4.png", record_pos=(0.073, 0.036), resolution=(2340, 1080))
                    },
                ]
            },
            {
                'name': '4',
                'template': Template(r"./img/chapters/chapter4.png", record_pos=(-0.308, -0.129), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '4-2',
                        'template': Template(r"./img/missions/4-2.png", record_pos=(0.044, 0.056), resolution=(2340, 1080))
                    },
                    {
                        'name': '4-4',
                        'template': Template(r"./img/missions/4-4.png", record_pos=(0.157, -0.012), resolution=(2340, 1080))

                    },
                    {
                        'name': '4-6',
                        'template': Template(r"./img/missions/4-6.png", record_pos=(0.158, -0.013), resolution=(2340, 1080))

                    },
                    {
                        'name': '4-7',
                        'template': Template(r"./img/missions/4-7.png", record_pos=(-0.154, -0.014), resolution=(2340, 1080))
                    },
                    {
                        'name': '4-8',
                        'template': Template(r"./img/missions/4-8.png", record_pos=(-0.018, -0.071), resolution=(2340, 1080))

                    },
                    {
                        'name': '4-9',
                        'template': Template(r"./img/missions/4-9.png", record_pos=(0.112, -0.013), resolution=(2340, 1080))
                    },
                    {
                        'name': 's4-1',
                        'template': Template(r"./img/missions/s4-1.png", record_pos=(-0.056, 0.057), resolution=(2340, 1080))
                    }
                ]
            },
            {
                'name': '5',
                'template': Template(r"./img/chapters/chapter5.png", record_pos=(-0.345, -0.129), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': 's5-7',
                        'template':Template(r"./img/missions/s5-7.png", record_pos=(0.215, 0.067), resolution=(2340, 1080))
                    },
                    {
                        'name': '5-10',
                        'template': Template(r"./img/missions/5-10.png", record_pos=(0.035, -0.011), resolution=(2340, 1080))
                    }
                ]
            },
            {
                'name': '6',
                'template': Template(r"./img/chapters/chapter6.png", record_pos=(-0.031, -0.129), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '6-16',
                        'template':Template(r"./img/missions/6-16.png", record_pos=(0.116, -0.025), resolution=(2340, 1080))
                    }
                ]
            },
            {
                'name': '7',
                'template': Template(r"./img/chapters/chapter7.png", record_pos=(0.288, -0.129), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '7-6',
                        'template': Template(r"./img/missions/7-6.png", record_pos=(-0.049, 0.009), resolution=(2340, 1080))
                    },
                    {
                        'name': '7-10',
                        'template':Template(r"./img/missions/7-10.png", record_pos=(-0.021, -0.066), resolution=(2340, 1080))
                    },
                    {
                        'name': '7-12',
                        'template': Template(r"./img/missions/7-12.png", record_pos=(0.26, 0.07), resolution=(2340, 1080))
                    },
                    {
                        'name': '7-15',
                        'template': Template(r"./img/missions/7-15.png", record_pos=(-0.046, 0.0), resolution=(2340, 1080))
                    },
                    {
                        'name': '7-16',
                        'template':Template(r"./img/missions/7-16.png", record_pos=(0.097, -0.072), resolution=(2340, 1080))
                    }
                ]
            },
        ]
    },
    {
        'name':
        '物资筹备','template': Template(r"./img/series/wuzichoubei.png", record_pos=(-0.347, 0.194), resolution=(2340, 1080)),
        'chapters': [
            {
                    'name': 'ls',
                'template': Template(r"./img/chapters/ls.png", record_pos=(-0.341, 0.09), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': 'ls-5',
                        'template': Template(r"./img/missions/ls-5.png", record_pos=(0.205, -0.118), resolution=(2340, 1080))
                    }
                ]
            },
            {
                'name': 'ap',
                'template': Template(r"./img/chapters/ap.png", record_pos=(-0.173, 0.094), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': 'ap-5',
                        'template': Template(r"./img/missions/ap-5.png", record_pos=(0.206, -0.117), resolution=(2340, 1080))
                    }
                ]
            }
        ]
    },
    {
        'name': '芯片搜索',
        'template': Template(r"./img/series/xinpiansousuo.png", record_pos=(-0.251, 0.193), resolution=(2340, 1080))
    }
]

# 坐标模糊化
def rangeTarget (targetAxios):
    d = random.randint(-10, 10)
    return [targetAxios[0] + d, targetAxios[1] + d]

# 模糊化点击图片
def rangeTouchImg(template):
    touch(rangeTarget(exists(template)))

# 进入到某个关卡系列
# params: '主线', '物资筹备', '芯片搜索'
def goToSeries(target):
    sleep(1.0)
    if exists(Template(r"./img/nav/home-fight.png", record_pos=(0.271, -0.132), resolution=(2340, 1080))):
        rangeTouchImg(Template(r"./img/nav/home-fight.png", record_pos=(0.271, -0.132), resolution=(2340, 1080)))
    else:
        rangeTouchImg(Template(r"./img/nav/top-home.png", record_pos=(-0.326, -0.205), resolution=(2340, 1080)))
        sleep(1.0)
        rangeTouchImg(Template(r"./img/nav/top-fight.png", record_pos=(-0.071, -0.173), resolution=(2340, 1080)))
    sleep(1.0)
    rangeTouchImg(target)
    sleep(2.0)

# 从左到右滑动，寻找相关选项
def swipeToArea(target, size):
    step = -0.25 if (size is 'small') else -0.5
    swipe(v1=[300, 300], vector=[1, 0], duration=0.2)
    swipe(v1=[300, 300], vector=[1, 0], duration=0.2)
    sleep(2)
    while (not exists(target)):
        swipe(v1=[1800, 300], vector=[step, 0], duration=0.5)
        sleep(1.0)
    rangeTouchImg(target)
    sleep(2.0)

# 刷关卡
def fight(times=1):
    num = 0
    while(times > 0):
        num += 0
        times -= 1
        rangeTouchImg(Template(r"./img/missionIcon/action-start.png", record_pos=(0.45, 0.189), resolution=(2340, 1080)))
        sleep(2)
        supplyTmp = Template(r"./img/missionIcon/use-supply.png", record_pos=(0.287, 0.139), resolution=(2340, 1080))
        if (exists(supplyTmp)):
            if (USE_SUPPLY is 'none'):
                break
            elif (USE_SUPPLY is 'potion'):
                if (exists(Template(r"./img/missionIcon/use-rock.png", record_pos=(0.126, -0.025), resolution=(2340, 1080)))):
                    break
                else: rangeTouchImg(supplyTmp)
            else:
                rangeTouchImg(supplyTmp)
            sleep(1)
            rangeTouchImg(Template(r"./img/missionIcon/action-start.png", record_pos=(0.45, 0.189), resolution=(2340, 1080)))
            sleep(2)
        rangeTouchImg(Template(r"./img/missionIcon/action-start-im.png", record_pos=(0.294, 0.092), resolution=(2340, 1080)))
        sleep(1)
        wait(Template(r"./img/missionIcon/mission-complete.png", record_pos=(-0.352, 0.178), resolution=(2340, 1080)), timeout=2000, interval=5)
        touch(rangeTarget([200, 200]))
        print(str.join(['已刷:', str(num), '次；剩余：'， str(times), '次']))
        sleep(3)

# 完整的一个关卡流程
def run(seryName='主线', chapterName='1', missionName='1-7', times=1):
    for s in series:
        if (s['name'] is seryName):
            seryTarget = s['template']
            for c in s['chapters']:
                if (c['name'] is chapterName):
                    chapterTarget = c['template']
                    for m in c['missions']:
                        if (m['name'] is missionName):
                            missionTarget = m['template']
                            break
                    break
            break
    print(seryTarget, chapterTarget, missionTarget)
    goToSeries(seryTarget)
    swipeToArea(chapterTarget, 'big')
    swipeToArea(missionTarget, 'small')
    print('------------------'+ seryName + ': ' + missionName +'--------------------')
    fight(times)

# ======刷图配置=======
# 例如
# run('主线', '7', '7-6', 8)
# run('主线', '1', '1-7', 20)
# run('主线', '5', '5-10', 10)

# ===================






