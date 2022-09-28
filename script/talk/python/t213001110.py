# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Hewg #1
#-----------------------------------------------------
def t213001110_1():
    """State 0,1"""
    # actionbutton:6210:"Talk"
    t213001110_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t213001110_1000():
    """State 0,2,3"""
    assert t213001110_x35()
    """State 1"""
    c1_120(1000)
    Quit()

def t213001110_2000():
    """State 0,2,3"""
    assert t213001110_x36()
    """State 1"""
    c1_120(2000)
    Quit()

def t213001110_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t213001110_x1():
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

def t213001110_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t213001110_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t213001110_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t213001110_x1()
    else:
        """State 4,7"""
        call = t213001110_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t213001110_x1()
    """State 9"""
    return 0

def t213001110_x4():
    """State 0,1"""
    assert t213001110_x1()
    """State 2"""
    return 0

def t213001110_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t213001110_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t213001110_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t213001110_x6(val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t213001110_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t213001110_x13(val1=val1, z1=z1)
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
            call = t213001110_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t213001110_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t213001110_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t213001110_x7(val2=10, val3=12):
    """State 0,1"""
    call = t213001110_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t213001110_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t213001110_x8(flag1=3223, val2=10, val3=12):
    """State 0,8"""
    assert t213001110_x34()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t213001110_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t213001110_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t213001110_x9(actionbutton1=6210, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t213001110_x10(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t213001110_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t213001110_x10(z6=_, val6=_):
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

def t213001110_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t213001110_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t213001110_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t213001110_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t213001110_x12():
    """State 0,1"""
    assert t213001110_x10(z6=1101, val6=1101)
    """State 2"""
    return 0

def t213001110_x13(val1=5, z1=1):
    """State 0,2"""
    assert t213001110_x23()
    """State 1"""
    call = t213001110_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t213001110_x25()
    """State 4"""
    return 0

def t213001110_x14():
    """State 0,1"""
    assert t213001110_x10(z6=1000, val6=1000)
    """State 2"""
    return 0

def t213001110_x15(val5=30):
    """State 0,1"""
    call = t213001110_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t213001110_x26()
    """State 3"""
    return 0

def t213001110_x16():
    """State 0,1"""
    assert t213001110_x10(z6=1100, val6=1100)
    """State 2"""
    return 0

def t213001110_x17(val2=10, val3=12):
    """State 0,5"""
    assert t213001110_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t213001110_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t213001110_x28()
    """Unused"""
    """State 6"""
    return 0

def t213001110_x18():
    """State 0,2"""
    call = t213001110_x10(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t213001110_x19():
    """State 0,1"""
    assert t213001110_x10(z6=1001, val6=1001)
    """State 2"""
    return 0

def t213001110_x20():
    """State 0,1"""
    assert t213001110_x10(z6=1103, val6=1103)
    """State 2"""
    return 0

def t213001110_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t213001110_x22(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t213001110_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t213001110_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t213001110_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t213001110_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t213001110_x23():
    """State 0,1"""
    assert t213001110_x24()
    """State 2"""
    return 0

def t213001110_x24():
    """State 0,1"""
    assert t213001110_x10(z6=1104, val6=1104)
    """State 2"""
    return 0

def t213001110_x25():
    """State 0,1"""
    call = t213001110_x10(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t213001110_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t213001110_x26():
    """State 0,1"""
    call = t213001110_x10(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t213001110_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t213001110_x27():
    """State 0,1"""
    call = t213001110_x10(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t213001110_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t213001110_x28():
    """State 0,1"""
    call = t213001110_x10(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t213001110_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t213001110_x29(text2=_, mode4=1):
    """State 0,4"""
    assert t213001110_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t213001110_x30(text1=_, z5=_, mode3=1):
    """State 0,5"""
    assert t213001110_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t213001110_x31():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t213001110_x32():
    """State 0,1"""
    assert t213001110_x10(z6=1002, val6=1002)
    """State 2"""
    return 0

def t213001110_x33():
    """State 0,1"""
    assert t213001110_x1()
    """State 2"""
    return 0

def t213001110_x34():
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

def t213001110_x35():
    """State 0,1"""
    if GetEventFlag(3225) == 1:
        """State 4"""
        def WhilePaused():
            c5_121(GetEventFlag(11102707) == 1 and not GetEventFlag(11109339), 9620)
        assert t213001110_x40()
        """State 3"""
        Label('L0')
        assert CheckSpecificPersonTalkHasEnded(0) == 1
        """State 8"""
        assert t213001110_x38()
    elif GetEventFlag(3226) == 1:
        """State 5"""
        assert t213001110_x43()
        Goto('L0')
    elif GetEventFlag(3227) == 1:
        """State 6"""
        assert t213001110_x45()
        Goto('L0')
    elif GetEventFlag(3228) == 1:
        """State 7"""
        assert t213001110_x48()
        Goto('L0')
    else:
        """State 2"""
        pass
    """State 9"""
    return 0

def t213001110_x36():
    """State 0,1"""
    if GetEventFlag(3225) == 1:
        """State 3"""
        assert t213001110_x41()
    else:
        """State 2"""
        # actionbutton:6210:"Talk"
        assert (t213001110_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                flag4=6000))
    """State 4"""
    return 0

def t213001110_x37():
    """State 0,5"""
    if not GetEventFlag(11102702):
        """State 1"""
        if not GetEventFlag(11109205) and not GetEventFlag(11102702):
            """State 9"""
            # talk:21300100:"You're a new face."
            assert t213001110_x29(text2=21300100, mode4=1)
            """State 2"""
            SetEventFlag(11109205, 1)
        elif GetEventFlag(11102703) == 1 and not GetEventFlag(11109209):
            """State 13"""
            # talk:21304200:"Ah. You, is it?"
            def WhilePaused():
                RequestAnimation(20016, -1)
            assert t213001110_x29(text2=21304200, mode4=1)
            """State 8"""
            SetEventFlag(11109209, 1)
        elif GetEventFlag(11102707) == 1 and not GetEventFlag(11109339):
            """State 14"""
            # talk:21308100:"Oh, it's you."
            def WhilePaused():
                RequestAnimation(20018, -1)
            assert t213001110_x29(text2=21308100, mode4=1)
            """State 6"""
            SetEventFlag(11109339, 1)
        elif (GetEventFlag(9101) == 1 or GetEventFlag(9104) == 1 or GetEventFlag(9112) == 1 or GetEventFlag(9120)
              == 1 or GetEventFlag(9122) == 1 or GetEventFlag(9130) == 1):
            """State 7"""
            if not GetEventFlag(11109206):
                """State 10"""
                # talk:21303000:"Now, look at you."
                assert t213001110_x29(text2=21303000, mode4=1)
                """State 4"""
                SetEventFlag(11109206, 1)
            else:
                """State 11"""
                Label('L0')
                # talk:21301000:"Well, where've you been hiding?"
                assert t213001110_x29(text2=21301000, mode4=1)
        else:
            Goto('L0')
        """State 3"""
        SetEventFlag(11102702, 1)
    else:
        """State 12"""
        # talk:21300200:"Back already?"
        assert t213001110_x29(text2=21300200, mode4=1)
    """State 15"""
    return 0

def t213001110_x38():
    """State 0,8"""
    c1_110()
    while True:
        """State 1"""
        ClearTalkListData()
        """State 30"""
        assert t213001110_x63()
        """State 11"""
        if GetEventFlag(3225) == 1:
            """State 14"""
            assert t213001110_x50()
        elif GetEventFlag(3226) == 1:
            """State 23"""
            assert t213001110_x57()
        elif GetEventFlag(3227) == 1:
            """State 27"""
            assert t213001110_x61()
        else:
            """State 12"""
            pass
        """State 3"""
        # action:22130001:"Strengthen armament"
        # AddTalkListData(1, 22130001, -1)
        # action:22130003:"Ashes of War"
        AddTalkListData(2, 22130003, -1)
        # action:22130018:"Ash of War duplication"
        AddTalkListDataIf(GetEventFlag(65800) == 1, 20, 22130018, -1)
        # action:20000011:"Sell"
        AddTalkListData(4, 20000011, -1)
        # action:22130004:"About prayer"
        AddTalkListDataIf(GetEventFlag(11109217) == 1, 5, 22130004, -1)
        # action:22130005:"About Roderika"
        AddTalkListDataIf(GetEventFlag(11109218) == 1, 6, 22130005, -1)
        # action:22130006:"About Roderika"
        AddTalkListDataIf(GetEventFlag(11109219) == 1, 7, 22130006, -1)
        # action:22130007:"About Roderika"
        AddTalkListDataIf(GetEventFlag(11109331) == 1, 8, 22130007, -1)
        # action:22130008:"About Roderika"
        AddTalkListDataIf(GetEventFlag(11109332) == 1, 9, 22130008, -1)
        # action:22130009:"Let's talk a while"
        AddTalkListDataIf(GetEventFlag(11109333) == 1, 10, 22130009, -1)
        # action:22130010:"About the chains on your legs"
        AddTalkListDataIf(GetEventFlag(11109334) == 1, 11, 22130010, -1)
        # action:22130011:"You're a prisoner?"
        AddTalkListDataIf(GetEventFlag(11109335) == 1, 12, 22130011, -1)
        # action:22130012:"About the god-slaying weapon"
        AddTalkListDataIf(GetEventFlag(11109233) == 1, 13, 22130012, -1)
        # action:22130013:"About the god-slaying weapon"
        AddTalkListDataIf(GetEventFlag(11109234) == 1, 14, 22130013, -1)
        # action:22130014:"Why are you still making weapons?"
        AddTalkListDataIf(GetEventFlag(11109235) == 1, 15, 22130014, -1)
        # action:22130015:"What happened to her?"
        AddTalkListDataIf(GetEventFlag(11109236) == 1, 16, 22130015, -1)
        # action:22130016:"About yourself"
        AddTalkListDataIf(GetEventFlag(11109248) == 1, 17, 22130016, -1)
        # action:20000009:"Leave"
        AddTalkListData(99, 20000009, -1)
        """State 6"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 2"""
        if GetTalkListEntryResult() == 1:
            """State 5"""
            CombineMenuFlagAndEventFlag(6001, 232)
            CombineMenuFlagAndEventFlag(6001, 233)
            CombineMenuFlagAndEventFlag(6001, 234)
            CombineMenuFlagAndEventFlag(6001, 235)
            c1_141(9)
            """State 4"""
            OpenEnhanceShop(0)
            assert not (CheckSpecificPersonMenuIsOpen(9, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            continue
        elif GetTalkListEntryResult() == 2:
            """State 9"""
            OpenEquipmentChangeOfPurposeShop()
            c1_141(7)
            assert not (CheckSpecificPersonMenuIsOpen(7, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            continue
        elif GetTalkListEntryResult() == 20:
            """State 13"""
            OpenAshOfWarShop(112000, 112099)
            assert not (CheckSpecificPersonMenuIsOpen(27, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            continue
        elif GetTalkListEntryResult() == 4:
            """State 7"""
            OpenSellShop(-1, -1)
            c1_141(6)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            continue
        elif GetTalkListEntryResult() == 5:
            """State 15"""
            assert t213001110_x51()
        elif GetTalkListEntryResult() == 6:
            """State 16"""
            assert t213001110_x52()
        elif GetTalkListEntryResult() == 7:
            """State 17"""
            assert t213001110_x39()
        elif GetTalkListEntryResult() == 8:
            """State 18"""
            assert t213001110_x49()
        elif GetTalkListEntryResult() == 9:
            """State 19"""
            assert t213001110_x53()
        elif GetTalkListEntryResult() == 10:
            """State 20"""
            assert t213001110_x54()
        elif GetTalkListEntryResult() == 11:
            """State 21"""
            assert t213001110_x55()
        elif GetTalkListEntryResult() == 12:
            """State 22"""
            assert t213001110_x56()
        elif GetTalkListEntryResult() == 13:
            """State 24"""
            assert t213001110_x58()
        elif GetTalkListEntryResult() == 14:
            """State 25"""
            assert t213001110_x59()
        elif GetTalkListEntryResult() == 15:
            """State 26"""
            assert t213001110_x44()
        elif GetTalkListEntryResult() == 16:
            """State 29"""
            assert t213001110_x60()
        elif GetTalkListEntryResult() == 17:
            """State 28"""
            assert t213001110_x62()
        else:
            """State 31"""
            return 0
        """State 10"""
        assert CheckSpecificPersonTalkHasEnded(0) == 1

def t213001110_x39():
    """State 0,7"""
    # talk:21305100:"The girl? What about her?"
    assert t213001110_x29(text2=21305100, mode4=1)
    while True:
        """State 5"""
        c1_110()
        """State 1"""
        ClearTalkListData()
        """State 3"""
        # action:22131000:"Would you watch over Roderika?"
        AddTalkListDataIf(not GetEventFlag(11109213), 1, 22131000, -1)
        # action:22131001:"Nothing"
        AddTalkListDataIf(not GetEventFlag(11109213), 2, 22131001, -1)
        # action:22131002:"It's what she wants"
        AddTalkListDataIf(GetEventFlag(11109213) == 1, 3, 22131002, -1)
        # action:22131003:"Understood"
        AddTalkListDataIf(GetEventFlag(11109213) == 1, 4, 22131003, -1)
        """State 4"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 2"""
        if GetTalkListEntryResult() == 1:
            """State 8"""
            # talk:21305200:"Are you out of your mind?"
            assert t213001110_x29(text2=21305200, mode4=1)
            """State 6"""
            SetEventFlag(11109213, 1)
            continue
        elif GetTalkListEntryResult() == 2:
            pass
        elif GetTalkListEntryResult() == 3:
            """State 9"""
            # talk:21305300:"I refuse to believe it."
            assert t213001110_x29(text2=21305300, mode4=1)
        elif GetTalkListEntryResult() == 4:
            pass
        """State 10"""
        return 0

def t213001110_x40():
    """State 0,1"""
    assert t213001110_x37()
    """State 2"""
    return 0

def t213001110_x41():
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6210:"Talk"
        call = t213001110_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                             flag4=6000)
        if call.Done():
            break
        elif GetEventFlag(11102704) == 1 and not GetEventFlag(11102703) and not GetEventFlag(11109209):
            pass
        elif GetEventFlag(11102708) == 1 and not GetEventFlag(11102707) and not GetEventFlag(11109339):
            Goto('L0')
        """State 4"""
        # talk:21304000:"Your divinity, have mercy, and grant me forgiveness."
        call = t213001110_x30(text1=21304000, z5=11102703, mode3=1)
        if call.Done():
            continue
        elif GetEventFlag(11102702) == 1:
            """State 1"""
            continue
        """State 5"""
        Label('L0')
        # talk:21308000:"No, no, no, no..."
        call = t213001110_x30(text1=21308000, z5=11102707, mode3=1)
        if call.Done():
            pass
        elif GetEventFlag(11102702) == 1:
            """State 2"""
            pass
    """State 6"""
    return 0

def t213001110_x42():
    """State 0,1"""
    if not GetEventFlag(11109238):
        """State 4"""
        # talk:21310000:"I knew you'd be back."
        assert t213001110_x29(text2=21310000, mode4=1)
        """State 2"""
        SetEventFlag(11109238, 1)
    else:
        """State 3"""
        if not GetEventFlag(9114):
            """State 5"""
            # talk:21310100:"Lay out your arms. Let's get smithing."
            assert t213001110_x29(text2=21310100, mode4=1)
        else:
            """State 6"""
            # talk:21312300:"I'll smith...as long as you like."
            assert t213001110_x29(text2=21312300, mode4=1)
    """State 7"""
    return 0

def t213001110_x43():
    """State 0,1"""
    assert t213001110_x42()
    """State 2"""
    return 0

def t213001110_x44():
    """State 0,2"""
    # talk:21311000:"Weren't you listening?"
    assert t213001110_x29(text2=21311000, mode4=1)
    """State 1"""
    SetEventFlag(11109227, 1)
    """State 3"""
    return 0

def t213001110_x45():
    """State 0,1"""
    assert t213001110_x46()
    """State 2"""
    return 0

def t213001110_x46():
    """State 0,2"""
    # talk:21314000:"Who are you?"
    assert t213001110_x29(text2=21314000, mode4=1)
    """State 1"""
    SetEventFlag(11109246, 1)
    """State 3"""
    return 0

def t213001110_x47():
    """State 0,2"""
    # talk:21315000:"Now, let's get smithing..."
    assert t213001110_x29(text2=21315000, mode4=1)
    """State 1"""
    SetEventFlag(11109306, 1)
    """State 3"""
    return 0

def t213001110_x48():
    """State 0,1"""
    assert t213001110_x47()
    """State 2"""
    return 0

def t213001110_x49():
    """State 0,2"""
    # talk:21306000:"I spoke with the girl."
    assert t213001110_x29(text2=21306000, mode4=1)
    """State 1"""
    SetEventFlag(11109207, 1)
    """State 3"""
    return 0

def t213001110_x50():
    """State 0,2"""
    if not GetEventFlag(11109336) and GetEventFlag(11102703) == 1:
        """State 1"""
        SetEventFlag(11109217, 1)
    elif GetEventFlag(3707) == 1 and not GetEventFlag(11109210):
        """State 3"""
        SetEventFlag(11109218, 1)
    elif GetEventFlag(11109256) == 1 and not GetEventFlag(11109213):
        """State 4"""
        SetEventFlag(11109219, 1)
    elif GetEventFlag(3708) == 1 and GetEventFlag(11109213) == 1 and not GetEventFlag(11109207):
        """State 5"""
        SetEventFlag(11109331, 1)
    elif GetEventFlag(11109267) == 1 and not GetEventFlag(11109211):
        """State 6"""
        SetEventFlag(11109332, 1)
    elif not GetEventFlag(110) and GetEventFlag(1054539216) == 1 and not GetEventFlag(11109229):
        """State 7"""
        SetEventFlag(11109333, 1)
    elif not GetEventFlag(11109212):
        """State 8"""
        SetEventFlag(11109334, 1)
    elif GetEventFlag(11109212) == 1 and not GetEventFlag(11109216):
        """State 9"""
        SetEventFlag(11109335, 1)
    else:
        """State 10"""
        pass
    """State 11"""
    return 0

def t213001110_x51():
    """State 0,2"""
    # talk:21304100:"Those words were not meant for you."
    assert t213001110_x29(text2=21304100, mode4=1)
    """State 1"""
    SetEventFlag(11109336, 1)
    """State 3"""
    return 0

def t213001110_x52():
    """State 0,2"""
    # talk:21305000:"The girl you brought here..."
    assert t213001110_x29(text2=21305000, mode4=1)
    """State 1"""
    SetEventFlag(11109210, 1)
    """State 3"""
    return 0

def t213001110_x53():
    """State 0,2"""
    # talk:21307000:"The girl has come a long way."
    assert t213001110_x29(text2=21307000, mode4=1)
    """State 1"""
    SetEventFlag(11109211, 1)
    """State 3"""
    return 0

def t213001110_x54():
    """State 0,2"""
    # talk:21309000:"Are you having second thoughts?"
    assert t213001110_x29(text2=21309000, mode4=1)
    """State 1"""
    SetEventFlag(11109229, 1)
    """State 3"""
    return 0

def t213001110_x55():
    """State 0,2"""
    # talk:21302000:"I see you've noticed the chains."
    assert t213001110_x29(text2=21302000, mode4=1)
    """State 1"""
    SetEventFlag(11109212, 1)
    """State 3"""
    return 0

def t213001110_x56():
    """State 0,2"""
    # talk:21302100:"Nah, don't read too much into it."
    assert t213001110_x29(text2=21302100, mode4=1)
    """State 1"""
    SetEventFlag(11109216, 1)
    """State 3"""
    return 0

def t213001110_x57():
    """State 0,1"""
    if not GetEventFlag(11109227) and GetEventFlag(11109275) == 1:
        """State 2"""
        SetEventFlag(11109235, 1)
    elif not GetEventFlag(11109232) and GetEventFlag(11109276) == 1:
        """State 3"""
        SetEventFlag(11109236, 1)
    else:
        """State 4"""
        pass
    """State 5"""
    if GetEventFlag(9114) == 1 and not GetEventFlag(11109230):
        """State 7"""
        SetEventFlag(11109233, 1)
    elif GetEventFlag(11109230) == 1 and not GetEventFlag(11109231):
        """State 8"""
        SetEventFlag(11109234, 1)
    else:
        """State 6"""
        pass
    """State 9"""
    return 0

def t213001110_x58():
    """State 0,2"""
    # talk:21313000:"Use my masterpiece to slay a god."
    assert t213001110_x29(text2=21313000, mode4=1)
    """State 1"""
    SetEventFlag(11109230, 1)
    """State 3"""
    return 0

def t213001110_x59():
    """State 0,2"""
    # talk:21313100:"I can't hold on much longer."
    assert t213001110_x29(text2=21313100, mode4=1)
    """State 1"""
    SetEventFlag(11109231, 1)
    """State 3"""
    return 0

def t213001110_x60():
    """State 0,2"""
    # talk:21311100:"I've upset the girl."
    assert t213001110_x29(text2=21311100, mode4=1)
    """State 1"""
    SetEventFlag(11109232, 1)
    """State 3"""
    return 0

def t213001110_x61():
    """State 0,2"""
    if not GetEventFlag(11109247):
        """State 1"""
        SetEventFlag(11109248, 1)
    else:
        """State 3"""
        pass
    """State 4"""
    return 0

def t213001110_x62():
    """State 0,2"""
    # talk:21314100:"Could you tell me what happened?"
    assert t213001110_x29(text2=21314100, mode4=1)
    """State 1"""
    SetEventFlag(11109247, -1)
    """State 3"""
    return 0

def t213001110_x63():
    """State 0,1"""
    SetEventFlag(11109217, 0)
    SetEventFlag(11109218, 0)
    SetEventFlag(11109219, 0)
    SetEventFlag(11109331, 0)
    SetEventFlag(11109332, 0)
    SetEventFlag(11109333, 0)
    SetEventFlag(11109334, 0)
    SetEventFlag(11109335, 0)
    """State 2"""
    SetEventFlag(11109235, 0)
    SetEventFlag(11109236, 0)
    SetEventFlag(11109233, 0)
    SetEventFlag(11109234, 0)
    """State 3"""
    SetEventFlag(11109248, 0)
    """State 4"""
    return 0

