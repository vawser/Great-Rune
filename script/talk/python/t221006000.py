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
            
#----------------------------------------------------
# Innards     
#----------------------------------------------------
def t221006000_x111():
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
            assert t221006000_x120(1047610210, 5, 80100300, 10, 80100600, 80100700)
            continue
        # Wisdom
        elif GetTalkListEntryResult() == 2:
            assert t221006000_x120(1047610220, 5, 80100310, 10, 80100601, 80100710)
            continue
        # Tenacity
        elif GetTalkListEntryResult() == 3:
            assert t221006000_x120(1047610230, 5, 80100320, 10, 80100602, 80100720)
            return 0
        # Fortitude
        elif GetTalkListEntryResult() == 4:
            assert t221006000_x120(1047610240, 5, 80100330, 10, 80100603, 80100730)
            return 0
        # Reflection
        elif GetTalkListEntryResult() == 5:
            assert t221006000_x120(1047610250, 5, 80100340, 10, 80100604, 80100740)
            return 0
        # Regeneration
        elif GetTalkListEntryResult() == 6:
            assert t221006000_x120(1047610260, 3, 80100350, 10, 80100605, 80100750)
            return 0
        # Tranquility
        elif GetTalkListEntryResult() == 7:
            assert t221006000_x120(1047610270, 3, 80100360, 10, 80100606, 80100760)
            return 0
        # Endurance
        elif GetTalkListEntryResult() == 8:
            assert t221006000_x120(1047610280, 5, 80100370, 10, 80100607, 80100770)
            return 0
        # Greed
        elif GetTalkListEntryResult() == 9:
            assert t221006000_x120(1047610290, 5, 80100380, 10, 80100608, 80100780)
            return 0
        # Finesse
        elif GetTalkListEntryResult() == 10:
            assert t221006000_x120(1047610300, 5, 80100390, 10, 80100609, 80100790)
            return 0
        # Courage
        elif GetTalkListEntryResult() == 11:
            assert t221006000_x120(1047610310, 5, 80100400, 10, 80100610, 80100800)
            return 0
        # Clarity
        elif GetTalkListEntryResult() == 12:
            assert t221006000_x120(1047610320, 5, 80100410, 10, 80100611, 80100810)
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
# Innards of X
def t221006000_x120(base_flag=_, max_count=_, rank_text=_, cost=_, cost_text=_, purchase_text=_):
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
                    assert t221006000_x151(80100014)
                else:
                    PlayerEquipmentQuantityChange(3, 1290, ( cost * -1 ) )
                    
                    # None -> Rank 1
                    if(GetEventFlag(base_flag) == 0):
                        SetEventFlag(base_flag, 1)
                        assert t221006000_x151(purchase_text)
                    # Rank 4 -> Rank 5
                    elif(GetEventFlag(base_flag + 3) == 1):
                        SetEventFlag(base_flag + 4, 1)
                        assert t221006000_x151(purchase_text + 4)
                    # Rank 3 -> Rank 4
                    elif(GetEventFlag(base_flag + 2) == 1):
                        SetEventFlag(base_flag + 3, 1)
                        assert t221006000_x151(purchase_text + 3)
                    # Rank 2 -> Rank 3
                    elif(GetEventFlag(base_flag + 1) == 1):
                        SetEventFlag(base_flag + 2, 1)
                        assert t221006000_x151(purchase_text + 2)
                    # Rank 1 -> Rank 2
                    elif(GetEventFlag(base_flag) == 1):
                        SetEventFlag(base_flag + 1, 1)
                        assert t221006000_x151(purchase_text + 1)
                    else:
                        pass
            # Cancel
            elif GetTalkListEntryResult() == 2:
                # Declined
                assert t221006000_x151(80100016)
                return 1
            else:
                return 2
   
            return 0
        # View Current Effect
        elif GetTalkListEntryResult() == 2:
            if(GetEventFlag(base_flag) == 0):
                assert t221006000_x151(80100500)
            elif(GetEventFlag(base_flag + 4) == 1):
                assert t221006000_x151(rank_text + 4)
            elif(GetEventFlag(base_flag + 3) == 1):
                assert t221006000_x151(rank_text + 3)
            elif(GetEventFlag(base_flag + 2) == 1):
                assert t221006000_x151(rank_text + 2)
            elif(GetEventFlag(base_flag + 1) == 1):
                assert t221006000_x151(rank_text + 1)
            elif(GetEventFlag(base_flag) == 1):
                assert t221006000_x151(rank_text)
            else:
                pass
                
            return 0
        # View Innard Effect
        elif GetTalkListEntryResult() == 3:
            assert t221006000_x151(rank_text)
                
            return 0
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0
            
#----------------------------------------------------------
# Utility
#----------------------------------------------------------
def t221006000_x151(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0
    