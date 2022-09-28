# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Grace #2
#-----------------------------------------------------
def t800003500_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t800003500_x52(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1)
    Quit()

def t800003500_1000():
    """State 0,2,3"""
    assert t800003500_x0()
    """State 1"""
    c1_120(1000)
    Quit()

def t800003500_1001():
    """State 0,2,3"""
    assert t800003500_x1()
    """State 1"""
    c1_120(1001)
    Quit()

def t800003500_1101():
    """State 0,2,3"""
    assert t800003500_x2()
    """State 1"""
    c1_120(1101)
    Quit()

def t800003500_1102():
    """State 0,2,3"""
    t800003500_x3()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t800003500_1103():
    """State 0,2,3"""
    assert t800003500_x4()
    """State 1"""
    c1_120(1103)
    Quit()

def t800003500_2000():
    """State 0,2,3"""
    assert t800003500_x5(val6=10, z5=12)
    """State 1"""
    c1_120(2000)
    Quit()

def t800003500_x0():
    """State 0,1"""
    if GetEventFlag(4705) == 1:
        """State 3"""
        assert t800003500_x6()
    else:
        """State 2"""
        pass
    """State 8"""
    Label('L0')
    return 0
    """Unused"""
    """State 4"""
    assert t800003500_x7()
    Goto('L0')
    """State 5"""
    assert t800003500_x8()
    Goto('L0')
    """State 6"""
    assert t800003500_x9()
    Goto('L0')
    """State 7"""
    assert t800003500_x10()
    Goto('L0')

def t800003500_x1():
    """State 0,2,6"""
    # talk:80080300:"Is that all you were, mate?"
    assert t800003500_x77(text1=80080300, mode3=1)
    """State 7"""
    Label('L0')
    return 0
    """Unused"""
    """State 1"""
    Goto('L1')
    """State 3,4"""
    Goto('L0')
    """State 5"""
    Label('L1')
    # talk:80081300:"I'll never forgive your kind..."
    assert t800003500_x77(text1=80081300, mode3=1)
    Goto('L0')

def t800003500_x2():
    """State 0,1,3,7"""
    assert t800003500_x41()
    """State 8"""
    Label('L0')
    return 0
    """Unused"""
    """State 2"""
    Goto('L1')
    """State 4,5"""
    Goto('L0')
    """State 6"""
    Label('L1')
    assert t800003500_x42()
    Goto('L0')

def t800003500_x3():
    """State 0,2"""
    if not GetEventFlag(1042369303):
        """State 3,7"""
        SetEventFlag(1042369303, 1)
        """State 6"""
        SetEventFlag(1042362710, 1)
        """State 9,11,15"""
        # talk:80080200:"I knew you for a highwayman all along."
        assert t800003500_x77(text1=80080200, mode3=1)
    elif not GetEventFlag(1042362710):
        """State 4,8"""
        SetEventFlag(1042362710, 1)
    else:
        """State 5"""
        pass
    """State 1"""
    Label('L0')
    Quit()
    """Unused"""
    """State 10"""
    Goto('L1')
    """State 12,13"""
    Goto('L0')
    """State 14"""
    Label('L1')
    # talk:80081200:"I see. I see how it is! You were one of them all along!"
    assert t800003500_x77(text1=80081200, mode3=1)
    Goto('L0')
    """State 16"""
    return 0

def t800003500_x4():
    """State 0,2,6"""
    # talk:80080400:"Is this...how it ends?"
    assert t800003500_x77(text1=80080400, mode3=1)
    """State 7"""
    Label('L0')
    return 0
    """Unused"""
    """State 1"""
    Goto('L1')
    """State 3,4"""
    Goto('L0')
    """State 5"""
    Label('L1')
    # talk:80081400:"Your kind...will all be razed clean."
    assert t800003500_x77(text1=80081400, mode3=1)
    Goto('L0')

def t800003500_x5(val6=10, z5=12):
    """State 0"""
    while True:
        """State 4"""
        Label('L0')
        if GetEventFlag(4705) == 1:
            """State 2,9"""
            call = t800003500_x40()
            if call.Done():
                break
            elif not GetEventFlag(4705):
                pass
        elif GetEventFlag(4717) == 1:
            """State 5,6"""
            assert not GetEventFlag(4717)
        else:
            """State 3,7"""
            # actionbutton:6000:"Talk"
            call = t800003500_x46(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000,
                                  flag12=6000, flag4=6000)
            if call.Done():
                break
            elif GetEventFlag(4705) == 1 or GetEventFlag(4709) == 1:
                pass
    """State 10"""
    Label('L1')
    return 0
    """Unused"""
    """State 1,8"""
    call = t800003500_x39(val6=val6, z5=z5)
    if call.Done():
        Goto('L1')
    elif not GetEventFlag(4709):
        Goto('L0')

def t800003500_x6():
    """State 0,1"""
    def WhilePaused():
        RequestAnimation(20008, -1)
    assert t800003500_x13()
    """State 2"""
    return 0

def t800003500_x7():
    """State 0,1"""
    assert t800003500_x21()
    """State 2"""
    return 0

def t800003500_x8():
    """State 0,1"""
    assert t800003500_x28()
    """State 2"""
    return 0

def t800003500_x9():
    """State 0,1"""
    if not GetEventFlag(35000500):
        """State 2"""
        assert t800003500_x37()
    else:
        """State 3"""
        assert t800003500_x38()
    """State 4"""
    return 0

