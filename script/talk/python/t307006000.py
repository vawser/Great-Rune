# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Preceptor Seluvis #1
#-----------------------------------------------------
def t307006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t307006000_x46(flag1=3563, flag2=3561, flag3=3562, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    Quit()

def t307006000_1000():
    """State 0,2,3"""
    assert t307006000_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t307006000_1101():
    """State 0,2,3"""
    assert t307006000_x1()
    """State 1"""
    c1_120(1101)
    Quit()

def t307006000_1102():
    """State 0,2,3"""
    t307006000_x2()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t307006000_2000():
    """State 0,2,3"""
    assert t307006000_x3()
    """State 1"""
    c1_120(2000)
    Quit()

def t307006000_x0():
    """State 0,1"""
    if GetEventFlag(3567) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        def ExitPause():
            SetEventFlag(1034502726, 0)
        assert t307006000_x4()
    elif GetEventFlag(3568) == 1:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        def ExitPause():
            SetEventFlag(1034502726, 0)
        assert t307006000_x5()
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t307006000_x1():
    """State 0,1"""
    assert t307006000_x35(flag9=1034502720, flag10=1034502721)
    """State 2"""
    return 0

def t307006000_x2():
    """State 0,1"""
    if not GetEventFlag(1034509302) and not GetEventFlag(1034502723):
        """State 4"""
        SetEventFlag(1034502722, 1)
        # talk:30780200:"You incorrigible lout."
        def WhilePaused():
            RequestAnimation(90300, -1)
        def ExitPause():
            SetEventFlag(1034502722, 0)
        assert (t307006000_x73(text2=30780200, flag9=1034509302, mode3=1) and CheckSpecificPersonTalkHasEnded(0)
                == 1)
        """State 3"""
        def WhilePaused():
            RequestAnimation(90300, -1)
        Quit()
    else:
        """State 2"""
        Quit()
    """Unused"""
    """State 5"""
    return 0

def t307006000_x3():
    """State 0,1,2"""
    # actionbutton:6000:"Talk"
    assert (t307006000_x40(actionbutton1=6000, flag5=6001, flag11=6000, flag12=6000, flag13=6000, flag14=6000,
            flag4=6000))
    """State 3"""
    return 0

def t307006000_x4():
    """State 0,1"""
    if GetEventFlag(1034509312) == 1:
        """State 2"""
        # goods:8164:Seluvis's Potion
        if ComparePlayerInventoryNumber(3, 8164, 0, 0, 0) == 1 or GetEventFlag(1034509313) == 1:
            """State 3"""
            if GetEventFlag(1034509313) == 1:
                """State 4"""
                if GetEventFlag(1034509335) == 1:
                    """State 7"""
                    assert t307006000_x13()
                else:
                    """State 8"""
                    assert t307006000_x12()
            else:
                """State 6"""
                # talk:30703000:"Ahh, so you made Nepheli drink the potion?"
                assert t307006000_x71(text3=30703000, z8=1034509313, mode5=1)
        else:
            """State 9"""
            assert t307006000_x36()
    else:
        """State 5"""
        assert t307006000_x6()
    """State 10"""
    return 0

def t307006000_x5():
    """State 0,1"""
    if not GetEventFlag(1034509316):
        """State 7"""
        assert t307006000_x39()
        """State 2"""
        # talk:30709200:"Good, I've been waiting for you."
        assert t307006000_x71(text3=30709200, z8=1034509316, mode5=1)
        """State 3"""
        # lot:101450:Amber Draught
        assert t307006000_x43(lot1=101450)
        """State 4"""
        # talk:30709210:"The dead-eyed doll lets down her guard in your presence, rather remarkably."
        def WhilePaused():
            RequestAnimationIf(GetWorkValue(1) == 1, 90305, -1)
        assert t307006000_x72(text1=30709210, mode4=1)
    else:
        """State 5"""
        # talk:30709210:"The dead-eyed doll lets down her guard in your presence, rather remarkably."
        assert t307006000_x72(text1=30709210, mode4=1)
    """State 6"""
    assert t307006000_x15()
    """State 8"""
    return 0

def t307006000_x6():
    """State 0,1"""
    if GetEventFlag(1034509310) == 1:
        """State 2"""
        if GetEventFlag(1034509311) == 1:
            """State 5"""
            # talk:30701500:"I could have sworn I told you to trouble me no more..."
            assert t307006000_x72(text1=30701500, mode4=1)
            """State 8"""
            call = t307006000_x7()
            if call.Get() == 0:
                """State 12"""
                assert t307006000_x11()
                Goto('L1')
            elif call.Get() == 1:
                pass
            elif call.Done():
                Goto('L1')
        else:
            """State 4"""
            # talk:30701300:"Have you fumbled out the correct answer now?"
            assert t307006000_x72(text1=30701300, mode4=1)
            """State 7"""
            call = t307006000_x7()
            if call.Get() == 0:
                """State 9"""
                Label('L0')
                assert t307006000_x8()
                Goto('L1')
            elif call.Get() == 1:
                pass
            elif call.Done():
                Goto('L1')
        """State 11"""
        assert t307006000_x10()
    else:
        """State 3"""
        # talk:30701000:"Well, well. You took me at my word."
        assert t307006000_x72(text1=30701000, mode4=1)
        """State 6"""
        call = t307006000_x7()
        if call.Get() == 0:
            Goto('L0')
        elif call.Get() == 1:
            """State 10"""
            assert t307006000_x9()
        elif call.Done():
            pass
    """State 13"""
    Label('L1')
    return 0

def t307006000_x7():
    """State 0,1"""
    c1_110()
    """State 2"""
    ClearTalkListData()
    """State 3"""
    # action:23071001:"Accept the task"
    AddTalkListData(1, 23071001, -1)
    # action:23071002:"Don't accept"
    AddTalkListData(2, 23071002, -1)
    """State 4"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 5"""
    if GetTalkListEntryResult() == 1:
        """State 6"""
        return 0
    elif GetTalkListEntryResult() == 2:
        """State 7"""
        return 1
    else:
        """State 8"""
        return 2

def t307006000_x8():
    """State 0,1"""
    # talk:30701100:"Good, good."
    assert t307006000_x71(text3=30701100, z8=1034509312, mode5=1)
    """State 2"""
    # lot:101400:Seluvis's Potion
    assert t307006000_x43(lot1=101400)
    """State 3"""
    # talk:30701110:"Find Nepheli, and ensure she drinks it."
    assert t307006000_x72(text1=30701110, mode4=1)
    """State 4"""
    return 0

def t307006000_x9():
    """State 0,1"""
    # talk:30701200:"I see..."
    assert t307006000_x71(text3=30701200, z8=1034509310, mode5=1)
    """State 2"""
    return 0

def t307006000_x10():
    """State 0,1"""
    # talk:30701400:"..."
    assert t307006000_x71(text3=30701400, z8=1034509311, mode5=1)
    """State 2"""
    return 0

def t307006000_x11():
    """State 0,1"""
    # talk:30701600:"Good, good."
    assert t307006000_x71(text3=30701600, z8=1034509312, mode5=1)
    """State 2"""
    # lot:101400:Seluvis's Potion
    assert t307006000_x43(lot1=101400)
    """State 3"""
    # talk:30701610:"Find Nepheli, and ensure she drinks it."
    assert t307006000_x72(text1=30701610, mode4=1)
    """State 4"""
    return 0

def t307006000_x12():
    """State 0,1"""
    if not GetEventFlag(1034509314):
        """State 4"""
        # talk:30703100:"You wish to begin right this moment?"
        assert t307006000_x71(text3=30703100, z8=1034509314, mode5=1)
    else:
        """State 3"""
        if GetEventFlag(1034509328) == 1:
            """State 2"""
            SetRNGSeedIf(CompareRNGValue(0, 0) != -1)
            ShuffleRNGSeedIf(not CompareRNGValue(0, 0) != -1, 10)
            if CompareRNGValue(4, 9) == 1:
                """State 7"""
                # talk:30706000:"How's the puppet I gave you?"
                assert t307006000_x72(text1=30706000, mode4=1)
                Goto('L0')
            else:
                pass
        else:
            pass
        """State 6"""
        # talk:30703200:"Begging for another lesson so soon?"
        assert t307006000_x72(text1=30703200, mode4=1)
    """State 5"""
    Label('L0')
    assert t307006000_x15()
    """State 8"""
    return 0

def t307006000_x13():
    """State 0,1"""
    if not GetEventFlag(1034509315):
        """State 7"""
        assert t307006000_x39()
        """State 2"""
        # talk:30709100:"Ah, are you still here?"
        assert t307006000_x71(text3=30709100, z8=1034509315, mode5=1)
        """State 4"""
        # lot:101410:Magic Scorpion Charm
        assert t307006000_x43(lot1=101410)
        """State 5"""
        # talk:30709110:"Now, just you wait. The merriment is soon to begin."
        def WhilePaused():
            RequestAnimationIf(GetWorkValue(1) == 1, 90305, -1)
        assert t307006000_x72(text1=30709110, mode4=1)
    else:
        """State 3"""
        # talk:30709500:"You'll be flabbergasted, I can assure you."
        assert t307006000_x72(text1=30709500, mode4=1)
    """State 6"""
    assert t307006000_x15()
    """State 8"""
    return 0

def t307006000_x14():
    """State 0,2"""
    if GetEventFlagValue(1034509345, 3) > 3:
        """State 3"""
        if not GetEventFlag(1034509338):
            """State 4"""
            # talk:30708000:"You're proving to be quite the puppeteer."
            assert t307006000_x71(text3=30708000, z8=1034509338, mode5=1)
        else:
            pass
    else:
        """State 1"""
        if GetEventFlag(1034502726) == 1:
            """State 5"""
            # talk:30703300:"Come now, the pretence of comprehension becomes you not."
            assert t307006000_x72(text1=30703300, mode4=1)
        else:
            pass
    """State 6"""
    return 0

def t307006000_x15():
    """State 0,6"""
    SetEventFlag(1034509346, 1)
    while Loop('mainloop'):
        """State 1"""
        Label('L0')
        c1_110()
        while True:
            """State 2"""
            ClearTalkListData()
            """State 8"""
            assert t307006000_x16(val12=8850, val13=8854, val14=1034509450, z7=0)
            """State 3"""
            ShowShopMessage(1)
            assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 4"""
            if GetTalkListEntryResult() == 1:
                """State 5"""
                OpenRegularShop(100275, 100299)
                assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                continue
            elif GetTalkListEntryResult() == 2:
                """State 7"""
                OpenRegularShop(100300, 100324)
                assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
                continue
            elif GetTalkListEntryResult() == 3:
                """State 11"""
                assert t307006000_x18()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 4:
                """State 12"""
                assert t307006000_x19()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 5:
                Break('mainloop')
            elif GetTalkListEntryResult() == 6:
                """State 10"""
                assert t307006000_x17()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 7:
                """State 14"""
                assert t307006000_x27()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 8:
                """State 15"""
                assert t307006000_x28()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 9:
                """State 16"""
                assert t307006000_x29()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 10:
                """State 17"""
                assert t307006000_x30()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 11:
                """State 18"""
                assert t307006000_x31()
            elif GetTalkListEntryResult() == 12:
                """State 19"""
                assert t307006000_x32()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 13:
                """State 20"""
                assert t307006000_x33()
                Continue('mainloop')
            elif GetTalkListEntryResult() == 50:
                """State 21"""
                # action:23160026:"Don't give a scroll"
                assert t307006000_x38(z5=0, val6=8850, val7=8854, val8=1034509450, val9=23160021, action1=23160026)
                continue
            else:
                """State 9"""
                assert t307006000_x14()
            """State 22"""
            return 0
    """State 13"""
    assert t307006000_x20()
    Goto('L0')

def t307006000_x16(val12=8850, val13=8854, val14=1034509450, z7=0):
    """State 0,1"""
    # action:23070006:"Study sorcery"
    AddTalkListData(1, 23070006, -1)
    # action:23070007:"Obtain a puppet"
    AddTalkListDataIf(GetEventFlag(1034509329) == 1, 2, 23070007, -1)
    """State 4"""
    assert t307006000_x37(val12=val12, val13=val13, val14=val14, z7=z7)
    """State 3"""
    assert t307006000_x21()
    """State 2"""
    # action:20000009:"Leave"
    AddTalkListData(99, 20000009, -1)
    """State 5"""
    return 0

def t307006000_x17():
    """State 0,5"""
    # talk:30705000:"You break into a man's private chambers, rooting about as you please?"
    assert t307006000_x72(text1=30705000, mode4=1)
    """State 3"""
    ClearTalkActionState()
    """State 1"""
    OpenDupeShop(0, 100300, 100309)
    assert not (CheckSpecificPersonMenuIsOpen(31, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    if DidYouDoSomethingInTheMenu(3) == 1:
        """State 4"""
        SetEventFlag(1034509328, 1)
        SetEventFlag(1034509347, 1)
    else:
        pass
    """State 6"""
    return 0

def t307006000_x18():
    """State 0,1"""
    # talk:30704100:"So, you had Nepheli drink the potion? Truly?"
    assert t307006000_x71(text3=30704100, z8=1034509332, mode5=1)
    """State 2"""
    return 0

def t307006000_x19():
    """State 0,1"""
    # talk:30704000:"Well, well. You're asking me about that, are you?"
    assert t307006000_x71(text3=30704000, z8=1034509330, mode5=1)
    """State 2"""
    # lot:101430:Seluvis's Introduction
    assert t307006000_x43(lot1=101430)
    """State 3"""
    return 0

def t307006000_x20():
    """State 0,1"""
    # talk:30711000:"Oh, perhaps you've already noticed."
    assert t307006000_x71(text3=30711000, z8=1034509331, mode5=1)
    """State 2"""
    return 0

def t307006000_x21():
    """State 0,1"""
    assert t307006000_x22()
    """State 2"""
    assert t307006000_x23()
    """State 3"""
    assert t307006000_x24()
    """State 4"""
    return 0

def t307006000_x22():
    """State 0,1"""
    SetEventFlag(1034509317, 0)
    SetEventFlag(1034509318, 0)
    SetEventFlag(1034509319, 0)
    SetEventFlag(1034509320, 0)
    SetEventFlag(1034509321, 0)
    SetEventFlag(1034509322, 0)
    SetEventFlag(1034509323, 0)
    SetEventFlag(1034509324, 0)
    SetEventFlag(1034509325, 0)
    SetEventFlag(1034509326, 0)
    SetEventFlag(1034509327, 0)
    """State 3"""
    assert t307006000_x25()
    """State 4"""
    assert t307006000_x26()
    """State 2"""
    SetEventFlagIf(not GetEventFlag(1034509332) and not GetEventFlag(11109919), 1034509321, 1)
    """State 5"""
    return 0

def t307006000_x23():
    """State 0,1"""
    return 0

def t307006000_x24():
    """State 0,1"""
    # action:23070016:"About Nepheli"
    AddTalkListDataIf(GetEventFlag(1034509321) == 1, 3, 23070016, -1)
    # action:23070009:"About Nokron"
    AddTalkListDataIf(GetEventFlag(1034509319) == 1, 4, 23070009, -1)
    # action:23070017:"Talk"
    AddTalkListDataIf(GetEventFlag(1034509320) == 1, 5, 23070017, -1)
    # action:23070008:"About your chambers"
    AddTalkListDataIf(GetEventFlag(1034509317) == 1, 6, 23070008, -1)
    # action:23070010:"I want a new puppet"
    AddTalkListDataIf(GetEventFlag(1034509318) == 1, 7, 23070010, -1)
    # action:23070011:"About the scheme"
    AddTalkListDataIf(GetEventFlag(1034509322) == 1, 8, 23070011, -1)
    # action:23070015:"About your scheme"
    AddTalkListDataIf(GetEventFlag(1034509323) == 1, 9, 23070015, -1)
    # action:23070018:"About Amber Starlight"
    AddTalkListDataIf(GetEventFlag(1034509324) == 1, 10, 23070018, -1)
    # action:23070012:"Give Amber Starlight"
    AddTalkListDataIf(GetEventFlag(1034509325) == 1, 11, 23070012, -1)
    # action:23070013:"About the draught"
    AddTalkListDataIf(GetEventFlag(1034509326) == 1, 12, 23070013, -1)
    # action:23070014:"About the draught"
    AddTalkListDataIf(GetEventFlag(1034509327) == 1, 13, 23070014, -1)
    """State 2"""
    return 0

def t307006000_x25():
    """State 0,2,1"""
    if GetEventFlag(12029155) == 1:
        """State 5"""
        if GetEventFlag(1034509330) == 1:
            pass
        else:
            """State 6"""
            SetEventFlag(1034509319, 1)
    else:
        pass
    """State 7"""
    Label('L0')
    return 0
    """Unused"""
    """State 3"""
    if GetEventFlag(1034509331) == 1:
        Goto('L0')
    else:
        pass
    """State 4"""
    SetEventFlag(1034509320, 1)
    Goto('L0')

def t307006000_x26():
    """State 0,1"""
    if GetEventFlag(400146) == 1:
        """State 2"""
        if GetEventFlag(1034509328) == 1:
            """State 4"""
            if GetEventFlagValue(1034509339, 3) > 2:
                """State 5"""
                if GetEventFlag(1034509329) == 1:
                    """State 7"""
                    if GetEventFlag(1034509338) == 1:
                        """State 8"""
                        if GetEventFlag(1034509333) == 1:
                            """State 9"""
                            # goods:8142:Amber Starlight
                            if (ComparePlayerInventoryNumber(3, 8142, 4, 1, 0) == 1 or GetEventFlag(1034509335)
                                == 1):
                                """State 10"""
                                if GetEventFlag(1034509335) == 1:
                                    """State 11"""
                                    if GetEventFlag(1034509316) == 1:
                                        """State 12"""
                                        if GetEventFlag(1034509336) == 1:
                                            """State 13"""
                                            if GetEventFlagValue(1034509342, 3) > 3:
                                                """State 14"""
                                                if GetEventFlag(1034509337) == 1:
                                                    pass
                                                else:
                                                    """State 21"""
                                                    SetEventFlag(1034509327, 1)
                                            else:
                                                pass
                                        else:
                                            """State 20"""
                                            SetEventFlag(1034509326, 1)
                                    else:
                                        pass
                                else:
                                    """State 19"""
                                    SetEventFlag(1034509325, 1)
                            else:
                                """State 18"""
                                SetEventFlag(1034509324, 1)
                        else:
                            """State 16"""
                            if GetEventFlag(1034509334) == 1:
                                """State 15"""
                                SetEventFlag(1034509323, 1)
                            else:
                                """State 17"""
                                SetEventFlag(1034509322, 1)
                    else:
                        pass
                else:
                    """State 6"""
                    SetEventFlag(1034509318, 1)
            else:
                pass
        else:
            """State 3"""
            SetEventFlag(1034509317, 1)
    else:
        pass
    """State 22"""
    return 0

def t307006000_x27():
    """State 0,1"""
    # talk:30707000:"What's that? You want another puppet?"
    assert t307006000_x71(text3=30707000, z8=1034509329, mode5=1)
    """State 2"""
    return 0

def t307006000_x28():
    """State 0,5"""
    assert t307006000_x39()
    """State 1"""
    # talk:30708100:"Perhaps, you'd be interested in a little scheme of mine?"
    def WhilePaused():
        RequestAnimationIf(GetWorkValue(1) == 1, 90305, -1)
    assert t307006000_x72(text1=30708100, mode4=1)
    """State 2"""
    call = t307006000_x34()
    def WhilePaused():
        RequestAnimationIf(GetWorkValue(1) == 1, 90305, -1)
    if call.Get() == 0:
        """State 3"""
        # talk:30708200:"Ahh, I knew I had you pegged."
        def WhilePaused():
            RequestAnimationIf(GetWorkValue(1) == 1, 90305, -1)
        assert t307006000_x71(text3=30708200, z8=1034509333, mode5=1)
    elif call.Get() == 1:
        """State 4"""
        # talk:30708300:"Very good."
        assert t307006000_x71(text3=30708300, z8=1034509334, mode5=1)
    elif call.Done():
        pass
    """State 6"""
    return 0

def t307006000_x29():
    """State 0,5"""
    assert t307006000_x39()
    """State 1"""
    # talk:30708400:"Ah ha. Might you be interested after all?"
    def WhilePaused():
        RequestAnimationIf(GetWorkValue(1) == 1, 90305, -1)
    assert t307006000_x72(text1=30708400, mode4=1)
    """State 2"""
    call = t307006000_x34()
    def WhilePaused():
        RequestAnimationIf(GetWorkValue(1) == 1, 90305, -1)
    if call.Get() == 0:
        """State 3"""
        # talk:30708200:"Ahh, I knew I had you pegged."
        def WhilePaused():
            RequestAnimationIf(GetWorkValue(1) == 1, 90305, -1)
        assert t307006000_x71(text3=30708200, z8=1034509333, mode5=1)
    elif call.Get() == 1:
        """State 4"""
        # talk:30708500:"Alright, enough of these games."
        assert t307006000_x72(text1=30708500, mode4=1)
    elif call.Done():
        pass
    """State 6"""
    return 0

def t307006000_x30():
    """State 0,2"""
    assert t307006000_x39()
    """State 1"""
    # talk:30708250:"Procure it for me."
    def WhilePaused():
        RequestAnimationIf(GetWorkValue(1) == 1, 90305, -1)
    assert t307006000_x72(text1=30708250, mode4=1)
    """State 3"""
    return 0

def t307006000_x31():
    """State 0,1"""
    # goods:8142:Amber Starlight
    PlayerEquipmentQuantityChange(3, 8142, -1)
    """State 2"""
    # talk:30709000:"Well, well, you managed to lay your hands on it!"
    assert t307006000_x70(text4=30709000, z9=1034509335, mode6=1)
    """State 3"""
    return 0

def t307006000_x32():
    """State 0,2"""
    assert t307006000_x39()
    """State 1"""
    # talk:30709300:"You...understand, don't you?"
    def WhilePaused():
        RequestAnimationIf(GetWorkValue(1) == 1, 90305, -1)
    assert t307006000_x71(text3=30709300, z8=1034509336, mode5=1)
    """State 3"""
    return 0

def t307006000_x33():
    """State 0,2"""
    assert t307006000_x39()
    """State 1"""
    # talk:30709400:"Come now, don't make me wait."
    def WhilePaused():
        RequestAnimationIf(GetWorkValue(1) == 1, 90305, -1)
    assert t307006000_x71(text3=30709400, z8=1034509337, mode5=1)
    """State 3"""
    return 0

def t307006000_x34():
    """State 0,1"""
    c1_110()
    """State 2"""
    ClearTalkListData()
    """State 3"""
    # action:23071009:"I'm interested"
    AddTalkListData(1, 23071009, -1)
    # action:23071010:"I'm not interested"
    AddTalkListData(2, 23071010, -1)
    """State 4"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 5"""
    if GetTalkListEntryResult() == 1:
        """State 6"""
        return 0
    elif GetTalkListEntryResult() == 2:
        """State 7"""
        return 1
    else:
        """State 8"""
        return 2

def t307006000_x35(flag9=1034502720, flag10=1034502721):
    """State 0,1"""
    if not GetEventFlag(flag9):
        """State 3"""
        # talk:30780000:"Agh!"
        assert t307006000_x73(text2=30780000, flag9=flag9, mode3=1)
    elif not GetEventFlag(flag10):
        """State 4"""
        # talk:30780100:"Enough of that, now."
        assert t307006000_x73(text2=30780100, flag9=flag10, mode3=1)
    else:
        """State 2"""
        pass
    """State 5"""
    return 0

def t307006000_x36():
    """State 0,7"""
    # talk:30701700:"I've no time for idle chit chat."
    assert t307006000_x72(text1=30701700, mode4=1)
    """State 8"""
    assert t307006000_x22()
    """State 1"""
    if not GetEventFlag(1034509319):
        pass
    else:
        """State 2"""
        c1_110()
        """State 3"""
        ClearTalkListData()
        """State 4"""
        # action:23071014:"Ask about Nokron"
        AddTalkListData(1, 23071014, -1)
        # action:23071015:"Leave"
        AddTalkListData(2, 23071015, -1)
        """State 5"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 6"""
        if GetTalkListEntryResult() == 1:
            """State 9"""
            assert t307006000_x19()
        else:
            pass
    """State 10"""
    return 0

def t307006000_x37(val12=8850, val13=8854, val14=1034509450, z7=0):
    """State 0,2"""
    call = t307006000_x76(val6=val12, val7=val13, val8=val14, z5=z7)
    if call.Get() == 1:
        """State 1"""
        Label('L0')
        # action:23070019:"Hand over the scroll"
        AddTalkListData(50, 23070019, -1)
    elif call.Done():
        """State 3"""
        call = t307006000_x76(val6=8866, val7=8866, val8=1034509455, z5=z7)
        if call.Get() == 1:
            Goto('L0')
        elif call.Done():
            pass
    """State 4"""
    return 0

def t307006000_x38(z5=0, val6=8850, val7=8854, val8=1034509450, val9=23160021, action1=23160026):
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        """State 5"""
        assert t307006000_x77(val11=1, val9=val9, val6=val6, val7=val7, val8=val8, z6=0)
        """State 8"""
        assert t307006000_x77(val11=50, val9=23160028, val6=8866, val7=8866, val8=1034509455, z6=0)
        """State 4"""
        # action:23160026:"Don't give a scroll"
        AddTalkListData(99, action1, -1)
        """State 2"""
        ShowShopMessage(0)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 3"""
        if not GetTalkListEntryResult() or GetTalkListEntryResult() == 99:
            break
        elif GetTalkListEntryResult() == 50:
            """State 9"""
            # talk:30710000:"Hmm. Is that a scroll?"
            assert t307006000_x78(val10=50, val6=8866, val8=1034509455, text1=30710000)
            """State 7"""
            Label('L0')
            call = t307006000_x76(val6=val6, val7=val7, val8=val8, z5=z5)
            if call.Get() == 1:
                pass
            elif call.Done():
                """State 10"""
                call = t307006000_x76(val6=8866, val7=8866, val8=1034509455, z5=z5)
                if call.Get() == 1:
                    pass
                elif call.Done():
                    break
        else:
            """State 6"""
            # talk:30710000:"Hmm. Is that a scroll?"
            assert t307006000_x78(val10=1, val6=val6, val8=val8, text1=30710000)
            Goto('L0')
    """State 11"""
    return 0

def t307006000_x39():
    """State 0,1"""
    if RelativeAngleBetweenTwoPlayers_SpecifyAxis(15) < 15 and GetDistanceToPlayer() > 1:
        """State 2"""
        Label('L0')
        SetWorkValue(1, 1)
    elif RelativeAngleBetweenTwoPlayers_SpecifyAxis(-15) < 15:
        Goto('L0')
    else:
        """State 3"""
        SetWorkValue(1, 0)
    """State 4"""
    return 0

def t307006000_x40(actionbutton1=6000, flag5=6001, flag11=6000, flag12=6000, flag13=6000, flag14=6000,
                   flag4=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag5) == 1 or GetEventFlag(flag11) == 1 or GetEventFlag(flag12) == 1 or
                GetEventFlag(flag13) == 1 or GetEventFlag(flag14) == 1)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 2"""
        if GetEventFlag(flag4) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag5) and not GetEventFlag(flag11) and not GetEventFlag(flag12) and not
              GetEventFlag(flag13) and not GetEventFlag(flag14)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t307006000_x41():
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

