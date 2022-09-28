# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Envoy of the Great-Jar
#-----------------------------------------------------
def t000001500_1():
    """State 0,1"""
    # Set Innard flags here
    assert t000001500_x80()
    
    # actionbutton:6210:"Talk"
    t000001500_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t000001500_1000():
    """State 0,2,3"""
    assert t000001500_x35()
    """State 1"""
    c1_120(1000)
    Quit()

def t000001500_2000():
    """State 0,2,3"""
    assert t000001500_x36()
    """State 1"""
    c1_120(2000)
    Quit()

def t000001500_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                  flag4=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag5) == 1 or GetEventFlag(flag9) == 1 or GetEventFlag(flag10) == 1 or
                GetEventFlag(flag11) == 1 or GetEventFlag(flag12) == 1)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 2"""
        if GetEventFlag(flag4) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag5) and not GetEventFlag(flag9) and not GetEventFlag(flag10) and not
              GetEventFlag(flag11) and not GetEventFlag(flag12)):
            pass
        # actionbutton:6210:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t000001500_x1():
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

def t000001500_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000001500_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t000001500_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t000001500_x1()
    else:
        """State 4,7"""
        call = t000001500_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t000001500_x1()
    """State 9"""
    return 0

def t000001500_x4():
    """State 0,1"""
    assert t000001500_x1()
    """State 2"""
    return 0

def t000001500_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t000001500_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t000001500_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t000001500_x6(val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t000001500_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t000001500_x13(val1=val1, z1=z1)
            def WhilePaused():
                c5_138(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
                GiveSpEffectToPlayer(9640)
                c5_139(1 == (mode1 == 1), -1, 0)
                c5_139(1 == (mode2 == 1), 0, -1)
            def ExitPause():
                c1_138(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif IsAttackedBySomeone() == 1 and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        elif GetEventFlag(flag8) == 1:
            Goto('L0')
        elif GetEventFlag(flag6) == 1 and not GetEventFlag(flag7) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t000001500_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t000001500_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t000001500_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t000001500_x7(val2=10, val3=12):
    """State 0,1"""
    call = t000001500_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t000001500_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t000001500_x8(flag1=3223, val2=10, val3=12):
    """State 0,8"""
    assert t000001500_x34()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t000001500_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000001500_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t000001500_x9(actionbutton1=6210, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t000001500_x10(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t000001500_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001500_x10(z6=_, val6=_):
    """State 0,1"""
    if f203(z6) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z6)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t000001500_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t000001500_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t000001500_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000001500_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t000001500_x12():
    """State 0,1"""
    assert t000001500_x10(z6=1101, val6=1101)
    """State 2"""
    return 0

def t000001500_x13(val1=5, z1=1):
    """State 0,2"""
    assert t000001500_x23()
    """State 1"""
    call = t000001500_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t000001500_x25()
    """State 4"""
    return 0

def t000001500_x14():
    """State 0,1"""
    assert t000001500_x10(z6=1000, val6=1000)
    """State 2"""
    return 0

def t000001500_x15(val5=30):
    """State 0,1"""
    call = t000001500_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t000001500_x26()
    """State 3"""
    return 0

def t000001500_x16():
    """State 0,1"""
    assert t000001500_x10(z6=1100, val6=1100)
    """State 2"""
    return 0

def t000001500_x17(val2=10, val3=12):
    """State 0,5"""
    assert t000001500_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t000001500_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t000001500_x28()
    """Unused"""
    """State 6"""
    return 0

def t000001500_x18():
    """State 0,2"""
    call = t000001500_x10(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t000001500_x19():
    """State 0,1"""
    assert t000001500_x10(z6=1001, val6=1001)
    """State 2"""
    return 0

def t000001500_x20():
    """State 0,1"""
    assert t000001500_x10(z6=1103, val6=1103)
    """State 2"""
    return 0

def t000001500_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t000001500_x22(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t000001500_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t000001500_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t000001500_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t000001500_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t000001500_x23():
    """State 0,1"""
    assert t000001500_x24()
    """State 2"""
    return 0

def t000001500_x24():
    """State 0,1"""
    assert t000001500_x10(z6=1104, val6=1104)
    """State 2"""
    return 0

def t000001500_x25():
    """State 0,1"""
    call = t000001500_x10(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t000001500_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001500_x26():
    """State 0,1"""
    call = t000001500_x10(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t000001500_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001500_x27():
    """State 0,1"""
    call = t000001500_x10(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t000001500_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001500_x28():
    """State 0,1"""
    call = t000001500_x10(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t000001500_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001500_x29(text2=_, mode4=1):
    """State 0,4"""
    assert t000001500_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text2, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode4:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t000001500_x30(text1=_, z5=_, mode3=1):
    """State 0,5"""
    assert t000001500_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z5, 1)
    """State 1"""
    TalkToPlayer(text1, -1, -1, 1)
    """State 4"""
    if not mode3:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t000001500_x31():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000001500_x32():
    """State 0,1"""
    assert t000001500_x10(z6=1002, val6=1002)
    """State 2"""
    return 0

def t000001500_x33():
    """State 0,1"""
    assert t000001500_x1()
    """State 2"""
    return 0

def t000001500_x34():
    """State 0,1"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 2"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 3"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 4"""
        ForceCloseMenu()
    else:
        pass
    """State 5"""
    return 0

