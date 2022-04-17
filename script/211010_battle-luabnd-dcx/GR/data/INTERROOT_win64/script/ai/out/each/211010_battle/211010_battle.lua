RegisterTableGoal(GOAL_BlackSwordMariques211010_Battle, "BlackSwordMariques211010_Battle")
REGISTER_GOAL_NO_SUB_GOAL(GOAL_BlackSwordMariques211010_Battle, true)
Goal.Initialize = function (arg0, arg1, arg2, arg3)
    arg1:SetStringIndexedNumber("WallGrapple_Flg", 0)
    arg1:SetStringIndexedNumber("WallDoesExist", 0)
    arg1:SetStringIndexedNumber("Disenchant_Cnt", 0)
    arg1:SetStringIndexedNumber("Wait_Cnt", 0)
    arg1:SetStringIndexedNumber("isCombo", 0)
    arg1:SetNumber(0, 0)
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
    arg1:SetStringIndexedNumber("isCombo", 0)
    if arg1:IsEventFlag(13002822) == true or arg1:IsEventFlag(13002823) == true or arg1:IsEventFlag(13002824) == true then
        arg1:SetStringIndexedNumber("WallGrapple_Flg", 1)
    else
        arg1:SetStringIndexedNumber("WallGrapple_Flg", 0)
    end
    if 0 < arg1:GetStringIndexedNumber("Disenchant_Cnt") and arg1:HasSpecialEffectId(TARGET_SELF, 15253) then
        arg1:SetStringIndexedNumber("Disenchant_Cnt", 0)
    elseif arg1:HasSpecialEffectId(TARGET_SELF, 15254) then
        arg1:SetStringIndexedNumber("Disenchant_Cnt", arg1:GetStringIndexedNumber("Disenchant_Cnt") + 1)
    end
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5026)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5027)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5028)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5029)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5030)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5031)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5032)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5033)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 15255)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 15256)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 15258)
    if arg1:HasSpecialEffectId(TARGET_SELF, 5034) then
        if arg1:HasSpecialEffectId(TARGET_SELF, 15299) then
            local0[22] = 50
        else
            local0[21] = 50
            local0[22] = 50
        end
    elseif arg1:HasSpecialEffectId(TARGET_SELF, 15270) and arg1:HasSpecialEffectId(TARGET_SELF, 5034) == false then
        local0[26] = 10000
    elseif arg1:HasSpecialEffectId(TARGET_SELF, 15299) and arg1:GetStringIndexedNumber("WallGrapple_Flg") == 1 then
        local0[23] = 10000
    elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 360, -1, 5 + arg1:GetMapHitRadius(TARGET_SELF)) and arg1:GetTimer(0) <= 0 and arg1:GetStringIndexedNumber("WallGrapple_Flg") == 1 then
        local0[23] = 30
    elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 240, -1, 999) then
        if 15 < local3 then
            if arg1:HasSpecialEffectId(TARGET_SELF, 15252) then
                local0[1] = 30
                local0[18] = 30
                local0[5] = 30
                if arg1:GetHpRate(TARGET_SELF) <= 0.7 then
                    local0[13] = 90
                end
            else
                local0[1] = 30
                local0[18] = 30
                local0[5] = 30
                if arg1:GetHpRate(TARGET_SELF) <= 0.7 then
                    local0[13] = 30
                end
            end
        elseif 6 < local3 then
            if not not arg1:HasSpecialEffectId(TARGET_SELF, 15252) or arg1:HasSpecialEffectId(TARGET_SELF, 15252) then
                local0[1] = 20
                local0[18] = 20
                local0[14] = 25
                if arg1:GetHpRate(TARGET_SELF) <= 0.7 then
                    local0[15] = 40
                end
            else
                local0[1] = 25
                local0[18] = 25
                local0[5] = 35
                local0[14] = 30
                if arg1:GetHpRate(TARGET_SELF) <= 0.7 then
                    local0[15] = 25
                end
            end
        elseif 4 < local3 then
            local0[1] = 30
            local0[18] = 30
            local0[5] = 25
            local0[14] = 20
            if arg1:GetHpRate(TARGET_SELF) <= 0.7 then
                local0[7] = 15
                local0[15] = 10
            end
        elseif 1.5 < local3 then
            if arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 180) then
                local0[4] = 0
                local0[5] = 20
                local0[6] = 0
                local0[14] = 30
                local0[20] = 20
                if arg1:GetHpRate(TARGET_SELF) <= 0.7 then
                    local0[15] = 10
                    local0[7] = 20
                end
            elseif arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
                local0[4] = 20
                local0[5] = 0
                local0[6] = 0
                local0[14] = 30
                local0[17] = 30
                local0[20] = 20
                if arg1:GetHpRate(TARGET_SELF) <= 0.7 then
                    local0[15] = 20
                    local0[7] = 10
                end
            end
        elseif -2 < local3 then
            if arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 180) then
                if arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 60) then
                    local0[4] = 0
                    local0[5] = 10
                    local0[6] = 50
                    local0[17] = 50
                    local0[19] = 25
                    local0[20] = 20
                    if arg1:GetHpRate(TARGET_SELF) <= 0.7 then
                        local0[7] = 20
                    end
                else
                    local0[4] = 0
                    local0[5] = 45
                    local0[6] = 0
                    local0[17] = 50
                    local0[19] = 25
                    local0[20] = 20
                    if arg1:GetHpRate(TARGET_SELF) <= 0.7 then
                        local0[7] = 35
                    end
                end
            elseif arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
                if arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 60) then
                    local0[4] = 10
                    local0[5] = 0
                    local0[6] = 50
                    local0[17] = 50
                    local0[19] = 25
                    local0[20] = 20
                    if arg1:GetHpRate(TARGET_SELF) <= 0.7 then
                        local0[15] = 20
                    end
                else
                    local0[4] = 20
                    local0[5] = 0
                    local0[6] = 0
                    local0[17] = 50
                    local0[19] = 25
                    local0[20] = 20
                    if arg1:GetHpRate(TARGET_SELF) <= 0.7 then
                        local0[15] = 35
                    end
                end
            end
        elseif arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 180) then
            local0[4] = 0
            local0[5] = 10
            local0[6] = 30
            local0[17] = 30
            local0[19] = 25
            local0[20] = 30
            if arg1:GetHpRate(TARGET_SELF) <= 0.7 then
                local0[7] = 25
                local0[15] = 20
            end
        elseif arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
            local0[4] = 10
            local0[5] = 0
            local0[6] = 35
            local0[17] = 50
            local0[19] = 25
            local0[20] = 35
            if arg1:GetHpRate(TARGET_SELF) <= 0.7 then
                local0[15] = 30
            end
        end
    elseif local3 < 0 then
        if arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 180) then
            local0[4] = 0
            local0[5] = 20
            local0[6] = 80
        elseif arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
            local0[4] = 20
            local0[5] = 0
            local0[6] = 30
            local0[17] = 50
        end
    elseif arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 180) then
        local0[4] = 0
        local0[5] = 0
        local0[6] = 0
        local0[42] = 100
    elseif arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
        local0[4] = 100
        local0[5] = 0
        local0[6] = 0
    end
    if arg1:GetNumber(0) == 0 then
        arg1:SetNumber(0, 1)
        local0[1] = 100000
    end
    if arg1:GetHpRate(TARGET_SELF) <= 0.7 and arg1:GetTimer(2) <= 0 and arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 120) and local3 <= 5 then
        local0[25] = 60
    end
    local0[20] = 0
    local0[1] = SetCoolTime(arg1, arg2, 3016, 30, local0[1], 1)
    local0[2] = SetCoolTime(arg1, arg2, 3021, 20, local0[2], 1)
    local0[3] = SetCoolTime(arg1, arg2, 3022, 15, local0[3], 0)
    local0[4] = SetCoolTime(arg1, arg2, 3026, 20, local0[4], 1)
    local0[5] = SetCoolTime(arg1, arg2, 3027, 15, local0[5], 0)
    local0[6] = SetCoolTime(arg1, arg2, 3028, 15, local0[6], 1)
    local0[7] = SetCoolTime(arg1, arg2, 3031, 15, local0[7], 1)
    local0[8] = SetCoolTime(arg1, arg2, 3032, 60, local0[8], 1)
    local0[9] = SetCoolTime(arg1, arg2, 3033, 45, local0[9], 1)
    local0[10] = SetCoolTime(arg1, arg2, 3034, 60, local0[10], 0)
    local0[11] = SetCoolTime(arg1, arg2, 3029, 30, local0[11], 0)
    local0[12] = SetCoolTime(arg1, arg2, 3023, 15, local0[12], 0)
    local0[13] = SetCoolTime(arg1, arg2, 3035, 20, local0[13], 1)
    local0[13] = SetCoolTime(arg1, arg2, 3030, 15, local0[13], 1)
    local0[14] = SetCoolTime(arg1, arg2, 3025, 10, local0[14], 1)
    local0[14] = SetCoolTime(arg1, arg2, 3020, 10, local0[14], 1)
    local0[15] = SetCoolTime(arg1, arg2, 3030, 20, local0[15], 1)
    local0[15] = SetCoolTime(arg1, arg2, 3035, 15, local0[15], 1)
    local0[17] = SetCoolTime(arg1, arg2, 3003, 16, local0[17], 1)
    local0[18] = SetCoolTime(arg1, arg2, 3001, 15, local0[18], 1)
    local0[19] = SetCoolTime(arg1, arg2, 3000, 15, local0[19], 1)
    local0[20] = SetCoolTime(arg1, arg2, 3036, 60, local0[20], 1)
    local0[44] = SetCoolTime(arg1, arg2, 2002, 30, local0[44], 0)
    local0[44] = SetCoolTime(arg1, arg2, 2003, 30, local0[44], 0)
    local1[1] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act01)
    local1[2] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act02)
    local1[3] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act03)
    local1[4] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act04)
    local1[5] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act05)
    local1[6] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act06)
    local1[7] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act07)
    local1[8] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act08)
    local1[9] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act09)
    local1[10] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act10)
    local1[11] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act11)
    local1[12] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act12)
    local1[13] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act13)
    local1[14] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act14)
    local1[15] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act15)
    local1[16] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act16)
    local1[17] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act17)
    local1[18] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act18)
    local1[19] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act19)
    local1[20] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act20)
    local1[21] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act21)
    local1[22] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act22)
    local1[23] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act23)
    local1[25] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act25)
    local1[26] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act26)
    local1[40] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act40)
    local1[41] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act41)
    local1[42] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act42)
    local1[43] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act43)
    local1[44] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act44)
    local1[45] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act45)
    local1[46] = REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_Act46)
    Common_Battle_Activate(arg1, arg2, local0, local1, REGIST_FUNC(arg1, arg2, BlackSwordMariques211010_ActAfter_AdjustSpace), local2)
    return 
