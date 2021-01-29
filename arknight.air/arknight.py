# -*- encoding=utf8 -*-
__author__ = "Doctor"

import logging
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

from airtest.core.api import *
# 识别图片的阈值
ST.THRESHOLD = 0.92
ST.THRESHOLD_STRICT = 0.92
# exists判断的超时时间
ST.FIND_TIMEOUT_TMP = 1

import random
import time

w,h=device().get_current_resolution() #获取手机分辨率
print(w, h)
auto_setup(__file__)

# ================刷图相关的配置在这里=================
# 是否使用理智补给：'none'不用，'potion'仅使用药剂，'rock'使用药剂+源石
USE_SUPPLY = 'rock'

# 如果设置了可用源石，那么单次运行，允许使用的最大源石数； 如果设为-1，则无限碎石头
max_rock_num = -1

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
_barLeft = Template(r"./img/nav/bar-left.png", record_pos=(-0.469, -0.206), resolution=(2340, 1080))


_proxy = Template(r"./img/missionIcon/proxy.png", record_pos=(0.409, 0.149), resolution=(2340, 1080))
_actionStart = Template(r"./img/missionIcon/action-start.png", record_pos=(0.45, 0.189), resolution=(2340, 1080))
_actionStart2 = Template(r"./img/missionIcon/action-start2.png", record_pos=(0.45, 0.191), resolution=(2340, 1080))
_actionStartIm = Template(r"./img/missionIcon/action-start-im.png", record_pos=(0.294, 0.092), resolution=(2340, 1080))
_supply = Template(r"./img/missionIcon/use-supply.png", record_pos=(0.287, 0.139), resolution=(2340, 1080))
_noTicket = Template(r"./img/missionIcon/no-ticket.png", record_pos=(0.387, -0.162), resolution=(2340, 1080))
_useRock = Template(r"./img/missionIcon/use-rock.png", record_pos=(0.126, -0.025), resolution=(2340, 1080))
_cancelUse = Template(r"./img/missionIcon/cancel-use.png", record_pos=(0.089, 0.139), resolution=(2340, 1080))
_levelUp = Template(r"./img/missionIcon/level-up.png", record_pos=(-0.198, 0.010), resolution=(2340, 1080), rgb=True, threshold=0.8)
_missionComplete = Template(r"./img/missionIcon/mission-complete.png", record_pos=(-0.32, 0.139), resolution=(2340, 1080))
_actionFailed = Template(r"./img/missionIcon/action-failed.png", record_pos=(0.22, -0.026), resolution=(2340, 1080), rgb=True, threshold=0.8)
_proxyFailed = Template(r"./img/missionIcon/proxy-failed.png", record_pos=(0.17, 0.095), resolution=(2244, 1080), rgb=True, threshold=0.8)
_giveUp = Template(r"./img/missionIcon/give-up.png", record_pos=(-0.149, 0.114), resolution=(2340, 1080), rgb=True, threshold=0.8)
currentSery = ''
currentChapter = ''
currentMission = ''
currentSeryTarget = ''
currentChapterTarget = ''
currentMissionTarget = ''
currentMissionOrder = 0
currentDeps = 0

__test__mode = False
__random__time = 1

#使用的理智药水
rationalPotion = 0
#使用的理智源石
rationalRock = 0

