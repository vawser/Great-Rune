// ==EMEVD==
// @docs    er-common.emedf.json
// @compress    DCX_KRAK
// @game    Sekiro
// @string    
// @linked    []
// @version    3.3.2
// ==/EMEVD==

$Event(90005200, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4) {
    EndIf(SpecialStandbyEndedFlag(X0_4));
    if (X20_4 != 0) {
        DisableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, false);
    }
    ForceAnimationPlayback(X0_4, X4_4, true, false, false);
    chrSp = (CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
        || CharacterType(10000, TargetType.Alive)
        || CharacterType(10000, TargetType.BluePhantom)
        || CharacterType(10000, TargetType.WhitePhantom);
    areaChrSp &= InArea(10000, X12_4)
        && CharacterBackreadStatus(X0_4)
        && (CharacterHasSpEffect(X0_4, 5080) || CharacterHasSpEffect(X0_4, 5450));
    if (!(X24_4 == 0 && X28_4 == 0 && X32_4 == 0)) {
        if (X24_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.Combat);
        }
        if (X28_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.ActiveAlert);
        }
        if (X32_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.PassiveAlert);
        }
        areaChrSp &= chr;
    }
L9:
    sp = CharacterHasSpEffect(X0_4, 481)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90110)
        && !CharacterHasSpEffect(X0_4, 90160);
    sp2 = CharacterHasSpEffect(X0_4, 482)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90120)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp3 = CharacterHasSpEffect(X0_4, 483)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90140)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90161);
    sp4 = CharacterHasSpEffect(X0_4, 484)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90130)
        && !CharacterHasSpEffect(X0_4, 90161)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp5 = CharacterHasSpEffect(X0_4, 487)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90150)
        && !CharacterHasSpEffect(X0_4, 90160);
    areaChrSp &= chrSp;
    WaitFor(
        areaChrSp
            || HasDamageType(X0_4, 0, DamageType.Unspecified)
            || CharacterHasStateInfo(X0_4, 436)
            || CharacterHasStateInfo(X0_4, 2)
            || CharacterHasStateInfo(X0_4, 5)
            || CharacterHasStateInfo(X0_4, 6)
            || CharacterHasStateInfo(X0_4, 260)
            || sp
            || sp2
            || sp3
            || sp4
            || sp5);
    WaitFixedTimeSeconds(0.1);
    SetNetworkconnectedThisEventSlot(ON);
    SetSpecialStandbyEndedFlag(X0_4, ON);
    if (!(!CharacterHasSpEffect(X0_4, 5080) && !CharacterHasSpEffect(X0_4, 5450))) {
        WaitFixedTimeSeconds(X16_4);
        if (X20_4 != 0) {
            EnableCharacterGravity(X0_4);
            SetCharacterMaphit(X0_4, true);
        }
        ForceAnimationPlayback(X0_4, X8_4, true, false, false);
        EndEvent();
    }
L0:
    if (X20_4 != 0) {
        EnableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, true);
    }
    EndEvent();
});

$Event(90005201, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4) {
    EndIf(SpecialStandbyEndedFlag(X0_4));
    if (X20_4 != 0) {
        DisableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, false);
    }
    ForceAnimationPlayback(X0_4, X4_4, true, false, false);
    chrSp = (CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
        || CharacterType(10000, TargetType.Alive)
        || CharacterType(10000, TargetType.BluePhantom)
        || CharacterType(10000, TargetType.WhitePhantom);
    areaChrSp &= EntityInRadiusOfEntity(10000, X0_4, X12_4, 1)
        && CharacterBackreadStatus(X0_4)
        && (CharacterHasSpEffect(X0_4, 5080) || CharacterHasSpEffect(X0_4, 5450));
    if (!(X24_4 == 0 && X28_4 == 0 && X32_4 == 0)) {
        if (X24_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.Combat);
        }
        if (X28_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.ActiveAlert);
        }
        if (X32_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.PassiveAlert);
        }
        areaChrSp &= chr;
    }
L9:
    sp = CharacterHasSpEffect(X0_4, 481)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90110)
        && !CharacterHasSpEffect(X0_4, 90160);
    sp2 = CharacterHasSpEffect(X0_4, 482)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90120)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp3 = CharacterHasSpEffect(X0_4, 483)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90140)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90161);
    sp4 = CharacterHasSpEffect(X0_4, 484)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90130)
        && !CharacterHasSpEffect(X0_4, 90161)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp5 = CharacterHasSpEffect(X0_4, 487)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90150)
        && !CharacterHasSpEffect(X0_4, 90160);
    areaChrSp &= chrSp;
    WaitFor(
        areaChrSp
            || HasDamageType(X0_4, 0, DamageType.Unspecified)
            || CharacterHasStateInfo(X0_4, 436)
            || CharacterHasStateInfo(X0_4, 2)
            || CharacterHasStateInfo(X0_4, 5)
            || CharacterHasStateInfo(X0_4, 6)
            || CharacterHasStateInfo(X0_4, 260)
            || sp
            || sp2
            || sp3
            || sp4
            || sp5);
    WaitFixedTimeSeconds(0.1);
    SetNetworkconnectedThisEventSlot(ON);
    SetSpecialStandbyEndedFlag(X0_4, ON);
    if (!(!CharacterHasSpEffect(X0_4, 5080) && !CharacterHasSpEffect(X0_4, 5450))) {
        WaitFixedTimeSeconds(X16_4);
        if (X20_4 != 0) {
            EnableCharacterGravity(X0_4);
            SetCharacterMaphit(X0_4, true);
        }
        ForceAnimationPlayback(X0_4, X8_4, true, false, false);
        EndEvent();
    }
L0:
    if (X20_4 != 0) {
        EnableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, true);
    }
    EndEvent();
});

$Event(90005210, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4) {
    EndIf(SpecialStandbyEndedFlag(X0_4));
    if (X24_4 != 0) {
        DisableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, false);
    }
    ForceAnimationPlayback(X0_4, X4_4, true, false, false);
    chrSp = (CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
        || CharacterType(10000, TargetType.Alive)
        || CharacterType(10000, TargetType.BluePhantom)
        || CharacterType(10000, TargetType.WhitePhantom);
    areaChrSp &= (InArea(10000, X12_4) && EntityInRadiusOfEntity(10000, X0_4, X16_4, 1))
        && CharacterBackreadStatus(X0_4)
        && (CharacterHasSpEffect(X0_4, 5080) || CharacterHasSpEffect(X0_4, 5450));
    if (!(X28_4 == 0 && X32_4 == 0 && X36_4 == 0)) {
        if (X28_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.Combat);
        }
        if (X32_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.ActiveAlert);
        }
        if (X36_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.PassiveAlert);
        }
        areaChrSp &= chr;
    }
L9:
    sp = CharacterHasSpEffect(X0_4, 481)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90110)
        && !CharacterHasSpEffect(X0_4, 90160);
    sp2 = CharacterHasSpEffect(X0_4, 482)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90120)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp3 = CharacterHasSpEffect(X0_4, 483)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90140)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90161);
    sp4 = CharacterHasSpEffect(X0_4, 484)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90130)
        && !CharacterHasSpEffect(X0_4, 90161)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp5 = CharacterHasSpEffect(X0_4, 487)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90150)
        && !CharacterHasSpEffect(X0_4, 90160);
    areaChrSp &= chrSp;
    WaitFor(
        areaChrSp
            || HasDamageType(X0_4, 0, DamageType.Unspecified)
            || CharacterHasStateInfo(X0_4, 436)
            || CharacterHasStateInfo(X0_4, 2)
            || CharacterHasStateInfo(X0_4, 5)
            || CharacterHasStateInfo(X0_4, 6)
            || CharacterHasStateInfo(X0_4, 260)
            || sp
            || sp2
            || sp3
            || sp4
            || sp5);
    WaitFixedTimeSeconds(0.1);
    SetNetworkconnectedThisEventSlot(ON);
    SetSpecialStandbyEndedFlag(X0_4, ON);
    if (!(!CharacterHasSpEffect(X0_4, 5080) && !CharacterHasSpEffect(X0_4, 5450))) {
        WaitFixedTimeSeconds(X20_4);
        if (X24_4 != 0) {
            EnableCharacterGravity(X0_4);
            SetCharacterMaphit(X0_4, true);
        }
        ForceAnimationPlayback(X0_4, X8_4, true, false, false);
        EndEvent();
    }
L0:
    if (X24_4 != 0) {
        EnableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, true);
    }
    EndEvent();
});

$Event(90005211, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4) {
    EndIf(SpecialStandbyEndedFlag(X0_4));
    if (X24_4 != 0) {
        DisableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, false);
    }
    ForceAnimationPlayback(X0_4, X4_4, true, false, false);
    chrSp = (CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
        || CharacterType(10000, TargetType.Alive)
        || CharacterType(10000, TargetType.BluePhantom)
        || CharacterType(10000, TargetType.WhitePhantom);
    if (0 != X12_4) {
        area |= InArea(10000, X12_4);
    }
    area |= EntityInRadiusOfEntity(10000, X0_4, X16_4, 1);
    areaChrSp &= area
        && CharacterBackreadStatus(X0_4)
        && (CharacterHasSpEffect(X0_4, 5080) || CharacterHasSpEffect(X0_4, 5450));
    if (!(X28_4 == 0 && X32_4 == 0 && X36_4 == 0)) {
        if (X28_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.Combat);
        }
        if (X32_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.ActiveAlert);
        }
        if (X36_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.PassiveAlert);
        }
        areaChrSp &= chr;
    }
L9:
    sp = CharacterHasSpEffect(X0_4, 481)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90110)
        && !CharacterHasSpEffect(X0_4, 90160);
    sp2 = CharacterHasSpEffect(X0_4, 482)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90120)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp3 = CharacterHasSpEffect(X0_4, 483)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90140)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90161);
    sp4 = CharacterHasSpEffect(X0_4, 484)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90130)
        && !CharacterHasSpEffect(X0_4, 90161)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp5 = CharacterHasSpEffect(X0_4, 487)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90150)
        && !CharacterHasSpEffect(X0_4, 90160);
    areaChrSp &= chrSp;
    WaitFor(
        areaChrSp
            || HasDamageType(X0_4, 0, DamageType.Unspecified)
            || CharacterHasStateInfo(X0_4, 436)
            || CharacterHasStateInfo(X0_4, 2)
            || CharacterHasStateInfo(X0_4, 5)
            || CharacterHasStateInfo(X0_4, 6)
            || CharacterHasStateInfo(X0_4, 260)
            || sp
            || sp2
            || sp3
            || sp4
            || sp5);
    WaitFixedTimeSeconds(0.1);
    SetNetworkconnectedThisEventSlot(ON);
    SetSpecialStandbyEndedFlag(X0_4, ON);
    if (!(!CharacterHasSpEffect(X0_4, 5080) && !CharacterHasSpEffect(X0_4, 5450))) {
        WaitFixedTimeSeconds(X20_4);
        if (X24_4 != 0) {
            EnableCharacterGravity(X0_4);
            SetCharacterMaphit(X0_4, true);
        }
        ForceAnimationPlayback(X0_4, X8_4, true, false, false);
        EndEvent();
    }
L0:
    if (X24_4 != 0) {
        EnableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, true);
    }
    EndEvent();
});

$Event(90005213, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4, X40_4, X44_4) {
    EndIf(SpecialStandbyEndedFlag(X0_4));
    if (X24_4 != 0) {
        DisableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, false);
    }
    ForceAnimationPlayback(X0_4, X4_4, true, false, false);
    chrSp = (CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
        || CharacterType(10000, TargetType.Alive)
        || CharacterType(10000, TargetType.BluePhantom)
        || CharacterType(10000, TargetType.WhitePhantom);
    if (0 != X12_4) {
        area |= InArea(10000, X12_4);
    }
    cond = SpecialStandbyEndedFlag(X40_4);
    area |= EntityInRadiusOfEntity(10000, X0_4, X16_4, 1) || cond;
    areaChrSp &= area
        && CharacterBackreadStatus(X0_4)
        && (CharacterHasSpEffect(X0_4, 5080) || CharacterHasSpEffect(X0_4, 5450));
    if (!(X28_4 == 0 && X32_4 == 0 && X36_4 == 0)) {
        if (X28_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.Combat);
        }
        if (X32_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.ActiveAlert);
        }
        if (X36_4 != 0) {
            chr |= CharacterAIState(X0_4, AIStateType.PassiveAlert);
        }
        areaChrSp &= chr;
    }
L9:
    sp = CharacterHasSpEffect(X0_4, 481)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90110)
        && !CharacterHasSpEffect(X0_4, 90160);
    sp2 = CharacterHasSpEffect(X0_4, 482)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90120)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp3 = CharacterHasSpEffect(X0_4, 483)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90140)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90161);
    sp4 = CharacterHasSpEffect(X0_4, 484)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90130)
        && !CharacterHasSpEffect(X0_4, 90161)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp5 = CharacterHasSpEffect(X0_4, 487)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90150)
        && !CharacterHasSpEffect(X0_4, 90160);
    areaChrSp &= chrSp;
    WaitFor(
        areaChrSp
            || HasDamageType(X0_4, 0, DamageType.Unspecified)
            || CharacterHasStateInfo(X0_4, 436)
            || CharacterHasStateInfo(X0_4, 2)
            || CharacterHasStateInfo(X0_4, 5)
            || CharacterHasStateInfo(X0_4, 6)
            || CharacterHasStateInfo(X0_4, 260)
            || sp
            || sp2
            || sp3
            || sp4
            || sp5);
    WaitFixedTimeSeconds(0.1);
    SetNetworkconnectedThisEventSlot(ON);
    SetSpecialStandbyEndedFlag(X0_4, ON);
    if (!(!CharacterHasSpEffect(X0_4, 5080) && !CharacterHasSpEffect(X0_4, 5450))) {
        if (!cond.Passed) {
            WaitFixedTimeSeconds(X20_4);
        } else {
            WaitFixedTimeSeconds(X44_4);
        }
        if (X24_4 != 0) {
            EnableCharacterGravity(X0_4);
            SetCharacterMaphit(X0_4, true);
        }
        ForceAnimationPlayback(X0_4, X8_4, true, false, false);
        EndEvent();
    }
L0:
    if (X24_4 != 0) {
        EnableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, true);
    }
    EndEvent();
});

$Event(90005220, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    EndIf(SpecialStandbyEndedFlag(X0_4));
    if (X16_4 != 0) {
        DisableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, false);
    }
    ForceAnimationPlayback(X0_4, X4_4, true, false, false);
    chrSp &= CharacterBackreadStatus(X0_4)
        && (CharacterHasSpEffect(X0_4, 5080) || CharacterHasSpEffect(X0_4, 5450));
    chr |= CharacterAIState(X0_4, AIStateType.Combat);
    if (X20_4 != 0) {
        chr |= CharacterAIState(X0_4, AIStateType.ActiveAlert);
    }
    if (X24_4 != 0) {
        chr |= CharacterAIState(X0_4, AIStateType.PassiveAlert);
    }
L9:
    sp = CharacterHasSpEffect(X0_4, 481)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90110)
        && !CharacterHasSpEffect(X0_4, 90160);
    sp2 = CharacterHasSpEffect(X0_4, 482)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90120)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp3 = CharacterHasSpEffect(X0_4, 483)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90140)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90161);
    sp4 = CharacterHasSpEffect(X0_4, 484)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90130)
        && !CharacterHasSpEffect(X0_4, 90161)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp5 = CharacterHasSpEffect(X0_4, 487)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90150)
        && !CharacterHasSpEffect(X0_4, 90160);
    chrSp &= chr && cond;
    WaitFor(
        chrSp
            || HasDamageType(X0_4, 0, DamageType.Unspecified)
            || CharacterHasStateInfo(X0_4, 436)
            || CharacterHasStateInfo(X0_4, 2)
            || CharacterHasStateInfo(X0_4, 5)
            || CharacterHasStateInfo(X0_4, 6)
            || CharacterHasStateInfo(X0_4, 260)
            || sp
            || sp2
            || sp3
            || sp4
            || sp5);
    WaitFixedTimeSeconds(0.1);
    SetNetworkconnectedThisEventSlot(ON);
    SetSpecialStandbyEndedFlag(X0_4, ON);
    if (!(!CharacterHasSpEffect(X0_4, 5080) && !CharacterHasSpEffect(X0_4, 5450))) {
        WaitFixedTimeSeconds(X12_4);
        if (X16_4 != 0) {
            EnableCharacterGravity(X0_4);
            SetCharacterMaphit(X0_4, true);
        }
        ForceAnimationPlayback(X0_4, X8_4, true, false, false);
        EndEvent();
    }
L0:
    if (X16_4 != 0) {
        EnableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, true);
    }
    EndEvent();
});

$Event(90005221, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    EndIf(SpecialStandbyEndedFlag(X0_4));
    if (X16_4 != 0) {
        DisableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, false);
    }
    ForceAnimationPlayback(X0_4, X4_4, true, false, false);
    WaitFor(
        HasDamageType(X0_4, 0, DamageType.Unspecified)
            || CharacterHasStateInfo(X0_4, 436)
            || CharacterHasStateInfo(X0_4, 2)
            || CharacterHasStateInfo(X0_4, 5)
            || CharacterHasStateInfo(X0_4, 6)
            || CharacterHasStateInfo(X0_4, 260)
            || (CharacterHasSpEffect(X0_4, 481)
                && !CharacterHasSpEffect(X0_4, 90100)
                && !CharacterHasSpEffect(X0_4, 90110)
                && !CharacterHasSpEffect(X0_4, 90160))
            || (CharacterHasSpEffect(X0_4, 482)
                && !CharacterHasSpEffect(X0_4, 90100)
                && !CharacterHasSpEffect(X0_4, 90120)
                && !CharacterHasSpEffect(X0_4, 90160)
                && !CharacterHasSpEffect(X0_4, 90162))
            || (CharacterHasSpEffect(X0_4, 483)
                && !CharacterHasSpEffect(X0_4, 90100)
                && !CharacterHasSpEffect(X0_4, 90140)
                && !CharacterHasSpEffect(X0_4, 90160)
                && !CharacterHasSpEffect(X0_4, 90161))
            || (CharacterHasSpEffect(X0_4, 484)
                && !CharacterHasSpEffect(X0_4, 90100)
                && !CharacterHasSpEffect(X0_4, 90130)
                && !CharacterHasSpEffect(X0_4, 90161)
                && !CharacterHasSpEffect(X0_4, 90162))
            || (CharacterHasSpEffect(X0_4, 487)
                && !CharacterHasSpEffect(X0_4, 90100)
                && !CharacterHasSpEffect(X0_4, 90150)
                && !CharacterHasSpEffect(X0_4, 90160)));
    WaitFixedTimeSeconds(0.1);
    if (!(!CharacterHasSpEffect(X0_4, 5080) && !CharacterHasSpEffect(X0_4, 5450))) {
        SetNetworkconnectedThisEventSlot(ON);
        SetSpecialStandbyEndedFlag(X0_4, ON);
        WaitFixedTimeSeconds(X12_4);
        if (X16_4 != 0) {
            EnableCharacterGravity(X0_4);
            SetCharacterMaphit(X0_4, true);
        }
        ForceAnimationPlayback(X0_4, X8_4, true, false, false);
        EndEvent();
    }
L0:
    if (X16_4 != 0) {
        EnableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, true);
    }
    EndEvent();
});

$Event(90005250, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    EndIf(ThisEventSlot());
    DisableCharacterAI(X0_4);
    chrSp = (CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
        || CharacterType(10000, TargetType.Alive)
        || CharacterType(10000, TargetType.BluePhantom)
        || CharacterType(10000, TargetType.WhitePhantom);
    sp = CharacterHasSpEffect(X0_4, 481)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90110)
        && !CharacterHasSpEffect(X0_4, 90160);
    sp2 = CharacterHasSpEffect(X0_4, 482)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90120)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp3 = CharacterHasSpEffect(X0_4, 483)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90140)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90161);
    sp4 = CharacterHasSpEffect(X0_4, 484)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90130)
        && !CharacterHasSpEffect(X0_4, 90161)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp5 = CharacterHasSpEffect(X0_4, 487)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90150)
        && !CharacterHasSpEffect(X0_4, 90160);
    areaChrSp = InArea(10000, X4_4) && chrSp;
    WaitFor(
        HasDamageType(X0_4, 0, DamageType.Unspecified)
            || CharacterHasStateInfo(X0_4, 436)
            || CharacterHasStateInfo(X0_4, 2)
            || CharacterHasStateInfo(X0_4, 5)
            || CharacterHasStateInfo(X0_4, 6)
            || CharacterHasStateInfo(X0_4, 260)
            || areaChrSp
            || sp
            || sp2
            || sp3
            || sp4
            || sp5);
    SetNetworkconnectedThisEventSlot(ON);
    if (areaChrSp.Passed) {
        WaitFixedTimeSeconds(X8_4);
        if (Signed(X12_4) != -1) {
            ForceAnimationPlayback(X0_4, X12_4, true, false, false);
        }
    }
L1:
    EnableCharacterAI(X0_4);
});

$Event(90005251, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    EndIf(ThisEventSlot());
    DisableCharacterAI(X0_4);
    chrSp = (CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
        || CharacterType(10000, TargetType.Alive)
        || CharacterType(10000, TargetType.BluePhantom)
        || CharacterType(10000, TargetType.WhitePhantom);
    sp = CharacterHasSpEffect(X0_4, 481)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90110)
        && !CharacterHasSpEffect(X0_4, 90160);
    sp2 = CharacterHasSpEffect(X0_4, 482)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90120)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp3 = CharacterHasSpEffect(X0_4, 483)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90140)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90161);
    sp4 = CharacterHasSpEffect(X0_4, 484)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90130)
        && !CharacterHasSpEffect(X0_4, 90161)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp5 = CharacterHasSpEffect(X0_4, 487)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90150)
        && !CharacterHasSpEffect(X0_4, 90160);
    areaChrSp = EntityInRadiusOfEntity(10000, X0_4, X4_4, 1) && chrSp;
    WaitFor(
        HasDamageType(X0_4, 0, DamageType.Unspecified)
            || CharacterHasStateInfo(X0_4, 436)
            || CharacterHasStateInfo(X0_4, 2)
            || CharacterHasStateInfo(X0_4, 5)
            || CharacterHasStateInfo(X0_4, 6)
            || CharacterHasStateInfo(X0_4, 260)
            || areaChrSp
            || sp
            || sp2
            || sp3
            || sp4
            || sp5);
    SetNetworkconnectedThisEventSlot(ON);
    if (areaChrSp.Passed) {
        WaitFixedTimeSeconds(X8_4);
        if (Signed(X12_4) != -1) {
            ForceAnimationPlayback(X0_4, X12_4, true, false, false);
        }
    }
L1:
    EnableCharacterAI(X0_4);
});

$Event(90005260, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    EndIf(ThisEventSlot());
    DisableCharacterAI(X0_4);
    chrSp = (CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
        || CharacterType(10000, TargetType.Alive)
        || CharacterType(10000, TargetType.BluePhantom)
        || CharacterType(10000, TargetType.WhitePhantom);
    area = InArea(10000, X4_4) && EntityInRadiusOfEntity(10000, X0_4, X8_4, 1);
    sp = CharacterHasSpEffect(X0_4, 481)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90110)
        && !CharacterHasSpEffect(X0_4, 90160);
    sp2 = CharacterHasSpEffect(X0_4, 482)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90120)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp3 = CharacterHasSpEffect(X0_4, 483)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90140)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90161);
    sp4 = CharacterHasSpEffect(X0_4, 484)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90130)
        && !CharacterHasSpEffect(X0_4, 90161)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp5 = CharacterHasSpEffect(X0_4, 487)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90150)
        && !CharacterHasSpEffect(X0_4, 90160);
    areaChrSp = area && chrSp;
    WaitFor(
        HasDamageType(X0_4, 0, DamageType.Unspecified)
            || CharacterHasStateInfo(X0_4, 436)
            || CharacterHasStateInfo(X0_4, 2)
            || CharacterHasStateInfo(X0_4, 5)
            || CharacterHasStateInfo(X0_4, 6)
            || CharacterHasStateInfo(X0_4, 260)
            || areaChrSp
            || sp
            || sp2
            || sp3
            || sp4
            || sp5);
    SetNetworkconnectedThisEventSlot(ON);
    if (areaChrSp.Passed) {
        WaitFixedTimeSeconds(X12_4);
        if (Signed(X16_4) != -1) {
            ForceAnimationPlayback(X0_4, X16_4, true, false, false);
        }
    }
L1:
    EnableCharacterAI(X0_4);
});

$Event(90005261, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    EndIf(ThisEventSlot());
    DisableCharacterAI(X0_4);
    chrSp = (CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
        || CharacterType(10000, TargetType.Alive)
        || CharacterType(10000, TargetType.BluePhantom)
        || CharacterType(10000, TargetType.WhitePhantom);
    sp = CharacterHasSpEffect(X0_4, 481)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90110)
        && !CharacterHasSpEffect(X0_4, 90160);
    sp2 = CharacterHasSpEffect(X0_4, 482)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90120)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp3 = CharacterHasSpEffect(X0_4, 483)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90140)
        && !CharacterHasSpEffect(X0_4, 90160)
        && !CharacterHasSpEffect(X0_4, 90161);
    sp4 = CharacterHasSpEffect(X0_4, 484)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90130)
        && !CharacterHasSpEffect(X0_4, 90161)
        && !CharacterHasSpEffect(X0_4, 90162);
    sp5 = CharacterHasSpEffect(X0_4, 487)
        && !CharacterHasSpEffect(X0_4, 90100)
        && !CharacterHasSpEffect(X0_4, 90150)
        && !CharacterHasSpEffect(X0_4, 90160);
    area = InArea(10000, X4_4) || EntityInRadiusOfEntity(10000, X0_4, X8_4, 1);
    areaChrSp = area && chrSp;
    WaitFor(
        HasDamageType(X0_4, 0, DamageType.Unspecified)
            || CharacterHasStateInfo(X0_4, 436)
            || CharacterHasStateInfo(X0_4, 2)
            || CharacterHasStateInfo(X0_4, 5)
            || CharacterHasStateInfo(X0_4, 6)
            || CharacterHasStateInfo(X0_4, 260)
            || areaChrSp
            || sp
            || sp2
            || sp3
            || sp4
            || sp5);
    SetNetworkconnectedThisEventSlot(ON);
    if (areaChrSp.Passed) {
        WaitFixedTimeSeconds(X12_4);
        if (Signed(X16_4) != -1) {
            ForceAnimationPlayback(X0_4, X16_4, true, false, false);
        }
    }
L1:
    EnableCharacterAI(X0_4);
});

$Event(90005271, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(ThisEventSlot());
    DisableCharacterAI(X0_4);
    WaitFor(
        HasDamageType(X0_4, 0, DamageType.Unspecified)
            || CharacterHasStateInfo(X0_4, 436)
            || CharacterHasStateInfo(X0_4, 2)
            || CharacterHasStateInfo(X0_4, 5)
            || CharacterHasStateInfo(X0_4, 6)
            || CharacterHasStateInfo(X0_4, 260)
            || (CharacterHasSpEffect(X0_4, 481)
                && !CharacterHasSpEffect(X0_4, 90100)
                && !CharacterHasSpEffect(X0_4, 90110)
                && !CharacterHasSpEffect(X0_4, 90160))
            || (CharacterHasSpEffect(X0_4, 482)
                && !CharacterHasSpEffect(X0_4, 90100)
                && !CharacterHasSpEffect(X0_4, 90120)
                && !CharacterHasSpEffect(X0_4, 90160)
                && !CharacterHasSpEffect(X0_4, 90162))
            || (CharacterHasSpEffect(X0_4, 483)
                && !CharacterHasSpEffect(X0_4, 90100)
                && !CharacterHasSpEffect(X0_4, 90140)
                && !CharacterHasSpEffect(X0_4, 90160)
                && !CharacterHasSpEffect(X0_4, 90161))
            || (CharacterHasSpEffect(X0_4, 484)
                && !CharacterHasSpEffect(X0_4, 90100)
                && !CharacterHasSpEffect(X0_4, 90130)
                && !CharacterHasSpEffect(X0_4, 90161)
                && !CharacterHasSpEffect(X0_4, 90162))
            || (CharacterHasSpEffect(X0_4, 487)
                && !CharacterHasSpEffect(X0_4, 90100)
                && !CharacterHasSpEffect(X0_4, 90150)
                && !CharacterHasSpEffect(X0_4, 90160)));
    SetNetworkconnectedThisEventSlot(ON);
    if (and1.Passed) {
        WaitFixedTimeSeconds(X4_4);
        if (Signed(X8_4) != -1) {
            ForceAnimationPlayback(X0_4, X8_4, true, false, false);
        }
    }
L1:
    EnableCharacterAI(X0_4);
});

$Event(90005300, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    if (EventFlag(X0_4)) {
        if (Signed(X16_4) != 0) {
            DisableCharacter(X4_4);
            ForceCharacterTreasure(X4_4);
            EndEvent();
        }
        DisableCharacter(X4_4);
        DisableCharacterCollision(X4_4);
        ForceCharacterDeath(X4_4, false);
        EndEvent();
    }
L0:
    WaitFor(CharacterRatioDead(X4_4));
    WaitFixedTimeSeconds(X12_4);
    SetEventFlagID(X0_4, ON);
    EndIf(!PlayerIsInOwnWorld());
    EndIf(Signed(X16_4) == 1);
    EndIf(Signed(X8_4) == 0);
    AwardItemsIncludingClients(X8_4);
    EndEvent();
});

$Event(90005360, Restart, function(X0_4, X4_4, X8_4) {
    if (EventFlag(X0_4)) {
        DisableCharacter(X4_4);
        DisableCharacterCollision(X4_4);
        EndEvent();
    }
L0:
    WaitFor(EventFlag(X0_4));
    DisplayBanner(TextBannerType.Unknown14);
    EndIf(!PlayerIsInOwnWorld());
    AwardItemsIncludingClients(X8_4);
});

$Event(90005390, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4) {
    EndIf(EventFlag(X0_4));
    WaitFor(EventFlag(X4_4) && CharacterDead(X12_4));
    WaitFixedTimeSeconds(1);
    if (Signed(X16_4) != 0) {
        SpawnOneshotSFX(TargetEntityType.Character, X8_4, 960, 601111);
    } else {
L2:
        SpawnOneshotSFX(TargetEntityType.Character, X8_4, 960, 601110);
    }
L3:
    WaitFixedTimeSeconds(3);
    DisableCharacter(X12_4);
    EndIf(!PlayerIsInOwnWorld());
    if (Signed(X20_4) != 0) {
        AwardItemsIncludingClients(X20_4);
    }
    SetNetworkconnectedEventFlagID(X0_4, ON);
});

$Event(90005391, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    if (EventFlag(X0_4)) {
        DisableCharacter(X8_4);
        DisableCharacterCollision(X8_4);
        DisableCharacter(X12_4);
        DisableCharacterCollision(X12_4);
        EndEvent();
    }
L0:
    if (EventFlag(X4_4)) {
        DisableCharacter(X8_4);
        DisableCharacterCollision(X8_4);
        EndEvent();
    }
L1:
    DisableCharacter(X12_4);
    DisableCharacterCollision(X12_4);
    DisableCharacterGravity(X12_4);
    DisableCharacterAI(X12_4);
    EnableCharacterFadeOnEnable(X12_4);
    WaitFor(CharacterDead(X8_4));
    EnableCharacterDefaultBackread(X8_4);
    EnableCharacterDefaultBackread(X12_4);
    WaitFixedTimeSeconds(0.5);
    WarpCharacterAndCopyFloor(X12_4, TargetEntityType.Character, X8_4, 900, X8_4);
    WaitFixedTimeSeconds(0.5);
    if (Signed(X16_4) != 0) {
        SpawnOneshotSFX(TargetEntityType.Character, X8_4, 900, 601101);
    } else {
L2:
        SpawnOneshotSFX(TargetEntityType.Character, X8_4, 900, 601100);
    }
L3:
    EnableCharacter(X12_4);
    EnableCharacterGravity(X12_4);
    EnableCharacterCollision(X12_4);
    EnableCharacterAI(X12_4);
    DisableCharacter(X8_4);
    DisableCharacterDefaultBackread(X8_4);
    DisableCharacterDefaultBackread(X12_4);
    if (PlayerIsInOwnWorld()) {
        SetNetworkconnectedEventFlagID(X4_4, ON);
    }
});

$Event(90005400, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    EndIf(ThisEventSlot());
    if (X16_4 != 0) {
        DisableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, false);
    }
    if (Signed(X4_4) != 0) {
        SetSpEffect(X0_4, X4_4);
    } else {
        SetSpEffect(X0_4, 4421);
    }
    ForceAnimationPlayback(X0_4, 14100, true, false, false);
    WaitFor(HasDamageType(X0_4, 0, DamageType.Unspecified) || CharacterHasSpEffect(X0_4, 5112));
    WaitFixedTimeFrames(1);
    if (CharacterHasSpEffect(X0_4, 5111)) {
        SetNetworkconnectedThisEventSlot(ON);
        if (!CharacterHasSpEffect(X0_4, 5112)) {
            WaitFixedTimeSeconds(X12_4);
        } else {
            WaitFixedTimeSeconds(X8_4);
        }
        if (X16_4 != 0) {
            EnableCharacterGravity(X0_4);
            SetCharacterMaphit(X0_4, true);
        }
        ForceAnimationPlayback(X0_4, 14102, true, false, false);
        EndEvent();
    }
