# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Roderika #2
#-----------------------------------------------------
def t320006000_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t320006000_x28(flag1=3703, flag2=3701, flag3=3702, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    def WhilePaused():
        c1_121(9620)
    Quit()

def t320006000_1000():
    """State 0,2,3"""
    assert t320006000_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t320006000_1101():
    """State 0,2,3"""
    assert t320006000_x1()
    """State 1"""
    c1_120(1101)
    Quit()

def t320006000_2000():
    """State 0,2,3"""
    assert t320006000_x2(z5=10, z6=12)
    """State 1"""
    c1_120(2000)
    Quit()

def t320006000_x0():
    """State 0,1"""
    if GetEventFlag(3705) == 1:
        """State 3"""
        def WhilePaused():
            RequestAnimationIf(not GetEventFlag(1041389412) or GetEventFlag(1041389409) == 1, 90300,
                               -1)
        assert t320006000_x3()
    elif GetEventFlag(3707) == 1:
        """State 4"""
        def WhilePaused():
            RequestAnimation(90310, -1)
        assert t320006000_x4()
    elif GetEventFlag(3708) == 1:
        """State 5"""
        def WhilePaused():
            RequestAnimation(90315, -1)
        assert t320006000_x5()
    elif GetEventFlag(3709) == 1:
        """State 6"""
        def WhilePaused():
            RequestAnimationIf(GetEventFlag(11109279) == 1, 90315, -1)
            RequestAnimationIf(not GetEventFlag(11109279) or GetEventFlag(1041382735) == 1, 90315, -1)
        assert t320006000_x16()
    else:
        """State 2"""
        pass
    """State 7"""
    return 0

def t320006000_x1():
    """State 0,4"""
    if not GetEventFlag(1041382731):
        """State 2,9"""
        # talk:32080000:"You're willing to make me a chrysalid?"
        assert t320006000_x54(text1=32080000, mode3=1)
        """State 1"""
        SetEventFlag(1041382731, 1)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    elif not GetEventFlag(1041382732):
        """State 5,10"""
        # talk:32080300:"I know how you must feel."
        assert t320006000_x54(text1=32080300, mode3=1)
        """State 6"""
        SetEventFlag(1041382732, 1)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    elif not GetEventFlag(1041382733):
        """State 7,11"""
        # talk:32080500:"Please, stop."
        assert t320006000_x54(text1=32080500, mode3=1)
        """State 8"""
        SetEventFlag(1041382733, 1)
        assert CheckSpecificPersonTalkHasEnded(0) == 1
    else:
        """State 3"""
        pass
    """State 12"""
    return 0

def t320006000_x2(z5=10, z6=12):
    """State 0,1"""
    if GetEventFlag(3705) == 1 or GetEventFlag(3707) == 1:
        """State 8"""
        if not GetEventFlag(1041389412):
            while True:
                """State 9"""
                # actionbutton:6000:"Talk"
                call = t320006000_x22(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                      flag12=6000, flag4=6000)
                if call.Done():
                    break
                elif GetEventFlag(1041382736) == 1 and not GetEventFlag(1041382731):
                    """State 11"""
                    # talk:32080000:"You're willing to make me a chrysalid?"
                    assert t320006000_x53(text2=32080000, z7=1041382731, mode4=1)
                    """State 2"""
                    assert GetEventFlag(1041382731) == 1
                    """State 5"""
                    Label('L0')
                    """State 6"""
                    if not GetEventFlag(1041389412):
                        pass
                    else:
                        """State 7"""
                        SetEventFlag(1041389409, 1)
                elif GetEventFlag(1041382737) == 1 and not GetEventFlag(1041382732):
                    """State 12"""
                    # talk:32080300:"I know how you must feel."
                    assert t320006000_x53(text2=32080300, z7=1041382732, mode4=1)
                    """State 3"""
                    assert GetEventFlag(1041382732) == 1
                    Goto('L0')
                elif GetEventFlag(1041382738) == 1 and not GetEventFlag(1041382733):
                    """State 13"""
                    # talk:32080500:"Please, stop."
                    assert t320006000_x53(text2=32080500, z7=1041382733, mode4=1)
                    """State 4"""
                    assert GetEventFlag(1041382733) == 1
                    Goto('L0')
        else:
            """State 10"""
            Label('L1')
            # actionbutton:6500:"Talk"
            assert (t320006000_x22(actionbutton1=6500, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                    flag12=6000, flag4=6000))
    else:
        Goto('L1')
    """State 14"""
    return 0

def t320006000_x3():
    """State 0,1"""
    if not GetEventFlag(1041389411):
        """State 3"""
        SetEventFlag(1041382735, 1)
        """State 4"""
        assert t320006000_x7()
    elif not GetEventFlag(1041389412):
        """State 5"""
        assert t320006000_x17()
        """State 2"""
        # goods:8171:Chrysalids' Memento
        if ComparePlayerInventoryNumber(3, 8171, 4, 1, 0) == 1 and not GetEventFlag(1041389412):
            """State 6"""
            assert t320006000_x12()
        else:
            pass
    else:
        """State 7"""
        SetEventFlag(1041389409, 1)
        assert t320006000_x11()
    """State 8"""
    return 0

def t320006000_x4():
    """State 0,3"""
    if GetEventFlag(11109255) == 1 and GetEventFlag(1041389412) == 1 and not GetEventFlag(11109258):
        """State 5"""
        assert t320006000_x18()
    else:
        """State 1"""
        if not GetEventFlag(11109256):
            """State 4"""
            assert t320006000_x13()
            """State 2"""
            if GetEventFlag(11109210) == 1:
                """State 6"""
                assert t320006000_x14()
            else:
                pass
        else:
            """State 7"""
            assert t320006000_x15()
    """State 8"""
    return 0

def t320006000_x5():
    """State 0,1"""
    assert t320006000_x8() and (CheckSpecificPersonTalkHasEnded(0) == 1 and not IsMenuOpen(63))
    """State 2"""
    assert t320006000_x9()
    """State 3"""
    return 0

def t320006000_x6():
    """State 0,1"""
    if not GetEventFlag(11109275):
        """State 3"""
        # talk:32006000:"Take a look around. The Roundtable Hold is burned. Razed to the ground."
        assert t320006000_x52(text3=32006000, mode5=1)
        """State 2"""
        SetEventFlag(11109275, 1)
    else:
        """State 4"""
        # talk:32006100:"I see. You're here for some spirit tuning?"
        assert t320006000_x52(text3=32006100, mode5=1)
    """State 5"""
    assert t320006000_x10()
    """State 6"""
    return 0

def t320006000_x7():
    """State 0,1"""
    if not GetEventFlag(1041389406):
        """State 2,11"""
        # talk:32000100:"Everyone's...been grafted."
        assert t320006000_x52(text3=32000100, mode5=1)
        """State 9"""
        if not GetEventFlag(60835):
            """State 8"""
            # gesture:93:Sitting Sideways
            AcquireGesture(93)
            SetEventFlag(60835, 1)
        else:
            """State 10"""
            pass
        """State 3"""
        SetEventFlag(1041389406, 1)
    elif not GetEventFlag(1041389407):
        """State 4,12"""
        # talk:32000200:"You're all on your own, are you?"
        assert t320006000_x52(text3=32000200, mode5=1)
        """State 5"""
        SetEventFlag(1041389407, 1)
    else:
        """State 6,13"""
        # talk:32000300:"Oh, I know."
        assert t320006000_x52(text3=32000300, mode5=1)
        """State 7"""
        SetEventFlag(1041389411, 1)
        """State 14"""
        # lot:101900:Spirit Jellyfish Ashes
        assert t320006000_x25(lot1=101900)
        """State 15"""
        # talk:32000310:"The poor thing deserves someone braver than myself…"
        assert t320006000_x52(text3=32000310, mode5=1)
    """State 16"""
    return 0

def t320006000_x8():
    """State 0,3"""
    SetEventFlag(1041382735, 1)
    """State 2"""
    if not GetEventFlag(11109265):
        """State 7"""
        # talk:32004000:"Good to see you again. Thank you very much!"
        assert t320006000_x52(text3=32004000, mode5=1)
        """State 5"""
        if not GetEventFlag(60835):
            """State 4"""
            # gesture:93:Sitting Sideways
            AcquireGesture(93)
            SetEventFlag(60835, 1)
        else:
            """State 6"""
            pass
        """State 1"""
        SetEventFlag(11109265, 1)
    else:
        """State 8"""
        # talk:32005000:"Greetings."
        assert t320006000_x52(text3=32005000, mode5=1)
    """State 9"""
    return 0

def t320006000_x9():
    """State 0,1"""
    c1_110()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 24,28"""
        assert t320006000_x19()
        """State 29"""
        assert t320006000_x20()
        """State 3"""
        # action:23200000:"Spirit Tuning"
        AddTalkListData(1, 23200000, -1)
        # action:23200001:"Talk"
        AddTalkListDataIf(GetEventFlag(11109266) == 1 and not GetEventFlag(11109267), 2, 23200001, -1)
        # action:23200009:"Please"
        AddTalkListDataIf(not GetEventFlag(1041389411), 3, 23200009, -1)
        # action:23200004:"There's something you should know"
        AddTalkListDataIf(GetEventFlag(11109260) == 1, 50, 23200004, -1)
        # action:23200005:"There's something you should know"
        AddTalkListDataIf(GetEventFlag(11109261) == 1, 50, 23200005, -1)
        # action:23200006:"About the spirits' voices"
        AddTalkListDataIf(GetEventFlag(11109262) == 1, 50, 23200006, -1)
        # action:23200007:"Please take care"
        AddTalkListDataIf(GetEventFlag(11109264) == 1, 50, 23200007, -1)
        # action:23200008:"About the spirits' voices"
        AddTalkListDataIf(GetEventFlag(11109263) == 1, 50, 23200008, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            OpenChampionsEquipmentShop(9100000, 9199999)
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            
        # if GetTalkListEntryResult() == 1:
            # """State 6,16"""
            # if GetEventFlag(11109266) == 1:
                # pass
            # else:
                # """State 17"""
                # SetEventFlag(1041389415, 1)
                # assert GetEventFlag(1041389416) == 1
                # """State 18"""
                # SetWorkValue(1, GetEventFlagValue(1041389417, 10))
                # """State 22"""
                # SetWorkValue(2, GetEventFlagValue(1041389427, 10))
            # """State 9"""
            # c1_136()
            # c1_141(23)
            # assert not (CheckSpecificPersonMenuIsOpen(23, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            # """State 23"""
            # if GetEventFlag(11109266) == 1:
                # pass
            # else:
                # """State 19"""
                # # goods:10903:Grave Glovewort [4], goods:10913:Ghost Glovewort [4]
                # if (ComparePlayerInventoryNumber(3, 10903, 0, GetWorkValue(1), 0) == 1 and ComparePlayerInventoryNumber(3,
                    # 10913, 0, GetWorkValue(2), 0) == 1):
                    # pass
                # else:
                    # """State 21"""
                    # SetEventFlag(11109266, 1)
                # """State 20"""
                # SetEventFlag(1041389415, 0)
                # SetEventFlag(1041389416, 0)
        elif GetTalkListEntryResult() == 2:
            """State 7,25"""
            # talk:32005100:"I feel like I'm really coming to grips with spirit tuning of late."
            assert t320006000_x52(text3=32005100, mode5=1)
            """State 12"""
            if not GetEventFlag(60803):
                """State 11"""
                # gesture:3:Curtsy
                AcquireGesture(3)
                SetEventFlag(60803, 1)
            else:
                """State 13"""
                pass
            """State 10"""
            SetEventFlag(11109267, 1)
            assert CheckSpecificPersonTalkHasEnded(0) == 1 and not IsMenuOpen(63)
        elif GetTalkListEntryResult() == 3:
            """State 14,26"""
            # talk:32005200:"I'd like to ask you a small favour."
            assert t320006000_x52(text3=32005200, mode5=1)
            """State 15"""
            SetEventFlag(1041389411, 1)
            """State 27"""
            # lot:101900:Spirit Jellyfish Ashes
            assert (t320006000_x25(lot1=101900) and (CheckSpecificPersonTalkHasEnded(0) == 1 and not
                    IsMenuOpen(63)))
        elif GetTalkListEntryResult() == 50:
            """State 30"""
            assert t320006000_x21() and CheckSpecificPersonTalkHasEnded(0) == 1
        else:
            """State 8,31"""
            return 0

def t320006000_x10():
    """State 0,1"""
    c1_110()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 3"""
        # action:23200000:"Spirit Tuning"
        AddTalkListData(1, 23200000, -1)
        # action:23200002:"About Hewg"
        AddTalkListDataIf(GetEventFlag(11109227) == 1 and not GetEventFlag(11109276), 2, 23200002, -1)
        # action:23200003:"What's happened to Hewg"
        AddTalkListDataIf(GetEventFlag(11109246) == 1 and not GetEventFlag(11109277), 3, 23200003, -1)
        # action:23200010:"Talk"
        AddTalkListDataIf(GetEventFlag(11109277) == 1 and not GetEventFlag(11109278), 4, 23200010, -1)
        # action:23200011:"Talk"
        AddTalkListDataIf(GetEventFlag(11109278) == 1 and not GetEventFlag(11109279), 5, 23200011, -1)
        # action:20000009:"Leave"
        AddTalkListData(99, 20000009, -1)
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            OpenChampionsEquipmentShop(9100000, 9199999)
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 7,17"""
            # talk:32007000:"Oh, is that right..."
            assert t320006000_x52(text3=32007000, mode5=1)
            """State 10"""
            SetEventFlag(11109276, 1)
            assert CheckSpecificPersonTalkHasEnded(0) == 1
        elif GetTalkListEntryResult() == 3:
            """State 9,18"""
            # talk:32008000:"Ah. So it wasn't just me this happened to..."
            assert t320006000_x52(text3=32008000, mode5=1)
            """State 11"""
            SetEventFlag(11109277, 1)
            assert CheckSpecificPersonTalkHasEnded(0) == 1
        elif GetTalkListEntryResult() == 4:
            """State 14,19"""
            # talk:32008100:"I'll remain with Hewg."
            assert t320006000_x52(text3=32008100, mode5=1)
            """State 13"""
            SetEventFlag(11109278, 1)
            assert CheckSpecificPersonTalkHasEnded(0) == 1
        elif GetTalkListEntryResult() == 5:
            """State 15,20"""
            # talk:32008200:"Please, become Elden Lord."
            assert t320006000_x52(text3=32008200, mode5=1)
            """State 16"""
            SetEventFlag(11109279, 1)
            SetEventFlag(1041382735, 1)
            assert CheckSpecificPersonTalkHasEnded(0) == 1
        else:
            """State 8,21"""
            return 0

def t320006000_x11():
    """State 0,2"""
    if not GetEventFlag(1041389413):
        """State 3"""
        # talk:32002000:"They all...believed in me."
        assert t320006000_x52(text3=32002000, mode5=1)
        """State 1"""
        SetEventFlag(1041389413, 1)
    else:
        """State 4"""
        # talk:32002100:"I think I'll head to the Roundtable Hold."
        assert t320006000_x52(text3=32002100, mode5=1)
    """State 5"""
    return 0

def t320006000_x12():
    """State 0,1"""
    ClearTalkListData()
    c1_110()
    """State 2"""
    # action:23201002:"Give Chrysalids' Memento"
    AddTalkListData(1, 23201002, -1)
    # action:20000009:"Leave"
    AddTalkListData(99, 20000009, -1)
    """State 3"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 4"""
    if GetTalkListEntryResult() == 1:
        """State 7,5"""
        # goods:8171:Chrysalids' Memento
        PlayerEquipmentQuantityChange(3, 8171, -1)
        """State 6"""
        SetEventFlag(1041389412, 1)
        """State 9"""
        # talk:32001300:"What's this?"
        assert t320006000_x52(text3=32001300, mode5=1)
    else:
        """State 8"""
        pass
    """State 10"""
    return 0

def t320006000_x13():
    """State 0,5"""
    if not GetEventFlag(11109255):
        """State 7"""
        SetEventFlag(1041382735, 1)
        """State 1"""
        if GetEventFlag(1041389406) == 1:
            """State 2,9"""
            # talk:32003000:"Greetings. Nice to see you again."
            assert t320006000_x52(text3=32003000, mode5=1)
        else:
            """State 3,10"""
            # talk:32003400:"A pleasure to meet you."
            assert t320006000_x52(text3=32003400, mode5=1)
        """State 4"""
        SetEventFlag(11109255, 1)
    else:
        """State 6"""
        if GetEventFlag(1041382735) == 1:
            """State 11"""
            # talk:32003500:"It's all a bit much for me, in truth."
            assert t320006000_x52(text3=32003500, mode5=1)
        else:
            """State 12"""
            # talk:32003600:"A pleasure to see you."
            assert t320006000_x52(text3=32003600, mode5=1)
        """State 8"""
        SetEventFlag(1041382735, 1)
    """State 13"""
    return 0

def t320006000_x14():
    """State 0,1"""
    ClearTalkListData()
    c1_110()
    """State 2"""
    # action:23201003:"Tell her what the blacksmith said"
    AddTalkListDataIf(GetEventFlag(11109210) == 1, 1, 23201003, -1)
    # action:23201004:"Don't tell her"
    AddTalkListData(2, 23201004, -1)
    """State 3"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 4"""
    if GetTalkListEntryResult() == 1:
        """State 5,7"""
        SetEventFlag(11109256, 1)
        """State 8"""
        # talk:32003200:"You're telling me I possess some kind of gift?"
        assert t320006000_x52(text3=32003200, mode5=1)
    else:
        """State 6"""
        pass
    """State 9"""
    return 0

def t320006000_x15():
    """State 0,1"""
    # talk:32003700:"If I do have a talent for spirit tuning, and goodness knows that would be a surprise…"
    assert t320006000_x52(text3=32003700, mode5=1)
    """State 2"""
    return 0

def t320006000_x16():
    """State 0,1"""
    assert t320006000_x6()
    """State 2"""
    return 0

def t320006000_x17():
    """State 0,1"""
    if GetEventFlag(1041382735) == 1 or not GetEventFlag(1041389408):
        """State 3"""
        # talk:32000500:"It was a pleasure to see you."
        assert t320006000_x52(text3=32000500, mode5=1)
        """State 2"""
        SetEventFlag(1041389408, 1)
    else:
        """State 4"""
        # talk:32001400:"A pleasure to see you."
        assert t320006000_x52(text3=32001400, mode5=1)
    """State 5"""
    return 0

def t320006000_x18():
    """State 0,2"""
    # talk:32003300:"Oh, and…"
    assert t320006000_x52(text3=32003300, mode5=1)
    """State 1"""
    SetEventFlag(11109258, 1)
    """State 3"""
    # lot:101910:Golden Seed
    assert t320006000_x25(lot1=101910)
    """State 4"""
    return 0

def t320006000_x19():
    """State 0,1"""
    SetEventFlag(11109260, 0)
    SetEventFlag(11109261, 0)
    SetEventFlag(11109262, 0)
    SetEventFlag(11109263, 0)
    SetEventFlag(11109264, 0)
    """State 2"""
    return 0

def t320006000_x20():
    """State 0,1"""
    if GetEventFlag(3063) == 1 and not GetEventFlag(11109268):
        """State 2"""
        SetEventFlag(11109260, 1)
    elif GetEventFlag(11109268) == 1 and not GetEventFlag(35009306):
        """State 3"""
        SetEventFlag(11109261, 1)
    elif GetEventFlag(11109268) == 1 and GetEventFlag(4247) == 1 and not GetEventFlag(11109270):
        """State 4"""
        SetEventFlag(11109262, 1)
    elif GetEventFlag(11109268) == 1 and GetEventFlag(4248) == 1 and not GetEventFlag(11109272):
        """State 6"""
        SetEventFlag(11109264, 1)
    elif GetEventFlag(11109272) == 1 and GetEventFlag(4249) == 1 and not GetEventFlag(11109271):
        """State 5"""
        SetEventFlag(11109263, 1)
    else:
        """State 7"""
        pass
    """State 8"""
    return 0

def t320006000_x21():
    """State 0,1"""
    if GetEventFlag(11109260) == 1:
        """State 8"""
        # talk:32005300:"I need to warn you about something."
        assert t320006000_x52(text3=32005300, mode5=1)
        """State 3"""
        SetEventFlag(11109268, 1)
    elif GetEventFlag(11109261) == 1:
        """State 9"""
        # talk:32005400:"I can hear it from across the wing, past the roundtable..."
        assert t320006000_x52(text3=32005400, mode5=1)
        """State 4"""
        SetEventFlag(11109269, 1)
    elif GetEventFlag(11109262) == 1:
        """State 11"""
        # talk:32005500:"I can't hear them any more; the voices of the spirits cowering from the curse..."
        assert t320006000_x52(text3=32005500, mode5=1)
        """State 5"""
        SetEventFlag(11109270, 1)
    elif GetEventFlag(11109264) == 1:
        """State 10"""
        # talk:32005600:"Be on your guard, I beg you."
        assert t320006000_x52(text3=32005600, mode5=1)
        """State 7"""
        SetEventFlag(11109272, 1)
    elif GetEventFlag(11109263) == 1:
        """State 12"""
        # talk:32005700:"The voices of the tormented spirits are silent again.."
        assert t320006000_x52(text3=32005700, mode5=1)
        """State 6"""
        SetEventFlag(11109271, 1)
    else:
        """State 2"""
        pass
    """State 13"""
    return 0

def t320006000_x22(actionbutton1=_, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000):
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
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t320006000_x23():
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

def t320006000_x24():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t320006000_x25(lot1=_):
    """State 0,1"""
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t320006000_x26(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t320006000_x42()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t320006000_x23()
    else:
        """State 4,7"""
        call = t320006000_x56()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t320006000_x23()
    """State 9"""
    return 0

def t320006000_x27():
    """State 0,1"""
    assert t320006000_x23()
    """State 2"""
    return 0

def t320006000_x28(flag1=3703, flag2=3701, flag3=3702, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t320006000_x45(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t320006000_x44()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t320006000_x29(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t320006000_x32(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t320006000_x36(val1=val1, z1=z1)
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
            call = t320006000_x38(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t320006000_x49() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t320006000_x34(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t320006000_x30(val2=10, val3=12):
    """State 0,1"""
    call = t320006000_x40(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t320006000_x26(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t320006000_x31(flag1=3703, val2=10, val3=12):
    """State 0,8"""
    assert t320006000_x58()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t320006000_x43()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t320006000_x23()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t320006000_x32(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t320006000_x33(z8=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t320006000_x22(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t320006000_x33(z8=_, val6=_):
    """State 0,1"""
    if f203(z8) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z8)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t320006000_x34(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t320006000_x23()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t320006000_x35()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t320006000_x50()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t320006000_x35():
    """State 0,1"""
    assert t320006000_x33(z8=1101, val6=1101)
    """State 2"""
    return 0

def t320006000_x36(val1=5, z1=1):
    """State 0,2"""
    assert t320006000_x46()
    """State 1"""
    call = t320006000_x37()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t320006000_x48()
    """State 4"""
    return 0

def t320006000_x37():
    """State 0,1"""
    assert t320006000_x33(z8=1000, val6=1000)
    """State 2"""
    return 0

def t320006000_x38(val5=12):
    """State 0,1"""
    call = t320006000_x39()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t320006000_x49()
    """State 3"""
    return 0

def t320006000_x39():
    """State 0,1"""
    assert t320006000_x33(z8=1100, val6=1100)
    """State 2"""
    return 0

def t320006000_x40(val2=10, val3=12):
    """State 0,5"""
    assert t320006000_x58()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t320006000_x41()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t320006000_x51()
    """Unused"""
    """State 6"""
    return 0

def t320006000_x41():
    """State 0,2"""
    call = t320006000_x33(z8=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t320006000_x42():
    """State 0,1"""
    assert t320006000_x33(z8=1001, val6=1001)
    """State 2"""
    return 0

def t320006000_x43():
    """State 0,1"""
    assert t320006000_x33(z8=1103, val6=1103)
    """State 2"""
    return 0

def t320006000_x44():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t320006000_x45(flag1=3703, flag2=3701, flag3=3702, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t320006000_x29(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t320006000_x31(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t320006000_x30(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t320006000_x57() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t320006000_x46():
    """State 0,1"""
    assert t320006000_x47()
    """State 2"""
    return 0

def t320006000_x47():
    """State 0,1"""
    assert t320006000_x33(z8=1104, val6=1104)
    """State 2"""
    return 0

def t320006000_x48():
    """State 0,1"""
    call = t320006000_x33(z8=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t320006000_x27()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t320006000_x49():
    """State 0,1"""
    call = t320006000_x33(z8=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t320006000_x27()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t320006000_x50():
    """State 0,1"""
    call = t320006000_x33(z8=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t320006000_x27()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t320006000_x51():
    """State 0,1"""
    call = t320006000_x33(z8=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t320006000_x27()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t320006000_x52(text3=_, mode5=1):
    """State 0,4"""
    assert t320006000_x24() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text3, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode5:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t320006000_x53(text2=_, z7=_, mode4=1):
    """State 0,5"""
    assert t320006000_x55() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z7, 1)
    """State 1"""
    TalkToPlayer(text2, -1, -1, 1)
    """State 4"""
    if not mode4:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t320006000_x54(text1=_, mode3=1):
    """State 0,4"""
    assert t320006000_x55() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, 1)
    """State 3"""
    if not mode3:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t320006000_x55():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t320006000_x56():
    """State 0,1"""
    assert t320006000_x33(z8=1002, val6=1002)
    """State 2"""
    return 0

def t320006000_x57():
    """State 0,1"""
    assert t320006000_x23()
    """State 2"""
    return 0

def t320006000_x58():
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

