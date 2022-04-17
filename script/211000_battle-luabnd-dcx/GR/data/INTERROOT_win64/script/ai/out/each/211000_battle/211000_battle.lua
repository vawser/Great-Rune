RegisterTableGoal(GOAL_BlackSwordMariques211000_Battle, "BlackSwordMariques211000_Battle")
REGISTER_GOAL_NO_SUB_GOAL(GOAL_BlackSwordMariques211000_Battle, true)
Goal.Initialize = function (arg0, arg1, arg2, arg3)
    return 
end

Goal.Activate = function (arg0, arg1, arg2)
    Init_Pseudo_Global(arg1, arg2)
    arg1:SetStringIndexedNumber("Dist_SideStep", 5)
    arg1:SetStringIndexedNumber("Dist_BackStep", 5)
    
    local local0 = {}
    local local1 = {}
    local local2 = {}
    
    Common_Clear_Param(local0, local1, local2)
    
    local local3 = arg1:GetDist(TARGET_ENE_0)
    local local4 = arg1:GetRandam_Int(1, 100)
    local local5 = arg1:GetExcelParam(AI_EXCEL_THINK_PARAM_TYPE__thinkAttr_doAdmirer)
    local local6 = arg1:GetEventRequest()
    
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5026)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5027)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5028)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5029)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5031)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5032)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5033)
    
    if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 240, -1, 999) then
        if 10 < local3 then
            local0[1] = 20
            local0[3] = 25
            local0[4] = 20
            local0[8] = 35
            local0[41] = 0
            local0[44] = 0
        elseif 7 < local3 then
            local0[1] = 30
            local0[4] = 15
            local0[2] = 0
            local0[5] = 30
            local0[6] = 25
        elseif 2.5 < local3 then
            local0[2] = 20
            local0[5] = 40
            local0[6] = 30
            local0[10] = 10
            local0[12] = 20
        else
            local0[1] = 0
            local0[2] = 30
            local0[4] = 20
            local0[5] = 0
            local0[7] = 15
            local0[10] = 10
            local0[11] = 25
            local0[12] = 30
            local0[40] = 0
            local0[41] = 0
            local0[43] = 0
        end
    elseif local3 < 2.5 then
        local0[2] = 20
        local0[9] = 80
        local0[12] = 20
    elseif local3 < 20 then
        local0[2] = 100
    else
        local0[42] = 100
    end
    
    if arg1:HasSpecialEffectId(TARGET_SELF, 18699) then
        local0[10] = 0
    end
    
    local0[1] = SetCoolTime(arg1, arg2, 3000, 20, local0[1], 0)
    local0[2] = SetCoolTime(arg1, arg2, 3001, 20, local0[2], 1)
    local0[2] = SetCoolTime(arg1, arg2, 3002, 20, local0[2], 1)
    local0[3] = SetCoolTime(arg1, arg2, 3003, 20, local0[3], 0)
    local0[4] = SetCoolTime(arg1, arg2, 3005, 25, local0[4], 0)
    local0[5] = SetCoolTime(arg1, arg2, 3007, 10, local0[5], 1)
    local0[6] = SetCoolTime(arg1, arg2, 3010, 10, local0[6], 1)
    local0[7] = SetCoolTime(arg1, arg2, 3011, 20, local0[7], 1)
    local0[8] = SetCoolTime(arg1, arg2, 3012, 10, local0[8], 1)
    local0[9] = SetCoolTime(arg1, arg2, 3014, 20, local0[9], 0)
    local0[10] = SetCoolTime(arg1, arg2, 3015, 40, local0[10], 0)
    local0[11] = SetCoolTime(arg1, arg2, 3038, 15, local0[11], 0)
    local0[12] = SetCoolTime(arg1, arg2, 3017, 15, local0[12], 1)
    local0[12] = SetCoolTime(arg1, arg2, 3018, 15, local0[12], 1)
    
    local1[1] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act01)
    local1[2] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act02)
    local1[3] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act03)
    local1[4] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act04)
    local1[5] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act05)
    local1[6] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act06)
    local1[7] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act07)
    local1[8] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act08)
    local1[9] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act09)
    local1[10] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act10)
    local1[11] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act11)
    local1[12] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act12)
    local1[40] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act40)
    local1[41] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act41)
    local1[42] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act42)
    local1[43] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act43)
    local1[44] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act44)
    local1[45] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act45)
    local1[46] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_Act46)
    
    Common_Battle_Activate(arg1, arg2, local0, local1, REGIST_FUNC(arg1, arg2, BlackSwordMariques211000_ActAfter_AdjustSpace), local2)
    return 
end

