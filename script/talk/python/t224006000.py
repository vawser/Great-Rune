# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Blaidd
#-----------------------------------------------------
def t224006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t224006000_x6(flag2=3763, flag3=3761, flag4=3762, val1=12, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag5=6000, flag6=6001, flag7=6000, flag8=6000, flag9=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t224006000_1000():
    """State 0,2,3"""
    assert t224006000_x37()
    """State 1"""
    c1_120(1000)
    Quit()

def t224006000_1101():
    """State 0,2,3"""
    assert t224006000_x38()
    """State 1"""
    c1_120(1101)
    Quit()

def t224006000_1102():
    """State 0,2,3"""
    t224006000_x39()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t224006000_2000():
    """State 0,2,3"""
    assert t224006000_x40()
    """State 1"""
    c1_120(2000)
    Quit()

def t224006000_x0(actionbutton1=_, flag6=6001, flag10=6000, flag11=6000, flag12=6000, flag13=6000, flag5=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag6) == 1 or GetEventFlag(flag10) == 1 or GetEventFlag(flag11) == 1 or
                GetEventFlag(flag12) == 1 or GetEventFlag(flag13) == 1)
        """State 4"""
        assert not GetEventFlag(flag5)
        """State 2"""
        if GetEventFlag(flag5) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag6) and not GetEventFlag(flag10) and not GetEventFlag(flag11) and not
              GetEventFlag(flag12) and not GetEventFlag(flag13)):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t224006000_x1():
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