L0:
    if (X16_4 != 0) {
        EnableCharacterGravity(X0_4);
        SetCharacterMaphit(X0_4, true);
    }
    EndEvent();
});

$Event(90005401, Restart, function(X0_4, X4_4) {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(X0_4));
    SetSpEffect(X4_4, 4430);
    WaitFor(PlayerIsInOwnWorld() && CharacterHasSpEffect(X4_4, 4431));
    SetEventFlagID(X0_4, ON);
});

$Event(90005410, Restart, function(X0_4, X4_4, X8_4) {
    if (!EventFlag(X0_4)) {
        WaitFor((PlayerIsInOwnWorld() && CharacterHasSpEffect(X4_4, 9500)) || EventFlag(X0_4));
        if (PlayerIsInOwnWorld()) {
            SetNetworkconnectedEventFlagID(X0_4, ON);
        }
    }
L0:
    Unknown200471(0, 0, X8_4);
    WaitFor((PlayerIsInOwnWorld() && CharacterHasSpEffect(20000, 202)) || !EventFlag(X0_4));
    if (PlayerIsInOwnWorld()) {
        SetNetworkconnectedEventFlagID(X0_4, OFF);
    }
    RestartEvent();
});

$Event(90005411, Restart, function(X0_4, X4_4, X8_4) {
    DisableNetworkSync();
    EndIf(!PlayerIsInOwnWorld());
    if (X8_4 == 0) {
        WaitFixedTimeFrames(1);
    }
    CreateAssetfollowingSFX(X0_4, 200, 620);
    WaitFor(CharacterHasSpEffect(X4_4, 9502));
    DeleteAssetfollowingSFX(X0_4, true);
    WaitFor(CharacterHasSpEffect(X4_4, 9503));
    RestartEvent();
});

$Event(90005420, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    DisableCharacterCollision(X0_4);
    AttachCaravanToController(X4_4, X0_4);
    AttachAssetToAsset(X8_4, X4_4, 151);
    SetNetworkUpdateRate(X0_4, true, CharacterUpdateFrequency.AtLeastEvery2Frames);
    SetNetworkUpdateRate(X12_4, true, CharacterUpdateFrequency.AtLeastEvery5Frames);
    SetNetworkUpdateRate(X16_4, true, CharacterUpdateFrequency.AlwaysUpdate);
    SetNetworkUpdateRate(X20_4, true, CharacterUpdateFrequency.AlwaysUpdate);
    ConnectCharacterToCaravan(X16_4, X4_4);
    ConnectCharacterToCaravan(X20_4, X4_4);
    EndEvent();
    WaitFixedTimeSeconds(X24_4);
});

$Event(90005421, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(X8_4));
    DisableObjAct(X4_4, -1);
    WaitFor(CharacterHasSpEffect(X0_4, 11500) && !EventFlag(X0_4));
    EnableObjAct(X4_4, -1);
    WaitFor(!CharacterHasSpEffect(X0_4, 11500));
    RestartEvent();
});

$Event(90005422, Restart, function(X0_4, X4_4, X8_4) {
    if (EventFlag(X0_4)) {
        EnableAssetTreasure(X4_4);
        EndEvent();
    }
L0:
    DisableAssetTreasure(X4_4);
    WaitFor((PlayerIsInOwnWorld() && ObjActEventFlag(X8_4)) || AssetDestroyed(X4_4, Equal, 1));
    WaitFixedTimeSeconds(3.2);
    EnableAssetTreasure(X4_4);
});

$Event(90005423, Restart, function(X0_4) {
    WaitFor(CharacterHasSpEffect(X0_4, 5551));
    ConnectCharacterToCaravan(X0_4, 0);
    ChangeCharactersCloth(X0_4, 20, 2);
});

$Event(90005424, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    WaitFor(AssetDestroyed(X0_4, Equal, 1));
    ChangeCharactersCloth(X4_4, 20, 2);
    ChangeCharactersCloth(X8_4, 20, 2);
    SetSpEffect(X4_4, 5551);
    SetSpEffect(X8_4, 5551);
    ForceCharacterDeath(X12_4, true);
    DisableAsset(X16_4);
    DisableObjAct(X16_4, -1);
    EnableAssetTreasure(X0_4);
});

$Event(90005440, Default, function(X0_4, X4_4) {
    SetSpEffect(X4_4, 14500);
    DisableCharacterHPBarDisplay(X4_4);
    DisableLockOnPoint(X0_4, 220);
    WaitFor(
        PlayerIsInOwnWorld()
            && CharacterHasSpEffect(10000, 3245)
            && EntityInRadiusOfEntity(X4_4, 10000, 6, 1));
    SetEventFlagID(X0_4, ON);
L0:
    SetSpEffect(X4_4, 14501);
    SetSpEffect(X4_4, 14502);
    EnableCharacterHPBarDisplay(X4_4);
    EnableLockOnPoint(X4_4, 220);
    WaitFor(
        (!CharacterHasSpEffect(10000, 3245) || !EntityInRadiusOfEntity(X4_4, 10000, 6, 1))
            && !CharacterHasSpEffect(X4_4, 14503)
            && PlayerIsInOwnWorld());
    RestartEvent();
    RequestCharacterAICommand(0, 0, 0);
    EzstateInstructionRequest(0, 0, 0);
});

$Event(90005450, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    EnableCharacterDefaultBackread(X0_4);
    EnableCharacterImmortality(X0_4);
    SetCharacterEnableDistance(X0_4, 2000);
    DisableCharacterDisableOnHitUnload(X0_4);
    EnableDistancebasedNetworkUpdateAuthority(X0_4);
    DisableCharacterHPBarDisplay(X0_4);
    AttachAssetToCharacter(X0_4, 100, X4_4);
    AttachAssetToCharacter(X0_4, 80, X8_4);
    AttachAssetToCharacter(X0_4, 165, X12_4);
});

$Event(90005451, Restart, function(X0_4, X4_4) {
    if (!ThisEventSlot()) {
        WaitFor(AssetRatioDestroyed(DestructionState.Destroyed, X4_4) >= 0.45);
    }
L0:
    SetSpEffect(X0_4, 12450);
});

$Event(90005452, Restart, function(X0_4, X4_4) {
    EndIf(EventFlag(X4_4));
    WaitFor(CharacterHasSpEffect(X0_4, 12455));
    SetNetworkconnectedEventFlagID(X4_4, ON);
});

$Event(90005453, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    EndIf(AssetDestroyed(X4_4, Equal, 1));
    AttachAssetToCharacter(X0_4, X8_4, X4_4);
    if (CharacterType(10000, TargetType.WhitePhantom)
        || CharacterType(10000, TargetType.GrayPhantom)
        || CharacterType(10000, TargetType.BluePhantom)
        || CharacterType(10000, TargetType.BlackPhantom)
        || CharacterType(10000, TargetType.Invader)
        || CharacterType(10000, TargetType.Invader2)
        || CharacterType(10000, TargetType.Invader3)) {
        EnableAssetInvunerability(X4_4);
    }
L10:
    WaitFor(AssetDestroyed(X0_4, Equal, 1) || CharacterHasSpEffect(X0_4, 12460));
    EndIf(AssetDestroyed(X4_4, Equal, 1));
    EnableAssetInvunerability(X4_4);
    WaitFixedTimeSeconds(X12_4);
    RequestAssetDestruction(X4_4, 0);
});

$Event(90005454, Restart, function(X0_4, X4_4, X8_4) {
    if (EventFlag(X8_4)) {
        ForceAnimationPlayback(X0_4, 30001, true, false, false);
    }
    if (!EventFlag(X4_4)) {
        SetSpEffect(X0_4, 5005);
        RequestCharacterAIReplan(X0_4);
        DisableCharacterGravity(X0_4);
        WaitFixedTimeFrames(1);
        if (EventFlag(X8_4)) {
            ForceAnimationPlayback(X0_4, 30001, true, false, false);
        } else {
            ForceAnimationPlayback(X0_4, 0, true, false, false);
        }
        WaitFor(
            EventFlag(X4_4) || (PlayerIsInOwnWorld() && EntityInRadiusOfEntity(X0_4, 10000, 200, 1)));
        SetNetworkconnectedEventFlagID(X4_4, ON);
    }
L0:
    SetSpEffect(X0_4, 5006);
    RequestCharacterAIReplan(X0_4);
    EnableCharacterGravity(X0_4);
    WaitFor(
        (PlayerIsInOwnWorld() && !EntityInRadiusOfEntity(X0_4, 10000, 220, 1)) || !EventFlag(X4_4));
    SetNetworkconnectedEventFlagID(X4_4, OFF);
    RestartEvent();
});

$Event(90005456, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    if (EventFlag(X12_4)) {
        EndEvent();
    }
L0:
    DisableObjAct(X4_4, -1);
    DisableObjAct(X8_4, -1);
    WaitFor(CharacterHasSpEffect(X0_4, 12455));
    EnableObjAct(X4_4, -1);
    EnableObjAct(X8_4, -1);
});

$Event(90005457, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    if (CharacterHasSpEffect(X0_4, 12455)) {
        DisableAsset(X4_4);
        DisableObjAct(X8_4, -1);
        ReproduceAssetAnimation(X8_4, 1);
        EndEvent();
    }
L0:
    AttachAssetToCharacter(X0_4, 100, X4_4);
    ReproduceAssetAnimation(X8_4, 1);
    DisableObjAct(X8_4, -1);
    DisableObjAct(X12_4, -1);
    WaitFor(CharacterHasSpEffect(X0_4, 12455));
    DisableAsset(X4_4);
    EnableObjAct(X12_4, -1);
});

$Event(90005458, Restart, function(X0_4, X4_4) {
    if (!ThisEventSlot()) {
        AttachAssetToCharacter(X0_4, 166, X4_4);
        DisableAsset(X4_4);
        WaitFor(CharacterHasSpEffect(X0_4, 12465));
    }
L0:
    EnableAsset(X4_4);
    SetNetworkconnectedThisEventSlot(ON);
    EndEvent();
});

$Event(90005459, Restart, function(X0_4, X4_4, X8_4) {
    DisableCharacter(X8_4);
    DisableCharacterCollision(X8_4);
    DisableCharacterGravity(X8_4);
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(PlayerIsInOwnWorld() && EventFlag(X4_4));
    EnableCharacter(X8_4);
    WarpCharacterAndCopyFloor(X8_4, TargetEntityType.Character, X0_4, 270, X0_4);
});

$Event(90005460, Restart, function(X0_4) {
    WaitFor(CharacterBackreadStatus(X0_4));
    CreateNPCPart(X0_4, 60, NPCPartType.Part6, 999999999, 1, 1, false, false);
    SetNPCPartSEAndSFX(X0_4, 60, 124, 124, -1, -1, -1);
});

$Event(90005461, Restart, function(X0_4) {
    WaitFor(CharacterBackreadStatus(X0_4) && !CharacterHasSpEffect(X0_4, 11753));
    CreateNPCPart(X0_4, 10, NPCPartType.Part1, 11, 1, 1, false, false);
    CreateNPCPart(X0_4, 20, NPCPartType.Part2, 11, 1, 1, false, false);
    cond = cond2;
    WaitFor(
        NPCPartHP(X0_4, 10) <= 0
            || NPCPartHP(X0_4, 20) <= 0
            || (NPCPartHP(X0_4, 10) <= 10 && NPCPartHP(X0_4, 20) <= 1)
            || (NPCPartHP(X0_4, 10) <= 9 && NPCPartHP(X0_4, 20) <= 2)
            || (NPCPartHP(X0_4, 10) <= 8 && NPCPartHP(X0_4, 20) <= 3)
            || (NPCPartHP(X0_4, 10) <= 7 && NPCPartHP(X0_4, 20) <= 4)
            || (NPCPartHP(X0_4, 10) <= 6 && NPCPartHP(X0_4, 20) <= 5)
            || (NPCPartHP(X0_4, 10) <= 5 && NPCPartHP(X0_4, 20) <= 6)
            || (NPCPartHP(X0_4, 10) <= 4 && NPCPartHP(X0_4, 20) <= 7)
            || (NPCPartHP(X0_4, 10) <= 3 && NPCPartHP(X0_4, 20) <= 8)
            || (NPCPartHP(X0_4, 10) <= 2 && NPCPartHP(X0_4, 20) <= 9)
            || (NPCPartHP(X0_4, 10) <= 1 && NPCPartHP(X0_4, 20) <= 10)
            || CharacterHasSpEffect(X0_4, 11753));
    SetNPCPartHP(X0_4, 10, 0, false);
    SetNPCPartHP(X0_4, 20, 0, false);
    if (!CharacterHasSpEffect(X0_4, 11753)) {
        ForceAnimationPlayback(X0_4, 20001, false, false, false);
    }
    WaitFixedTimeSeconds(2);
    RestartEvent();
});

$Event(90005462, Restart, function(X0_4) {
    WaitFor(CharacterBackreadStatus(X0_4) && !CharacterHasSpEffect(X0_4, 11752));
    CreateNPCPart(X0_4, 30, NPCPartType.Part3, 11, 1, 1, false, false);
    CreateNPCPart(X0_4, 50, NPCPartType.Part5, 11, 1, 1, false, false);
    WaitFor(
        NPCPartHP(X0_4, 30) <= 0
            || NPCPartHP(X0_4, 50) <= 0
            || (NPCPartHP(X0_4, 30) <= 10 && NPCPartHP(X0_4, 50) <= 1)
            || (NPCPartHP(X0_4, 30) <= 9 && NPCPartHP(X0_4, 50) <= 2)
            || (NPCPartHP(X0_4, 30) <= 8 && NPCPartHP(X0_4, 50) <= 3)
            || (NPCPartHP(X0_4, 30) <= 7 && NPCPartHP(X0_4, 50) <= 4)
            || (NPCPartHP(X0_4, 30) <= 6 && NPCPartHP(X0_4, 50) <= 5)
            || (NPCPartHP(X0_4, 30) <= 5 && NPCPartHP(X0_4, 50) <= 6)
            || (NPCPartHP(X0_4, 30) <= 4 && NPCPartHP(X0_4, 50) <= 7)
            || (NPCPartHP(X0_4, 30) <= 3 && NPCPartHP(X0_4, 50) <= 8)
            || (NPCPartHP(X0_4, 30) <= 2 && NPCPartHP(X0_4, 50) <= 9)
            || (NPCPartHP(X0_4, 30) <= 1 && NPCPartHP(X0_4, 50) <= 10));
    SetNPCPartHP(X0_4, 30, 0, false);
    SetNPCPartHP(X0_4, 50, 0, false);
    ForceAnimationPlayback(X0_4, 20000, false, false, false);
    WaitFixedTimeSeconds(2);
    RestartEvent();
});

$Event(90005463, Restart, function(X0_4, X4_4) {
    if (!ThisEventSlot()) {
        WaitFor(
            EventValue(X0_4, 3) >= 5
                || (HasDamageType(X4_4, 0, DamageType.Unspecified)
                    && !CharacterHasSpEffect(X0_4, 11757)));
    }
L0:
    SetSpEffect(X4_4, 11757);
});

$Event(90005464, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    EndIf(EventValue(X0_4, 3) > X12_4);
    DisableCharacter(X8_4);
    DisableCharacterCollision(X8_4);
    DisableCharacterAI(X8_4);
    WaitFor(
        CharacterHasSpEffect(X4_4, 11771) && EventValue(X0_4, 3) == X12_4 && !CharacterDead(X4_4));
    WaitFixedTimeFrames(1);
    IncrementEventValue(X0_4, 3, 5);
    EnableCharacter(X8_4);
    ForceAnimationPlayback(X8_4, 20000, false, false, false);
    WarpCharacterAndCopyFloor(X8_4, TargetEntityType.Character, X4_4, 70, X4_4);
    WaitFixedTimeSeconds(3);
    EnableCharacterCollision(X8_4);
    EnableCharacterAI(X8_4);
});