-- Bestial Sling
function BlackSwordMariques211000_Act01(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 15, 0, 999, 0, 0, 2, 2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Side Dodge -> Bestial Sling
function BlackSwordMariques211000_Act02(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    if arg0:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 180) then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3001, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
        GetWellSpace_Odds = 0
        return GetWellSpace_Odds
    else
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3002, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
        GetWellSpace_Odds = 0
        return GetWellSpace_Odds
    end
end

-- Rock Toss
function BlackSwordMariques211000_Act03(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 20, 0, 999, 0, 0, 2, 2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5026)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3003, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end
 
-- Slam -> Beast Claw
function BlackSwordMariques211000_Act04(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5031)
    Approach_Act_Flex(arg0, arg1, 30, 0, 999, 0, 0, 2, 2)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3005, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Quick Slash
function BlackSwordMariques211000_Act05(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 7, 0, 999, 0, 0, 2, 2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5027)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5028)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5032)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3007, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Beast Claw
function BlackSwordMariques211000_Act06(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 9, 0, 999, 0, 0, 2, 2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3010, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Slash and Backspin
function BlackSwordMariques211000_Act07(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3011, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Forward Thrust
function BlackSwordMariques211000_Act08(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 12.5, 0, 999, 100, 0, 2, 10)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5027)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5028)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5029)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5032)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5033)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3012, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Side Slash -> Jump Dodge
function BlackSwordMariques211000_Act09(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3014, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Large Rock Toss
function BlackSwordMariques211000_Act10(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3015, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Backstep -> Bestial Sling
function BlackSwordMariques211000_Act11(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3038, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Side Dodge -> Thrust
function BlackSwordMariques211000_Act12(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5027)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5028)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5029)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5032)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5033)
    if arg0:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 180) then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3017, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
        GetWellSpace_Odds = 0
        return GetWellSpace_Odds
    else
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3018, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
        GetWellSpace_Odds = 0
        return GetWellSpace_Odds
    end
end

