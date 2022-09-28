# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Ritual of Dragon Communion #1
#-----------------------------------------------------
def t601006000_1():
    """State 0,1"""
    t601006000_x0(z1=101975, z2=101999)
    Quit()

def t601006000_x0(z1=101975, z2=101999):
    """State 0"""
    if not IsClientPlayer():
        """State 1"""
        Label('L0')
        call = t601006000_x1(z1=z1, z2=z2)
        if IsClientPlayer() == 1:
            """State 2"""
            Label('L1')
            call = t601006000_x2()
            if not IsClientPlayer():
                Goto('L0')
            elif IsPlayerDead() == 1:
                pass
        elif IsPlayerDead() == 1:
            pass
    else:
        Goto('L1')
    """State 3"""
    call = t601006000_x4()
    assert not IsPlayerDead()
    Goto('L0')
    """Unused"""
    """State 4"""
    return 0

def t601006000_x1(z1=101975, z2=101999):
    """State 0"""
    while True:
        """State 2"""
        # actionbutton:6580:"Examine altar"
        assert (t601006000_x5(actionbutton1=6580, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000,
                flag6=6000))
        """State 1"""
        TurnCharacterToFaceEntity(-1, 10000, -1, -1)
        ClearPlayerDamageInfo()
        assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
        """State 3"""
        ClearTalkActionState()
        call = t601006000_x3(z1=z1, z2=z2)
        def WhilePaused():
            GiveSpEffectToPlayerIf(not DidYouDoSomethingInTheMenu(0), 9611)
            GiveSpEffectToPlayerIf((DoesPlayerHaveSpEffect(9611) == 1 or DoesPlayerHaveSpEffect(9612) == 1) and DidYouDoSomethingInTheMenu(0) == 1,
                                   9613)
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 3 or HasPlayerBeenAttacked() == 1:
            pass
        """State 4"""
        assert t601006000_x6()
    """Unused"""
    """State 5"""
    return 0

def t601006000_x2():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t601006000_x3(z1=101975, z2=101999):
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        c1_110()
        """State 2"""
        # action:26010000:"Ritual of Dragon Communion"
        AddTalkListData(1, 26010000, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 5,7"""
            OpenDragonCommunionShop(z1, z2)
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        else:
            """State 6,8"""
            return 0

def t601006000_x4():
    """State 0,2"""
    assert t601006000_x6()
    """State 1"""
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t601006000_x5(actionbutton1=6580, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000):
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
        # actionbutton:6580:"Examine altar"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t601006000_x6():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