$Event(90005470, Restart, function(X0_4) {
    WaitFor(CharacterBackreadStatus(X0_4));
    if (!ThisEventSlot()) {
        if (CharacterHasSpEffect(X0_4, 12160)) {
            CreateNPCPart(X0_4, 20, NPCPartType.Part2, 80, 1, 3, false, false);
            SetNPCPartSEAndSFX(X0_4, 20, 120, 120, -1, -1, -1);
        }
        if (CharacterHasSpEffect(X0_4, 12161)) {
            CreateNPCPart(X0_4, 30, NPCPartType.Part3, 80, 1, 3, false, false);
            SetNPCPartSEAndSFX(X0_4, 30, 120, 120, -1, -1, -1);
        }
        if (CharacterHasSpEffect(X0_4, 12162)) {
            CreateNPCPart(X0_4, 40, NPCPartType.Part4, 75, 1, 3, false, false);
            SetNPCPartSEAndSFX(X0_4, 40, 120, 120, -1, -1, -1);
        }
        if (CharacterHasSpEffect(X0_4, 12163)) {
            CreateNPCPart(X0_4, 50, NPCPartType.Part5, 75, 1, 3, false, false);
            SetNPCPartSEAndSFX(X0_4, 50, 120, 120, -1, -1, -1);
        }
    }
L1:
    if (CharacterHasSpEffect(X0_4, 12160)) {
        hpSp = NPCPartHP(X0_4, 20) <= 0
            && CharacterHasSpEffect(X0_4, 12156)
            && CharacterHasSpEffect(X0_4, 12168)
            && !CharacterHasSpEffect(X0_4, 12170)
            && !CharacterHasSpEffect(X0_4, 12171);
    }
    if (CharacterHasSpEffect(X0_4, 12161)) {
        hpSp2 = NPCPartHP(X0_4, 30) <= 0
            && CharacterHasSpEffect(X0_4, 12156)
            && CharacterHasSpEffect(X0_4, 12169)
            && !CharacterHasSpEffect(X0_4, 12170)
            && !CharacterHasSpEffect(X0_4, 12171);
    }
    if (CharacterHasSpEffect(X0_4, 12162)) {
        hpSp3 = NPCPartHP(X0_4, 40) <= 0
            && !CharacterHasSpEffect(X0_4, 12170)
            && !CharacterHasSpEffect(X0_4, 12171);
    }
    if (CharacterHasSpEffect(X0_4, 12163)) {
        hpSp4 = NPCPartHP(X0_4, 50) <= 0
            && !CharacterHasSpEffect(X0_4, 12170)
            && !CharacterHasSpEffect(X0_4, 12171);
    }
    WaitFor(hpSp || hpSp2 || hpSp3 || hpSp4);
    GotoIf(L5, hpSp4.Passed);
    GotoIf(L4, hpSp3.Passed);
    GotoIf(L3, hpSp2.Passed);
    GotoIf(L2, hpSp.Passed);
    Goto(L9);
L2:
    ForceAnimationPlayback(X0_4, 20011, false, true, false);
    CreateNPCPart(X0_4, 20, NPCPartType.Part2, 80, 1, 3, false, false);
    SetNPCPartSEAndSFX(X0_4, 20, 120, 120, -1, -1, -1);
    Goto(L9);
L3:
    ForceAnimationPlayback(X0_4, 20008, false, true, false);
    CreateNPCPart(X0_4, 30, NPCPartType.Part3, 80, 1, 3, false, false);
    SetNPCPartSEAndSFX(X0_4, 20, 120, 120, -1, -1, -1);
    Goto(L9);
L4:
    if (!CharacterHasSpEffect(X0_4, 12156)) {
        ForceAnimationPlayback(X0_4, 20006, false, true, false);
    } else {
        ForceAnimationPlayback(X0_4, 20010, false, true, false);
    }
    CreateNPCPart(X0_4, 40, NPCPartType.Part4, 75, 1, 3, false, false);
    SetNPCPartSEAndSFX(X0_4, 40, 120, 120, -1, -1, -1);
    Goto(L9);
L5:
    if (!CharacterHasSpEffect(X0_4, 12156)) {
        ForceAnimationPlayback(X0_4, 20007, false, true, false);
    } else {
        ForceAnimationPlayback(X0_4, 2009, false, true, false);
    }
    CreateNPCPart(X0_4, 50, NPCPartType.Part5, 75, 1, 3, false, false);
    SetNPCPartSEAndSFX(X0_4, 50, 120, 120, -1, -1, -1);
    Goto(L9);
    if (CharacterHasSpEffect(X0_4, 12160)) {
        SetNPCPartHP(X0_4, 20, 9999999, false);
    }
    if (CharacterHasSpEffect(X0_4, 12161)) {
        SetNPCPartHP(X0_4, 30, 9999999, false);
    }
    if (CharacterHasSpEffect(X0_4, 12162)) {
        SetNPCPartHP(X0_4, 40, 9999999, false);
    }
    if (CharacterHasSpEffect(X0_4, 12163)) {
        SetNPCPartHP(X0_4, 50, 9999999, false);
    }
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

$Event(90005471, Restart, function(X0_4) {
    WaitFor(
        CharacterBackreadStatus(X0_4)
            && CharacterHasSpEffect(X0_4, 12160)
            && !CharacterHasSpEffect(X0_4, 12170));
    if (ThisEventSlot()) {
        SetNPCPartHP(X0_4, 20, 9999999, false);
    } else {
        CreateNPCPart(X0_4, 20, NPCPartType.Part2, 80, 1, 3, false, false);
        SetNPCPartSEAndSFX(X0_4, 20, 120, 120, -1, -1, -1);
    }
L0:
    WaitFor(
        (NPCPartHP(X0_4, 20) <= 0
            && CharacterHasSpEffect(X0_4, 12156)
            && CharacterHasSpEffect(X0_4, 12168)
            && !CharacterHasSpEffect(X0_4, 12171))
            || CharacterHasSpEffect(X0_4, 12170));
    if (!CharacterHasSpEffect(X0_4, 12170)) {
        ForceAnimationPlayback(X0_4, 20011, false, true, false);
    }
    CreateNPCPart(X0_4, 20, NPCPartType.Part2, 80, 1, 3, false, false);
    SetNPCPartSEAndSFX(X0_4, 20, 120, 120, -1, -1, -1);
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

$Event(90005472, Restart, function(X0_4) {
    WaitFor(
        CharacterBackreadStatus(X0_4)
            && CharacterHasSpEffect(X0_4, 12161)
            && !CharacterHasSpEffect(X0_4, 12170));
    if (ThisEventSlot()) {
        SetNPCPartHP(X0_4, 30, 9999999, false);
    } else {
        CreateNPCPart(X0_4, 30, NPCPartType.Part3, 80, 1, 3, false, false);
        SetNPCPartSEAndSFX(X0_4, 30, 120, 120, -1, -1, -1);
    }
L0:
    WaitFor(
        (NPCPartHP(X0_4, 30) <= 0
            && CharacterHasSpEffect(X0_4, 12156)
            && CharacterHasSpEffect(X0_4, 12169)
            && !CharacterHasSpEffect(X0_4, 12171))
            || CharacterHasSpEffect(X0_4, 12170));
    if (!CharacterHasSpEffect(X0_4, 12170)) {
        ForceAnimationPlayback(X0_4, 20008, false, true, false);
    }
    CreateNPCPart(X0_4, 30, NPCPartType.Part3, 80, 1, 3, false, false);
    SetNPCPartSEAndSFX(X0_4, 30, 120, 120, -1, -1, -1);
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

$Event(90004473, Restart, function(X0_4) {
    WaitFor(
        CharacterBackreadStatus(X0_4)
            && CharacterHasSpEffect(X0_4, 12162)
            && !CharacterHasSpEffect(X0_4, 12170));
    if (ThisEventSlot()) {
        SetNPCPartHP(X0_4, 40, 9999999, false);
    } else {
        CreateNPCPart(X0_4, 40, NPCPartType.Part4, 75, 1, 3, false, false);
        SetNPCPartSEAndSFX(X0_4, 40, 120, 120, -1, -1, -1);
    }
L0:
    WaitFor(
        (NPCPartHP(X0_4, 40) <= 0 && !CharacterHasSpEffect(X0_4, 12171))
            || CharacterHasSpEffect(X0_4, 12170));
    if (!CharacterHasSpEffect(X0_4, 12170)) {
        if (!CharacterHasSpEffect(X0_4, 12156)) {
            ForceAnimationPlayback(X0_4, 20006, false, true, false);
            CreateNPCPart(X0_4, 40, NPCPartType.Part4, 75, 1, 3, false, false);
            SetNPCPartSEAndSFX(X0_4, 40, 120, 120, -1, -1, -1);
        } else {
L1:
            ForceAnimationPlayback(X0_4, 20010, false, true, false);
            CreateNPCPart(X0_4, 40, NPCPartType.Part4, 75, 1, 3, false, false);
            SetNPCPartSEAndSFX(X0_4, 40, 120, 120, -1, -1, -1);
            Goto(L9);
        }
    }
L9:
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

$Event(90005474, Restart, function(X0_4) {
    WaitFor(
        CharacterBackreadStatus(X0_4)
            && CharacterHasSpEffect(X0_4, 12163)
            && !CharacterHasSpEffect(X0_4, 12170));
    if (ThisEventSlot()) {
        SetNPCPartHP(X0_4, 50, 9999999, false);
    } else {
        CreateNPCPart(X0_4, 50, NPCPartType.Part5, 75, 1, 3, false, false);
        SetNPCPartSEAndSFX(X0_4, 50, 120, 120, -1, -1, -1);
    }
L0:
    WaitFor(
        (NPCPartHP(X0_4, 50) <= 0 && !CharacterHasSpEffect(X0_4, 12171))
            || CharacterHasSpEffect(X0_4, 12170));
    if (!CharacterHasSpEffect(X0_4, 12170)) {
        if (!CharacterHasSpEffect(X0_4, 12156)) {
            ForceAnimationPlayback(X0_4, 20007, false, true, false);
            CreateNPCPart(X0_4, 50, NPCPartType.Part5, 75, 1, 3, false, false);
            SetNPCPartSEAndSFX(X0_4, 50, 120, 120, -1, -1, -1);
        } else {
L1:
            ForceAnimationPlayback(X0_4, 20009, false, true, false);
            CreateNPCPart(X0_4, 50, NPCPartType.Part5, 75, 1, 3, false, false);
            SetNPCPartSEAndSFX(X0_4, 50, 120, 120, -1, -1, -1);
            Goto(L9);
        }
    }
L9:
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

$Event(90005476, Default, function(X0_4, X4_4) {
    if (CharacterDead(X0_4)) {
        DisableCharacter(X4_4);
        DisableCharacterCollision(X4_4);
        EndEvent();
    }
L0:
    WaitFor(CharacterHasSpEffect(X0_4, 11805));
    WarpCharacterAndCopyFloor(X4_4, TargetEntityType.Character, X0_4, 230, X4_4);
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

$Event(90005480, Restart, function(X0_4) {
    WaitFor(
        CharacterBackreadStatus(X0_4)
            && !CharacterHasSpEffect(X0_4, 16472)
            && !CharacterHasSpEffect(X0_4, 16473)
            && !CharacterHasSpEffect(X0_4, 16474)
            && !CharacterHasSpEffect(X0_4, 16475));
    GotoIf(S0, !ThisEventSlot());
    GotoIf(S1, NPCPartHP(X0_4, 30) != 0);
S0:
    SetSpEffect(X0_4, 16498);
    CreateNPCPart(X0_4, 30, NPCPartType.Part3, 61, 1, 1, false, false);
    ChangeCharacterDispmask(X0_4, 10, ON);
S1:
    GotoIf(S2, !ThisEventSlot());
    GotoIf(S3, NPCPartHP(X0_4, 40) != 0);
S2:
    SetSpEffect(X0_4, 16498);
    CreateNPCPart(X0_4, 40, NPCPartType.Part4, 61, 1, 1, false, false);
    ChangeCharacterDispmask(X0_4, 11, ON);
S3:
    GotoIf(S4, !ThisEventSlot());
    GotoIf(S5, NPCPartHP(X0_4, 50) != 0);
S4:
    SetSpEffect(X0_4, 16498);
    CreateNPCPart(X0_4, 50, NPCPartType.Part5, 61, 1, 1, false, false);
    ChangeCharacterDispmask(X0_4, 12, ON);
S5:
    GotoIf(S6, !ThisEventSlot());
    GotoIf(S7, NPCPartHP(X0_4, 60) != 0);
S6:
    SetSpEffect(X0_4, 16498);
    CreateNPCPart(X0_4, 60, NPCPartType.Part6, 61, 1, 1, false, false);
    ChangeCharacterDispmask(X0_4, 13, ON);
S7:
L0:
    hp = NPCPartHP(X0_4, 30) <= 0;
    hp2 = NPCPartHP(X0_4, 40) <= 0;
    hp3 = NPCPartHP(X0_4, 50) <= 0;
    hp4 = NPCPartHP(X0_4, 60) <= 0;
    WaitFor(hp || hp2 || hp3 || hp4);
    GotoIf(L3, hp.Passed);
    GotoIf(L4, hp2.Passed);
    GotoIf(L5, hp3.Passed);
    GotoIf(L6, hp4.Passed);
L3:
    SetSpEffect(X0_4, 16497);
    SetSpEffect(X0_4, 16484);
    SetSpEffect(X0_4, 16472);
    ChangeCharacterDispmask(X0_4, 10, OFF);
    WaitFixedTimeFrames(2);
    if (!CharacterHasSpEffect(X0_4, 16485)) {
        ForceAnimationPlayback(X0_4, 20000, false, true, false);
    }
    Goto(L9);
L4:
    SetSpEffect(X0_4, 16497);
    SetSpEffect(X0_4, 16484);
    SetSpEffect(X0_4, 16473);
    ChangeCharacterDispmask(X0_4, 11, OFF);
    WaitFixedTimeFrames(2);
    if (!CharacterHasSpEffect(X0_4, 16485)) {
        ForceAnimationPlayback(X0_4, 20001, false, true, false);
    }
    Goto(L9);
L5:
    SetSpEffect(X0_4, 16497);
    SetSpEffect(X0_4, 16484);
    SetSpEffect(X0_4, 16474);
    ChangeCharacterDispmask(X0_4, 12, OFF);
    WaitFixedTimeFrames(2);
    if (!CharacterHasSpEffect(X0_4, 16485)) {
        ForceAnimationPlayback(X0_4, 20002, false, true, false);
    }
    Goto(L9);
L6:
    SetSpEffect(X0_4, 16497);
    SetSpEffect(X0_4, 16484);
    SetSpEffect(X0_4, 16475);
    ChangeCharacterDispmask(X0_4, 13, OFF);
    WaitFixedTimeFrames(2);
    if (!CharacterHasSpEffect(X0_4, 16485)) {
        ForceAnimationPlayback(X0_4, 20003, false, true, false);
    }
    Goto(L9);
L9:
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

$Event(90005481, Restart, function(X0_4) {
    CreateNPCPart(X0_4, 10, NPCPartType.Part1, 9999, 1, 1, false, false);
    SetNPCPartSEAndSFX(X0_4, 0, 110, 110, -1, -1, -1);
    WaitFor(
        CharacterHasSpEffect(X0_4, 16499)
            && NPCPartAttributeDamage(X0_4, 10, 0, DamageType.Unspecified));
    ForceAnimationPlayback(X0_4, 20007, false, false, false);
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

$Event(90005485, Restart, function(X0_4) {
    DisableNetworkSync();
    if (!ThisEventSlot()) {
        EnableCharacterDefaultBackread(X0_4);
        SetCharacterEnableDistance(X0_4, 2000);
        DisableCharacterDisableOnHitUnload(X0_4);
        EnableDistancebasedNetworkUpdateAuthority(X0_4);
    }
L0:
    DisableCharacterGravity(X0_4);
    WaitFor(EntityInRadiusOfEntity(X0_4, 10000, 200, 1));
    EnableCharacterGravity(X0_4);
    WaitFor(EntityInRadiusOfEntity(X0_4, 10000, 220, 1));
    RestartEvent();
});

$Event(90005490, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    DisableCharacterGravity(X0_4);
    SetNetworkUpdateRate(X0_4, true, CharacterUpdateFrequency.AtLeastEvery5Frames);
    DisableCharacterDisableOnHitUnload(X0_4);
    SetCharacterEnableDistance(X0_4, 2000);
    IssueShortWarpRequest(X0_4, TargetEntityType.Asset, X8_4, 100);
    ReproduceAssetAnimation(X8_4, 0);
    if (PlayerIsInOwnWorld()) {
        SetNetworkUpdateAuthority(X0_4, AuthorityLevel.Forced);
    }
    WaitFor(
        (((CharacterType(10000, TargetType.BlackPhantom) && CharacterHasSpEffect(10000, 3710))
            || CharacterType(10000, TargetType.Alive)
            || CharacterType(10000, TargetType.GrayPhantom)
            || CharacterType(10000, TargetType.WhitePhantom)
            || CharacterType(10000, TargetType.BluePhantom))
            && InArea(10000, X20_4)
            && CharacterAIState(X0_4, AIStateType.Combat)
            && !CharacterDead(X4_4))
            || ObjActEventFlag(X16_4));
    SetNetworkUpdateRate(X0_4, true, CharacterUpdateFrequency.AlwaysUpdate);
    SetSpEffect(X0_4, 16601);
    if (X24_4 != 0) {
        RequestCharacterAICommand(X0_4, 20, 0);
    } else {
        RequestCharacterAICommand(X0_4, 10, 0);
    }
    RequestCharacterAIReplan(X0_4);
    ForceAnimationPlayback(X8_4, 0, false, true, true);
    EnableObjAct(X12_4, -1);
    RequestCharacterAICommand(X0_4, -1, 0);
    RequestCharacterAIReplan(X0_4);
    SetNetworkUpdateRate(X0_4, true, CharacterUpdateFrequency.AtLeastEvery5Frames);
    RestartEvent();
});

$Event(90005491, Restart, function(X0_4, X4_4, X8_4) {
    WaitFor(
        !CharacterDead(X0_4, GreaterOrEqual, 1)
            && EntityInRadiusOfEntity(X0_4, X4_4, 2, 1)
            && InArea(10000, X8_4));
    InitializeObjAct(X4_4, -1, -1);
    WaitFixedTimeSeconds(0.5);
    RestartEvent();
});

$Event(90005500, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4, X40_4, X44_4, X48_4) {
    if (!(((EventFlag(X0_4) && EventFlag(X4_4)) || (!EventFlag(X0_4) && !EventFlag(X4_4)))
        && EventFlag(X40_4))) {
        if (EventFlag(X4_4)) {
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                EnableObjAct(X24_4, -1);
                DisableObjAct(X16_4, -1);
            }
            obj = ObjActEventFlag(X28_4);
            flag = !EventFlag(X0_4);
            areaFlag &= InArea(10000, X32_4);
            if (X48_4 != 0) {
                areaFlag &= EventFlag(X48_4);
            }
            WaitFor(obj || flag || areaFlag);
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                DisableObjAct(X24_4, -1);
            }
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                SetNetworkconnectedEventFlagID(X40_4, ON);
                SetNetworkconnectedEventFlagID(X0_4, OFF);
            }
            SetEventFlagID(X4_4, OFF);
            if (!obj.Passed) {
                GotoIf(L1, EventFlag(X44_4));
                GotoIf(S9, X8_4 == 10);
                GotoIf(S8, X8_4 == 9);
                GotoIf(S7, X8_4 == 8);
                GotoIf(S6, X8_4 == 7);
                GotoIf(S5, X8_4 == 6);
                GotoIf(S4, X8_4 == 5);
                GotoIf(S3, X8_4 == 4);
                GotoIf(S2, X8_4 == 3);
                GotoIf(S1, X8_4 == 2);
                GotoIf(S0, X8_4 == 1);
                ForceAnimationPlayback(X12_4, 21, false, true, true);
                Goto(L2);
S0:
                ForceAnimationPlayback(X12_4, 1000021, false, true, true);
                Goto(L2);
S1:
                ForceAnimationPlayback(X12_4, 2000021, false, true, true);
                Goto(L2);
S2:
                ForceAnimationPlayback(X12_4, 3000021, false, true, true);
                Goto(L2);
S3:
                ForceAnimationPlayback(X12_4, 4000021, false, true, true);
                Goto(L2);
S4:
                ForceAnimationPlayback(X12_4, 5000021, false, true, true);
                Goto(L2);
S5:
                ForceAnimationPlayback(X12_4, 6000021, false, true, true);
                Goto(L2);
S6:
                ForceAnimationPlayback(X12_4, 7000021, false, true, true);
                Goto(L2);
S7:
                ForceAnimationPlayback(X12_4, 8000021, false, true, true);
                Goto(L2);
S8:
                ForceAnimationPlayback(X12_4, 9000021, false, true, true);
                Goto(L2);
S9:
                ForceAnimationPlayback(X12_4, 10000021, false, true, true);
            } else {
L1:
                if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                    SetNetworkconnectedEventFlagID(X44_4, ON);
                }
                WaitFixedTimeSeconds(2);
                GotoIf(S19, X8_4 == 10);
                GotoIf(S18, X8_4 == 9);
                GotoIf(S17, X8_4 == 8);
                GotoIf(S16, X8_4 == 7);
                GotoIf(S15, X8_4 == 6);
                GotoIf(S14, X8_4 == 5);
                GotoIf(S13, X8_4 == 4);
                GotoIf(S12, X8_4 == 3);
                GotoIf(S11, X8_4 == 2);
                GotoIf(S10, X8_4 == 1);
                ForceAnimationPlayback(X12_4, 21, false, true, true);
                Goto(L11);
S10:
                ForceAnimationPlayback(X12_4, 1000021, false, true, true);
                Goto(L11);
S11:
                ForceAnimationPlayback(X12_4, 2000021, false, true, true);
                Goto(L11);
S12:
                ForceAnimationPlayback(X12_4, 3000021, false, true, true);
                Goto(L11);
S13:
                ForceAnimationPlayback(X12_4, 4000021, false, true, true);
                Goto(L11);
S14:
                ForceAnimationPlayback(X12_4, 5000021, false, true, true);
                Goto(L11);
S15:
                ForceAnimationPlayback(X12_4, 6000021, false, true, true);
                Goto(L11);
S16:
                ForceAnimationPlayback(X12_4, 7000021, false, true, true);
                Goto(L11);
S17:
                ForceAnimationPlayback(X12_4, 8000021, false, true, true);
                Goto(L11);
S18:
                ForceAnimationPlayback(X12_4, 9000021, false, true, true);
                Goto(L11);
S19:
                ForceAnimationPlayback(X12_4, 10000021, false, true, true);
L11:
                ForceAnimationPlayback(X24_4, 3, false, false, true);
                if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                    SetNetworkconnectedEventFlagID(X44_4, OFF);
                }
            }
L2:
            WaitFor(
                AssetBackread(X12_4, Equal, 1) && (!AllPlayersInArea(X36_4) || EventFlag(X0_4)));
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                SetNetworkconnectedEventFlagID(X40_4, OFF);
                GotoIf(S29, X8_4 == 10);
                GotoIf(S28, X8_4 == 9);
                GotoIf(S27, X8_4 == 8);
                GotoIf(S26, X8_4 == 7);
                GotoIf(S25, X8_4 == 6);
                GotoIf(S24, X8_4 == 5);
                GotoIf(S23, X8_4 == 4);
                GotoIf(S22, X8_4 == 3);
                GotoIf(S21, X8_4 == 2);
                GotoIf(S20, X8_4 == 1);
                ForceAnimationPlayback(X12_4, 110, false, false, true);
                Goto(L12);
S20:
                ForceAnimationPlayback(X12_4, 1000110, false, false, true);
                Goto(L12);
S21:
                ForceAnimationPlayback(X12_4, 2000110, false, false, true);
                Goto(L12);
S22:
                ForceAnimationPlayback(X12_4, 3000110, false, false, true);
                Goto(L12);
S23:
                ForceAnimationPlayback(X12_4, 4000110, false, false, true);
                Goto(L12);
S24:
                ForceAnimationPlayback(X12_4, 5000110, false, false, true);
                Goto(L12);
S25:
                ForceAnimationPlayback(X12_4, 6000110, false, false, true);
                Goto(L12);
S26:
                ForceAnimationPlayback(X12_4, 7000110, false, false, true);
                Goto(L12);
S27:
                ForceAnimationPlayback(X12_4, 8000110, false, false, true);
                Goto(L12);
S28:
                ForceAnimationPlayback(X12_4, 9000110, false, false, true);
                Goto(L12);
S29:
                ForceAnimationPlayback(X12_4, 10000110, false, false, true);
            } else {
L3:
                GotoIf(S39, X8_4 == 10);
                GotoIf(S38, X8_4 == 9);
                GotoIf(S37, X8_4 == 8);
                GotoIf(S36, X8_4 == 7);
                GotoIf(S35, X8_4 == 6);
                GotoIf(S34, X8_4 == 5);
                GotoIf(S33, X8_4 == 4);
                GotoIf(S32, X8_4 == 3);
                GotoIf(S31, X8_4 == 2);
                GotoIf(S30, X8_4 == 1);
                ForceAnimationPlayback(X12_4, 110, false, true, true);
                Goto(L12);
S30:
                ForceAnimationPlayback(X12_4, 1000110, false, true, true);
                Goto(L12);
S31:
                ForceAnimationPlayback(X12_4, 2000110, false, true, true);
                Goto(L12);
S32:
                ForceAnimationPlayback(X12_4, 3000110, false, true, true);
                Goto(L12);
S33:
                ForceAnimationPlayback(X12_4, 4000110, false, true, true);
                Goto(L12);
S34:
                ForceAnimationPlayback(X12_4, 5000110, false, true, true);
                Goto(L12);
S35:
                ForceAnimationPlayback(X12_4, 6000110, false, true, true);
                Goto(L12);
S36:
                ForceAnimationPlayback(X12_4, 7000110, false, true, true);
                Goto(L12);
S37:
                ForceAnimationPlayback(X12_4, 8000110, false, true, true);
                Goto(L12);
S38:
                ForceAnimationPlayback(X12_4, 9000110, false, true, true);
                Goto(L12);
S39:
                ForceAnimationPlayback(X12_4, 10000110, false, true, true);
            }
L12:
            RestartEvent();
        }
L0:
        if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
            EnableObjAct(X16_4, -1);
            DisableObjAct(X24_4, -1);
        }
        obj2 = ObjActEventFlag(X20_4);
        flag2 = EventFlag(X0_4);
        areaSpFlag &= InArea(10000, X36_4) && !CharacterHasSpEffect(10000, 4800);
        if (X48_4 != 0) {
            areaSpFlag &= EventFlag(X48_4);
        }
        WaitFor(obj2 || flag2 || areaSpFlag);
        if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
            DisableObjAct(X16_4, -1);
        }
        if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
            SetNetworkconnectedEventFlagID(X40_4, ON);
            SetNetworkconnectedEventFlagID(X0_4, ON);
        }
        SetEventFlagID(X4_4, ON);
        if (!obj2.Passed) {
            GotoIf(L4, EventFlag(X44_4));
            GotoIf(S49, X8_4 == 10);
            GotoIf(S48, X8_4 == 9);
            GotoIf(S47, X8_4 == 8);
            GotoIf(S46, X8_4 == 7);
            GotoIf(S45, X8_4 == 6);
            GotoIf(S44, X8_4 == 5);
            GotoIf(S43, X8_4 == 4);
            GotoIf(S42, X8_4 == 3);
            GotoIf(S41, X8_4 == 2);
            GotoIf(S40, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 12, false, true, true);
            Goto(L5);
S40:
            ForceAnimationPlayback(X12_4, 1000012, false, true, true);
            Goto(L5);
S41:
            ForceAnimationPlayback(X12_4, 2000012, false, true, true);
            Goto(L5);
S42:
            ForceAnimationPlayback(X12_4, 3000012, false, true, true);
            Goto(L5);
S43:
            ForceAnimationPlayback(X12_4, 4000012, false, true, true);
            Goto(L5);
S44:
            ForceAnimationPlayback(X12_4, 5000012, false, true, true);
            Goto(L5);
S45:
            ForceAnimationPlayback(X12_4, 6000012, false, true, true);
            Goto(L5);
S46:
            ForceAnimationPlayback(X12_4, 7000012, false, true, true);
            Goto(L5);
S47:
            ForceAnimationPlayback(X12_4, 8000012, false, true, true);
            Goto(L5);
S48:
            ForceAnimationPlayback(X12_4, 9000012, false, true, true);
            Goto(L5);
S49:
            ForceAnimationPlayback(X12_4, 10000012, false, true, true);
        } else {
L4:
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                SetNetworkconnectedEventFlagID(X44_4, ON);
            }
            WaitFixedTimeSeconds(2);
            GotoIf(S59, X8_4 == 10);
            GotoIf(S58, X8_4 == 9);
            GotoIf(S57, X8_4 == 8);
            GotoIf(S56, X8_4 == 7);
            GotoIf(S55, X8_4 == 6);
            GotoIf(S54, X8_4 == 5);
            GotoIf(S53, X8_4 == 4);
            GotoIf(S52, X8_4 == 3);
            GotoIf(S51, X8_4 == 2);
            GotoIf(S50, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 12, false, true, true);
            Goto(L14);
S50:
            ForceAnimationPlayback(X12_4, 1000012, false, true, true);
            Goto(L14);
S51:
            ForceAnimationPlayback(X12_4, 2000012, false, true, true);
            Goto(L14);
S52:
            ForceAnimationPlayback(X12_4, 3000012, false, true, true);
            Goto(L14);
S53:
            ForceAnimationPlayback(X12_4, 4000012, false, true, true);
            Goto(L14);
S54:
            ForceAnimationPlayback(X12_4, 5000012, false, true, true);
            Goto(L14);
S55:
            ForceAnimationPlayback(X12_4, 6000012, false, true, true);
            Goto(L14);
S56:
            ForceAnimationPlayback(X12_4, 7000012, false, true, true);
            Goto(L14);
S57:
            ForceAnimationPlayback(X12_4, 8000012, false, true, true);
            Goto(L14);
S58:
            ForceAnimationPlayback(X12_4, 9000012, false, true, true);
            Goto(L14);
S59:
            ForceAnimationPlayback(X12_4, 10000012, false, true, true);
L14:
            ForceAnimationPlayback(X16_4, 3, false, false, true);
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                SetNetworkconnectedEventFlagID(X44_4, OFF);
            }
        }
L5:
        WaitFor(AssetBackread(X12_4, Equal, 1) && (!AllPlayersInArea(X32_4) || !EventFlag(X0_4)));
        if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
            SetNetworkconnectedEventFlagID(X40_4, OFF);
            GotoIf(S69, X8_4 == 10);
            GotoIf(S68, X8_4 == 9);
            GotoIf(S67, X8_4 == 8);
            GotoIf(S66, X8_4 == 7);
            GotoIf(S65, X8_4 == 6);
            GotoIf(S64, X8_4 == 5);
            GotoIf(S63, X8_4 == 4);
            GotoIf(S62, X8_4 == 3);
            GotoIf(S61, X8_4 == 2);
            GotoIf(S60, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 120, false, false, true);
            Goto(L15);
S60:
            ForceAnimationPlayback(X12_4, 1000120, false, false, true);
            Goto(L15);
S61:
            ForceAnimationPlayback(X12_4, 2000120, false, false, true);
            Goto(L15);
S62:
            ForceAnimationPlayback(X12_4, 3000120, false, false, true);
            Goto(L15);
S63:
            ForceAnimationPlayback(X12_4, 4000120, false, false, true);
            Goto(L15);
S64:
            ForceAnimationPlayback(X12_4, 5000120, false, false, true);
            Goto(L15);
S65:
            ForceAnimationPlayback(X12_4, 6000120, false, false, true);
            Goto(L15);
S66:
            ForceAnimationPlayback(X12_4, 7000120, false, false, true);
            Goto(L15);
S67:
            ForceAnimationPlayback(X12_4, 8000120, false, false, true);
            Goto(L15);
S68:
            ForceAnimationPlayback(X12_4, 9000120, false, false, true);
            Goto(L15);
S69:
            ForceAnimationPlayback(X12_4, 10000120, false, false, true);
        } else {
L6:
            GotoIf(S79, X8_4 == 10);
            GotoIf(S78, X8_4 == 9);
            GotoIf(S77, X8_4 == 8);
            GotoIf(S76, X8_4 == 7);
            GotoIf(S75, X8_4 == 6);
            GotoIf(S74, X8_4 == 5);
            GotoIf(S73, X8_4 == 4);
            GotoIf(S72, X8_4 == 3);
            GotoIf(S71, X8_4 == 2);
            GotoIf(S70, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 120, false, true, true);
            Goto(L15);
S70:
            ForceAnimationPlayback(X12_4, 1000120, false, true, true);
            Goto(L15);
S71:
            ForceAnimationPlayback(X12_4, 2000120, false, true, true);
            Goto(L15);
S72:
            ForceAnimationPlayback(X12_4, 3000120, false, true, true);
            Goto(L15);
S73:
            ForceAnimationPlayback(X12_4, 4000120, false, true, true);
            Goto(L15);
S74:
            ForceAnimationPlayback(X12_4, 5000120, false, true, true);
            Goto(L15);
S75:
            ForceAnimationPlayback(X12_4, 6000120, false, true, true);
            Goto(L15);
S76:
            ForceAnimationPlayback(X12_4, 7000120, false, true, true);
            Goto(L15);
S77:
            ForceAnimationPlayback(X12_4, 8000120, false, true, true);
            Goto(L15);
S78:
            ForceAnimationPlayback(X12_4, 9000120, false, true, true);
            Goto(L15);
S79:
            ForceAnimationPlayback(X12_4, 10000120, false, true, true);
        }
L15:
        RestartEvent();
    }
L9:
    WaitFor(!EventFlag(X40_4));
    RestartEvent();
});

$Event(90005501, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    if (PlayerIsInOwnWorld()) {
        SetEventFlagID(X24_4, OFF);
    }
    WaitFor(AssetBackread(X12_4, Equal, 1));
    if (EventFlag(X0_4)) {
        if (X8_4 != 10) {
            GotoIf(S8, X8_4 == 9);
            GotoIf(S7, X8_4 == 8);
            GotoIf(S6, X8_4 == 7);
            GotoIf(S5, X8_4 == 6);
            GotoIf(S4, X8_4 == 5);
            GotoIf(S3, X8_4 == 4);
            GotoIf(S2, X8_4 == 3);
            GotoIf(S1, X8_4 == 2);
            GotoIf(S0, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 20, false, false, false);
            Goto(L10);
S0:
            ForceAnimationPlayback(X12_4, 1000020, false, false, false);
            Goto(L10);
S1:
            ForceAnimationPlayback(X12_4, 2000020, false, false, false);
            Goto(L10);
S2:
            ForceAnimationPlayback(X12_4, 3000020, false, false, false);
            Goto(L10);
S3:
            ForceAnimationPlayback(X12_4, 4000020, false, false, false);
            Goto(L10);
S4:
            ForceAnimationPlayback(X12_4, 5000020, false, false, false);
            Goto(L10);
S5:
            ForceAnimationPlayback(X12_4, 6000020, false, false, false);
            Goto(L10);
S6:
            ForceAnimationPlayback(X12_4, 7000020, false, false, false);
            Goto(L10);
S7:
            ForceAnimationPlayback(X12_4, 8000020, false, false, false);
            Goto(L10);
S8:
            ForceAnimationPlayback(X12_4, 9000020, false, false, false);
        } else {
            ForceAnimationPlayback(X12_4, 10000020, false, false, false);
        }
L10:
        SetEventFlagID(X4_4, ON);
        DisableObjAct(X16_4, -1);
        EndEvent();
    }
L0:
    GotoIf(S18, X8_4 == 10);
    GotoIf(S17, X8_4 == 9);
    GotoIf(S16, X8_4 == 8);
    GotoIf(S15, X8_4 == 7);
    GotoIf(S14, X8_4 == 6);
    GotoIf(S13, X8_4 == 5);
    GotoIf(S12, X8_4 == 4);
    GotoIf(S11, X8_4 == 3);
    GotoIf(S10, X8_4 == 2);
    GotoIf(S9, X8_4 == 1);
    ForceAnimationPlayback(X12_4, 10, false, false, true);
    Goto(L15);
S9:
    ForceAnimationPlayback(X12_4, 1000010, false, false, true);
    Goto(L15);
S10:
    ForceAnimationPlayback(X12_4, 2000010, false, false, true);
    Goto(L15);
S11:
    ForceAnimationPlayback(X12_4, 3000010, false, false, true);
    Goto(L15);
S12:
    ForceAnimationPlayback(X12_4, 4000010, false, false, true);
    Goto(L15);
S13:
    ForceAnimationPlayback(X12_4, 5000010, false, false, true);
    Goto(L15);
S14:
    ForceAnimationPlayback(X12_4, 6000010, false, false, true);
    Goto(L15);
S15:
    ForceAnimationPlayback(X12_4, 7000010, false, false, true);
    Goto(L15);
S16:
    ForceAnimationPlayback(X12_4, 8000010, false, false, true);
    Goto(L15);
S17:
    ForceAnimationPlayback(X12_4, 9000010, false, false, true);
    Goto(L15);
S18:
    ForceAnimationPlayback(X12_4, 10000010, false, false, true);
L15:
    SetEventFlagID(X4_4, OFF);
    DisableObjAct(X20_4, -1);
    EndEvent();
});

$Event(90005502, Restart, function(X0_4, X4_4, X8_4) {
    DisableNetworkSync();
    EndIf(EventFlag(X0_4));
    WaitFixedTimeFrames(2);
    DisableObjAct(X4_4, -1);
    areaChr = InArea(10000, X8_4)
        && (CharacterType(10000, TargetType.Alive) || CharacterType(10000, TargetType.GrayPhantom));
    WaitFor(areaChr || ActionButtonInArea(8301, X4_4) || EventFlag(X0_4));
    if (!areaChr.Passed) {
        EndIf(EventFlag(X0_4));
        DisplayGenericDialog(4000, PromptType.OKCANCEL, NumberofOptions.OneButton, 0, 3);
        RestartEvent();
    }
L0:
    if (PlayerIsInOwnWorld()) {
        SetNetworkconnectedEventFlagID(X0_4, ON);
    }
    RestartEvent();
});

$Event(90005503, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4, X40_4) {
    if (!(((EventFlag(X0_4) && EventFlag(X4_4)) || (!EventFlag(X0_4) && !EventFlag(X4_4)))
        && EventFlag(X32_4))) {
        if (EventFlag(X4_4)) {
            flag = !EventFlag(X0_4);
            cond &= InArea(10000, X16_4) && !CharacterHasSpEffect(10000, 4800);
            if (X40_4 != 0) {
                cond &= EventFlag(X40_4);
            }
            areaSpFlag &= InArea(10000, X28_4) && !CharacterHasSpEffect(10000, 4800);
            if (X40_4 != 0) {
                areaSpFlag &= EventFlag(X40_4);
            }
            WaitFor(flag || cond || areaSpFlag);
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                SetNetworkconnectedEventFlagID(X32_4, ON);
                SetNetworkconnectedEventFlagID(X0_4, OFF);
            }
            SetEventFlagID(X4_4, OFF);
            GotoIf(S3, X8_4 == 4);
            GotoIf(S2, X8_4 == 3);
            GotoIf(S1, X8_4 == 2);
            GotoIf(S0, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 21, false, true, true);
            Goto(L2);
S0:
            ForceAnimationPlayback(X12_4, 1000021, false, true, true);
            Goto(L2);
S1:
            ForceAnimationPlayback(X12_4, 2000021, false, true, true);
            Goto(L2);
S2:
            ForceAnimationPlayback(X12_4, 3000021, false, true, true);
            Goto(L2);
S3:
            ForceAnimationPlayback(X12_4, 4000021, false, true, true);
L2:
            WaitFor(
                AssetBackread(X12_4, Equal, 1)
                    && ((!AllPlayersInArea(X24_4) && !AllPlayersInArea(X20_4)) || EventFlag(X0_4)));
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                SetNetworkconnectedEventFlagID(X32_4, OFF);
                GotoIf(S7, X8_4 == 4);
                GotoIf(S6, X8_4 == 3);
                GotoIf(S5, X8_4 == 2);
                GotoIf(S4, X8_4 == 1);
                ForceAnimationPlayback(X12_4, 110, false, false, true);
                Goto(L12);
S4:
                ForceAnimationPlayback(X12_4, 1000110, false, false, true);
                Goto(L12);
S5:
                ForceAnimationPlayback(X12_4, 2000110, false, false, true);
                Goto(L12);
S6:
                ForceAnimationPlayback(X12_4, 3000110, false, false, true);
                Goto(L12);
S7:
                ForceAnimationPlayback(X12_4, 4000110, false, false, true);
            } else {
L3:
                GotoIf(S11, X8_4 == 4);
                GotoIf(S10, X8_4 == 3);
                GotoIf(S9, X8_4 == 2);
                GotoIf(S8, X8_4 == 1);
                ForceAnimationPlayback(X12_4, 110, false, true, true);
                Goto(L12);
S8:
                ForceAnimationPlayback(X12_4, 1000110, false, true, true);
                Goto(L12);
S9:
                ForceAnimationPlayback(X12_4, 2000110, false, true, true);
                Goto(L12);
S10:
                ForceAnimationPlayback(X12_4, 3000110, false, true, true);
                Goto(L12);
S11:
                ForceAnimationPlayback(X12_4, 4000110, false, true, true);
            }
L12:
            RestartEvent();
        }
L0:
        flag2 = EventFlag(X0_4);
        areaSpFlag2 &= InArea(10000, X24_4) && !CharacterHasSpEffect(10000, 4800);
        if (X40_4 != 0) {
            areaSpFlag2 &= EventFlag(X40_4);
        }
        areaSpFlag3 &= InArea(10000, X20_4) && !CharacterHasSpEffect(10000, 4800);
        if (X40_4 != 0) {
            areaSpFlag3 &= EventFlag(X40_4);
        }
        WaitFor(flag2 || areaSpFlag2 || areaSpFlag3);
        if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
            DisableObjAct(X16_4, -1);
        }
        if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
            SetNetworkconnectedEventFlagID(X32_4, ON);
            SetNetworkconnectedEventFlagID(X0_4, ON);
        }
        SetEventFlagID(X4_4, ON);
        if (!flag2.Passed) {
            GotoIf(L4, EventFlag(X36_4));
            GotoIf(S15, X8_4 == 4);
            GotoIf(S14, X8_4 == 3);
            GotoIf(S13, X8_4 == 2);
            GotoIf(S12, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 12, false, true, true);
            Goto(L5);
S12:
            ForceAnimationPlayback(X12_4, 1000012, false, true, true);
            Goto(L5);
S13:
            ForceAnimationPlayback(X12_4, 2000012, false, true, true);
            Goto(L5);
S14:
            ForceAnimationPlayback(X12_4, 3000012, false, true, true);
            Goto(L5);
S15:
            ForceAnimationPlayback(X12_4, 4000012, false, true, true);
        } else {
L4:
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                SetNetworkconnectedEventFlagID(X36_4, ON);
            }
            WaitFixedTimeSeconds(2);
            GotoIf(S19, X8_4 == 4);
            GotoIf(S18, X8_4 == 3);
            GotoIf(S17, X8_4 == 2);
            GotoIf(S16, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 12, false, true, true);
            Goto(L14);
S16:
            ForceAnimationPlayback(X12_4, 1000012, false, true, true);
            Goto(L14);
S17:
            ForceAnimationPlayback(X12_4, 2000012, false, true, true);
            Goto(L14);
S18:
            ForceAnimationPlayback(X12_4, 3000012, false, true, true);
            Goto(L14);
S19:
            ForceAnimationPlayback(X12_4, 4000012, false, true, true);
L14:
            ForceAnimationPlayback(X16_4, 3, false, false, true);
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                SetNetworkconnectedEventFlagID(X36_4, OFF);
            }
        }
L5:
        cond &= AssetBackread(X12_4, Equal, 1)
            && ((!AllPlayersInArea(X24_4) && !AllPlayersInArea(X20_4)) || !EventFlag(X0_4));
        WaitFor(cond);
        if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
            SetNetworkconnectedEventFlagID(X32_4, OFF);
            GotoIf(S23, X8_4 == 4);
            GotoIf(S22, X8_4 == 3);
            GotoIf(S21, X8_4 == 2);
            GotoIf(S20, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 120, false, false, true);
            Goto(L15);
S20:
            ForceAnimationPlayback(X12_4, 1000120, false, false, true);
            Goto(L15);
S21:
            ForceAnimationPlayback(X12_4, 2000120, false, false, true);
            Goto(L15);
S22:
            ForceAnimationPlayback(X12_4, 3000120, false, false, true);
            Goto(L15);
S23:
            ForceAnimationPlayback(X12_4, 4000120, false, false, true);
        } else {
L6:
            GotoIf(S27, X8_4 == 4);
            GotoIf(S26, X8_4 == 3);
            GotoIf(S25, X8_4 == 2);
            GotoIf(S24, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 120, false, false, true);
            Goto(L15);
S24:
            ForceAnimationPlayback(X12_4, 1000120, false, false, true);
            Goto(L15);
S25:
            ForceAnimationPlayback(X12_4, 2000120, false, false, true);
            Goto(L15);
S26:
            ForceAnimationPlayback(X12_4, 3000120, false, false, true);
            Goto(L15);
S27:
            ForceAnimationPlayback(X12_4, 4000120, false, false, true);
        }
L15:
        RestartEvent();
    }
L9:
    WaitFor(!EventFlag(X32_4));
    RestartEvent();
});

$Event(90005504, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    if (PlayerIsInOwnWorld()) {
        SetEventFlagID(X16_4, OFF);
    }
    if (EventFlag(X0_4)) {
        if (X8_4 != 4) {
            GotoIf(S2, X8_4 == 3);
            GotoIf(S1, X8_4 == 2);
            GotoIf(S0, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 20, false, false, false);
            Goto(L10);
S0:
            ForceAnimationPlayback(X12_4, 1000020, false, false, false);
            Goto(L10);
S1:
            ForceAnimationPlayback(X12_4, 2000020, false, false, false);
            Goto(L10);
S2:
            ForceAnimationPlayback(X12_4, 3000020, false, false, false);
        } else {
            ForceAnimationPlayback(X12_4, 4000020, false, false, false);
            Goto(L10);
        }
L10:
        SetEventFlagID(X4_4, ON);
        EndEvent();
    }
L0:
    GotoIf(S6, X8_4 == 4);
    GotoIf(S5, X8_4 == 3);
    GotoIf(S4, X8_4 == 2);
    GotoIf(S3, X8_4 == 1);
    ForceAnimationPlayback(X12_4, 10, false, false, true);
    Goto(L15);
S3:
    ForceAnimationPlayback(X12_4, 1000010, false, false, true);
    Goto(L15);
S4:
    ForceAnimationPlayback(X12_4, 2000010, false, false, true);
    Goto(L15);
S5:
    ForceAnimationPlayback(X12_4, 3000010, false, false, true);
    Goto(L15);
S6:
    ForceAnimationPlayback(X12_4, 4000010, false, false, true);
L15:
    SetEventFlagID(X4_4, OFF);
    EndEvent();
});