end

function BlackSwordMariques211010_Act01(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 10, 0, 999, 0, 0, 5, 5)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5027)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5028)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5029)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5031)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5032)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5033)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3016, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act02(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 10, 0, 999, 0, 0, 5, 5)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3021, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act03(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 8, 0, 999, 0, 0, 5, 5)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 20, 3022, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act04(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3026, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act05(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5027)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5028)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5029)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5031)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5032)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5033)
    Approach_Act_Flex(arg0, arg1, 15, 0, 999, 100, 0, 5, 5)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3027, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act06(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5027)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5028)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5029)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5031)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5032)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5033)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3028, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act07(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 20, 0, 999, 100, 0, 5, 5)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5027)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5028)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5029)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5031)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5032)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5033)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3031, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act08(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 25, 0, 999, 0, 0, 5, 5)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3032, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act09(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 20, 0, 999, 0, 0, 5, 5)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3033, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act10(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 11, 0, 999, 0, 0, 5, 5)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3034, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act11(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 8.5, 0, 999, 0, 0, 5, 5)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3029, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act12(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 17, 0, 999, 0, 0, 5, 5)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5027)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5028)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5029)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5030)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5031)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5032)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5033)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3023, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act13(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 20, 0, 999, 100, 0, 5, 5)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 15256)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3035, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act14(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 10, 0, 999, 0, 0, 5, 5)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5027)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5028)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5029)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5031)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5032)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5033)
    arg0:SetTimer(1, 20)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3025, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act15(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 15255)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3030, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act16(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 20, 3033, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act17(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 20, 3003, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act18(arg0, arg1, arg2)
    Approach_Act_Flex(arg0, arg1, 8, 0, 999, 0, 0, 5, 5)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5027)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5028)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5029)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5031)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5032)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5033)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3001, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act19(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5027)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5028)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5029)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5031)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5032)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5033)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 15258)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 20, 3000, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act20(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 15, 3036, TARGET_SELF, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act21(arg0, arg1, arg2)
    if arg0:HasSpecialEffectId(TARGET_SELF, 15299) == false then
        arg0:SetTimer(0, 15)
    end
    arg0:SetStringIndexedNumber("Wait_Cnt", 0)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3037, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act22(arg0, arg1, arg2)
    if arg0:HasSpecialEffectId(TARGET_SELF, 15299) == false then
        arg0:SetTimer(0, 20)
    end
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3038, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act23(arg0, arg1, arg2)
    if arg0:HasSpecialEffectId(TARGET_SELF, 15299) == false then
        arg0:SetTimer(0, 5)
    end
    local local0 = 15
    local local1 = 3036
    local local2 = 5 - arg0:GetMapHitRadius(TARGET_SELF)
    local local3 = 0
    local local4 = 0
    if arg0:GetStringIndexedNumber("isCombo") == 1 then
        arg1:AddSubGoal(GOAL_COMMON_ComboRepeat, local0, local1, POINT_EVENT, local2, local3, local4, 0, 0)
    else
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, local0, local1, POINT_EVENT, local2, local3, local4, 0, 0)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act25(arg0, arg1, arg2)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5025)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5027)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5028)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5029)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5031)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5032)
    arg0:AddObserveSpecialEffectAttribute(TARGET_SELF, 5033)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3015, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    arg0:SetTimer(2, 30)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act26(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 20006, TARGET_ENE_0, 5 - arg0:GetMapHitRadius(TARGET_SELF), 0, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act40(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_COMMON_ApproachTarget, 3, TARGET_ENE_0, 14.8, TARGET_SELF, true, -1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act41(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, 8, TARGET_SELF, false, -1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act42(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_COMMON_Turn, 2, TARGET_ENE_0, arg0:GetRandam_Int(55, 60), 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act43(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_COMMON_StepSafety, 1, 0, 100, 0, 0, TARGET_ENE_0, 1, 0, true)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act44(arg0, arg1, arg2)
    local local0 = true
    arg1:AddSubGoal(GOAL_COMMON_SidewayMove, 3.5, TARGET_ENE_0, arg0:GetRandam_Int(0, 1), 100, true, isLifeSuccess, -1, GUARD_GOAL_DESIRE_RET_Failed)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act45(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_COMMON_ApproachTarget, 6, TARGET_ENE_0, 15, TARGET_SELF, true, -1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_Act46(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_COMMON_LeaveTargetToPathEnd, 3, TARGET_ENE_0, 8, TARGET_ENE_0, true, -1, GUARD_GOAL_DESIRE_RET_Failed, false, 1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function BlackSwordMariques211010_ActAfter_AdjustSpace(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_BlackSwordMariques211010_AfterAttackAct, 10)
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
    if arg1:IsEventFlag(13002822) == true or arg1:IsEventFlag(13002823) == true or arg1:IsEventFlag(13002824) == true then
        arg1:SetStringIndexedNumber("WallGrapple_Flg", 1)
    else
        arg1:SetStringIndexedNumber("WallGrapple_Flg", 0)
    end
    arg1:SetStringIndexedNumber("isCombo", 1)
    if arg1:IsInterupt(INTERUPT_Damaged) then

    end
    if arg1:IsInterupt(INTERUPT_Shoot) and arg1:HasSpecialEffectId(TARGET_SELF, 15257) and arg1:GetTimer(4) <= 0 and arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 120) then
        arg2:ClearSubGoal()
        if 15 < local3 then
            Approach_Act_Flex(arg1, arg2, 13, 0, 999, 100, 0, 5, 5)
        end
        arg1:SetTimer(4, 5)
        arg2:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 1.5, 3027, TARGET_ENE_0, 0, 0, 0, 0, 0)
        return true
    elseif arg1:IsInterupt(INTERUPT_ActivateSpecialEffect) then
        if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 360, -1, 5 + arg1:GetMapHitRadius(TARGET_SELF)) and arg1:GetTimer(0) <= 0 and arg1:GetStringIndexedNumber("WallGrapple_Flg") == 1 and (not not arg1:HasSpecialEffectId(TARGET_SELF, 15258) or not not arg1:HasSpecialEffectId(TARGET_SELF, 5027) or not not arg1:HasSpecialEffectId(TARGET_SELF, 5028) or arg1:HasSpecialEffectId(TARGET_SELF, 5032)) then
            arg2:ClearSubGoal()
            BlackSwordMariques211010_Act23(arg1, arg2)
            return true
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 5027) then
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, -1, 4.5 + arg1:GetMapHitRadius(TARGET_SELF)) and arg1:GetRemainingAttackCoolTime(3003) <= 0 and local4 < 45 then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3003, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, -1, 9.5 + arg1:GetMapHitRadius(TARGET_SELF)) and 2.5 < local3 then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3017, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, -1, 9.5 + arg1:GetMapHitRadius(TARGET_SELF)) then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3002, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            end
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 5028) then
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, -1, 8 + arg1:GetMapHitRadius(TARGET_SELF)) and 1 < local3 then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3018, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 40 + arg1:GetMapHitRadius(TARGET_SELF)) and 1 < local3 and arg1:GetTimer(1) <= 0 then
                arg1:SetTimer(1, 30)
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3025, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            elseif local3 < 1 then
                arg2:ClearSubGoal()
                if arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 120) then
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3028, TARGET_ENE_0, 0, 0, 0, 0, 0)
                elseif arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3003, TARGET_ENE_0, 0, 0, 0, 0, 0)
                elseif arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 180) then
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3027, TARGET_ENE_0, 0, 0, 0, 0, 0)
                end
                return true
            end
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 5029) then
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_RF, 240, -1, 9 + arg1:GetMapHitRadius(TARGET_SELF)) then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3019, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            end
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 5033) and arg1:GetTimer(3) <= 0 then
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_RF, 240, -1, 999 + arg1:GetMapHitRadius(TARGET_SELF)) and 3 < local3 then
                arg1:SetTimer(3, 15)
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3004, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            end
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 5030) then
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, -1, 9 + arg1:GetMapHitRadius(TARGET_SELF)) and -0.5 < local3 then
                if local4 < 10 then
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3017, TARGET_ENE_0, 0, 0, 0, 0, 0)
                    return true
                else
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3024, TARGET_ENE_0, 0, 0, 0, 0, 0)
                    return true
                end
            end
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 5031) then
            if arg1:GetHpRate(TARGET_SELF) <= 0.7 and arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 50 + arg1:GetMapHitRadius(TARGET_SELF)) and 5 < local3 then
                arg1:SetTimer(2, 30)
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3007, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 120, -1, 11 + arg1:GetMapHitRadius(TARGET_SELF)) and 5 < local3 then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3029, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            end
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 5032) then
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, -1, 1 + arg1:GetMapHitRadius(TARGET_SELF)) and arg1:GetTimer(2) <= 0 and arg1:GetHpRate(TARGET_SELF) <= 0.7 then
                arg1:SetTimer(2, 30)
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3005, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, -1, 40 + arg1:GetMapHitRadius(TARGET_SELF)) and 1 < local3 and arg1:GetTimer(1) <= 0 then
                arg1:SetTimer(1, 20)
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3020, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            end
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 15255) then
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, -1, 9 + arg1:GetMapHitRadius(TARGET_SELF)) then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 20010, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, -1, 13.3 + arg1:GetMapHitRadius(TARGET_SELF)) and local4 < 50 then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 20010, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            end
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 15256) then
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, -1, 9 + arg1:GetMapHitRadius(TARGET_SELF)) then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 20011, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, -1, 13.3 + arg1:GetMapHitRadius(TARGET_SELF)) and local4 < 50 then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 20011, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            end
        elseif arg1:HasSpecialEffectId(TARGET_SELF, 15258) then
            if arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 60, -1, 8 + arg1:GetMapHitRadius(TARGET_SELF)) then
                if 70 >= local4 then
                    arg2:ClearSubGoal()
                    arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, 0, 0, 0, 0, 0)
                end
                return true
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_R, 180, -1, 8 + arg1:GetMapHitRadius(TARGET_SELF)) then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3003, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            elseif arg1:IsInsideTargetCustom(TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_L, 180, -1, 8 + arg1:GetMapHitRadius(TARGET_SELF)) then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3027, TARGET_ENE_0, 0, 0, 0, 0, 0)
                return true
            end
        end
    end
    return false
end

RegisterTableGoal(GOAL_BlackSwordMariques211010_AfterAttackAct, "BlackSwordMariques211010_AfterAttackAct")
REGISTER_GOAL_NO_SUB_GOAL(GOAL_BlackSwordMariques211010_AfterAttackAct, true)
Goal.Update = function (arg0, arg1, arg2)
    return Update_Default_NoSubGoal(arg0, arg1, arg2)
end

return 