-- Approach (Close)
function BlackSwordMariques211000_Act40(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, 2, TARGET_SELF, true, -1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Approach (Medium)
function BlackSwordMariques211000_Act41(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, 8, TARGET_SELF, false, -1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Turn
function BlackSwordMariques211000_Act42(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_COMMON_Turn, 2, TARGET_ENE_0, arg0:GetRandam_Int(15, 20), 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Step
function BlackSwordMariques211000_Act43(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_COMMON_StepSafety, 1, 0, 100, 0, 0, TARGET_ENE_0, 1, 0, true)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Side Move
function BlackSwordMariques211000_Act44(arg0, arg1, arg2)
    local local0 = true
    arg1:AddSubGoal(GOAL_COMMON_SidewayMove, 2, TARGET_ENE_0, arg0:GetRandam_Int(0, 1), 15, true, isLifeSuccess, -1, GUARD_GOAL_DESIRE_RET_Failed)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Approach
function BlackSwordMariques211000_Act45(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_COMMON_ApproachTarget, 6, TARGET_ENE_0, 15, TARGET_SELF, true, -1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

-- Leave Target
function BlackSwordMariques211000_Act46(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_COMMON_LeaveTargetToPathEnd, 3, TARGET_ENE_0, 8, TARGET_ENE_0, true, -1, GUARD_GOAL_DESIRE_RET_Failed, false, 1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211000_ActAfter_AdjustSpace(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_BlackSwordMariques211000_AfterAttackAct, 10)
    return 
end

Goal.Update = function (arg0, arg1, arg2)
    return Update_Default_NoSubGoal(arg0, arg1, arg2)
end

Goal.Terminate = function (arg0, arg1, arg2)
    return 
end

Goal.Interrupt = function (arg0, arg1, arg2)
    if arg1:IsLadderAct(TARGET_SELF) then
        return false
    end
    local local0 = 5 - arg1:GetMapHitRadius(TARGET_SELF)
    local local1 = 0
    local local2 = 20
    local local3 = arg1:GetDist(TARGET_ENE_0)
    local local4 = arg1:GetRandam_Int(1, 100)
    local local5 = arg1:GetRandam_Int(1, 100)
    
    local interruptRoll = arg1:GetRandam_Int(1, 100)
    
    if arg1:IsInterupt(INTERUPT_Damaged) then

    end
    
    -- SpEffect Interrupts
    if arg1:IsInterupt(INTERUPT_ActivateSpecialEffect) then
    
        -- Rock Toss occured
        if arg1:HasSpecialEffectId(TARGET_SELF, 5026) then
        
            -- Player infront of enemy
            -- Player within 10m of enemy
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 20 + arg1:GetMapHitRadius(TARGET_SELF)) and 10 < local3 then
            
                -- Bestial Sling
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3004, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            end
            
        -- Slash/Thrust occured
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 5027) then
        
            -- Player infront of enemy
            -- Player within 1.5m of enemy
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 7 + arg1:GetMapHitRadius(TARGET_SELF)) and 1.5 < local3 then
            
                -- Quick Slash
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3008, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            -- Player infront of enemy
            -- Player beyond 1.5m of enemy
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 15 + arg1:GetMapHitRadius(TARGET_SELF)) and local3 < 1.5 then
                if local4 < 60 and arg1:GetTimer(1) <= 0 then
                    
                    -- Double Slash
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3016, TARGET_ENE_0, 0, 0, 0, 0, 0)
                    arg1:SetTimer(1, 15)
                elseif local5 < 70 and 20 < arg1:GetAttackPassedTime(3005) then
                
                    -- Beast Claw
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3005, TARGET_ENE_0, 0, 0, 0, 0, 0)
                else
                    -- Backstep -> Bestial Sling
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3038, TARGET_ENE_0, 0, 0, 0, 0, 0)
                end
                return true
            end
        -- Slash/Thrust occured
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 5028) then
            -- Player infront of enemy
            -- Player within 1.5m of enemy
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 200, -1, 3.6 + arg1:GetMapHitRadius(TARGET_SELF)) and 1.5 < local3 then
            
                -- Downwards Slam
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3009, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            -- Player infront of enemy
            -- Player within 1.5m of enemy
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 5.5 + arg1:GetMapHitRadius(TARGET_SELF)) and 1.5 < local3 then
                if 50 < local4 then
                
                    -- Downwards Slam
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3009, TARGET_ENE_0, 0, 0, 0, 0, 0)
                    return true
                else
                
                    -- Side Slash
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3039, TARGET_ENE_0, 0, 0, 0, 0, 0)
                    return true
                end
            -- Player infront of enemy
            -- Player within 1.5m of enemy
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 9 + arg1:GetMapHitRadius(TARGET_SELF)) and 1.5 < local3 then
            
                -- Side Slash
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3039, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            -- Player infront of enemy
            -- Player beyond 1.5m of enemy
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 15 + arg1:GetMapHitRadius(TARGET_SELF)) and local3 < 1.5 then
                if local4 < 60 and arg1:GetTimer(1) <= 0 then
                    -- Backstep -> Double Slash
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3016, TARGET_ENE_0, 0, 0, 0, 0, 0)
                    arg1:SetTimer(1, 15)
                elseif local5 < 70 and 20 < arg1:GetAttackPassedTime(3005) then
                
                    -- Beast Claw
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3005, TARGET_ENE_0, 0, 0, 0, 0, 0)
                else
                
                    -- Backstep -> Bestial Sling
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3038, TARGET_ENE_0, 0, 0, 0, 0, 0)
                end
                return true
            end
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 5029) then
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 8.2 + arg1:GetMapHitRadius(TARGET_SELF)) and 2.5 < local3 then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3013, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 15 + arg1:GetMapHitRadius(TARGET_SELF)) and local3 < 3.5 then
                if local4 < 60 and arg1:GetTimer(1) <= 0 then
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3016, TARGET_ENE_0, 0, 0, 0, 0, 0)
                    arg1:SetTimer(1, 15)
                elseif local5 < 70 and 20 < arg1:GetAttackPassedTime(3005) then
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3005, TARGET_ENE_0, 0, 0, 0, 0, 0)
                else
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3038, TARGET_ENE_0, 0, 0, 0, 0, 0)
                end
                return true
            end
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 5031) then
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 50 + arg1:GetMapHitRadius(TARGET_SELF)) and 9 < local3 then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3006, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            end
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 5032) then
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 200, -1, 5.4 + arg1:GetMapHitRadius(TARGET_SELF)) and 1.5 < local3 then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3009, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 15 + arg1:GetMapHitRadius(TARGET_SELF)) and local3 < 1.5 then
                if local4 < 60 and arg1:GetTimer(1) <= 0 then
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3016, TARGET_ENE_0, 0, 0, 0, 0, 0)
                    arg1:SetTimer(1, 15)
                elseif local5 < 70 and 20 < arg1:GetAttackPassedTime(3005) then
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3005, TARGET_ENE_0, 0, 0, 0, 0, 0)
                else
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3038, TARGET_ENE_0, 0, 0, 0, 0, 0)
                end
                return true
            end
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 5033) then
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 7 + arg1:GetMapHitRadius(TARGET_SELF)) and 1.5 < local3 then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3008, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 15 + arg1:GetMapHitRadius(TARGET_SELF)) and local3 < 1.5 then
                if local4 < 60 and arg1:GetTimer(1) <= 0 then
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3016, TARGET_ENE_0, 0, 0, 0, 0, 0)
                    arg1:SetTimer(1, 15)
                elseif local5 < 70 and 20 < arg1:GetAttackPassedTime(3005) then
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3005, TARGET_ENE_0, 0, 0, 0, 0, 0)
                else
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 5, 3038, TARGET_ENE_0, 0, 0, 0, 0, 0)
                end
                return true
            end
        end
    end
    return false
end

RegisterTableGoal(GOAL_BlackSwordMariques211000_AfterAttackAct, "BlackSwordMariques211000_AfterAttackAct")
REGISTER_GOAL_NO_SUB_GOAL(GOAL_BlackSwordMariques211000_AfterAttackAct, true)
Goal.Update = function (arg0, arg1, arg2)
    return Update_Default_NoSubGoal(arg0, arg1, arg2)
end

return 