def t800003500_x10():
    """State 0,3"""
    if not GetEventFlag(35000500):
        """State 4,6"""
        # talk:80007100:"The frenzied flame...burned me..."
        def WhilePaused():
            RequestAnimation(20041, -1)
        assert t800003500_x76(text2=80007100, mode4=1)
    else:
        """State 5,7"""
        # talk:80001500:"The howl of a wolf, in the Mistwood..."
        def WhilePaused():
            RequestAnimation(20041, -1)
        assert t800003500_x76(text2=80001500, mode4=1)
    """State 1"""
    SetEventFlag(35009270, 1)
    """State 2"""
    Quit()
    """Unused"""
    """State 8"""
    return 0

def t800003500_x11():
    """State 0,1"""
    SetEventFlag(1042362712, 1)
    """State 2"""
    return 0

def t800003500_x12():
    """State 0,1"""
    if not GetEventFlag(1042369308):
        """State 2,7"""
        # talk:80000100:"You're a Tarnished, I can see it."
        assert t800003500_x76(text2=80000100, mode4=1)
        """State 10"""
        assert t800003500_x11()
        """State 5"""
        SetEventFlag(1042369308, 1)
        """State 6"""
        SetEventFlag(1042369302, 1)
    elif GetEventFlag(1042362712) == 1:
        """State 3,8"""
        assert t800003500_x16()
    else:
        """State 4,9"""
        assert t800003500_x15()
    """State 11"""
    return 0

def t800003500_x13():
    """State 0,1"""
    assert t800003500_x12()
    """State 2"""
    assert t800003500_x14()
    """State 3"""
    return 0

def t800003500_x14():
    """State 0,19"""
    SetEventFlag(1042369306, 0)
    """State 20"""
    SetEventFlag(1042369307, 0)
    """State 1"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 27"""
        assert t800003500_x19()
        """State 29"""
        assert t800003500_x43()
        """State 3"""
        
        # DISABLE FOR RELEASE
        # Browse Inventory
        # AddTalkListData(10, 99999030, -1)
        # Browse Cut Content
        # AddTalkListData(11, 99999032, -1)
        # Get Runes
        # AddTalkListData(12, 99999200, -1)
        
        # action:20000010:"Purchase"
        AddTalkListData(1, 20000010, -1)
        # action:20000011:"Sell"
        AddTalkListData(2, 20000011, -1)
        # action:28000002:"About Kalé"
        AddTalkListDataIf(GetEventFlag(1042369319) == 1, 3, 28000002, -1)
        # action:28000004:"Talk"
        AddTalkListDataIf(GetEventFlag(1042369321) == 1, 3, 28000004, -1)
        # action:28000005:"Talk"
        AddTalkListDataIf(GetEventFlag(1042369322) == 1, 3, 28000005, -1)
        # action:28000014:"About the howling in Mistwood"
        AddTalkListDataIf(GetEventFlag(1042369320) == 1, 4, 28000014, -1)
        # action:28000015:"About Blaidd"
        AddTalkListDataIf(GetEventFlag(1042369325) == 1, 4, 28000015, -1)
        # goods:8500:Crafting Kit, action:28000003:"Recommendation"
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 8500, 1, 1, 0) == 1, 5, 28000003, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 6"""
            # goods:8500:Crafting Kit
            if ComparePlayerInventoryNumber(3, 8500, 4, 1, 0) == 1:
                """State 13"""
                pass
            else:
                """State 14,12"""
                SetEventFlag(1042369306, 1)
            """State 10"""
            OpenRegularShop(100500, 100524)
            c1_141(5)
            """State 24"""
            call = t800003500_x17()
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 18"""
            # goods:8500:Crafting Kit
            if ComparePlayerInventoryNumber(3, 8500, 4, 1, 0) == 1:
                """State 15,17"""
                SetEventFlag(1042369307, 1)
            else:
                """State 16"""
                pass
        elif GetTalkListEntryResult() == 2:
            """State 7,11"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 8,25"""
            assert t800003500_x18()
        elif GetTalkListEntryResult() == 4:
            """State 23,30"""
            assert t800003500_x44()
        elif GetTalkListEntryResult() == 5:
            """State 21,28"""
            # talk:80000800:"You know, if you can spare the runes,"
            assert t800003500_x76(text2=80000800, mode4=1)
            """State 22"""
            SetEventFlag(1042369314, 1)
        # Browse Inventory
        elif GetTalkListEntryResult() == 10:
            assert t800003500_x100()
        # Browse Cut Content
        elif GetTalkListEntryResult() == 11:
            assert t800003500_x200()
        # Get Runes
        elif GetTalkListEntryResult() == 12:
            GiveSpEffectToPlayer(9006000)
        else:
            """State 9,26"""
            assert t800003500_x20()
            """State 31"""
            return 0

def t800003500_x15():
    """State 0,1"""
    if not GetEventFlag(1042369311) and not GetEventFlag(4707):
        """State 2,4"""
        # talk:80000300:"Wait, weren't you...?"
        assert t800003500_x76(text2=80000300, mode4=1)
    else:
        """State 3,5"""
        # talk:80000400:"Ah, it's you again."
        assert t800003500_x76(text2=80000400, mode4=1)
    """State 6"""
    assert t800003500_x11()
    """State 7"""
    return 0

def t800003500_x16():
    """State 0,1"""
    # talk:80000200:"What is it? Still going to purchase something?"
    assert t800003500_x76(text2=80000200, mode4=1)
    """State 2"""
    return 0

