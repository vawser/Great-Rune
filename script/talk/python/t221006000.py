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
        # eventflag:400470:lot:104700:Great-Jar's Arsenal
        if GetEventFlag(400470) == 1:
            """State 3"""
            call = t221006000_x7()
            if call.Done():
                assert t221006000_x110()
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
   
#----------------------------------------------------
# Innards     
#----------------------------------------------------
# Great Jar - Shop
def t221006000_x110():
    while True:
        ClearTalkListData()
        c1_110()
        
        # Offer Innards
        AddTalkListData(1, 80100000, -1)
        
        # Browse Collection
        AddTalkListData(2, 80100010, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Offer Innards
        if GetTalkListEntryResult() == 1:
            assert t221006000_x111()
            assert not (CheckSpecificPersonMenuIsOpen(28, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Browse Collection
        elif GetTalkListEntryResult() == 2:
            OpenRegularShop(9201000, 9201999)
            assert not (CheckSpecificPersonMenuIsOpen(28, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        else:
            """State 6,8"""
            return 0
            
def t221006000_x111():
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
            assert t221006000_x120()
            continue
        # Wisdom
        elif GetTalkListEntryResult() == 2:
            assert t221006000_x121()
            continue
        # Tenacity
        elif GetTalkListEntryResult() == 3:
            assert t221006000_x122()
            return 0
        # Fortitude
        elif GetTalkListEntryResult() == 4:
            assert t221006000_x123()
            return 0
        # Reflection
        elif GetTalkListEntryResult() == 5:
            assert t221006000_x124()
            return 0
        # Regeneration
        elif GetTalkListEntryResult() == 6:
            assert t221006000_x125()
            return 0
        # Tranquility
        elif GetTalkListEntryResult() == 7:
            assert t221006000_x126()
            return 0
        # Endurance
        elif GetTalkListEntryResult() == 8:
            assert t221006000_x127()
            return 0
        # Greed
        elif GetTalkListEntryResult() == 9:
            assert t221006000_x128()
            return 0
        # Finesse
        elif GetTalkListEntryResult() == 10:
            assert t221006000_x129()
            return 0
        # Courage
        elif GetTalkListEntryResult() == 11:
            assert t221006000_x130()
            return 0
        # Clarity
        elif GetTalkListEntryResult() == 12:
            assert t221006000_x131()
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Vitality
def t221006000_x120():
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
            assert t221006000_x150(30000, 80100200, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t221006000_x151(80100300)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Wisdom
def t221006000_x121():
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
            assert t221006000_x150(30010, 80100201, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t221006000_x151(80100301)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Tenacity
def t221006000_x122():
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
            assert t221006000_x150(30020, 80100202, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t221006000_x151(80100302)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Fortitude
def t221006000_x123():
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
            assert t221006000_x150(30030, 80100203, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t221006000_x151(80100303)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Reflection
def t221006000_x124():
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
            assert t221006000_x150(30040, 80100204, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t221006000_x151(80100304)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Regeneration
def t221006000_x125():
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
            assert t221006000_x150(30050, 80100205, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t221006000_x151(80100305)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Tranquility
def t221006000_x126():
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
            assert t221006000_x150(30060, 80100206, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t221006000_x151(80100306)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Endurance
def t221006000_x127():
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
            assert t221006000_x150(30070, 80100207, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t221006000_x151(80100307)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Greed
def t221006000_x128():
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
            assert t221006000_x150(30080, 80100208, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t221006000_x151(80100308)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Finesse
def t221006000_x129():
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
            assert t221006000_x150(30090, 80100209, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t221006000_x151(80100309)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Courage
def t221006000_x130():
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
            assert t221006000_x150(30100, 80100210, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t221006000_x151(80100310)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of Clarity
def t221006000_x131():
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
            assert t221006000_x150(30110, 80100211, -10)
            return 0
        # View Effect
        elif GetTalkListEntryResult() == 2:
            assert t221006000_x151(80100311)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
#----------------------------------------------------------
# Utility
#----------------------------------------------------------
def t221006000_x150(innard_item=_, purchase_message=_, cost=_):
    # Purchase this innard
    call = t221006000_x151(80100013)
    
    if call.Get() == 0:
        if ComparePlayerInventoryNumber(3, 1290, 3, cost, 0) == 1:
            # Insufficient Potent Innards
            assert t221006000_x151(80100014)
        else:
            PlayerEquipmentQuantityChange(3, 1290, cost)
            PlayerEquipmentQuantityChange(3, innard_item, 1)
            
            # X purchased
            assert t221006000_x151(purchase_message)
    elif call.Get() == 1:
        pass
    return 0
    
def t221006000_x151(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0