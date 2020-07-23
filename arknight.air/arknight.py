# -*- encoding=utf8 -*-
__author__ = "Doctor"

import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

from airtest.core.api import *
# 识别图片的阈值
ST.THRESHOLD = 0.95
# exists判断的超时时间
ST.FIND_TIMEOUT_TMP = 3

import random
import time
w,h=device().get_current_resolution() #获取手机分辨率
auto_setup(__file__)

# ================刷图相关的配置在这里=================
# 是否使用理智补给：'none'不用，'potion'仅使用药剂，'rock'使用药剂+源石
USE_SUPPLY = 'rock'

# 关卡最少耗时，默认60，即至少60秒后才开启 关卡完成 检测
MIN_MISSION_TIME = 60

# 开启升级检测功能，True开启，False关闭。关闭此检测后，关卡结束会更快，满级大佬必备
LEVEL_UP_CHECK = False

# 开启代理失败检测，True开启，False关闭。如果对自己的代理有信心，关闭即可
PROXY_ERROR_CHECK = False

# 开启凌晨4点跨夜模式，True开启，False关闭。此功能尚未完全测试完成，不建议使用（不建议熬夜玩游戏伤身体）
ACROSS_NIGHT = False
# ===================================================

_gameStart = Template(r"./img/signIn/game-start.png", record_pos=(0.0, 0.205), resolution=(2340, 1080))
_gameLog = Template(r"./img/signIn/game-log.png", record_pos=(0.338, -0.168), resolution=(2340, 1080))
_gameLogClose = Template(r"./img/signIn/game-log-close.png", record_pos=(0.38, -0.194), resolution=(2340, 1080))
_gameMonthLogin = Template(r"./img/signIn/game-month-login.png", record_pos=(0.001, -0.161), resolution=(2340, 1080))
_gameMonthLoginClose = Template(r"./img/signIn/game-month-login-close.png", record_pos=(0.0, 0.181), resolution=(2340, 1080))
_gameDayLogin = Template(r"./img/signIn/game-day-login.png", record_pos=(0.239, 0.158), resolution=(2340, 1080))
_gameDayLoginClose = Template(r"./img/signIn/game-day-login-close.png", record_pos=(0.36, -0.182), resolution=(2340, 1080))

currentSery = ''
currentChapter = ''
currentMission = ''

# arknights 关卡数据
series = [
    {
        'name': '主线',
        'template': Template(r"./img/series/main-line.png", record_pos=(-0.446, 0.193), resolution=(2340, 1080)),
        'chapters': [
            {
                'name': '1',
                'template': Template(r"./img/chapters/chapter1.png", record_pos=(-0.257, 0.007), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '1-7',
                        'template': Template(r"./img/missions/1-7.png", record_pos=(0.07, -0.088), resolution=(2340, 1080))
                    }
                ]
            },
            {
                'name': '2',
                'template': Template(r"./img/chapters/chapter2.png", record_pos=(0.287, 0.029), resolution=(2340, 1080)),
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
                'template': Template(r"./img/chapters/chapter3.png", record_pos=(0.044, 0.003), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '3-1',
                        'template': Template(r"./img/missions/3-1.png", record_pos=(-0.081, -0.009), resolution=(2340, 1080))
                    },
                    {
                        'name': '3-2',
                        'template': Template(r"./img/missions/3-2.png", record_pos=(-0.379, -0.015), resolution=(2340, 1080))
                    },
                    {
                        'name': '3-3',
                        'template': Template(r"./img/missions/3-3.png", record_pos=(-0.2, -0.018), resolution=(2340, 1080))
                    },
                    {
                        'name': '3-4',
                        'template': Template(r"./img/missions/3-4.png", record_pos=(0.036, 0.038), resolution=(2340, 1080))
                    },
                ]
            },
            {
                'name': '4',
                'template': Template(r"./img/chapters/chapter4.png", record_pos=(-0.314, 0.031), resolution=(2340, 1080)),
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
                'template': Template(r"./img/chapters/chapter5.png", record_pos=(-0.002, 0.018), resolution=(2340, 1080)),
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
                'template': Template(r"./img/chapters/chapter6.png", record_pos=(-0.027, 0.017), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '6-16',
                        'template':Template(r"./img/missions/6-16.png", record_pos=(0.116, -0.025), resolution=(2340, 1080))
                    }
                ]
            },
            {
                'name': '7',
                'template': Template(r"./img/chapters/chapter7.png", record_pos=(0.295, 0.008), resolution=(2340, 1080)),
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
            },
            {
                'name': 'ca',
                'template': Template(r"./img/chapters/ca.png", record_pos=(-0.174, 0.075), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': 'ca-5',
                        'template': Template(r"./img/missions/ca-5.png", record_pos=(0.203, -0.117), resolution=(2340, 1080))
                    }
                ]
            },
            {
                'name': 'ce',
                'template': Template(r"./img/chapters/ce.png", record_pos=(-0.004, 0.068), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': 'ce-5',
                        'template': Template(r"./img/missions/ce-5.png", record_pos=(0.201, -0.118), resolution=(2340, 1080))
                    }
                ]
            }
        ]
    },
    {
        'name': '芯片搜索',
        'template': Template(r"./img/series/xinpiansousuo.png", record_pos=(-0.251, 0.193), resolution=(2340, 1080)),
        'chapters': [
            {
                'name': 'pr-b',
                'template': Template(r"./img/chapters/pr-b.png", record_pos=(-0.258, 0.074), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': 'pr-b-1',
                        'template': Template(r"./img/missions/pr-b-1.png", record_pos=(-0.157, 0.052), resolution=(2340, 1080))
                    },
                    {
                        'name': 'pr-b-2',
                        'template': Template(r"./img/missions/pr-b-2.png", record_pos=(0.134, -0.074), resolution=(2340, 1080))
                    }
                ]
            },
            {
                'name': 'pr-d',
                'template': Template(r"./img/chapters/pr-d.png", record_pos=(-0.087, 0.074), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': 'pr-d-1',
                        'template': Template(r"./img/missions/pr-d-1.png", record_pos=(-0.147, 0.048), resolution=(2340, 1080))
                    },
                    {
                        'name': 'pr-d-2',
                        'template': Template(r"./img/missions/pr-d-2.png", record_pos=(0.124, -0.063), resolution=(2340, 1080))
                    },
                ]
            }
        ]
    }
]