$Event(90005505, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4, X40_4) {
    if (!(((EventFlag(X0_4) && EventFlag(X4_4)) || (!EventFlag(X0_4) && !EventFlag(X4_4)))
        && EventFlag(X32_4))) {
        if (EventFlag(X4_4)) {
            if (PlayerIsInOwnWorld()) {
                EnableObjAct(X24_4, -1);
                DisableObjAct(X16_4, -1);
            }
            obj = ObjActEventFlag(X28_4);
            flag = !EventFlag(X0_4);
            if (X40_4 != 0) {
                flagAct &= EventFlag(X40_4);
            }
            flagAct &= ActionButtonInArea(8320, X12_4);
            WaitFor(obj || flag || flagAct);
            if (PlayerIsInOwnWorld()) {
                DisableObjAct(X24_4, -1);
            }
            if (PlayerIsInOwnWorld()) {
                SetNetworkconnectedEventFlagID(X32_4, ON);
                SetNetworkconnectedEventFlagID(X0_4, OFF);
            }
            SetEventFlagID(X4_4, OFF);
            GotoIf(L1, flagAct.Passed);
            GotoIf(L2, obj.Passed);
            GotoIf(L2, EventFlag(X36_4));
            GotoIf(S1, X8_4 == 2);
            GotoIf(S0, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 21, false, true, true);
            Goto(L3);
S0:
            ForceAnimationPlayback(X12_4, 1000021, false, true, true);
            Goto(L3);
S1:
            ForceAnimationPlayback(X12_4, 2000021, false, true, true);
            Goto(L3);
L1:
            IssueShortWarpRequest(10000, TargetEntityType.Asset, X12_4, 191);
            ForceAnimationPlayback(10000, 60200, false, false, false);
            GotoIf(S3, X8_4 == 2);
            GotoIf(S2, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 21, false, true, true);
            Goto(L3);
S2:
            ForceAnimationPlayback(X12_4, 1000021, false, true, true);
            Goto(L3);
S3:
            ForceAnimationPlayback(X12_4, 2000021, false, true, true);
            Goto(L3);
L2:
            SetNetworkconnectedEventFlagID(X36_4, ON);
            WaitFixedTimeSeconds(2);
            if (X8_4 != 2) {
                GotoIf(S4, X8_4 == 1);
                ForceAnimationPlayback(X12_4, 21, false, true, true);
                Goto(L11);
S4:
                ForceAnimationPlayback(X12_4, 1000021, false, true, true);
            } else {
                ForceAnimationPlayback(X12_4, 2000021, false, true, true);
            }
L11:
            ForceAnimationPlayback(X24_4, 3, false, false, true);
            SetNetworkconnectedEventFlagID(X36_4, OFF);
L3:
            WaitFor(AssetBackread(X12_4, Equal, 1));
            if (PlayerIsInOwnWorld()) {
                SetNetworkconnectedEventFlagID(X32_4, OFF);
                GotoIf(S6, X8_4 == 2);
                GotoIf(S5, X8_4 == 1);
                ForceAnimationPlayback(X12_4, 110, false, false, true);
                Goto(L12);
S5:
                ForceAnimationPlayback(X12_4, 1000110, false, false, true);
                Goto(L12);
S6:
                ForceAnimationPlayback(X12_4, 2000110, false, false, true);
            } else {
L4:
                if (X8_4 != 2) {
                    GotoIf(S7, X8_4 == 1);
                    ForceAnimationPlayback(X12_4, 110, false, true, true);
                    Goto(L12);
S7:
                    ForceAnimationPlayback(X12_4, 1000110, false, true, true);
                } else {
                    ForceAnimationPlayback(X12_4, 2000110, false, true, true);
                }
            }
L12:
            RestartEvent();
        }
L0:
        if (PlayerIsInOwnWorld()) {
            EnableObjAct(X16_4, -1);
            DisableObjAct(X24_4, -1);
        }
        obj2 = ObjActEventFlag(X20_4);
        flag2 = EventFlag(X0_4);
        if (X40_4 != 0) {
            flagAct2 &= EventFlag(X40_4);
        }
        flagAct2 &= ActionButtonInArea(8320, X12_4);
        WaitFor(obj2 || flag2 || flagAct2);
        if (PlayerIsInOwnWorld()) {
            DisableObjAct(X16_4, -1);
        }
        if (PlayerIsInOwnWorld()) {
            SetNetworkconnectedEventFlagID(X32_4, ON);
            SetNetworkconnectedEventFlagID(X0_4, ON);
        }
        SetEventFlagID(X4_4, ON);
        GotoIf(L5, flagAct2.Passed);
        GotoIf(L6, obj2.Passed);
        GotoIf(L6, EventFlag(X36_4));
        GotoIf(S9, X8_4 == 2);
        GotoIf(S8, X8_4 == 1);
        ForceAnimationPlayback(X12_4, 12, false, true, true);
        Goto(L7);
S8:
        ForceAnimationPlayback(X12_4, 1000012, false, true, true);
        Goto(L7);
S9:
        ForceAnimationPlayback(X12_4, 2000012, false, true, true);
        Goto(L7);
L5:
        IssueShortWarpRequest(10000, TargetEntityType.Asset, X12_4, 191);
        ForceAnimationPlayback(10000, 60200, false, false, false);
        GotoIf(S11, X8_4 == 2);
        GotoIf(S10, X8_4 == 1);
        ForceAnimationPlayback(X12_4, 12, false, true, true);
        Goto(L7);
S10:
        ForceAnimationPlayback(X12_4, 1000012, false, true, true);
        Goto(L7);
S11:
        ForceAnimationPlayback(X12_4, 2000012, false, true, true);
        Goto(L7);
L6:
        SetNetworkconnectedEventFlagID(X36_4, ON);
        WaitFixedTimeSeconds(2);
        if (X8_4 != 2) {
            GotoIf(S12, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 12, false, true, true);
            Goto(L14);
S12:
            ForceAnimationPlayback(X12_4, 1000012, false, true, true);
        } else {
            ForceAnimationPlayback(X12_4, 2000012, false, true, true);
        }
L14:
        ForceAnimationPlayback(X16_4, 3, false, false, true);
        SetNetworkconnectedEventFlagID(X36_4, OFF);
L7:
        WaitFor(AssetBackread(X12_4, Equal, 1));
        if (PlayerIsInOwnWorld()) {
            SetNetworkconnectedEventFlagID(X32_4, OFF);
            GotoIf(S14, X8_4 == 2);
            GotoIf(S13, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 120, false, false, true);
            Goto(L15);
S13:
            ForceAnimationPlayback(X12_4, 1000120, false, false, true);
            Goto(L15);
S14:
            ForceAnimationPlayback(X12_4, 2000120, false, false, true);
        } else {
L8:
            if (X8_4 != 2) {
                GotoIf(S15, X8_4 == 1);
                ForceAnimationPlayback(X12_4, 120, false, true, true);
                Goto(L15);
S15:
                ForceAnimationPlayback(X12_4, 1000120, false, true, true);
            } else {
                ForceAnimationPlayback(X12_4, 2000120, false, true, true);
            }
        }
L15:
        RestartEvent();
    }
L9:
    WaitFor(!EventFlag(X32_4));
    RestartEvent();
});

$Event(90005507, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4, X40_4, X44_4, X48_4) {
    if (!(((EventFlag(X0_4) && EventFlag(X4_4)) || (!EventFlag(X0_4) && !EventFlag(X4_4)))
        && EventFlag(X40_4))) {
        if (EventFlag(X4_4)) {
            area = InArea(10000, X28_4);
            flag = !EventFlag(X0_4);
            areaFlag &= InArea(10000, X32_4);
            if (X48_4 != 0) {
                areaFlag &= EventFlag(X48_4);
            }
            WaitFor(area || flag || areaFlag);
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                SetNetworkconnectedEventFlagID(X40_4, ON);
                SetNetworkconnectedEventFlagID(X0_4, OFF);
            }
            SetEventFlagID(X4_4, OFF);
            if (!area.Passed) {
                GotoIf(L1, EventFlag(X44_4));
                ForceAnimationPlayback(X24_4, 1, false, false, true);
                GotoIf(S9, X8_4 == 10);
                GotoIf(S8, X8_4 == 9);
                GotoIf(S7, X8_4 == 8);
                GotoIf(S6, X8_4 == 7);
                GotoIf(S5, X8_4 == 6);
                GotoIf(S4, X8_4 == 5);
                GotoIf(S3, X8_4 == 4);
                GotoIf(S2, X8_4 == 3);
                GotoIf(S1, X8_4 == 2);
                GotoIf(S0, X8_4 == 1);
                ForceAnimationPlayback(X12_4, 21, false, true, true);
                Goto(L2);
S0:
                ForceAnimationPlayback(X12_4, 1000021, false, true, true);
                Goto(L2);
S1:
                ForceAnimationPlayback(X12_4, 2000021, false, true, true);
                Goto(L2);
S2:
                ForceAnimationPlayback(X12_4, 3000021, false, true, true);
                Goto(L2);
S3:
                ForceAnimationPlayback(X12_4, 4000021, false, true, true);
                Goto(L2);
S4:
                ForceAnimationPlayback(X12_4, 5000021, false, true, true);
                Goto(L2);
S5:
                ForceAnimationPlayback(X12_4, 6000021, false, true, true);
                Goto(L2);
S6:
                ForceAnimationPlayback(X12_4, 7000021, false, true, true);
                Goto(L2);
S7:
                ForceAnimationPlayback(X12_4, 8000021, false, true, true);
                Goto(L2);
S8:
                ForceAnimationPlayback(X12_4, 9000021, false, true, true);
                Goto(L2);
S9:
                ForceAnimationPlayback(X12_4, 10000021, false, true, true);
            } else {
L1:
                if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                    SetNetworkconnectedEventFlagID(X44_4, ON);
                }
                ForceAnimationPlayback(X24_4, 1, false, false, true);
                WaitFixedTimeSeconds(0.5);
                GotoIf(S19, X8_4 == 10);
                GotoIf(S18, X8_4 == 9);
                GotoIf(S17, X8_4 == 8);
                GotoIf(S16, X8_4 == 7);
                GotoIf(S15, X8_4 == 6);
                GotoIf(S14, X8_4 == 5);
                GotoIf(S13, X8_4 == 4);
                GotoIf(S12, X8_4 == 3);
                GotoIf(S11, X8_4 == 2);
                GotoIf(S10, X8_4 == 1);
                ForceAnimationPlayback(X12_4, 21, false, true, true);
                Goto(L11);
S10:
                ForceAnimationPlayback(X12_4, 1000021, false, true, true);
                Goto(L11);
S11:
                ForceAnimationPlayback(X12_4, 2000021, false, true, true);
                Goto(L11);
S12:
                ForceAnimationPlayback(X12_4, 3000021, false, true, true);
                Goto(L11);
S13:
                ForceAnimationPlayback(X12_4, 4000021, false, true, true);
                Goto(L11);
S14:
                ForceAnimationPlayback(X12_4, 5000021, false, true, true);
                Goto(L11);
S15:
                ForceAnimationPlayback(X12_4, 6000021, false, true, true);
                Goto(L11);
S16:
                ForceAnimationPlayback(X12_4, 7000021, false, true, true);
                Goto(L11);
S17:
                ForceAnimationPlayback(X12_4, 8000021, false, true, true);
                Goto(L11);
S18:
                ForceAnimationPlayback(X12_4, 9000021, false, true, true);
                Goto(L11);
S19:
                ForceAnimationPlayback(X12_4, 10000021, false, true, true);
L11:
                if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                    SetNetworkconnectedEventFlagID(X44_4, OFF);
                }
            }
L2:
            WaitFor(
                AssetBackread(X12_4, Equal, 1) && (!AllPlayersInArea(X36_4) || EventFlag(X0_4)));
            ForceAnimationPlayback(X16_4, 3, false, false, true);
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                SetNetworkconnectedEventFlagID(X40_4, OFF);
                GotoIf(S29, X8_4 == 10);
                GotoIf(S28, X8_4 == 9);
                GotoIf(S27, X8_4 == 8);
                GotoIf(S26, X8_4 == 7);
                GotoIf(S25, X8_4 == 6);
                GotoIf(S24, X8_4 == 5);
                GotoIf(S23, X8_4 == 4);
                GotoIf(S22, X8_4 == 3);
                GotoIf(S21, X8_4 == 2);
                GotoIf(S20, X8_4 == 1);
                ForceAnimationPlayback(X12_4, 110, false, false, true);
                Goto(L12);
S20:
                ForceAnimationPlayback(X12_4, 1000110, false, false, true);
                Goto(L12);
S21:
                ForceAnimationPlayback(X12_4, 2000110, false, false, true);
                Goto(L12);
S22:
                ForceAnimationPlayback(X12_4, 3000110, false, false, true);
                Goto(L12);
S23:
                ForceAnimationPlayback(X12_4, 4000110, false, false, true);
                Goto(L12);
S24:
                ForceAnimationPlayback(X12_4, 5000110, false, false, true);
                Goto(L12);
S25:
                ForceAnimationPlayback(X12_4, 6000110, false, false, true);
                Goto(L12);
S26:
                ForceAnimationPlayback(X12_4, 7000110, false, false, true);
                Goto(L12);
S27:
                ForceAnimationPlayback(X12_4, 8000110, false, false, true);
                Goto(L12);
S28:
                ForceAnimationPlayback(X12_4, 9000110, false, false, true);
                Goto(L12);
S29:
                ForceAnimationPlayback(X12_4, 10000110, false, false, true);
            } else {
L3:
                GotoIf(S39, X8_4 == 10);
                GotoIf(S38, X8_4 == 9);
                GotoIf(S37, X8_4 == 8);
                GotoIf(S36, X8_4 == 7);
                GotoIf(S35, X8_4 == 6);
                GotoIf(S34, X8_4 == 5);
                GotoIf(S33, X8_4 == 4);
                GotoIf(S32, X8_4 == 3);
                GotoIf(S31, X8_4 == 2);
                GotoIf(S30, X8_4 == 1);
                ForceAnimationPlayback(X12_4, 110, false, true, true);
                Goto(L12);
S30:
                ForceAnimationPlayback(X12_4, 1000110, false, true, true);
                Goto(L12);
S31:
                ForceAnimationPlayback(X12_4, 2000110, false, true, true);
                Goto(L12);
S32:
                ForceAnimationPlayback(X12_4, 3000110, false, true, true);
                Goto(L12);
S33:
                ForceAnimationPlayback(X12_4, 4000110, false, true, true);
                Goto(L12);
S34:
                ForceAnimationPlayback(X12_4, 5000110, false, true, true);
                Goto(L12);
S35:
                ForceAnimationPlayback(X12_4, 6000110, false, true, true);
                Goto(L12);
S36:
                ForceAnimationPlayback(X12_4, 7000110, false, true, true);
                Goto(L12);
S37:
                ForceAnimationPlayback(X12_4, 8000110, false, true, true);
                Goto(L12);
S38:
                ForceAnimationPlayback(X12_4, 9000110, false, true, true);
                Goto(L12);
S39:
                ForceAnimationPlayback(X12_4, 10000110, false, true, true);
            }
L12:
            RestartEvent();
        }
L0:
        area2 = InArea(10000, X20_4);
        flag2 = EventFlag(X0_4);
        areaSpFlag &= InArea(10000, X36_4) && !CharacterHasSpEffect(10000, 4800);
        if (X48_4 != 0) {
            areaSpFlag &= EventFlag(X48_4);
        }
        WaitFor(area2 || flag2 || areaSpFlag);
        if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
            SetNetworkconnectedEventFlagID(X40_4, ON);
            SetNetworkconnectedEventFlagID(X0_4, ON);
        }
        SetEventFlagID(X4_4, ON);
        if (!area2.Passed) {
            GotoIf(L4, EventFlag(X44_4));
            ForceAnimationPlayback(X16_4, 1, false, false, true);
            GotoIf(S49, X8_4 == 10);
            GotoIf(S48, X8_4 == 9);
            GotoIf(S47, X8_4 == 8);
            GotoIf(S46, X8_4 == 7);
            GotoIf(S45, X8_4 == 6);
            GotoIf(S44, X8_4 == 5);
            GotoIf(S43, X8_4 == 4);
            GotoIf(S42, X8_4 == 3);
            GotoIf(S41, X8_4 == 2);
            GotoIf(S40, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 12, false, true, true);
            Goto(L5);
S40:
            ForceAnimationPlayback(X12_4, 1000012, false, true, true);
            Goto(L5);
S41:
            ForceAnimationPlayback(X12_4, 2000012, false, true, true);
            Goto(L5);
S42:
            ForceAnimationPlayback(X12_4, 3000012, false, true, true);
            Goto(L5);
S43:
            ForceAnimationPlayback(X12_4, 4000012, false, true, true);
            Goto(L5);
S44:
            ForceAnimationPlayback(X12_4, 5000012, false, true, true);
            Goto(L5);
S45:
            ForceAnimationPlayback(X12_4, 6000012, false, true, true);
            Goto(L5);
S46:
            ForceAnimationPlayback(X12_4, 7000012, false, true, true);
            Goto(L5);
S47:
            ForceAnimationPlayback(X12_4, 8000012, false, true, true);
            Goto(L5);
S48:
            ForceAnimationPlayback(X12_4, 9000012, false, true, true);
            Goto(L5);
S49:
            ForceAnimationPlayback(X12_4, 10000012, false, true, true);
        } else {
L4:
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                SetNetworkconnectedEventFlagID(X44_4, ON);
            }
            ForceAnimationPlayback(X16_4, 1, false, false, true);
            WaitFixedTimeSeconds(0.5);
            GotoIf(S59, X8_4 == 10);
            GotoIf(S58, X8_4 == 9);
            GotoIf(S57, X8_4 == 8);
            GotoIf(S56, X8_4 == 7);
            GotoIf(S55, X8_4 == 6);
            GotoIf(S54, X8_4 == 5);
            GotoIf(S53, X8_4 == 4);
            GotoIf(S52, X8_4 == 3);
            GotoIf(S51, X8_4 == 2);
            GotoIf(S50, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 12, false, true, true);
            Goto(L14);
S50:
            ForceAnimationPlayback(X12_4, 1000012, false, true, true);
            Goto(L14);
S51:
            ForceAnimationPlayback(X12_4, 2000012, false, true, true);
            Goto(L14);
S52:
            ForceAnimationPlayback(X12_4, 3000012, false, true, true);
            Goto(L14);
S53:
            ForceAnimationPlayback(X12_4, 4000012, false, true, true);
            Goto(L14);
S54:
            ForceAnimationPlayback(X12_4, 5000012, false, true, true);
            Goto(L14);
S55:
            ForceAnimationPlayback(X12_4, 6000012, false, true, true);
            Goto(L14);
S56:
            ForceAnimationPlayback(X12_4, 7000012, false, true, true);
            Goto(L14);
S57:
            ForceAnimationPlayback(X12_4, 8000012, false, true, true);
            Goto(L14);
S58:
            ForceAnimationPlayback(X12_4, 9000012, false, true, true);
            Goto(L14);
S59:
            ForceAnimationPlayback(X12_4, 10000012, false, true, true);
L14:
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                SetNetworkconnectedEventFlagID(X44_4, OFF);
            }
        }
L5:
        WaitFor(AssetBackread(X12_4, Equal, 1) && (!AllPlayersInArea(X32_4) || !EventFlag(X0_4)));
        ForceAnimationPlayback(X24_4, 3, false, false, true);
        if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
            SetNetworkconnectedEventFlagID(X40_4, OFF);
            GotoIf(S69, X8_4 == 10);
            GotoIf(S68, X8_4 == 9);
            GotoIf(S67, X8_4 == 8);
            GotoIf(S66, X8_4 == 7);
            GotoIf(S65, X8_4 == 6);
            GotoIf(S64, X8_4 == 5);
            GotoIf(S63, X8_4 == 4);
            GotoIf(S62, X8_4 == 3);
            GotoIf(S61, X8_4 == 2);
            GotoIf(S60, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 120, false, false, true);
            Goto(L15);
S60:
            ForceAnimationPlayback(X12_4, 1000120, false, false, true);
            Goto(L15);
S61:
            ForceAnimationPlayback(X12_4, 2000120, false, false, true);
            Goto(L15);
S62:
            ForceAnimationPlayback(X12_4, 3000120, false, false, true);
            Goto(L15);
S63:
            ForceAnimationPlayback(X12_4, 4000120, false, false, true);
            Goto(L15);
S64:
            ForceAnimationPlayback(X12_4, 5000120, false, false, true);
            Goto(L15);
S65:
            ForceAnimationPlayback(X12_4, 6000120, false, false, true);
            Goto(L15);
S66:
            ForceAnimationPlayback(X12_4, 7000120, false, false, true);
            Goto(L15);
S67:
            ForceAnimationPlayback(X12_4, 8000120, false, false, true);
            Goto(L15);
S68:
            ForceAnimationPlayback(X12_4, 9000120, false, false, true);
            Goto(L15);
S69:
            ForceAnimationPlayback(X12_4, 10000120, false, false, true);
        } else {
L6:
            GotoIf(S79, X8_4 == 10);
            GotoIf(S78, X8_4 == 9);
            GotoIf(S77, X8_4 == 8);
            GotoIf(S76, X8_4 == 7);
            GotoIf(S75, X8_4 == 6);
            GotoIf(S74, X8_4 == 5);
            GotoIf(S73, X8_4 == 4);
            GotoIf(S72, X8_4 == 3);
            GotoIf(S71, X8_4 == 2);
            GotoIf(S70, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 120, false, true, true);
            Goto(L15);
S70:
            ForceAnimationPlayback(X12_4, 1000120, false, true, true);
            Goto(L15);
S71:
            ForceAnimationPlayback(X12_4, 2000120, false, true, true);
            Goto(L15);
S72:
            ForceAnimationPlayback(X12_4, 3000120, false, true, true);
            Goto(L15);
S73:
            ForceAnimationPlayback(X12_4, 4000120, false, true, true);
            Goto(L15);
S74:
            ForceAnimationPlayback(X12_4, 5000120, false, true, true);
            Goto(L15);
S75:
            ForceAnimationPlayback(X12_4, 6000120, false, true, true);
            Goto(L15);
S76:
            ForceAnimationPlayback(X12_4, 7000120, false, true, true);
            Goto(L15);
S77:
            ForceAnimationPlayback(X12_4, 8000120, false, true, true);
            Goto(L15);
S78:
            ForceAnimationPlayback(X12_4, 9000120, false, true, true);
            Goto(L15);
S79:
            ForceAnimationPlayback(X12_4, 10000120, false, true, true);
        }
L15:
        RestartEvent();
    }
L9:
    WaitFor(!EventFlag(X40_4));
    RestartEvent();
});

$Event(90005508, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    if (PlayerIsInOwnWorld()) {
        SetEventFlagID(X24_4, OFF);
    }
    if (EventFlag(X0_4)) {
        if (X8_4 != 10) {
            GotoIf(S8, X8_4 == 9);
            GotoIf(S7, X8_4 == 8);
            GotoIf(S6, X8_4 == 7);
            GotoIf(S5, X8_4 == 6);
            GotoIf(S4, X8_4 == 5);
            GotoIf(S3, X8_4 == 4);
            GotoIf(S2, X8_4 == 3);
            GotoIf(S1, X8_4 == 2);
            GotoIf(S0, X8_4 == 1);
            ForceAnimationPlayback(X12_4, 20, false, false, false);
            Goto(L10);
S0:
            ForceAnimationPlayback(X12_4, 1000020, false, false, false);
            Goto(L10);
S1:
            ForceAnimationPlayback(X12_4, 2000020, false, false, false);
            Goto(L10);
S2:
            ForceAnimationPlayback(X12_4, 3000020, false, false, false);
            Goto(L10);
S3:
            ForceAnimationPlayback(X12_4, 4000020, false, false, false);
            Goto(L10);
S4:
            ForceAnimationPlayback(X12_4, 5000020, false, false, false);
            Goto(L10);
S5:
            ForceAnimationPlayback(X12_4, 6000020, false, false, false);
            Goto(L10);
S6:
            ForceAnimationPlayback(X12_4, 7000020, false, false, false);
            Goto(L10);
S7:
            ForceAnimationPlayback(X12_4, 8000020, false, false, false);
            Goto(L10);
S8:
            ForceAnimationPlayback(X12_4, 9000020, false, false, false);
        } else {
            ForceAnimationPlayback(X12_4, 10000020, false, false, false);
        }
L10:
        SetEventFlagID(X4_4, ON);
        ReproduceAssetAnimation(X16_4, 1);
        EndEvent();
    }
L0:
    GotoIf(S18, X8_4 == 10);
    GotoIf(S17, X8_4 == 9);
    GotoIf(S16, X8_4 == 8);
    GotoIf(S15, X8_4 == 7);
    GotoIf(S14, X8_4 == 6);
    GotoIf(S13, X8_4 == 5);
    GotoIf(S12, X8_4 == 4);
    GotoIf(S11, X8_4 == 3);
    GotoIf(S10, X8_4 == 2);
    GotoIf(S9, X8_4 == 1);
    ForceAnimationPlayback(X12_4, 10, false, false, true);
    Goto(L15);
S9:
    ForceAnimationPlayback(X12_4, 1000010, false, false, true);
    Goto(L15);
S10:
    ForceAnimationPlayback(X12_4, 2000010, false, false, true);
    Goto(L15);
S11:
    ForceAnimationPlayback(X12_4, 3000010, false, false, true);
    Goto(L15);
S12:
    ForceAnimationPlayback(X12_4, 4000010, false, false, true);
    Goto(L15);
S13:
    ForceAnimationPlayback(X12_4, 5000010, false, false, true);
    Goto(L15);
S14:
    ForceAnimationPlayback(X12_4, 6000010, false, false, true);
    Goto(L15);
S15:
    ForceAnimationPlayback(X12_4, 7000010, false, false, true);
    Goto(L15);
S16:
    ForceAnimationPlayback(X12_4, 8000010, false, false, true);
    Goto(L15);
S17:
    ForceAnimationPlayback(X12_4, 9000010, false, false, true);
    Goto(L15);
S18:
    ForceAnimationPlayback(X12_4, 10000010, false, false, true);
L15:
    SetEventFlagID(X4_4, OFF);
    ReproduceAssetAnimation(X20_4, 1);
    EndEvent();
});

$Event(90005510, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4) {
    EndIf(!PlayerIsInOwnWorld());
    if (!EventFlag(X0_4)) {
        WaitFor(PlayerIsInOwnWorld() && ObjActEventFlag(X8_4));
        WaitFixedTimeRealFrames(1);
        DisplayGenericDialog(X16_4, PromptType.OKCANCEL, NumberofOptions.NoButtons, X4_4, 3);
        SetEventFlagID(X0_4, ON);
    }
L0:
    if (X20_4 != 1) {
        DisableObjAct(X4_4, X12_4);
    }
    EndEvent();
});

$Event(90005511, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    if (!EventFlag(X0_4)) {
        WaitFor(ObjActEventFlag(X8_4));
        SetEventFlagID(X0_4, ON);
    }
L0:
    EndIf(X16_4 == 1);
    DisableObjActAssignIdx(X4_4, X12_4, 0);
    DisableObjActAssignIdx(X4_4, X12_4, 1);
    DisableObjActAssignIdx(X4_4, X12_4, 2);
    DisableObjActAssignIdx(X4_4, X12_4, 3);
    EndEvent();
});

$Event(90005512, Default, function(X0_4, X4_4, X8_4) {
    DisableNetworkSync();
    if (!EventFlag(X0_4)) {
        WaitFor(EventFlag(X0_4) || (InArea(10000, X4_4) && PlayerIsInOwnWorld()));
        RestartIf(EventFlag(X0_4));
        SetSpEffect(10000, 4150);
        WaitFixedTimeSeconds(3);
        RestartEvent();
    }
L0:
    WaitFor(InArea(10000, X4_4) || InArea(10000, X8_4));
    SetSpEffect(10000, 4150);
    WaitFixedTimeSeconds(3);
    RestartEvent();
});

$Event(90005513, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    if (EventFlag(X0_4)) {
        DisableObjAct(X8_4, X16_4);
        ReproduceAssetAnimation(X4_4, X24_4);
        EndEvent();
    }
L0:
    WaitFor(!EventFlag(X0_4) && ObjActEventFlag(X12_4));
    SetNetworkconnectedEventFlagID(X0_4, ON);
    DisableObjAct(X8_4, X16_4);
    ForceAnimationPlayback(X4_4, X20_4, false, false, false);
});

$Event(90005515, Default, function(X0_4, X4_4) {
    DisableNetworkSync();
    WaitFor((PlayerIsInOwnWorld() && ActionButtonInArea(7101, X4_4)) || EventFlag(X0_4));
    EndIf(EventFlag(X0_4));
    DisplayGenericDialog(4010, PromptType.OKCANCEL, NumberofOptions.OneButton, X4_4, 3);
    RestartEvent();
});

$Event(90005520, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    if (EventFlag(X0_4)) {
        ReproduceAssetAnimation(X4_4, 2);
        RegisterLadder(X8_4, X12_4, X4_4);
        EndEvent();
    }
L0:
    WaitFor(PlayerIsInOwnWorld() && ActionButtonInArea(9200, X4_4));
    SetNetworkconnectedEventFlagID(X0_4, ON);
    if (PlayerIsInOwnWorld()) {
        RotateCharacter(10000, X4_4, 60210, false);
    }
    ForceAnimationPlayback(X4_4, 1, false, true, false);
    RegisterLadder(X8_4, X12_4, X4_4);
});

$Event(90005525, Restart, function(X0_4, X4_4) {
    if (!EventFlag(X0_4)) {
        WaitFor(PlayerIsInOwnWorld() && HasDamageType(X4_4, 20000, DamageType.Unspecified));
        SetNetworkconnectedEventFlagID(X0_4, ON);
        ForceAnimationPlayback(X4_4, 1, false, true, false);
    }
L0:
    DisableAsset(X4_4);
});

$Event(900055278, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4) {
    if (EventFlag(X0_4)) {
        DisableAsset(X4_4);
        EndEvent();
    }
L0:
    DeleteAssetfollowingSFX(X4_4, true);
    CreateAssetfollowingSFX(X4_4, 101, X8_4);
    onlineAct = PlayerIsInOwnWorld() && ActionButtonInArea(X12_4, X4_4);
    flag = EventFlag(X0_4);
    WaitFor(onlineAct || flag);
    if (!flag.Passed) {
        DisplayGenericDialog(X16_4, PromptType.YESNO, NumberofOptions.NoButtons, X0_4, 3);
        WaitFixedTimeSeconds(1);
        RestartEvent();
    }
L1:
    SetNetworkconnectedEventFlagID(X0_4, ON);
    DeleteAssetfollowingSFX(X4_4, true);
    DisableAsset(X4_4);
    EndEvent();
    EndIf(Signed(X20_4) == 0);
    EndIf(Signed(X24_4) == 0);
    EndIf(Signed(X28_4) == 0);
});

$Event(90005540, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    if (EventFlag(X0_4)) {
        DisableObjAct(X8_4, X16_4);
        ReproduceAssetAnimation(X4_4, X24_4);
        EndEvent();
    }
L0:
    WaitFor(!EventFlag(X0_4) && ObjActEventFlag(X12_4));
    SetNetworkconnectedEventFlagID(X0_4, ON);
    DisableObjAct(X8_4, X16_4);
    ForceAnimationPlayback(X4_4, X20_4, false, false, false);
});

$Event(90005550, Restart, function(X0_4, X4_4, X8_4) {
    if (EventFlag(X0_4)) {
        ReproduceAssetAnimation(X4_4, 1);
        DisableObjAct(X4_4, -1);
        EnableAssetTreasure(X4_4);
        EndEvent();
    }
L0:
    DisableAssetTreasure(X4_4);
    WaitFor(ObjActEventFlag(X8_4));
    WaitFixedTimeFrames(10);
    EnableAssetTreasure(X4_4);
    SetEventFlagID(X0_4, ON);
});

$Event(90005560, Restart, function(X0_4, X4_4, X8_4) {
    if (EventFlag(X0_4)) {
        ReproduceAssetDestruction(X4_4, 1);
        EnableAssetTreasure(X4_4);
        EndEvent();
    }
L0:
    if (Signed(X8_4) == 0) {
        DeleteAssetfollowingSFX(X4_4, true);
        CreateAssetfollowingSFX(X4_4, 200, 803300);
    }
    DisableAssetTreasure(X4_4);
    WaitFor(AssetDestroyed(X4_4, Equal, 1));
    SetNetworkconnectedEventFlagID(X0_4, ON);
    EnableAssetTreasure(X4_4);
    if (Signed(X8_4) == 0) {
        DeleteAssetfollowingSFX(X4_4, true);
    }
});

$Event(90005570, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4) {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(X0_4));
    if (Signed(X16_4) == 3) {
        CreateAssetfollowingSFX(X8_4, 90, 6103);
    } else if (Signed(X16_4) == 2) {
        CreateAssetfollowingSFX(X8_4, 90, 6102);
    } else if (Signed(X16_4) == 1) {
        CreateAssetfollowingSFX(X8_4, 90, 6101);
    } else {
        CreateAssetfollowingSFX(X8_4, 90, 6100);
    }
L1:
    onlineFlagAct &= PlayerIsInOwnWorld() && !EventFlag(X0_4);
    if (Signed(X12_4) == 2) {
        onlineFlagAct &= ActionButtonInArea(4250, X8_4);
    } else if (Signed(X12_4) == 1) {
        onlineFlagAct &= ActionButtonInArea(4300, X8_4);
    } else {
        onlineFlagAct &= ActionButtonInArea(4200, X8_4);
    }
L2:
    WaitFor(onlineFlagAct || EventFlag(X0_4));
    DeleteAssetfollowingSFX(X8_4, true);
    EndIf(EventFlag(X0_4));
    WaitFixedTimeRealFrames(1);
    AwardGesture(X4_4);
    SetEventFlagID(X0_4, ON);
    EndIf(Signed(0) == X20_4);
});

$Event(900005571, Default, function(X0_4, X4_4, X8_4, X12_4) {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(X0_4));
    WaitFor(PlayerIsInOwnWorld() && EventFlag(X8_4));
    AwardGesture(X4_4);
    SetEventFlagID(X0_4, ON);
    EndIf(Signed(0) == X12_4);
});

$Event(90005600, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    RegisterBonfire(X0_4, X4_4, 0, 0, 0, X8_4);
    if (0 != X12_4) {
        DisableCharacterCollision(X12_4);
    }
    if (!EventFlag(X0_4)) {
        WaitFor(
            PlayerIsInOwnWorld() && EntityInRadiusOfEntity(10000, X4_4, 5, 1) && EventFlag(X0_4));
        EndIf(0 == X12_4);
        DisableCharacterCollision(X12_4);
        SetSpEffect(X12_4, 530);
        WaitFixedTimeSeconds(1.5);
    }
L0:
    DisableCharacter(X12_4);
});

