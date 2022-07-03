from life_logger import *

ltm = LogTypeManager()
ltm.addLogTypeList(
    [
    LogType('먹은 음식', 3600 * 1000, ['백반', '중식', '한식', '짬뽕']),
    LogType('한 행동', 3600, ['공부', '게임', '식사']),
    LogType('기분', 3600, ['평범', '행복', '불안']),
    LogType('수면시간', 3600 * 24, ['평범', '행복', '불안'])
    ])

ltm_json = ltm.toJSON()
print(ltm_json)

ltm2 = LogTypeManager()
ltm2.setJson(ltm_json)

ltm2_json = ltm2.toJSON()
print('ltm2====================')
print(ltm2_json)