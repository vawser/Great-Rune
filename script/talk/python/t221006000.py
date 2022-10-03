# -*- coding: utf-8 -*-
#-----------------------------------------------------
# The Great Jar
#-----------------------------------------------------
def t221006000_1():
    """State 0,1"""
    t221006000_x9()
    Quit()

def t221006000_x0(actionbutton1=6570, flag2=6001, flag3=6000, flag4=6000, flag5=6000, flag6=6000, flag7=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1 or GetEventFlag(flag4) == 1 or GetEventFlag(flag5)
                == 1 or GetEventFlag(flag6) == 1)
        """State 4"""
        assert not GetEventFlag(flag7)
        """State 2"""
        if GetEventFlag(flag7) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag2) and not GetEventFlag(flag3) and not GetEventFlag(flag4) and not
              GetEventFlag(flag5) and not GetEventFlag(flag6)):
            pass
        # actionbutton:6570:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t221006000_x1():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t221006000_x2(text1=_, flag1=0, mode1=1):
    """State 0,4"""
    assert t221006000_x1() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, flag1)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode1:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t221006000_x3(lot1=104700):
    """State 0,1"""
    # lot:104700:Great-Jar's Arsenal
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t221006000_x4():
    """State 0"""
    while True:
        """State 2"""
        call = t221006000_x5()
        assert IsClientPlayer() == 1 or IsMultiplayerInProgress() == 1
        """State 1"""
        assert not IsClientPlayer() and not IsMultiplayerInProgress()
    """Unused"""
    """State 3"""
    return 0

def t221006000_x5():
    """State 0"""
    while True:
        """State 1"""
        # eventflag:400470:lot:104700:Great-Jar's Arsenal
        if GetEventFlag(400470) == 1:
            """State 3"""
            call = t221006000_x7()
            if call.Done():
                pass
            # eventflag:400470:lot:104700:Great-Jar's Arsenal
            elif not GetEventFlag(400470):
                pass
        elif GetEventFlag(1047419201) == 1:
            """State 4"""
            assert t221006000_x8()
        elif GetEventFlag(1047419200) == 1:
            """State 5"""
            call = t221006000_x10()
            if call.Done():
                pass
            # eventflag:400470:lot:104700:Great-Jar's Arsenal
            elif GetEventFlag(400470) == 1:
                pass
        else:
            """State 2"""
            call = t221006000_x6()
            if call.Done():
                pass
            # eventflag:400470:lot:104700:Great-Jar's Arsenal
            elif GetEventFlag(1047419201) == 1 or GetEventFlag(400470) == 1:
                pass
    """Unused"""
    """State 6"""
    return 0

def t221006000_x6():
    """State 0,1"""
    # actionbutton:6570:"Talk"
    assert (t221006000_x0(actionbutton1=6570, flag2=6001, flag3=6000, flag4=6000, flag5=6000, flag6=6000,
            flag7=6000))
    """State 2"""
    # talk:22100100:"..."
    def ExitPause():
        SetEventFlag(1047419200, 1)
    assert t221006000_x2(text1=22100100, flag1=0, mode1=1)
    """State 3"""
    return 0

def t221006000_x7():
    """State 0,1"""
    # actionbutton:6570:"Talk"
    assert (t221006000_x0(actionbutton1=6570, flag2=6001, flag3=6000, flag4=6000, flag5=6000, flag6=6000,
            flag7=6000))
    """State 2"""
    RequestAnimation(20004, -1)
    # talk:22100120:"..."
    assert t221006000_x2(text1=22100120, flag1=0, mode1=1)
    """State 3"""
    return 0

def t221006000_x8():
    """State 0,1"""
    # actionbutton:6570:"Talk"
    assert (t221006000_x0(actionbutton1=6570, flag2=6001, flag3=6000, flag4=6000, flag5=6000, flag6=6000,
            flag7=6000))
    """State 3"""
    # talk:22100100:"..."
    assert t221006000_x2(text1=22100100, flag1=0, mode1=1)
    """State 2"""
    # lot:104700:Great-Jar's Arsenal
    assert t221006000_x3(lot1=104700)
    """State 4"""
    return 0

def t221006000_x9():
    """State 0"""
    while True:
        """State 2"""
        call = t221006000_x4()
        assert CheckSelfDeath() == 1
        """State 1"""
        assert not CheckSelfDeath()
    """Unused"""
    """State 3"""
    return 0

def t221006000_x10():
    """State 0"""
    assert GetEventFlag(1047419201) == 1
    """State 1"""
    assert GetCurrentStateElapsedTime() > 1
    """State 2"""
    c1_121(9780)
    """State 3"""
    return 0