$Event(90005605, Restart, function(X0_4, X4_1, X5_1, X6_1, X7_1, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4, X40_4) {
    EndIf(!PlayerIsInOwnWorld());
    SetEventFlagID(X20_4, OFF);
    SetEventFlagID(X24_4, OFF);
    if (!ThisEventSlot()) {
        DeleteAssetfollowingSFX(X0_4, true);
        SetEventFlagID(X16_4, OFF);
        WaitFixedTimeFrames(1);
    }
    onlineFlag |= HasMultiplayerState(MultiplayerState.Multiplayer)
        || HasMultiplayerState(MultiplayerState.MultiplayerPending);
    if (X28_4 != 0) {
        onlineFlag |= !EventFlag(X28_4);
    }
    if (!onlineFlag) {
        if (!EventFlag(X16_4)) {
            CreateAssetfollowingSFX(X0_4, 200, 806870);
            SetEventFlagID(X16_4, ON);
        }
    }
L1:
    onlineFlagAct &= PlayerIsInOwnWorld()
        && !(HasMultiplayerState(MultiplayerState.Multiplayer)
            || HasMultiplayerState(MultiplayerState.MultiplayerPending));
    if (X28_4 != 0) {
        if (Signed(X32_4) == 0) {
            onlineFlagAct &= EventFlag(X28_4) && EventFlag(X16_4);
        }
    }
    onlineFlagAct &= ActionButtonInArea(9140, X0_4);
    onlineFlag2 |= HasMultiplayerState(MultiplayerState.Multiplayer)
        || HasMultiplayerState(MultiplayerState.MultiplayerPending);
    if (X28_4 != 0) {
        onlineFlag2 |= !EventFlag(X28_4);
    }
    onlineFlag3 = onlineFlag2 && EventFlag(X16_4);
    onlineFlag4 |= HasMultiplayerState(MultiplayerState.Multiplayer)
        || HasMultiplayerState(MultiplayerState.MultiplayerPending);
    if (X28_4 != 0) {
        onlineFlag4 |= !EventFlag(X28_4);
    }
    onlineFlag5 = !onlineFlag4 && !EventFlag(X16_4);
    flag = EventFlagState(CHANGE, TargetEventFlagType.EventFlag, X28_4);
    onlineFlagAct2 |= onlineFlagAct || onlineFlag3 || onlineFlag5;
    if (X28_4 != 0) {
        onlineFlagAct2 |= flag;
    }
    WaitFor(onlineFlagAct2);
    if (!onlineFlagAct.Passed) {
        if (onlineFlag3.Passed) {
            DeleteAssetfollowingSFX(X0_4, true);
            SetEventFlagID(X16_4, OFF);
        }
L2:
        WaitFixedTimeSeconds(0.033);
        RestartEvent();
    }
L3:
    if (!(X28_4 == 0 || Signed(X32_4) == 0)) {
        if (!EventFlag(X28_4)) {
            DisplayGenericDialog(X32_4, PromptType.YESNO, NumberofOptions.NoButtons, X0_4, 3);
            WaitFixedTimeSeconds(1);
            RestartEvent();
        }
    }
L4:
    DisplayGenericDialogAndSetEventFlags(4300, PromptType.YESNO, NumberofOptions.TwoButtons, X0_4, 3, X20_4, X24_4, X24_4);
    if (!EventFlag(X20_4)) {
        WaitFixedTimeSeconds(1);
        RestartEvent();
    }
L6:
    RestartIf(
        HasMultiplayerState(MultiplayerState.Multiplayer)
            || HasMultiplayerState(MultiplayerState.MultiplayerPending));
    RotateCharacter(10000, X0_4, -1, true);
    ForceAnimationPlayback(10000, 60490, false, false, false);
    WaitFixedTimeSeconds(3);
    WarpPlayer(X4_1, X5_1, X6_1, X7_1, X8_4, X12_4);
    RestartEvent();
    WaitFixedTimeSeconds(X36_4);
    WaitFixedTimeSeconds(X40_4);
});

$Event(900005610, Default, function(X0_4, X4_4, X8_4, X12_4) {
    DisableNetworkSync();
    DeleteAssetfollowingSFX(X0_4, true);
    if (0 != X12_4) {
        flagChr &= EventFlag(X12_4);
    }
    flagChr &= CharacterRidingMount(10000);
    WaitFor(flagChr);
    CreateAssetfollowingSFX(X0_4, X4_4, X8_4);
    if (0 != X12_4) {
        flagChr2 |= !EventFlag(X12_4);
    }
    flagChr2 |= !CharacterRidingMount(10000);
    WaitFor(flagChr2);
    RestartEvent();
});

$Event(90005616, Default, function(X0_4, X4_4) {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(X0_4));
    WaitFor(PlayerIsInOwnWorld() && !EventFlag(X0_4) && EventFlag(400239) && InArea(10000, X4_4));
    DisplayBlinkingMessage(20600);
});

// Stonesword Key - Remove Dog
$Event(90005620, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    DisableNetworkSync();
    if (EventFlag(X0_4)) {
        EndEvent();
    }
L0:
    SetEventFlagID(X16_4, OFF);
    SetEventFlagID(X20_4, OFF);
    DeleteAssetfollowingSFX(X4_4, true);
    CreateAssetfollowingSFX(X4_4, 200, 806040);
    if (X12_4 != 0) {
        CreateAssetfollowingSFX(X4_4, 201, 806040);
    }
    DisableAsset(X8_4);
    if (X12_4 != 0) {
        DisableAsset(X12_4);
    }
    WaitFor((PlayerIsInOwnWorld() && ActionButtonInArea(9220, X4_4)) || EventFlag(X0_4));
    if (!EventFlag(X0_4)) {
        DisplayGenericDialogAndSetEventFlags(108000, PromptType.YESNO, NumberofOptions.TwoButtons, X4_4, 1.75, X16_4, X20_4, X20_4);
        if (!EventFlag(X16_4)) {
            WaitFixedTimeSeconds(0.5);
            RestartEvent();
        }
L1:
        StoreItemAmountHeldInEventValue(ItemType.Goods, 8000, 9580, 8);
        GotoIf(L2, X12_4 != 0);
        GotoIf(L3, EventValue(9580, 8) >= 1);
L2:
        GotoIf(L4, EventValue(9580, 8) >= 2);
        ForceAnimationPlayback(10000, 50050, false, false, false);
        WaitFixedTimeSeconds(1.4);
        if (EventValue(9580, 8) < 1) {
            DisplayGenericDialog(308000, PromptType.OKCANCEL, NumberofOptions.NoButtons, X4_4, 3);
            RestartEvent();
        }
L5:
        DisplayGenericDialog(408000, PromptType.OKCANCEL, NumberofOptions.NoButtons, X4_4, 3);
        RestartEvent();
L3:
        IssueShortWarpRequest(10000, TargetEntityType.Asset, X4_4, 191);
        ForceAnimationPlayback(10000, 60810, false, false, false);
        WaitFixedTimeSeconds(2.7);
        DisplayGenericDialog(208000, PromptType.OKCANCEL, NumberofOptions.NoButtons, X4_4, 3);
        EnableAsset(X8_4);
        RemoveItemFromPlayer(ItemType.Goods, 8000, 1);
        SetNetworkconnectedEventFlagID(X0_4, ON);
        Goto(L8);
L4:
        IssueShortWarpRequest(10000, TargetEntityType.Asset, X4_4, 191);
        ForceAnimationPlayback(10000, 60810, false, false, false);
        WaitFixedTimeSeconds(2.67);
        EnableAsset(X8_4);
        ForceAnimationPlayback(10000, 60811, false, false, false);
        WaitFixedTimeSeconds(1.5);
        DisplayGenericDialog(208000, PromptType.OKCANCEL, NumberofOptions.NoButtons, X4_4, 3);
        EnableAsset(X12_4);
        RemoveItemFromPlayer(ItemType.Goods, 8000, 2);
        SetNetworkconnectedEventFlagID(X0_4, ON);
    } else {
L9:
        EnableAsset(X8_4);
        EnableAsset(X12_4);
    }
L8:
    DeleteAssetfollowingSFX(X4_4, true);
    EndEvent();
    EndIf(Signed(0) == X24_4);
});

// Stonesword Key - Unlock Door automatically if unlocked previously
$Event(90005621, Default, function(X0_4, X4_4) {
    if (EventFlag(X0_4)) {
        DisableAsset(X4_4);
        EndEvent();
    }
L0:
    CreateAssetfollowingSFX(X4_4, 101, 806042);
    WaitFor(PlayerIsInOwnWorld() && EventFlag(X0_4));
    DeleteAssetfollowingSFX(X4_4, true);
    PlaySE(X4_4, SoundType.SFX, 90011);
    WaitFixedTimeSeconds(0.5);
    DisableAsset(X4_4);
});

$Event(90005630, Restart, function(X0_4, X4_4, X8_4) {
    DisableNetworkSync();
    WaitFor(PlayerIsInOwnWorld() && ActionButtonInArea(9270, X4_4));
    UseFarviewCamera(X0_4, X4_4, X8_4);
    RotateCharacter(10000, X4_4, -1, true);
    RotateCharacter(10000, X4_4, 60480, false);
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

$Event(90005631, Restart, function(X0_4, X4_4) {
    DisableNetworkSync();
    WaitFor(ActionButtonInArea(9330, X0_4));
    DisplayGenericDialog(X4_4, PromptType.YESNO, NumberofOptions.NoButtons, X0_4, 3);
    WaitFixedTimeSeconds(2);
    RestartEvent();
});

$Event(90005632, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(EventFlag(X0_4));
    EndIf(!PlayerIsInOwnWorld());
    DeleteAssetfollowingSFX(X4_4, false);
    CreateAssetfollowingSFX(X4_4, 200, 806840);
    WaitFor(PlayerIsInOwnWorld() && ActionButtonInArea(9310, X4_4));
    DeleteAssetfollowingSFX(X4_4, true);
    PlaySE(X4_4, SoundType.SFX, 806841);
    WaitFixedTimeSeconds(0.1);
    AwardItemsIncludingClients(X8_4);
});

$Event(90005633, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    SetSpEffect(X0_4, 10124);
    DisableCharacter(X8_4);
    DisableCharacterCollision(X8_4);
    DisableAsset(X20_4);
    DisableAsset(X24_4);
    DisableAssetTreasure(X24_4);
    EndIf(EventFlag(X0_4));
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(PlayerIsInOwnWorld() && EventFlag(X4_4) && EntityInRadiusOfEntity(X8_4, 10000, 15, 1));
    EnableCharacter(X8_4);
    ClearSpEffect(X0_4, 10124);
    ForceAnimationPlayback(X8_4, X12_4, false, false, false);
    EnableAsset(X20_4);
    EnableAsset(X24_4);
    ForceAnimationPlayback(X20_4, 2, false, false, false);
    WaitFor(PlayerIsInOwnWorld() && EventFlag(X4_4) && EntityInRadiusOfEntity(X8_4, 10000, 5, 1));
    ForceAnimationPlayback(X8_4, X16_4, false, false, false);
    ForceAnimationPlayback(X20_4, 1, false, false, false);
    WaitFixedTimeSeconds(3.8);
    DisableCharacter(X8_4);
    DisableAsset(X20_4);
    EnableAssetTreasure(X24_4);
});

$Event(90005636, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4) {
    if (EventFlag(X0_4)) {
        DisableCharacter(X4_4);
        DisableCharacterCollision(X4_4);
        EndEvent();
    }
L0:
    if (!EventFlag(X24_4)) {
        DisableCharacter(X4_4);
        DisableCharacterCollision(X4_4);
        DisableCharacterAI(X4_4);
    }
L1:
    onlineFlag = PlayerIsInOwnWorld() && EventFlag(X0_4);
    flagArea = EventFlag(X24_4) && InArea(X4_4, X20_4);
    onlineFlagAreaAct |= onlineFlag || flagArea;
    onlineFlagAreaAct2 &= PlayerIsInOwnWorld() && !EventFlag(X0_4);
    if (EventFlag(X24_4)) {
        onlineFlagAreaAct2 &= !EntityInRadiusOfEntity(10000, X4_4, 30, 1);
    }
    onlineFlagAreaAct2 &= ActionButtonInArea(9300, X8_4);
    onlineFlagAreaAct |= onlineFlagAreaAct2;
    WaitFor(onlineFlagAreaAct);
    if (EventFlag(X24_4)) {
        SpawnOneshotSFX(TargetEntityType.Character, X4_4, 905, 643041);
        SpawnOneshotSFX(TargetEntityType.Character, X4_4, 960, 643040);
        WaitFixedTimeSeconds(0.2);
        DisableCharacter(X4_4);
        DisableCharacterAI(X4_4);
        if (flagArea.Passed) {
            WarpCharacterAndCopyFloor(X4_4, TargetEntityType.Area, X16_4, -1, 10000);
            WaitFixedTimeSeconds(0.1);
        }
L2:
        GotoIf(L3, !onlineFlagAreaAct2.Passed);
    }
L1:
    if (!EventFlag(X24_4)) {
        SetNetworkconnectedEventFlagID(X24_4, ON);
    }
    WarpCharacterAndCopyFloor(X4_4, TargetEntityType.Area, X16_4, -1, 10000);
    if (0 != X28_4) {
        ChangeCharacterPatrolBehavior(X4_4, X28_4);
    }
    WaitFixedTimeFrames(1);
    EnableCharacter(X4_4);
    DisableCharacterCollision(X4_4);
    ForceAnimationPlayback(X4_4, 20028, false, false, false);
    WaitFixedTimeSeconds(0.5);
    EnableCharacterAI(X4_4);
    SetSpEffect(X4_4, X12_4);
L3:
    RestartEvent();
    EndIf(Signed(0) == X32_4);
});

$Event(90005637, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(EventFlag(X0_4));
    WaitFor(EventFlag(X0_4) || InArea(X4_4, X8_4));
    EndIf(EventFlag(X0_4));
    SetSpEffect(X4_4, 4463);
    WaitFixedTimeSeconds(3);
    RestartEvent();
});

$Event(90005640, Restart, function(X0_4, X4_4) {
    if (EventFlag(X0_4)) {
        WaitFor(AssetBackread(X4_4, Equal, 1));
        ReproduceAssetAnimation(X4_4, 2);
        EndEvent();
    }
L0:
    WaitFor(AssetBackread(X4_4, Equal, 1) && EntityInRadiusOfEntity(10000, X4_4, 50, 1));
    SetEventFlagID(X0_4, ON);
    ForceAnimationPlayback(X4_4, 1, false, false, false);
});

$Event(90005645, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_1, X21_1, X22_1, X23_1) {
    if (!EventFlag(X0_4)) {
        DisableAsset(X12_4);
        WaitFor(
            PlayerIsInOwnWorld() && !EntityInRadiusOfEntity(10000, X12_4, 1, 1) && EventFlag(X0_4));
    }
L0:
    EnableAsset(X12_4);
    WaitFor(
        !(HasMultiplayerState(MultiplayerState.MultiplayerPending)
            || HasMultiplayerState(MultiplayerState.Multiplayer))
            && ActionButtonInArea(9290, X12_4));
    DisplayGenericDialogAndSetEventFlags(4100, PromptType.YESNO, NumberofOptions.TwoButtons, X12_4, 3, X4_4, X8_4, X8_4);
    if (!EventFlag(X4_4)) {
        SetEventFlagID(X8_4, ON);
        WaitFixedTimeSeconds(2);
        RestartEvent();
    }
L1:
    WaitFixedTimeSeconds(1);
    WarpPlayer(X20_1, X21_1, X22_1, X23_1, X16_4, 0);
});

$Event(90005646, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_1, X21_1, X22_1, X23_1) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(PlayerIsInOwnWorld() && EventFlag(X0_4));
    if (!ThisEventSlot()) {
        CreateAssetfollowingSFX(X12_4, 190, 1300);
    }
    WaitFor(
        !(HasMultiplayerState(MultiplayerState.MultiplayerPending)
            || HasMultiplayerState(MultiplayerState.Multiplayer))
            && ActionButtonInArea(9290, X12_4));
    DisplayGenericDialogAndSetEventFlags(4100, PromptType.YESNO, NumberofOptions.TwoButtons, X12_4, 3, X4_4, X8_4, X8_4);
    if (!EventFlag(X4_4)) {
        SetEventFlagID(X8_4, ON);
        WaitFixedTimeSeconds(2);
        RestartEvent();
    }
L1:
    ForceAnimationPlayback(10000, 60460, false, false, false);
    WaitFixedTimeSeconds(2.5);
    WarpPlayer(X20_1, X21_1, X22_1, X23_1, X16_4, 0);
});

$Event(90005650, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    if (EventFlag(X0_4)) {
        ReproduceAssetAnimation(X4_4, 2);
        DisableObjAct(X8_4, X16_4);
        EndEvent();
    }
L0:
    WaitFor(PlayerIsInOwnWorld() && ObjActEventFlag(X12_4));
    SetNetworkconnectedEventFlagID(X0_4, ON);
    if (PlayerIsInOwnWorld()) {
        DisplayGenericDialog(4200, PromptType.OKCANCEL, NumberofOptions.NoButtons, X8_4, 5);
    } else {
        DisplayBlinkingMessage(4200);
    }
    ForceAnimationPlayback(X4_4, 1, false, false, false);
    EndEvent();
});

$Event(90005652, Default, function(X0_4, X4_4, X8_4) {
    if (EventFlag(X0_4)) {
        ReproduceAssetAnimation(X4_4, 2);
        EndEvent();
    }
L0:
    WaitFor(PlayerIsInOwnWorld() && EventFlag(X8_4));
    SetNetworkconnectedEventFlagID(X0_4, ON);
    DisplayGenericDialog(4200, PromptType.OKCANCEL, NumberofOptions.NoButtons, 0, 5);
    ForceAnimationPlayback(X4_4, 1, false, false, false);
    EndEvent();
});

$Event(90005651, Default, function(X0_4, X4_4) {
    DisableNetworkSync();
    WaitFor(ActionButtonInArea(7200, X4_4) || EventFlag(X0_4));
    EndIf(EventFlag(X0_4));
    DisplayGenericDialog(4001, PromptType.OKCANCEL, NumberofOptions.NoButtons, X4_4, 3);
    WaitFixedTimeFrames(1);
    RestartEvent();
});

$Event(90005660, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    CreateBulletOwner(X0_4);
    WaitFor(InArea(10000, X8_4));
    ForceAnimationPlayback(X4_4, 1, false, true, false);
    WaitFixedTimeSeconds(0.5);
    if (Signed(X12_4) != 0) {
        ShootBullet(X0_4, X16_4, -1, X12_4, 0, 0, 0);
        ShootBullet(X0_4, X20_4, -1, X12_4, 0, 0, 0);
        ShootBullet(X0_4, X24_4, -1, X12_4, 0, 0, 0);
    } else {
        ShootBullet(X0_4, X16_4, -1, 102000, 0, 0, 0);
        ShootBullet(X0_4, X20_4, -1, 102000, 0, 0, 0);
        ShootBullet(X0_4, X24_4, -1, 102000, 0, 0, 0);
    }
    WaitFixedTimeSeconds(0.6);
    if (Signed(X12_4) != 0) {
        ShootBullet(X0_4, X16_4, -1, X12_4, 0, 0, 0);
        ShootBullet(X0_4, X20_4, -1, X12_4, 0, 0, 0);
        ShootBullet(X0_4, X24_4, -1, X12_4, 0, 0, 0);
    } else {
        ShootBullet(X0_4, X16_4, -1, 102000, 0, 0, 0);
        ShootBullet(X0_4, X20_4, -1, 102000, 0, 0, 0);
        ShootBullet(X0_4, X24_4, -1, 102000, 0, 0, 0);
    }
    WaitFixedTimeSeconds(0.6);
    if (Signed(X12_4) != 0) {
        ShootBullet(X0_4, X16_4, -1, X12_4, 0, 0, 0);
        ShootBullet(X0_4, X20_4, -1, X12_4, 0, 0, 0);
        ShootBullet(X0_4, X24_4, -1, X12_4, 0, 0, 0);
    } else {
        ShootBullet(X0_4, X16_4, -1, 102000, 0, 0, 0);
        ShootBullet(X0_4, X20_4, -1, 102000, 0, 0, 0);
        ShootBullet(X0_4, X24_4, -1, 102000, 0, 0, 0);
    }
    WaitFixedTimeSeconds(3);
    WaitFor(!AllPlayersInArea(X8_4));
    ForceAnimationPlayback(X4_4, 3, false, true, false);
    RestartEvent();
});

$Event(90005670, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    if (!EventFlag(X4_4)) {
        WaitFor(
            ((CharacterType(10000, TargetType.Alive)
                || CharacterType(10000, TargetType.BluePhantom)
                || CharacterType(10000, TargetType.WhitePhantom))
                && InArea(10000, X16_4)
                && !EventFlag(X0_4))
                || EventFlag(X4_4));
        if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
            SetNetworkconnectedEventFlagID(X0_4, ON);
        }
        ForceAnimationPlayback(X12_4, 12, false, true, false);
    }
L0:
    GotoIf(L10, !AllPlayersInArea(X20_4));
    GotoIf(S0, 0 == X24_4);
    GotoIf(L10, !EventFlag(X24_4));
S0:
    if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
        SetNetworkconnectedEventFlagID(X4_4, ON);
    }
    SetEventFlagID(X8_4, ON);
    ForceAnimationPlayback(X12_4, 20, false, true, false);
    RestartEvent();
L10:
    WaitFixedTimeSeconds(0.1);
    if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
        SetNetworkconnectedEventFlagID(X4_4, OFF);
    }
    ForceAnimationPlayback(X12_4, 21, false, true, false);
    if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
        SetNetworkconnectedEventFlagID(X0_4, OFF);
        ForceAnimationPlayback(X12_4, 10, false, false, false);
    } else {
        ForceAnimationPlayback(X12_4, 10, false, true, false);
    }
    RestartEvent();
});

$Event(90005673, Default, function(X0_4, X4_4) {
    WaitFor(
        (CharacterType(10000, TargetType.Alive)
            || CharacterType(10000, TargetType.WhitePhantom)
            || CharacterType(10000, TargetType.BluePhantom))
            && InArea(10000, X4_4));
    if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
        SetNetworkconnectedEventFlagID(X0_4, ON);
    }
    chrArea = (CharacterType(10000, TargetType.BlackPhantom)
        || CharacterType(10000, TargetType.Invader)
        || CharacterType(10000, TargetType.Invader2)
        || CharacterType(10000, TargetType.Invader3))
        && InArea(10000, X4_4);
    WaitFor(chrArea || !AllPlayersInArea(X4_4));
    if (chrArea.Passed) {
        WaitFixedTimeSeconds(1);
    }
    if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
        SetNetworkconnectedEventFlagID(X0_4, OFF);
    }
    RestartEvent();
});

$Event(90005671, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    DisableNetworkSync();
    WaitFor(EventFlag(X0_4) && InArea(10000, X8_4) && CharacterHasSpEffect(10000, 4195));
    WarpAssetToCharacter(X4_4, 10000, 93);
    WaitFixedTimeFrames(1);
    CreateDamagingAsset(X8_4, X4_4, X12_4, X16_4, DamageTargetType.Character, 2, 0.1, 0);
    WaitFixedTimeFrames(1);
    DeleteAssetEvent(X4_4);
    WaitFixedTimeSeconds(0.5);
    RestartEvent();
});

$Event(90005672, Default, function(X0_4, X4_4) {
    WaitFor(EventFlag(X0_4) && InArea(10000, X4_4));
    SetSpEffect(10000, 4195);
    WaitFixedTimeSeconds(0.5);
    RestartEvent();
});

$Event(90005675, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    if (MapHasPermissionToUpdate(false, 0, 0, 0, 0) && EventFlag(X0_4)) {
        SetNetworkconnectedEventFlagID(X0_4, OFF);
        SetThisEventSlot(OFF);
    }
L10:
    WaitFor((InArea(10000, X12_4) || ThisEventSlot()) && !EventFlag(X0_4));
    if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
        SetNetworkconnectedEventFlagID(X0_4, ON);
    }
    if (!ThisEventSlot()) {
        WaitFixedTimeSeconds(X20_4);
    }
    if (Signed(1) != X24_4) {
        ForceAnimationPlayback(X8_4, 1, false, false, false);
    } else {
        ForceAnimationPlayback(X8_4, 2, false, false, false);
    }
    if (Signed(X16_4) != 0) {
        CreateBigDamagingAsset(X4_4, X8_4, 30, 31, X16_4, DamageTargetType.Character, 0.1, 1, 0);
    } else {
        CreateBigDamagingAsset(X4_4, X8_4, 30, 31, 103000, DamageTargetType.Character, 0.1, 1, 0);
    }
    WaitFixedTimeSeconds(1);
    DeleteAssetEvent(X4_4);
    WaitFixedTimeSeconds(4.1);
    WaitFixedTimeSeconds(0.1);
    if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
        SetNetworkconnectedEventFlagID(X0_4, OFF);
    }
    RestartEvent();
});

$Event(90005680, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
        SetEventFlagID(X12_4, OFF);
    }
    WaitFor(AssetBackread(X16_4, Equal, 1));
    if (EventFlag(X0_4)) {
        ForceAnimationPlayback(X16_4, 20, false, false, false);
        SetEventFlagID(X4_4, ON);
        SetEventFlagID(X8_4, ON);
        EndEvent();
    }
L0:
    ForceAnimationPlayback(X16_4, 10, false, false, false);
    SetEventFlagID(X4_4, OFF);
    SetEventFlagID(X8_4, OFF);
    EndEvent();
});

$Event(90005681, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    if (!(((EventFlag(X0_4) && EventFlag(X4_4)) || (!EventFlag(X0_4) && !EventFlag(X4_4)))
        && EventFlag(X12_4))) {
        if (EventFlag(X0_4)) {
            WaitFor(
                !EventFlag(X0_4)
                    || (EventFlag(X4_4) && HasDamageType(X16_4, 20000, DamageType.Unspecified)));
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                SetNetworkconnectedEventFlagID(X0_4, OFF);
                SetNetworkconnectedEventFlagID(X12_4, ON);
            }
            SetEventFlagID(X4_4, OFF);
            SetEventFlagID(X8_4, OFF);
            ForceAnimationPlayback(X16_4, 21, false, true, false);
            if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
                SetNetworkconnectedEventFlagID(X12_4, OFF);
            }
            RestartEvent();
        }
L0:
        WaitFor(
            EventFlag(X0_4)
                || (!EventFlag(X4_4) && HasDamageType(X16_4, 20000, DamageType.Unspecified)));
        if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
            SetNetworkconnectedEventFlagID(X0_4, ON);
            SetNetworkconnectedEventFlagID(X12_4, ON);
        }
        SetEventFlagID(X4_4, ON);
        ForceAnimationPlayback(X16_4, 12, false, true, false);
        if (MapHasPermissionToUpdate(false, 0, 0, 0, 0)) {
            SetNetworkconnectedEventFlagID(X12_4, OFF);
        }
        SetEventFlagID(X8_4, ON);
        RestartEvent();
    }
L9:
    WaitFor(!EventFlag(X12_4));
    RestartEvent();
});

$Event(90005682, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4) {
    flagArea &= EventFlag(X0_4);
    if (X8_4 != 0) {
        flagArea &= InArea(10000, X8_4);
    }
    WaitFor(flagArea);
    CreateBulletOwner(X12_4);
    if (Signed(X24_4) != 0) {
        if (Signed(X16_4) != 0) {
            ShootBullet(X12_4, X4_4, X24_4, X16_4, 0, 0, 0);
        } else {
            ShootBullet(X12_4, X4_4, X24_4, 101100, 0, 0, 0);
        }
        if (Signed(X20_4) != 0) {
            ShootBullet(X12_4, X4_4, X24_4, X20_4, 0, 0, 0);
        } else {
            ShootBullet(X12_4, X4_4, X24_4, 101102, 0, 0, 0);
        }
    }
L1:
    if (Signed(X28_4) != 0) {
        if (Signed(X16_4) != 0) {
            ShootBullet(X12_4, X4_4, X28_4, X16_4, 0, 0, 0);
        } else {
            ShootBullet(X12_4, X4_4, X28_4, 101100, 0, 0, 0);
        }
        if (Signed(X20_4) != 0) {
            ShootBullet(X12_4, X4_4, X28_4, X20_4, 0, 0, 0);
        } else {
            ShootBullet(X12_4, X4_4, X28_4, 101102, 0, 0, 0);
        }
    }
L2:
    if (Signed(X32_4) != 0) {
        if (Signed(X16_4) != 0) {
            ShootBullet(X12_4, X4_4, X32_4, X16_4, 0, 0, 0);
        } else {
            ShootBullet(X12_4, X4_4, X32_4, 101100, 0, 0, 0);
        }
        if (Signed(X20_4) != 0) {
            ShootBullet(X12_4, X4_4, X32_4, X20_4, 0, 0, 0);
        } else {
            ShootBullet(X12_4, X4_4, X32_4, 101102, 0, 0, 0);
        }
    }
L3:
    if (Signed(X36_4) != 0) {
        if (Signed(X16_4) != 0) {
            ShootBullet(X12_4, X4_4, X36_4, X16_4, 0, 0, 0);
        } else {
            ShootBullet(X12_4, X4_4, X36_4, 101100, 0, 0, 0);
        }
        if (Signed(X20_4) != 0) {
            ShootBullet(X12_4, X4_4, X36_4, X20_4, 0, 0, 0);
        } else {
            ShootBullet(X12_4, X4_4, X36_4, 101102, 0, 0, 0);
        }
    }
L4:
    WaitFixedTimeSeconds(7.2);
    RestartEvent();
});

$Event(90005683, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    DisableNetworkSync();
    if (EventFlag(X0_4)) {
        DeleteAssetfollowingSFX(X4_4, true);
        SetEventFlagID(X12_4, OFF);
        SetEventFlagID(X16_4, OFF);
        EndEvent();
    }
L0:
    if (!EventFlag(X12_4)) {
        WaitFor(ActionButtonInArea(9260, X4_4));
        DisplayGenericDialog(4210, PromptType.OKCANCEL, NumberofOptions.NoButtons, X4_4, 3);
        SetEventFlagID(X12_4, ON);
        SetEventFlagID(X16_4, ON);
    }
L1:
    if (1049551600 != X4_4) {
        CreateAssetfollowingSFX(X4_4, X8_4, 800530);
    } else {
L10:
        CreateAssetfollowingSFX(X4_4, X8_4, 800531);
    }
L1:
    WaitFor(EventFlag(X0_4));
    RestartEvent();
    CreateAssetfollowingSFX(X4_4, X8_4, 800530);
});

$Event(90005684, Default, function(X0_4) {
    DisableNetworkSync();
    WaitFor(ActionButtonInArea(9260, X0_4));
    DisplayGenericDialog(4210, PromptType.OKCANCEL, NumberofOptions.NoButtons, X0_4, 3);
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

$Event(90005685, Default, function(X0_4) {
    EnableCharacterImmortality(X0_4);
    DisableCharacterInvincibility(X0_4);
    DisableLockOnPoint(X0_4, 220);
    DisableCharacterHPBarDisplay(X0_4);
    SetSpEffect(X0_4, 5000);
    SetNetworkUpdateRate(X0_4, true, CharacterUpdateFrequency.AlwaysUpdate);
});

$Event(90005686, Default, function(X0_4, X4_4) {
    WaitFor(EventFlag(X4_4));
    ShootBullet(X0_4, X0_4, 10, 244600980, 0, 0, 0);
    ShootBullet(X0_4, X0_4, 15, 244600980, 0, 0, 0);
    ShootBullet(X0_4, X0_4, 20, 244600981, 0, 0, 0);
    ShootBullet(X0_4, X0_4, 25, 244600981, 0, 0, 0);
    ShootBullet(X0_4, X0_4, 30, 244600981, 0, 0, 0);
    WaitFixedTimeFrames(1);
    RestartEvent();
});

$Event(90005687, Default, function(X0_4, X4_4, X8_4) {
    EndIf(ThisEventSlot());
    WaitFor(InArea(10000, X8_4));
    ChangeCharacterPatrolBehavior(X0_4, X4_4);
    WaitFixedTimeFrames(1);
});

$Event(90005688, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    WaitFor(InArea(X0_4, X4_4));
    GotoIf(L1, InArea(10000, X12_4));
    GotoIf(S0, 0 == X20_4);
    GotoIf(L2, InArea(10000, X20_4));
S0:
    ChangeCharacterPatrolBehavior(X0_4, X8_4);
    Goto(L20);
L1:
    ChangeCharacterPatrolBehavior(X0_4, X16_4);
    Goto(L20);
L2:
    ChangeCharacterPatrolBehavior(30090400, X24_4);
    Goto(L20);
L20:
    WaitFor(!InArea(X0_4, X4_4));
    RestartEvent();
});

$Event(90005690, Restart, function(X0_4) {
    DisableNetworkSync();
    WaitFor(InArea(10000, X0_4));
    SetSpEffect(10000, 4080);
    WaitFor(!InArea(10000, X0_4));
    ClearSpEffect(10000, 4080);
    RestartEvent();
});

$Event(90005691, Restart, function(X0_4) {
    DisableNetworkSync();
    WaitFor(InArea(10000, X0_4));
    SetSpEffect(10000, 4085);
    WaitFor(!InArea(10000, X0_4));
    ClearSpEffect(10000, 4085);
    RestartEvent();
});

$Event(90005694, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4) {
    DeleteAssetEvent(X0_4);
    if (Signed(0) == X12_4) {
        CreateDamagingAsset(X0_4, X4_4, X8_4, X16_4, DamageTargetType.Character, X20_4, X24_4, X28_4);
    } else {
        CreateBigDamagingAsset(X0_4, X4_4, X8_4, X12_4, X16_4, DamageTargetType.Character, X20_4, X24_4, X28_4);
    }
});