def t224006000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t224006000_x3(action1=22241010):
    """State 0,1"""
    # action:22241010:"Cannot do this during multiplayer"
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t224006000_x4(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t224006000_x20()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t224006000_x1()
    else:
        """State 4,7"""
        call = t224006000_x34()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t224006000_x1()
    """State 9"""
    return 0

def t224006000_x5():
    """State 0,1"""
    assert t224006000_x1()
    """State 2"""
    return 0

def t224006000_x6(flag2=3763, flag3=3761, flag4=3762, val1=12, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag5=6000, flag6=6001, flag7=6000, flag8=6000, flag9=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t224006000_x23(flag2=flag2, flag3=flag3, flag4=flag4, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag5=flag5, flag6=flag6,
                              flag7=flag7, flag8=flag8, flag9=flag9, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t224006000_x22()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t224006000_x7(val1=12, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag5=6000, flag6=6001,
                  flag7=6000, flag8=6000, flag9=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t224006000_x10(actionbutton1=actionbutton1, flag5=flag5, flag6=flag6, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t224006000_x14(val1=val1, z1=z1)
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
        elif GetEventFlag(flag9) == 1:
            Goto('L0')
        elif GetEventFlag(flag7) == 1 and not GetEventFlag(flag8) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t224006000_x16(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t224006000_x27() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t224006000_x12(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t224006000_x8(val2=10, val3=12):
    """State 0,1"""
    call = t224006000_x18(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t224006000_x4(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t224006000_x9(flag2=3763, val2=10, val3=12):
    """State 0,8"""
    assert t224006000_x36()
    """State 1"""
    if GetEventFlag(flag2) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t224006000_x21()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t224006000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t224006000_x10(actionbutton1=6000, flag5=6000, flag6=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t224006000_x11(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t224006000_x0(actionbutton1=actionbutton1, flag6=flag6, flag10=6000, flag11=6000, flag12=6000,
                flag13=6000, flag5=flag5))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t224006000_x11(z6=_, val6=_):
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

def t224006000_x12(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t224006000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t224006000_x13()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t224006000_x28()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t224006000_x13():
    """State 0,1"""
    assert t224006000_x11(z6=1101, val6=1101)
    """State 2"""
    return 0

def t224006000_x14(val1=12, z1=1):
    """State 0,2"""
    assert t224006000_x24()
    """State 1"""
    call = t224006000_x15()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t224006000_x26()
    """State 4"""
    return 0

def t224006000_x15():
    """State 0,1"""
    assert t224006000_x11(z6=1000, val6=1000)
    """State 2"""
    return 0

def t224006000_x16(val5=12):
    """State 0,1"""
    call = t224006000_x17()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t224006000_x27()
    """State 3"""
    return 0

def t224006000_x17():
    """State 0,1"""
    assert t224006000_x11(z6=1100, val6=1100)
    """State 2"""
    return 0

def t224006000_x18(val2=10, val3=12):
    """State 0,5"""
    assert t224006000_x36()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t224006000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t224006000_x29()
    """Unused"""
    """State 6"""
    return 0

def t224006000_x19():
    """State 0,2"""
    call = t224006000_x11(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t224006000_x20():
    """State 0,1"""
    assert t224006000_x11(z6=1001, val6=1001)
    """State 2"""
    return 0

def t224006000_x21():
    """State 0,1"""
    assert t224006000_x11(z6=1103, val6=1103)
    """State 2"""
    return 0

def t224006000_x22():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t224006000_x23(flag2=3763, flag3=3761, flag4=3762, val1=12, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag5=6000, flag6=6001, flag7=6000, flag8=6000, flag9=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t224006000_x7(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, flag9=flag9, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag2) == 1:
            """State 3"""
            Label('L0')
            call = t224006000_x9(flag2=flag2, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag2):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag3) == 1 or GetEventFlag(flag4) == 1:
            """State 2"""
            call = t224006000_x8(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag2) == 1:
                Goto('L0')
            elif not GetEventFlag(flag3) and not GetEventFlag(flag4):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t224006000_x35() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t224006000_x24():
    """State 0,1"""
    assert t224006000_x25()
    """State 2"""
    return 0

def t224006000_x25():
    """State 0,1"""
    assert t224006000_x11(z6=1104, val6=1104)
    """State 2"""
    return 0

def t224006000_x26():
    """State 0,1"""
    call = t224006000_x11(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t224006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t224006000_x27():
    """State 0,1"""
    call = t224006000_x11(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t224006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t224006000_x28():
    """State 0,1"""
    call = t224006000_x11(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t224006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t224006000_x29():
    """State 0,1"""
    call = t224006000_x11(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t224006000_x5()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t224006000_x30(text5=_, z5=_, mode5=1):
    """State 0,5"""
    assert t224006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text5, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode5:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(z5, 1)
    """State 6"""
    return 0

def t224006000_x31(text4=_, mode4=1):
    """State 0,4"""
    assert t224006000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text4, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode4:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t224006000_x32(text1=_, flag1=_, mode3=1):
    """State 0,5"""
    assert t224006000_x33() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag1, 1)
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

def t224006000_x33():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t224006000_x34():
    """State 0,1"""
    assert t224006000_x11(z6=1002, val6=1002)
    """State 2"""
    return 0

def t224006000_x35():
    """State 0,1"""
    assert t224006000_x1()
    """State 2"""
    return 0

def t224006000_x36():
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

def t224006000_x37():
    """State 0,1"""
    if GetEventFlag(3765) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimation(20039, -1)
        assert t224006000_x41()
    elif GetEventFlag(3767) == 1 or GetEventFlag(3766) == 1:
        """State 4"""
        def WhilePaused():
            RequestAnimation(20039, -1)
        assert t224006000_x59()
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t224006000_x38():
    """State 0,1"""
    if GetEventFlag(3765) == 1:
        """State 2"""
        # talk:22480000:"Ngh!", talk:22480100:"Enough of that, Tarnished."
        assert t224006000_x78(text2=22480000, text3=22480100)
    else:
        """State 3"""
        # talk:22481000:"Agh.", talk:22481100:"Cease this treachery at once."
        assert t224006000_x78(text2=22481000, text3=22481100)
    """State 4"""
    return 0

def t224006000_x39():
    """State 0,1"""
    if GetEventFlag(3765) == 1:
        """State 2"""
        # talk:22480200:"If that's the cloth you're cut from,"
        t224006000_x81(text1=22480200, flag1=1034499202)
        def WhilePaused():
            RequestAnimation(20039, -1)
        Quit()
    else:
        """State 3"""
        # talk:22481200:"This is a true shame."
        t224006000_x81(text1=22481200, flag1=1034499204)
        def WhilePaused():
            RequestAnimation(20039, -1)
        Quit()
    """Unused"""
    """State 4"""
    return 0

def t224006000_x40():
    """State 0,3"""
    # actionbutton:6360:"Talk"
    call = t224006000_x0(actionbutton1=6360, flag6=6001, flag10=6000, flag11=6000, flag12=6000, flag13=6000,
                         flag5=6000)
    if call.Done():
        """State 4"""
        return 0
    elif GetEventFlag(3768) == 1:
        """State 1,2"""
        Quit()

def t224006000_x41():
    """State 0,1"""
    if GetEventFlag(1034499205) == 1:
        """State 2"""
        if GetEventFlag(1034499206) == 1:
            """State 5"""
            assert t224006000_x45()
        else:
            """State 4"""
            assert t224006000_x44()
    else:
        """State 3"""
        assert t224006000_x43()
    """State 6"""
    return 0

def t224006000_x42():
    """State 0,2"""
    CombineMenuFlagAndEventFlag(6001, 232)
    CombineMenuFlagAndEventFlag(6001, 233)
    CombineMenuFlagAndEventFlag(6001, 234)
    CombineMenuFlagAndEventFlag(6001, 235)
    c1_141(9)
    """State 1"""
    OpenEnhanceShop(0)
    if not (CheckSpecificPersonMenuIsOpen(9, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
        pass
    elif IsMultiplayerInProgress() == 1:
        """State 3"""
        assert t224006000_x1()
    """State 4"""
    return 0

def t224006000_x43():
    """State 0,1"""
    # talk:22400100:"Well, look at you. We don't receive many visitors."
    assert t224006000_x30(text5=22400100, z5=1034499205, mode5=1)
    """State 2"""
    return 0

def t224006000_x44():
    """State 0,3"""
    # talk:22401000:"Oh, pardon me. It's hardly my place to ask, is it."
    assert t224006000_x30(text5=22401000, z5=1034499206, mode5=1)
    """State 1"""
    SetEventFlag(1034499208, 1)
    SetEventFlag(1034499209, 1)
    SetEventFlag(1034499230, 1)
    """State 2"""
    assert t224006000_x46()
    """State 4"""
    return 0

def t224006000_x45():
    """State 0,1"""
    if not GetEventFlag(1034492702):
        """State 2"""
        if not GetEventFlag(1034499207):
            """State 6"""
            # talk:22401100:"Well, it's kind of you to speak to me again."
            assert t224006000_x30(text5=22401100, z5=1034499207, mode5=1)
        else:
            """State 4"""
            # talk:22401200:"Brave Tarnished. Here to put my old bones to work again?"
            assert t224006000_x31(text4=22401200, mode4=1)
    else:
        """State 5"""
        # talk:22401500:"Something else for you?"
        assert t224006000_x31(text4=22401500, mode4=1)
    """State 3"""
    assert t224006000_x46()
    """State 7"""
    return 0

def t224006000_x46():
    """State 0,1"""
    SetEventFlag(1034492702, 1)
    while Loop('mainloop'):
        """State 2"""
        Label('L0')
        c1_110()
        while True:
            """State 3"""
            ClearTalkListData()
            """State 9"""
            assert t224006000_x47()
            """State 4"""
            ShowShopMessage(1)
            assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 5"""
            if GetTalkListEntryResult() == 1:
                """State 6,10"""
                assert t224006000_x48()
            elif GetTalkListEntryResult() == 2:
                Break('mainloop')
            elif GetTalkListEntryResult() == 3:
                """State 11"""
                assert t224006000_x49()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 4:
                """State 13"""
                assert t224006000_x51()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 5:
                """State 14"""
                assert t224006000_x52()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 20:
                """State 7,8"""
                OpenRegularShop(100225, 100249)
                assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            else:
                """State 15"""
                return 0
    """State 12"""
    assert t224006000_x50()
    Goto('L0')

def t224006000_x47():
    """State 0,1"""
    # action:22240020:"Purchase"
    AddTalkListData(20, 22240020, -1)
    # action:22240000:"Strengthen armaments"
    AddTalkListData(1, 22240000, -1)
    """State 3"""
    assert t224006000_x53()
    """State 2"""
    # action:20000009:"Leave"
    AddTalkListData(99, 20000009, -1)
    """State 4"""
    return 0

def t224006000_x48():
    """State 0,1"""
    if IsMultiplayerInProgress() == 1:
        """State 3"""
        # action:22241010:"Cannot do this during multiplayer"
        assert t224006000_x3(action1=22241010)
    else:
        """State 2"""
        def WhilePaused():
            RequestAnimation(20042, -1)
        assert t224006000_x42()
    """State 4"""
    return 0

def t224006000_x49():
    """State 0,1"""
    # talk:22401400:"Oh, watch out, there."
    assert t224006000_x30(text5=22401400, z5=1034499211, mode5=1)
    """State 2"""
    return 0

def t224006000_x50():
    """State 0,1"""
    # talk:22401300:"Brave Tarnished. A word of warning, if you please."
    assert t224006000_x30(text5=22401300, z5=1034499210, mode5=1)
    """State 2"""
    return 0

def t224006000_x51():
    """State 0,1"""
    # talk:22401600:"I've explained the peril."
    assert t224006000_x31(text4=22401600, mode4=1)
    """State 2"""
    return 0

def t224006000_x52():
    """State 0,2"""
    # talk:22401700:"Blaidd actually did that, did he?"
    assert t224006000_x30(text5=22401700, z5=1034499212, mode5=1)
    """State 1"""
    SetEventFlag(1034509360, 1)
    """State 3"""
    return 0

def t224006000_x53():
    """State 0,1"""
    assert t224006000_x54()
    """State 2"""
    assert t224006000_x55()
    """State 3"""
    assert t224006000_x56()
    """State 4"""
    return 0

def t224006000_x54():
    """State 0,2"""
    SetEventFlag(1034499213, 0)
    SetEventFlag(1034499214, 0)
    SetEventFlag(1034499215, 0)
    SetEventFlag(1034499216, 0)
    """State 1"""
    SetEventFlagIf(not GetEventFlag(1034499211), 1034499214, 1)
    """State 3"""
    SetEventFlagIf(not GetEventFlag(1034499210), 1034499213, 1)
    SetEventFlagIf(GetEventFlag(1034499210) == 1, 1034499216, 1)
    """State 4"""
    SetEventFlagIf(not GetEventFlag(1034499212) and GetEventFlag(1044349256) == 1, 1034499215, 1)
    """State 5"""
    return 0

def t224006000_x55():
    """State 0,1"""
    if GetEventFlag(1034499214) == 1:
        """State 2"""
        SetEventFlag(1034499213, 0)
        SetEventFlag(1034499215, 0)
    else:
        """State 5"""
        if GetEventFlag(1034499213) == 1:
            """State 3"""
            SetEventFlag(1034499214, 0)
            SetEventFlag(1034499215, 0)
        else:
            """State 6"""
            if GetEventFlag(1034499215) == 1:
                """State 4"""
                SetEventFlag(1034499213, 0)
                SetEventFlag(1034499214, 0)
            else:
                pass
    """State 7"""
    return 0

def t224006000_x56():
    """State 0,1"""
    # action:22240001:"Talk"
    AddTalkListDataIf(GetEventFlag(1034499213) == 1, 2, 22240001, -1)
    # action:22240002:"Please take care"
    AddTalkListDataIf(GetEventFlag(1034499214) == 1, 3, 22240002, -1)
    # action:22240014:"Blaidd sent me"
    AddTalkListDataIf(GetEventFlag(1034499215) == 1, 5, 22240014, -1)
    # action:22240013:"About advice"
    AddTalkListDataIf(GetEventFlag(1034499216) == 1, 4, 22240013, -1)
    """State 2"""
    return 0

def t224006000_x57():
    """State 0,1"""
    if not GetEventFlag(1034492702):
        """State 2"""
        ShuffleRNGSeedIf(not CompareRNGValue(0, 0) != -1, 2)
        if CompareRNGValue(0, 0) == 1:
            """State 3"""
            # talk:22403600:"Well, my fellow. How may I serve you?"
            assert t224006000_x31(text4=22403600, mode4=1)
        else:
            """State 4"""
            # talk:22403700:"Greetings, my fellow. How can I help?"
            assert t224006000_x31(text4=22403700, mode4=1)
    else:
        """State 5"""
        # talk:22403800:"Something else for you?"
        assert t224006000_x31(text4=22403800, mode4=1)
    """State 6"""
    return 0

def t224006000_x58():
    """State 0,1"""
    SetEventFlag(1034492702, 1)
    while Loop('mainloop'):
        """State 2"""
        c1_110()
        while True:
            """State 3"""
            Label('L0')
            ClearTalkListData()
            """State 10"""
            assert t224006000_x60()
            """State 4"""
            ShowShopMessage(1)
            assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 5"""
            if GetTalkListEntryResult() == 1:
                Break('mainloop')
            elif GetTalkListEntryResult() == 2:
                """State 11"""
                assert t224006000_x62()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 3:
                """State 15"""
                assert t224006000_x79()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 4:
                """State 16"""
                assert t224006000_x69()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 5:
                """State 17"""
                assert t224006000_x70()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 6:
                """State 21"""
                assert t224006000_x71()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 7:
                """State 20"""
                assert t224006000_x80()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 8:
                """State 18"""
                assert t224006000_x76()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 9:
                """State 19"""
                assert t224006000_x77()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 10:
                """State 12"""
                assert t224006000_x61()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 11:
                """State 13"""
                assert t224006000_x63()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 12:
                """State 14"""
                assert t224006000_x64()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 13:
                """State 22"""
                assert t224006000_x72()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 14:
                """State 23"""
                assert t224006000_x73()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 15:
                """State 24"""
                assert t224006000_x83()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 16:
                """State 25"""
                assert t224006000_x84()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 20:
                """State 7,8"""
                OpenRegularShop(100225, 100249)
                assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            else:
                """State 26"""
                return 0
    """State 6,9"""
    assert t224006000_x48()
    Goto('L0')

def t224006000_x59():
    """State 0,1"""
    if GetEventFlag(1034509433) == 1:
        """State 2"""
        if not GetEventFlag(1034499233):
            """State 6"""
            # talk:22415000:"Oh, there you are. Good of you to drop by."
            assert t224006000_x30(text5=22415000, z5=1034499233, mode5=1)
        else:
            """State 4"""
            Label('L0')
            assert t224006000_x57()
    elif GetEventFlag(9130) == 1:
        """State 3"""
        if not GetEventFlag(1034499238) and GetEventFlag(1034509412) == 1:
            """State 7"""
            # talk:22404000:"Ah, you've finally come. Blaidd told me everything."
            assert t224006000_x30(text5=22404000, z5=1034499238, mode5=1)
        else:
            Goto('L0')
    else:
        Goto('L0')
    """State 5"""
    assert t224006000_x58()
    """State 8"""
    return 0

def t224006000_x60():
    """State 0,1"""
    # action:22240020:"Purchase"
    AddTalkListData(20, 22240020, -1)
    # action:22240000:"Strengthen armaments"
    AddTalkListData(1, 22240000, -1)
    """State 3"""
    assert t224006000_x65()
    """State 2"""
    # action:20000009:"Leave"
    AddTalkListData(99, 20000009, -1)
    """State 4"""
    return 0

def t224006000_x61():
    """State 0,1"""
    # talk:22403100:"Blaidd is Lady Ranni's stepbrother."
    assert t224006000_x30(text5=22403100, z5=1034499223, mode5=1)
    """State 2"""
    return 0

def t224006000_x62():
    """State 0,1"""
    # talk:22403000:"I take it you've heard of the Eternal City of Nokstella?"
    assert t224006000_x30(text5=22403000, z5=1034499222, mode5=1)
    """State 2"""
    return 0

def t224006000_x63():
    """State 0,2,3"""
    # talk:22403200:"Jerren. Now, that's a name I haven't heard for a while."
    assert t224006000_x30(text5=22403200, z5=1034499220, mode5=1)
    """State 1"""
    Label('L0')
    SetEventFlag(1034499224, 1)
    """State 5"""
    return 0
    """Unused"""
    """State 4"""
    # talk:22403250:"Jerren. Now, that's a name I haven't heard for a while."
    assert t224006000_x30(text5=22403250, z5=1034499220, mode5=1)
    Goto('L0')

def t224006000_x64():
    """State 0,1"""
    # talk:22403900:"Go with Blaidd to the festival grounds."
    assert t224006000_x31(text4=22403900, mode4=1)
    """State 2"""
    return 0

def t224006000_x65():
    """State 0,1"""
    assert t224006000_x66()
    """State 2"""
    assert t224006000_x67()
    """State 3"""
    assert t224006000_x68()
    """State 4"""
    return 0

def t224006000_x66():
    """State 0,1"""
    SetEventFlag(1034499225, 0)
    SetEventFlag(1034499226, 0)
    SetEventFlag(1034499227, 0)
    SetEventFlag(1034499228, 0)
    SetEventFlag(1034499229, 0)
    SetEventFlag(1034499244, 0)
    SetEventFlag(1034499245, 0)
    SetEventFlag(1034499246, 0)
    SetEventFlag(1034499221, 0)
    SetEventFlag(1034499249, 0)
    SetEventFlag(1034499247, 0)
    SetEventFlag(1034499248, 0)
    SetEventFlag(1034499231, 0)
    SetEventFlag(1034499234, 0)
    SetEventFlag(1034499235, 0)
    """State 3"""
    if GetEventFlag(1034509433) == 1:
        """State 7"""
        assert t224006000_x74()
        """State 6"""
        assert t224006000_x82()
    else:
        """State 5"""
        assert t224006000_x74()
        """State 2"""
        SetEventFlagIf(not GetEventFlag(1034499223) and not GetEventFlag(9130), 1034499227, 1)
        """State 4"""
        assert t224006000_x75()
    """State 8"""
    return 0

def t224006000_x67():
    """State 0,1"""
    return 0

def t224006000_x68():
    """State 0,1"""
    # action:22240003:"About Nokron"
    AddTalkListDataIf(GetEventFlag(1034499225) == 1, 2, 22240003, -1)
    # action:22240008:"Talk"
    AddTalkListDataIf(GetEventFlag(1034499244) == 1, 4, 22240008, -1)
    # action:22240015:"Talk"
    AddTalkListDataIf(GetEventFlag(1034499246) == 1, 6, 22240015, -1)
    # action:22240011:"Why is Blaidd in the Evergaol?"
    AddTalkListDataIf(GetEventFlag(1034499247) == 1, 8, 22240011, -1)
    # action:22240012:"Blaidd's death"
    AddTalkListDataIf(GetEventFlag(1034499248) == 1, 9, 22240012, -1)
    # action:22240005:"About Blaidd"
    AddTalkListDataIf(GetEventFlag(1034499227) == 1, 10, 22240005, -1)
    # action:22240006:"About Jerren"
    AddTalkListDataIf(GetEventFlag(1034499228) == 1, 11, 22240006, -1)
    # action:22240016:"About Jerren"
    AddTalkListDataIf(GetEventFlag(1034499221) == 1, 13, 22240016, -1)
    # action:22240010:"About Jerren"
    AddTalkListDataIf(GetEventFlag(1034499249) == 1, 14, 22240010, -1)
    # action:22240017:"Talk"
    AddTalkListDataIf(GetEventFlag(1034499234) == 1, 15, 22240017, -1)
    # action:22240018:"Talk"
    AddTalkListDataIf(GetEventFlag(1034499235) == 1, 16, 22240018, -1)
    # action:22240009:"About Blaidd"
    AddTalkListDataIf(GetEventFlag(1034499245) == 1, 5, 22240009, -1)
    # action:22240003:"About Nokron"
    AddTalkListDataIf(GetEventFlag(1034499226) == 1, 3, 22240003, -1)
    # action:22240015:"Talk"
    AddTalkListDataIf(GetEventFlag(1034499231) == 1, 7, 22240015, -1)
    # action:22240007:"Please go to the festival grounds"
    AddTalkListDataIf(GetEventFlag(1034499229) == 1, 12, 22240007, -1)
    """State 2"""
    return 0

def t224006000_x69():
    """State 0,1"""
    # talk:22404100:"Oh, Blaidd wanted me to tell you."
    assert t224006000_x30(text5=22404100, z5=1034499239, mode5=1)
    """State 2"""
    return 0

def t224006000_x70():
    """State 0,1"""
    # talk:22404200:"You need not await Blaidd."
    assert t224006000_x31(text4=22404200, mode4=1)
    """State 2"""
    return 0

def t224006000_x71():
    """State 0,1"""
    # talk:22410100:"Thanks to you, Lady Ranni's fate once again stirs, and the path to Nokron has opened."
    assert t224006000_x30(text5=22410100, z5=1034499240, mode5=1)
    """State 2"""
    return 0

def t224006000_x72():
    """State 0,1"""
    # talk:22405100:"Jerren. Now, that's a name I haven't heard for a while."
    assert t224006000_x30(text5=22405100, z5=1034499220, mode5=1)
    """State 2"""
    return 0

def t224006000_x73():
    """State 0,1"""
    # talk:22405000:"Now the festival is over, and General Radahn is defeated..."
    assert t224006000_x30(text5=22405000, z5=1034499243, mode5=1)
    """State 2"""
    return 0

def t224006000_x74():
    """State 0,13"""
    if GetEventFlag(9130) == 1:
        """State 9"""
        if GetEventFlag(3617) == 1 and GetEventFlag(3603) == 1:
            pass
        else:
            """State 1"""
            if GetEventFlag(1044359255) == 1:
                """State 7"""
                if GetEventFlag(1034499241) == 1:
                    pass
                else:
                    """State 8"""
                    SetEventFlag(1034499247, 1)
            else:
                """State 14"""
                if GetEventFlag(1034509433) == 1:
                    pass
                else:
                    """State 2"""
                    if GetEventFlag(1034509412) == 1:
                        """State 3"""
                        if not GetEventFlag(1034499239):
                            """State 4"""
                            SetEventFlag(1034499244, 1)
                        else:
                            """State 5"""
                            SetEventFlag(1034499245, 1)
                    else:
                        """State 10"""
                        if GetEventFlag(1034499240) == 1:
                            """State 11"""
                            SetEventFlag(1034499231, 1)
                        else:
                            """State 6"""
                            SetEventFlag(1034499246, 1)
    else:
        """State 12"""
        SetEventFlagIf(not GetEventFlag(1034499222) and not GetEventFlag(1034499220), 1034499225, 1)
        SetEventFlagIf(GetEventFlag(1034499222) == 1 and not GetEventFlag(1034499220), 1034499226, 1)
    """State 15"""
    return 0

def t224006000_x75():
    """State 0,5"""
    if GetEventFlag(9130) == 1:
        """State 1"""
        if GetEventFlag(1051369210) == 1:
            """State 10"""
            if GetEventFlag(1034499220) == 1:
                """State 3"""
                if GetEventFlag(1034499243) == 1:
                    pass
                else:
                    """State 4"""
                    SetEventFlag(1034499249, 1)
            else:
                """State 2"""
                SetEventFlag(1034499221, 1)
        else:
            pass
    else:
        """State 9"""
        if GetEventFlag(1051369210) == 1:
            """State 6"""
            if GetEventFlag(1034499220) == 1:
                """State 8"""
                SetEventFlag(1034499229, 1)
            else:
                """State 7"""
                SetEventFlag(1034499228, 1)
        else:
            pass
    """State 11"""
    return 0

def t224006000_x76():
    """State 0,1"""
    # talk:22406000:"I presume you've spoken with Blaidd?"
    assert t224006000_x30(text5=22406000, z5=1034499241, mode5=1)
    """State 2"""
    return 0

def t224006000_x77():
    """State 0,1"""
    # talk:22407000:"Unthinkable, how could Blaidd..."
    assert t224006000_x30(text5=22407000, z5=1034499242, mode5=1)
    """State 2"""
    return 0

def t224006000_x78(text2=_, text3=_):
    """State 0,1"""
    if not GetEventFlag(1034492700):
        """State 3"""
        assert t224006000_x32(text1=text2, flag1=1034492700, mode3=1)
    elif not GetEventFlag(1034492701):
        """State 4"""
        assert t224006000_x32(text1=text3, flag1=1034492701, mode3=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t224006000_x79():
    """State 0,1"""
    # talk:22403000:"I take it you've heard of the Eternal City of Nokstella?"
    assert t224006000_x31(text4=22403000, mode4=1)
    """State 2"""
    return 0

def t224006000_x80():
    """State 0,1"""
    # talk:22410100:"Thanks to you, Lady Ranni's fate once again stirs, and the path to Nokron has opened."
    assert t224006000_x31(text4=22410100, mode4=1)
    """State 2"""
    return 0

def t224006000_x81(text1=_, flag1=_):
    """State 0,1"""
    if not GetEventFlag(flag1) and not GetEventFlag(1034492704):
        """State 4"""
        SetEventFlag(1034492703, 1)
        def ExitPause():
            SetEventFlag(1034492703, 0)
        assert (t224006000_x32(text1=text1, flag1=flag1, mode3=1) and CheckSpecificPersonTalkHasEnded(0)
                == 1)
        """State 3"""
        Quit()
    else:
        """State 2"""
        Quit()
    """Unused"""
    """State 5"""
    return 0

def t224006000_x82():
    """State 0,4"""
    if GetEventFlag(3617) == 1 and GetEventFlag(3603) == 1:
        """State 1"""
        if GetEventFlag(1034499242) == 1:
            pass
        else:
            """State 2"""
            SetEventFlag(1034499248, 1)
    else:
        """State 3"""
        SetEventFlagIf(not GetEventFlag(1034499232), 1034499234, 1)
        SetEventFlagIf(GetEventFlag(1034499232) == 1, 1034499235, 1)
    """State 5"""
    return 0

def t224006000_x83():
    """State 0,1"""
    # talk:22415100:"My purpose is nearing its end."
    assert t224006000_x30(text5=22415100, z5=1034499232, mode5=1)
    """State 2"""
    return 0

def t224006000_x84():
    """State 0,1"""
    # talk:22415300:"Lady Ranni has departed on her journey."
    assert t224006000_x31(text4=22415300, mode4=1)
    """State 2"""
    return 0