# arknights 关卡数据
series = [
    {
        'name': '主线',
        'template': Template(r"./img/series/main-line.png", record_pos=(-0.446, 0.193), resolution=(2340, 1080)),
        'chapters': [
            {
                'name': '1',
                'template': Template(r"./img/chapters/chapter1.png", record_pos=(-0.257, 0.007), resolution=(2340, 1080), ),
                'missions': [
                    {
                        'name': '1-7',
                        'template': Template(r"./img/missions/1-7.png", record_pos=(0.07, -0.088), resolution=(2340, 1080), rgb=True)
                    }
                ]
            },
            {
                'name': '2',
                'template': Template(r"./img/chapters/chapter2.png", record_pos=(0.287, 0.029), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '2-3',
                        'template': Template(r"./img/missions/2-3.png", record_pos=(0.078, 0.047), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's2-5',
                        'template': Template(r"./img/missions/s2-5.png", record_pos=(-0.193, -0.014), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's2-6',
                        'template': Template(r"./img/missions/s2-6.png", record_pos=(-0.311, 0.048), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's2-7',
                        'template': Template(r"./img/missions/s2-7.png", record_pos=(-0.116, 0.049), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '2-5',
                        'template': Template(r"./img/missions/2-5.png", record_pos=(0.13, 0.043), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '2-6',
                        'template': Template(r"./img/missions/2-6.png", record_pos=(0.221, 0.047), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's2-8',
                        'template': Template(r"./img/missions/s2-8.png", record_pos=(-0.094, 0.048), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's2-9',
                        'template': Template(r"./img/missions/s2-9.png", record_pos=(-0.052, 0.048), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '2-10',
                        'template': Template(r"./img/missions/2-10.png", record_pos=(0.3, 0.044), resolution=(2340, 1080), rgb=True)
                    },
                ],
            },
            {
                'name': '3',
                'template': Template(r"./img/chapters/chapter3.png", record_pos=(0.044, 0.003), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '3-1',
                        'template': Template(r"./img/missions/3-1.png", record_pos=(-0.081, -0.009), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '3-2',
                        'template': Template(r"./img/missions/3-2.png", record_pos=(-0.379, -0.015), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '3-3',
                        'template': Template(r"./img/missions/3-3.png", record_pos=(-0.2, -0.018), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's3-1',
                        'template': Template(r"./img/missions/s3-1.png", record_pos=(-0.034, 0.116), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's3-2',
                        'template': Template(r"./img/missions/s3-2.png", record_pos=(-0.203, 0.116), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '3-4',
                        'template': Template(r"./img/missions/3-4.png", record_pos=(0.036, 0.038), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '3-7',
                        'template': Template(r"./img/missions/3-7.png", record_pos=(-0.124, -0.028), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's3-3',
                        'template': Template(r"./img/missions/s3-3.png", record_pos=(0.169, 0.041), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's3-4',
                        'template': Template(r"./img/missions/s3-4.png", record_pos=(0.347, 0.04), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's3-6',
                        'template': Template(r"./img/missions/s3-6.png", record_pos=(0.018, 0.041), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's3-7',
                        'template': Template(r"./img/missions/s3-7.png", record_pos=(0.266, 0.036), resolution=(2400, 1080), rgb=True)
                    },
                ]
            },
            {
                'name': '4',
                'template': Template(r"./img/chapters/chapter4.png", record_pos=(-0.314, 0.031), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '4-2',
                        'template': Template(r"./img/missions/4-2.png", record_pos=(-0.131, 0.059), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's4-1',
                        'template': Template(r"./img/missions/s4-1.png", record_pos=(0.122, 0.059), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '4-4',
                        'template': Template(r"./img/missions/4-4.png", record_pos=(-0.347, -0.01), resolution=(2340, 1080), rgb=True)

                    },
                    {
                        'name': '4-5',
                        'template': Template(r"./img/missions/4-5.png", record_pos=(-0.206, -0.068), resolution=(2340, 1080), rgb=True)

                    },
                    {
                        'name': '4-6',
                        'template': Template(r"./img/missions/4-6.png", record_pos=(-0.282, -0.01), resolution=(2340, 1080), rgb=True)

                    },
                    {
                        'name': '4-7',
                        'template': Template(r"./img/missions/4-7.png", record_pos=(-0.304, -0.01), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '4-8',
                        'template': Template(r"./img/missions/4-8.png", record_pos=(-0.166, -0.068), resolution=(2340, 1080), rgb=True)

                    },
                    {
                        'name': '4-9',
                        'template': Template(r"./img/missions/4-9.png", record_pos=(-0.036, -0.009), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's4-10',
                        'template': Template(r"./img/missions/s4-10.png", record_pos=(-0.099, -0.071), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '4-10',
                        'template': Template(r"./img/missions/4-10.png", record_pos=(0.248, -0.011), resolution=(2340, 1080), rgb=True)
                    },
                ]
            },
            {
                'name': '5',
                'template': Template(r"./img/chapters/chapter5.png", record_pos=(-0.002, 0.018), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '5-1',
                        'template':Template(r"./img/missions/5-1.png", record_pos=(0.021, 0.029), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '5-3',
                        'template':Template(r"./img/missions/5-3.png", record_pos=(0.141, -0.024), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '5-5',
                        'template':Template(r"./img/missions/5-5.png", record_pos=(-0.143, -0.024), resolution=(2244, 1080), rgb=True)
                    },
                    {
                        'name': '5-6',
                        'template':Template(r"./img/missions/5-6.png", record_pos=(-0.127, -0.08), resolution=(1920, 1080), rgb=True)
                    },
                    {
                        'name': '5-7',
                        'template':Template(r"./img/missions/5-7.png", record_pos=(-0.056, -0.066), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '5-8',
                        'template':Template(r"./img/missions/5-8.png", record_pos=(0.159, -0.001), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's5-7',
                        'template':Template(r"./img/missions/s5-7.png", record_pos=(0.215, 0.067), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's5-8',
                        'template':Template(r"./img/missions/s5-8.png", record_pos=(-0.109, 0.071), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '5-10',
                        'template': Template(r"./img/missions/5-10.png", record_pos=(0.035, -0.011), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 's5-9',
                        'template': Template(r"./img/missions/s5-9.png", record_pos=(0.069, 0.068), resolution=(2400, 1080), rgb=True)
                    },
                ]
            },
            {
                'name': '6',
                'template': Template(r"./img/chapters/chapter6.png", record_pos=(-0.027, 0.017), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '6-2',
                        'template': Template(r"./img/missions/6-2.png", record_pos=(0.07, -0.056), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '6-4',
                        'template': Template(r"./img/missions/6-4.png", record_pos=(-0.003, 0.051), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '6-5',
                        'template': Template(r"./img/missions/6-5.png", record_pos=(-0.075, -0.005), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '6-11',
                        'template': Template(r"./img/missions/6-11.png", record_pos=(-0.074, 0.039), resolution=(2340, 1080)),
                    },
                    {
                        'name': '6-12',
                        'template': Template(r"./img/missions/6-12.png", record_pos=(0.028, -0.015), resolution=(2340, 1080)),
                    },
                    {
                        'name': '6-16',
                        'template':Template(r"./img/missions/6-16.png", record_pos=(0.116, -0.025), resolution=(2340, 1080), rgb=True)
                    }
                ]
            },
            {
                'name': '7',
                'template': Template(r"./img/chapters/chapter7.png", record_pos=(0.295, 0.008), resolution=(2340, 1080)),
                'missions': [
                    {
                        'name': '7-4',
                        'template': Template(r"./img/missions/7-4.png", record_pos=(-0.126, 0.064), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '7-5',
                        'template': Template(r"./img/missions/7-5.png", record_pos=(0.059, 0.062), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '7-6',
                        'template': Template(r"./img/missions/7-6.png", record_pos=(-0.049, 0.009), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '7-8',
                        'template': Template(r"./img/missions/7-8.png", record_pos=(0.11, 0.012), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '7-10',
                        'template':Template(r"./img/missions/7-10.png", record_pos=(-0.021, -0.066), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '7-12',
                        'template': Template(r"./img/missions/7-12.png", record_pos=(0.26, 0.07), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '7-15',
                        'template': Template(r"./img/missions/7-15.png", record_pos=(-0.046, 0.0), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '7-16',
                        'template':Template(r"./img/missions/7-16.png", record_pos=(0.097, -0.072), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '7-17',
                        'template':Template(r"./img/missions/7-17.png", record_pos=(0.058, -0.012), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': '7-18',
                        'template':Template(r"./img/missions/7-18.png", record_pos=(-0.244, -0.01), resolution=(2340, 1080), rgb=True)
                    },
                ]
            },
            {
                'name': '8',
                'template': Template(r"./img/chapters/chapter8.png", record_pos=(0.296, 0.01), resolution=(2400, 1080)),
                'missions': [
                    {
                        'name': 'r8-1',
                        'template': Template(r"./img/missions/r8-1.png", record_pos=(-0.114, -0.075), resolution=(2400, 1080))
                    },
                    {
                        'name': 'r8-2',
                        'template': Template(r"./img/missions/r8-2.png", record_pos=(0.086, -0.076), resolution=(2400, 1080))
                    },
                    {
                        'name': 'r8-3',
                        'template': Template(r"./img/missions/r8-3.png", record_pos=(-0.452, -0.076), resolution=(2400, 1080))
                    },
                    {
                        'name': 'r8-4',
                        'template': Template(r"./img/missions/r8-4.png", record_pos=(-0.288, -0.076), resolution=(2400, 1080))
                    },
                    {
                        'name': 'r8-5',
                        'template': Template(r"./img/missions/r8-5.png", record_pos=(-0.129, -0.077), resolution=(2400, 1080))
                    },
                    {
                        'name': 'r8-6',
                        'template': Template(r"./img/missions/r8-6.png", record_pos=(0.034, -0.077), resolution=(2400, 1080))
                    },
                    {
                        'name': 'r8-7',
                        'template': Template(r"./img/missions/r8-7.png", record_pos=(0.109, -0.125), resolution=(2400, 1080))
                    },
                    {
                        'name': 'r8-8',
                        'template': Template(r"./img/missions/r8-8.png", record_pos=(-0.311, -0.077), resolution=(2400, 1080))
                    },
                    {
                        'name': 'm8-6',
                        'template': Template(r"./img/missions/m8-6.png", record_pos=(-0.317, 0.066), resolution=(2400, 1080))
                    },
                    {
                        'name': 'r8-9',
                        'template': Template(r"./img/missions/r8-9.png", record_pos=(-0.106, -0.076), resolution=(2400, 1080))
                    },
                    {
                        'name': 'm8-7',
                        'template': Template(r"./img/missions/m8-7.png", record_pos=(-0.11, 0.066), resolution=(2400, 1080))
                    },
                    {
                        'name': 'r8-10',
                        'template': Template(r"./img/missions/r8-10.png", record_pos=(0.025, -0.075), resolution=(2400, 1080))
                    },
                    {
                        'name': 'r8-11',
                        'template': Template(r"./img/missions/r8-11.png", record_pos=(0.158, -0.077), resolution=(2400, 1080))
                    },
                    {
                        'name': 'm8-8',
                        'template': Template(r"./img/missions/m8-8.png", record_pos=(0.157, 0.066), resolution=(2400, 1080))
                    },
                    {
                        'name': 'jt8-2',
                        'template': Template(r"./img/missions/jt8-2.png", record_pos=(0.092, -0.004), resolution=(2400, 1080))
                    },
                    {
                        'name': 'jt8-3',
                        'template': Template(r"./img/missions/jt8-3.png", record_pos=(-0.001, -0.005), resolution=(2400, 1080))
                    },
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
                'template': Template(r"./img/chapters/ls.png", record_pos=(-0.357, -0.059), resolution=(2244, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'ls-5',
                        'template': Template(r"./img/missions/ls-5.png", record_pos=(0.205, -0.118), resolution=(2340, 1080), rgb=True)
                    }
                ]
            },
            {
                'name': 'ap',
                'template': Template(r"./img/chapters/ap.png", record_pos=(-0.179, -0.06), resolution=(2244, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'ap-5',
                        'template': Template(r"./img/missions/ap-5.png", record_pos=(0.206, -0.117), resolution=(2340, 1080), rgb=True)
                    }
                ]
            },
            {
                'name': 'sk',
                'template': Template(r"./img/chapters/sk.png", record_pos=(-0.002, -0.061), resolution=(2244, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'sk-5',
                        'template': Template(r"./img/missions/sk-5.png", record_pos=(0.214, -0.115), resolution=(2340, 1080), rgb=True)
                    }
                ]
            },
            {
                'name': 'ca',
                'template': Template(r"./img/chapters/ca.png", record_pos=(0.356, -0.061), resolution=(2244, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'ca-5',
                        'template': Template(r"./img/missions/ca-5.png", record_pos=(0.203, -0.117), resolution=(2340, 1080), rgb=True)
                    }
                ]
            },
            {
                'name': 'ce',
                'template': Template(r"./img/chapters/ce.png", record_pos=(0.179, -0.059), resolution=(2244, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'ce-5',
                        'template': Template(r"./img/missions/ce-5.png", record_pos=(0.201, -0.118), resolution=(2340, 1080), rgb=True)
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
                'name': 'pr-a',
                'template': Template(r"./img/chapters/pr-a.png", record_pos=(0.268, -0.06), resolution=(2244, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'pr-a-1',
                        'template': Template(r"./img/missions/pr-a-1.png", record_pos=(-0.135, 0.056), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 'pr-a-2',
                        'template': Template(r"./img/missions/pr-a-2.png", record_pos=(0.124, -0.065), resolution=(2340, 1080), rgb=True)
                    },
                ]
            },
            {
                'name': 'pr-c',
                'template': Template(r"./img/chapters/pr-c.png", record_pos=(-0.09, -0.061), resolution=(2244, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'pr-c-1',
                        'template': Template(r"./img/missions/pr-c-1.png", record_pos=(-0.195, 0.043), resolution=(1920, 1080), rgb=True)
                    },
                    {
                        'name': 'pr-c-2',
                        'template': Template(r"./img/missions/pr-c-2.png", record_pos=(0.152, -0.075), resolution=(1920, 1080), rgb=True)
                    }
                ]
            },
            {
                'name': 'pr-b',
                'template': Template(r"./img/chapters/pr-b.png", record_pos=(-0.268, -0.06), resolution=(2244, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'pr-b-1',
                        'template': Template(r"./img/missions/pr-b-1.png", record_pos=(-0.157, 0.052), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 'pr-b-2',
                        'template': Template(r"./img/missions/pr-b-2.png", record_pos=(0.134, -0.074), resolution=(2340, 1080), rgb=True)
                    }
                ]
            },
            {
                'name': 'pr-d',
                'template': Template(r"./img/chapters/pr-d.png", record_pos=(0.089, -0.06), resolution=(2244, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'pr-d-1',
                        'template': Template(r"./img/missions/pr-d-1.png", record_pos=(-0.147, 0.048), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 'pr-d-2',
                        'template': Template(r"./img/missions/pr-d-2.png", record_pos=(0.124, -0.063), resolution=(2340, 1080), rgb=True)
                    },
                ]
            }
        ]
    },
    {
        'name': '火蓝之心',
        'template': Template(r"./img/series/hosf.png", record_pos=(0.039, 0.183), resolution=(2340, 1080)),
        'chapters': [
            {
                'name': 'of',
                'template': Template(r"./img/chapters/of.png", record_pos=(0.301, -0.021), resolution=(2340, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'of-6',
                        'template': Template(r"./img/missions/of-6.png", record_pos=(-0.284, -0.092), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 'of-7',
                        'template': Template(r"./img/missions/of-7.png", record_pos=(0.065, -0.015), resolution=(2340, 1080), rgb=True)
                    },
                    {
                        'name': 'of-8',
                        'template': Template(r"./img/missions/of-8.png", record_pos=(0.217, 0.055), resolution=(2340, 1080), rgb=True)
                    },
                ]
            },
            {
                'name': 'of-f',
                'template': Template(r"./img/chapters/of-f.png", record_pos=(0.287, 0.035), resolution=(2340, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'of-f4',
                        'template': Template(r"./img/missions/of-f4.png", record_pos=(0.24, -0.029), resolution=(2340, 1080))
                    },
                ]
            }
        ]
    },
    {
        'name': '密林悍将',
        'template': Template(r"./img/series/gtgr.png", record_pos=(0.12, 0.188), resolution=(2400, 1080)),
        'chapters': [
            {
                'name': 'ri',
                'template': Template(r"./img/chapters/ri.png", record_pos=(0.399, -0.013), resolution=(2400, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'ri-4',
                        'template': Template(r"./img/missions/ri-4.png", record_pos=(-0.255, 0.069), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'ri-5',
                        'template': Template(r"./img/missions/ri-5.png", record_pos=(0.096, 0.078), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'ri-6',
                        'template': Template(r"./img/missions/ri-6.png", record_pos=(-0.355, 0.076), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'ri-7',
                        'template': Template(r"./img/missions/ri-7.png", record_pos=(-0.099, -0.039), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'ri-8',
                        'template': Template(r"./img/missions/ri-8.png", record_pos=(-0.255, 0.028), resolution=(2400, 1080), rgb=True)
                    }
                ]
            }
        ]
    },
     {
        'name': '踏寻往西之风',
        'template': Template(r"./img/series/windpass.png", record_pos=(0.025, 0.19), resolution=(2400, 1080)),
        'chapters': [
            {
                'name': 'fa',
                'template': Template(r"./img/chapters/fa.png", record_pos=(-0.381, 0.066), resolution=(2400, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'fa-4',
                        'template': Template(r"./img/missions/fa-4.png", record_pos=(-0.03, 0.047), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'fa-5',
                        'template': Template(r"./img/missions/fa-5.png", record_pos=(0.084, -0.042), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'fa-6',
                        'template': Template(r"./img/missions/fa-6.png", record_pos=(0.176, 0.084), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'fa-7',
                        'template': Template(r"./img/missions/fa-7.png", record_pos=(0.252, 0.013), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'fa-8',
                        'template': Template(r"./img/missions/fa-8.png", record_pos=(0.322, -0.075), resolution=(2400, 1080), rgb=True)
                    }
                ]
            }
        ]
    },
    {
        'name': '骑兵与猎人',
        'template': Template(r"./img/series/grani.png", record_pos=(0.024, 0.18), resolution=(2400, 1080)),
        'chapters': [
            {
                'name': 'gt',
                'template': Template(r"./img/chapters/gt.png", record_pos=(0.216, 0.018), resolution=(2400, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'gt-1',
                        'template': Template(r"./img/missions/gt-1.png", record_pos=(-0.265, 0.015), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'gt-2',
                        'template': Template(r"./img/missions/gt-2.png", record_pos=(-0.185, -0.053), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'gt-3',
                        'template': Template(r"./img/missions/gt-3.png", record_pos=(-0.067, 0.004), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'gt-4',
                        'template': Template(r"./img/missions/gt-4.png", record_pos=(0.033, 0.081), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'gt-5',
                        'template': Template(r"./img/missions/gt-5.png", record_pos=(0.133, 0.013), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'gt-6',
                        'template': Template(r"./img/missions/gt-6.png", record_pos=(0.203, -0.061), resolution=(2400, 1080), rgb=True)
                    },
                ]
            }
        ]
    },
    {
        'name': '玛利亚临光',
        'template': Template(r"./img/series/maliya.png", record_pos=(0.025, 0.181), resolution=(2400, 1080)),
        'chapters': [
            {
                'name': 'mn',
                'template': Template(r"./img/chapters/mn.png", record_pos=(0.352, 0.047), resolution=(2400, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'mn-6',
                        'template': Template(r"./img/missions/mn-6.png", record_pos=(-0.143, -0.037), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'mn-7',
                        'template': Template(r"./img/missions/mn-7.png", record_pos=(-0.166, -0.14), resolution=(2400, 1080), rgb=True)
                    },
                    {
                        'name': 'mn-8',
                        'template': Template(r"./img/missions/mn-8.png", record_pos=(0.148, -0.062), resolution=(2400, 1080), rgb=True)
                    },
                ]
            }
        ]
    },
    {
        'name': '孤岛风云',
        'template': Template(r"./img/series/gudaofengyun.png", record_pos=(0.157, 0.225), resolution=(1920, 1081)),
        'chapters': [
            {
                'name': 'mb',
                'template': Template(r"./img/chapters/mb.png", record_pos=(0.321, -0.142), resolution=(1920, 1081)),
                'missions': [
                    {
                        'name': 'mb-6',
                        'template': Template(r"./img/missions/mb-6.png", record_pos=(0.172, 0.028), resolution=(1920, 1081))
                    },
                    {
                        'name': 'mb-7',
                        'template': Template(r"./img/missions/mb-7.png", record_pos=(0.173, 0.129), resolution=(1920, 1081))
                    },
                    {
                        'name': 'mb-8',
                        'template': Template(r"./img/missions/mb-8.png", record_pos=(0.402, 0.129), resolution=(1920, 1081))
                    },
                ]
            }
        ]
    },
    {
        'name': '此地之外',
        'template': Template(r"./img/series/cidizhiwai.png", record_pos=(0.025, 0.181), resolution=(2400, 1080)),
        'chapters': [
            {
                'name': 'bh',
                'template': Template(r"./img/chapters/bh.png", record_pos=(0.238, 0.126), resolution=(2400, 1080), rgb=True, threshold=0.8),
                'missions': [
                    {
                        'name': 'bh-6',
                        'template': Template(r"./img/missions/bh-6.png", record_pos=(0.131, 0.058), resolution=(2400, 1080))
                    },
                    {
                        'name': 'bh-7',
                        'template': Template(r"./img/missions/bh-7.png", record_pos=(0.204, -0.057), resolution=(2400, 1080))
                    },
                    {
                        'name': 'bh-8',
                        'template': Template(r"./img/missions/bh-8.png", record_pos=(0.301, 0.005), resolution=(2400, 1080))
                    },
                ]
            }
        ]
    }
]

# 需要额外门票的关卡
def isNeedTicket(chapterName):
    needTicket = ['of-f']
    return needTicket.count(chapterName) > 0

# 整理对照表
def mgnMaps():
    maps = {}
    for s in series:
        seryName = s['name']
        seryTarget = s['template']
        for c in s['chapters']:
            chapterName = c['name']
            chapterTarget = c['template']
            for m in c['missions']:
                index = c['missions'].index(m)
                missionName = m['name']
                missionTarget = m['template']
                maps[missionName] = { 'seryTarget': seryTarget, 'chapterTarget': chapterTarget, 'missionTarget': missionTarget, 'seryName': seryName, 'chapterName': chapterName, 'missionName': missionName, 'missionOrder': index }
    return maps

missionMaps = mgnMaps()

# 时间模糊化
def rt(time):
    return time + random.randint(0, __random__time)

# 坐标模糊化
def rangeTarget (targetAxios, range=5):
    d=random.randint(-range, range)
    return [targetAxios[0] + d, targetAxios[1] + d]

# 模糊化点击图片
def rangeTouchImg(template):
    touch(rangeTarget(exists(template)), duration=0.03)

# 设置全局
def setCurrent(s, c, m, st, ct, mt, mo):
    global currentSery
    global currentChapter
    global currentMission
    global currentSeryTarget
    global currentChapterTarget
    global currentMissionTarget
    global currentMissionOrder

    currentSery = s
    currentChapter = c
    currentMission = m
    currentSeryTarget = st
    currentChapterTarget = ct
    currentMissionTarget = mt
    currentMissionOrder = mo

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
def goToSeries(target, name=''):
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
        rangeTouchImg(Template(r"./img/nav/home.png", record_pos=(-0.35, -0.06), resolution=(2340, 1080)))
        sleep(rt(3))
        touch(wait(Template(r"./img/nav/home-fight.png", record_pos=(0.271, -0.132), resolution=(2340, 1080))))
    sleep(rt(3))
    if (exists(target)):
        rangeTouchImg(target)
        sleep(rt(2))
        return True
    else:
        print('系列不存在或未开放：' + name)
        return False

# 从左到右滑动，寻找相关选项
def swipeToArea(target, type, name='', missionOrder=False):
    # 先直接尝试寻找目标
    if (exists(target)):
        if (__test__mode and type == 'mission'): return True
        rangeTouchImg(target)
        sleep(rt(2))
        return True
    # 如果没有寻找到，则再从左到右寻找
    # 最大重试次数
    maxTimes = 15 if (type == 'mission') else 5
    vStartLeft = [0.128*w, 0.278*h]
    vStartRight = [0.769*w, 0.278*h]
    step = -0.2 if (type == 'mission') else -0.5
    if ((missionOrder is False)):
        swipe(v1=vStartLeft, vector=[1, 0], duration=0.2)
        swipe(v1=vStartLeft, vector=[1, 0], duration=0.2)
    else:
        step = -step if (missionOrder < currentMissionOrder) else step
    sleep(rt(2))
    while ((not exists(target)) and maxTimes > 0):
        maxTimes -= 1
        swipe(vStartRight, vector=[step, 0], steps=30, duration=1)
        touch([0.5*w, 0.08*h], duration=2)
    if (maxTimes <= 0):
        des = '关卡' if (type == 'mission') else '章节'
        print(des + '不存在或未开放：' + name)
        return False
    else:
        if (__test__mode and type == 'mission'): return True
        rangeTouchImg(target)
        sleep(rt(2))
        return True

# 刷关卡
def fight(times=1, missionTarget=False, actionStartChange=False):
    global max_rock_num
    global _actionStart
    global _actionStart2
    global rationalPotion
    global rationalRock
    _actionStartLocal = _actionStart2 if actionStartChange else _actionStart
    # 本关卡的默认时间为全局配置的时间；重复通关同一关卡后，该时间会被不断优化修正
    minMissionTime = MIN_MISSION_TIME
    num = 0
    # 如果没有选择代理指挥，则勾选代理指挥
    if (exists(_proxy)):
        touch(_proxy)
    while(times > 0):
        num += 1
        times -= 1
        # # 判断关卡有没有被选择
        # if (missionTarget and exists(missionTarget)):
        #     rangeTouchImg(missionTarget)
        #     sleep(rt(1))
        wait(_actionStartLocal)
        rangeTouchImg(_actionStartLocal)
        sleep(2)
        # 如果体力不足了
        if (actionStartChange):
            if (exists(_noTicket)):
                break
        elif (exists(_supply)):
            # 不需要补充体力
            if (USE_SUPPLY == 'none'):
                rangeTouchImg(_cancelUse)
                print('------------------ 体力用尽，结束 --------------------')
                break
            # 只喝体力药
            elif (USE_SUPPLY == 'potion'):
                if (exists(_useRock)):
                    rangeTouchImg(_cancelUse)
                    break
                else: 
                    rangeTouchImg(_supply)
                    rationalPotion += 1
                    print('------已使用理智液: ' + str(rationalPotion) + '------')
            # 不仅喝体力药，还要碎石
            else:
                # 如果是碎石，那么考虑最大碎石头数
                if (exists(_useRock)):
                    if (max_rock_num == 0):
                        break
                    max_rock_num -= 1
                rangeTouchImg(_supply)
                rationalRock = rationalRock + 1
                print('------已使用理智源石: ' + str(rationalRock) + '------')
            sleep(rt(3))
            wait(_actionStartLocal)
            rangeTouchImg(_actionStartLocal)
            sleep(rt(2))
        wait(_actionStartIm)
        rangeTouchImg(_actionStartIm)
        sysTimeStart = (int(time.strftime("%H", time.localtime())))
        # 记录关卡开始的时间戳
        timeStart = int(time.time())
        # 最快的关卡2倍速也不会低于 MIN_MISSION_TIME
        sleep(rt(minMissionTime))
        while True:
            isCompleted = False
            # 预先检查是否完成
            if (exists(_missionComplete)):
                isCompleted = True
                # 记录关卡结束后的时间戳，并重新计算关卡时间
                minMissionTime = (int(time.time()) - timeStart) - 10
                # 检测到后，先等待3秒
                sleep(rt(4))
            # 如果任务完成了
            if (exists(_missionComplete)):
                if (not isCompleted):
                    isCompleted = True
                    sleep(rt(4))
                    minMissionTime = (int(time.time()) - timeStart) - 10
                touch(rangeTarget([230, 230], 30))
                print(''.join(['已刷:', str(num), "次; 剩余：", str(times), '次; 时间：', str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))]))
                sysTimeEnd = (int(time.strftime("%H", time.localtime())))
                break
            # 如果代理失误了
            elif (PROXY_ERROR_CHECK and exists(_proxyFailed)):
                touch(_giveUp)
                touch(wait(_actionFailed))
                num -= 1
                times += 1
                print('------代理失误------')
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
        wait(_actionStartLocal)
        # 如果刚好进入了每日登陆
        # if (sysTimeStart == 3 and sysTimeEnd == 4 and ACROSS_NIGHT and skipSignIn()):
        #     if (not ((currentSery == '') and (currentChapter == '') and (currentMission == ''))):
        #         goToSeries(currentSeryTarget, currentSery)
        #         swipeToArea(currentChapterTarget, 'chapter', currentChapter)
        #         swipeToArea(currentMissionTarget, 'mission', currentMission)

# 完整的一个关卡流程
def runMission(seryName, chapterName, missionName, seryTarget, chapterTarget, missionTarget, missionOrder, times=1):
    global currentDeps
    isSameChapter = False
    if (seryName == currentSery):
        touch([0.5*w, 0.08*h])
        if (chapterName != currentChapter):
            if (currentDeps == 2):
                touch(_barLeft)
                currentDeps = 1
                sleep(1)
            if (not swipeToArea(chapterTarget, 'chapter', chapterName)): return
            currentDeps = 2
        else: isSameChapter = True
    else:
        if (not goToSeries(seryTarget, seryName)): return
        currentDeps = 1
        if (not swipeToArea(chapterTarget, 'chapter', chapterName)): return
        currentDeps = 2
    if (not swipeToArea(missionTarget, 'mission', missionName, isSameChapter and missionOrder)): return
    setCurrent(seryName, chapterName, missionName, seryTarget, chapterTarget, missionTarget, missionOrder)
    print('------------------'+ seryName + ': ' + missionName +'--------------------')
    if (__test__mode):
        point = '进入关卡_'+currentMission+'-测试截图'
        assert_exists(missionTarget, point)
        return
    else: fight(times, missionTarget, isNeedTicket(chapterName))

# 检查关卡是否存在
def checkMission(mList=[]):
    passed = True
    length = len(mList)
    for i in mList:
        name = i[0]
        times = i[1]
        if (not missionMaps[name]):
            passed = False
            print('关卡'+name+'未在脚本数据中')
        if (times < 0):
            passed = False
            print('关卡'+name+'的重复数不可为负')
    return passed
# 执行函数
def run(runList=[]):
    if (checkMission(runList)):
        for i in runList:
            name = i[0]
            times = i[1]
            missionInfo = missionMaps[i[0]]
            runMission(missionInfo['seryName'], missionInfo['chapterName'], missionInfo['missionName'], missionInfo['seryTarget'], missionInfo['chapterTarget'], missionInfo['missionTarget'], missionInfo['missionOrder'], times)

# 对全部关卡进行测试并截图报告
def runTest(start=False):
    global __test__mode
    global __random__time
    __test__mode = True
    cacheRandomTime = __random__time
    __random__time = 0
    startCollect = False if (start) else True
    runList = []
    for i in missionMaps:
        if (not startCollect): startCollect = i == start
        if (startCollect): runList.append([i, 0])
    run(runList)
    sleep(1)
    __test__mode = False
    __random__time = cacheRandomTime

# ======刷图流程=======
# 例如
run([["4-6", 1], ['3-3', 8], ['s5-8', 11], ['s3-6', 1], ['7-10', 3]])
# runTest('4-6')
# ===================