# 时间模糊化
def rt(time):
    return time + random.randint(0,1)

# 坐标模糊化
def rangeTarget (targetAxios, range=5):
    d=random.randint(-range, range)
    return [targetAxios[0] + d, targetAxios[1] + d]

# 模糊化点击图片
def rangeTouchImg(template):
    touch(rangeTarget(exists(template)))

# 设置全局
def setCurrent(s, c, m):
    currentSery = s
    currentChapter = c
    currentMission = m

# 跳过每日登陆和月卡签到
def skipSignIn():
    sleep(2)
    hasDoSignIn = False
    if (exists(_gameLog)):
        hasDoSignIn = True
        sleep(1)
        rangeTouchImg(_gameLogClose)
        sleep(2)
    if (exists(_gameMonthLogin)):
        hasDoSignIn = True
        sleep(1)
        rangeTouchImg(_gameMonthLoginClose)
        sleep(2)
    if (exists(_gameDayLogin)):
        hasDoSignIn = True
        sleep(1)
        rangeTouchImg(_gameDayLoginClose)
        sleep(2)
    return hasDoSignIn

# 进入到某个关卡系列
# params: '主线', '物资筹备', '芯片搜索'
def goToSeries(target):
    # 先尝试寻找目标
    if (exists(target)):
        rangeTouchImg(target)
        sleep(rt(2))
        return True
    sleep(rt(1))
    if exists(Template(r"./img/nav/home-fight.png", record_pos=(0.271, -0.132), resolution=(2340, 1080))):
        rangeTouchImg(Template(r"./img/nav/home-fight.png", record_pos=(0.271, -0.132), resolution=(2340, 1080)))
    else:
        rangeTouchImg(Template(r"./img/nav/top-home.png", record_pos=(-0.326, -0.205), resolution=(2340, 1080)))
        sleep(rt(1))
        rangeTouchImg(Template(r"./img/nav/top-fight.png", record_pos=(-0.071, -0.173), resolution=(2340, 1080)))
    sleep(rt(1))
    if (exists(target)):
        rangeTouchImg(target)
        sleep(rt(2))
        return True
    else:
        return False

# 从左到右滑动，寻找相关选项
def swipeToArea(target, size):
    # 先直接尝试寻找目标
    if (exists(target)):
        rangeTouchImg(target)
        sleep(rt(2))
        return True
    # 如果没有寻找到，则再从左到右寻找
    # 最大重试次数
    maxTimes = 15
    vStartLeft = [0.128*w, 0.278*w]
    vStartRight = [0.769*w, 0.278*w]
    step = -0.25 if (size == 'small') else -0.5
    swipe(v1=vStartLeft, vector=[1, 0], duration=0.2)
    swipe(v1=vStartLeft, vector=[1, 0], duration=0.2)
    sleep(rt(2))
    while ((not exists(target)) and maxTimes > 0):
        maxTimes -= 1
        swipe(vStartRight, vector=[step, 0], duration=0.5)
        touch(v=vStartRight, duration=1)
    if (maxTimes <= 0):
        return False
    else:
        rangeTouchImg(target)
        sleep(rt(2))
        return True