$Event(90005695, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4) {
    DeleteAssetEvent(X0_4);
    EndIf(AssetDestroyed(X4_4, Equal, 1));
    if (Signed(0) == X12_4) {
        CreateDamagingAsset(X0_4, X4_4, X8_4, X16_4, DamageTargetType.Character, X20_4, X24_4, X28_4);
    } else {
        CreateBigDamagingAsset(X0_4, X4_4, X8_4, X12_4, X16_4, DamageTargetType.Character, X20_4, X24_4, X28_4);
    }
    WaitFor(AssetDestroyed(X0_4, Equal, 1));
    DeleteAssetEvent(X0_4);
});

$Event(90005700, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(!EventFlag(3000));
    EndIf(EventFlag(X4_4));
    EndIf(EventFlag(X8_4));
    SetEventFlagID(X12_4, OFF);
    WaitFor(
        !EventFlag(X4_4)
            && !EventFlag(X8_4)
            && HPRatio(X0_4) > 0
            && (((HasDamageType(X0_4, 10000, DamageType.Unspecified)
                || HasDamageType(X0_4, 40000, DamageType.Unspecified)
                || CharacterHasSpEffect(X0_4, 1650000))
                && HPRatio(X0_4) < X16_4)
                || CharacterHasSpEffect(X0_4, 9641)
                || EventFlag(X12_4)));
    EndIf(EventFlag(X4_4));
    EndIf(EventFlag(X8_4));
    SetCharacterTeamType(X0_4, TeamType.HostileNPC);
    SetSpEffect(X0_4, 9628);
    SetSpEffect(X0_4, 9635);
    if (Signed(1) != X28_4) {
        BatchSetNetworkconnectedEventFlags(X20_4, X24_4, OFF);
        SetNetworkconnectedEventFlagID(X4_4, ON);
    } else {
L0:
        BatchSetNetworkconnectedEventFlags(X20_4, X24_4, OFF);
        SetNetworkconnectedEventFlagID(X8_4, ON);
    }
L9:
    SaveRequest();
});

$Event(90005701, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(!EventFlag(3000));
    WaitFixedTimeFrames(1);
    WaitFor(!EventFlag(X4_4) && !EventFlag(X8_4));
    GotoIf(L0, Signed(9) == X16_4);
    GotoIf(L1, Signed(8) == X16_4);
    GotoIf(L2, Signed(7) == X16_4);
    GotoIf(L3, Signed(6) == X16_4);
    GotoIf(L4, Signed(5) == X16_4);
    GotoIf(L5, Signed(4) == X16_4);
    GotoIf(L6, Signed(3) == X16_4);
    GotoIf(L7, Signed(2) == X16_4);
    GotoIf(L8, Signed(1) == X16_4);
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified));
    WaitFixedTimeFrames(1);
L0:
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified));
    WaitFixedTimeFrames(1);
L1:
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified));
    WaitFixedTimeFrames(1);
L2:
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified));
    WaitFixedTimeFrames(1);
L3:
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified));
    WaitFixedTimeFrames(1);
L4:
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified));
    WaitFixedTimeFrames(1);
L5:
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified));
    WaitFixedTimeFrames(1);
L6:
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified));
    WaitFixedTimeFrames(1);
L7:
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified));
    WaitFixedTimeFrames(1);
L8:
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified));
    SetEventFlagID(X12_4, ON);
    RestartEvent();
});

$Event(90005702, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(!EventFlag(X4_4) && CharacterDead(X0_4));
    BatchSetNetworkconnectedEventFlags(X8_4, X12_4, OFF);
    SetNetworkconnectedEventFlagID(X4_4, ON);
    SaveRequest();
});

$Event(90005703, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4) {
    EndIf(!PlayerIsInOwnWorld());
    SetEventFlagID(X12_4, OFF);
    if (!EventFlag(X20_4)) {
        SetSpEffect(X0_4, 9628);
        SetSpEffect(X0_4, 9635);
        SetSpEffect(X0_4, 9643);
        if (!CharacterHasSpEffect(X0_4, 445)) {
            SetSpEffect(X0_4, 442);
        }
        SetSpEffect(X0_4, 9644);
    }
L0:
    WaitFor(!EventFlag(X16_4) && EventFlag(X20_4));
    SetSpEffect(X0_4, 9629);
    SetSpEffect(X0_4, 9634);
    SetSpEffect(X0_4, 9642);
    SetSpEffect(X0_4, 9647);
    if (!CharacterHasSpEffect(X0_4, 445)) {
        SetSpEffect(X0_4, 440);
    }
    SetSpEffect(X0_4, 9645);
    dmgSp = HasDamageType(X0_4, 10000, DamageType.Unspecified)
        || HasDamageType(X0_4, 40000, DamageType.Unspecified)
        || CharacterHasSpEffect(X0_4, 1650000);
    if (HPRatio(X0_4) >= 1) {
        hpDmgSp &= HPRatio(X0_4) < 0.65;
    } else if (HPRatio(X0_4) >= 0.9) {
        hpDmgSp &= HPRatio(X0_4) < 0.55;
    } else if (HPRatio(X0_4) >= 0.8) {
        hpDmgSp &= HPRatio(X0_4) < 0.45;
    } else if (HPRatio(X0_4) >= 0.7) {
        hpDmgSp &= HPRatio(X0_4) < 0.35;
    } else if (HPRatio(X0_4) >= 0.7) {
        hpDmgSp &= HPRatio(X0_4) < 0.25;
    } else {
        hpDmgSp &= HPRatio(X0_4) < 0.15;
        Goto(L10);
    }
L10:
    hpDmgSp &= dmgSp;
    flag = EventFlag(X4_4) || EventFlag(X8_4);
    hpFlagSpDmg = HPRatio(X0_4) > 0 && (EventFlag(X12_4) || CharacterHasSpEffect(X0_4, 9641) || flag || hpDmgSp);
    flag2 = EventFlag(X16_4);
    WaitFor(flag2 || hpFlagSpDmg);
    RestartIf(flag2.Passed);
    SetCharacterTeamType(X0_4, TeamType.HostileNPC);
    SetSpEffect(X0_4, 9628);
    SetSpEffect(X0_4, 9635);
    SetSpEffect(X0_4, 9643);
    if (!CharacterHasSpEffect(X0_4, 445)) {
        SetSpEffect(X0_4, 442);
    }
    SetSpEffect(X0_4, 9644);
    if (!flag.Passed) {
        if (Signed(1) != X28_4) {
            BatchSetNetworkconnectedEventFlags(X20_4, X24_4, OFF);
            SetNetworkconnectedEventFlagID(X4_4, ON);
        } else {
L1:
            BatchSetNetworkconnectedEventFlags(X20_4, X24_4, OFF);
            SetNetworkconnectedEventFlagID(X8_4, ON);
        }
    }
L9:
    SaveRequest();
    RestartEvent();
});

$Event(90005704, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFixedTimeFrames(1);
    WaitFor(!EventFlag(X4_4) && EventFlag(X8_4));
    GotoIf(L4, Signed(4) == X16_4);
    GotoIf(L3, Signed(3) == X16_4);
    GotoIf(L2, Signed(2) == X16_4);
    GotoIf(L1, Signed(1) == X16_4);
    flag = EventFlag(X4_4) || !EventFlag(X8_4);
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified)
            || flag);
    RestartIf(flag.Passed);
    WaitFixedTimeFrames(1);
L4:
    flag2 = EventFlag(X4_4) || !EventFlag(X8_4);
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified)
            || flag2);
    RestartIf(flag2.Passed);
    WaitFixedTimeFrames(1);
L3:
    flag3 = EventFlag(X4_4) || !EventFlag(X8_4);
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified)
            || flag3);
    RestartIf(flag3.Passed);
    WaitFixedTimeFrames(1);
L2:
    flag4 = EventFlag(X4_4) || !EventFlag(X8_4);
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified)
            || flag4);
    RestartIf(flag4.Passed);
    WaitFixedTimeFrames(1);
L1:
    flag5 = EventFlag(X4_4) || !EventFlag(X8_4);
    WaitFor(
        HasDamageType(X0_4, 10000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified)
            || flag5);
    RestartIf(flag5.Passed);
    SetEventFlagID(X12_4, ON);
    RestartEvent();
});

$Event(90005705, Restart, function(X0_4) {
    WaitFixedTimeFrames(1);
    EnableCharacter(X0_4);
    SetCharacterBackreadState(X0_4, false);
    EndIf(!PlayerIsInOwnWorld());
    EnableCharacterImmortality(X0_4);
    WaitFor(HasDamageType(X0_4, 10000, DamageType.Unspecified));
    ForceAnimationPlayback(X0_4, 20022, false, false, false);
    WaitFixedTimeSeconds(10);
    DisableCharacter(X0_4);
    SetCharacterBackreadState(X0_4, true);
    EndEvent();
});

$Event(90005706, Restart, function(X0_4, X4_4, X8_4) {
    SetCharacterBackreadState(X0_4, false);
    EnableCharacter(X0_4);
    DisableCharacterGravity(X0_4);
    ForceAnimationPlayback(X0_4, X4_4, false, false, false);
    EndIf(X8_4 == 0);
    WaitFor(CharacterHasSpEffect(X0_4, 9624));
    IssueShortWarpRequest(X0_4, TargetEntityType.Area, X8_4, -1);
    DisableCharacterGravity(X0_4);
    EndEvent();
});

$Event(90005707, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4, X40_4) {
    EndIf(!PlayerIsInOwnWorld());
    SetEventFlagID(X12_4, OFF);
    WaitFor(!EventFlag(X16_4) && EventFlag(X20_4));
L0:
    SetSpEffect(X0_4, 9642);
    dmgSp = HasDamageType(X0_4, 10000, DamageType.Unspecified)
        || HasDamageType(X0_4, 40000, DamageType.Unspecified)
        || CharacterHasSpEffect(X0_4, 1650000);
    if (HPRatio(X0_4) >= 1) {
        hpDmgSp &= HPRatio(X0_4) < 0.65;
    } else if (HPRatio(X0_4) >= 0.9) {
        hpDmgSp &= HPRatio(X0_4) < 0.55;
    } else if (HPRatio(X0_4) >= 0.8) {
        hpDmgSp &= HPRatio(X0_4) < 0.45;
    } else if (HPRatio(X0_4) >= 0.7) {
        hpDmgSp &= HPRatio(X0_4) < 0.35;
    } else if (HPRatio(X0_4) >= 0.7) {
        hpDmgSp &= HPRatio(X0_4) < 0.25;
    } else {
        hpDmgSp &= HPRatio(X0_4) < 0.15;
        Goto(L10);
    }
L10:
    hpDmgSp &= dmgSp;
    hpFlagSpDmg = HPRatio(X0_4) > 0
        && (EventFlag(X12_4)
            || CharacterHasSpEffect(X0_4, 9641)
            || EventFlag(X4_4)
            || EventFlag(X8_4)
            || hpDmgSp);
    flag = EventFlag(X16_4);
    WaitFor(flag || hpFlagSpDmg);
    RestartIf(flag.Passed);
    if (!or5.Passed) {
        if (Signed(1) != X28_4) {
            BatchSetNetworkconnectedEventFlags(X20_4, X24_4, OFF);
            SetNetworkconnectedEventFlagID(X4_4, ON);
        } else {
L0:
            BatchSetNetworkconnectedEventFlags(X20_4, X24_4, OFF);
            SetNetworkconnectedEventFlagID(X8_4, ON);
        }
    }
L9:
    SaveRequest();
    if (X36_4 != 0) {
        WaitFixedTimeRealFrames(2);
        WaitFor(!EventFlag(X36_4));
    }
    ForceAnimationPlayback(X0_4, X32_4, false, false, false);
    SetEventFlagID(X40_4, ON);
    RestartEvent();
});

$Event(90005708, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(CharacterBackreadStatus(X0_4) && EventFlag(X4_4));
    WaitFixedTimeRealFrames(1);
    RestartIf(!EventFlag(X4_4));
    if (X8_4 == 0) {
        ResetCharacterPosition(X0_4);
    } else {
        IssueShortWarpRequest(X0_4, TargetEntityType.Area, X8_4, -1);
    }
});

$Event(90005709, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(HasDamageType(X0_4, 0, DamageType.Unspecified));
    SpawnOneshotSFX(TargetEntityType.Character, X0_4, X4_4, X8_4);
    RestartEvent();
});

$Event(90005710, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    WaitFor(!EventFlag(X0_4));
    CreateAssetfollowingSFX(X4_4, X8_4, X12_4);
    WaitFor(EventFlag(X0_4));
    WaitFixedTimeSeconds(2);
    DeleteAssetfollowingSFX(X4_4, true);
    RestartEvent();
});

$Event(90005711, Restart, function(X0_4, X4_4) {
    if (!PlayerIsInOwnWorld()) {
        EndEvent();
    }
L0:
    SetNetworkUpdateAuthority(20000, AuthorityLevel.Forced);
    WaitFor(EventFlag(X0_4));
    ChangeCharacterPatrolBehavior(35000, X4_4);
    RestartEvent();
});

$Event(90005712, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    DisableNetworkSync();
    EndIf(!PlayerIsInOwnWorld());
    CreateAssetfollowingSFX(X4_4, X8_4, X12_4);
    WaitFor(CharacterHasSpEffect(X0_4, 9502));
    DeleteAssetfollowingSFX(X4_4, true);
    WaitFor(CharacterHasSpEffect(X0_4, 9503));
    RestartEvent();
});

$Event(90005713, Restart, function(X0_4, X4_4, X8_4) {
    if (!EventFlag(X0_4)) {
        WaitFor(
            (PlayerIsInOwnWorld() && CharacterHasSpEffect(X4_4, 9500))
                || (!PlayerIsInOwnWorld() && EventFlag(X0_4)));
        if (PlayerIsInOwnWorld()) {
            SetNetworkconnectedEventFlagID(X0_4, ON);
        }
    }
L0:
    EnableCharacterAI(X8_4);
    WaitFor(
        (PlayerIsInOwnWorld() && CharacterHasSpEffect(20000, 202))
            || (!PlayerIsInOwnWorld() && !EventFlag(X0_4)));
    if (PlayerIsInOwnWorld()) {
        SetNetworkconnectedEventFlagID(X0_4, OFF);
    }
    RestartEvent();
});

$Event(90005720, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    EndIf(CharacterHasSpEffect(X0_4, 11020));
    DisableCharacter(X4_4);
    DisableCharacterCollision(X4_4);
    WaitFor(CharacterHasSpEffect(X0_4, 10960) && CharacterHasSpEffect(X0_4, X8_4));
    EnableCharacter(X4_4);
    EnableCharacterCollision(X4_4);
    SetSpEffect(X4_4, 8551);
    WarpCharacterAndCopyFloor(X4_4, TargetEntityType.Character, X0_4, X12_4, X0_4);
    ForceAnimationPlayback(X4_4, 20000, false, false, false);
    EndEvent();
});

$Event(90005721, Restart, function(X0_4, X4_4) {
    WaitFor(CharacterDead(X0_4));
    WaitRandomTimeSeconds(0.5, 1.5);
    ForceCharacterDeath(X4_4, true);
    EndEvent();
});

$Event(90005722, Restart, function(X0_4, X4_4) {
    if (CharacterHasSpEffect(X0_4, 11020)) {
        SetCharacterTeamType(X0_4, TeamType.HostileNPC);
        SetCharacterTeamType(X4_4, TeamType.HostileNPC);
    }
L0:
    WaitFor(HPRatio(X0_4) < 0.65 || HPRatio(X4_4, GreaterOrEqual, 1) < 0.65);
    SetSpEffect(X0_4, 11012);
    SetSpEffect(X0_4, 11020);
    SetCharacterTeamType(X0_4, TeamType.HostileNPC);
    SetCharacterTeamType(X4_4, TeamType.HostileNPC);
    EndEvent();
});

$Event(90005723, Restart, function(X0_4) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(!CharacterHasSpEffect(X0_4, 11001) && !CharacterHasSpEffect(X0_4, 11020));
    SetSpEffect(X0_4, 11000);
    WaitFor(CharacterHasSpEffect(X0_4, 11001) || CharacterHasSpEffect(X0_4, 11020));
    ClearSpEffect(X0_4, 11000);
    RestartEvent();
});

$Event(90005724, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4) {
    if (EventFlag(X0_4)) {
        DisableCharacter(X20_4);
        DisableCharacterCollision(X20_4);
        if (Signed(X16_4) != 0) {
            DisableCharacter(X4_4);
            DisableCharacterCollision(X4_4);
            ForceCharacterTreasure(X4_4);
            EndEvent();
        }
        DisableCharacter(X4_4);
        DisableCharacterCollision(X4_4);
        ForceCharacterDeath(X4_4, false);
        EndEvent();
    }
L0:
    WaitFor(CharacterDead(X4_4));
    WaitFixedTimeSeconds(X12_4);
    SetEventFlagID(X0_4, ON);
    EndIf(!PlayerIsInOwnWorld());
    EndIf(Signed(X16_4) == 1);
    AwardItemsIncludingClients(X8_4);
    EndEvent();
});

$Event(90005725, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    WaitFixedTimeFrames(1);
    if (PlayerIsInOwnWorld()) {
        if (EventFlag(X0_4) && EventFlag(X12_4)) {
            SetEventFlagID(X12_4, OFF);
        }
    }
L0:
    DisableCharacter(X16_4);
    SetCharacterBackreadState(X16_4, true);
    DisableCharacter(X20_4);
    SetCharacterBackreadState(X20_4, true);
    DisableAsset(X24_4);
    GotoIf(L1, EventFlag(X0_4));
    GotoIf(L2, EventFlag(X4_4));
    GotoIf(L4, EventFlag(X8_4));
L1:
    EnableCharacter(X16_4);
    SetCharacterBackreadState(X16_4, false);
    if (!CharacterHasSpEffect(X16_4, 11035)) {
        ForceAnimationPlayback(X16_4, 930003, false, false, false);
    }
    if (CharacterHasSpEffect(X16_4, 11035)) {
        ForceAnimationPlayback(X16_4, 930002, false, false, false);
    }
    EnableCharacter(X20_4);
    SetCharacterBackreadState(X20_4, false);
    EnableAsset(X24_4);
    Goto(L20);
L2:
    EnableCharacter(X16_4);
    SetCharacterBackreadState(X16_4, false);
    SetCharacterTeamType(X16_4, TeamType.HostileNPC);
    EnableCharacter(X20_4);
    SetCharacterBackreadState(X20_4, false);
    SetCharacterTeamType(X20_4, TeamType.HostileNPC);
    EnableAsset(X24_4);
    Goto(L20);
L4:
    ForceCharacterTreasure(X16_4);
    DisableCharacter(X16_4);
    SetCharacterBackreadState(X16_4, true);
    DisableCharacter(X20_4);
    SetCharacterBackreadState(X20_4, true);
    DisableAsset(X24_4);
    Goto(L20);
L20:
    EndEvent();
});

$Event(90005726, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4) {
    WaitFixedTimeFrames(1);
    if (PlayerIsInOwnWorld()) {
        if (EventFlag(X0_4) && EventFlag(X12_4)) {
            SetEventFlagID(X12_4, OFF);
        }
    }
L0:
    DisableCharacter(X16_4);
    SetCharacterBackreadState(X16_4, true);
    DisableAsset(X20_4);
    GotoIf(L1, EventFlag(X0_4));
    GotoIf(L2, EventFlag(X4_4));
    GotoIf(L4, EventFlag(X8_4));
L1:
    EnableCharacter(X16_4);
    SetCharacterBackreadState(X16_4, false);
    ForceAnimationPlayback(X16_4, 930003, false, false, false);
    EnableAsset(X20_4);
    Goto(L20);
L2:
    EnableCharacter(X16_4);
    SetCharacterBackreadState(X16_4, false);
    SetCharacterTeamType(X16_4, TeamType.HostileNPC);
    EnableAsset(X20_4);
    Goto(L20);
L4:
    ForceCharacterTreasure(X16_4);
    DisableCharacter(X16_4);
    SetCharacterBackreadState(X16_4, true);
    DisableAsset(X20_4);
    Goto(L20);
L20:
    EndEvent();
});

$Event(90005727, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(X16_4));
    SetSpEffect(X4_4, 9629);
    SetSpEffect(X4_4, 9634);
    SetSpEffect(X4_4, 9642);
    SetSpEffect(X4_4, 440);
    SetSpEffect(X4_4, 9645);
    SetSpEffect(X8_4, 9629);
    SetSpEffect(X8_4, 9634);
    SetSpEffect(X8_4, 9642);
    SetSpEffect(X8_4, 440);
    SetSpEffect(X8_4, 9645);
    WaitFor(
        EventFlag(X0_4)
            || (HasDamageType(X4_4, 20000, DamageType.Unspecified) && CharacterHPValue(X4_4) < 1)
            || (HasDamageType(X8_4, 20000, DamageType.Unspecified) && CharacterHPValue(X8_4) < 1));
    SetCharacterTeamType(X4_4, TeamType.HostileNPC);
    EnableCharacterAI(X4_4);
    SetSpEffect(X4_4, 9628);
    SetSpEffect(X4_4, 9635);
    SetSpEffect(X4_4, 9643);
    SetSpEffect(X4_4, 442);
    SetSpEffect(X4_4, 9644);
    SetCharacterTeamType(X8_4, TeamType.HostileNPC);
    EnableCharacterAI(X8_4);
    SetSpEffect(X8_4, 9628);
    SetSpEffect(X8_4, 9635);
    SetSpEffect(X8_4, 9643);
    SetSpEffect(X8_4, 442);
    SetSpEffect(X8_4, 9644);
    if (!EventFlag(X16_4)) {
        BatchSetNetworkconnectedEventFlags(X12_4, X16_4, OFF);
        SetNetworkconnectedEventFlagID(X0_4, ON);
    }
    EndEvent();
});

$Event(90005728, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(
        (HasDamageType(X0_4, 20000, DamageType.Unspecified)
            || HasDamageType(X0_4, 40000, DamageType.Unspecified))
            && !EventFlag(X8_4));
    SetNetworkconnectedEventFlagID(X4_4, ON);
    EndEvent();
});

$Event(90005729, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(X0_4));
    SetCharacterTalkRange(X4_4, X8_4);
    WaitForEventFlag(ON, TargetEventFlagType.EventFlag, X12_4);
    WaitFixedTimeSeconds(30);
    SetNetworkconnectedEventFlagID(X12_4, OFF);
    RestartEvent();
});

$Event(90005730, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(!EventFlag(X0_4) && EventFlag(X12_4) && !EventFlag(X16_4) && !EventFlag(X20_4));
    if (!EventFlag(X8_4)) {
        flag = EventFlag(X0_4) || !EventFlag(X12_4) || EventFlag(X16_4) || EventFlag(X20_4);
        WaitFor(EventFlag(X8_4) || flag);
        RestartIf(flag.Passed);
        SetEventFlagID(X0_4, ON);
        RestartEvent();
    }
L0:
    flag2 = EventFlag(X0_4) || !EventFlag(X12_4) || EventFlag(X16_4) || EventFlag(X20_4) || !EventFlag(X8_4);
    WaitFor(ElapsedSeconds(X4_4) || flag2);
    RestartIf(flag2.Passed);
    SetEventFlagID(X0_4, ON);
    RestartEvent();
});

$Event(90005731, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    EndIf(!PlayerIsInOwnWorld());
    if (!EventFlag(X0_4)) {
        WaitFor(EntityInRadiusOfEntity(10000, X4_4, X8_4, 1));
        SetEventFlagID(X0_4, ON);
    }
L0:
    WaitFor(
        !EntityInRadiusOfEntity(10000, X4_4, X8_4, 1)
            && !EntityInRadiusOfEntity(10000, X4_4, X12_4, 1));
    SetEventFlagID(X0_4, OFF);
    RestartEvent();
});

$Event(90005732, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(!PlayerIsInOwnWorld());
    if (!EventFlag(X0_4)) {
        WaitFor(InArea(10000, X4_4));
        SetEventFlagID(X0_4, ON);
    }
L0:
    WaitFor(!InArea(10000, X4_4) && !InArea(10000, X8_4));
    SetEventFlagID(X0_4, OFF);
    RestartEvent();
});

$Event(90005733, Restart, function(X0_4) {
    EndIf(!PlayerIsInOwnWorld());
    DisableNetworkSync();
    SetEventFlagID(X0_4, OFF);
    WaitFor(EventFlag(X0_4) && PlayerIsInOwnWorld());
    SendCharacterDataToOnlinePlayers(0);
    RestartEvent();
});

$Event(90005740, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_2, X28_4, X32_4, X36_4, X40_4, X44_4) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(EventFlag(X0_4));
    if (Signed(X16_4) != 0) {
        GotoIf(L0, X20_4 == 0);
        WarpAssetToCharacter(X20_4, X12_4, X24_2);
        WaitFixedTimeRealFrames(1);
        area &= EntityInRadiusOfEntity(10000, X20_4, X28_4, 1);
        GotoIf(L9, area);
        GotoIf(L9, 
            EntityInRadiusOfEntity(10000, X20_4, X44_4, 1)
                && EntityInRadiusOfEntity(10000, X12_4, X44_4, 1));
        RotateCharacter(10000, X20_4, -1, true);
        RotateCharacter(10000, X20_4, 90006, false);
        Goto(L8);
    }
L0:
    RotateCharacter(10000, X12_4, -1, true);
    area &= EntityInRadiusOfEntity(10000, X12_4, X28_4, 1);
    GotoIf(L9, area);
    RotateCharacter(10000, X12_4, 90006, false);
    Goto(L8);
L8:
    WaitFixedTimeRealFrames(1);
    sp = !CharacterHasSpEffect(10000, 9900);
    flagTime = !EventFlag(X0_4) || ElapsedSeconds(2);
    spFlagTimeArea |= sp || flagTime;
    if (Signed(X16_4) != 0) {
        GotoIf(S0, X20_4 == 0);
        spFlagTimeArea |= EntityInRadiusOfEntity(10000, X20_4, X28_4, 1);
    } else {
S0:
        spFlagTimeArea |= EntityInRadiusOfEntity(10000, X12_4, X28_4, 1);
    }
    WaitFor(spFlagTimeArea);
    if (!sp.Passed) {
        if (!flagTime.Passed) {
L9:
            SetEventFlagID(X4_4, ON);
            if (X8_4 != 0) {
                SetEventFlagID(X8_4, ON);
            }
            if (Signed(X16_4) != 0) {
                IssueShortWarpRequest(10000, TargetEntityType.Character, X12_4, X16_4);
            }
            if (Signed(X40_4) != -1) {
                RotateCharacter(10000, X12_4, X32_4, false);
            } else {
                RotateCharacter(10000, X12_4, X32_4, true);
            }
            Goto(L8);
L8:
            WaitFixedTimeRealFrames(1);
            sp2 = !CharacterHasSpEffect(10000, 9900);
            WaitFor(!EventFlag(X0_4) || sp2);
            if (!sp2.Passed) {
                if (Signed(X36_4) != -1) {
                    if (Signed(X40_4) != -1) {
                        sp3 = !CharacterHasSpEffect(10000, 9900);
                        WaitFor(CharacterHasSpEffect(10000, X40_4) || sp3);
                        GotoIf(L20, sp3.Passed);
                    }
L10:
                    SetEventFlagID(X4_4, OFF);
                    ForceAnimationPlayback(10000, X36_4, false, true, false);
                    RestartEvent();
                }
L18:
                SetEventFlagID(X4_4, OFF);
                RestartEvent();
            }
        }
L19:
        SetEventFlagID(X0_4, OFF);
        ForceAnimationPlayback(10000, 0, false, false, false);
        RestartEvent();
    }
L20:
    SetEventFlagID(X0_4, OFF);
    SetEventFlagID(X4_4, OFF);
    RestartEvent();
});

$Event(90005741, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4) {
    EndIf(!PlayerIsInOwnWorld());
    if (X8_4 != 0) {
        cond &= EventFlag(X8_4);
    }
    cond &= EventFlag(X0_4);
    WaitFor(cond);
    SetEventFlagID(X4_4, ON);
    if (X8_4 != 0) {
        SetEventFlagID(X8_4, OFF);
    }
    if (X20_4 != 1) {
        if (Signed(X28_4) != -1) {
            ForceAnimationPlayback(X12_4, X16_4, false, false, false);
        } else {
            ForceAnimationPlayback(X12_4, X16_4, false, true, false);
        }
    } else {
L0:
        if (Signed(X28_4) != -1) {
            RotateCharacter(X12_4, 10000, X16_4, false);
        } else {
            RotateCharacter(X12_4, 10000, X16_4, true);
        }
        Goto(L10);
    }
L10:
    cond &= !EventFlag(X0_4);
    if (Signed(X28_4) != -1) {
        cond &= CharacterHasSpEffect(X12_4, X28_4);
    }
    WaitFor(cond);
    if (Signed(X24_4) != -1) {
        SetEventFlagID(X4_4, OFF);
        ForceAnimationPlayback(X12_4, X24_4, false, true, false);
        WaitFixedTimeSeconds(X32_4);
        RestartEvent();
    }
L19:
    SetEventFlagID(X4_4, OFF);
    WaitFixedTimeSeconds(X32_4);
    RestartEvent();
L20:
    SetEventFlagID(X0_4, OFF);
    SetEventFlagID(X4_4, OFF);
    RestartEvent();
});

$Event(90005742, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_2, X28_4, X32_4, X36_4, X40_4, X44_4, X48_4) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(EventFlag(X0_4));
    if (Signed(X16_4) != 0) {
        GotoIf(L0, X20_4 == 0);
        WarpAssetToCharacter(X20_4, X12_4, X24_2);
        WaitFixedTimeRealFrames(1);
        area &= EntityInRadiusOfEntity(10000, X20_4, X28_4, 1);
        GotoIf(L9, area);
        areaFlag &= EntityInRadiusOfEntity(10000, X20_4, X44_4, 1)
            && EntityInRadiusOfEntity(10000, X12_4, X44_4, 1);
        GotoIf(L9, areaFlag);
        RotateCharacter(10000, X20_4, -1, true);
        RotateCharacter(10000, X20_4, 90006, false);
        Goto(L8);
    }
L0:
    RotateCharacter(10000, X12_4, -1, true);
    area &= EntityInRadiusOfEntity(10000, X12_4, X28_4, 1);
    GotoIf(L9, area);
    RotateCharacter(10000, X12_4, 90006, false);
    Goto(L8);
L8:
    WaitFixedTimeRealFrames(1);
    sp = !CharacterHasSpEffect(10000, 9900);
    flagTime = !EventFlag(X0_4) || ElapsedSeconds(2);
    spFlagTimeArea |= sp || flagTime;
    if (Signed(X16_4) != 0) {
        GotoIf(S0, X20_4 == 0);
        spFlagTimeArea |= EntityInRadiusOfEntity(10000, X20_4, X28_4, 1);
    } else {
S0:
        spFlagTimeArea |= EntityInRadiusOfEntity(10000, X12_4, X28_4, 1);
    }
    WaitFor(spFlagTimeArea);
    if (!sp.Passed) {
        if (!flagTime.Passed) {
L9:
            SetEventFlagID(X4_4, ON);
            if (X8_4 != 0) {
                SetEventFlagID(X8_4, ON);
            }
            if (Signed(X16_4) != 0) {
                IssueShortWarpRequest(10000, TargetEntityType.Character, X12_4, X16_4);
            }
            if (Signed(X40_4) != -1) {
                RotateCharacter(10000, X12_4, X32_4, false);
            } else {
                RotateCharacter(10000, X12_4, X32_4, true);
            }
            Goto(L8);
L8:
            WaitFixedTimeRealFrames(1);
            sp2 = !CharacterHasSpEffect(10000, 9900);
            areaFlag &= EventFlag(X48_4);
            WaitFor(!EventFlag(X0_4) || sp2 || areaFlag);
            GotoIf(L20, sp2.Passed);
            GotoIf(L18, Signed(X36_4) == -1);
            GotoIf(L20, areaFlag.Passed);
            if (Signed(X40_4) != -1) {
                sp3 = !CharacterHasSpEffect(10000, 9900);
                WaitFor(CharacterHasSpEffect(10000, X40_4) || sp3);
                GotoIf(L20, sp3.Passed);
            }
L10:
            SetEventFlagID(X4_4, OFF);
            ForceAnimationPlayback(10000, X36_4, false, true, false);
            RestartEvent();
L18:
            SetEventFlagID(X4_4, OFF);
            RestartEvent();
        }
L19:
        SetEventFlagID(X0_4, OFF);
        ForceAnimationPlayback(10000, 0, false, false, false);
        RestartEvent();
    }
