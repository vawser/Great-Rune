# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Envoy of the Great-Jar
#-----------------------------------------------------
def t000001500_1():
    """State 0,1"""
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

#----------------------------------------------------
# Innards     
#----------------------------------------------------
def t000001500_x38():
    while True:
        ClearTalkListData()
        c1_110()
        
        # Offer Innards
        AddTalkListData(1, 80100000, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Offer Innards
        if GetTalkListEntryResult() == 1:
            assert t000001500_x100()
            assert not CheckSpecificPersonGenericDialogIsOpen(0)
        else:
            """State 6,8"""
            return 0
            
#----------------------------------------------------
# Innards     
#----------------------------------------------------
def t000001500_x100():
    c1110()
    
    while True:
        ClearTalkListData()

        # Innards of Vitality
        AddTalkListData(1, 80100100, -1)
        
        # Innards of Wisdom
        AddTalkListData(2, 80100101, -1)
        
        # Innards of Tenacity
        AddTalkListData(3, 80100102, -1)
        
        # Innards of Fortitude
        AddTalkListData(4, 80100103, -1)
        
        # Innards of Reflection
        AddTalkListData(5, 80100104, -1)
        
        # Innards of Regeneration
        AddTalkListData(6, 80100105, -1)
        
        # Innards of Tranquility
        AddTalkListData(7, 80100106, -1)
        
        # Innards of Endurance
        AddTalkListData(8, 80100107, -1)
        
        # Innards of Greed
        AddTalkListData(9, 80100108, -1)
        
        # Innards of Finesse
        AddTalkListData(10, 80100109, -1)
        
        # Innards of Courage
        AddTalkListData(11, 80100110, -1)
        
        # Innards of Clarity
        AddTalkListData(12, 80100111, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Vitality
        if GetTalkListEntryResult() == 1:
            assert t000001500_x120(1047610210, 5, 80100300, 10, 80100600, 80100700)
            continue
        # Wisdom
        elif GetTalkListEntryResult() == 2:
            assert t000001500_x120(1047610220, 5, 80100310, 10, 80100601, 80100710)
            continue
        # Tenacity
        elif GetTalkListEntryResult() == 3:
            assert t000001500_x120(1047610230, 5, 80100320, 10, 80100602, 80100720)
            return 0
        # Fortitude
        elif GetTalkListEntryResult() == 4:
            assert t000001500_x120(1047610240, 5, 80100330, 10, 80100603, 80100730)
            return 0
        # Reflection
        elif GetTalkListEntryResult() == 5:
            assert t000001500_x120(1047610250, 5, 80100340, 10, 80100604, 80100740)
            return 0
        # Regeneration
        elif GetTalkListEntryResult() == 6:
            assert t000001500_x120(1047610260, 3, 80100350, 10, 80100605, 80100750)
            return 0
        # Tranquility
        elif GetTalkListEntryResult() == 7:
            assert t000001500_x120(1047610270, 3, 80100360, 10, 80100606, 80100760)
            return 0
        # Endurance
        elif GetTalkListEntryResult() == 8:
            assert t000001500_x120(1047610280, 5, 80100370, 10, 80100607, 80100770)
            return 0
        # Greed
        elif GetTalkListEntryResult() == 9:
            assert t000001500_x120(1047610290, 5, 80100380, 10, 80100608, 80100780)
            return 0
        # Finesse
        elif GetTalkListEntryResult() == 10:
            assert t000001500_x120(1047610300, 5, 80100390, 10, 80100609, 80100790)
            return 0
        # Courage
        elif GetTalkListEntryResult() == 11:
            assert t000001500_x120(1047610310, 5, 80100400, 10, 80100610, 80100800)
            return 0
        # Clarity
        elif GetTalkListEntryResult() == 12:
            assert t000001500_x120(1047610320, 5, 80100410, 10, 80100611, 80100810)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of X
def t000001500_x120(base_flag=_, max_count=_, rank_text=_, cost=_, cost_text=_, purchase_text=_):
    c1110()
    
    while True:
        ClearTalkListData()

        # Acquire
        AddTalkListDataIf(GetEventFlag(base_flag + (max_count - 1)) == 0, 1, 80100012, -1)
        
        # View Current Effect
        AddTalkListDataIf(GetEventFlag(base_flag) == 1, 2, 80100011, -1)
        
        # View Innard Effect
        AddTalkListDataIf(GetEventFlag(base_flag) == 0, 3, 80100013, -1)
        
        # Quit
        AddTalkListData(99, 80100015, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Acquire
        if GetTalkListEntryResult() == 1:
            c1_110()
    
            ClearTalkListData()
            
            # Acquire
            AddTalkListData(1, cost_text, -1)
            
            # Cancel
            AddTalkListData(2, 80100015, -1)
            
            OpenConversationChoicesMenu(0)
            
            assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))

            # Acquire
            if GetTalkListEntryResult() == 1:
                if ComparePlayerInventoryNumber(3, 1290, 3, cost, 0) == 1:
                    # Insufficient Potent Innards
                    assert t000001500_x151(80100014)
                else:
                    PlayerEquipmentQuantityChange(3, 1290, ( cost * -1 ) )
                    
                    # None -> Rank 1
                    if(GetEventFlag(base_flag) == 0):
                        SetEventFlag(base_flag, 1)
                        assert t000001500_x151(purchase_text)
                    # Rank 4 -> Rank 5
                    elif(GetEventFlag(base_flag + 3) == 1):
                        SetEventFlag(base_flag + 4, 1)
                        assert t000001500_x151(purchase_text + 4)
                    # Rank 3 -> Rank 4
                    elif(GetEventFlag(base_flag + 2) == 1):
                        SetEventFlag(base_flag + 3, 1)
                        assert t000001500_x151(purchase_text + 3)
                    # Rank 2 -> Rank 3
                    elif(GetEventFlag(base_flag + 1) == 1):
                        SetEventFlag(base_flag + 2, 1)
                        assert t000001500_x151(purchase_text + 2)
                    # Rank 1 -> Rank 2
                    elif(GetEventFlag(base_flag) == 1):
                        SetEventFlag(base_flag + 1, 1)
                        assert t000001500_x151(purchase_text + 1)
                    else:
                        pass
            # Cancel
            elif GetTalkListEntryResult() == 2:
                # Declined
                assert t000001500_x151(80100016)
                return 1
            else:
                return 2
   
            return 0
        # View Current Effect
        elif GetTalkListEntryResult() == 2:
            if(GetEventFlag(base_flag) == 0):
                assert t000001500_x151(80100500)
            elif(GetEventFlag(base_flag + 4) == 1):
                assert t000001500_x151(rank_text + 4)
            elif(GetEventFlag(base_flag + 3) == 1):
                assert t000001500_x151(rank_text + 3)
            elif(GetEventFlag(base_flag + 2) == 1):
                assert t000001500_x151(rank_text + 2)
            elif(GetEventFlag(base_flag + 1) == 1):
                assert t000001500_x151(rank_text + 1)
            elif(GetEventFlag(base_flag) == 1):
                assert t000001500_x151(rank_text)
            else:
                pass
                
            return 0
        # View Innard Effect
        elif GetTalkListEntryResult() == 3:
            assert t000001500_x151(rank_text)
                
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
#----------------------------------------------------------
# Utility
#----------------------------------------------------------
def t000001500_x151(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0
    