# 刷关卡
def fight(times=1, missionTarget=False):
    _proxy = Template(r"./img/missionIcon/proxy.png", record_pos=(0.409, 0.149), resolution=(2340, 1080))
    _actionStart = Template(r"./img/missionIcon/action-start.png", record_pos=(0.45, 0.189), resolution=(2340, 1080))
    _actionStartIm = Template(r"./img/missionIcon/action-start-im.png", record_pos=(0.294, 0.092), resolution=(2340, 1080))
    _supply = Template(r"./img/missionIcon/use-supply.png", record_pos=(0.287, 0.139), resolution=(2340, 1080))
    _useRock = Template(r"./img/missionIcon/use-rock.png", record_pos=(0.126, -0.025), resolution=(2340, 1080))
    _cancelUse = Template(r"./img/missionIcon/cancel-use.png", record_pos=(0.089, 0.139), resolution=(2340, 1080))
    _levelUp = Template(r"./img/missionIcon/level-up.png", record_pos=(-0.198, 0.010), resolution=(2340, 1080))
    _missionComplete = Template(r"./img/missionIcon/mission-complete.png", record_pos=(-0.352, 0.178), resolution=(2340, 1080))
    _actionFailed = Template(r"./img/missionIcon/action-failed.png", record_pos=(0.22, -0.026), resolution=(2340, 1080))
    _proxyFailed = Template(r"./img/missionIcon/proxy-failed.png", record_pos=(-0.216, -0.048), resolution=(2340, 1080))
    _giveUp = Template(r"./img/missionIcon/give-up.png", record_pos=(-0.149, 0.114), resolution=(2340, 1080))
    # 本关卡的默认时间为全局配置的时间；重复通关同一关卡后，该时间会被不断优化修正
    minMissionTime = MIN_MISSION_TIME
    num = 0
    # 如果没有选择代理指挥，则勾选代理指挥
    if (exists(_proxy)):
        touch(_proxy)

    while(times > 0):
        num += 1
        times -= 1
        # 判断关卡有没有被选择
        if (missionTarget and exists(missionTarget)):
            rangeTouchImg(missionTarget)
            sleep(rt(1))
        rangeTouchImg(_actionStart)
        sleep(rt(2))
        # 如果体力不足了
        if (exists(_supply)):
            # 不需要补充体力
            if (USE_SUPPLY == 'none'):
                rangeTouchImg(_cancelUse)
                break
            # 只喝体力药
            elif (USE_SUPPLY == 'potion'):
                if (exists(_useRock)):
                    rangeTouchImg(_cancelUse)
                    break
                else: rangeTouchImg(_supply)
            # 不仅喝体力药，还要碎石
            else:
                rangeTouchImg(_supply)
            sleep(rt(1))
            rangeTouchImg(_actionStart)
            sleep(rt(2))
        rangeTouchImg(_actionStartIm)
        # 记录关卡开始的时间戳
        timeStart = int(time.time())
        # 最快的关卡2倍速也不会低于 MIN_MISSION_TIME
        sleep(rt(minMissionTime))
        while True:
            # 如果任务完成了
            if (exists(_missionComplete)):
                sleep(rt(3))
                touch(rangeTarget([230, 230], 30))
                sleep(rt(3))
                print(''.join(['已刷:', str(num), "次; 剩余：", str(times), '次']))
                # 记录关卡结束后的时间戳，并重新计算关卡时间
                minMissionTime = (int(time.time()) - timeStart) - 10
                break
            # 如果代理失误了
            elif (PROXY_ERROR_CHECK and exists(_proxyFailed)):
                touch(_giveUp)
                touch(wait(_actionFailed))
                break
            # 如果升级了
            elif (LEVEL_UP_CHECK and exists(_levelUp)):
                # 等待升级动画结束
                sleep(rt(3))
                rangeTouchImg(_levelUp)
                # 等待2s后继续循环，进入elif
                sleep(2)
            # 如果任务未完成，等待5s, 继续循环
            else:
                sleep(5)
        sleep(rt(3))
        # 如果刚好进入了每日登陆
        if (ACROSS_NIGHT and skipSignIn()):
            if ((currentSery == '') and (currentChapter == '') and (currentMission == '')):
                run(currentSery, currentChapter, currentMission, times)
            break

# 完整的一个关卡流程
def run(seryName='主线', chapterName='1', missionName='1-7', times=1):
    seryTarget = False
    chapterTarget = False
    missionTarget = False
    for s in series:
        if (s['name'] == seryName):
            seryTarget = s['template']
            for c in s['chapters']:
                if (c['name'] == chapterName):
                    chapterTarget = c['template']
                    for m in c['missions']:
                        if (m['name'] == missionName):
                            missionTarget = m['template']
                            break
                    break
            break
    if (not (seryTarget and chapterTarget and missionTarget)):
        print ('未找到以下关卡信息：' + seryName + '_' + chapterName + '_' + missionName)
        return False
    if (goToSeries(seryTarget)):
        if (swipeToArea(chapterTarget, 'big')):
            if (swipeToArea(missionTarget, 'small')):
                setCurrent(seryName, chapterName, missionName)
                print('------------------'+ seryName + ': ' + missionName +'--------------------')
                fight(times, missionTarget)
                setCurrent('', '', '')
            else:
                print('关卡不存在或未开放：' + seryName)
        else:
            print('章节不存在或未开放：' + seryName)
    else:
        print('系列不存在或未开放：' + seryName)

# ======刷图流程=======
# 例如
# run('主线', '7', '7-16', 18)
# run('物资筹备', 'ce', 'ce-5', 99)
# run('芯片搜索', 'pr-b', 'pr-b-2', 10)

# ===================