def t307006000_x42():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t307006000_x43(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t307006000_x44(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t307006000_x60()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t307006000_x41()
    else:
        """State 4,7"""
        call = t307006000_x75()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t307006000_x41()
    """State 9"""
    return 0

def t307006000_x45():
    """State 0,1"""
    assert t307006000_x41()
    """State 2"""
    return 0

def t307006000_x46(flag1=3563, flag2=3561, flag3=3562, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t307006000_x63(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t307006000_x62()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t307006000_x47(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t307006000_x50(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t307006000_x54(val1=val1, z1=z1)
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
            call = t307006000_x56(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t307006000_x67() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t307006000_x52(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t307006000_x48(val2=10, val3=12):
    """State 0,1"""
    call = t307006000_x58(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t307006000_x44(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t307006000_x49(flag1=3563, val2=10, val3=12):
    """State 0,8"""
    assert t307006000_x80()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t307006000_x61()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t307006000_x41()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t307006000_x50(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t307006000_x51(z10=2000, val15=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t307006000_x40(actionbutton1=actionbutton1, flag5=flag5, flag11=6000, flag12=6000, flag13=6000,
                flag14=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t307006000_x51(z10=_, val15=_):
    """State 0,1"""
    if f203(z10) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z10)
        assert f202() == val15
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t307006000_x52(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t307006000_x41()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t307006000_x53()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t307006000_x68()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t307006000_x53():
    """State 0,1"""
    assert t307006000_x51(z10=1101, val15=1101)
    """State 2"""
    return 0

def t307006000_x54(val1=5, z1=1):
    """State 0,2"""
    assert t307006000_x64()
    """State 1"""
    call = t307006000_x55()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t307006000_x66()
    """State 4"""
    return 0

def t307006000_x55():
    """State 0,1"""
    assert t307006000_x51(z10=1000, val15=1000)
    """State 2"""
    return 0

def t307006000_x56(val5=12):
    """State 0,1"""
    call = t307006000_x57()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t307006000_x67()
    """State 3"""
    return 0

def t307006000_x57():
    """State 0,1"""
    assert t307006000_x51(z10=1100, val15=1100)
    """State 2"""
    return 0

def t307006000_x58(val2=10, val3=12):
    """State 0,5"""
    assert t307006000_x80()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t307006000_x59()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t307006000_x69()
    """Unused"""
    """State 6"""
    return 0

def t307006000_x59():
    """State 0,2"""
    call = t307006000_x51(z10=1102, val15=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t307006000_x60():
    """State 0,1"""
    assert t307006000_x51(z10=1001, val15=1001)
    """State 2"""
    return 0

def t307006000_x61():
    """State 0,1"""
    assert t307006000_x51(z10=1103, val15=1103)
    """State 2"""
    return 0

def t307006000_x62():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t307006000_x63(flag1=3563, flag2=3561, flag3=3562, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t307006000_x47(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t307006000_x49(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t307006000_x48(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t307006000_x79() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t307006000_x64():
    """State 0,1"""
    assert t307006000_x65()
    """State 2"""
    return 0

def t307006000_x65():
    """State 0,1"""
    assert t307006000_x51(z10=1104, val15=1104)
    """State 2"""
    return 0

def t307006000_x66():
    """State 0,1"""
    call = t307006000_x51(z10=1201, val15=1201)
    if call.Get() == 1:
        """State 2"""
        assert t307006000_x45()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t307006000_x67():
    """State 0,1"""
    call = t307006000_x51(z10=1300, val15=1300)
    if call.Get() == 1:
        """State 2"""
        assert t307006000_x45()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t307006000_x68():
    """State 0,1"""
    call = t307006000_x51(z10=1301, val15=1301)
    if call.Get() == 1:
        """State 2"""
        assert t307006000_x45()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t307006000_x69():
    """State 0,1"""
    call = t307006000_x51(z10=1302, val15=1302)
    if call.Get() == 1:
        """State 2"""
        assert t307006000_x45()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t307006000_x70(text4=30709000, z9=1034509335, mode6=1):
    """State 0,5"""
    assert t307006000_x42() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z9, 1)
    """State 1"""
    # talk:30709000:"Well, well, you managed to lay your hands on it!"
    TalkToPlayer(text4, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode6:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t307006000_x71(text3=_, z8=_, mode5=1):
    """State 0,5"""
    assert t307006000_x42() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text3, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 4"""
    if not mode5:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 2"""
    SetEventFlag(z8, 1)
    """State 6"""
    return 0

def t307006000_x72(text1=_, mode4=1):
    """State 0,4"""
    assert t307006000_x42() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode4:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t307006000_x73(text2=_, flag9=_, mode3=1):
    """State 0,5"""
    assert t307006000_x74() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(flag9, 1)
    """State 1"""
    TalkToPlayer(text2, -1, -1, 1)
    """State 4"""
    if not mode3:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t307006000_x74():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t307006000_x75():
    """State 0,1"""
    assert t307006000_x51(z10=1002, val15=1002)
    """State 2"""
    return 0

def t307006000_x76(val6=_, val7=_, val8=_, z5=0):
    """State 0,1"""
    SetWorkValue(z5, 0)
    while True:
        """State 2"""
        if (ComparePlayerInventoryNumber(3, val6 + GetWorkValue(z5), 4, 1, 0) == 1 and not GetEventFlag(val8
            + GetWorkValue(z5))):
            """State 4"""
            return 1
        elif GetWorkValue(z5) > val7 - val6:
            break
        else:
            """Pass"""
            SetWorkValue(z5, GetWorkValue(z5) + 1)
    """State 3"""
    return 0

def t307006000_x77(val11=_, val9=_, val6=_, val7=_, val8=_, z6=0):
    """State 0,1"""
    SetWorkValue(z6, 0)
    while True:
        """State 2"""
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, val6 + GetWorkValue(z6), 4, 1, 0) == 1 and not GetEventFlag(val8 + GetWorkValue(z6)),
                          val11 + GetWorkValue(z6), val9 + GetWorkValue(z6), -1)
        if GetWorkValue(z6) > val7 - val6:
            break
        else:
            """Pass"""
            SetWorkValue(z6, GetWorkValue(z6) + 1)
    """State 3,4"""
    return 0

def t307006000_x78(val10=_, val6=_, val8=_, text1=30710000):
    """State 0,1"""
    PlayerEquipmentQuantityChange(3, val6 + GetTalkListEntryResult() - val10, -1)
    """State 2"""
    SetEventFlag(val8 + GetTalkListEntryResult() - val10, 1)
    """State 3"""
    assert t307006000_x72(text1=text1, mode4=1)
    """State 4"""
    return 0

def t307006000_x79():
    """State 0,1"""
    assert t307006000_x41()
    """State 2"""
    return 0

def t307006000_x80():
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