L20:
    SetEventFlagID(X0_4, OFF);
    SetEventFlagID(X4_4, OFF);
    RestartEvent();
});

$Event(90005743, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4) {
    EndIf(!PlayerIsInOwnWorld());
    if (X8_4 != 0) {
        cond &= EventFlag(X8_4);
    }
    cond &= EventFlag(X0_4);
    WaitFor(cond);
    SetEventFlagID(X4_4, ON);
    if (X8_4 != 0) {
        SetEventFlagID(X8_4, OFF);
    }
    if (X20_4 != 1) {
        if (Signed(X28_4) != -1) {
            ForceAnimationPlayback(X12_4, X16_4, false, false, false);
        } else {
            ForceAnimationPlayback(X12_4, X16_4, false, true, false);
        }
    } else {
L0:
        if (Signed(X28_4) != -1) {
            RotateCharacter(X12_4, 10000, X16_4, false);
        } else {
            RotateCharacter(X12_4, 10000, X16_4, true);
        }
        Goto(L10);
    }
L10:
    cond &= !EventFlag(X0_4);
    if (Signed(X28_4) != -1) {
        cond &= CharacterHasSpEffect(X12_4, X28_4);
    }
    flag = EventFlag(X36_4);
    WaitFor(cond || flag);
    GotoIf(L19, Signed(X24_4) == -1);
    GotoIf(L20, flag.Passed);
    SetEventFlagID(X4_4, OFF);
    ForceAnimationPlayback(X12_4, X24_4, false, true, false);
    WaitFixedTimeSeconds(X32_4);
    RestartEvent();
L19:
    SetEventFlagID(X4_4, OFF);
    WaitFixedTimeSeconds(X32_4);
    RestartEvent();
L20:
    SetEventFlagID(X0_4, OFF);
    SetEventFlagID(X4_4, OFF);
    RestartEvent();
});

$Event(90005750, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    DisableNetworkSync();
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(EventFlag(X20_4) && !AllBatchEventFlags(X12_4, X16_4));
    if (Signed(X24_4) != 0) {
        CreateAssetfollowingSFX(X0_4, 90, X24_4);
    } else {
        CreateAssetfollowingSFX(X0_4, 90, 6101);
    }
    flag = !EventFlag(X20_4) || AllBatchEventFlags(X12_4, X16_4);
    WaitFor(ActionButtonInArea(X4_4, X0_4) || flag);
    if (!flag.Passed) {
        DeleteAssetfollowingSFX(X0_4, true);
        AwardItemsIncludingClients(X8_4);
        EzstateInstructionRequest(10000, 60070, 0);
        EndEvent();
    }
L0:
    DeleteAssetfollowingSFX(X0_4, true);
    RestartEvent();
});

$Event(90005751, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(HasDamageType(X0_4, 20000, DamageType.Unspecified) && PlayerIsInOwnWorld());
    SpawnOneshotSFX(TargetEntityType.Asset, X0_4, X4_4, X8_4);
    RestartEvent();
});

$Event(90005752, Default, function(X0_4, X4_4, X8_4, X12_4) {
    DisableNetworkSync();
    if (ThisEventSlot()) {
        dmg = HasDamageType(X0_4, 20000, DamageType.Unspecified);
        WaitFor(PlayerIsInOwnWorld() && (ElapsedSeconds(X12_4) || dmg));
        RestartIf(dmg.Passed);
        DeleteAssetfollowingSFX(X0_4, true);
    }
L0:
    WaitFor(PlayerIsInOwnWorld() && HasDamageType(X0_4, 20000, DamageType.Unspecified));
    CreateAssetfollowingSFX(X0_4, X4_4, X8_4);
    RestartEvent();
});

$Event(90005760, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    EndIf(EventFlag(X0_4));
    if (!ThisEventSlot()) {
        WaitFor(
            EventFlag(X12_4) && !EventFlag(9000) && PlayerIsInOwnWorld() && InArea(10000, X8_4));
    }
L0:
    EnableCharacter(X4_4);
    SetCharacterBackreadState(X4_4, false);
    ForceAnimationPlayback(X4_4, 20000, false, false, false);
    EndEvent();
});

$Event(90005770, Restart, function(X0_4) {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(X0_4));
    WaitFor(EventFlag(X0_4));
    SetNetworkconnectedEventFlagID(X0_4, ON);
});

$Event(90005771, Restart, function(X0_4, X4_4) {
    EndIf(!PlayerIsInOwnWorld());
    SetEventFlagID(X4_4, OFF);
    WaitFor(EntityInRadiusOfEntity(10000, X0_4, 3, 1));
    SetEventFlagID(X4_4, ON);
    WaitFor(!EntityInRadiusOfEntity(10000, X0_4, 3, 1));
    RestartEvent();
});

$Event(90005772, Restart, function(X0_4) {
    SetCharacterBackreadState(X0_4, true);
    DisableCharacter(X0_4);
});

$Event(90005773, Default, function(X0_4) {
    EndIf(!PlayerIsInOwnWorld());
    SetEventFlagID(X0_4, OFF);
    WaitFor(EventFlag(X0_4));
    SaveRequest();
    RestartEvent();
});

$Event(90005774, Default, function(X0_4, X4_4, X8_4) {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(X8_4));
    WaitFor(ElapsedSeconds(2) && EventFlag(X0_4));
    if (PlayerIsInOwnWorld()) {
        AwardItemsIncludingClients(X4_4);
    }
    EndEvent();
});

$Event(90005775, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(X4_4));
    WaitFor(EventFlag(X4_4));
    OpenWorldMapPoint(X0_4, X8_4);
});

$Event(90005780, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_1, X32_4) {
    if (PlayerIsInOwnWorld()) {
        SetNetworkUpdateAuthority(X12_4, AuthorityLevel.Forced);
    }
    DeleteNPCSummonSign(X12_4);
    EndIf(EventFlag(X0_4));
    EndIf(EventFlag(X8_4));
    if (0 != X24_4) {
        flagOnlineChrArea &= EventFlag(X24_4);
    }
    flagOnlineChrArea &= PlayerIsInOwnWorld()
        && CharacterBackreadStatus(X12_4)
        && EntityInRadiusOfEntity(10000, X12_4, 10, 1);
    WaitFor(flagOnlineChrArea);
    PlaceNPCSummonSign(X16_4, X12_4, X20_4, X4_4, X8_4, X28_1);
    EndIf(Signed(0) == X32_4);
});

$Event(90005781, Default, function(X0_4, X4_4, X8_4, X12_4) {
    DisableCharacter(X12_4);
    DisableCharacterCollision(X12_4);
    DisableCharacterAI(X12_4);
    EndIf(EventFlag(X0_4));
    EndIf(EventFlag(X8_4));
    WaitFor(EventFlag(X4_4));
    SetCharacterBackreadState(X12_4, false);
    EnableCharacter(X12_4);
    EnableCharacterCollision(X12_4);
    EnableCharacterAI(X12_4);
    EnableCharacterDefaultBackread(X12_4);
    WaitFor(EventFlag(X8_4));
    DisableCharacterDefaultBackread(X12_4);
});

$Event(90005782, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(EventFlag(X0_4) && EventFlag(X4_4));
    RequestCharacterAICommand(X8_4, 10, 0);
    RequestCharacterAIReplan(X8_4);
    SetEventPoint(X8_4, X16_4, 0);
    WaitFor(InArea(X8_4, X16_4));
    if (Signed(X20_4) != 0) {
        RotateCharacter(X8_4, X12_4, X20_4, true);
    } else {
        RotateCharacter(X8_4, X12_4, 60060, true);
    }
    time = ElapsedSeconds(3);
    WaitFor(time || InArea(X8_4, X4_4));
    RestartIf(time.Passed);
    RequestCharacterAICommand(X8_4, -1, 0);
    RequestCharacterAIReplan(X8_4);
    SetNetworkUpdateRate(X8_4, true, CharacterUpdateFrequency.AlwaysUpdate);
});

$Event(90005784, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4) {
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(EventFlag(X0_4) && EventFlag(X4_4));
    RequestCharacterAICommand(X8_4, 10, 0);
    RequestCharacterAIReplan(X8_4);
    SetEventPoint(X8_4, X16_4, 0);
    WaitFor(InArea(X8_4, X16_4));
    if (Signed(X20_4) != 0) {
        RotateCharacter(X8_4, X12_4, X20_4, true);
    } else {
        RotateCharacter(X8_4, X12_4, 60060, true);
    }
    time = ElapsedSeconds(3);
    WaitFor(time || InArea(X8_4, X12_4));
    RestartIf(time.Passed);
    RequestCharacterAICommand(X8_4, -1, 0);
    RequestCharacterAIReplan(X8_4);
    SetNetworkUpdateRate(X8_4, true, CharacterUpdateFrequency.AlwaysUpdate);
});

$Event(90005783, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    EndIf(EventFlag(X0_4));
    flag = EventFlag(X0_4) && EventFlag(X4_4);
    onlineFlagChrArea &= PlayerIsInOwnWorld()
        && EventFlag(X4_4)
        && CharacterAIState(X12_4, AIStateType.Combat, NotEqual, 1);
    if (X20_4 == 0) {
        onlineFlagChrArea &= !EntityInRadiusOfEntity(10000, X16_4, 75, 1);
    } else {
        onlineFlagChrArea &= !InArea(10000, X20_4);
    }
    onlineFlagArea &= PlayerIsInOwnWorld() && EventFlag(X4_4);
    if (Signed(X24_4) != 2) {
        GotoIf(S0, Signed(X24_4) == 1);
        onlineFlagArea &= !EntityInRadiusOfEntity(10000, X16_4, 180, 1);
        Goto(S1);
S0:
        onlineFlagArea &= !EntityInRadiusOfEntity(10000, X16_4, 360, 1);
    } else {
        onlineFlagArea &= !EntityInRadiusOfEntity(10000, X16_4, 720, 1);
    }
S1:
    WaitFor(flag || onlineFlagChrArea || onlineFlagArea);
    EndIf(EventFlag(X0_4) && EventFlag(X8_4));
    SendNPCSummonHome(X12_4);
    EndEvent();
});

$Event(90005785, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    EndIf(EventFlag(X0_4));
    flag = EventFlag(X0_4) && EventFlag(X4_4);
    onlineFlagArea &= PlayerIsInOwnWorld() && EventFlag(X4_4);
    if (X20_4 == 0) {
        onlineFlagArea &= !EntityInRadiusOfEntity(10000, X16_4, X24_4, 1);
    } else {
        onlineFlagArea &= !InArea(10000, X20_4);
    }
    WaitFor(flag || onlineFlagArea);
    EndIf(EventFlag(X0_4) && EventFlag(X8_4));
    SendNPCSummonHome(X12_4);
    EndEvent();
});

// NPC Invader
// X4_4 is the death flag
$Event(90005790, Default, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4, X40_1, X44_4) {
    DisableNetworkSync();
    EndIf(!PlayerIsInOwnWorld());
    if (0 != X0_4) {
        EndIf(EventFlag(X0_4));
    }
    EndIf(EventFlag(X4_4));
    if (PlayerIsInOwnWorld()) {
        SetNetworkUpdateAuthority(X16_4, AuthorityLevel.Forced);
    }
    EndIf(EventFlag(X12_4));
    onlineFlagArea &= PlayerIsInOwnWorld() && !EventFlag(X0_4) && !EventFlag(X4_4) && !EventFlag(X8_4);
    if (0 != X36_4) {
        onlineFlagArea &= EventFlag(X36_4);
    }
    onlineFlagArea &= InArea(10000, X28_4) && !EventFlag(9000);
    WaitFor(onlineFlagArea);
    WaitFixedTimeSeconds(X32_4);
    PlaceNPCSummonSign(X20_4, X16_4, X24_4, X8_4, X12_4, X40_1);
    WaitFixedTimeSeconds(1);
    RestartEvent();
    EndIf(Signed(0) == X44_4);
});

$Event(90005791, Default, function(X0_4, X4_4, X8_4, X12_4) {
    DisableCharacter(X12_4);
    DisableCharacterCollision(X12_4);
    DisableCharacterAI(X12_4);
    EndIf(EventFlag(X0_4));
    EndIf(EventFlag(X8_4));
    WaitFor(EventFlag(X4_4));
    SetCharacterBackreadState(X12_4, false);
    SetNetworkUpdateRate(X12_4, true, CharacterUpdateFrequency.AtLeastEvery2Frames);
    EnableCharacter(X12_4);
    EnableCharacterCollision(X12_4);
    EnableCharacterAI(X12_4);
    EnableCharacterDefaultBackread(X12_4);
    WaitFor(EventFlag(X8_4));
    DisableCharacterDefaultBackread(X12_4);
    SetNetworkUpdateRate(X12_4, false, CharacterUpdateFrequency.AtLeastEvery2Frames);
});

$Event(90005792, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4) {
    if (EventFlag(X0_4)) {
        DisableCharacter(X12_4);
        DisableCharacterCollision(X12_4);
        ForceCharacterDeath(X12_4, false);
        EndEvent();
    }
L0:
    WaitFor(CharacterRatioDead(X12_4) && EventFlag(X4_4));
    WaitFixedTimeSeconds(X20_4);
    SetEventFlagID(X0_4, ON);
    EndIf(!PlayerIsInOwnWorld());
    EndIf(Signed(X16_4) == 0);
    AwardItemsIncludingClients(X16_4);
    EndEvent();
    flag = EventFlag(X8_4);
});

$Event(90005793, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    EndIf(EventFlag(X0_4));
    EndIf(!PlayerIsInOwnWorld());
    flag = EventFlag(X0_4);
    onlineFlagChrArea &= PlayerIsInOwnWorld()
        && EventFlag(X4_4)
        && CharacterAIState(X12_4, AIStateType.Combat, NotEqual, 1);
    if (X20_4 == 0) {
        onlineFlagChrArea &= !EntityInRadiusOfEntity(10000, X16_4, 110, 1);
    } else {
        onlineFlagChrArea &= !InArea(10000, X20_4);
    }
    onlineFlagArea &= PlayerIsInOwnWorld() && EventFlag(X4_4);
    if (Signed(X24_4) != 2) {
        GotoIf(S0, Signed(X24_4) == 1);
        onlineFlagArea &= !EntityInRadiusOfEntity(10000, X16_4, 180, 1);
        Goto(S1);
S0:
        onlineFlagArea &= !EntityInRadiusOfEntity(10000, X16_4, 360, 1);
    } else {
        onlineFlagArea &= !EntityInRadiusOfEntity(10000, X16_4, 720, 1);
    }
S1:
    WaitFor(flag || onlineFlagChrArea || onlineFlagArea);
    EndIf(EventFlag(X0_4));
    SendNPCSummonHome(X12_4);
    EndEvent();
    flag2 = !EventFlag(X8_4);
});

$Event(90005795, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4) {
    DisableNetworkSync();
    EndIf(!PlayerIsInOwnWorld());
    SetEventFlagID(X12_4, OFF);
    SetEventFlagID(X16_4, OFF);
    DeleteAssetfollowingSFX(X28_4, true);
    EndIf(EventFlag(X0_4));
    WaitFor(
        EventFlag(X8_4)
            && PlayerIsInOwnWorld()
            && !(HasMultiplayerState(MultiplayerState.Multiplayer)
                || HasMultiplayerState(MultiplayerState.MultiplayerPending)));
    CreateAssetfollowingSFX(X28_4, 100, X32_4);
    online = HasMultiplayerState(MultiplayerState.Multiplayer)
        || HasMultiplayerState(MultiplayerState.MultiplayerPending);
    WaitFor(online || ActionButtonInArea(X24_4, X28_4) || !EventFlag(X8_4));
    RestartIf(online.Passed);
    RestartIf(!EventFlag(X8_4));
    DisplayGenericDialogAndSetEventFlags(X20_4, PromptType.YESNO, NumberofOptions.TwoButtons, X28_4, 2, X12_4, X16_4, X16_4);
    RestartIf(!EventFlag(X12_4));
    SetEventFlagID(X4_4, ON);
    SetSpEffect(10000, 15);
    WaitFixedTimeSeconds(20);
    RestartEvent();
});

$Event(90005796, Restart, function(X0_4, X4_4, X8_1, X12_4) {
    DisableNetworkSync();
    EndIf(PlayerIsInOwnWorld());
    EndIf(EventFlag(X0_4));
    WaitFor(CharacterRatioDead(X4_4));
    SetEventFlagID(X0_4, ON);
    DisplayBanner(X8_1);
    if (X12_4 != 0) {
        SetPsuedoMultiplayerReturnPosition(X12_4);
    }
    IssueEndOfPseudoMultiplayerNotification(true);
});

$Event(90005797, Restart, function(X0_4, X4_4, X8_1, X12_4, X16_4) {
    DisableNetworkSync();
    EndIf(PlayerIsInOwnWorld());
    EndIf(EventFlag(X0_4));
    WaitFor(CharacterRatioDead(X4_4));
    SetEventFlagID(X0_4, ON);
    DisplayBanner(X8_1);
    SetSpEffect(20000, X16_4);
    if (X12_4 != 0) {
        SetPsuedoMultiplayerReturnPosition(X12_4);
    }
    IssueEndOfPseudoMultiplayerNotification(true);
});

$Event(9005800, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4) {
    if (!EventFlag(X0_4)) {
        WaitFixedTimeFrames(1);
        if (X24_4 != 0) {
            GotoIf(L0, EventFlag(X24_4));
            if (X28_4 != 0) {
                areaFlag |= InArea(10000, X28_4);
            }
            areaFlag |= EventFlag(X24_4);
            WaitFor((areaFlag && PlayerIsInOwnWorld()) || EventFlag(X0_4));
            RestartIf(EventFlag(X0_4));
            Goto(L1);
        }
L0:
        if (PlayerIsInOwnWorld()) {
            WaitFor(
                EventFlag(X0_4)
                    || (PlayerIsInOwnWorld() && !EventFlag(X0_4) && ActionButtonInArea(X20_4, X4_4)));
            GotoIf(L2, !PlayerIsInOwnWorld());
            RestartIf(EventFlag(X0_4));
            SuppressSoundForFogGate(5);
            if (!CharacterHasSpEffect(10000, 4250)) {
                RotateCharacter(10000, X8_4, 60060, true);
            } else {
                RotateCharacter(10000, X8_4, 60060, false);
            }
        }
L3:
        GotoIf(L1, EventFlag(X12_4));
        time = ElapsedSeconds(3);
        WaitFor(
            ((InArea(10000, X8_4) || time) && PlayerIsInOwnWorld() && !EventFlag(X0_4))
                || EventFlag(X0_4));
        RestartIf(EventFlag(X0_4));
        RestartIf(time.Passed);
L1:
        if (PlayerIsInOwnWorld()) {
            IssueBossRoomEntryNotification();
            SetNetworkUpdateAuthority(X16_4, AuthorityLevel.Forced);
        }
L2:
        ActivateMultiplayerdependantBuffs(X16_4);
        SetNetworkconnectedEventFlagID(X12_4, ON);
        EndIf(!PlayerIsInOwnWorld());
        RestartEvent();
    }
L10:
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(
        PlayerIsInOwnWorld()
            && EventFlag(X0_4)
            && (HasMultiplayerState(MultiplayerState.Invasion)
                || HasMultiplayerState(MultiplayerState.InvasionPending))
            && ActionButtonInArea(10000, X4_4));
    RotateCharacter(10000, X8_4, 60060, true);
    SendInvadingPhantomsHome(0);
    RestartEvent();
});

$Event(9005801, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4) {
    DisableNetworkSync();
    EndIf(EventFlag(X0_4));
    WaitFor(
        !EventFlag(X0_4)
            && EventFlag(X12_4)
            && CharacterType(10000, TargetType.WhitePhantom)
            && ActionButtonInArea(X20_4, X4_4));
    SuppressSoundForFogGate(5);
    RotateCharacter(10000, X8_4, 60060, true);
    time = ElapsedSeconds(3);
    WaitFor(CharacterType(10000, TargetType.WhitePhantom) && (InArea(10000, X8_4) || time));
    RestartIf(time.Passed);
    SetEventFlagID(X16_4, ON);
    RestartEvent();
});

$Event(9005810, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    if (!EventFlag(X0_4)) {
        DisableCharacter(X8_4);
        DisableAsset(X12_4);
        WaitFixedTimeSeconds(1);
        WaitFor(EventFlag(X0_4));
        SpawnOneshotSFX(TargetEntityType.Asset, X12_4, 200, 1060);
        WaitFixedTimeSeconds(0.5);
        EnableCharacter(X8_4);
        EnableAsset(X12_4);
    }
L0:
    RegisterBonfire(X4_4, X12_4, 5, 180, 0, X16_4);
});

$Event(9005811, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    DisableNetworkSync();
    DisableAsset(X4_4);
    DeleteAssetfollowingSFX(X4_4, true);
    chrFlag = (CharacterType(10000, TargetType.BlackPhantom)
        || CharacterType(10000, TargetType.Invader)
        || CharacterType(10000, TargetType.Invader2)
        || CharacterType(10000, TargetType.Invader3))
        && !EventFlag(X0_4);
    chrFlag2 = (CharacterType(10000, TargetType.WhitePhantom) || CharacterType(10000, TargetType.BluePhantom))
        && !EventFlag(X0_4);
    if (0 != X12_4) {
        flag &= EventFlag(X12_4);
    }
    flag &= !EventFlag(X0_4);
    WaitFor(
        chrFlag
            || chrFlag2
            || flag
            || ((HasMultiplayerState(MultiplayerState.Invasion)
                || HasMultiplayerState(MultiplayerState.InvasionPending))
                && EventFlag(X0_4)
                && !CharacterType(10000, TargetType.WhitePhantom))
            || ((HasMultiplayerState(MultiplayerState.Invasion)
                || HasMultiplayerState(MultiplayerState.InvasionPending))
                && EventFlag(X0_4)
                && CharacterType(10000, TargetType.WhitePhantom)
                && !EntityInRadiusOfEntity(10000, X4_4, 1, 1)));
    EnableAsset(X4_4);
    DeleteAssetfollowingSFX(X4_4, true);
    CreateAssetfollowingSFX(X4_4, 101, X8_4);
    chrFlag3 = (CharacterType(10000, TargetType.BlackPhantom)
        || CharacterType(10000, TargetType.Invader)
        || CharacterType(10000, TargetType.Invader2)
        || CharacterType(10000, TargetType.Invader3))
        && !EventFlag(X0_4);
    chrFlag4 = (CharacterType(10000, TargetType.WhitePhantom) || CharacterType(10000, TargetType.BluePhantom))
        && !EventFlag(X0_4);
    if (0 != X12_4) {
        flag2 &= EventFlag(X12_4);
    }
    flag2 &= !EventFlag(X0_4);
    WaitFor(
        !chrFlag3
            && !chrFlag4
            && !flag2
            && !((HasMultiplayerState(MultiplayerState.Invasion)
                || HasMultiplayerState(MultiplayerState.InvasionPending))
                && EventFlag(X0_4)
                && !CharacterType(10000, TargetType.WhitePhantom))
            && !((HasMultiplayerState(MultiplayerState.Invasion)
                || HasMultiplayerState(MultiplayerState.InvasionPending))
                && EventFlag(X0_4)
                && CharacterType(10000, TargetType.WhitePhantom)
                && !EntityInRadiusOfEntity(10000, X4_4, 1, 1)));
    RestartEvent();
});

$Event(9005812, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    DisableNetworkSync();
    DisableAsset(X4_4);
    DeleteAssetfollowingSFX(X4_4, true);
    if (!EventFlag(X0_4)) {
        if (0 != X12_4) {
            flag &= EventFlag(X12_4);
        }
        flag &= !EventFlag(X0_4);
        WaitFor(
            flag
                || (CharacterType(10000, TargetType.WhitePhantom)
                    || CharacterType(10000, TargetType.BluePhantom))
                || (CharacterType(10000, TargetType.BlackPhantom)
                    || CharacterType(10000, TargetType.Invader)
                    || CharacterType(10000, TargetType.Invader2)
                    || CharacterType(10000, TargetType.Invader3)));
        EnableAsset(X4_4);
        DeleteAssetfollowingSFX(X4_4, true);
        CreateAssetfollowingSFX(X4_4, 101, X8_4);
        if (0 != X12_4) {
            flag2 &= EventFlag(X12_4);
        }
        flag2 &= !EventFlag(X0_4);
        WaitFor(
            !flag2
                && !(CharacterType(10000, TargetType.WhitePhantom)
                    || CharacterType(10000, TargetType.BluePhantom))
                && !(CharacterType(10000, TargetType.BlackPhantom)
                    || CharacterType(10000, TargetType.Invader)
                    || CharacterType(10000, TargetType.Invader2)
                    || CharacterType(10000, TargetType.Invader3)));
        RestartEvent();
    }
L0:
    WaitFor(
        (HasMultiplayerState(MultiplayerState.Invasion)
            || HasMultiplayerState(MultiplayerState.InvasionPending))
            || EventFlag(9982));
    WaitFor(
        !(HasMultiplayerState(MultiplayerState.Invasion)
            || HasMultiplayerState(MultiplayerState.InvasionPending))
            && !EventFlag(9982));
    RestartEvent();
    CreateAssetfollowingSFX(X4_4, 101, X16_4);
});

$Event(9005813, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4) {
    DisableNetworkSync();
    DisableAsset(X4_4);
    DeleteAssetfollowingSFX(X4_4, true);
    if (!EventFlag(X0_4)) {
        if (0 != X12_4) {
            flag &= EventFlag(X12_4);
        }
        flag &= !EventFlag(X0_4);
        WaitFor(
            flag
                || (CharacterType(10000, TargetType.WhitePhantom)
                    || CharacterType(10000, TargetType.BluePhantom))
                || (CharacterType(10000, TargetType.BlackPhantom)
                    || CharacterType(10000, TargetType.Invader)
                    || CharacterType(10000, TargetType.Invader2)
                    || CharacterType(10000, TargetType.Invader3)));
        EnableAsset(X4_4);
        DeleteAssetfollowingSFX(X4_4, true);
        CreateAssetfollowingSFX(X4_4, 101, X8_4);
        if (0 != X12_4) {
            flag2 &= EventFlag(X12_4);
        }
        flag2 &= !EventFlag(X0_4);
        WaitFor(
            !flag2
                && !(CharacterType(10000, TargetType.WhitePhantom)
                    || CharacterType(10000, TargetType.BluePhantom))
                && !(CharacterType(10000, TargetType.BlackPhantom)
                    || CharacterType(10000, TargetType.Invader)
                    || CharacterType(10000, TargetType.Invader2)
                    || CharacterType(10000, TargetType.Invader3)));
        RestartEvent();
    }
L0:
    WaitFor(
        HasMultiplayerState(MultiplayerState.Invasion)
            || HasMultiplayerState(MultiplayerState.InvasionPending)
            || HasMultiplayerState(MultiplayerState.MultiplayerPending)
            || HasMultiplayerState(MultiplayerState.Multiplayer));
    EnableAsset(X4_4);
    DeleteAssetfollowingSFX(X4_4, true);
    CreateAssetfollowingSFX(X4_4, 101, X16_4);
    WaitFor(
        !(HasMultiplayerState(MultiplayerState.Invasion)
            || HasMultiplayerState(MultiplayerState.InvasionPending)
            || HasMultiplayerState(MultiplayerState.Multiplayer)
            || HasMultiplayerState(MultiplayerState.MultiplayerPending)));
    RestartEvent();
});

$Event(9005822, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4) {
    DisableNetworkSync();
    if (EventFlag(X0_4)) {
        EndEvent();
    }
L0:
    if (PlayerIsInOwnWorld()) {
        SetEventFlagID(X8_4, OFF);
    }
    flag &= EventFlag(X8_4);
    if (!PlayerIsInOwnWorld()) {
        flag &= EventFlag(X12_4);
    }
    if (0 != X16_4) {
        flag &= EventFlag(X16_4);
    }
    WaitFor(flag);
    WaitFixedTimeFrames(1);
    if (!EventFlag(X20_4)) {
        SetBossBGM(X4_4, BossBGMState.Start);
    }
    WaitFor(EventFlag(X20_4) || EventFlag(X0_4));
    if (!EventFlag(X0_4)) {
        WaitFixedTimeFrames(1);
        if (Signed(X24_4) != 0) {
        }
        SetBossBGM(X4_4, BossBGMState.HeatUp);
        WaitFor(EventFlag(X0_4));
    }
L1:
    if (Signed(X28_4) != 1) {
        SetBossBGM(X4_4, BossBGMState.Stop2);
        EndEvent();
    }
    SetBossBGM(X4_4, BossBGMState.Stop1);
});

$Event(9005823, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4) {
    DisableNetworkSync();
    if (PlayerIsInOwnWorld()) {
        SetEventFlagID(X8_4, OFF);
    }
    if (EventFlag(X0_4)) {
        EndEvent();
    }
L0:
    flag &= EventFlag(X8_4);
    if (!PlayerIsInOwnWorld()) {
        flag &= EventFlag(X12_4);
    }
    if (0 != X16_4) {
        flag &= EventFlag(X16_4);
    }
    WaitFor(flag);
    SetBossBGM(X4_4, BossBGMState.Start);
    flag2 |= EventFlag(X20_4) || EventFlag(X24_4) || EventFlag(X0_4);
    WaitFor(flag2);
    if (!EventFlag(X0_4)) {
        if (!EventFlag(X24_4)) {
            WaitFixedTimeFrames(1);
            if (Signed(X28_4) != 1) {
            }
            SetBossBGM(X4_4, BossBGMState.HeatUp);
            flag2 |= EventFlag(X24_4) || EventFlag(X0_4);
            WaitFor(flag2);
            GotoIf(L2, EventFlag(X0_4));
        }
L1:
        Unknown201008(90003003);
        WaitFor(EventFlag(X0_4));
    }
L2:
    if (Signed(X32_4) != 1) {
        SetBossBGM(X4_4, BossBGMState.Stop2);
        EndEvent();
    }
    SetBossBGM(X4_4, BossBGMState.Stop1);
});

$Event(90005830, Restart, function(X0_4, X4_4) {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(X0_4));
    WaitFor(EventFlag(X0_4) || (InArea(10000, X4_4) && PlayerIsInOwnWorld()));
    RestartIf(EventFlag(X0_4));
    SetSpEffect(10000, 4250);
    WaitFixedTimeSeconds(3);
    RestartEvent();
});

$Event(9005840, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(EventFlag(X0_4));
    WaitFor(CharacterHPValue(X8_4) <= 0);
    WaitFixedTimeSeconds(4);
    PlaySE(X8_4, SoundType.SFX, 888880000);
    WaitFor(CharacterDead(X8_4));
    HandleBossDefeatAndDisplayBanner(X8_4, TextBannerType.DemigodFelled);
    SetEventFlagID(X0_4, ON);
    if (X4_4 != 0) {
        SetEventFlagID(X4_4, ON);
    }
});

$Event(9005845, Restart, function(X0_4, X4_4) {
    if (EventFlag(X0_4)) {
        DisableCharacter(X4_4);
        DisableCharacterCollision(X4_4);
        ForceCharacterDeath(X4_4, false);
        EndEvent();
    }
L0:
    DisableCharacterAI(X4_4);
    if (!EventFlag(11000801)) {
        WaitFor(
            (PlayerIsInOwnWorld() && EntityInRadiusOfEntity(10000, 11000800, 20, 1))
                || HasDamageType(X4_4, 10000, DamageType.Unspecified));
        SetNetworkconnectedEventFlagID(11000801, ON);
    } else {
L1:
        WaitFor(EventFlag(11002805) && InArea(10000, 11002800));
    }
L2:
    EnableCharacterAI(11005800);
    SetNetworkUpdateRate(11005800, true, CharacterUpdateFrequency.AlwaysUpdate);
    DisplayBossHealthBar(Enabled, 11000800, 0, 0);
});

$Event(90005860, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4) {
    if (Signed(X16_4) != 0) {
        Unknown200476(X0_4, X16_4);
    }
    if (EventFlag(X0_4)) {
        DisableCharacter(X8_4);
        DisableCharacterCollision(X8_4);
        ForceCharacterDeath(X8_4, false);
        EndIf(!PlayerIsInOwnWorld());
        EndIf(Signed(X16_4) == 0);
        WaitFixedTimeSeconds(1);
        AwardItemsIncludingClients(X16_4);
        EndEvent();
    }
L0:
    WaitFor(CharacterHPValue(X8_4) <= 0);
    WaitFixedTimeSeconds(2);
    PlaySE(X8_4, SoundType.SFX, 888880000);
    WaitFor(CharacterDead(X8_4));
    GotoIf(S0, X12_4 == 3);
    if (X12_4 != 2) {
        if (X12_4 != 1) {
            HandleBossDefeatAndDisplayBanner(X8_4, TextBannerType.EnemyFelled);
            Goto(L1);
        }
        HandleBossDefeatAndDisplayBanner(X8_4, TextBannerType.GreatEnemyFelled);
    }
    Goto(L1);
S0:
    HandleBossDefeatAndDisplayBanner(X8_4, TextBannerType.DemigodFelled);
    Goto(L1);
    HandleBossDefeatAndDisplayBanner(X8_4, TextBannerType.LegendFelled);
L1:
    SetEventFlagID(X0_4, ON);
    if (X4_4 != 0) {
        SetEventFlagID(X4_4, ON);
    }
    EndIf(!PlayerIsInOwnWorld());
    EndIf(Signed(X16_4) == 0);
    WaitFixedTimeSeconds(5);
    AwardItemsIncludingClients(X16_4);
    EndEvent();
    WaitFixedTimeSeconds(X20_4);
});