def t800003500_x17():
    """State 0"""
    assert DidYouDoSomethingInTheMenu(0) == 1
    """State 12"""
    if not GetEventFlag(1042362713):
        """State 1,11"""
        SetEventFlag(1042362713, 1)
        """State 3"""
        if not GetEventFlag(1042369309):
            """State 4,7"""
            SetEventFlag(1042369309, 1)
        elif not GetEventFlag(1042369310):
            """State 5,8"""
            SetEventFlag(1042369310, 1)
        else:
            """State 6,9"""
            SetEventFlag(1042369311, 1)
    else:
        """State 2"""
        pass
    """State 10"""
    Quit()
    """Unused"""
    """State 13"""
    return 0

def t800003500_x18():
    """State 0,1"""
    if GetEventFlag(1042369319) == 1:
        """State 2,9"""
        # talk:80000700:"I am of a nomadic people."
        assert t800003500_x76(text2=80000700, mode4=1)
        """State 5"""
        SetEventFlag(1042369313, 1)
        """State 6"""
        SetEventFlag(1042362714, 1)
    elif GetEventFlag(1042369321) == 1:
        """State 3,10"""
        # talk:80001000:"There are others of my people who yet survive in these lands."
        assert t800003500_x76(text2=80001000, mode4=1)
        """State 7"""
        SetEventFlag(1042369315, 1)
    else:
        """State 4,11"""
        # talk:80001200:"Perhaps you don't need to hear this, but..."
        assert t800003500_x76(text2=80001200, mode4=1)
        """State 8"""
        SetEventFlag(1042369317, 1)
    """State 12"""
    return 0

def t800003500_x19():
    """State 0,1"""
    SetEventFlag(1042369319, 0)
    SetEventFlag(1042369321, 0)
    SetEventFlag(1042369322, 0)
    """State 2"""
    if not GetEventFlag(1042369313):
        """State 3"""
        SetEventFlag(1042369319, 1)
    elif GetEventFlag(1042369313) == 1 and not GetEventFlag(1042362714) and not GetEventFlag(1042369315):
        """State 4"""
        SetEventFlag(1042369321, 1)
    elif GetEventFlag(1042369315) == 1 and not GetEventFlag(1042369317):
        """State 5"""
        SetEventFlag(1042369322, 1)
    else:
        """State 6"""
        pass
    """State 7"""
    return 0

def t800003500_x20():
    """State 0,1"""
    if GetEventFlag(1042369306) == 1 and GetEventFlag(1042369307) == 1 and GetEventFlag(1042369314) == 1:
        """State 2,4"""
        # talk:80000900:"I'm glad you took my warning to heart."
        assert t800003500_x76(text2=80000900, mode4=1)
    else:
        """State 3,5"""
        assert t800003500_x26()
    """State 6"""
    return 0

def t800003500_x21():
    """State 0,1"""
    assert t800003500_x22()
    """State 2"""
    assert t800003500_x23()
    """State 3"""
    return 0

def t800003500_x22():
    """State 0,1"""
    if not GetEventFlag(1037429255) and not GetEventFlag(1042369311):
        """State 2,7"""
        # talk:80003100:"We meet again, I see."
        assert t800003500_x76(text2=80003100, mode4=1)
        """State 11"""
        Label('L0')
        assert t800003500_x11()
        """State 6"""
        SetEventFlag(1037429255, 1)
    elif not GetEventFlag(1037429255) and GetEventFlag(1042369311) == 1:
        """State 3,8"""
        # talk:80003000:"Ah, good to see you."
        assert t800003500_x76(text2=80003000, mode4=1)
        Goto('L0')
    elif GetEventFlag(1042362712) == 1:
        """State 4,9"""
        assert t800003500_x16()
    else:
        """State 5,10"""
        assert t800003500_x15()
    """State 12"""
    return 0

def t800003500_x23():
    """State 0,13"""
    SetEventFlag(1037429258, 0)
    """State 1"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 18"""
        assert t800003500_x27()
        """State 3"""
        # action:20000010:"Purchase"
        AddTalkListData(1, 20000010, -1)
        # action:20000011:"Sell"
        AddTalkListData(2, 20000011, -1)
        # action:28000013:""
        AddTalkListDataIf(GetEventFlag(1037429264) == 1, 3, 28000013, -1)
        # action:28000008:""
        AddTalkListDataIf(GetEventFlag(1037429265) == 1, 3, 28000008, -1)
        # action:28000009:""
        AddTalkListDataIf(GetEventFlag(1037429266) == 1, 3, 28000009, -1)
        # action:28000010:""
        AddTalkListDataIf(GetEventFlag(1037429267) == 1, 3, 28000010, -1)
        # goods:1200:Gold-Pickled Fowl Foot
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 1200, 4, 1, 0) == 1, 4, 28000000, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 6,11"""
            OpenRegularShop(100625, 100649)
            """State 14"""
            call = t800003500_x17()
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 7,12"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 8,15"""
            assert t800003500_x24()
        elif GetTalkListEntryResult() == 4:
            """State 9,16"""
            assert t800003500_x25()
        else:
            """State 10,17"""
            assert t800003500_x34()
            """State 19"""
            return 0

