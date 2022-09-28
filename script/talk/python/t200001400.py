# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Rennala
#-----------------------------------------------------
def t200001400_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t200001400_x7(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=20, val5=20, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t200001400_1000():
    """State 0,2"""
    assert t200001400_x37()
    """State 1"""
    c1_120(1000)
    Quit()

def t200001400_2000():
    """State 0,2,3"""
    assert t200001400_x38()
    """State 1"""
    c1_120(2000)
    Quit()

def t200001400_x0(action2=22001000):
    """State 0,1"""
    # action:22001000:"Use a Larval Tear to accept rebirth?"
    OpenGenericDialog(8, action2, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t200001400_x1(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t200001400_x2():
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

def t200001400_x3():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t200001400_x4(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t200001400_x5(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t200001400_x21()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t200001400_x2()
    else:
        """State 4,7"""
        call = t200001400_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t200001400_x2()
    """State 9"""
    return 0

def t200001400_x6():
    """State 0,1"""
    assert t200001400_x2()
    """State 2"""
    return 0

def t200001400_x7(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=20, val5=20, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t200001400_x24(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t200001400_x23()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t200001400_x8(val1=5, val2=10, val3=12, val4=20, val5=20, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t200001400_x11(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t200001400_x15(val1=val1, z1=z1)
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
            call = t200001400_x17(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t200001400_x28() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t200001400_x13(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t200001400_x9(val2=10, val3=12):
    """State 0,1"""
    call = t200001400_x19(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t200001400_x5(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t200001400_x10(flag1=6000, val2=10, val3=12):
    """State 0,8"""
    assert t200001400_x36()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t200001400_x22()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t200001400_x2()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t200001400_x11(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t200001400_x12(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t200001400_x1(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200001400_x12(z6=_, val6=_):
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

def t200001400_x13(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t200001400_x2()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t200001400_x14()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t200001400_x29()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t200001400_x14():
    """State 0,1"""
    assert t200001400_x12(z6=1101, val6=1101)
    """State 2"""
    return 0

def t200001400_x15(val1=5, z1=1):
    """State 0,2"""
    assert t200001400_x25()
    """State 1"""
    call = t200001400_x16()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t200001400_x27()
    """State 4"""
    return 0

def t200001400_x16():
    """State 0,1"""
    assert t200001400_x12(z6=1000, val6=1000)
    """State 2"""
    return 0

def t200001400_x17(val5=20):
    """State 0,1"""
    call = t200001400_x18()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t200001400_x28()
    """State 3"""
    return 0

def t200001400_x18():
    """State 0,1"""
    assert t200001400_x12(z6=1100, val6=1100)
    """State 2"""
    return 0

def t200001400_x19(val2=10, val3=12):
    """State 0,5"""
    assert t200001400_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t200001400_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t200001400_x30()
    """Unused"""
    """State 6"""
    return 0

def t200001400_x20():
    """State 0,2"""
    call = t200001400_x12(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t200001400_x21():
    """State 0,1"""
    assert t200001400_x12(z6=1001, val6=1001)
    """State 2"""
    return 0

def t200001400_x22():
    """State 0,1"""
    assert t200001400_x12(z6=1103, val6=1103)
    """State 2"""
    return 0

def t200001400_x23():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t200001400_x24(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=20, val5=20, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t200001400_x8(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t200001400_x10(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t200001400_x9(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t200001400_x35() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t200001400_x25():
    """State 0,1"""
    assert t200001400_x26()
    """State 2"""
    return 0

def t200001400_x26():
    """State 0,1"""
    assert t200001400_x12(z6=1104, val6=1104)
    """State 2"""
    return 0

def t200001400_x27():
    """State 0,1"""
    call = t200001400_x12(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t200001400_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200001400_x28():
    """State 0,1"""
    call = t200001400_x12(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t200001400_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200001400_x29():
    """State 0,1"""
    call = t200001400_x12(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t200001400_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200001400_x30():
    """State 0,1"""
    call = t200001400_x12(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t200001400_x6()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t200001400_x31(text2=_, mode4=1):
    """State 0,4"""
    assert t200001400_x3() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t200001400_x32(text1=_, z5=_, mode3=1):
    """State 0,5"""
    assert t200001400_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t200001400_x33():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t200001400_x34():
    """State 0,1"""
    assert t200001400_x12(z6=1002, val6=1002)
    """State 2"""
    return 0

def t200001400_x35():
    """State 0,1"""
    assert t200001400_x2()
    """State 2"""
    return 0

def t200001400_x36():
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

def t200001400_x37():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(20010, -1)
    assert t200001400_x40()
    """State 2"""
    return 0

def t200001400_x38():
    """State 0,1"""
    assert t200001400_x41()
    """State 2"""
    return 0

def t200001400_x39():
    """State 0,6"""
    if not GetEventFlag(14002702):
        """State 7"""
        Label('L0')
        if not GetEventFlag(14009205):
            """State 53"""
            # talk:20001000:"Ah...thou..."
            assert t200001400_x31(text2=20001000, mode4=1)
        elif not GetEventFlag(14002703) and GetEventFlag(14009206) == 1:
            """State 54"""
            # talk:20001100:"Ah...thou..."
            assert t200001400_x31(text2=20001100, mode4=1)
        else:
            """State 55"""
            # talk:20001400:"Ah...thou..."
            assert t200001400_x31(text2=20001400, mode4=1)
            """State 12"""
            SetEventFlag(14002703, 0)
        """State 8"""
        SetEventFlag(14009205, 1)
        """State 46"""
        if not GetEventFlag(3468):
            pass
        else:
            """State 47"""
            SetEventFlag(14009210, 1)
        while True:
            """State 1"""
            c1_110()
            ClearTalkListData()
            """State 15"""
            # action:22000000:"Rebirth"
            AddTalkListData(1, 22000000, -1)
            # action:22000001:"Cosmetics"
            AddTalkListData(2, 22000001, -1)
            # Boss Rebirth
            AddTalkListData(3, 80000000, -1)
            
            # action:22000002:"Leave"
            AddTalkListData(99, 22000002, -1)
            """State 3"""
            ShowShopMessage(1)
            """State 4"""
            assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 2"""
            if GetTalkListEntryResult() == 1:
                """State 32"""
                if GetEventFlag(14002702) == 1:
                    pass
                else:
                    """State 26"""
                    PlayerEquipmentQuantityChange(3, 2170, -1)
                    # goods:8185:Larval Tear
                    if ComparePlayerInventoryNumber(3, 8185, 4, 1, 0) == 1:
                        """State 59"""
                        # action:22001000:"Use a Larval Tear to accept rebirth?"
                        call = t200001400_x0(action2=22001000)
                        if call.Done() and GetGenericDialogButtonResult() == 1:
                            """State 34"""
                            pass
                        elif call.Done():
                            continue
                    else:
                        """State 61"""
                        # action:22001002:"A Larval Tear is required for rebirth"
                        assert t200001400_x4(action1=22001002)
                        continue
                """State 58"""
                # talk:20001200:"Now, bear this sweeting into life anew."
                assert t200001400_x31(text2=20001200, mode4=1)
                """State 16"""
                TurnCharacterToFaceEntity(-1, 10000, -1, -1)
                ReallocateAttributes()
                ClearTalkActionState()
                assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
                """State 49"""
                def WhilePaused():
                    GiveSpEffectToPlayer(9614)
                assert not (CheckSpecificPersonMenuIsOpen(19, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                """State 17"""
                if DidYouDoSomethingInTheMenu(2) == 1:
                    """State 21,48"""
                    def WhilePaused():
                        GiveSpEffectToPlayer(9616)
                    assert DoesPlayerHaveSpEffect(9617) == 1
                    """State 37"""
                    if not GetEventFlag(60839):
                        """State 36"""
                        # gesture:97:Balled Up
                        AcquireGesture(97)
                        SetEventFlag(60839, 1)
                    else:
                        """State 38"""
                        pass
                    """State 22"""
                    if not GetEventFlag(14002702):
                        """State 19,25"""
                        SetEventFlagValue(14009220, 10, GetEventFlagValue(14009220, 10) + 1)
                        # goods:8185:Larval Tear
                        PlayerEquipmentQuantityChange(3, 8185, -1)
                    else:
                        """State 20"""
                        pass
                    """State 24"""
                    SetEventFlag(14009206, 1)
                    """State 23"""
                    SetEventFlag(14002702, 1)
                    """State 13"""
                    RequestSave(0)
                    if GetEventFlagValue(14009220, 10) > 5:
                        """State 57"""
                        # talk:20001600:"Ah, thou'rt now a sweeting full fine and fair."
                        assert t200001400_x31(text2=20001600, mode4=1)
                        """State 14"""
                        SetEventFlag(14009207, 1)
                    else:
                        """State 29"""
                        pass
                    """State 51"""
                    assert not DoesPlayerHaveSpEffect(9617)
                else:
                    """State 33"""
                    if GetEventFlag(14002702) == 1:
                        pass
                    else:
                        """State 35,18,60"""
                        # action:22001001:"Since you weren't reborn with new attributes,\nthe Larval Tear was not spent"
                        assert t200001400_x4(action1=22001001)
            elif GetTalkListEntryResult() == 2:
                """State 27"""
                TurnCharacterToFaceEntity(-1, 10000, -1, -1)
                OpenCharaMakeMenu(0)
                ClearTalkActionState()
                assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
                """State 50"""
                def WhilePaused():
                    GiveSpEffectToPlayer(9614)
                assert not (CheckSpecificPersonMenuIsOpen(16, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                """State 28,42"""
                if DidYouDoSomethingInTheMenu(1) == 1:
                    """State 40"""
                    if not GetEventFlag(60839):
                        """State 39"""
                        # gesture:97:Balled Up
                        AcquireGesture(97)
                        SetEventFlag(60839, 1)
                    else:
                        """State 41"""
                        pass
                else:
                    """State 43"""
                    pass
            # Boss Rebirth
            elif GetTalkListEntryResult() == 3:
                assert t200001400_x90()
            else:
                """State 5,30"""
                if not GetEventFlag(14002702):
                    """State 56"""
                    # talk:20001300:"Be not alarmed, nor afeard."
                    assert t200001400_x31(text2=20001300, mode4=1)
                    """State 9"""
                    SetEventFlag(14002703, 1)
                    break
                else:
                    """State 31"""
                    break
    else:
        """State 44"""
        if not GetEventFlag(14009207):
            """State 52"""
            # talk:20001500:"Ah, it seemeth thou'rt a sweeting rather fair."
            assert t200001400_x31(text2=20001500, mode4=1)
            """State 10"""
            SetEventFlag(14002704, 1)
            """State 11"""
            SetEventFlag(14002702, 0)
        else:
            """State 45"""
            SetEventFlag(14002702, 0)
            Goto('L0')
    """State 62"""
    return 0

def t200001400_x40():
    """State 0,1"""
    assert t200001400_x39()
    """State 2"""
    return 0

def t200001400_x41():
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6000:"Talk"
        call = t200001400_x1(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            break
        elif (GetEventFlag(14002705) == 1 and not GetEventFlag(14009205) and not GetEventFlag(3468) and
              not GetEventFlag(14002700)):
            pass
        elif (GetEventFlag(14002706) == 1 and not GetEventFlag(14009210) and GetEventFlag(3468) == 1
              and not GetEventFlag(14002701)):
            Goto('L0')
        """State 4"""
        # talk:20000900:"Where did ye flee, my sweetings?"
        call = t200001400_x32(text1=20000900, z5=14002700, mode3=1)
        if call.Done():
            continue
        elif GetDistanceToPlayer() > 20 or GetEventFlag(14009205) == 1:
            """State 1"""
            continue
        """State 5"""
        Label('L0')
        # talk:20003000:"Where did ye flee, my sweetings?"
        call = t200001400_x32(text1=20003000, z5=14002701, mode3=1)
        if call.Done():
            pass
        elif GetDistanceToPlayer() > 20 or GetEventFlag(14009210) == 1:
            """State 2"""
            pass
    """State 6"""
    return 0

# Boos Rebirth
def t200001400_x90():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Stranded Graveyard         
        AddTalkListData(1, 80000100, -1)
        # Limgrave
        AddTalkListData(2, 80000200, -1)
        # Stormveil Castle 
        AddTalkListData(3, 80000300, -1)
        # Weeping Penisula
        AddTalkListData(4, 80000400, -1)
        # Liurnia of the Lakes 
        AddTalkListData(5, 80000500, -1)
        # Academy of Raya Lucaria   
        AddTalkListData(6, 80000600, -1)
        # Mt. Gelmir
        AddTalkListData(7, 80000700, -1)
        # Volcano Manor
        AddTalkListData(8, 80000800, -1)
        # Altus Plateau
        AddTalkListData(9, 80000900, -1)
        # Caelid
        AddTalkListData(10, 80001000, -1)
        # Capital Outskirts
        AddTalkListData(11, 80001100, -1)
        # Leyndell, Royal Capital 
        AddTalkListData(12, 80001200, -1)
        # Siofra River
        AddTalkListData(13, 80001300, -1)
        # Ainsel River
        AddTalkListData(14, 80001400, -1)
        # Lake of Rot  
        AddTalkListData(15, 80001500, -1)
        # Deeproot Depths
        AddTalkListData(16, 80001600, -1)
        # Mohgwyn Palace
        AddTalkListData(17, 80001700, -1)
        # Nokron, Eternal City 
        AddTalkListData(18, 80001800, -1)
        # Consecrated Snowfield
        AddTalkListData(19, 80001900, -1)
        # Mountaintops of the Giants  
        AddTalkListData(20, 80002000, -1)
        # Leyndell, Ashen Capital      
        AddTalkListData(21, 80002100, -1)
        # Crumbling Farum Azula 
        AddTalkListData(22, 80002200, -1)
        # Miquella's Haligtree
        AddTalkListData(23, 80002300, -1)
        # Elden Throne
        AddTalkListData(24, 80002400, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Stranded Graveyard         
        if GetTalkListEntryResult() == 1:
            assert t200001400_x91()
        # Limgrave
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x92()
        # Stormveil Castle
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x93()
        # Weeping Penisula
        elif GetTalkListEntryResult() == 4:
            assert t200001400_x94()
        # Liurnia of the Lakes
        elif GetTalkListEntryResult() == 5:
            assert t200001400_x95()
        # Academy of Raya Lucaria
        elif GetTalkListEntryResult() == 6:
            assert t200001400_x96()
        # Mt. Gelmir
        elif GetTalkListEntryResult() == 7:
            assert t200001400_x97()
        # Volcano Manor
        elif GetTalkListEntryResult() == 8:
            assert t200001400_x98()
        # Altus Plateau
        elif GetTalkListEntryResult() == 9:
            assert t200001400_x99()
        # Caelid
        elif GetTalkListEntryResult() == 10:
            assert t200001400_x100()
        # Capital Outskirts
        elif GetTalkListEntryResult() == 11:
            assert t200001400_x101()
        # Leyndell, Royal Capital
        elif GetTalkListEntryResult() == 12:
            assert t200001400_x102()
        # Siofra River
        elif GetTalkListEntryResult() == 13:
            assert t200001400_x103()
        # Ainsel River
        elif GetTalkListEntryResult() == 14:
            assert t200001400_x104()
        # Lake of Rot
        elif GetTalkListEntryResult() == 15:
            assert t200001400_x105()
        # Deeproot Depths
        elif GetTalkListEntryResult() == 16:
            assert t200001400_x106()
        # Mohgwyn Palace
        elif GetTalkListEntryResult() == 17:
            assert t200001400_x107()
        # Nokron, Eternal City
        elif GetTalkListEntryResult() == 18:
            assert t200001400_x108()
        # Consecrated Snowfield
        elif GetTalkListEntryResult() == 19:
            assert t200001400_x109()
        # Mountaintops of the Giants
        elif GetTalkListEntryResult() == 20:
            assert t200001400_x110()
        # Leyndell, Ashen Capital
        elif GetTalkListEntryResult() == 21:
            assert t200001400_x111()
        # Crumbling Farum Azula
        elif GetTalkListEntryResult() == 22:
            assert t200001400_x112()
        # Miquella's Haligtree
        elif GetTalkListEntryResult() == 23:
            assert t200001400_x113()
        # Elden Throne
        elif GetTalkListEntryResult() == 24:
            assert t200001400_x114()
        else:
            return 0


    
# Stranded Graveyard     
def t200001400_x91():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Ulcerated Tree Spirit
        AddTalkListData(1, 80010100, -1)
        # Soldier of Godrick
        AddTalkListData(2, 80010101, -1)
        # Grafted Scion
        AddTalkListData(3, 80010102, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Ulcerated Tree Spirit 
        if GetTalkListEntryResult() == 1:
            assert t200001400_x120(18000800, 80020100)
        # Soldier of Godrick
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x120(18000850, 80020101)
        # Grafted Scion
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x120(10010800, 80020102)
        else:
            return 0


    
# Limgrave
def t200001400_x92():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Cemetery Shade
        AddTalkListData(1, 80010200, -1)
        # Erdtree Burial Watchdog
        AddTalkListData(2, 80010201, -1)
        # Grave Warden Duelist
        AddTalkListData(3, 80010202, -1)
        # Black Knife Assassin
        AddTalkListData(4, 80010203, -1)
        # Patches
        AddTalkListData(5, 80010204, -1)
        # Demi-Human Chief
        AddTalkListData(6, 80010205, -1)
        # Guardian Golem
        AddTalkListData(7, 80010206, -1)
        # Miranda the Blighted Bloom
        AddTalkListData(8, 80010207, -1)
        # Beastman of Farum Azula
        AddTalkListData(9, 80010208, -1)
        # Stonedigger Troll
        AddTalkListData(10, 80010209, -1)
        # Tree Sentinel
        AddTalkListData(11, 80010210, -1)
        # Crucible Knight
        AddTalkListData(12, 80010211, -1)
        # Death Rite Bird
        AddTalkListData(13, 80010212, -1)
        # Ball-Bearing Hunter
        AddTalkListData(14, 80010213, -1)
        # Flying Dragon Agheel
        AddTalkListData(15, 80010214, -1)
        # Night's Cavalry
        AddTalkListData(16, 80010215, -1)
        # Bloodhound Knight Darriwil
        AddTalkListData(17, 80010216, -1)
        # Mad Pumpkin Head
        AddTalkListData(18, 80010217, -1)
        # Tibia Mariner
        AddTalkListData(19, 80010218, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Cemetery Shade
        if GetTalkListEntryResult() == 1:
            assert t200001400_x120(30000800, 80020200)
        # Erdtree Burial Watchdog
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x120(30020800, 80020201)
        # Grave Warden Duelist
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x120(30040800, 80020202)
        # Black Knife Assassin
        elif GetTalkListEntryResult() == 4:
            assert t200001400_x120(30110800, 80020203)
        # Patches
        elif GetTalkListEntryResult() == 5:
            assert t200001400_x120(31000800, 80020204)
        # Demi-Human Chief
        elif GetTalkListEntryResult() == 6:
            assert t200001400_x120(31150800, 80020205)
        # Guardian Golem
        elif GetTalkListEntryResult() == 7:
            assert t200001400_x120(31170800, 80020206)
        # Miranda the Blighted Bloom
        elif GetTalkListEntryResult() == 8:
            assert t200001400_x120(31020800, 80020207)
        # Beastman of Farum Azula
        elif GetTalkListEntryResult() == 9:
            assert t200001400_x120(31030800, 80020208)
        # Stonedigger Troll
        elif GetTalkListEntryResult() == 10:
            assert t200001400_x120(32010800, 80020209)
        # Tree Sentinel
        elif GetTalkListEntryResult() == 11:
            assert t200001400_x120(1042360800, 80020210)
        # Crucible Knight
        elif GetTalkListEntryResult() == 12:
            assert t200001400_x120(1042370800, 80020211)
        # Death Rite Bird
        elif GetTalkListEntryResult() == 13:
            assert t200001400_x120(1042380800, 80020212)
        # Ball-Bearing Hunter
        elif GetTalkListEntryResult() == 14:
            assert t200001400_x120(1042380850, 80020213)
        # Flying Dragon Agheel
        elif GetTalkListEntryResult() == 15:
            assert t200001400_x120(1043360800, 80020214)
        # Night's Cavalry
        elif GetTalkListEntryResult() == 16:
            assert t200001400_x120(1043370340, 80020215)
        # Bloodhound Knight Darriwil
        elif GetTalkListEntryResult() == 17:
            assert t200001400_x120(1044350800, 80020216)
        # Mad Pumpkin Head
        elif GetTalkListEntryResult() == 18:
            assert t200001400_x120(1044360800, 80020217)
        # Tibia Mariner
        elif GetTalkListEntryResult() == 19:
            assert t200001400_x120(1045390800, 80020218)
        else:
            return 0


    
# Stormveil Castle 
def t200001400_x93():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Margit, the Fell Omen
        AddTalkListData(1, 80010300, -1)
        # Godrick the Grafted
        AddTalkListData(2, 80010301, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Margit, the Fell Omen
        if GetTalkListEntryResult() == 1:
            assert t200001400_x121(10000850, 71001, 80020300)
        # Godrick the Grafted
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x121(10000800, 71000, 80020301)
        else:
            return 0


    
# Weeping Penisula
def t200001400_x94():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Erdtree Burial Watchdog
        AddTalkListData(1, 80010400, -1)
        # Runebear
        AddTalkListData(2, 80010401, -1)
        # Scaly Misbegotten
        AddTalkListData(3, 80010402, -1)
        # Ancient Hero of Zamor
        AddTalkListData(4, 80010403, -1)
        # Leonine Misbegotten
        AddTalkListData(5, 80010404, -1)
        # Erdtree Avatar
        AddTalkListData(6, 80010405, -1)
        # Death Rite Bird
        AddTalkListData(7, 80010406, -1)
        # Night's Cavalry
        AddTalkListData(8, 80010407, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Erdtree Burial Watchdog
        if GetTalkListEntryResult() == 1:
            assert t200001400_x120(30010800, 80020400)
        # Runebear
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x120(31010800, 80020401)
        # Scaly Misbegotten
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x120(32000800, 80020402)
        # Ancient Hero of Zamor
        elif GetTalkListEntryResult() == 4:
            assert t200001400_x120(1042330800, 80020403)
        # Leonine Misbegotten
        elif GetTalkListEntryResult() == 5:
            assert t200001400_x120(1043300800, 80020404)
        # Erdtree Avatar
        elif GetTalkListEntryResult() == 6:
            assert t200001400_x120(1043330800, 80020405)
        # Death Rite Bird
        elif GetTalkListEntryResult() == 7:
            assert t200001400_x120(1044320340, 80020406)
        # Night's Cavalry
        elif GetTalkListEntryResult() == 8:
            assert t200001400_x120(1044320342, 80020407)
        else:
            return 0


    
# Liurnia of the Lakes 
def t200001400_x95():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Spirit-Caller Snail
        AddTalkListData(1, 80010500, -1)
        # Cemetery Shade
        AddTalkListData(2, 80010501, -1)
        # Black Knife Assassin
        AddTalkListData(3, 80010502, -1)
        # Erdtree Burial Watchdog
        AddTalkListData(4, 80010503, -1)
        # Cleanrot Knight
        AddTalkListData(5, 80010504, -1)
        # Bloodhound Knight
        AddTalkListData(6, 80010505, -1)
        # Crystalians #1
        AddTalkListData(7, 80010506, -1)
        # Crystalians #2
        AddTalkListData(8, 80010507, -1)
        # Magma Wyrm Makar
        AddTalkListData(9, 80010508, -1)
        # Alecto, Black Knife Ringleader
        AddTalkListData(10, 80010509, -1)
        # Bols, Carian Knight
        AddTalkListData(11, 80010510, -1)
        # Glintstone Dragon Adula
        AddTalkListData(12, 80010511, -1)
        # Glintstone Dragon Smarag
        AddTalkListData(13, 80010512, -1)
        # Royal Revenant
        AddTalkListData(14, 80010513, -1)
        # Omenkiller
        AddTalkListData(15, 80010514, -1)
        # Royal Knight Loretta
        AddTalkListData(16, 80010515, -1)
        # Onyx Lord
        AddTalkListData(17, 80010516, -1)
        # Ball-Bearing Hunter
        AddTalkListData(18, 80010517, -1)
        # Adan, Thief of Fire
        AddTalkListData(19, 80010518, -1)
        # Tibia Mariner
        AddTalkListData(20, 80010519, -1)
        # Night's Cavalry #1
        AddTalkListData(21, 80010520, -1)
        # Night's Cavalry #2
        AddTalkListData(22, 80010521, -1)
        # Death Rite Bird #1
        AddTalkListData(23, 80010522, -1)
        # Death Rite Bird #2
        AddTalkListData(24, 80010523, -1)
        # Erdtree Avatar #1
        AddTalkListData(25, 80010524, -1)
        # Erdtree Avatar #2
        AddTalkListData(26, 80010525, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Spirit-Caller Snail
        if GetTalkListEntryResult() == 1:
            assert t200001400_x120(30030800, 80020500)
        # Cemetery Shade
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x120(30050800, 80020501)
        # Black Knife Assassin
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x120(30050850, 80020502)
        # Erdtree Burial Watchdog
        elif GetTalkListEntryResult() == 4:
            assert t200001400_x120(30060800, 80020503)
        # Cleanrot Knight
        elif GetTalkListEntryResult() == 5:
            assert t200001400_x120(31040800, 80020504)
        # Bloodhound Knight
        elif GetTalkListEntryResult() == 6:
            assert t200001400_x120(31050800, 80020505)
        # Crystalians #1
        elif GetTalkListEntryResult() == 7:
            assert t200001400_x120(31060800, 80020506)
        # Crystalians #2
        elif GetTalkListEntryResult() == 8:
            assert t200001400_x120(32020800, 80020507)
        # Magma Wyrm Makar
        elif GetTalkListEntryResult() == 9:
            assert t200001400_x121(39200800, 73900, 80020508)
        # Alecto, Black Knife Ringleader
        elif GetTalkListEntryResult() == 10:
            assert t200001400_x120(1033420800, 80020509)
        # Bols, Carian Knight
        elif GetTalkListEntryResult() == 11:
            assert t200001400_x120(1033450800, 80020510)
        # Glintstone Dragon Adula
        elif GetTalkListEntryResult() == 12:
            assert t200001400_x121(1034420800, 1034500800, 80020511)
        # Glintstone Dragon Smarag
        elif GetTalkListEntryResult() == 13:
            assert t200001400_x120(1034450800, 80020512)
        # Royal Revenant
        elif GetTalkListEntryResult() == 14:
            assert t200001400_x120(1034480800, 80020513)
        # Omenkiller
        elif GetTalkListEntryResult() == 15:
            assert t200001400_x120(1035420800, 80020514)
        # Royal Knight Loretta
        elif GetTalkListEntryResult() == 16:
            assert t200001400_x120(1035500800, 80020515)
        # Onyx Lord
        elif GetTalkListEntryResult() == 17:
            assert t200001400_x120(1036500800, 80020516)
        # Ball-Bearing Hunter
        elif GetTalkListEntryResult() == 18:
            assert t200001400_x120(1037460800, 80020517)
        # Adan, Thief of Fire
        elif GetTalkListEntryResult() == 19:
            assert t200001400_x120(1038410800, 80020518)
        # Tibia Mariner
        elif GetTalkListEntryResult() == 20:
            assert t200001400_x120(1039440800, 80020519)
        # Night's Cavalry #1
        elif GetTalkListEntryResult() == 21:
            assert t200001400_x120(1036480340, 80020520)
        # Night's Cavalry #2
        elif GetTalkListEntryResult() == 22:
            assert t200001400_x120(1039430340, 80020521)
        # Death Rite Bird #1
        elif GetTalkListEntryResult() == 23:
            assert t200001400_x120(1036450340, 80020522)
        # Death Rite Bird #2
        elif GetTalkListEntryResult() == 24:
            assert t200001400_x120(1037420340, 80020523)
        # Erdtree Avatar #1
        elif GetTalkListEntryResult() == 25:
            assert t200001400_x120(1033430800, 80020524)
        # Erdtree Avatar #2
        elif GetTalkListEntryResult() == 26:
            assert t200001400_x120(1038480800, 80020525)
        else:
            return 0


    
# Academy of Raya Lucaria   
def t200001400_x96():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Rennala, Queen of the Full Moon
        # AddTalkListData(1, 80010600, -1)
        # Red Wolf of Radagon
        AddTalkListData(2, 80010601, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Rennala, Queen of the Full Moon
        if GetTalkListEntryResult() == 1:
            assert t200001400_x121(14000800, 71400, 80020600)
        # Red Wolf of Radagon
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x121(14000850, 71401, 80020601)
        else:
            return 0


    
# Mt. Gelmir
def t200001400_x97():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Red Wolf of the Champion
        AddTalkListData(1, 80010700, -1)
        # Misbegotten Warrior/Perfumer Tricia
        AddTalkListData(2, 80010701, -1)
        # Kindred of Rot
        AddTalkListData(3, 80010702, -1)
        # Demi-Human Queen Margot
        AddTalkListData(4, 80010703, -1)
        # Magma Wyrm
        AddTalkListData(5, 80010704, -1)
        # Full-Grown Fallingstar Beast
        AddTalkListData(6, 80010705, -1)
        # Demi-Human Queen
        AddTalkListData(7, 80010706, -1)
        # Ulcerated Tree Spirit
        AddTalkListData(8, 80010707, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Red Wolf of the Champion  
        if GetTalkListEntryResult() == 1:
            assert t200001400_x120(30090800, 80020700)
        # Misbegotten Warrior/Perfumer Tricia
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x121(30120800, 30120801, 80020701)
        # Kindred of Rot  
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x120(31070800, 80020702)
        # Demi-Human Queen Margot  
        elif GetTalkListEntryResult() == 4:
            assert t200001400_x120(31090800, 80020703)
        # Magma Wyrm 
        elif GetTalkListEntryResult() == 5:
            assert t200001400_x120(1035530800, 80020704)
        # Full-Grown Fallingstar Beast
        elif GetTalkListEntryResult() == 6:
            assert t200001400_x120(1036540800, 80020705)
        # Demi-Human Queen
        elif GetTalkListEntryResult() == 7:
            assert t200001400_x120(1037530800, 80020706)
        # Ulcerated Tree Spirit
        elif GetTalkListEntryResult() == 8:
            assert t200001400_x120(1037540810, 80020707)
        else:
            return 0


    
# Volcano Manor
def t200001400_x98():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Rykard, Lord of Blasphemy
        AddTalkListData(1, 80010800, -1)
        # Godskin Noble
        AddTalkListData(2, 80010801, -1)
        # Abductor Virgins
        AddTalkListData(3, 80010802, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Rykard, Lord of Blasphemy
        if GetTalkListEntryResult() == 1:
            assert t200001400_x121(16000800, 71600, 80020800)
        # Godskin Noble  
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x121(16000850, 71601, 80020801)
        # Abductor Virgins
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x121(16000860, 71606, 80020802)
        else:
            return 0


    
# Altus Plateau
def t200001400_x99():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Erdtree Burial Watchdog
        AddTalkListData(1, 80010900, -1)
        # Ancient Hero of Zamor
        AddTalkListData(2, 80010901, -1)
        # Crucible Knight Ordovis/Crucible Knight
        AddTalkListData(3, 80010902, -1)
        # Grave Warden Duelist
        AddTalkListData(4, 80010903, -1)
        # Miranda the Blighted Bloom
        AddTalkListData(5, 80010904, -1)
        # Black Knife Assassin #1
        AddTalkListData(6, 80010905, -1)
        # Black Knife Assassin #2
        AddTalkListData(7, 80010906, -1)
        # Necromancer Garris
        AddTalkListData(8, 80010907, -1)
        # Stonedigger Troll
        AddTalkListData(9, 80010908, -1)
        # Crystalians
        AddTalkListData(10, 80010909, -1)
        # Onyx Lord
        AddTalkListData(11, 80010910, -1)
        # Ancient Dragon Lansseax
        AddTalkListData(12, 80010911, -1)
        # Demi-Human Queen
        AddTalkListData(13, 80010912, -1)
        # Tibia Mariner
        AddTalkListData(14, 80010913, -1)
        # Godefroy the Grafted
        AddTalkListData(15, 80010914, -1)
        # Night's Cavalry
        AddTalkListData(16, 80010915, -1)
        # Elemer of the Briar
        AddTalkListData(17, 80010916, -1)
        # Sanguine Noble
        AddTalkListData(18, 80010917, -1)
        # Fallingstar Beast
        AddTalkListData(19, 80010918, -1)
        # Tree Sentinel Duo
        AddTalkListData(20, 80010919, -1)
        # Wormface
        AddTalkListData(21, 80010920, -1)
        # Godskin Apostle
        AddTalkListData(22, 80010921, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Erdtree Burial Watchdog  
        if GetTalkListEntryResult() == 1:
            assert t200001400_x120(30070800, 80020900)
        # Ancient Hero of Zamor
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x120(30080800, 80020901)
        # Crucible Knight Ordovis  
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x121(30100800, 30100801, 80020902)
        # Grave Warden Duelist  
        elif GetTalkListEntryResult() == 4:
            assert t200001400_x120(30130800, 80020903)
        # Miranda the Blighted Bloom   
        elif GetTalkListEntryResult() == 5:
            assert t200001400_x120(31180800, 80020904)
        # Black Knife Assassin #1
        elif GetTalkListEntryResult() == 6:
            assert t200001400_x120(31190800, 80020905)
        # Black Knife Assassin #2   
        elif GetTalkListEntryResult() == 7:
            assert t200001400_x120(1040520800, 80020906)
        # Necromancer Garris
        elif GetTalkListEntryResult() == 8:
            assert t200001400_x120(31190850, 80020907)
        # Stonedigger Troll
        elif GetTalkListEntryResult() == 9:
            assert t200001400_x120(32040800, 80020908)
        # Crystalians    
        elif GetTalkListEntryResult() == 10:
            assert t200001400_x121(32050800, 32050801, 80020909)
        # Onyx Lord 
        elif GetTalkListEntryResult() == 11:
            assert t200001400_x120(34120800, 80020910)
        # Ancient Dragon Lansseax 
        elif GetTalkListEntryResult() == 12:
            assert t200001400_x121(1037510800, 1041520800, 80020911)
        # Demi-Human Queen   
        elif GetTalkListEntryResult() == 13:
            assert t200001400_x120(1038510800, 80020912)
        # Tibia Mariner  
        elif GetTalkListEntryResult() == 14:
            assert t200001400_x120(1038520340, 80020913)
        # Godefroy the Grafted
        elif GetTalkListEntryResult() == 15:
            assert t200001400_x120(1039500800, 80020914)
        # Night's Cavalry
        elif GetTalkListEntryResult() == 16:
            assert t200001400_x120(1039510800, 80020915)
        # Elemer of the Briar
        elif GetTalkListEntryResult() == 17:
            assert t200001400_x120(1039540800, 80020916)
        # Sanguine Noble 
        elif GetTalkListEntryResult() == 18:
            assert t200001400_x120(1040530800, 80020917)
        # Fallingstar Beast    
        elif GetTalkListEntryResult() == 19:
            assert t200001400_x120(1041500800, 80020918)
        # Tree Sentinel Duo
        elif GetTalkListEntryResult() == 20:
            assert t200001400_x120(1041510800, 80020919)
        # Wormface 
        elif GetTalkListEntryResult() == 21:
            assert t200001400_x120(1041530800, 80020920)
        # Godskin Apostle
        elif GetTalkListEntryResult() == 22:
            assert t200001400_x120(1042550800, 80020921)
        else:
            return 0


    
# Caelid
def t200001400_x100():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Starscourge Radahn
        AddTalkListData(1, 80011000, -1)
        # Erdtree Burial Watchdog
        AddTalkListData(2, 80011001, -1)
        # Cemetery Shade
        AddTalkListData(3, 80011002, -1)
        # Beastman of Farum Azula
        AddTalkListData(4, 80011003, -1)
        # Putrid Crystalians
        AddTalkListData(5, 80011004, -1)
        # Cleanrot Knight
        AddTalkListData(6, 80011005, -1)
        # Frenzied Duelist
        AddTalkListData(7, 80011006, -1)
        # Magma Wyrm
        AddTalkListData(8, 80011007, -1)
        # Fallingstar Beast
        AddTalkListData(9, 80011008, -1)
        # Godskin Apostle
        AddTalkListData(10, 80011009, -1)
        # Decaying Ekzykes
        AddTalkListData(11, 80011010, -1)
        # Monstrous Dog
        AddTalkListData(12, 80011011, -1)
        # Ball-Bearing Hunter
        AddTalkListData(13, 80011012, -1)
        # Death Rite Bird
        AddTalkListData(14, 80011013, -1)
        # Commander O'Neil
        AddTalkListData(15, 80011014, -1)
        # Nox Priest and Swordstress
        AddTalkListData(16, 80011015, -1)
        # Battlemage Hugues
        AddTalkListData(17, 80011016, -1)
        # Crucible Knight
        AddTalkListData(18, 80011017, -1)
        # Black Blade Kindred
        AddTalkListData(19, 80011018, -1)
        # Flying Dragon Greyll
        AddTalkListData(20, 80011019, -1)
        # Night's Cavalry #1
        AddTalkListData(21, 80011020, -1)
        # Night's Cavalry #2
        AddTalkListData(22, 80011021, -1)
        # Putrid Tree Spirit
        AddTalkListData(23, 80011022, -1)
        # Putrid Avatar #1
        AddTalkListData(24, 80011023, -1)
        # Putrid Avatar #2
        AddTalkListData(25, 80011024, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Starscourge Radahn
        if GetTalkListEntryResult() == 1:
            assert t200001400_x121(1052380800, 76422, 80021000)
        # Erdtree Burial Watchdog
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x120(30140800, 80021001)
        # Cemetery Shade
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x120(30150800, 80021002)
        # Beastman of Farum Azula    
        elif GetTalkListEntryResult() == 4:
            assert t200001400_x120(31100800, 80021003)
        # Putrid Crystalians
        elif GetTalkListEntryResult() == 5:
            assert t200001400_x120(31110800, 80021004)
        # Cleanrot Knight
        elif GetTalkListEntryResult() == 6:
            assert t200001400_x120(31200800, 80021005)
        # Frenzied Duelist
        elif GetTalkListEntryResult() == 7:
            assert t200001400_x120(31210800, 80021006)
        # Magma Wyrm 
        elif GetTalkListEntryResult() == 8:
            assert t200001400_x120(32070800, 80021007)
        # Fallingstar Beast   
        elif GetTalkListEntryResult() == 9:
            assert t200001400_x120(32080800, 80021008)
        # Godskin Apostle
        elif GetTalkListEntryResult() == 10:
            assert t200001400_x120(34130800, 80021009)
        # Decaying Ekzykes
        elif GetTalkListEntryResult() == 11:
            assert t200001400_x120(1048370800, 80021010)
        # Monstrous Dog 
        elif GetTalkListEntryResult() == 12:
            assert t200001400_x120(1048400800, 80021011)
        # Ball-Bearing Hunter
        elif GetTalkListEntryResult() == 13:
            assert t200001400_x120(1048410800, 80021012)
        # Death Rite Bird  
        elif GetTalkListEntryResult() == 14:
            assert t200001400_x120(1049370850, 80021013)
        # Commander O'Neil  
        elif GetTalkListEntryResult() == 15:
            assert t200001400_x120(1049380800, 80021014)
        # Nox Priest and Swordstress
        elif GetTalkListEntryResult() == 16:
            assert t200001400_x120(1049390800, 80021015)
        # Battlemage Hugues
        elif GetTalkListEntryResult() == 17:
            assert t200001400_x120(1049390850, 80021016)
        # Crucible Knight
        elif GetTalkListEntryResult() == 18:
            assert t200001400_x120(1051360800, 80021017)
        # Black Blade Kindred  
        elif GetTalkListEntryResult() == 19:
            assert t200001400_x120(1051430800, 80021018)
        # Flying Dragon Greyll
        elif GetTalkListEntryResult() == 20:
            assert t200001400_x120(1052410800, 80021019)
        # Night's Cavalry #1 
        elif GetTalkListEntryResult() == 21:
            assert t200001400_x120(1049370800, 80021020)
        # Night's Cavalry #2
        elif GetTalkListEntryResult() == 22:
            assert t200001400_x120(1052410850, 80021021)
        # Putrid Tree Spirit
        elif GetTalkListEntryResult() == 23:
            assert t200001400_x120(30160800, 80021022)
        # Putrid Avatar #1
        elif GetTalkListEntryResult() == 24:
            assert t200001400_x120(1051400800, 80021023)
        # Putrid Avatar #2    
        elif GetTalkListEntryResult() == 25:
            assert t200001400_x120(1047400800, 80021024)
        else:
            return 0


    
# Capital Outskirts
def t200001400_x101():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Fell Twins
        AddTalkListData(1, 80011100, -1)
        # Ball-Bearing Hunter
        AddTalkListData(2, 80011101, -1)
        # Death Rite Bird
        AddTalkListData(3, 80011102, -1)
        # Draconic Tree Sentinel
        AddTalkListData(4, 80011103, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Fell Twins
        if GetTalkListEntryResult() == 1:
            assert t200001400_x120(34140850, 80021100)
        # Ball-Bearing Hunter  
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x120(1043530800, 80021100)
        # Death Rite Bird
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x120(1044530800, 80021100)
        # Draconic Tree Sentinel  
        elif GetTalkListEntryResult() == 4:
            assert t200001400_x120(1045520800, 80021100)
        else:
            return 0


    
# Leyndell, Royal Capital 
def t200001400_x102():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Godfrey, First Elden Lord
        AddTalkListData(1, 80011200, -1)
        # Morgott, the Omen King
        AddTalkListData(2, 80011201, -1)
        # Mohg, The Omen
        AddTalkListData(3, 80011202, -1)
        # Esgar, Priest of Blood
        AddTalkListData(4, 80011203, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Godfrey, First Elden Lord    
        if GetTalkListEntryResult() == 1:
            assert t200001400_x121(11000850, 71101, 80021200)
        # Morgott, the Omen King
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x121(11000800, 71100, 80021201)
        # Mohg, The Omen
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x121(35000800, 73500, 80021202)
        # Esgar, Priest of Blood
        elif GetTalkListEntryResult() == 4:
            assert t200001400_x120(35000850, 80021203)
        else:
            return 0


    
# Siofra River
def t200001400_x103():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Valiant Gargoyles
        AddTalkListData(1, 80011300, -1)
        # Dragonkin Soldier
        AddTalkListData(2, 80011301, -1)
        # Ancestor Spirit
        AddTalkListData(3, 80011302, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Valiant Gargoyles  
        if GetTalkListEntryResult() == 1:
            assert t200001400_x120(12020800, 80021300)
        # Dragonkin Soldier
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x120(12020830, 80021301)
        # Ancestor Spirit
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x120(12080800, 80021302)
        else:
            return 0


    
# Ainsel River
def t200001400_x104():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Dragonkin Soldier of Nokstella
        AddTalkListData(1, 80011400, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # BDragonkin Soldier of Nokstella 
        if GetTalkListEntryResult() == 1:
            assert t200001400_x121(12010800, 71210, 80021400)
        else:
            return 0


    
# Lake of Rot  
def t200001400_x105():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Dragonkin Soldier
        AddTalkListData(1, 80011500, -1)
        # Astel, Naturalborn of the Void
        AddTalkListData(2, 80011501, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Dragonkin Soldier  
        if GetTalkListEntryResult() == 1:
            assert t200001400_x120(12010850, 80021500)
        # Astel, Naturalborn of the Void
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x121(12040800, 71240, 80021501)
        else:
            return 0


    
# Deeproot Depths
def t200001400_x106():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Crucible Knight Sirulia
        AddTalkListData(1, 80011600, -1)
        # Fia's Champions
        AddTalkListData(2, 80011601, -1)
        # Lichdragon Fortissax
        AddTalkListData(3, 80011602, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Crucible Knight Sirulia 
        if GetTalkListEntryResult() == 1:
            assert t200001400_x120(12030390, 80021600)
        # Fia's Champions    
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x121(12030800, 71230, 80021601)
        # Lichdragon Fortissax 
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x120(12030850, 80021602)
        else:
            return 0


    
# Mohgwyn Palace
def t200001400_x107():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Mohg, Lord of Blood
        AddTalkListData(1, 80011700, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Mohg, Lord of Blood
        if GetTalkListEntryResult() == 1:
            assert t200001400_x121(12050800, 71250, 80021700)
        else:
            return 0


    
# Nokron, Eternal City 
def t200001400_x108():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Regal Ancestor Spirit
        AddTalkListData(1, 80011800, -1)
        # Mimic Tear
        AddTalkListData(2, 80011801, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Regal Ancestor Spirit   
        if GetTalkListEntryResult() == 1:
            assert t200001400_x120(12090800, 80021800)
        # Mimic Tear  
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x121(12020850, 71221, 80021801)
        else:
            return 0


    
# Consecrated Snowfield
def t200001400_x109():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Putrid Grave Warden Duelist
        AddTalkListData(1, 80011900, -1)
        # Astel, Stars of Darkness
        AddTalkListData(2, 80011901, -1)
        # Death Rite Bird
        AddTalkListData(3, 80011902, -1)
        # Putrid Avatar
        AddTalkListData(4, 80011903, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Putrid Grave Warden Duelist   
        if GetTalkListEntryResult() == 1:
            assert t200001400_x120(30190800, 80021900)
        # Astel, Stars of Darkness   
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x120(32110800, 80021901)
        # Death Rite Bird   
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x120(1048570800, 80021902)
        # Putrid Avatar
        elif GetTalkListEntryResult() == 4:
            assert t200001400_x120(1050570850, 80021903)
        else:
            return 0


    
# Mountaintops of the Giants  
def t200001400_x110():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Fire Giant
        AddTalkListData(1, 80012000, -1)
        # Ancient Hero of Zamor
        AddTalkListData(2, 80012001, -1)
        # Ulcerated Tree Sprit
        AddTalkListData(3, 80012002, -1)
        # Misbegotten Crusader
        AddTalkListData(4, 80012003, -1)
        # Spirit-Caller Snail
        AddTalkListData(5, 80012004, -1)
        # Black Blade Kindred
        AddTalkListData(6, 80012005, -1)
        # Great Wyrm Theodorix
        AddTalkListData(7, 80012006, -1)
        # Death Rite Bird
        AddTalkListData(8, 80012007, -1)
        # Commander Niall
        AddTalkListData(9, 80012008, -1)
        # Erdtree Avatar
        AddTalkListData(10, 80012009, -1)
        # Roundtable Knight Vyke
        AddTalkListData(11, 80012010, -1)
        # Borealis the Freezing Fog
        AddTalkListData(12, 80012011, -1)
        # Night's Cavalry #1
        AddTalkListData(13, 80012012, -1)
        # Night's Cavalry #2
        AddTalkListData(14, 80012013, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Fire Giant
        if GetTalkListEntryResult() == 1:
            assert t200001400_x121(1052520800, 76509, 80022000)
        # Ancient Hero of Zamor  
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x120(30170800, 80022001)
        # Ulcerated Tree Sprit
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x120(30180800, 80022002)
        # Misbegotten Crusader 
        elif GetTalkListEntryResult() == 4:
            assert t200001400_x120(31120800, 80022003)
        # Spirit-Caller Snail 
        elif GetTalkListEntryResult() == 5:
            assert t200001400_x120(31220800, 80022004)
        # Black Blade Kindred 
        elif GetTalkListEntryResult() == 6:
            assert t200001400_x120(1049520800, 80022005)
        # Great Wyrm Theodorix  
        elif GetTalkListEntryResult() == 7:
            assert t200001400_x120(1050560800, 80022006)
        # Death Rite Bird  
        elif GetTalkListEntryResult() == 8:
            assert t200001400_x120(1050570800, 80022007)
        # Commander Niall 
        elif GetTalkListEntryResult() == 9:
            assert t200001400_x120(1051570800, 80022008)
        # Erdtree Avatar  
        elif GetTalkListEntryResult() == 10:
            assert t200001400_x120(1052560800, 80022009)
        # Roundtable Knight Vyke  
        elif GetTalkListEntryResult() == 11:
            assert t200001400_x120(1053560800, 80022010)
        # Borealis the Freezing Fog
        elif GetTalkListEntryResult() == 12:
            assert t200001400_x120(1054560800, 80022011)
        # Night's Cavalry #1  
        elif GetTalkListEntryResult() == 13:
            assert t200001400_x120(1048510800, 80022012)
        # Night's Cavalry #2 
        elif GetTalkListEntryResult() == 14:
            assert t200001400_x120(1248550800, 80022013)
        else:
            return 0


    
# Leyndell, Ashen Capital     
def t200001400_x111():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Hoarah Loux
        AddTalkListData(1, 80012100, -1)
        # Sir Gideon Ofnir
        AddTalkListData(2, 80012101, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Hoarah Loux  
        if GetTalkListEntryResult() == 1:
            assert t200001400_x121(11050800, 71120, 80022100)
        # Sir Gideon Ofnir 
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x121(11050850, 71121, 80022101)
        else:
            return 0


    
# Crumbling Farum Azula  
def t200001400_x112():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Maliketh, The Black Blade
        AddTalkListData(1, 80012200, -1)
        # Dragonlord Placidusax
        AddTalkListData(2, 80012201, -1)
        # Godskin Duo
        AddTalkListData(3, 80012202, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Maliketh, The Black Blade
        if GetTalkListEntryResult() == 1:
            assert t200001400_x121(13000800, 71300, 80022200)
        # Dragonlord Placidusax 
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x121(13000830, 71301, 80022201)
        # Godskin Duo   
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x121(13000850, 71302, 80022202)
        else:
            return 0


    
# Miquella's Haligtree
def t200001400_x113():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Malenia, Blade of Miquella
        # AddTalkListData(1, 80012300, -1)
        # Loretta, Knight of the Haligtree
        AddTalkListData(2, 80012301, -1)
        # Stray Mimic Tear
        AddTalkListData(3, 80012302, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Malenia, Blade of Miquella
        if GetTalkListEntryResult() == 1:
            assert t200001400_x121(15000800, 71500, 80022300)
        # Loretta, Knight of the Haligtree
        elif GetTalkListEntryResult() == 2:
            assert t200001400_x121(15000850, 71505, 80022301)
        # Stray Mimic Tear
        elif GetTalkListEntryResult() == 3:
            assert t200001400_x120(30200800, 80022302)
        else:
            return 0


    
# Elden Throne
def t200001400_x114():
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Radagon and the Elden Beast
        AddTalkListData(1, 80012400, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Radagon and the Elden Beast
        if GetTalkListEntryResult() == 1:
            assert t200001400_x121(19000800, 71900, 80022400)
        else:
            return 0


    
# Boss Menu
def t200001400_x120(flag=_, message_id=_):
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Alive
        AddTalkListDataIf(GetEventFlag(flag) == 0, 2, 80000010, -1)
        # Dead
        AddTalkListDataIf(GetEventFlag(flag) == 1, 3, 80000011, -1)
        
        # Location
        AddTalkListData(4, message_id, -1)
        
        # Resurrect
        AddTalkListDataIf(GetEventFlag(flag) == 1, 1, 80000004, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))

        # Resurrect
        if GetTalkListEntryResult() == 1:
            if ComparePlayerInventoryNumber(3, 8185, 4, 1, 0) == 1:
                # Use a Larval Tear to accept rebirth?
                call = t200001400_x0(action2=22001000)
                
                if call.Done() and GetGenericDialogButtonResult() == 1:
                    SetEventFlag(flag, 0)
                elif call.Done():
                    continue
            else:
                # A Larval Tear is required for rebirth
                assert t200001400_x4(action1=22001002)
                continue
        else:
            return 0
    
# Boss Menu - Multi-stage Boss
def t200001400_x121(flag=_, flag2=_, message_id=_):
    """State 0,10"""
    assert GetCurrentStateElapsedTime() > 0.1

    """State 5"""
    c1_110()
    
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Alive
        AddTalkListDataIf(GetEventFlag(flag) == 0, 2, 80000010, -1)
        # Dead
        AddTalkListDataIf(GetEventFlag(flag) == 1, 3, 80000011, -1)
        
        # Location
        AddTalkListData(4, message_id, -1)
        
        # Resurrect
        AddTalkListDataIf(GetEventFlag(flag) == 1, 1, 80000004, -1)
        
        # Return
        AddTalkListData(99, 80000001, -1)
    
        c1_140(1)
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))

        # Resurrect
        if GetTalkListEntryResult() == 1:
            if ComparePlayerInventoryNumber(3, 8185, 4, 1, 0) == 1:
                # Use a Larval Tear to accept rebirth?
                call = t200001400_x0(action2=22001000)
                
                if call.Done() and GetGenericDialogButtonResult() == 1:
                    SetEventFlag(flag, 0)
                    SetEventFlag(flag2, 0)
                elif call.Done():
                    continue
            else:
                # A Larval Tear is required for rebirth
                assert t200001400_x4(action1=22001002)
                continue
        else:
            return 0
    
    