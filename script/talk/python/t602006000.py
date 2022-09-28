# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Smithing Table
#-----------------------------------------------------
def t602006000_1():
    """State 0,1"""
    t602006000_x0()
    Quit()

def t602006000_x0():
    """State 0"""
    if not IsClientPlayer():
        """State 1"""
        Label('L0')
        call = t602006000_x1()
        if IsClientPlayer() == 1:
            """State 2"""
            Label('L1')
            call = t602006000_x2()
            if not IsClientPlayer():
                Goto('L0')
            elif IsPlayerDead() == 1:
                pass
        elif IsPlayerDead() == 1:
            pass
    else:
        Goto('L1')
    """State 3"""
    call = t602006000_x4()
    assert not IsPlayerDead()
    Goto('L0')
    """Unused"""
    """State 4"""
    return 0

def t602006000_x1():
    """State 0"""
    while True:
        """State 1"""
        # actionbutton:6250:"Use smithing table"
        call = t602006000_x5(actionbutton1=6250, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000,
                             flag6=6000)
        if call.Done():
            """State 2"""
            call = t602006000_x3()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 3 or IsMultiplayerInProgress() == 1:
                pass
        elif IsMultiplayerInProgress() == 1:
            pass
        """State 3"""
        assert t602006000_x6() and not IsMultiplayerInProgress()
    """Unused"""
    """State 4"""
    return 0

def t602006000_x2():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t602006000_x3():
    """State 0"""
    while True:
        """State 1"""
        Label('L0')
        ClearTalkListData()
        c1_110()
        """State 2"""
        # action:26020000:"Strengthen armament"
        # AddTalkListData(1, 26020000, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 5,9"""
            CombineMenuFlagAndEventFlag(6001, 232)
            CombineMenuFlagAndEventFlag(6001, 233)
            CombineMenuFlagAndEventFlag(6001, 234)
            CombineMenuFlagAndEventFlag(6001, 235)
            """State 8"""
            OpenEnhanceShop(1)
            c1_141(25)
            assert not (CheckSpecificPersonMenuIsOpen(25, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        else:
            """State 6,11"""
            return 0
    """Unused"""
    """State 7,10"""
    OpenEquipmentChangeOfPurposeShop()
    assert not (CheckSpecificPersonMenuIsOpen(7, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    Goto('L0')

def t602006000_x4():
    """State 0,2"""
    assert t602006000_x6()
    """State 1"""
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t602006000_x5(actionbutton1=6250, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag1) == 1 or GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1 or GetEventFlag(flag4)
                == 1 or GetEventFlag(flag5) == 1)
        """State 4"""
        assert not GetEventFlag(flag6)
        """State 2"""
        if GetEventFlag(flag6) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag1) and not GetEventFlag(flag2) and not GetEventFlag(flag3) and not
              GetEventFlag(flag4) and not GetEventFlag(flag5)):
            pass
        # actionbutton:6250:"Use smithing table"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t602006000_x6():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