def t800003500_x24():
    """State 0,1"""
    if GetEventFlag(1037429264) == 1:
        """State 2,10"""
        # talk:80003200:"Have you seen a crow around here by any chance?"
        assert t800003500_x76(text2=80003200, mode4=1)
        """State 6"""
        SetEventFlag(1037429260, 1)
    elif GetEventFlag(1037429265) == 1:
        """State 3,11"""
        # talk:80003400:"So, about the letter you brought me..."
        assert t800003500_x76(text2=80003400, mode4=1)
        """State 7"""
        SetEventFlag(1037429261, 1)
    elif GetEventFlag(1037429266) == 1:
        """State 4,12"""
        # talk:80003600:"I've always preferred my own company, to that of other people's..."
        assert t800003500_x76(text2=80003600, mode4=1)
        """State 8"""
        SetEventFlag(1037429262, 1)
    else:
        """State 5,13"""
        # talk:80003500:"Once I decipher that cryptogram, I'll be packing up shop again."
        assert t800003500_x76(text2=80003500, mode4=1)
        """State 9"""
        SetEventFlag(1037429263, 1)
    """State 14"""
    return 0

def t800003500_x25():
    """State 0,8"""
    call = t800003500_x45(action1=28001001)
    if call.Get() == 0:
        """State 2,1"""
        # goods:1200:Gold-Pickled Fowl Foot
        PlayerEquipmentQuantityChange(3, 1200, -1)
        """State 4"""
        ChangePlayerStat(8, 0, 2000)
        """State 5"""
        SetEventFlag(1037429256, 1)
        """State 7"""
        SetEventFlag(1037422710, 1)
        """State 6"""
        SetEventFlag(1037429258, 1)
        """State 9"""
        # talk:80003300:"My thanks. I've been wanting to get my hands on this."
        assert t800003500_x76(text2=80003300, mode4=1)
    elif call.Done():
        """State 3"""
        pass
    """State 10"""
    return 0

def t800003500_x26():
    """State 0,1"""
    if DidYouDoSomethingInTheMenu(0) == 1:
        """State 2,4"""
        # talk:80000600:"Good-bye. Nice to do business."
        assert t800003500_x76(text2=80000600, mode4=1)
    else:
        """State 3,5"""
        # talk:80000500:"Good-bye for now."
        assert t800003500_x76(text2=80000500, mode4=1)
    """State 6"""
    return 0

def t800003500_x27():
    """State 0,2"""
    SetEventFlag(1037429264, 0)
    SetEventFlag(1037429265, 0)
    SetEventFlag(1037429266, 0)
    SetEventFlag(1037429267, 0)
    """State 1"""
    # goods:1200:Gold-Pickled Fowl Foot
    if ComparePlayerInventoryNumber(3, 1200, 1, 1, 0) == 1 and not GetEventFlag(1037429256):
        """State 3"""
        SetEventFlag(1037429264, 1)
    elif not GetEventFlag(1037422710) and GetEventFlag(1037429256) == 1 and not GetEventFlag(1037429261):
        """State 4"""
        SetEventFlag(1037429265, 1)
    elif GetEventFlag(1037429261) == 1 and not GetEventFlag(1037429262):
        """State 5"""
        SetEventFlag(1037429266, 1)
    elif GetEventFlag(1037429262) == 1 and GetEventFlag(62200) == 1:
        """State 6"""
        SetEventFlag(1037429267, 1)
    else:
        """State 7"""
        pass
    """State 8"""
    return 0

def t800003500_x28():
    """State 0,1"""
    assert t800003500_x29()
    """State 2"""
    assert t800003500_x30()
    """State 3"""
    return 0

def t800003500_x29():
    """State 0,1"""
    if not GetEventFlag(11009305):
        """State 2,6"""
        # talk:80005000:"Ah, good to see you."
        assert t800003500_x76(text2=80005000, mode4=1)
        """State 7"""
        assert t800003500_x11()
        """State 5"""
        SetEventFlag(11009305, 1)
    elif GetEventFlag(1042362712) == 1:
        """State 3,8"""
        assert t800003500_x16()
    else:
        """State 4,9"""
        assert t800003500_x15()
    """State 10"""
    return 0

def t800003500_x30():
    """State 0,13"""
    SetEventFlag(11009309, 0)
    """State 1"""
    c1_110()
    ClearTalkActionState()
    while True:
        """State 2"""
        ClearTalkListData()
        """State 18"""
        assert t800003500_x36()
        """State 3"""
        # action:20000010:"Purchase"
        AddTalkListData(1, 20000010, -1)
        # action:20000011:"Sell"
        AddTalkListData(2, 20000011, -1)
        # action:28000011:""
        AddTalkListDataIf(GetEventFlag(11009311) == 1, 3, 28000011, -1)
        # action:28000012:""
        AddTalkListDataIf(GetEventFlag(11009312) == 1, 3, 28000012, -1)
        # goods:1210:Exalted Flesh
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 1210, 4, 1, 0) == 1, 4, 28000001, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 5"""
        if GetTalkListEntryResult() == 1:
            """State 6,11"""
            OpenRegularShop(100650, 100674)
            """State 14"""
            call = t800003500_x17()
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            """State 7,12"""
            OpenSellShop(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(6, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 3:
            """State 8,16"""
            assert t800003500_x33()
        elif GetTalkListEntryResult() == 4:
            """State 9,15"""
            assert t800003500_x31()
        else:
            """State 10,17"""
            assert t800003500_x35()
            """State 19"""
            return 0

def t800003500_x31():
    """State 0,13"""
    call = t800003500_x45(action1=28001002)
    if call.Get() == 0:
        """State 2,1"""
        # goods:1210:Exalted Flesh
        PlayerEquipmentQuantityChange(3, 1210, -1)
        """State 4"""
        ChangePlayerStat(8, 0, 2000)
        """State 5"""
        SetEventFlag(11009306, 1)
        """State 6"""
        SetEventFlag(11009309, 1)
        """State 14"""
        # talk:80005200:"Where...did you find this letter?"
        assert t800003500_x76(text2=80005200, mode4=1)
        """State 7"""
        ClearTalkListData()
        """State 8"""
        AddTalkListData(1, 28001003, -1)
        """State 9"""
        OpenConversationChoicesMenu(0)
        assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 10"""
        if GetTalkListEntryResult() == 1:
            """State 11,15"""
            assert t800003500_x32()
        else:
            """State 12"""
            pass
    elif call.Done():
        """State 3"""
        pass
    """State 16"""
    return 0

