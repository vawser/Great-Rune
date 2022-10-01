# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Grace
#-----------------------------------------------------
def t000001000_1():
    """State 0,1"""
    t000001000_x22()
    Quit()

def t000001000_x0(action2=_):
    """State 0,1"""
    OpenGenericDialog(8, action2, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t000001000_x1():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t000001000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000001000_x3(actionbutton1=_, flag3=6001, flag4=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 2"""
        assert CompareBonfireState(1)
        """State 4"""
        if GetEventFlag(flag4) == 1:
            """State 5"""
            assert GetEventFlag(flag3) == 1 and not GetEventFlag(flag4)
            """State 6"""
            assert GetCurrentStateElapsedTime() > 1
        elif GetEventFlag(flag3) == 1 and not GetEventFlag(flag4):
            pass
        """State 3"""
        if CompareBonfireState(0):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif not GetEventFlag(flag3) or GetEventFlag(flag4) == 1:
            pass
    """State 7"""
    return 0

def t000001000_x4(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t000001000_x5(actionbutton5=6100, flag1=6001, flag2=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert GetEventFlag(flag1) == 1 and not GetEventFlag(flag2)
        """State 2"""
        # actionbutton:6100:"Touch grace"
        if CheckActionButtonArea(actionbutton5):
            break
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif not GetEventFlag(flag1) or GetEventFlag(flag2) == 1:
            pass
    """State 4"""
    return 0

def t000001000_x6(goods3=1000, goods4=10020):
    """State 0,14"""
    if GetEventFlag(720080) == 1:
        """State 15"""
        pass
    else:
        """State 16,17"""
        SetEventFlag(720080, 1)
    """State 1"""
    if GetTotalBonfireLevel() <= 13:
        """State 2,13,26"""
        # goods:1000:Flask of Crimson Tears, goods:1001:Flask of Crimson Tears, goods:1002:Flask of Crimson Tears +1, goods:1003:Flask of Crimson Tears +1, goods:1004:Flask of Crimson Tears +2, goods:1005:Flask of Crimson Tears +2, goods:1006:Flask of Crimson Tears +3, goods:1007:Flask of Crimson Tears +3, goods:1008:Flask of Crimson Tears +4, goods:1009:Flask of Crimson Tears +4, goods:1010:Flask of Crimson Tears +5, goods:1011:Flask of Crimson Tears +5, goods:1012:Flask of Crimson Tears +6, goods:1013:Flask of Crimson Tears +6, goods:1014:Flask of Crimson Tears +7, goods:1015:Flask of Crimson Tears +7, goods:1016:Flask of Crimson Tears +8, goods:1017:Flask of Crimson Tears +8, goods:1018:Flask of Crimson Tears +9, goods:1019:Flask of Crimson Tears +9, goods:1020:Flask of Crimson Tears +10, goods:1021:Flask of Crimson Tears +10, goods:1022:Flask of Crimson Tears +11, goods:1023:Flask of Crimson Tears +11, goods:1024:Flask of Crimson Tears +12, goods:1025:Flask of Crimson Tears +12
        call = t000001000_x17(goods3=goods3, goods6=0, z31=1)
        if call.Get() == 0:
            """State 12,25"""
            # action:13040150:"No Flask of Crimson Tears in inventory"
            assert t000001000_x4(action1=13040150)
        elif call.Done():
            """State 11,19"""
            SetWorkValue(1, 1)
            """State 20"""
            call = t000001000_x0(action2=20011000 + GetWorkValue(1))
            if call.Get() == 0:
                """State 6,10"""
                # goods:10020:Sacred Tear
                if ComparePlayerInventoryNumber(3, goods4, 4, GetWorkValue(1), 0) == 1:
                    """State 4,8"""
                    BonfireActivation(GetTotalBonfireLevel() + 1)
                    """State 9"""
                    # goods:10020:Sacred Tear
                    PlayerEquipmentQuantityChange(3, goods4, GetWorkValue(1) * -1)
                    """State 27"""
                    assert t000001000_x19(goods3=goods3)
                    """State 24"""
                    assert t000001000_x16(goods5=goods3)
                    """State 22"""
                    # action:13040020:"Increased the amount of HP/FP replenished by your flasks"
                    assert t000001000_x4(action1=13040020)
                    """State 18"""
                    SetWorkValue(1, 0)
                else:
                    """State 5,28"""
                    # action:20011000:"No Sacred Tear in inventory"
                    assert t000001000_x4(action1=20011000)
            elif call.Done():
                """State 7"""
                pass
    else:
        """State 3,21"""
        # action:13040000:"The amount of HP/FP your flasks replenish cannot be increased any further"
        assert t000001000_x4(action1=13040000)
    """State 29"""
    return 0
    """Unused"""
    """State 23"""
    t000001000_x11()
    Quit()

def t000001000_x7(goods1=1000, goods2=10010):
    """State 0,15"""
    if GetEventFlag(720070) == 1:
        """State 16"""
        pass
    else:
        """State 17,18"""
        SetEventFlag(720070, 1)
    """State 1"""
    if GetEstusAllocation(0) + GetEstusAllocation(1) < 13:
        """State 2,13,26"""
        # goods:1000:Flask of Crimson Tears, goods:1001:Flask of Crimson Tears, goods:1002:Flask of Crimson Tears +1, goods:1003:Flask of Crimson Tears +1, goods:1004:Flask of Crimson Tears +2, goods:1005:Flask of Crimson Tears +2, goods:1006:Flask of Crimson Tears +3, goods:1007:Flask of Crimson Tears +3, goods:1008:Flask of Crimson Tears +4, goods:1009:Flask of Crimson Tears +4, goods:1010:Flask of Crimson Tears +5, goods:1011:Flask of Crimson Tears +5, goods:1012:Flask of Crimson Tears +6, goods:1013:Flask of Crimson Tears +6, goods:1014:Flask of Crimson Tears +7, goods:1015:Flask of Crimson Tears +7, goods:1016:Flask of Crimson Tears +8, goods:1017:Flask of Crimson Tears +8, goods:1018:Flask of Crimson Tears +9, goods:1019:Flask of Crimson Tears +9, goods:1020:Flask of Crimson Tears +10, goods:1021:Flask of Crimson Tears +10, goods:1022:Flask of Crimson Tears +11, goods:1023:Flask of Crimson Tears +11, goods:1024:Flask of Crimson Tears +12, goods:1025:Flask of Crimson Tears +12
        call = t000001000_x17(goods3=goods1, goods6=0, z31=1)
        if call.Get() == 0:
            """State 12,25"""
            # action:13040150:"No Flask of Crimson Tears in inventory"
            assert t000001000_x4(action1=13040150)
        elif call.Done():
            """State 11,19"""
            SetWorkValue(1, GetEstusAllocation(0) + GetEstusAllocation(1) + -4)
            """State 28"""
            assert (t000001000_x21(z18=1, z19=1, z20=2, z21=2, z22=3, z23=3, z24=4, z25=4, z26=5, z27=5,
                    z28=1))
            """State 21"""
            call = t000001000_x0(action2=20011010 + GetWorkValue(1))
            if call.Get() == 0:
                """State 6,14"""
                # goods:10010:Golden Seed
                if ComparePlayerInventoryNumber(3, goods2, 4, GetWorkValue(1), 0) == 1:
                    """State 4,8"""
                    # goods:10010:Golden Seed
                    PlayerEquipmentQuantityChange(3, goods2, GetWorkValue(1) * -1)
                    """State 9"""
                    EstusAllocationUpdate(GetEstusAllocation(0) + 1, 0)
                    """State 27"""
                    assert t000001000_x16(goods5=goods1)
                    """State 22"""
                    # action:13040140:"Added a charge to Flask of Crimson Tears"
                    assert t000001000_x4(action1=13040140)
                    """State 20"""
                    SetWorkValue(1, 0)
                    """State 10"""
                else:
                    """State 5,23"""
                    # action:20011010:"Not enough Golden Seeds"
                    assert t000001000_x4(action1=20011010)
            elif call.Done():
                """State 7"""
                pass
    else:
        """State 3,24"""
        # action:13040120:"Flask charges already at maximum"
        assert t000001000_x4(action1=13040120)
    """State 29"""
    return 0

def t000001000_x8(goods7=1000):
    """State 0,1"""
    # goods:1001:Flask of Crimson Tears, goods:1000:Flask of Crimson Tears
    if DoesPlayerHaveItem(3, goods7 + 1 + 0 * 50 + 0 * 2) == 1 or DoesPlayerHaveItem(3, goods7 + 0 + 0 * 50 + 0 * 2) == 1:
        """State 2"""
        BonfireActivation(1)
        """State 13"""
        Label('L0')
        """State 18"""
        assert t000001000_x9(goods7=goods7)
    # goods:1003:Flask of Crimson Tears +1, goods:1002:Flask of Crimson Tears +1
    elif DoesPlayerHaveItem(3, goods7 + 1 + 0 * 50 + 1 * 2) == 1 or DoesPlayerHaveItem(3, goods7 + 0 + 0 * 50 + 1 * 2) == 1:
        """State 3"""
        BonfireActivation(2)
        Goto('L0')
    # goods:1005:Flask of Crimson Tears +2, goods:1004:Flask of Crimson Tears +2
    elif DoesPlayerHaveItem(3, goods7 + 1 + 0 * 50 + 2 * 2) == 1 or DoesPlayerHaveItem(3, goods7 + 0 + 0 * 50 + 2 * 2) == 1:
        """State 4"""
        BonfireActivation(3)
        Goto('L0')
    # goods:1007:Flask of Crimson Tears +3, goods:1006:Flask of Crimson Tears +3
    elif DoesPlayerHaveItem(3, goods7 + 1 + 0 * 50 + 3 * 2) == 1 or DoesPlayerHaveItem(3, goods7 + 0 + 0 * 50 + 3 * 2) == 1:
        """State 5"""
        BonfireActivation(4)
        Goto('L0')
    # goods:1009:Flask of Crimson Tears +4, goods:1008:Flask of Crimson Tears +4
    elif DoesPlayerHaveItem(3, goods7 + 1 + 0 * 50 + 4 * 2) == 1 or DoesPlayerHaveItem(3, goods7 + 0 + 0 * 50 + 4 * 2) == 1:
        """State 6"""
        BonfireActivation(5)
        Goto('L0')
    # goods:1011:Flask of Crimson Tears +5, goods:1010:Flask of Crimson Tears +5
    elif DoesPlayerHaveItem(3, goods7 + 1 + 0 * 50 + 5 * 2) == 1 or DoesPlayerHaveItem(3, goods7 + 0 + 0 * 50 + 5 * 2) == 1:
        """State 7"""
        BonfireActivation(6)
        Goto('L0')
    # goods:1013:Flask of Crimson Tears +6, goods:1012:Flask of Crimson Tears +6
    elif DoesPlayerHaveItem(3, goods7 + 1 + 0 * 50 + 6 * 2) == 1 or DoesPlayerHaveItem(3, goods7 + 0 + 0 * 50 + 6 * 2) == 1:
        """State 8"""
        BonfireActivation(7)
        Goto('L0')
    # goods:1015:Flask of Crimson Tears +7, goods:1014:Flask of Crimson Tears +7
    elif DoesPlayerHaveItem(3, goods7 + 1 + 0 * 50 + 7 * 2) == 1 or DoesPlayerHaveItem(3, goods7 + 0 + 0 * 50 + 7 * 2) == 1:
        """State 9"""
        BonfireActivation(8)
        Goto('L0')
    # goods:1017:Flask of Crimson Tears +8, goods:1016:Flask of Crimson Tears +8
    elif DoesPlayerHaveItem(3, goods7 + 1 + 0 * 50 + 8 * 2) == 1 or DoesPlayerHaveItem(3, goods7 + 0 + 0 * 50 + 8 * 2) == 1:
        """State 10"""
        BonfireActivation(9)
        Goto('L0')
    # goods:1019:Flask of Crimson Tears +9, goods:1018:Flask of Crimson Tears +9
    elif DoesPlayerHaveItem(3, goods7 + 1 + 0 * 50 + 9 * 2) == 1 or DoesPlayerHaveItem(3, goods7 + 0 + 0 * 50 + 9 * 2) == 1:
        """State 11"""
        BonfireActivation(10)
        Goto('L0')
    # goods:1021:Flask of Crimson Tears +10, goods:1020:Flask of Crimson Tears +10
    elif DoesPlayerHaveItem(3, goods7 + 1 + 0 * 50 + 10 * 2) == 1 or DoesPlayerHaveItem(3, goods7 + 0 + 0 * 50 + 10 * 2) == 1:
        """State 12"""
        BonfireActivation(11)
        Goto('L0')
    elif True:
        """State 15"""
        pass
    # goods:1023:Flask of Crimson Tears +11, goods:1022:Flask of Crimson Tears +11
    elif DoesPlayerHaveItem(3, goods7 + 1 + 0 * 50 + 11 * 2) == 1 or DoesPlayerHaveItem(3, goods7 + 0 + 0 * 50 + 11 * 2) == 1:
        """State 16"""
        BonfireActivation(12)
        Goto('L0')
    # goods:1025:Flask of Crimson Tears +12, goods:1024:Flask of Crimson Tears +12
    elif DoesPlayerHaveItem(3, goods7 + 1 + 0 * 50 + 12 * 2) == 1 or DoesPlayerHaveItem(3, goods7 + 0 + 0 * 50 + 12 * 2) == 1:
        """State 17"""
        BonfireActivation(13)
        Goto('L0')
    """State 14,19"""
    return 0

def t000001000_x9(goods7=1000):
    """State 0,15"""
    # goods:1000:Flask of Crimson Tears, goods:1002:Flask of Crimson Tears +1, goods:1004:Flask of Crimson Tears +2, goods:1006:Flask of Crimson Tears +3, goods:1008:Flask of Crimson Tears +4, goods:1010:Flask of Crimson Tears +5, goods:1012:Flask of Crimson Tears +6, goods:1014:Flask of Crimson Tears +7
    call = t000001000_x12(goods7=goods7, goods8=0, goods9=0)
    if call.Get() == 1:
        """State 1,11"""
        # goods:1000:Flask of Crimson Tears, goods:1002:Flask of Crimson Tears +1, goods:1004:Flask of Crimson Tears +2, goods:1006:Flask of Crimson Tears +3, goods:1008:Flask of Crimson Tears +4, goods:1010:Flask of Crimson Tears +5, goods:1012:Flask of Crimson Tears +6, goods:1014:Flask of Crimson Tears +7, goods:1016:Flask of Crimson Tears +8, goods:1018:Flask of Crimson Tears +9
        assert t000001000_x10(goods7=goods7, goods10=0, goods11=0)
    elif call.Done():
        """State 16"""
        # goods:1001:Flask of Crimson Tears, goods:1003:Flask of Crimson Tears +1, goods:1005:Flask of Crimson Tears +2, goods:1007:Flask of Crimson Tears +3, goods:1009:Flask of Crimson Tears +4, goods:1011:Flask of Crimson Tears +5, goods:1013:Flask of Crimson Tears +6, goods:1015:Flask of Crimson Tears +7
        call = t000001000_x12(goods7=goods7, goods8=0, goods9=1)
        if call.Get() == 1:
            """State 8,10"""
            # goods:1001:Flask of Crimson Tears, goods:1003:Flask of Crimson Tears +1, goods:1005:Flask of Crimson Tears +2, goods:1007:Flask of Crimson Tears +3, goods:1009:Flask of Crimson Tears +4, goods:1011:Flask of Crimson Tears +5, goods:1013:Flask of Crimson Tears +6, goods:1015:Flask of Crimson Tears +7, goods:1017:Flask of Crimson Tears +8, goods:1019:Flask of Crimson Tears +9
            assert t000001000_x10(goods7=goods7, goods10=0, goods11=1)
        elif call.Done():
            """State 2"""
            pass
    """State 5,17"""
    # goods:1050:Flask of Cerulean Tears, goods:1052:Flask of Cerulean Tears +1, goods:1054:Flask of Cerulean Tears +2, goods:1056:Flask of Cerulean Tears +3, goods:1058:Flask of Cerulean Tears +4, goods:1060:Flask of Cerulean Tears +5, goods:1062:Flask of Cerulean Tears +6, goods:1064:Flask of Cerulean Tears +7
    call = t000001000_x12(goods7=goods7, goods8=1, goods9=0)
    if call.Get() == 1:
        """State 3,13"""
        # goods:1050:Flask of Cerulean Tears, goods:1052:Flask of Cerulean Tears +1, goods:1054:Flask of Cerulean Tears +2, goods:1056:Flask of Cerulean Tears +3, goods:1058:Flask of Cerulean Tears +4, goods:1060:Flask of Cerulean Tears +5, goods:1062:Flask of Cerulean Tears +6, goods:1064:Flask of Cerulean Tears +7, goods:1066:Flask of Cerulean Tears +8, goods:1068:Flask of Cerulean Tears +9
        assert t000001000_x10(goods7=goods7, goods10=1, goods11=0)
    elif call.Done():
        """State 18"""
        # goods:1051:Flask of Cerulean Tears, goods:1053:Flask of Cerulean Tears +1, goods:1055:Flask of Cerulean Tears +2, goods:1057:Flask of Cerulean Tears +3, goods:1059:Flask of Cerulean Tears +4, goods:1061:Flask of Cerulean Tears +5, goods:1063:Flask of Cerulean Tears +6, goods:1065:Flask of Cerulean Tears +7
        call = t000001000_x12(goods7=goods7, goods8=1, goods9=1)
        if call.Get() == 1:
            """State 9,12"""
            # goods:1051:Flask of Cerulean Tears, goods:1053:Flask of Cerulean Tears +1, goods:1055:Flask of Cerulean Tears +2, goods:1057:Flask of Cerulean Tears +3, goods:1059:Flask of Cerulean Tears +4, goods:1061:Flask of Cerulean Tears +5, goods:1063:Flask of Cerulean Tears +6, goods:1065:Flask of Cerulean Tears +7, goods:1067:Flask of Cerulean Tears +8, goods:1069:Flask of Cerulean Tears +9
            assert t000001000_x10(goods7=goods7, goods10=1, goods11=1)
        elif call.Done():
            """State 4"""
            pass
    """State 6,14"""
    assert t000001000_x11()
    """State 7,19"""
    return 0

def t000001000_x10(goods7=1000, goods10=_, goods11=_):
    """State 0,1"""
    if DoesPlayerHaveItem(3, goods7 + goods11 + goods10 * 50 + 0 * 2) == 1:
        """State 3"""
        ReplaceTool(goods7 + goods10 * 50 + 0 * 2 + goods11, goods7 + goods10 * 50 + goods11 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif DoesPlayerHaveItem(3, goods7 + goods11 + goods10 * 50 + 1 * 2) == 1:
        """State 4"""
        ReplaceTool(goods7 + goods10 * 50 + 1 * 2 + goods11, goods7 + goods10 * 50 + goods11 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif DoesPlayerHaveItem(3, goods7 + goods11 + goods10 * 50 + 2 * 2) == 1:
        """State 5"""
        ReplaceTool(goods7 + goods10 * 50 + 2 * 2 + goods11, goods7 + goods10 * 50 + goods11 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif DoesPlayerHaveItem(3, goods7 + goods11 + goods10 * 50 + 3 * 2) == 1:
        """State 6"""
        ReplaceTool(goods7 + goods10 * 50 + 3 * 2 + goods11, goods7 + goods10 * 50 + goods11 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif DoesPlayerHaveItem(3, goods7 + goods11 + goods10 * 50 + 4 * 2) == 1:
        """State 7"""
        ReplaceTool(goods7 + goods10 * 50 + 4 * 2 + goods11, goods7 + goods10 * 50 + goods11 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif DoesPlayerHaveItem(3, goods7 + goods11 + goods10 * 50 + 5 * 2) == 1:
        """State 8"""
        ReplaceTool(goods7 + goods10 * 50 + 5 * 2 + goods11, goods7 + goods10 * 50 + goods11 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    elif DoesPlayerHaveItem(3, goods7 + goods11 + goods10 * 50 + 6 * 2) == 1:
        """State 9"""
        ReplaceTool(goods7 + goods10 * 50 + 6 * 2 + goods11, goods7 + goods10 * 50 + goods11 + 2 * (GetTotalBonfireLevel() - 1),
                    1)
    else:
        """State 2"""
        pass
    """State 13"""
    return 0
    """Unused"""
    """State 10"""
    ReplaceTool(goods7 + goods10 * 50 + 7 * 2 + goods11, goods7 + goods10 * 50 + goods11 + 2 * (GetTotalBonfireLevel() - 1),
                1)
    Quit()
    """State 11"""
    ReplaceTool(goods7 + goods10 * 50 + 8 * 2 + goods11, goods7 + goods10 * 50 + goods11 + 2 * (GetTotalBonfireLevel() - 1),
                1)
    Quit()
    """State 12"""
    ReplaceTool(goods7 + goods10 * 50 + 9 * 2 + goods11, goods7 + goods10 * 50 + goods11 + 2 * (GetTotalBonfireLevel() - 1),
                1)
    Quit()

def t000001000_x11():
    """State 0,1,13,14"""
    return 0
    """Unused"""
    """State 2,3,4"""
    Quit()
    """State 5"""
    Quit()
    """State 6"""
    Quit()
    """State 7"""
    Quit()
    """State 8"""
    Quit()
    """State 9"""
    Quit()
    """State 10"""
    Quit()
    """State 11"""
    Quit()
    """State 12"""
    Quit()

def t000001000_x12(goods7=1000, goods8=_, goods9=_):
    """State 0,1"""
    if (not DoesPlayerHaveItem(3, goods7 + goods9 + goods8 * 50 + 0 * 2) and not DoesPlayerHaveItem(3,
        goods7 + goods9 + goods8 * 50 + 1 * 2) and not DoesPlayerHaveItem(3, goods7 + goods9 + goods8
        * 50 + 2 * 2) and not DoesPlayerHaveItem(3, goods7 + goods9 + goods8 * 50 + 3 * 2) and not DoesPlayerHaveItem(3,
        goods7 + goods9 + goods8 * 50 + 4 * 2) and not DoesPlayerHaveItem(3, goods7 + goods9 + goods8
        * 50 + 5 * 2) and not DoesPlayerHaveItem(3, goods7 + goods9 + goods8 * 50 + 6 * 2) and not DoesPlayerHaveItem(3,
        goods7 + goods9 + goods8 * 50 + 7 * 2)):
        """State 2,3"""
        return 0
    else:
        """State 4"""
        return 1

def t000001000_x13():
    """State 0,1"""
    if DoesPlayerHaveSpEffect(8990) == 1:
        """State 2"""
        GiveSpEffectToPlayer(8998)
        """State 3"""
        SetEventFlag(100210, 0)
        SetEventFlag(100200, 0)
    else:
        pass
    """State 4"""
    return 0

def t000001000_x14(text1=_, z32=_, mode2=1):
    """State 0,5"""
    assert t000001000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode2:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(z32, 1)
    """State 6"""
    return 0

def t000001000_x15(goods5=1000):
    """State 0,4,10"""
    # goods:1000:Flask of Crimson Tears, goods:1001:Flask of Crimson Tears, goods:1002:Flask of Crimson Tears +1, goods:1003:Flask of Crimson Tears +1, goods:1004:Flask of Crimson Tears +2, goods:1005:Flask of Crimson Tears +2, goods:1006:Flask of Crimson Tears +3, goods:1007:Flask of Crimson Tears +3, goods:1008:Flask of Crimson Tears +4, goods:1009:Flask of Crimson Tears +4, goods:1010:Flask of Crimson Tears +5, goods:1011:Flask of Crimson Tears +5, goods:1012:Flask of Crimson Tears +6, goods:1013:Flask of Crimson Tears +6, goods:1014:Flask of Crimson Tears +7, goods:1015:Flask of Crimson Tears +7, goods:1016:Flask of Crimson Tears +8, goods:1017:Flask of Crimson Tears +8, goods:1018:Flask of Crimson Tears +9, goods:1019:Flask of Crimson Tears +9, goods:1020:Flask of Crimson Tears +10, goods:1021:Flask of Crimson Tears +10, goods:1022:Flask of Crimson Tears +11, goods:1023:Flask of Crimson Tears +11, goods:1024:Flask of Crimson Tears +12, goods:1025:Flask of Crimson Tears +12
    call = t000001000_x17(goods3=goods5, goods6=0, z31=1)
    if call.Get() == 0:
        """State 2,8"""
        # action:13040150:"No Flask of Crimson Tears in inventory"
        assert t000001000_x4(action1=13040150)
    elif call.Done():
        """State 1,7,12"""
        # goods:1050:Flask of Cerulean Tears, goods:1051:Flask of Cerulean Tears, goods:1052:Flask of Cerulean Tears +1, goods:1053:Flask of Cerulean Tears +1, goods:1054:Flask of Cerulean Tears +2, goods:1055:Flask of Cerulean Tears +2, goods:1056:Flask of Cerulean Tears +3, goods:1057:Flask of Cerulean Tears +3, goods:1058:Flask of Cerulean Tears +4, goods:1059:Flask of Cerulean Tears +4, goods:1060:Flask of Cerulean Tears +5, goods:1061:Flask of Cerulean Tears +5, goods:1062:Flask of Cerulean Tears +6, goods:1063:Flask of Cerulean Tears +6, goods:1064:Flask of Cerulean Tears +7, goods:1065:Flask of Cerulean Tears +7, goods:1066:Flask of Cerulean Tears +8, goods:1067:Flask of Cerulean Tears +8, goods:1068:Flask of Cerulean Tears +9, goods:1069:Flask of Cerulean Tears +9, goods:1070:Flask of Cerulean Tears +10, goods:1071:Flask of Cerulean Tears +10, goods:1072:Flask of Cerulean Tears +11, goods:1073:Flask of Cerulean Tears +11, goods:1074:Flask of Cerulean Tears +12, goods:1075:Flask of Cerulean Tears +12
        call = t000001000_x17(goods3=goods5, goods6=1, z31=1)
        if call.Get() == 0:
            """State 6,11"""
            # action:13040160:"No Flask of Cerulean Tears in inventory"
            assert t000001000_x4(action1=13040160)
        elif call.Done():
            """State 5,3"""
            OpenEstusAllotMenu()
            assert not (CheckSpecificPersonMenuIsOpen(14, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 9"""
            assert t000001000_x16(goods5=goods5)
    """State 13"""
    return 0

def t000001000_x16(goods5=1000):
    """State 0,3"""
    # goods:1000:Flask of Crimson Tears, goods:1001:Flask of Crimson Tears, goods:1002:Flask of Crimson Tears +1, goods:1003:Flask of Crimson Tears +1, goods:1004:Flask of Crimson Tears +2, goods:1005:Flask of Crimson Tears +2, goods:1006:Flask of Crimson Tears +3, goods:1007:Flask of Crimson Tears +3, goods:1008:Flask of Crimson Tears +4, goods:1009:Flask of Crimson Tears +4, goods:1010:Flask of Crimson Tears +5, goods:1011:Flask of Crimson Tears +5, goods:1012:Flask of Crimson Tears +6, goods:1013:Flask of Crimson Tears +6, goods:1014:Flask of Crimson Tears +7, goods:1015:Flask of Crimson Tears +7, goods:1016:Flask of Crimson Tears +8, goods:1017:Flask of Crimson Tears +8, goods:1018:Flask of Crimson Tears +9, goods:1019:Flask of Crimson Tears +9, goods:1020:Flask of Crimson Tears +10, goods:1021:Flask of Crimson Tears +10, goods:1022:Flask of Crimson Tears +11, goods:1023:Flask of Crimson Tears +11, goods:1024:Flask of Crimson Tears +12, goods:1025:Flask of Crimson Tears +12
    call = t000001000_x17(goods3=goods5, goods6=0, z31=1)
    if call.Get() == 1:
        """State 4"""
        assert t000001000_x18(goods5=goods5, mode1=0, z30=GetWorkValue(1))
        """State 5"""
        assert t000001000_x18(goods5=goods5, mode1=1, z30=GetWorkValue(1))
    elif call.Done():
        """State 1"""
        pass
    """State 2"""
    SetWorkValue(1, 0)
    """State 6"""
    return 0

def t000001000_x17(goods3=1000, goods6=_, z31=1):
    """State 0,13"""
    SetWorkValue(z31, 0)
    if (DoesPlayerHaveItem(3, goods3 + 0 + goods6 * 50 + 0 * 2) == 1 or DoesPlayerHaveItem(3, goods3
        + 1 + goods6 * 50 + 0 * 2) == 1):
        """State 1"""
        SetWorkValue(z31, 0)
    elif (DoesPlayerHaveItem(3, goods3 + 0 + goods6 * 50 + 1 * 2) == 1 or DoesPlayerHaveItem(3, goods3
          + 1 + goods6 * 50 + 1 * 2) == 1):
        """State 2"""
        SetWorkValue(z31, 1)
    elif (DoesPlayerHaveItem(3, goods3 + 0 + goods6 * 50 + 2 * 2) == 1 or DoesPlayerHaveItem(3, goods3
          + 1 + goods6 * 50 + 2 * 2) == 1):
        """State 3"""
        SetWorkValue(z31, 2)
    elif (DoesPlayerHaveItem(3, goods3 + 0 + goods6 * 50 + 3 * 2) == 1 or DoesPlayerHaveItem(3, goods3
          + 1 + goods6 * 50 + 3 * 2) == 1):
        """State 4"""
        SetWorkValue(z31, 3)
    elif (DoesPlayerHaveItem(3, goods3 + 0 + goods6 * 50 + 4 * 2) == 1 or DoesPlayerHaveItem(3, goods3
          + 1 + goods6 * 50 + 4 * 2) == 1):
        """State 5"""
        SetWorkValue(z31, 4)
    elif (DoesPlayerHaveItem(3, goods3 + 0 + goods6 * 50 + 5 * 2) == 1 or DoesPlayerHaveItem(3, goods3
          + 1 + goods6 * 50 + 5 * 2) == 1):
        """State 6"""
        SetWorkValue(z31, 5)
    elif (DoesPlayerHaveItem(3, goods3 + 0 + goods6 * 50 + 6 * 2) == 1 or DoesPlayerHaveItem(3, goods3
          + 1 + goods6 * 50 + 6 * 2) == 1):
        """State 7"""
        SetWorkValue(z31, 6)
    elif (DoesPlayerHaveItem(3, goods3 + 0 + goods6 * 50 + 7 * 2) == 1 or DoesPlayerHaveItem(3, goods3
          + 1 + goods6 * 50 + 7 * 2) == 1):
        """State 8"""
        SetWorkValue(z31, 7)
    elif (DoesPlayerHaveItem(3, goods3 + 0 + goods6 * 50 + 8 * 2) == 1 or DoesPlayerHaveItem(3, goods3
          + 1 + goods6 * 50 + 8 * 2) == 1):
        """State 9"""
        SetWorkValue(z31, 8)
    elif (DoesPlayerHaveItem(3, goods3 + 0 + goods6 * 50 + 9 * 2) == 1 or DoesPlayerHaveItem(3, goods3
          + 1 + goods6 * 50 + 9 * 2) == 1):
        """State 10"""
        SetWorkValue(z31, 9)
    elif (DoesPlayerHaveItem(3, goods3 + 0 + goods6 * 50 + 10 * 2) == 1 or DoesPlayerHaveItem(3, goods3
          + 1 + goods6 * 50 + 10 * 2) == 1):
        """State 11"""
        SetWorkValue(z31, 10)
    elif (DoesPlayerHaveItem(3, goods3 + 0 + goods6 * 50 + 11 * 2) == 1 or DoesPlayerHaveItem(3, goods3
          + 1 + goods6 * 50 + 11 * 2) == 1):
        """State 14"""
        SetWorkValue(z31, 11)
    elif (DoesPlayerHaveItem(3, goods3 + 0 + goods6 * 50 + 12 * 2) == 1 or DoesPlayerHaveItem(3, goods3
          + 1 + goods6 * 50 + 12 * 2) == 1):
        """State 15"""
        SetWorkValue(z31, 12)
    else:
        """State 12"""
        SetWorkValue(z31, 13)
        """State 16"""
        return 0
    """State 17"""
    return 1

def t000001000_x18(goods5=1000, mode1=_, z30=_):
    """State 0,6"""
    if not GetEstusAllocation(mode1) < 0:
        """State 7,12"""
        if (DoesPlayerHaveItem(3, goods5 + 0 + mode1 * 50 + z30 * 2) == 1 or DoesPlayerHaveItem(3, goods5
            + 1 + mode1 * 50 + z30 * 2) == 1):
            """State 13,1"""
            if DoesPlayerHaveItem(3, goods5 + 0 + mode1 * 50 + z30 * 2) == 1:
                """State 2,4"""
                ReplaceTool(1000 + mode1 * 50 + z30 * 2 + 0, 1000 + mode1 * 50 + z30 * 2 + 1, 1)
            else:
                """State 3"""
                pass
            while True:
                """State 5"""
                if (0 == ComparePlayerInventoryNumber(3, 1000 + 1 + mode1 * 50 + z30 * 2, 4, GetEstusAllocation(mode1),
                    0)):
                    """State 9,11"""
                    PlayerEquipmentQuantityChange(3, 1000 + 1 + mode1 * 50 + z30 * 2, 1)
                else:
                    """State 10"""
                    break
        else:
            """State 14"""
            pass
    else:
        """State 8"""
        pass
    """State 15"""
    return 0

def t000001000_x19(goods3=1000):
    """State 0,3"""
    # goods:1000:Flask of Crimson Tears, goods:1001:Flask of Crimson Tears, goods:1002:Flask of Crimson Tears +1, goods:1003:Flask of Crimson Tears +1, goods:1004:Flask of Crimson Tears +2, goods:1005:Flask of Crimson Tears +2, goods:1006:Flask of Crimson Tears +3, goods:1007:Flask of Crimson Tears +3, goods:1008:Flask of Crimson Tears +4, goods:1009:Flask of Crimson Tears +4, goods:1010:Flask of Crimson Tears +5, goods:1011:Flask of Crimson Tears +5, goods:1012:Flask of Crimson Tears +6, goods:1013:Flask of Crimson Tears +6, goods:1014:Flask of Crimson Tears +7, goods:1015:Flask of Crimson Tears +7, goods:1016:Flask of Crimson Tears +8, goods:1017:Flask of Crimson Tears +8, goods:1018:Flask of Crimson Tears +9, goods:1019:Flask of Crimson Tears +9, goods:1020:Flask of Crimson Tears +10, goods:1021:Flask of Crimson Tears +10, goods:1022:Flask of Crimson Tears +11, goods:1023:Flask of Crimson Tears +11, goods:1024:Flask of Crimson Tears +12, goods:1025:Flask of Crimson Tears +12
    call = t000001000_x17(goods3=goods3, goods6=0, z31=1)
    if call.Get() == 1:
        """State 4"""
        assert t000001000_x20(goods3=goods3, z29=GetWorkValue(1))
        """State 2"""
        SetWorkValue(1, 0)
    elif call.Done():
        """State 1"""
        pass
    """State 5"""
    return 0

def t000001000_x20(goods3=1000, z29=_):
    """State 0,1"""
    ReplaceToolIf(DoesPlayerHaveItem(3, 1000 + 0 + 0 * 50 + z29 * 2) == 1, goods3 + 0 * 50 + z29 * 2 + 0,
                  goods3 + 0 * 50 + 0 + 2 * (GetTotalBonfireLevel() - 1), 1)
    """State 2"""
    ReplaceToolIf(DoesPlayerHaveItem(3, 1000 + 1 + 0 * 50 + z29 * 2) == 1, goods3 + 0 * 50 + z29 * 2 + 1,
                  goods3 + 0 * 50 + 1 + 2 * (GetTotalBonfireLevel() - 1), 1)
    """State 3"""
    ReplaceToolIf(DoesPlayerHaveItem(3, 1000 + 0 + 1 * 50 + z29 * 2) == 1, goods3 + 1 * 50 + z29 * 2 + 0,
                  goods3 + 1 * 50 + 0 + 2 * (GetTotalBonfireLevel() - 1), 1)
    """State 4"""
    ReplaceToolIf(DoesPlayerHaveItem(3, 1000 + 1 + 1 * 50 + z29 * 2) == 1, goods3 + 1 * 50 + z29 * 2 + 1,
                  goods3 + 1 * 50 + 1 + 2 * (GetTotalBonfireLevel() - 1), 1)
    """State 5"""
    return 0

def t000001000_x21(z18=1, z19=1, z20=2, z21=2, z22=3, z23=3, z24=4, z25=4, z26=5, z27=5, z28=1):
    """State 0"""
    if not GetWorkValue(z28):
        """State 1"""
        SetWorkValue(z28, z18)
    elif GetWorkValue(z28) == 1:
        """State 2"""
        SetWorkValue(z28, z19)
    elif GetWorkValue(z28) == 2:
        """State 3"""
        SetWorkValue(z28, z20)
    elif GetWorkValue(z28) == 3:
        """State 4"""
        SetWorkValue(z28, z21)
    elif GetWorkValue(z28) == 4:
        """State 5"""
        SetWorkValue(z28, z22)
    elif GetWorkValue(z28) == 5:
        """State 6"""
        SetWorkValue(z28, z23)
    elif GetWorkValue(z28) == 6:
        """State 7"""
        SetWorkValue(z28, z24)
    elif GetWorkValue(z28) == 7:
        """State 8"""
        SetWorkValue(z28, z25)
    elif GetWorkValue(z28) == 8:
        """State 9"""
        SetWorkValue(z28, z26)
    elif GetWorkValue(z28) == 9:
        """State 10"""
        SetWorkValue(z28, z27)
    else:
        """State 11"""
        SetWorkValue(z28, 5)
    """State 12"""
    return 0

def t000001000_x22():
    """State 0"""
    if not GetEventFlag(9000):
        """State 3,1"""
        SetEventFlag(4652, 0)
        SetEventFlag(4653, 0)
        SetEventFlag(4654, 0)
        SetEventFlag(4655, 0)
        SetEventFlag(4656, 0)
        SetEventFlag(4657, 0)
        SetEventFlag(4651, 0)
    else:
        """State 2"""
        pass
    while True:
        """State 4"""
        if IsMultiplayerInProgress() == 1:
            """State 6"""
            call = t000001000_x25()
            assert not IsMultiplayerInProgress()
        elif GetEventFlag(1042369415) == 1:
            """State 7"""
            call = t000001000_x63()
            assert not GetEventFlag(1042369415)
        else:
            """State 5"""
            def WhilePaused():
                GiveSpEffectToPlayerIf(GetEventFlag(9000) == 1 and not GetWorkValue(0), 9607)
                GiveSpEffectToPlayerIf(GetEventFlag(9000) == 1 and GetWorkValue(0) == 10, 9608)
                GiveSpEffectToPlayerIf(GetEventFlag(9000) == 1 and GetDistanceToPlayer() < 1.05, 9609)
                GiveSpEffectToPlayerIf(GetEventFlag(4698) == 1 and GetEventFlag(9001) == 1, 9606)
            assert t000001000_x23()
    """Unused"""
    """State 8"""
    return 0

def t000001000_x23():
    """State 0,1"""
    if CompareBonfireLevel(5, 0) == 1 or GetEventFlag(11102790) == 1:
        """State 2"""
        Label('L0')
        assert GetWhetherChrEventAnimHasEnded(10000) == 1
    else:
        """State 3,30"""
        call = t000001000_x40()
        if call.Done():
            """State 7"""
            TurnCharacterToFaceEntity(-1, 10000, -1, -1)
            assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
            """State 4"""
            c1_40()
            assert CompareBonfireLevel(5, 0) == 1
            """State 9,10"""
            UpdatePlayerRespawnPoint()
            Goto('L0')
        elif CompareBonfireLevel(5, 0) == 1 or GetEventFlag(11102790) == 1:
            pass
    """State 31"""
    call = t000001000_x40()
    if call.Done():
        """State 5"""
        ClearPlayerDamageInfo()
        """State 11"""
        GiveSpEffectToPlayer(202)
        """State 6"""
        SetTalkTime(1)
        """State 35"""
        assert t000001000_x67()
        """State 23"""
        SetEventFlag(4698, 0)
        SetEventFlagIf(DoesSelfHaveSpEffect(9680) == 1 and not GetEventFlag(953), 4698, 1)
        SetEventFlagIf(GetEventFlagValue(955, 3) > 2 and DoesSelfHaveSpEffect(9681) == 1 and not GetEventFlag(953),
                       4698, 1)
        """State 28"""
        assert t000001000_x32()
        """State 8"""
        TurnCharacterToFaceEntity(-1, 10000, -1, -1)
        assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
        """State 12"""
        UpdatePlayerRespawnPoint()
        """State 19"""
        StartBonfireAnimLoop(1, 1, 1, 1, GetWorkValue(0), 0.5)
        """State 13"""
        c1_117(0, 0, 0, 0, 0, 0, 0, 0.1, 0, 1.5, 0, 0.75, 0.5)
        """State 18"""
        SetEventFlag(9000, 1)
        SetEventFlag(9020, 1)
        c5_138(not GetEventFlag(11102790), 1001000)
        c5_138(GetEventFlag(11102790) == 1, 1001001)
        if not GetEventFlag(4698):
            """State 34"""
            assert t000001000_x66()
        else:
            """State 33"""
            assert t000001000_x64()
        """State 17"""
        if not GetEventFlag(9001):
            """State 21"""
            pass
        else:
            """State 20"""
            assert not GetEventFlag(9001)
        """State 27"""
        assert t000001000_x30()
        """State 15"""
        if not GetEventFlag(4653):
            """State 22,37"""
            Label('L1')
            assert t000001000_x68()
            """State 29"""
            call = t000001000_x31()
            def WhilePaused():
                GiveSpEffectToPlayerIf(GetEventFlag(4651) == 1, 9620)
            def ExitPause():
                EndBonfireKindleAnimLoop(GetWorkValue(0))
            if call.Done():
                pass
            elif (((GetDistanceToPlayer() > 3 and not GetEventFlag(11102790)) or GetDistanceToPlayer()
                  > 7) and GetCurrentStateElapsedFrames() > 1):
                """State 26"""
                Label('L2')
                assert t000001000_x24()
            elif CompareBonfireState(0) and GetCurrentStateElapsedFrames() > 1:
                Goto('L2')
            elif HasPlayerBeenAttacked() == 1 and GetCurrentStateElapsedFrames() > 1:
                Goto('L2')
            elif IsMultiplayerInProgress() == 1 and GetCurrentStateElapsedFrames() > 1:
                Goto('L2')
            elif GetEventFlag(1042369415) == 1 and GetCurrentStateElapsedFrames() > 1:
                Goto('L2')
            elif (CompareBonfireLevel(0, 0) == 1 and not GetEventFlag(11102790) and GetCurrentStateElapsedFrames()
                  > 1):
                Goto('L2')
        else:
            """State 16,32"""
            call = t000001000_x50()
            if call.Done():
                Goto('L1')
            elif GetEventFlag(1042369415) == 1 and GetCurrentStateElapsedFrames() > 1:
                """State 24"""
                Label('L3')
                def ExitPause():
                    EndBonfireKindleAnimLoop(GetWorkValue(0))
                Goto('L2')
            elif IsMultiplayerInProgress() == 1 and GetCurrentStateElapsedFrames() > 1:
                Goto('L3')
            elif HasPlayerBeenAttacked() == 1 and GetCurrentStateElapsedFrames() > 1:
                Goto('L3')
            elif (((GetDistanceToPlayer() > 3 and not GetEventFlag(11102790)) or GetDistanceToPlayer()
                  > 7) and GetCurrentStateElapsedFrames() > 1):
                Goto('L3')
            elif CompareBonfireState(0) and GetCurrentStateElapsedFrames() > 1:
                Goto('L3')
        """State 36"""
        assert t000001000_x67()
        """State 14"""
        SetEventFlag(9000, 0)
        SetEventFlag(9020, 0)
        c1_138(-1)
        c1_140(0)
        assert GetCurrentStateElapsedFrames() > 1
        """State 25"""
        if not IsMultiplayerInProgress() and not GetEventFlag(1042369415):
            Goto('L0')
        else:
            pass
    elif (IsMultiplayerInProgress() == 1 or GetEventFlag(1042369415) == 1 or (CompareBonfireLevel(0,
          0) == 1 and not GetEventFlag(11102790))):
        pass
    """State 38"""
    return 0

def t000001000_x24():
    """State 0,1"""
    assert t000001000_x1()
    """State 2"""
    return 0

def t000001000_x25():
    """State 0"""
    while True:
        """State 1"""
        call = t000001000_x26()
        assert IsClientPlayer() == 1
        """State 2"""
        call = t000001000_x27()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t000001000_x26():
    """State 0,6"""
    call = t000001000_x1()
    if call.Done() and CompareBonfireLevel(5, 0) == 1:
        pass
    elif call.Done():
        """State 2,7"""
        # actionbutton:6100:"Touch grace"
        call = t000001000_x3(actionbutton1=6100, flag3=6001, flag4=6000)
        if call.Done():
            """State 4"""
            TurnCharacterToFaceEntity(-1, 10000, -1, -1)
            assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
            """State 3"""
            c1_40()
            """State 5"""
            UpdatePlayerRespawnPoint()
            assert CompareBonfireLevel(5, 0) == 1
        elif CompareBonfireLevel(5, 0) == 1:
            pass
    """State 1"""
    Quit()
    """Unused"""
    """State 8"""
    return 0

def t000001000_x27():
    """State 0,1"""
    assert t000001000_x1()
    """State 2"""
    return 0

def t000001000_x28():
    """State 0,1"""
    if not GetEventFlag(4651):
        """State 3"""
        if GetEventFlag(4698) == 1:
            """State 5,10"""
            assert t000001000_x35(z13=20006, val4=0.5, z14=1, z15=2, z16=60)
        elif GetEventFlag(108) == 1:
            """State 9,13"""
            assert t000001000_x35(z13=20000, val4=3.5, z14=1, z15=2, z16=60)
        else:
            """State 4,6"""
            # eventflag:400001:lot:100010:Rold Medallion
            if not GetEventFlag(400001):
                """State 7,11"""
                assert t000001000_x35(z13=20000, val4=3.5, z14=1, z15=2, z16=60)
            else:
                """State 8,12"""
                assert t000001000_x35(z13=20001, val4=3.5, z14=1, z15=2, z16=60)
    else:
        """State 2"""
        pass
    """State 14"""
    return 0

def t000001000_x29(z17=_):
    """State 0,1"""
    c1_129(z17, 1.4)
    """State 2"""
    SetEventFlag(4651, 0)
    SetEventFlag(4652, 0)
    SetEventFlag(4653, 0)
    SetEventFlag(4654, 0)
    SetEventFlag(4655, 0)
    SetEventFlag(4656, 0)
    SetEventFlag(4657, 0)
    """State 3"""
    return 0

def t000001000_x30():
    """State 0"""
    if GetEventFlag(11102790) == 1:
        """State 3"""
        pass
    elif GetEventFlag(110) == 1:
        """State 1"""
        pass
    elif not GetEventFlag(953) or GetEventFlag(4698) == 1:
        """State 4"""
        assert t000001000_x59()
    elif not GetEventFlag(4680):
        """State 2"""
        pass
    elif GetEventFlag(108) == 1:
        """State 7"""
        assert t000001000_x62()
    # eventflag:400001:lot:100010:Rold Medallion
    elif GetEventFlag(11009260) == 1 and not GetEventFlag(400001):
        """State 6"""
        assert t000001000_x61()
    else:
        """State 5"""
        assert t000001000_x60()
    """State 8"""
    return 0

def t000001000_x31():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1 or not GetEventFlag(4651)
    """State 11"""
    assert not GetEventFlag(9001)
    
    """State 18"""
    # goods:1001:Flask of Crimson Tears, goods:1000:Flask of Crimson Tears, goods:1003:Flask of Crimson Tears +1, goods:1002:Flask of Crimson Tears +1, goods:1005:Flask of Crimson Tears +2, goods:1004:Flask of Crimson Tears +2, goods:1007:Flask of Crimson Tears +3, goods:1006:Flask of Crimson Tears +3, goods:1009:Flask of Crimson Tears +4, goods:1008:Flask of Crimson Tears +4, goods:1011:Flask of Crimson Tears +5, goods:1010:Flask of Crimson Tears +5, goods:1013:Flask of Crimson Tears +6, goods:1012:Flask of Crimson Tears +6, goods:1015:Flask of Crimson Tears +7, goods:1014:Flask of Crimson Tears +7, goods:1017:Flask of Crimson Tears +8, goods:1016:Flask of Crimson Tears +8, goods:1019:Flask of Crimson Tears +9, goods:1018:Flask of Crimson Tears +9, goods:1021:Flask of Crimson Tears +10, goods:1020:Flask of Crimson Tears +10, goods:1023:Flask of Crimson Tears +11, goods:1022:Flask of Crimson Tears +11, goods:1025:Flask of Crimson Tears +12, goods:1024:Flask of Crimson Tears +12, goods:1050:Flask of Cerulean Tears, goods:1051:Flask of Cerulean Tears, goods:1052:Flask of Cerulean Tears +1, goods:1053:Flask of Cerulean Tears +1, goods:1054:Flask of Cerulean Tears +2, goods:1055:Flask of Cerulean Tears +2, goods:1056:Flask of Cerulean Tears +3, goods:1057:Flask of Cerulean Tears +3, goods:1058:Flask of Cerulean Tears +4, goods:1059:Flask of Cerulean Tears +4, goods:1060:Flask of Cerulean Tears +5, goods:1061:Flask of Cerulean Tears +5, goods:1062:Flask of Cerulean Tears +6, goods:1063:Flask of Cerulean Tears +6, goods:1064:Flask of Cerulean Tears +7, goods:1065:Flask of Cerulean Tears +7, goods:1067:Flask of Cerulean Tears +8, goods:1066:Flask of Cerulean Tears +8, goods:1069:Flask of Cerulean Tears +9, goods:1068:Flask of Cerulean Tears +9
    assert t000001000_x8(goods7=1000)
    """State 5"""
    c1_110()
    while True:
        """State 1"""
        Label('L0')
        ClearTalkListData()
        """State 2"""
        # action:15000420:"Pass time"
        AddTalkListDataIf(not GetEventFlag(9411) or GetEventFlag(9412) == 1, 1, 15000420, -1)
        # action:15000540:"Level Up"
        AddTalkListDataIf(GetEventFlag(4680) == 1 or GetEventFlag(4699) == 1, 2, 15000540, -1)
        """State 29"""
        assert t000001000_x71(z1=3, z2=15000371)
        """State 17"""
        # action:15000390:"Memorize spell"
        AddTalkListData(4, 15000390, -1)
        # goods:250:Flask of Wondrous Physick, goods:251:Flask of Wondrous Physick, action:15000510:"Mix Wondrous Physick"
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 250, 2, 0, 0) == 1 or ComparePlayerInventoryNumber(3, 251, 2, 0, 0) == 1,
                          5, 15000510, -1)
        # action:15000395:"Sort chest"
        AddTalkListData(6, 15000395, -1)
        # action:15000520:"Great Runes"
        AddTalkListDataIf(f230(15) == 1, 7, 15000520, -1)
        # goods:8590:Whetstone Knife, action:15000530:"Ashes of War"
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 8590, 4, 1, 0) == 1, 8, 15000530, -1)
        # goods:8163:Tailoring Tools, goods:8188:Golden Tailoring Tools, action:22230000:"Alter garments"
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 8163, 2, 0, 0) == 1 or ComparePlayerInventoryNumber(3, 8188, 2, 0, 0) == 1,
                          9, 22230000, -1)
        """State 26"""
        assert t000001000_x52()
        """State 15"""
        
        # Time Manipulation
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 32001, 2, 0, 0) == 1, 80, 80101000, -1)
        
        # Weather Manipulation
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 32002, 2, 0, 0) == 1, 81, 80101100, -1)
        
        # action:20000009:"Leave"
        AddTalkListData(99, 20000009, -1)
        """State 6"""
        SetEventFlag(4652, 0)
        SetEventFlag(4656, 0)
        SetEventFlag(4654, 0)
        SetEventFlag(4655, 0)
        """State 3"""
        c1_140(1)
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 8"""
        if GetTalkListEntryResult() == 1:
            """State 19"""
            c1_140(0)
            c1_110()
            def ExitPause():
                c1_110()
            assert t000001000_x33()
        elif GetTalkListEntryResult() == 2:
            """State 20"""
            assert t000001000_x34()
        elif GetTalkListEntryResult() == 3:
            """State 25"""
            c1_140(0)
            c1_110()
            def ExitPause():
                c1_110()
            assert t000001000_x47()
        elif GetTalkListEntryResult() == 4:
            """State 7"""
            OpenMagicEquip(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(11, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 5:
            """State 12"""
            OpenPhysickMenu()
            assert not (CheckSpecificPersonMenuIsOpen(21, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 6:
            """State 9"""
            OpenRepository()
            assert not (CheckSpecificPersonMenuIsOpen(3, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 7:
            """State 13"""
            c1_137()
            assert not (CheckSpecificPersonMenuIsOpen(24, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 8:
            """State 14"""
            OpenEquipmentChangeOfPurposeShop()
            assert not (CheckSpecificPersonMenuIsOpen(7, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 9:
            """State 16"""
            OpenTailoringShop(111000, 111399)
            assert not (CheckSpecificPersonMenuIsOpen(26, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 11:
            """State 21"""
            assert t000001000_x36(z12=4655)
        elif GetTalkListEntryResult() == 12:
            """State 28"""
            assert t000001000_x36(z12=4657)
        elif GetTalkListEntryResult() == 15:
            """State 27"""
            assert t000001000_x54()
        elif GetTalkListEntryResult() == 32:
            """State 23"""
            assert t000001000_x38()
        # Time Manipulation
        elif GetTalkListEntryResult() == 80:
            assert t000001000_x80()
        # Weather Manipulation
        elif GetTalkListEntryResult() == 81:
            assert t000001000_x81()
        elif GetTalkListEntryResult() == 41 and GetEventFlag(120) == 1 and GetEventFlag(11102790) == 1:
            """State 24"""
            assert t000001000_x42()
        else:
            """State 4,30"""
            return 0
    """Unused"""
    """State 22"""
    assert t000001000_x37()
    Goto('L0')

def t000001000_x32():
    """State 0,1"""
    if GetEventFlag(1054532702) == 1:
        """State 2,4"""
        Label('L0')
        """State 3"""
        SetWorkValue(0, 0)
    elif GetEventFlag(4698) == 1:
        """State 8"""
        Goto('L0')
    elif GetEventFlag(11102790) == 1:
        """State 6,7"""
        SetWorkValue(0, 30)
    else:
        """State 5,9"""
        assert t000001000_x39()
    """State 10"""
    return 0

def t000001000_x33():
    """State 0,5"""
    CloseShopMessage()
    while True:
        """State 1"""
        ClearTalkListData()
        """State 2"""
        # action:15000430:"Until morning"
        AddTalkListData(1, 15000430, -1)
        # action:15000440:"Until noon"
        AddTalkListData(2, 15000440, -1)
        # action:15000450:"Until nightfall"
        AddTalkListData(3, 15000450, -1)
        # action:15000460:"Cancel"
        AddTalkListData(99, 15000460, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 6"""
        if GetTalkListEntryResult() == 1:
            """State 7"""
            def ExitPause():
                c1_133(0.5)
            assert t000001000_x45(val2=0)
        elif GetTalkListEntryResult() == 2:
            """State 8"""
            def ExitPause():
                c1_133(0.5)
            assert t000001000_x45(val2=1)
        elif GetTalkListEntryResult() == 3:
            """State 9"""
            def ExitPause():
                c1_133(0.5)
            assert t000001000_x45(val2=2)
        else:
            """State 4,10"""
            return 0

