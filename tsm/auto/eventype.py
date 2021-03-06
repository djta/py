# -*- coding: utf-8 -*-

'''
本文件仅用于存放对于事件类型常量的定义。

由于python中不存在真正的常量概念，因此选择使用全大写的变量名来代替常量。
这里设计的命名规则以EVENT_前缀开头。

常量的内容通常选择一个能够代表真实意义的字符串（便于理解）。

建议将所有的常量定义放在该文件中，便于检查是否存在重复的现象。
'''


EVENT_TIMER = 'eTimer'                          # 计时器事件，每隔1秒发送一次
EVENT_AXEAGLE = 'axeagel'
EVENT_MARKETDATA = 'eMarketData'                # 行情推送事件
EVENT_MARKETDATA_CONTRACT = 'eMarketData.'      # 特定合约的行情快照事件
EVENT_MATCH_CONTRACT = 'eMatch.'                # 特定合约的成交事件
EVENT_SENDMAIL = 'eSendMail'                    # 发送邮件事件
EVENT_TRADE = 'eTrade'                          # 交易事件
EVENT_CON_TRADE = 'eConTrade'                   # 条件订单
EVENT_TRADE_CONTRACT = 'eTrade.'                # 特定合约的交易事件
EVENT_TRADE_REMARKS = 'eTradeRM.'                 # 特定备注的交易事件
EVENT_QUERY_RET = 'eQueryRet.'                  # 特定功能号的查询结果
EVENT_FIRST_TABLE_SUCCESS = 'eFirstTableSuccess'# 第一结果集的执行成功信息
EVENT_FIRST_TABLE_ERROR = 'eFirstTableError'    # 第一结果集的错误信息（后台返回的业务错误信息）
EVENT_EA_ERROR = 'eEaError'                    # Ea返回错误信息（互联网交易网关返回的错误信息）

#----------------------------------------------------------------------
def test():
    """检查是否存在内容重复的常量定义"""
    check_dict = {}
    
    global_dict = globals()    
    
    for key, value in global_dict.items():
        if '__' not in key:                       # 不检查python内置对象
            if value in check_dict:
                check_dict[value].append(key)
            else:
                check_dict[value] = [key]
            
    for key, value in check_dict.items():
        if len(value)>1:
            print u'存在重复的常量定义:' + str(key) 
            for name in value:
                print name
            print ''
        
    print u'测试完毕'
    

# 直接运行脚本可以进行测试
if __name__ == '__main__':
    test()