def t800003500_x32():
    """State 0,2"""
    # talk:80005300:"I can't imagine how it ended up there..."
    assert t800003500_x76(text2=80005300, mode4=1)
    """State 1"""
    SetEventFlag(11009307, 1)
    """State 3"""
    # lot:100420:Glowstone
    assert t800003500_x49(lot1=100420)
    """State 4"""
    # talk:80005310:"I hope you can join me at the Great Caravan, in fact."
    assert t800003500_x76(text2=80005310, mode4=1)
    """State 5"""
    return 0

def t800003500_x33():
    """State 0,1"""
    if GetEventFlag(11009311) == 1:
        """State 2,5"""
        # talk:80005100:"Oh yes, about the cryptogram from the letter..."
        assert t800003500_x76(text2=80005100, mode4=1)
        """State 4"""
        SetEventFlag(11009310, 1)
    else:
        """State 3,6"""
        assert t800003500_x32()
    """State 7"""
    return 0

def t800003500_x34():
    """State 0,1"""
    if GetEventFlag(1037429258) == 1:
        """State 2,4"""
        # talk:80000600:"Good-bye. Nice to do business."
        assert t800003500_x76(text2=80000600, mode4=1)
    else:
        """State 3,5"""
        assert t800003500_x26()
    """State 6"""
    return 0

def t800003500_x35():
    """State 0,1"""
    if GetEventFlag(11009309) == 1:
        """State 2,4"""
        # talk:80000600:"Good-bye. Nice to do business."
        assert t800003500_x76(text2=80000600, mode4=1)
    else:
        """State 3,5"""
        assert t800003500_x26()
    """State 6"""
    return 0

def t800003500_x36():
    """State 0,1"""
    SetEventFlag(11009311, 0)
    SetEventFlag(11009312, 0)
    """State 2"""
    if not GetEventFlag(11009310):
        """State 3"""
        SetEventFlag(11009311, 1)
    elif GetEventFlag(11009306) == 1 and not GetEventFlag(11009307):
        """State 4"""
        SetEventFlag(11009312, 1)
    else:
        """State 5"""
        pass
    """State 6"""
    return 0

def t800003500_x37():
    """State 0,1"""
    if not GetEventFlag(35009255):
        """State 2,10"""
        # talk:80005400:"Ah, you, is it..."
        assert t800003500_x76(text2=80005400, mode4=1)
        """State 6"""
        SetEventFlag(35009255, 1)
    elif not GetEventFlag(35009256):
        """State 3,11"""
        # talk:80005500:"I'm sorry, but we won't be trading any longer."
        assert t800003500_x76(text2=80005500, mode4=1)
        """State 7"""
        SetEventFlag(35009256, 1)
    elif not GetEventFlag(35009257):
        """State 4,12"""
        # talk:80005600:"I should apologise to you."
        assert t800003500_x76(text2=80005600, mode4=1)
        """State 8"""
        SetEventFlag(35009257, 1)
    else:
        """State 5,13"""
        # talk:80005700:"I'm sorry, but we won't be trading any longer."
        assert t800003500_x76(text2=80005700, mode4=1)
        """State 9"""
        SetEventFlag(35009255, 1)
    """State 14"""
    return 0

def t800003500_x38():
    """State 0,1"""
    if not GetEventFlag(35009254):
        """State 2,5"""
        # talk:80005800:"Wait, what's that?"
        assert t800003500_x76(text2=80005800, mode4=1)
        """State 4"""
        SetEventFlag(35009254, 1)
    else:
        """State 3,6"""
        # talk:80005900:"Oh, that's it... That's what I need..."
        assert t800003500_x76(text2=80005900, mode4=1)
    """State 7"""
    return 0

def t800003500_x39(val6=10, z5=12):
    """State 0"""
    while True:
        """State 3"""
        SetEventFlag(35002710, 0)
        if GetEventFlag(4703) == 1:
            break
        elif not GetEventFlag(35002710) and GetDistanceToPlayer() < val6:
            """State 1"""
            SetEventFlag(35002710, 1)
            """State 4"""
            # talk:80007000:"O Three Fingers, throw wide the door."
            assert t800003500_x77(text1=80007000, mode3=1) and GetCurrentStateElapsedTime() > 35
    """State 2"""
    Quit()
    """Unused"""
    """State 5"""
    return 0