def t000001000_x34():
    """State 0"""
    if not GetEventFlag(4651):
        """State 3,4"""
        OpenSoul()
        assert not (CheckSpecificPersonMenuIsOpen(10, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    else:
        """State 2,1"""
        SetEventFlag(4652, 1)
        SetEventFlag(4656, 1)
        """State 5"""
        assert not GetEventFlag(4652)
        """State 6"""
        SetWorkValue(0, 0)
    """State 7"""
    return 0

def t000001000_x35(z13=_, val4=_, z14=1, z15=2, z16=60):
    """State 0,4"""
    assert not DoesPlayerHaveSpEffect(9600) and not DoesPlayerHaveSpEffect(9603)
    """State 1"""
    c1_128(2180, 21800000, 1, 3000, z13, z14, z15, z16)
    """State 2"""
    SetEventFlag(4651, 1)
    """State 3"""
    assert GetCurrentStateElapsedTime() > val4
    """State 5"""
    return 0

def t000001000_x36(z12=_):
    """State 0"""
    if not GetEventFlag(4651):
        """State 1,8"""
        assert t000001000_x28()
    else:
        """State 4"""
        pass
    """State 3"""
    SetEventFlag(4652, 1)
    SetEventFlag(z12, 1)
    """State 2"""
    assert (not GetEventFlag(4652) or (GetCurrentStateElapsedTime() > 5 and not DoesPlayerHaveSpEffect(9600)
            and not DoesPlayerHaveSpEffect(9603)))
    """State 5"""
    if not GetEventFlag(4680):
        """State 6,9"""
        assert t000001000_x29(z17=20010)
    else:
        """State 7"""
        pass
    """State 10"""
    return 0

def t000001000_x37():
    """State 0,1"""
    SetEventFlag(1054539200, 1)
    """State 4"""
    assert t000001000_x28()
    """State 2"""
    SetEventFlag(4652, 1)
    """State 3"""
    assert not GetEventFlag(4652)
    """State 5"""
    return 0

def t000001000_x38():
    """State 0,1"""
    SetEventFlag(1054539201, 1)
    """State 2"""
    SetEventFlag(1054539205, 1)
    """State 3"""
    assert GetCurrentStateElapsedTime() > 1.5
    """State 5"""
    SetEventFlag(9000, 0)
    SetEventFlag(9020, 0)
    """State 4"""
    c1_138(-1)
    Quit()
    """Unused"""
    """State 6"""
    return 0

def t000001000_x39():
    """State 0,1"""
    if not CompareRNGValue(0, 0) != -1:
        """State 3,4"""
        ShuffleRNGSeed(100)
    else:
        """State 2"""
        pass
    """State 5"""
    SetRNGSeed()
    """State 6"""
    if CompareRNGValue(3, 69) == 1:
        """State 7,8"""
        SetWorkValue(0, 0)
    elif CompareRNGValue(3, 99) == 1:
        """State 9,10"""
        SetWorkValue(0, 10)
    else:
        """State 11,12"""
        SetWorkValue(0, 0)
    """State 13"""
    return 0

def t000001000_x40():
    """State 0"""
    while True:
        """State 1"""
        if GetEventFlag(1054532702) == 1:
            """State 2,7"""
            # actionbutton:6100:"Touch grace", actionbutton:6101:"Rest at site of grace"
            call = t000001000_x65(actionbutton1=6100, actionbutton2=6101, val1=45, z7=-120)
            if call.Done():
                break
            elif not GetEventFlag(1054532702):
                pass
        elif GetEventFlag(11102790) == 1:
            """State 4,6"""
            # actionbutton:6102:"Rest at table of lost grace", actionbutton:6103:"Rest at table of lost grace"
            call = t000001000_x44(actionbutton3=6102, actionbutton4=6103, val3=45)
            if call.Done():
                break
            elif not GetEventFlag(11102790):
                pass
        else:
            """State 3,5"""
            # actionbutton:6100:"Touch grace", actionbutton:6101:"Rest at site of grace"
            call = t000001000_x41(actionbutton1=6100, actionbutton2=6101)
            if call.Done():
                break
            elif GetEventFlag(1054532702) == 1 or GetEventFlag(11102790) == 1:
                pass
    """State 8"""
    return 0

def t000001000_x41(actionbutton1=_, actionbutton2=_):
    """State 0,1"""
    if CompareBonfireLevel(0, 0) == 1:
        """State 2,4"""
        assert t000001000_x3(actionbutton1=actionbutton1, flag3=6001, flag4=6000)
    else:
        """State 3,5"""
        assert t000001000_x3(actionbutton1=actionbutton2, flag3=6001, flag4=6000)
    """State 6"""
    return 0

def t000001000_x42():
    """State 0,7"""
    # action:20011080:"Begin Journey <?nextLoopCount?>?"
    call = t000001000_x0(action2=20011080)
    if call.Get() == 0:
        """State 2,8"""
        # action:20011081:"If you begin Journey <?nextLoopCount?>, you will not be able\nto return to the present world of Journey <?loopCount?>.\nBegin Journey <?nextLoopCount?>?"
        call = t000001000_x0(action2=20011081)
        if call.Get() == 0:
            """State 3,5"""
            SetEventFlag(3001, 1)
            """State 6"""
            Quit()
        elif call.Done():
            """State 4"""
            pass
    elif call.Done():
        """State 1"""
        pass
    """State 9"""
    return 0

def t000001000_x43(z8=11, z9=12):
    """State 0,2"""
    SetEventFlag(1042379200, 0)
    SetEventFlag(1042379202, 0)
    SetEventFlag(1042379206, 0)
    SetEventFlag(1046389201, 0)
    SetEventFlag(1043349250, 0)
    SetEventFlag(1038509250, 0)
    SetEventFlag(1043539250, 0)
    SetEventFlag(11009255, 0)
    SetEventFlag(1043509200, 0)
    SetEventFlag(1054559200, 0)
    SetEventFlag(1036489250, 0)
    SetEventFlag(1039519250, 0)
    SetEventFlag(1037519200, 0)
    SetEventFlag(10009656, 0)
    SetEventFlag(11009270, 0)
    SetEventFlag(11009275, 0)
    SetEventFlag(1054539210, 0)
    SetEventFlag(35009350, 0)
    SetEventFlag(35009352, 0)
    SetEventFlag(1054539215, 0)
    """State 4"""
    SetEventFlag(1042379208, 0)
    SetEventFlag(11009265, 0)
    SetEventFlag(35009355, 0)
    SetEventFlag(35009358, 0)
    if not GetEventFlag(953):
        """State 1"""
        if not GetEventFlag(4699):
            pass
        else:
            """State 8"""
            assert t000001000_x46(z9=z8)
    elif GetEventFlag(11102790) == 1:
        """State 3"""
        pass
    # eventflag:400001:lot:100010:Rold Medallion
    elif GetEventFlag(11009260) == 1 and not GetEventFlag(400001):
        """State 5"""
        pass
    elif GetEventFlag(108) == 1:
        """State 7"""
        pass
    elif GetEventFlag(110) == 1:
        """State 6"""
        pass
    else:
        """State 9"""
        assert t000001000_x49(z8=z8, z9=z9)
    """State 10"""
    return 0

def t000001000_x44(actionbutton3=6102, actionbutton4=6103, val3=45):
    """State 0"""
    if GetRelativeAngleBetweenPlayerAndSelf() < val3:
        """State 1"""
        Label('L0')
        """State 3"""
        call = t000001000_x41(actionbutton1=actionbutton3, actionbutton2=actionbutton4)
        if call.Done():
            """State 4"""
            return 0
        elif not GetRelativeAngleBetweenPlayerAndSelf() < val3:
            pass
    else:
        pass
    """State 2"""
    assert GetRelativeAngleBetweenPlayerAndSelf() < val3
    Goto('L0')

def t000001000_x45(val2=_):
    """State 0,8"""
    assert t000001000_x13()
    """State 4"""
    if not val2:
        """State 1"""
        c1_132(2)
        c1_134(0, 0, 0, 0, f219(), f220(), f221(), 2.5, 0.75, 2, 0, 0.75, 0.5)
    elif val2 == 1:
        """State 2"""
        c1_132(2)
        c1_134(0, 0, 0, 0, f222(), f223(), f224(), 2.5, 0.75, 2, 0, 0.75, 0.5)
    elif val2 == 2:
        """State 3"""
        c1_132(2)
        c1_134(0, 0, 0, 0, f225(), f226(), f227(), 2.5, 0.75, 2, 0, 0.75, 0.5)
    """State 5"""
    assert GetCurrentStateElapsedTime() > 0.8
    """State 9"""
    assert t000001000_x29(z17=0)
    """State 6"""
    assert not f233()
    """State 7"""
    assert GetCurrentStateElapsedTime() > 2.5
    """State 10"""
    return 0

def t000001000_x46(z9=_):
    """State 0,1"""
    # action:99990301:"Speak with Merina"
    AddTalkListData(z9, 99990301, -1)
    """State 2"""
    return 0

def t000001000_x47():
    """State 0,10"""
    assert t000001000_x48()
    """State 5"""
    CloseShopMessage()
    while True:
        """State 1"""
        ClearTalkListData()
        """State 11"""
        assert t000001000_x69(z5=1, z6=15000370)
        """State 12"""
        assert t000001000_x70(z3=2, z4=15000380)
        """State 2"""
        # action:15000385:"Allocate flask charges"
        AddTalkListData(3, 15000385, -1)
        # action:15000372:"Cancel"
        AddTalkListData(99, 15000372, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 6"""
        if GetTalkListEntryResult() == 1:
            """State 7"""
            # goods:1000:Flask of Crimson Tears, goods:1001:Flask of Crimson Tears, goods:1002:Flask of Crimson Tears +1, goods:1003:Flask of Crimson Tears +1, goods:1004:Flask of Crimson Tears +2, goods:1005:Flask of Crimson Tears +2, goods:1006:Flask of Crimson Tears +3, goods:1007:Flask of Crimson Tears +3, goods:1008:Flask of Crimson Tears +4, goods:1009:Flask of Crimson Tears +4, goods:1010:Flask of Crimson Tears +5, goods:1011:Flask of Crimson Tears +5, goods:1012:Flask of Crimson Tears +6, goods:1013:Flask of Crimson Tears +6, goods:1014:Flask of Crimson Tears +7, goods:1015:Flask of Crimson Tears +7, goods:1016:Flask of Crimson Tears +8, goods:1017:Flask of Crimson Tears +8, goods:1018:Flask of Crimson Tears +9, goods:1019:Flask of Crimson Tears +9, goods:1020:Flask of Crimson Tears +10, goods:1021:Flask of Crimson Tears +10, goods:1022:Flask of Crimson Tears +11, goods:1023:Flask of Crimson Tears +11, goods:1024:Flask of Crimson Tears +12, goods:1025:Flask of Crimson Tears +12, goods:10010:Golden Seed
            assert t000001000_x7(goods1=1000, goods2=10010)
        elif GetTalkListEntryResult() == 2:
            """State 8"""
            # goods:1000:Flask of Crimson Tears, goods:1001:Flask of Crimson Tears, goods:1002:Flask of Crimson Tears +1, goods:1003:Flask of Crimson Tears +1, goods:1004:Flask of Crimson Tears +2, goods:1005:Flask of Crimson Tears +2, goods:1006:Flask of Crimson Tears +3, goods:1007:Flask of Crimson Tears +3, goods:1008:Flask of Crimson Tears +4, goods:1009:Flask of Crimson Tears +4, goods:1010:Flask of Crimson Tears +5, goods:1011:Flask of Crimson Tears +5, goods:1012:Flask of Crimson Tears +6, goods:1013:Flask of Crimson Tears +6, goods:1014:Flask of Crimson Tears +7, goods:1015:Flask of Crimson Tears +7, goods:1016:Flask of Crimson Tears +8, goods:1017:Flask of Crimson Tears +8, goods:1018:Flask of Crimson Tears +9, goods:1019:Flask of Crimson Tears +9, goods:1020:Flask of Crimson Tears +10, goods:1021:Flask of Crimson Tears +10, goods:1022:Flask of Crimson Tears +11, goods:1023:Flask of Crimson Tears +11, goods:1024:Flask of Crimson Tears +12, goods:1025:Flask of Crimson Tears +12, goods:10020:Sacred Tear
            assert t000001000_x6(goods3=1000, goods4=10020)
        elif GetTalkListEntryResult() == 3:
            """State 9"""
            # goods:1000:Flask of Crimson Tears, goods:1050:Flask of Cerulean Tears, goods:1001:Flask of Crimson Tears, goods:1051:Flask of Cerulean Tears, goods:1002:Flask of Crimson Tears +1, goods:1052:Flask of Cerulean Tears +1, goods:1003:Flask of Crimson Tears +1, goods:1053:Flask of Cerulean Tears +1, goods:1004:Flask of Crimson Tears +2, goods:1054:Flask of Cerulean Tears +2, goods:1005:Flask of Crimson Tears +2, goods:1055:Flask of Cerulean Tears +2, goods:1006:Flask of Crimson Tears +3, goods:1056:Flask of Cerulean Tears +3, goods:1007:Flask of Crimson Tears +3, goods:1057:Flask of Cerulean Tears +3, goods:1008:Flask of Crimson Tears +4, goods:1058:Flask of Cerulean Tears +4, goods:1009:Flask of Crimson Tears +4, goods:1059:Flask of Cerulean Tears +4, goods:1010:Flask of Crimson Tears +5, goods:1060:Flask of Cerulean Tears +5, goods:1011:Flask of Crimson Tears +5, goods:1061:Flask of Cerulean Tears +5, goods:1012:Flask of Crimson Tears +6, goods:1062:Flask of Cerulean Tears +6, goods:1013:Flask of Crimson Tears +6, goods:1063:Flask of Cerulean Tears +6, goods:1014:Flask of Crimson Tears +7, goods:1064:Flask of Cerulean Tears +7, goods:1015:Flask of Crimson Tears +7, goods:1065:Flask of Cerulean Tears +7, goods:1016:Flask of Crimson Tears +8, goods:1066:Flask of Cerulean Tears +8, goods:1017:Flask of Crimson Tears +8, goods:1067:Flask of Cerulean Tears +8, goods:1018:Flask of Crimson Tears +9, goods:1068:Flask of Cerulean Tears +9, goods:1019:Flask of Crimson Tears +9, goods:1069:Flask of Cerulean Tears +9, goods:1020:Flask of Crimson Tears +10, goods:1070:Flask of Cerulean Tears +10, goods:1021:Flask of Crimson Tears +10, goods:1071:Flask of Cerulean Tears +10, goods:1022:Flask of Crimson Tears +11, goods:1072:Flask of Cerulean Tears +11, goods:1023:Flask of Crimson Tears +11, goods:1073:Flask of Cerulean Tears +11, goods:1024:Flask of Crimson Tears +12, goods:1074:Flask of Cerulean Tears +12, goods:1025:Flask of Crimson Tears +12, goods:1075:Flask of Cerulean Tears +12
            assert t000001000_x15(goods5=1000)
        else:
            """State 4,13"""
            return 0

def t000001000_x48():
    """State 0"""
    if not GetEventFlag(720070) or not GetEventFlag(720080):
        """State 1,3"""
        SetEventFlag(720070, 1)
        SetEventFlag(720080, 1)
        """State 4"""
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t000001000_x49(z8=11, z9=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 1"""
    assert t000001000_x57(z8=z8)
    """State 2"""
    assert t000001000_x58(z9=z9)
    """State 3"""
    return 0

def t000001000_x50():
    """State 0,9"""
    assert t000001000_x28()
    """State 7"""
    SetEventFlag(4652, 1)
    """State 4"""
    assert (not GetEventFlag(4652) or (GetCurrentStateElapsedTime() > 5 and not DoesPlayerHaveSpEffect(9600)
            and not DoesPlayerHaveSpEffect(9603)))
    """State 1"""
    if not GetEventFlag(4680):
        """State 2,8"""
        Label('L0')
        assert t000001000_x29(z17=20010) and GetCurrentStateElapsedTime() > 3
    elif GetEventFlag(108) == 1:
        """State 6"""
        Goto('L0')
    # eventflag:400001:lot:100010:Rold Medallion
    elif GetEventFlag(11009260) == 1 and not GetEventFlag(400001):
        """State 5"""
        Goto('L0')
    else:
        """State 3"""
        pass
    """State 10"""
    return 0

def t000001000_x51(z11=15):
    """State 0"""
    if not GetEventFlag(12019257):
        """State 1"""
        if not GetEventFlag(12019255):
            """State 5"""
            c1_149(z11, 21060900, -1, 0, 0)
        elif not GetEventFlag(12019256):
            """State 6"""
            c1_149(z11, 21060901, -1, 0, 0)
        else:
            """State 7"""
            c1_149(z11, 21060902, -1, 0, 0)
    elif not GetEventFlag(12019260):
        """State 2"""
        if not GetEventFlag(12012711):
            """State 8"""
            c5_149(not GetEventFlag(12019258), z11, 21060903, -1, 0, 0)
            c5_149(GetEventFlag(12019258) == 1, z11, 21060903, -1, 0, 0)
        elif GetEventFlag(1045379208) == 1:
            """State 9"""
            c1_149(z11, 21060910, -1, 0, 1)
        else:
            """State 13"""
            c1_149(z11, 21060911, -1, 0, 1)
    elif not GetEventFlag(12019265):
        """State 3"""
        if not GetEventFlag(12012712) or not GetEventFlag(1045379208):
            """State 10"""
            c5_149(not GetEventFlag(12019261), z11, 21060912, -1, 0, 0)
            c5_149(GetEventFlag(12019261) == 1, z11, 21060912, -1, 0, 0)
        else:
            """State 11"""
            c1_149(z11, 21060920, -1, 0, 1)
    else:
        """State 4,12"""
        c5_149(not GetEventFlag(12019266), z11, 21060921, -1, 0, 1)
        c5_149(GetEventFlag(12019266) == 1, z11, 21060921, -1, 0, 0)
    """State 14"""
    return 0

def t000001000_x52():
    """State 0"""
    # eventflag:400394:lot:103940:Miniature Ranni
    if (GetEventFlag(400394) == 1 and not GetEventFlag(12019280) and (GetEventFlag(12012710) == 1 or
        GetEventFlag(12012711) == 1 or GetEventFlag(12012712) == 1)):
        """State 4"""
        assert t000001000_x51(z11=15)
    # eventflag:400394:lot:103940:Miniature Ranni
    elif GetEventFlag(400394) == 1 and GetEventFlag(1034509406) == 1 and GetEventFlag(12012713) == 1:
        """State 5"""
        assert t000001000_x53(z10=15)
    else:
        """State 3"""
        assert t000001000_x43(z8=11, z9=12)
    """State 1"""
    c5_149(GetEventFlag(1054532702) == 1 and GetEventFlag(108) == 1 and not GetEventFlag(110), 32, 20010101,
           -1, 0, 1)
    # action:20010080:"Begin Journey <?nextLoopCount?>"
    AddTalkListDataIf(GetEventFlag(120) == 1 and GetEventFlag(11102790) == 1, 41, 20010080, -1)
    """State 6"""
    return 0
    """Unused"""
    """State 2"""
    Quit()

def t000001000_x53(z10=15):
    """State 0"""
    if not GetEventFlag(12019275):
        """State 1"""
        c1_149(z10, 21060930, -1, 0, 0)
    else:
        """State 2"""
        c5_149(not GetEventFlag(12019276), z10, 21060931, -1, 0, 0)
        c5_149(GetEventFlag(12019276) == 1, z10, 21060931, -1, 0, 0)
    """State 3"""
    return 0

def t000001000_x54():
    """State 0"""
    if not GetEventFlag(12012713):
        """State 1"""
        assert t000001000_x55()
    else:
        """State 2"""
        assert t000001000_x56()
    """State 3"""
    return 0

def t000001000_x55():
    """State 0"""
    if not GetEventFlag(12019257):
        """State 1"""
        if not GetEventFlag(12019255):
            """State 5"""
            # talk:10619000:"..."
            assert t000001000_x14(text1=10619000, z32=12019255, mode2=1)
        elif not GetEventFlag(12019256):
            """State 6"""
            # talk:10619100:"..."
            assert t000001000_x14(text1=10619100, z32=12019256, mode2=1)
        else:
            """State 7"""
            # talk:10619200:"..."
            call = t000001000_x14(text1=10619200, z32=12019257, mode2=1)
            if call.Done():
                pass
            elif call.Done():
                pass
    elif not GetEventFlag(12019260):
        """State 2"""
        if not GetEventFlag(12012711):
            """State 11"""
            # talk:10619300:"Perform for me a service, as recompense."
            assert t000001000_x14(text1=10619300, z32=12019258, mode2=1)
        elif GetEventFlag(1045379208) == 1:
            """State 8"""
            # talk:10620000:"Let us speak of the past, a while."
            assert t000001000_x14(text1=10620000, z32=12019260, mode2=1)
        else:
            """State 9"""
            # talk:10603000:"Let us speak of the past, a while."
            assert t000001000_x14(text1=10603000, z32=12019260, mode2=1)
    elif not GetEventFlag(12019265):
        """State 3"""
        if not GetEventFlag(12012712) or not GetEventFlag(1045379208):
            """State 12"""
            # talk:10620100:"I turned my back on the Two Fingers and we have each been cursing the other since."
            assert t000001000_x14(text1=10620100, z32=12019261, mode2=1)
        else:
            """State 10"""
            # talk:10621000:"Even when I turned my back upon the Two Fingers."
            assert t000001000_x14(text1=10621000, z32=12019265, mode2=1)
    else:
        """State 4,13"""
        # talk:10621100:"Ach, this form hath loosened my tongue."
        assert t000001000_x14(text1=10621100, z32=12019266, mode2=1)
    """State 14"""
    return 0

def t000001000_x56():
    """State 0"""
    if not GetEventFlag(12019275):
        """State 2"""
        # talk:10625000:"..."
        assert t000001000_x14(text1=10625000, z32=12019275, mode2=1)
    else:
        """State 3"""
        # talk:10625100:"Mine will be an order not of gold, but the stars and moon of the chill night."
        assert t000001000_x14(text1=10625100, z32=12019276, mode2=1)
    """State 1"""
    SetEventFlag(1034509407, 1)
    """State 4"""
    return 0

def t000001000_x57(z8=11):
    """State 0,7"""
    if not GetEventFlag(4680):
        """State 4"""
        if not GetEventFlag(1042372700):
            """State 2"""
            c1_149(z8, 21000001, -1, 0, 1)
            SetEventFlag(1042379200, 1)
        elif GetEventFlag(4699) == 1:
            """State 31"""
            assert t000001000_x46(z9=z8)
        else:
            """State 5"""
            pass
    else:
        """State 6"""
        if (GetEventFlag(10009655) == 1 and not GetEventFlag(105) and not DoesPlayerHaveSpEffect(4270)
            and not DoesPlayerHaveSpEffect(4271) and not DoesPlayerHaveSpEffect(4272) and not DoesPlayerHaveSpEffect(4280)
            and not DoesPlayerHaveSpEffect(4282) and not DoesPlayerHaveSpEffect(4286)):
            """State 18"""
            c1_149(z8, 21000050, -1, 0, 1)
            SetEventFlag(10009656, 1)
        elif GetEventFlag(1042372701) == 1 and not GetEventFlag(1042379203) and not GetEventFlag(10009655):
            """State 3"""
            c1_149(z8, 21000002, -1, 0, 1)
            SetEventFlag(1042379202, 1)
        elif GetEventFlag(1042372703) == 1:
            """State 28"""
            SetEventFlag(1042379208, 1)
            c5_149(not GetEventFlag(1042379209), z8, 21000004, -1, 0, 1)
            c5_149(GetEventFlag(1042379209) == 1, z8, 21000004, -1, 0, 0)
        elif (not GetEventFlag(1042372702) and not GetEventFlag(1042379207) and GetEventFlag(1042379203)
              == 1 and not GetEventFlag(10009655)):
            """State 8"""
            c1_149(z8, 21000003, -1, 0, 1)
            SetEventFlag(1042379206, 1)
        elif GetEventFlag(1046382701) == 1 and not GetEventFlag(1046389202):
            """State 9"""
            SetEventFlag(1046389201, 1)
            c5_149(not GetEventFlag(1046389203) and not GetEventFlag(1046382700), z8, 21000005, -1, 0, 1)
            c5_149(GetEventFlag(1046389203) == 1 and not GetEventFlag(1046382700), z8, 21000005, -1, 0, 0)
            # action:21000006:"Talk to Melina"
            AddTalkListDataIf(GetEventFlag(1046382700) == 1, z8, 21000006, -1)
        elif GetEventFlag(1043342700) == 1 and not GetEventFlag(1043349251):
            """State 10"""
            SetEventFlag(1043349250, 1)
            c5_149(not GetEventFlag(1043349252) and not GetEventFlag(1046382700), z8, 21000007, -1, 0, 1)
            c5_149(GetEventFlag(1043349252) == 1 and not GetEventFlag(1046382700), z8, 21000007, -1, 0, 0)
            # action:21000008:"Talk to Melina"
            AddTalkListDataIf(GetEventFlag(1046382700) == 1, z8, 21000008, -1)
        elif GetEventFlag(1038502710) == 1 and not GetEventFlag(1038509251):
            """State 11"""
            SetEventFlag(1038509250, 1)
            c5_149(not GetEventFlag(1038509252) and not GetEventFlag(1046382700), z8, 21000009, -1, 0, 1)
            c5_149(GetEventFlag(1038509252) == 1 and not GetEventFlag(1046382700), z8, 21000009, -1, 0, 0)
            # action:21000010:"Talk to Melina"
            AddTalkListDataIf(GetEventFlag(1046382700) == 1, z8, 21000010, -1)
        elif GetEventFlag(1043532710) == 1 and not GetEventFlag(1043539251):
            """State 12"""
            SetEventFlag(1043539250, 1)
            c5_149(not GetEventFlag(1043539252) and not GetEventFlag(1046382700), z8, 21000011, -1, 0, 1)
            c5_149(GetEventFlag(1043539252) == 1 and not GetEventFlag(1046382700), z8, 21000011, -1, 0, 0)
            # action:21000012:"Talk to Melina"
            AddTalkListDataIf(GetEventFlag(1046382700) == 1, z8, 21000012, -1)
        elif GetEventFlag(11002740) == 1 and not GetEventFlag(11009256):
            """State 13"""
            SetEventFlag(11009255, 1)
            c5_149(not GetEventFlag(11009257) and not GetEventFlag(1046382700), z8, 21000013, -1, 0, 1)
            c5_149(GetEventFlag(11009257) == 1 and not GetEventFlag(1046382700), z8, 21000013, -1, 0, 0)
            # action:21000014:"Talk to Melina"
            AddTalkListDataIf(GetEventFlag(1046382700) == 1, z8, 21000014, -1)
        elif GetEventFlag(1043502700) == 1 and not GetEventFlag(1043509201):
            """State 25"""
            SetEventFlag(1043509200, 1)
            c5_149(not GetEventFlag(1043509202) and not GetEventFlag(1046382700), z8, 21000015, -1, 0, 1)
            c5_149(GetEventFlag(1043509202) == 1 and not GetEventFlag(1046382700), z8, 21000015, -1, 0, 0)
            # action:21000016:"Talk to Melina"
            AddTalkListDataIf(GetEventFlag(1046382700) == 1, z8, 21000016, -1)
        elif GetEventFlag(1054552700) == 1 and not GetEventFlag(1054559201):
            """State 14"""
            SetEventFlag(1054559200, 1)
            c5_149(not GetEventFlag(1054559202) and not GetEventFlag(1046382700), z8, 21000017, -1, 0, 1)
            c5_149(GetEventFlag(1054559202) == 1 and not GetEventFlag(1046382700), z8, 21000017, -1, 0, 0)
            # action:21000018:"Talk to Melina"
            AddTalkListDataIf(GetEventFlag(1046382700) == 1, z8, 21000018, -1)
        # eventflag:400001:lot:100010:Rold Medallion
        elif (not GetEventFlag(1037519201) and not GetEventFlag(11009260) and not GetEventFlag(400001)
              and (GetEventFlag(1037512700) == 1 or GetEventFlag(1038512700) == 1 or GetEventFlag(1038502711)
              == 1 or GetEventFlag(1039512711) == 1 or GetEventFlag(1037522700) == 1)):
            """State 17"""
            c1_149(z8, 21000022, -1, 0, 1)
            SetEventFlag(1037519200, 1)
        elif (GetEventFlag(1036482710) == 1 and GetEventFlag(1036489213) == 1 and GetEventFlag(3940)
              == 1 and not GetEventFlag(1036489251)):
            """State 15"""
            c1_149(z8, 21000020, -1, 0, 1)
            SetEventFlag(1036489250, 1)
        elif (GetEventFlag(1039512710) == 1 and GetEventFlag(1039519209) == 1 and GetEventFlag(1036489210)
              == 1 and GetEventFlag(3940) == 1 and not GetEventFlag(1039519251)):
            """State 16"""
            SetEventFlag(1039519250, 1)
            c1_149(z8, 21000021, -1, 0, 1)
        elif GetEventFlag(11002745) == 1:
            """State 29"""
            c5_149(not GetEventFlag(11009266), z8, 21000023, -1, 0, 0)
            c5_149(GetEventFlag(11009266) == 1, z8, 21000023, -1, 0, 0)
            SetEventFlag(11009265, 1)
        elif ((GetEventFlag(1054552701) == 1 or GetEventFlag(1052562700) == 1 or GetEventFlag(1052542700)
              == 1 or GetEventFlag(1051532700) == 1 or GetEventFlag(1052532710) == 1) and not GetEventFlag(1054539211)):
            """State 21"""
            SetEventFlag(1054539210, 1)
            c1_149(z8, 21000026, -1, 0, 1)
        elif GetEventFlag(1054532702) == 1:
            """State 22"""
            SetEventFlag(1054539215, 1)
            c5_149(not GetEventFlag(1054539216), z8, 21000027, -1, 0, 1)
            c5_149(GetEventFlag(1054539216) == 1, z8, 21000027, -1, 0, 1)
        elif (GetEventFlag(35002730) == 1 or GetEventFlag(35002731) == 1) and not GetEventFlag(35009351):
            """State 23"""
            SetEventFlag(35009350, 1)
            c1_149(z8, 21000028, -1, 0, 1)
        elif GetEventFlag(35002731) == 1 and not GetEventFlag(35009353):
            """State 24"""
            SetEventFlag(35009352, 1)
            c1_149(z8, 21000030, -1, 0, 1)
        elif GetEventFlag(35002732) == 1 and not GetEventFlag(35002733):
            """State 26"""
            c5_149(not GetEventFlag(35009356) and not GetEventFlag(35009357), z8, 21000029, -1, 0, 0)
            c5_149(GetEventFlag(35009356) == 1 or GetEventFlag(35009357) == 1, z8, 21000029, -1, 0, 0)
            SetEventFlag(35009355, 1)
        elif GetEventFlag(35002733) == 1:
            """State 27"""
            c5_149(not GetEventFlag(35009359), z8, 21000031, -1, 0, 0)
            c5_149(GetEventFlag(35009359) == 1, z8, 21000031, -1, 0, 0)
            SetEventFlag(35009358, 1)
        elif GetEventFlag(11109387) == 1 and not GetEventFlag(11009271):
            """State 19"""
            SetEventFlag(11009270, 1)
            c1_149(z8, 21000024, -1, 0, 1)
        elif GetEventFlag(1049539207) == 1 and not GetEventFlag(11009276):
            """State 20"""
            SetEventFlag(11009275, 1)
            c1_149(z8, 21000025, -1, 0, 1)
        elif GetEventFlag(4699) == 1:
            """State 30"""
            assert t000001000_x46(z9=z8)
        else:
            """State 1"""
            pass
    """State 32"""
    return 0

def t000001000_x58(z9=12):
    """State 0,5"""
    if not GetEventFlag(4680):
        """State 2"""
        if GetEventFlag(4699) == 1:
            """State 7"""
            assert t000001000_x46(z9=z9)
        else:
            """State 3"""
            pass
    else:
        """State 4"""
        if GetEventFlag(4699) == 1:
            """State 6"""
            assert t000001000_x46(z9=z9)
        else:
            """State 1"""
            pass
    """State 8"""
    return 0

def t000001000_x59():
    """State 0"""
    if GetEventFlag(953) == 1:
        """State 3,1"""
        SetEventFlag(4653, 1)
    else:
        """State 2"""
        pass
    """State 4"""
    return 0

def t000001000_x60():
    """State 0"""
    if (GetEventFlag(10000851) == 1 and not GetEventFlag(10009655) and not DoesPlayerHaveSpEffect(4270)
        and not DoesPlayerHaveSpEffect(4271) and not DoesPlayerHaveSpEffect(4272) and not DoesPlayerHaveSpEffect(4280)
        and not DoesPlayerHaveSpEffect(4282) and not DoesPlayerHaveSpEffect(4286)):
        """State 2,3"""
        Label('L0')
        SetEventFlag(4653, 1)
    elif ((GetEventFlag(3062) == 1 or GetEventFlag(3063) == 1 or GetEventFlag(3064) == 1 or GetEventFlag(3065)
          == 1) and not GetEventFlag(10009655) and not DoesPlayerHaveSpEffect(4270) and not DoesPlayerHaveSpEffect(4271)
          and not DoesPlayerHaveSpEffect(4272) and not DoesPlayerHaveSpEffect(4280) and not DoesPlayerHaveSpEffect(4282)
          and not DoesPlayerHaveSpEffect(4286)):
        """State 4"""
        Goto('L0')
    # eventflag:400001:lot:100010:Rold Medallion
    elif (not GetEventFlag(11009260) and not GetEventFlag(400001) and not GetEventFlag(9104) and (GetEventFlag(11002741)
          == 1 or GetEventFlag(11002742) == 1 or GetEventFlag(11002743) == 1 or GetEventFlag(11002744)
          == 1)):
        """State 5"""
        Goto('L0')
    # eventflag:400001:lot:100010:Rold Medallion
    elif GetEventFlag(9104) == 1 and not GetEventFlag(400001):
        """State 6"""
        Goto('L0')
    else:
        """State 1"""
        pass
    """State 7"""
    return 0

def t000001000_x61():
    """State 0"""
    # eventflag:400001:lot:100010:Rold Medallion
    if GetEventFlag(9104) == 1 and not GetEventFlag(400001):
        """State 2,1"""
        SetEventFlag(4653, 1)
    else:
        """State 3"""
        pass
    """State 4"""
    return 0

def t000001000_x62():
    """State 0"""
    if not GetEventFlag(35009360):
        """State 3,1"""
        SetEventFlag(4653, 1)
    else:
        """State 2"""
        pass
    """State 4"""
    return 0

def t000001000_x63():
    """State 0"""
    while True:
        """State 1"""
        if CompareBonfireLevel(0, 0) == 1:
            """State 2"""
            # actionbutton:6100:"Touch grace"
            assert t000001000_x5(actionbutton5=6100, flag1=6001, flag2=6000)
        else:
            """State 3"""
            # actionbutton:6101:"Rest at site of grace"
            assert t000001000_x3(actionbutton1=6101, flag3=6001, flag4=6000)
        """State 4"""
        # action:20011020:"Cannot rest at sites of grace right now"
        assert t000001000_x4(action1=20011020)
    """Unused"""
    """State 5"""
    return 0

def t000001000_x64():
    """State 0,2"""
    if GetCurrentStateElapsedTime() > 0.8:
        """State 3"""
        GiveSpEffectToPlayer(9606)
        def WhilePaused():
            GiveSpEffectToPlayer(9606)
        def ExitPause():
            GiveSpEffectToPlayer(9606)
        if not f233():
            pass
        elif GetEventFlag(9001) == 1:
            """State 1"""
            Label('L0')
    elif GetEventFlag(9001) == 1:
        Goto('L0')
    """State 4"""
    return 0

def t000001000_x65(actionbutton1=6100, actionbutton2=6101, val1=45, z7=-120):
    """State 0"""
    if RelativeAngleBetweenTwoPlayers_SpecifyAxis(z7) < val1:
        """State 1"""
        Label('L0')
        """State 3"""
        call = t000001000_x41(actionbutton1=actionbutton1, actionbutton2=actionbutton2)
        if call.Done():
            """State 4"""
            return 0
        elif not RelativeAngleBetweenTwoPlayers_SpecifyAxis(z7) < val1:
            pass
    else:
        pass
    """State 2"""
    assert RelativeAngleBetweenTwoPlayers_SpecifyAxis(z7) < val1
    Goto('L0')

def t000001000_x66():
    """State 0,2"""
    if GetCurrentStateElapsedTime() > 0.8:
        """State 3"""
        GiveSpEffectToPlayer(9610)
        def WhilePaused():
            GiveSpEffectToPlayer(9610)
        def ExitPause():
            GiveSpEffectToPlayer(9610)
        if not f233():
            pass
        elif GetEventFlag(9001) == 1:
            """State 1"""
            Label('L0')
    elif GetEventFlag(9001) == 1:
        Goto('L0')
    """State 4"""
    return 0

def t000001000_x67():
    """State 0"""
    # eventflag:400001:lot:100010:Rold Medallion
    if GetEventFlag(400001) == 1 and not GetEventFlag(108) and not GetEventFlag(11002745):
        """State 1,3"""
        assert t000001000_x29(z17=20011)
    else:
        """State 2,4"""
        assert t000001000_x29(z17=20010)
    """State 5"""
    return 0

def t000001000_x68():
    """State 0"""
    if GetEventFlag(1054532702) == 1:
        """State 1"""
        if GetEventFlag(110) == 1 and not GetEventFlag(1054532703) and not GetEventFlag(9116):
            """State 3,7"""
            SetEventFlag(9000, 0)
            SetEventFlag(9020, 0)
            """State 6"""
            c1_138(-1)
            """State 5"""
            SetEventFlag(1054539206, 1)
            assert GetCurrentStateElapsedTime() > 15
            """State 8"""
            c5_138(not GetEventFlag(11102790), 1001000)
            SetEventFlag(9000, 1)
            SetEventFlag(9020, 1)
            SetEventFlag(1054539206, 0)
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 9"""
    return 0

def t000001000_x69(z5=1, z6=15000370):
    """State 0,5"""
    SetWorkValue(1, GetEstusAllocation(0) + GetEstusAllocation(1) + -4)
    """State 6"""
    assert t000001000_x21(z18=1, z19=1, z20=2, z21=2, z22=3, z23=3, z24=4, z25=4, z26=5, z27=5, z28=1)
    """State 3"""
    # goods:10010:Golden Seed
    if (ComparePlayerInventoryNumber(3, 10010, 4, GetWorkValue(1), 0) == 1 and GetEstusAllocation(0)
        + GetEstusAllocation(1) < 13):
        """State 1"""
        c1_149(z5, z6, -1, 0, 1)
    else:
        """State 2"""
        c1_149(z5, z6, -1, 0, 0)
    """State 4"""
    SetWorkValue(1, 0)
    """State 7"""
    return 0

def t000001000_x70(z3=2, z4=15000380):
    """State 0,3"""
    # goods:10020:Sacred Tear
    if ComparePlayerInventoryNumber(3, 10020, 4, 1, 0) == 1 and GetTotalBonfireLevel() <= 13:
        """State 1"""
        c1_149(z3, z4, -1, 0, 1)
    else:
        """State 2"""
        c1_149(z3, z4, -1, 0, 0)
    """State 4"""
    return 0

def t000001000_x71(z1=3, z2=15000371):
    """State 0,4"""
    SetWorkValue(1, GetEstusAllocation(0) + GetEstusAllocation(1) + -4)
    """State 7"""
    assert t000001000_x21(z18=1, z19=1, z20=2, z21=2, z22=3, z23=3, z24=4, z25=4, z26=5, z27=5, z28=1)
    """State 3"""
    # goods:10010:Golden Seed
    if (ComparePlayerInventoryNumber(3, 10010, 1, GetWorkValue(1), 0) == 1 or not GetEstusAllocation(0)
        + GetEstusAllocation(1) < 13):
        """State 2"""
        # goods:10020:Sacred Tear
        if ComparePlayerInventoryNumber(3, 10020, 3, 0, 0) == 1 or not GetTotalBonfireLevel() <= 13:
            """State 5"""
            c1_149(z1, z2, -1, 0, 0)
        else:
            """State 1"""
            Label('L0')
            c1_149(z1, z2, -1, 0, 1)
    else:
        Goto('L0')
    """State 6"""
    SetWorkValue(1, 0)
    """State 8"""
    return 0

#----------------------------------------------------------
# Time Selection
#----------------------------------------------------------
def t000001000_x80():
    c1110()
    
    while True:
        ClearTalkListData()

        # Clear Adjustment
        AddTalkListData(5, 80101006, -1)
        
        # Randomise Time
        AddTalkListData(1, 80101005, -1)
        
        # Force Day
        AddTalkListData(2, 80101002, -1)
        
        # Force Noon
        AddTalkListData(3, 80101003, -1)
        
        # Force Night
        AddTalkListData(4, 80101004, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Randomise Time
        if GetTalkListEntryResult() == 1:
            call = t000001000_x150(80101010)
    
            if call.Get() == 0:
                SetEventFlag(1047610410, 1)
                SetEventFlag(1047610411, 0)
                SetEventFlag(1047610412, 0)
                SetEventFlag(1047610413, 0)
            elif call.Get() == 1:
                pass
            return 0
        # Force Day
        elif GetTalkListEntryResult() == 2:
            call = t000001000_x150(80101011)
    
            if call.Get() == 0:
                SetEventFlag(1047610410, 0)
                SetEventFlag(1047610411, 1)
                SetEventFlag(1047610412, 0)
                SetEventFlag(1047610413, 0)
            elif call.Get() == 1:
                pass
            return 0
        # Force Noon
        elif GetTalkListEntryResult() == 3:
            call = t000001000_x150(80101012)
    
            if call.Get() == 0:
                SetEventFlag(1047610410, 0)
                SetEventFlag(1047610411, 0)
                SetEventFlag(1047610412, 1)
                SetEventFlag(1047610413, 0)
            elif call.Get() == 1:
                pass
            return 0
        # Force Night
        elif GetTalkListEntryResult() == 4:
            call = t000001000_x150(80101013)
    
            if call.Get() == 0:
                SetEventFlag(1047610410, 0)
                SetEventFlag(1047610411, 0)
                SetEventFlag(1047610412, 0)
                SetEventFlag(1047610413, 1)
            elif call.Get() == 1:
                pass
            return 0
        # Clear Adjustment
        elif GetTalkListEntryResult() == 5:
            call = t000001000_x150(80101014)
    
            if call.Get() == 0:
                SetEventFlag(1047610410, 0)
                SetEventFlag(1047610411, 0)
                SetEventFlag(1047610412, 0)
                SetEventFlag(1047610413, 0)
            elif call.Get() == 1:
                pass
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
        assert CheckSpecificPersonTalkHasEnded(0) == 1

#----------------------------------------------------------
# Weather
#----------------------------------------------------------
def t000001000_x81():
    c1110()
    
    while True:
        ClearTalkListData()

        # None
        AddTalkListData(1, 80101101, -1)
        
        # Clear Skies
        AddTalkListData(2, 80101102, -1)
        
        # Rain
        AddTalkListData(3, 80101103, -1)
        
        # Windy Rain
        AddTalkListData(5, 80101105, -1)
        
        # Scattered Rain
        AddTalkListData(16, 80101116, -1)
        
        # Snow
        AddTalkListData(4, 80101104, -1)
        
        # Heavy Snow
        AddTalkListData(11, 80101111, -1)
        
        # Fog
        AddTalkListData(6, 80101106, -1)
        
        # Windy Fog
        AddTalkListData(10, 80101110, -1)
        
        # Heavy Fog
        AddTalkListData(12, 80101112, -1)
        
        # Rainy, Heavy Fog
        AddTalkListData(14, 80101114, -1)
        
        # Snowy, Heavy Fog
        AddTalkListData(15, 80101115, -1)
        
        # Cloudless
        AddTalkListData(7, 80101107, -1)
        
        # Flat Clouds
        AddTalkListData(8, 80101108, -1)
        
        # Rainy Clouds
        AddTalkListData(17, 80101117, -1)
        
        # Puffy Clouds
        AddTalkListData(9, 80101109, -1)
        
        # Windy, Puffy Clouds
        AddTalkListData(13, 80101113, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # None
        if GetTalkListEntryResult() == 1:
            call = t000001000_x150(80101165)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610500)
            elif call.Get() == 1:
                pass
            return 0
        # Default
        elif GetTalkListEntryResult() == 2:
            call = t000001000_x150(80101150)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610510)
            elif call.Get() == 1:
                pass
            return 0
        # Rain
        elif GetTalkListEntryResult() == 3:
            call = t000001000_x150(80101151)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610511)
            elif call.Get() == 1:
                pass
            return 0
        # Snow
        elif GetTalkListEntryResult() == 4:
            call = t000001000_x150(80101152)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610512)
            elif call.Get() == 1:
                pass
            return 0
        # Windy Rain
        elif GetTalkListEntryResult() == 5:
            call = t000001000_x150(80101153)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610513)
            elif call.Get() == 1:
                pass
            return 0
        # Fog
        elif GetTalkListEntryResult() == 6:
            call = t000001000_x150(80101154)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610514)
            elif call.Get() == 1:
                pass
            return 0
        # Cloudless
        elif GetTalkListEntryResult() == 7:
            call = t000001000_x150(80101155)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610515)
            elif call.Get() == 1:
                pass
            return 0
        # Flat Clouds
        elif GetTalkListEntryResult() == 8:
            call = t000001000_x150(80101156)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610516)
            elif call.Get() == 1:
                pass
            return 0
        # Puffy Clouds
        elif GetTalkListEntryResult() == 9:
            call = t000001000_x150(80101157)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610517)
            elif call.Get() == 1:
                pass
            return 0
        # Rainy Clouds
        elif GetTalkListEntryResult() == 17:
            call = t000001000_x150(80101166)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610518)
            elif call.Get() == 1:
                pass
            return 0
        # Windy Fog
        elif GetTalkListEntryResult() == 10:
            call = t000001000_x150(80101158)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610519)
            elif call.Get() == 1:
                pass
            return 0
        # Heavy Snow
        elif GetTalkListEntryResult() == 11:
            call = t000001000_x150(80101159)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610520)
            elif call.Get() == 1:
                pass
            return 0
        # Heavy Fog
        elif GetTalkListEntryResult() == 12:
            call = t000001000_x150(80101160)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610521)
            elif call.Get() == 1:
                pass
            return 0
        # Windy, Puffy Clouds
        elif GetTalkListEntryResult() == 13:
            call = t000001000_x150(80101161)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610522)
            elif call.Get() == 1:
                pass
            return 0
        # Rainy, Heavy Fog
        elif GetTalkListEntryResult() == 14:
            call = t000001000_x150(80101162)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610523)
            elif call.Get() == 1:
                pass
            return 0
        # Snowy, Heavy Fog
        elif GetTalkListEntryResult() == 15:
            call = t000001000_x150(80101163)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610524)
            elif call.Get() == 1:
                pass
            return 0
        # Scattered Rain
        elif GetTalkListEntryResult() == 16:
            call = t000001000_x150(80101164)
    
            if call.Get() == 0:
                assert t000001000_x151(1047610525)
            elif call.Get() == 1:
                pass
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
        
# Utility
def t000001000_x150(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0
    
# Set Weather
def t000001000_x151(flag=_):
    SetEventFlag(1047610510, 0)
    SetEventFlag(1047610511, 0)
    SetEventFlag(1047610512, 0)
    SetEventFlag(1047610513, 0)
    SetEventFlag(1047610514, 0)
    SetEventFlag(1047610515, 0)
    SetEventFlag(1047610516, 0)
    SetEventFlag(1047610517, 0)
    SetEventFlag(1047610518, 0)
    SetEventFlag(1047610519, 0)
    SetEventFlag(1047610520, 0)
    SetEventFlag(1047610521, 0)
    SetEventFlag(1047610522, 0)
    SetEventFlag(1047610523, 0)
    SetEventFlag(1047610524, 0)
    SetEventFlag(1047610525, 0)
    
    SetEventFlag(flag, 1)
    
    return 0