$Event(90005861, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4) {
    if (Signed(X16_4) != 0) {
        Unknown200476(X0_4, X16_4);
    }
    if (EventFlag(X0_4)) {
        DisableCharacter(X8_4);
        DisableCharacterCollision(X8_4);
        ForceCharacterDeath(X8_4, false);
        EndIf(!PlayerIsInOwnWorld());
        EndIf(Signed(X16_4) == 0);
        WaitFixedTimeSeconds(1);
        AwardItemsIncludingClients(X16_4);
        EndEvent();
    }
L0:
    WaitFor(CharacterHPValue(X8_4) <= 0);
    WaitFixedTimeSeconds(2);
    PlaySE(X8_4, SoundType.SFX, 888880000);
    WaitFor(CharacterDead(X8_4));
    GotoIf(S0, X12_4 == 3);
    if (X12_4 != 2) {
        if (X12_4 != 1) {
            HandleBossDefeatAndDisplayBanner(X8_4, TextBannerType.EnemyFelled);
            Goto(L1);
        }
        HandleBossDefeatAndDisplayBanner(X8_4, TextBannerType.GreatEnemyFelled);
    }
    Goto(L1);
S0:
    HandleBossDefeatAndDisplayBanner(X8_4, TextBannerType.DemigodFelled);
    Goto(L1);
    HandleBossDefeatAndDisplayBanner(X8_4, TextBannerType.LegendFelled);
L1:
    SetEventFlagID(X0_4, ON);
    if (X4_4 != 0) {
        SetEventFlagID(X4_4, ON);
    }
    EndIf(!PlayerIsInOwnWorld());
    EndIf(Signed(X16_4) == 0);
    WaitFixedTimeSeconds(5);
    AwardItemsIncludingClients(X16_4);
    WaitFixedTimeSeconds(2);
    DisplayBlinkingMessage(X20_4);
    EndEvent();
    WaitFixedTimeSeconds(X24_4);
});

$Event(90005870, Default, function(X0_4, X4_4, X8_4) {
    DisableNetworkSync();
    WaitFor(
        CharacterAIState(X0_4, AIStateType.Combat) && FieldBattleBGMActive(X8_4) && !EventFlag(9000));
    GotoIf(L0, !EventFlag(9290));
    GotoIf(L1, !EventFlag(9291));
    WaitFixedTimeSeconds(5);
    RestartEvent();
L0:
    SetEventFlagID(9290, ON);
    WaitFixedTimeSeconds(1);
    DisplayBossHealthBar(Enabled, X0_4, 0, X4_4);
    if (PlayerIsInOwnWorld()) {
        SetNetworkUpdateAuthority(X0_4, AuthorityLevel.Forced);
        SetNetworkUpdateRate(X0_4, true, CharacterUpdateFrequency.AtLeastEvery2Frames);
    }
    WaitFor(
        !(CharacterAIState(X0_4, AIStateType.Combat) && FieldBattleBGMActive(X8_4))
            || CharacterDead(X0_4)
            || EventFlag(9000));
    if (CharacterDead(X0_4)) {
        WaitFixedTimeSeconds(3);
    } else if (!EventFlag(9000)) {
        WaitFixedTimeSeconds(1);
    }
    DisplayBossHealthBar(Disabled, X0_4, 0, X4_4);
    if (PlayerIsInOwnWorld()) {
        SetNetworkUpdateAuthority(X0_4, AuthorityLevel.Normal);
        SetNetworkUpdateRate(X0_4, false, CharacterUpdateFrequency.AtLeastEvery2Frames);
    }
    SetEventFlagID(9290, OFF);
    RestartEvent();
L1:
    SetEventFlagID(9291, ON);
    WaitFixedTimeSeconds(1);
    DisplayBossHealthBar(Enabled, X0_4, 1, X4_4);
    if (PlayerIsInOwnWorld()) {
        SetNetworkUpdateAuthority(X0_4, AuthorityLevel.Forced);
        SetNetworkUpdateRate(X0_4, true, CharacterUpdateFrequency.AtLeastEvery2Frames);
    }
    WaitFor(
        !(CharacterAIState(X0_4, AIStateType.Combat) && FieldBattleBGMActive(X8_4))
            || CharacterDead(X0_4)
            || EventFlag(9000));
    if (CharacterDead(X0_4)) {
        WaitFixedTimeSeconds(3);
    } else if (!EventFlag(9000)) {
        WaitFixedTimeSeconds(1);
    }
    DisplayBossHealthBar(Disabled, X0_4, 1, X4_4);
    if (PlayerIsInOwnWorld()) {
        SetNetworkUpdateAuthority(X0_4, AuthorityLevel.Normal);
        SetNetworkUpdateRate(X0_4, false, CharacterUpdateFrequency.AtLeastEvery2Frames);
    }
    SetEventFlagID(9291, OFF);
    RestartEvent();
});

$Event(90005871, Default, function(X0_4, X4_4, X8_4, X12_4) {
    DisableNetworkSync();
    WaitFor(
        CharacterAIState(X0_4, AIStateType.Combat) && FieldBattleBGMActive(X8_4) && !EventFlag(9000));
    GotoIf(L0, !EventFlag(9290));
    GotoIf(L1, !EventFlag(9291));
    WaitFixedTimeSeconds(5);
    RestartEvent();
L0:
    SetEventFlagID(9290, ON);
    WaitFixedTimeSeconds(1);
    DisplayBossHealthBar(Enabled, X0_4, 0, X4_4);
    if (PlayerIsInOwnWorld()) {
        SetNetworkUpdateAuthority(X0_4, AuthorityLevel.Forced);
        SetNetworkUpdateRate(X0_4, true, CharacterUpdateFrequency.AtLeastEvery2Frames);
        SetNetworkUpdateAuthority(X12_4, AuthorityLevel.Forced);
        SetNetworkUpdateRate(X12_4, true, CharacterUpdateFrequency.AtLeastEvery2Frames);
    }
    WaitFor(
        !(CharacterAIState(X0_4, AIStateType.Combat) && FieldBattleBGMActive(X8_4))
            || CharacterDead(X0_4)
            || EventFlag(9000));
    if (CharacterDead(X0_4)) {
        WaitFixedTimeSeconds(3);
    } else if (!EventFlag(9000)) {
        WaitFixedTimeSeconds(1);
    }
    DisplayBossHealthBar(Disabled, X0_4, 0, X4_4);
    if (PlayerIsInOwnWorld()) {
        SetNetworkUpdateAuthority(X0_4, AuthorityLevel.Normal);
        SetNetworkUpdateRate(X0_4, false, CharacterUpdateFrequency.AtLeastEvery2Frames);
        SetNetworkUpdateAuthority(X12_4, AuthorityLevel.Normal);
        SetNetworkUpdateRate(X12_4, false, CharacterUpdateFrequency.AtLeastEvery2Frames);
    }
    SetEventFlagID(9290, OFF);
    RestartEvent();
L1:
    SetEventFlagID(9291, ON);
    WaitFixedTimeSeconds(1);
    DisplayBossHealthBar(Enabled, X0_4, 1, X4_4);
    if (PlayerIsInOwnWorld()) {
        SetNetworkUpdateAuthority(X0_4, AuthorityLevel.Forced);
        SetNetworkUpdateRate(X0_4, true, CharacterUpdateFrequency.AtLeastEvery2Frames);
        SetNetworkUpdateAuthority(X0_4, AuthorityLevel.Forced);
        SetNetworkUpdateRate(X0_4, true, CharacterUpdateFrequency.AtLeastEvery2Frames);
    }
    WaitFor(
        !(CharacterAIState(X0_4, AIStateType.Combat) && FieldBattleBGMActive(X8_4))
            || CharacterDead(X0_4)
            || EventFlag(9000));
    if (CharacterDead(X0_4)) {
        WaitFixedTimeSeconds(3);
    } else if (!EventFlag(9000)) {
        WaitFixedTimeSeconds(1);
    }
    DisplayBossHealthBar(Disabled, X0_4, 1, X4_4);
    if (PlayerIsInOwnWorld()) {
        SetNetworkUpdateAuthority(X0_4, AuthorityLevel.Normal);
        SetNetworkUpdateRate(X0_4, false, CharacterUpdateFrequency.AtLeastEvery2Frames);
        SetNetworkUpdateAuthority(X0_4, AuthorityLevel.Normal);
        SetNetworkUpdateRate(X0_4, false, CharacterUpdateFrequency.AtLeastEvery2Frames);
    }
    SetEventFlagID(9291, OFF);
    RestartEvent();
});

$Event(90005872, Default, function(X0_4, X4_4, X8_4) {
    DisableNetworkSync();
    if (0 != X8_4) {
        flagHp &= EventFlag(X8_4);
    } else {
        flagHp &= HPRatio(X0_4) <= 0.55;
    }
    flagHp &= FieldBattleBGMActive(X4_4);
    WaitFor(flagHp);
    SetFieldBattleBGMHeatUp(X4_4, true);
    WaitFor(CharacterDead(X0_4) || !FieldBattleBGMActive(X4_4));
    SetFieldBattleBGMHeatUp(X4_4, false);
    WaitFixedTimeSeconds(0.3);
    RestartEvent();
});

$Event(90005880, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_1, X21_1, X22_1, X23_1, X24_4) {
    EndIf(EventFlag(X0_4));
    EndIf(!PlayerIsInOwnWorld());
    EndIf(!EventFlag(X4_4));
    WaitFor(CharacterDead(X12_4));
    WaitFixedTimeSeconds(3);
    HandleBossDefeatAndDisplayBanner(X12_4, TextBannerType.EnemyFelled);
    DeactivateGparamOverride(10);
    AwardItemsIncludingClients(X16_4);
    SetNetworkconnectedEventFlagID(X0_4, ON);
    WaitFixedTimeSeconds(5);
    SetSpEffect(20000, 8870);
    WaitFixedTimeSeconds(2);
    SetEventFlagID(X8_4, ON);
    SetEventFlagID(9295, ON);
    WarpPlayer(X20_1, X21_1, X22_1, X23_1, X24_4, 0);
    EndEvent();
});

$Event(90005881, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_1, X25_1, X26_1, X27_1, X28_4) {
    SetEventFlagID(X8_4, OFF);
    SetEventFlagID(X12_4, OFF);
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(X0_4));
    EndIf(EventFlag(X4_4));
    WaitFor(
        !HasMultiplayerState(MultiplayerState.MultiplayerPending)
            && HasMultiplayerState(MultiplayerState.Singleplayer)
            && ActionButtonInArea(9230, X20_4));
    DisplayGenericDialogAndSetEventFlags(X16_4, PromptType.YESNO, NumberofOptions.TwoButtons, X20_4, 3, X8_4, X12_4, X12_4);
    RestartIf(EventFlag(X12_4));
    RestartIf(
        HasMultiplayerState(MultiplayerState.Multiplayer)
            || HasMultiplayerState(MultiplayerState.MultiplayerPending));
    SetNetworkconnectedEventFlagID(X4_4, ON);
    SetSpEffect(10000, 514);
    WaitFixedTimeFrames(1);
    ForceAnimationPlayback(10000, 60450, false, false, false);
    WaitFixedTimeSeconds(1.5);
    WarpCharacterAndCopyFloorWithFadeout(10000, TargetEntityType.Area, X28_4, -1, 10000, true, true);
    SetEventFlagID(9021, ON);
    EndEvent();
    WarpPlayer(X24_1, X25_1, X26_1, X27_1, X28_4, 0);
});

$Event(90005882, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4, X40_4, X44_4) {
    if (EventFlag(X0_4)) {
        DisableCharacter(X12_4);
        DisableCharacterCollision(X12_4);
        ForceCharacterDeath(X12_4, false);
        DisableAsset(X24_4);
        EndEvent();
    }
L0:
    DisableCharacter(X12_4);
    DisableCharacterCollision(X12_4);
    DisableCharacterAI(X12_4);
    DisableAsset(X24_4);
    EndIf(!EventFlag(X4_4));
    EndIf(!PlayerIsInOwnWorld());
    WaitFixedTimeFrames(1);
    SetEventFlagID(1099002100, ON);
    SetEventFlagID(X8_4, ON);
    SetSpEffect(10000, 190);
    ActivateGparamOverride(0, 0);
    ChangeWeather(Weather.PuffyClouds, -1, false);
    ShootBullet(X28_4, X32_4, 100, 100500, 0, 90, 0);
    DisableCharacter(X20_4);
    DisableCharacterCollision(X20_4);
    DisableCharacterAI(X20_4);
    if (Signed(-1) != X40_4) {
        ForceAnimationPlayback(X12_4, X40_4, false, false, false);
    } else {
        DisableCharacter(X12_4);
        DisableCharacterCollision(X12_4);
    }
    DisableCharacterHPBarDisplay(X12_4);
    SetNetworkconnectedEventFlagID(X4_4, OFF);
    SetSpEffect(10000, 514);
    EnableAsset(X24_4);
    CreateAssetfollowingSFX(X24_4, 200, 806700);
    ForceAnimationPlayback(10000, 60451, false, false, false);
    WaitFixedTimeSeconds(1);
    SetSpEffect(20000, 8870);
    WaitFor(
        !EntityInRadiusOfEntity(10000, X24_4, 12, 1)
            || HasDamageType(X12_4, 10000, DamageType.Unspecified)
            || HasDamageType(X12_4, 0, DamageType.Unspecified));
    SetEventFlagID(1099002100, OFF);
    if (Signed(-1) == X40_4) {
        EnableCharacter(X12_4);
        EnableCharacterCollision(X12_4);
    }
    if (Signed(-1) != X44_4) {
        ForceAnimationPlayback(X12_4, X44_4, false, false, false);
    }
    EnableCharacterAI(X12_4);
    SetNetworkUpdateRate(X12_4, true, CharacterUpdateFrequency.AlwaysUpdate);
    SetEventFlagID(X16_4, ON);
    WaitFixedTimeSeconds(1);
    DisplayBossHealthBar(Enabled, X12_4, 0, X36_4);
});

$Event(90005883, Restart, function(X0_4, X4_4, X8_4) {
    ForceAnimationPlayback(X8_4, 0, true, false, false);
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(X0_4));
    ForceAnimationPlayback(X8_4, 10, true, false, false);
    EndIf(EventFlag(X4_4));
    WaitFor(
        HasMultiplayerState(MultiplayerState.Singleplayer)
            && !HasMultiplayerState(MultiplayerState.MultiplayerPending));
    WaitFixedTimeFrames(1);
    ForceAnimationPlayback(X8_4, 1, true, false, false);
    WaitFor(
        !(HasMultiplayerState(MultiplayerState.Singleplayer)
            && !HasMultiplayerState(MultiplayerState.MultiplayerPending)));
    WaitFixedTimeFrames(1);
    RestartEvent();
});

$Event(90005884, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    SetSpEffect(X8_4, 9531);
    DisableCharacterAI(X8_4);
    DisableCharacterCollision(X8_4);
    DisableAsset(X12_4);
    EndIf(!EventFlag(X0_4));
    EndIf(!EventFlag(X4_4));
    EndIf(!PlayerIsInOwnWorld());
    WaitFixedTimeFrames(1);
    SetSpEffect(X8_4, 9532);
    EnableCharacterCollision(X8_4);
    EnableAsset(X12_4);
});

$Event(90005885, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4) {
    DisableNetworkSync();
    if (EventFlag(X0_4)) {
        EndEvent();
    }
L0:
    WaitFor(EventFlag(X8_4));
    WaitFixedTimeFrames(1);
    if (Signed(0) != X4_4) {
        SetBossBGM(X4_4, BossBGMState.Start);
    } else {
        SetBossBGM(921100, BossBGMState.Start);
    }
    WaitFor(EventFlag(X12_4) || EventFlag(X0_4));
    if (!EventFlag(X0_4)) {
        WaitFixedTimeFrames(1);
        if (Signed(X16_4) != 1) {
            if (Signed(0) != X4_4) {
                SetBossBGM(X4_4, BossBGMState.HeatUp);
            } else {
                SetBossBGM(925000, BossBGMState.HeatUp);
            }
        }
        WaitFor(EventFlag(X0_4));
    }
L1:
    if (Signed(X20_4) != 1) {
        if (Signed(0) != X4_4) {
            SetBossBGM(X4_4, BossBGMState.Stop2);
        } else {
            SetBossBGM(925000, BossBGMState.Stop2);
        }
        EndEvent();
    }
    if (Signed(0) != X4_4) {
        SetBossBGM(X4_4, BossBGMState.Stop1);
    } else {
        SetBossBGM(925000, BossBGMState.Stop1);
    }
});

$Event(91005600, Restart, function(X0_4, X4_4, X8_4) {
    DisableNetworkSync();
    DisableAsset(X4_4);
    DeleteAssetfollowingSFX(X4_4, true);
    WaitFor(
        (HasMultiplayerState(MultiplayerState.Multiplayer)
            || HasMultiplayerState(MultiplayerState.MultiplayerPending)
            || HasMultiplayerState(MultiplayerState.Invasion)
            || HasMultiplayerState(MultiplayerState.InvasionPending))
            || EventFlag(9982));
    EnableAsset(X4_4);
    DeleteAssetfollowingSFX(X4_4, true);
    CreateAssetfollowingSFX(X4_4, 101, X8_4);
    WaitFor(
        !(HasMultiplayerState(MultiplayerState.Multiplayer)
            || HasMultiplayerState(MultiplayerState.MultiplayerPending)
            || HasMultiplayerState(MultiplayerState.Invasion)
            || HasMultiplayerState(MultiplayerState.InvasionPending))
            && !EventFlag(9982));
    RestartEvent();
    WaitFor(EventFlag(X0_4));
});

$Event(90005100, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4, X40_4, X44_4, X48_4, X52_4, X56_4) {
    if (!EventFlag(9000)) {
        DeleteAssetfollowingSFX(X8_4, false);
        WaitFixedTimeFrames(1);
    }
    DeleteAssetfollowingSFX(X8_4, true);
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(EventFlag(X4_4) && !EventFlag(9000));
    CreateAssetfollowingSFX(X8_4, 100, 6400);
    if (X16_4 == 0) {
        SetEventFlagID(X20_4, ON);
    } else if (X16_4 == 1) {
        SetEventFlagID(X24_4, ON);
    } else if (X16_4 == 2) {
        SetEventFlagID(X28_4, ON);
    } else if (X16_4 == 3) {
        SetEventFlagID(X32_4, ON);
    } else if (X16_4 == 4) {
        SetEventFlagID(X36_4, ON);
    } else if (X16_4 == 5) {
        SetEventFlagID(X40_4, ON);
    } else if (X16_4 == 6) {
        SetEventFlagID(X44_4, ON);
    } else if (X16_4 == 7) {
        SetEventFlagID(X48_4, ON);
    } else if (X16_4 == 8) {
        SetEventFlagID(X52_4, ON);
    } else {
        SetEventFlagID(X56_4, ON);
        Goto(L6);
    }
L6:
    if (PlayerIsInOwnWorld()) {
        if (!EventFlag(69080)) {
            WaitFor(PlayerIsInOwnWorld() && !CharacterHasSpEffect(10000, 100680));
            SetEventFlagID(710510, ON);
            ShowTutorialPopup(1510, true, true);
            DirectlyGivePlayerItem(ItemType.Goods, 9108, 710510, 1);
            SetEventFlagID(69080, ON);
        }
    }
L5:
    EndEvent();
    DeleteAssetfollowingSFX(X8_4, false);
    EndIf(!PlayerIsInOwnWorld());
    if (EventFlag(X0_4)) {
        SetEventFlagID(X20_4, OFF);
        SetEventFlagID(X24_4, OFF);
        SetEventFlagID(X28_4, OFF);
        SetEventFlagID(X32_4, OFF);
        SetEventFlagID(X36_4, OFF);
        SetEventFlagID(X40_4, OFF);
        SetEventFlagID(X44_4, OFF);
        SetEventFlagID(X48_4, OFF);
        SetEventFlagID(X52_4, OFF);
        SetEventFlagID(X56_4, OFF);
        EndEvent();
    }
L3:
    EndIf(EventValue(X12_4, 4) > X16_4);
    WaitFor(EventFlag(X0_4) || (EventFlag(X4_4) && !EventFlag(9000)));
    RestartIf(EventValue(X12_4, 4) > X16_4);
    CreateAssetfollowingSFX(X8_4, 100, 6400);
    if (X16_4 == 0) {
        SetEventFlagID(X20_4, ON);
        EventValueOperation(X12_4, 4, 0, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X20_4, OFF);
    }
    if (X16_4 == 1) {
        SetEventFlagID(X24_4, ON);
        EventValueOperation(X12_4, 4, 1, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X24_4, OFF);
    }
    if (X16_4 == 2) {
        SetEventFlagID(X28_4, ON);
        EventValueOperation(X12_4, 4, 2, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X28_4, OFF);
    }
    if (X16_4 == 3) {
        SetEventFlagID(X32_4, ON);
        EventValueOperation(X12_4, 4, 3, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X32_4, OFF);
    }
    if (X16_4 == 4) {
        SetEventFlagID(X36_4, ON);
        EventValueOperation(X12_4, 4, 4, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X36_4, OFF);
    }
    if (X16_4 == 5) {
        SetEventFlagID(X40_4, ON);
        EventValueOperation(X12_4, 4, 5, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X40_4, OFF);
    }
    if (X16_4 == 6) {
        SetEventFlagID(X40_4, ON);
        EventValueOperation(X12_4, 4, 6, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X40_4, OFF);
    }
    if (X16_4 == 7) {
        SetEventFlagID(X40_4, ON);
        EventValueOperation(X12_4, 4, 7, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X40_4, OFF);
    }
    if (X16_4 == 8) {
        SetEventFlagID(X40_4, ON);
        EventValueOperation(X12_4, 4, 8, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X40_4, OFF);
    }
    if (X16_4 == 9) {
        SetEventFlagID(X40_4, ON);
        EventValueOperation(X12_4, 4, 9, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X40_4, OFF);
    }
    WaitFor(EventValue(X12_4, 4) != X16_4 || EventFlag(X0_4));
    WaitFixedTimeFrames(1);
    RestartEvent();
});

$Event(90005101, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4, X40_4, X44_4, X48_4, X52_4, X56_4) {
    if (!EventFlag(9000)) {
        DeleteAssetfollowingSFX(X8_4, false);
        WaitFixedTimeFrames(1);
    }
    DeleteAssetfollowingSFX(X8_4, true);
    EndIf(!PlayerIsInOwnWorld());
    WaitFor(EventFlag(X4_4) && !EventFlag(9000));
    CreateAssetfollowingSFX(X8_4, 100, 6401);
    if (X16_4 == 0) {
        SetEventFlagID(X20_4, ON);
    } else if (X16_4 == 1) {
        SetEventFlagID(X24_4, ON);
    } else if (X16_4 == 2) {
        SetEventFlagID(X28_4, ON);
    } else if (X16_4 == 3) {
        SetEventFlagID(X32_4, ON);
    } else if (X16_4 == 4) {
        SetEventFlagID(X36_4, ON);
    } else if (X16_4 == 5) {
        SetEventFlagID(X40_4, ON);
    } else if (X16_4 == 6) {
        SetEventFlagID(X44_4, ON);
    } else if (X16_4 == 7) {
        SetEventFlagID(X48_4, ON);
    } else if (X16_4 == 8) {
        SetEventFlagID(X52_4, ON);
    } else {
        SetEventFlagID(X56_4, ON);
        Goto(L6);
    }
L6:
    if (PlayerIsInOwnWorld()) {
        if (!EventFlag(710510)) {
            WaitFor(PlayerIsInOwnWorld() && !CharacterHasSpEffect(10000, 100680));
            SetEventFlagID(710510, ON);
            ShowTutorialPopup(1510, true, true);
            DirectlyGivePlayerItem(ItemType.Goods, 9108, 710510, 1);
        }
    }
L5:
    EndEvent();
    DeleteAssetfollowingSFX(X8_4, false);
    EndIf(!PlayerIsInOwnWorld());
    if (EventFlag(X0_4)) {
        SetEventFlagID(X20_4, OFF);
        SetEventFlagID(X24_4, OFF);
        SetEventFlagID(X28_4, OFF);
        SetEventFlagID(X32_4, OFF);
        SetEventFlagID(X36_4, OFF);
        SetEventFlagID(X40_4, OFF);
        SetEventFlagID(X44_4, OFF);
        SetEventFlagID(X48_4, OFF);
        SetEventFlagID(X52_4, OFF);
        SetEventFlagID(X56_4, OFF);
        EndEvent();
    }
L3:
    EndIf(EventValue(X12_4, 4) > X16_4);
    WaitFor(EventFlag(X0_4) || (EventFlag(X4_4) && !EventFlag(9000)));
    RestartIf(EventValue(X12_4, 4) > X16_4);
    CreateAssetfollowingSFX(X8_4, 100, 6401);
    if (X16_4 == 0) {
        SetEventFlagID(X20_4, ON);
        EventValueOperation(X12_4, 4, 0, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X20_4, OFF);
    }
    if (X16_4 == 1) {
        SetEventFlagID(X24_4, ON);
        EventValueOperation(X12_4, 4, 1, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X24_4, OFF);
    }
    if (X16_4 == 2) {
        SetEventFlagID(X28_4, ON);
        EventValueOperation(X12_4, 4, 2, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X28_4, OFF);
    }
    if (X16_4 == 3) {
        SetEventFlagID(X32_4, ON);
        EventValueOperation(X12_4, 4, 3, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X32_4, OFF);
    }
    if (X16_4 == 4) {
        SetEventFlagID(X36_4, ON);
        EventValueOperation(X12_4, 4, 4, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X36_4, OFF);
    }
    if (X16_4 == 5) {
        SetEventFlagID(X40_4, ON);
        EventValueOperation(X12_4, 4, 5, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X40_4, OFF);
    }
    if (X16_4 == 6) {
        SetEventFlagID(X40_4, ON);
        EventValueOperation(X12_4, 4, 6, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X40_4, OFF);
    }
    if (X16_4 == 7) {
        SetEventFlagID(X40_4, ON);
        EventValueOperation(X12_4, 4, 7, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X40_4, OFF);
    }
    if (X16_4 == 8) {
        SetEventFlagID(X40_4, ON);
        EventValueOperation(X12_4, 4, 8, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X40_4, OFF);
    }
    if (X16_4 == 9) {
        SetEventFlagID(X40_4, ON);
        EventValueOperation(X12_4, 4, 9, 0, 1, CalculationType.Assign);
    } else {
        SetEventFlagID(X40_4, OFF);
    }
    WaitFor(EventValue(X12_4, 4) != X16_4 || EventFlag(X0_4));
    WaitFixedTimeFrames(1);
    RestartEvent();
});

$Event(90005110, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4) {
    EndIf(EventFlag(X0_4));
    EndIf(!PlayerIsInOwnWorld());
    EndIf(!EventFlag(X4_4));
    DeleteAssetfollowingSFX(X8_4, true);
    CreateAssetfollowingSFX(X8_4, 100, X20_4);
    WaitFor(PlayerIsInOwnWorld() && ActionButtonInArea(X24_4, X8_4));
    RotateCharacter(10000, X8_4, -1, true);
    ForceAnimationPlayback(10000, X28_4, false, false, false);
    DeleteAssetfollowingSFX(X8_4, true);
    WaitFixedTimeSeconds(4);
    DisplayBanner(TextBannerType.GreatRuneRestored);
    AwardItemsIncludingClients(X12_4);
    RemoveItemFromPlayer(ItemType.Goods, X16_4, 1);
    SetEventFlagID(X0_4, ON);
    EndEvent();
    EndIf(Signed(X32_4) == 0);
});

$Event(9005910, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    DeleteAssetfollowingSFX(X0_4, true);
    GotoIf(L1, !AnyBatchEventFlags(X4_4, X8_4));
    GotoIf(L2, !AllBatchEventFlags(X4_4, X8_4));
    Goto(L9);
L1:
    if (Signed(3) >= X12_4) {
        CreateAssetfollowingSFX(X0_4, 201, 62);
    } else {
        CreateAssetfollowingSFX(X0_4, 201, 63);
    }
    WaitFor(AnyBatchEventFlags(X4_4, X8_4));
    RestartEvent();
L2:
    CreateAssetfollowingSFX(X0_4, 201, 61);
    WaitFor(AllBatchEventFlags(X4_4, X8_4));
    RestartEvent();
L9:
    DeleteAssetfollowingSFX(X0_4, true);
    EndEvent();
});

$Event(9005911, Restart, function(X0_4) {
    CreateAssetfollowingSFX(X0_4, 201, 40);
    WaitFor(EntityInRadiusOfEntity(10000, X0_4, 3, 1));
    DeleteAssetfollowingSFX(X0_4, true);
});

$Event(9005912, Restart, function(X0_4, X4_4) {
    EndIf(EventFlag(X0_4));
    WaitFor(EventFlag(X0_4));
    DisplaySubareaWelcomeMessage(X4_4);
});

$Event(9005920, Restart, function(X0_4, X4_4, X8_4, X12_4, X16_4, X20_4, X24_4, X28_4, X32_4, X36_4) {
    if (!EventFlag(9800)) {
        DisableCharacter(X0_4);
        DisableCharacterCollision(X0_4);
    } else {
        EnableCharacter(X0_4);
        EnableCharacterCollision(X0_4);
    }
    if (!EventFlag(9801)) {
        DisableCharacter(X4_4);
        DisableCharacterCollision(X4_4);
    } else {
        EnableCharacter(X4_4);
        EnableCharacterCollision(X4_4);
    }
    if (!EventFlag(9802)) {
        DisableCharacter(X8_4);
        DisableCharacterCollision(X8_4);
    } else {
        EnableCharacter(X8_4);
        EnableCharacterCollision(X8_4);
    }
    if (!EventFlag(9803)) {
        DisableCharacter(X12_4);
        DisableCharacterCollision(X12_4);
    } else {
        EnableCharacter(X12_4);
        EnableCharacterCollision(X12_4);
    }
    if (!EventFlag(9804)) {
        DisableCharacter(X16_4);
        DisableCharacterCollision(X16_4);
    } else {
        EnableCharacter(X16_4);
        EnableCharacterCollision(X16_4);
    }
    if (!EventFlag(9805)) {
        DisableCharacter(X20_4);
        DisableCharacterCollision(X20_4);
    } else {
        EnableCharacter(X20_4);
        EnableCharacterCollision(X20_4);
    }
    if (!EventFlag(9806)) {
        DisableCharacter(X24_4);
        DisableCharacterCollision(X24_4);
    } else {
        EnableCharacter(X24_4);
        EnableCharacterCollision(X24_4);
    }
    if (!EventFlag(9807)) {
        DisableCharacter(X28_4);
        DisableCharacterCollision(X28_4);
    } else {
        EnableCharacter(X28_4);
        EnableCharacterCollision(X28_4);
    }
    if (!EventFlag(9808)) {
        DisableCharacter(X32_4);
        DisableCharacterCollision(X32_4);
    } else {
        EnableCharacter(X32_4);
        EnableCharacterCollision(X32_4);
    }
    if (!EventFlag(9809)) {
        DisableCharacter(X36_4);
        DisableCharacterCollision(X36_4);
    } else {
        EnableCharacter(X36_4);
        EnableCharacterCollision(X36_4);
    }
});

$Event(90005920, Restart, function(X0_4, X4_4, X8_4) {
    EndIf(EventFlag(X0_4));
    CreateAssetfollowingSFX(X4_4, 100, 6150);
    WaitFor(ObjActEventFlag(X8_4));
    SetEventFlagID(X0_4, ON);
    WaitFixedTimeSeconds(0.3);
    DeleteAssetfollowingSFX(X4_4, true);
});

$Event(9005990, Restart, function(X0_4) {
    WaitFixedTimeSeconds(X0_4);
});

// Great Rune - SpEffect Applied on Flag ON
$Event(9005991, Restart, function(X0_4, X4_4, X8_4) {
    if(EventFlag(X4_4))
    {
        SetSpEffect(X0_4, X8_4);
    }
    else
    {
        ClearSpEffect(X0_4, X8_4);
    }
    
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

// Great Rune - SpEffect Applied on Flag OFF
$Event(9005992, Restart, function(X0_4, X4_4, X8_4) {
    if(EventFlag(X4_4))
    {
        ClearSpEffect(X0_4, X8_4);
    }
    else
    {
        SetSpEffect(X0_4, X8_4);
    }
    
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