def t800003500_x40():
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6000:"Talk"
        call = t800003500_x46(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                              flag4=6000)
        if call.Done():
            break
        elif GetEventFlag(1042362715) == 1 and not GetEventFlag(1042362716):
            """State 1,2"""
            SetEventFlag(1042362716, 1)
            """State 4"""
            # talk:80080100:"What's the matter with you?"
            assert t800003500_x77(text1=80080100, mode3=1)
    """State 5"""
    return 0

def t800003500_x41():
    """State 0,1"""
    if not GetEventFlag(1042362711) and not GetEventFlag(1042362716):
        """State 2,6"""
        SetEventFlag(1042362711, 1)
        """State 10"""
        # talk:80080000:"Urgh!"
        assert t800003500_x77(text1=80080000, mode3=1)
    elif GetEventFlag(1042362711) == 1 and not GetEventFlag(1042362716):
        """State 3,8"""
        SetEventFlag(1042362716, 1)
        """State 11"""
        # talk:80080100:"What's the matter with you?"
        assert t800003500_x77(text1=80080100, mode3=1)
    elif not GetEventFlag(1042362711) and GetEventFlag(1042362716) == 1:
        """State 4,9"""
        SetEventFlag(1042362711, 1)
        """State 12"""
        # talk:80080000:"Urgh!"
        assert t800003500_x77(text1=80080000, mode3=1)
    else:
        """State 5"""
        """State 7"""
        pass
    """State 13"""
    return 0

def t800003500_x42():
    """State 0,1"""
    if not GetEventFlag(1042362711):
        """State 2,5"""
        SetEventFlag(1042362711, 1)
        """State 7"""
        # talk:80081000:"<takes damage>"
        assert t800003500_x77(text1=80081000, mode3=1)
    elif not GetEventFlag(1042362716):
        """State 3,6"""
        SetEventFlag(1042362716, 1)
        """State 8"""
        # talk:80081100:"So you're just like the others?"
        assert t800003500_x77(text1=80081100, mode3=1)
    else:
        """State 4"""
        pass
    """State 9"""
    return 0

def t800003500_x43():
    """State 0,1"""
    SetEventFlag(1042369320, 0)
    SetEventFlag(1042369325, 0)
    """State 2"""
    if GetEventFlag(1045379206) == 1 and not GetEventFlag(1045379205) and not GetEventFlag(1042369328):
        """State 3"""
        SetEventFlag(1042369320, 1)
    elif GetEventFlag(1045379205) == 1 and GetEventFlag(1042369328) == 1 and not GetEventFlag(1042369329):
        """State 4"""
        SetEventFlag(1042369325, 1)
    else:
        """State 5"""
        pass
    """State 6"""
    return 0

def t800003500_x44():
    """State 0,1"""
    if GetEventFlag(1042369320) == 1:
        """State 2,10"""
        # talk:80001500:"The howl of a wolf, in the Mistwood..."
        assert t800003500_x76(text2=80001500, mode4=1)
        """State 4"""
        SetEventFlag(1042369328, 1)
        if not GetEventFlag(60830):
            """State 6,9"""
            SetEventFlag(60830, 1)
            """State 8"""
            # gesture:73:Finger Snap
            AcquireGesture(73)
            assert GetCurrentStateElapsedTime() > 1
        else:
            """State 7"""
            pass
    else:
        """State 3,11"""
        # talk:80001700:"Oh, then you met Blaidd, did you?"
        assert t800003500_x76(text2=80001700, mode4=1)
        """State 5"""
        SetEventFlag(1042369329, 1)
    """State 12"""
    return 0