def t000001500_x35():
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 8"""
    assert t000001500_x38()
    """State 9"""
    return 0

def t000001500_x36():
    """State 0,1"""
    assert t000001500_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000)
                
    """State 4"""
    return 0

# Innards Flags Setup
def t000001500_x80():
    assert t000001500_x81(30000, 75010) # Innards of Vitality
    assert t000001500_x81(30010, 75020) # Innards of Wisdom
    assert t000001500_x81(30020, 75030) # Innards of Tenacity
    assert t000001500_x81(30030, 75040) # Innards of Fortitude
    assert t000001500_x81(30040, 75050) # Innards of Reflection
    assert t000001500_x82(30050, 75060) # Innards of Regeneration
    assert t000001500_x82(30060, 75070) # Innards of Tranquility
    assert t000001500_x81(30070, 75080) # Innards of Endurance
    assert t000001500_x81(30080, 75090) # Innards of Greed
    assert t000001500_x81(30090, 75100) # Innards of Finesse
    assert t000001500_x81(30100, 75110) # Innards of Courage
    assert t000001500_x81(30110, 75120) # Innards of Clarity
    
    return 0

# Update Innard Flags - Stack 5
def t000001500_x81(item=_, flag=_):
    SetEventFlag(flag, 0)
    SetEventFlag(flag + 1, 0)
    SetEventFlag(flag + 2, 0)
    SetEventFlag(flag + 3, 0)
    SetEventFlag(flag + 4, 0)

    if(ComparePlayerInventoryNumber(3, item, 0, 1, 0) == 1):
        SetEventFlag(flag, 1)
    elif(ComparePlayerInventoryNumber(3, item, 0, 2, 0) == 1):
        SetEventFlag(flag + 1, 1)
    elif(ComparePlayerInventoryNumber(3, item, 0, 3, 0) == 1):
        SetEventFlag(flag + 2, 1)
    elif(ComparePlayerInventoryNumber(3, item, 0, 4, 0) == 1):
        SetEventFlag(flag + 3, 1)
    elif(ComparePlayerInventoryNumber(3, item, 0, 5, 0) == 1):
        SetEventFlag(flag + 4, 1)
    else:
        pass
        
    return 0
    
# Update Innard Flags - Stack 3
def t000001500_x82(item=_, flag=_):
    SetEventFlag(flag, 0)
    SetEventFlag(flag + 1, 0)
    SetEventFlag(flag + 2, 0)
    
    if(ComparePlayerInventoryNumber(3, item, 0, 1, 0) == 1):
        SetEventFlag(flag + 1, 1)
    elif(ComparePlayerInventoryNumber(3, item, 0, 2, 0) == 1):
        SetEventFlag(flag + 2, 1)
    elif(ComparePlayerInventoryNumber(3, item, 0, 3, 0) == 1):
        SetEventFlag(flag + 3, 1)
    else:
        pass
        
    return 0
    
#----------------------------------------------------
# Innards     
#----------------------------------------------------
def t000001500_x38():
    c1110()
    
    while True:
        ClearTalkListData()

        # Innards of Vitality
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 30000, 3, 4, 0) == 1, 1, 80100100, -1)
        
        # Innards of Wisdom
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 30010, 3, 4, 0) == 1, 2, 80100101, -1)
        
        # Innards of Tenacity
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 30020, 3, 4, 0) == 1, 3, 80100102, -1)
        
        # Innards of Fortitude
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 30030, 3, 4, 0) == 1, 4, 80100103, -1)
        
        # Innards of Reflection
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 30040, 3, 4, 0) == 1, 5, 80100104, -1)
        
        # Innards of Regeneration
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 30050, 3, 2, 0) == 1, 6, 80100105, -1)
        
        # Innards of Tranquility
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 30050, 3, 2, 0) == 1, 7, 80100106, -1)
        
        # Innards of Endurance
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 30060, 3, 4, 0) == 1, 8, 80100107, -1)
        
        # Innards of Greed
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 30070, 3, 4, 0) == 1, 9, 80100108, -1)
        
        # Innards of Finesse
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 30080, 3, 4, 0) == 1, 10, 80100109, -1)
        
        # Innards of Courage
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 30090, 3, 4, 0) == 1, 11, 80100110, -1)
        
        # Innards of Clarity
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 30100, 3, 4, 0) == 1, 12, 80100111, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Vitality
        if GetTalkListEntryResult() == 1:
            assert t000001500_x120()
            continue
        # Wisdom
        elif GetTalkListEntryResult() == 2:
            assert t000001500_x121()
            continue
        # Tenacity
        elif GetTalkListEntryResult() == 3:
            assert t000001500_x122()
            return 0
        # Fortitude
        elif GetTalkListEntryResult() == 4:
            assert t000001500_x123()
            return 0
        # Reflection
        elif GetTalkListEntryResult() == 5:
            assert t000001500_x124()
            return 0
        # Regeneration
        elif GetTalkListEntryResult() == 6:
            assert t000001500_x125()
            return 0
        # Tranquility
        elif GetTalkListEntryResult() == 7:
            assert t000001500_x126()
            return 0
        # Endurance
        elif GetTalkListEntryResult() == 8:
            assert t000001500_x127()
            return 0
        # Greed
        elif GetTalkListEntryResult() == 9:
            assert t000001500_x128()
            return 0
        # Finesse
        elif GetTalkListEntryResult() == 10:
            assert t000001500_x129()
            return 0
        # Courage
        elif GetTalkListEntryResult() == 11:
            assert t000001500_x130()
            return 0
        # Clarity
        elif GetTalkListEntryResult() == 12:
            assert t000001500_x131()
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Vitality
def t000001500_x120():
    c1110()
    
    while True:
        ClearTalkListData()

        # Purchase
        AddTalkListData(1, 80100012, -1)
        
        # View Effect
        AddTalkListData(2, 80100011, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Purchase
        if GetTalkListEntryResult() == 1:
            assert t000001500_x150(30000, 80100200, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t000001500_x151(80100300)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Wisdom
def t000001500_x121():
    c1110()
    
    while True:
        ClearTalkListData()

        # Purchase
        AddTalkListData(1, 80100012, -1)
        
        # View Effect
        AddTalkListData(2, 80100011, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Purchase
        if GetTalkListEntryResult() == 1:
            assert t000001500_x150(30010, 80100201, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t000001500_x151(80100301)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Tenacity
def t000001500_x122():
    c1110()
    
    while True:
        ClearTalkListData()

        # Purchase
        AddTalkListData(1, 80100012, -1)
        
        # View Effect
        AddTalkListData(2, 80100011, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Purchase
        if GetTalkListEntryResult() == 1:
            assert t000001500_x150(30020, 80100202, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t000001500_x151(80100302)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Fortitude
def t000001500_x123():
    c1110()
    
    while True:
        ClearTalkListData()

        # Purchase
        AddTalkListData(1, 80100012, -1)
        
        # View Effect
        AddTalkListData(2, 80100011, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Purchase
        if GetTalkListEntryResult() == 1:
            assert t000001500_x150(30030, 80100203, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t000001500_x151(80100303)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Reflection
def t000001500_x124():
    c1110()
    
    while True:
        ClearTalkListData()

        # Purchase
        AddTalkListData(1, 80100012, -1)
        
        # View Effect
        AddTalkListData(2, 80100011, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Purchase
        if GetTalkListEntryResult() == 1:
            assert t000001500_x150(30040, 80100204, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t000001500_x151(80100304)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Regeneration
def t000001500_x125():
    c1110()
    
    while True:
        ClearTalkListData()

        # Purchase
        AddTalkListData(1, 80100012, -1)
        
        # View Effect
        AddTalkListData(2, 80100011, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Purchase
        if GetTalkListEntryResult() == 1:
            assert t000001500_x150(30050, 80100205, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t000001500_x151(80100305)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Tranquility
def t000001500_x126():
    c1110()
    
    while True:
        ClearTalkListData()

        # Purchase
        AddTalkListData(1, 80100012, -1)
        
        # View Effect
        AddTalkListData(2, 80100011, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Purchase
        if GetTalkListEntryResult() == 1:
            assert t000001500_x150(30060, 80100206, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t000001500_x151(80100306)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Endurance
def t000001500_x127():
    c1110()
    
    while True:
        ClearTalkListData()

        # Purchase
        AddTalkListData(1, 80100012, -1)
        
        # View Effect
        AddTalkListData(2, 80100011, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Purchase
        if GetTalkListEntryResult() == 1:
            assert t000001500_x150(30070, 80100207, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t000001500_x151(80100307)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Greed
def t000001500_x128():
    c1110()
    
    while True:
        ClearTalkListData()

        # Purchase
        AddTalkListData(1, 80100012, -1)
        
        # View Effect
        AddTalkListData(2, 80100011, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Purchase
        if GetTalkListEntryResult() == 1:
            assert t000001500_x150(30080, 80100208, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t000001500_x151(80100308)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Finesse
def t000001500_x129():
    c1110()
    
    while True:
        ClearTalkListData()

        # Purchase
        AddTalkListData(1, 80100012, -1)
        
        # View Effect
        AddTalkListData(2, 80100011, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Purchase
        if GetTalkListEntryResult() == 1:
            assert t000001500_x150(30090, 80100209, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t000001500_x151(80100309)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Courage
def t000001500_x130():
    c1110()
    
    while True:
        ClearTalkListData()

        # Purchase
        AddTalkListData(1, 80100012, -1)
        
        # View Effect
        AddTalkListData(2, 80100011, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Purchase
        if GetTalkListEntryResult() == 1:
            assert t000001500_x150(30100, 80100210, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t000001500_x151(80100310)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Clarity
def t000001500_x131():
    c1110()
    
    while True:
        ClearTalkListData()

        # Purchase
        AddTalkListData(1, 80100012, -1)
        
        # View Effect
        AddTalkListData(2, 80100011, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Purchase
        if GetTalkListEntryResult() == 1:
            assert t000001500_x150(30110, 80100211, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t000001500_x151(80100311)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0


            
#----------------------------------------------------------
# Utility
#----------------------------------------------------------
def t000001500_x150(innard_item=_, purchase_message=_, cost=_):
    # Purchase this innard
    call = t000001500_x151(80100013)
    
    if call.Get() == 0:
        if ComparePlayerInventoryNumber(3, 1290, 3, cost, 0) == 1:
            # Insufficient Potent Innards
            assert t000001500_x151(80100014)
        else:
            PlayerEquipmentQuantityChange(3, 1290, cost)
            PlayerEquipmentQuantityChange(3, innard_item, 1)
            
            # X purchased
            assert t000001500_x151(purchase_message)
            
            # Update innard flags
            assert t000001500_x80()
    elif call.Get() == 1:
        pass
    return 0
    
def t000001500_x151(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0
    