def t800003500_x45(action1=_):
    """State 0,1"""
    OpenGenericDialog(8, action1, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t800003500_x46(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t800003500_x47():
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

def t800003500_x48():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t800003500_x49(lot1=100420):
    """State 0,1"""
    # lot:100420:Glowstone
    AwardItemLot(lot1)
    assert not IsMenuOpen(63) and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    return 0

def t800003500_x50(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t800003500_x66()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t800003500_x47()
    else:
        """State 4,7"""
        call = t800003500_x79()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t800003500_x47()
    """State 9"""
    return 0

def t800003500_x51():
    """State 0,1"""
    assert t800003500_x47()
    """State 2"""
    return 0

def t800003500_x52(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t800003500_x69(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t800003500_x68()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t800003500_x53(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                   flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                   mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t800003500_x56(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t800003500_x60(val1=val1, z1=z1)
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
            call = t800003500_x62(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t800003500_x73() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t800003500_x58(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t800003500_x54(val2=10, val3=12):
    """State 0,1"""
    call = t800003500_x64(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t800003500_x50(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t800003500_x55(flag1=6000, val2=10, val3=12):
    """State 0,8"""
    assert t800003500_x81()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t800003500_x67()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t800003500_x47()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t800003500_x56(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t800003500_x57(z6=2000, val7=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t800003500_x46(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800003500_x57(z6=_, val7=_):
    """State 0,1"""
    if f203(z6) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z6)
        assert f202() == val7
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t800003500_x58(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t800003500_x47()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t800003500_x59()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t800003500_x74()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t800003500_x59():
    """State 0,1"""
    assert t800003500_x57(z6=1101, val7=1101)
    """State 2"""
    return 0

def t800003500_x60(val1=5, z1=1):
    """State 0,2"""
    assert t800003500_x70()
    """State 1"""
    call = t800003500_x61()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t800003500_x72()
    """State 4"""
    return 0

def t800003500_x61():
    """State 0,1"""
    assert t800003500_x57(z6=1000, val7=1000)
    """State 2"""
    return 0

def t800003500_x62(val5=12):
    """State 0,1"""
    call = t800003500_x63()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t800003500_x73()
    """State 3"""
    return 0

def t800003500_x63():
    """State 0,1"""
    assert t800003500_x57(z6=1100, val7=1100)
    """State 2"""
    return 0

def t800003500_x64(val2=10, val3=12):
    """State 0,5"""
    assert t800003500_x81()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t800003500_x65()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t800003500_x75()
    """Unused"""
    """State 6"""
    return 0

def t800003500_x65():
    """State 0,2"""
    call = t800003500_x57(z6=1102, val7=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t800003500_x66():
    """State 0,1"""
    assert t800003500_x57(z6=1001, val7=1001)
    """State 2"""
    return 0

def t800003500_x67():
    """State 0,1"""
    assert t800003500_x57(z6=1103, val7=1103)
    """State 2"""
    return 0

def t800003500_x68():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t800003500_x69(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t800003500_x53(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                              flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                              z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t800003500_x55(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t800003500_x54(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t800003500_x80() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t800003500_x70():
    """State 0,1"""
    assert t800003500_x71()
    """State 2"""
    return 0

def t800003500_x71():
    """State 0,1"""
    assert t800003500_x57(z6=1104, val7=1104)
    """State 2"""
    return 0

def t800003500_x72():
    """State 0,1"""
    call = t800003500_x57(z6=1201, val7=1201)
    if call.Get() == 1:
        """State 2"""
        assert t800003500_x51()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800003500_x73():
    """State 0,1"""
    call = t800003500_x57(z6=1300, val7=1300)
    if call.Get() == 1:
        """State 2"""
        assert t800003500_x51()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800003500_x74():
    """State 0,1"""
    call = t800003500_x57(z6=1301, val7=1301)
    if call.Get() == 1:
        """State 2"""
        assert t800003500_x51()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800003500_x75():
    """State 0,1"""
    call = t800003500_x57(z6=1302, val7=1302)
    if call.Get() == 1:
        """State 2"""
        assert t800003500_x51()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t800003500_x76(text2=_, mode4=1):
    """State 0,4"""
    assert t800003500_x48() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t800003500_x77(text1=_, mode3=1):
    """State 0,4"""
    assert t800003500_x78() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t800003500_x78():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t800003500_x79():
    """State 0,1"""
    assert t800003500_x57(z6=1002, val7=1002)
    """State 2"""
    return 0

def t800003500_x80():
    """State 0,1"""
    assert t800003500_x47()
    """State 2"""
    return 0

def t800003500_x81():
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

# Browse Inventory
def t800003500_x100():

    c1_110()
    ClearTalkActionState()
    
    while True:
        """State 2"""
        ClearTalkListData()
        
        # Weapons
        AddTalkListData(1, 99999000, -1)
        # Ammunition
        AddTalkListData(2, 99999004, -1)
        # Spells
        AddTalkListData(3, 99999002, -1)
        # Ashes of War
        AddTalkListData(4, 99999005, -1)
        # Armor
        AddTalkListData(5, 99999001, -1)
        # Talismans
        AddTalkListData(6, 99999003, -1)
        # Items
        AddTalkListData(7, 99999031, -1)
        # Gestures
        AddTalkListData(11, 99999010, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Weapons
        if GetTalkListEntryResult() == 1:
            OpenRegularShop(9300000, 9309999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Armor
        elif GetTalkListEntryResult() == 5:
            OpenRegularShop(9310000, 9319999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Spells
        elif GetTalkListEntryResult() == 3:
            OpenRegularShop(9320000, 9329999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Talismans
        elif GetTalkListEntryResult() == 6:
            OpenRegularShop(9330000, 9339999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Ammunition
        elif GetTalkListEntryResult() == 2:
            OpenRegularShop(9340000, 9349999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Ashes of War
        elif GetTalkListEntryResult() == 4:
            OpenRegularShop(9350000, 9359999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Items
        elif GetTalkListEntryResult() == 7:
            assert t800003500_x101()
        # Gestures
        elif GetTalkListEntryResult() == 11:
            assert t800003500_x110()
        else:
            return 0
            
# Item Menu
def t800003500_x101():
    c1_110()
    ClearTalkActionState()
    
    while True:
        """State 2"""
        ClearTalkListData()

        # Consumables
        AddTalkListData(1, 99999006, -1)
        # Materials
        AddTalkListData(2, 99999008, -1)
        # Spirit Summons
        AddTalkListData(3, 99999007, -1)
        # Miscellenous Items
        AddTalkListData(4, 99999009, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Consumables
        if GetTalkListEntryResult() == 1:
            OpenRegularShop(9370000, 9379999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Materials
        elif GetTalkListEntryResult() == 2:
            OpenRegularShop(9380000, 9389999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Spirit Summons
        elif GetTalkListEntryResult() == 3:
            OpenRegularShop(9360000, 9369999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Miscellenous Items
        elif GetTalkListEntryResult() == 4:
            OpenRegularShop(9390000, 9399999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        else:
            return 0
            
# Gesture Menu
def t800003500_x110():
    c1_110()
    ClearTalkActionState()
    
    while True:
        """State 2"""
        ClearTalkListData()
        
        # Unlock
        AddTalkListData(1, 99999100, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))

        # Gestures
        if GetTalkListEntryResult() == 1:
            # 
            AcquireGesture(0)
            SetEventFlag(60800, 1)
            # 
            AcquireGesture(1)
            SetEventFlag(60801, 1)
            # 
            AcquireGesture(2)
            SetEventFlag(60802, 1)
            # Curtsy
            AcquireGesture(3)
            SetEventFlag(60803, 1)
            # 
            AcquireGesture(4)
            SetEventFlag(60804, 1)
            # My Lord
            AcquireGesture(5)
            SetEventFlag(60805, 1)
            # 
            AcquireGesture(6)
            SetEventFlag(60806, 1)
            # 
            AcquireGesture(7)
            SetEventFlag(60807, 1)
            # 
            AcquireGesture(8)
            SetEventFlag(60808, 1)
            # 
            AcquireGesture(9)
            SetEventFlag(60809, 1)
            # As You Wish
            AcquireGesture(10)
            SetEventFlag(60810, 1)
            # 
            AcquireGesture(20)
            SetEventFlag(60811, 1)
            # 
            AcquireGesture(21)
            SetEventFlag(60812, 1)
            # 
            AcquireGesture(22)
            SetEventFlag(60813, 1)
            # 
            AcquireGesture(23)
            SetEventFlag(60814, 1)
            # 
            AcquireGesture(24)
            SetEventFlag(60815, 1)
            # Calm Down!
            AcquireGesture(25)
            SetEventFlag(60816, 1)
            # Nod In Thought
            AcquireGesture(30)
            SetEventFlag(60817, 1)
            # 
            AcquireGesture(40)
            SetEventFlag(60818, 1)
            # Grovel For Mercy
            AcquireGesture(41)
            SetEventFlag(60819, 1)
            # 
            AcquireGesture(50)
            SetEventFlag(60820, 1)
            # Heartening Cry
            AcquireGesture(51)
            SetEventFlag(60821, 1)
            # 
            AcquireGesture(52)
            SetEventFlag(60822, 1)
            # 
            AcquireGesture(53)
            SetEventFlag(60823, 1)
            # 
            AcquireGesture(54)
            SetEventFlag(60824, 1)
            # 
            AcquireGesture(60)
            SetEventFlag(60826, 1)
            # 
            AcquireGesture(70)
            SetEventFlag(60827, 1)
            # Triumphant Delight
            AcquireGesture(71)
            SetEventFlag(60828, 1)
            # 
            AcquireGesture(72)
            SetEventFlag(60829, 1)
            # Finger Snap
            AcquireGesture(73)
            SetEventFlag(60830, 1)
            # 
            AcquireGesture(80)
            SetEventFlag(60831, 1)
            # Patches Squat
            AcquireGesture(90)
            SetEventFlag(60832, 1)
            # 
            AcquireGesture(91)
            SetEventFlag(60833, 1)
            # 
            AcquireGesture(92)
            SetEventFlag(60834, 1)
            # Sitting Sideways
            AcquireGesture(93)
            SetEventFlag(60835, 1)
            # 
            AcquireGesture(94)
            SetEventFlag(60836, 1)
            # Spread Out
            AcquireGesture(95)
            SetEventFlag(60837, 1)
            # Balled Up
            AcquireGesture(97)
            SetEventFlag(60839, 1)
            # What Do You Want?
            AcquireGesture(98)
            SetEventFlag(60840, 1)
            # Prayer
            AcquireGesture(100)
            SetEventFlag(60841, 1)
            # Desperate Prayer
            AcquireGesture(101)
            SetEventFlag(60842, 1)
            # 
            AcquireGesture(102)
            SetEventFlag(60843, 1)
            SetEventFlag(60844, 1)
            # Erudition
            AcquireGesture(103)
            SetEventFlag(60845, 1)
            # Outer Order
            AcquireGesture(104)
            SetEventFlag(60846, 1)
            # Inner Order
            AcquireGesture(105)
            SetEventFlag(60847, 1)
            # Golden Order Totality
            AcquireGesture(106)
            SetEventFlag(60848, 1)
            # 
            AcquireGesture(108)
            SetEventFlag(60849, 1)
            
            # All gestures unlocked.
            OpenGenericDialog(7, 99999011, 1, 0, 1)
            
            return 0
        else:
            return 0
            
# Browse Cut Content
def t800003500_x200():

    c1_110()
    ClearTalkActionState()
    
    while True:
        """State 2"""
        ClearTalkListData()
        
        # Armor
        AddTalkListData(5, 99999001, -1)
        # Goods
        AddTalkListData(7, 99999033, -1)
        # Gestures
        AddTalkListData(11, 99999010, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Armor
        if GetTalkListEntryResult() == 5:
            OpenRegularShop(9410000, 9419999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Goods
        elif GetTalkListEntryResult() == 7:
            OpenRegularShop(9400000, 9409999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Gestures
        elif GetTalkListEntryResult() == 11:
            assert t800003500_x210()
        else:
            return 0
            
# Gesture Menu
def t800003500_x210():
    c1_110()
    ClearTalkActionState()
    
    while True:
        """State 2"""
        ClearTalkListData()
        
        # Unlock
        AddTalkListData(1, 99999100, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        """State 4"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))

        # Gestures
        if GetTalkListEntryResult() == 1:
            # Carian Oath
            AcquireGesture(55)
            SetEventFlag(60825, 1)
            # Fetal Position
            AcquireGesture(96)
            SetEventFlag(60838, 1)
            
            # All gestures unlocked.
            OpenGenericDialog(7, 99999011, 1, 0, 1)
            
            return 0
        else:
            return 0