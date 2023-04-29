import isystem.connect as ic
import time

import parameters as P
import CANoe
import helper

r = helper.Riden_Connect()
app = CANoe.CanoeSync()

helper.Lunch_App(app)

while (app == None):
    pass  # Do nothing in particular while app is loading

app.Start()

time.sleep(5)


def test_1101_1():
    connMgr = ic.ConnectionMgr()
    connMgr.connectMRU('')
    tcCtrl = ic.CTestCaseController(connMgr, 0)

    helper.STD_PRECONDITION_SIM(app, r)

    time.sleep(1)

    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1MsgSts_na,d"))
    assert eval_value == 2, "1s_PSFAS_INP_Mot1MsgSts_na Failed, s_PSFAS_INP_Mot1MsgSts_na = " + \
                            str(eval_value)
    eval_value = int(tcCtrl.evaluate("s_PSFQM_INP_Mot1MsgErrSts_na,d"))
    assert eval_value == 0, "1s_PSFQM_INP_Mot1MsgErrSts_na Failed, s_PSFQM_INP_Mot1MsgErrSts_na = " + \
                            str(eval_value)


def test_1101_2():
    connMgr = ic.ConnectionMgr()
    connMgr.connectMRU('')
    tcCtrl = ic.CTestCaseController(connMgr, 0)

    helper.STD_PRECONDITION_SIM(app, r)

    time.sleep(1)

    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1MsgSts_na,d"))
    assert eval_value == 4, "1s_PSFAS_INP_Mot1MsgSts_na Failed, s_PSFAS_INP_Mot1MsgSts_na = " + \
                            str(eval_value)

    eval_value = int(tcCtrl.evaluate("s_PSFQM_INP_Mot1MsgErrSts_na,d"))
    assert eval_value == 1, "1s_PSFQM_INP_Mot1MsgErrSts_na Failed, s_PSFQM_INP_Mot1MsgErrSts_na = " + \
                            str(eval_value)


def test_1101_3():
    connMgr = ic.ConnectionMgr()
    connMgr.connectMRU('')
    tcCtrl = ic.CTestCaseController(connMgr, 0)

    helper.STD_PRECONDITION_SIM(app, r)

    helper.SetSignalValue(app, P.SA1_Blockade_Pos, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFQM_INP_Mot1BlkPos_Deg,d"))
    assert eval_value == 0, "1s_PSFQM_INP_Mot1BlkPos_Deg Failed, s_PSFQM_INP_Mot1BlkPos_Deg = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.SA1_Blockade_Pos, 4095)
    eval_value = int(tcCtrl.evaluate("s_PSFQM_INP_Mot1BlkPos_Deg,d"))
    assert eval_value == 4095, "1s_PSFQM_INP_Mot1BlkPos_Deg Failed, s_PSFQM_INP_Mot1BlkPos_Deg = " + \
                               str(eval_value)

    helper.SetSignalValue(app, P.SA1_Initialisiert, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1Init_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1Init_In_b Failed, s_PSFAS_INP_Mot1Init_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.SA1_Initialisiert, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1Init_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1Init_In_b Failed, s_PSFAS_INP_Mot1Init_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.SA1_Ist_Drehrichtung, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1Dir_na,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1Dir_na Failed, s_PSFAS_INP_Mot1Dir_na = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.SA1_Ist_Drehrichtung, 3)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1Dir_na,d"))
    assert eval_value == 3, "2s_PSFAS_INP_Mot1Dir_na Failed, s_PSFAS_INP_Mot1Dir_na = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.SA1_Ist_Pos, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1Pos_In_Deg,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1Pos_In_Deg Failed, s_PSFAS_INP_Mot1Pos_In_Deg = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.SA1_Ist_Pos, 4095)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1Pos_In_Deg,d"))
    assert eval_value == 4095, "2s_PSFAS_INP_Mot1Pos_In_Deg Failed, s_PSFAS_INP_Mot1Pos_In_Deg = " + \
                               str(eval_value)

    helper.SetSignalValue(app, P.SA1_Pos_erreicht, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1PosRchd_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1PosRchd_In_b Failed, s_PSFAS_INP_Mot1PosRchd_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.SA1_Pos_erreicht, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1PosRchd_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1PosRchd_In_b Failed, s_PSFAS_INP_Mot1PosRchd_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.SA1_Referenziert, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1Ref_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1Ref_In_b Failed, s_PSFAS_INP_Mot1Ref_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.SA1_Referenziert, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1Ref_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1Ref_In_b Failed, s_PSFAS_INP_Mot1Ref_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.SA1_Blockade_Pos, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1RespErr_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1RespErr_In_b Failed, s_PSFAS_INP_Mot1RespErr_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.SA1_ResponseError, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1RespErr_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1RespErr_In_b Failed, s_PSFAS_INP_Mot1RespErr_In_b = " + \
                            str(eval_value)


def test_1101_4():
    connMgr = ic.ConnectionMgr()
    connMgr.connectMRU('')
    tcCtrl = ic.CTestCaseController(connMgr, 0)

    helper.STD_PRECONDITION_SIM(app, r)

    helper.SetSignalValue(app, P.R_SA1_Fehler_1, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1BlkLow_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1BlkLow_b Failed, s_PSFAS_INP_Mot1BlkLow_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_1, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1BlkLow_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1BlkLow_b Failed, s_PSFAS_INP_Mot1BlkLow_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_2, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1BlkUp_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1BlkUp_b Failed, s_PSFAS_INP_Mot1BlkUp_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_2, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1BlkUp_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1BlkUp_b Failed, s_PSFAS_INP_Mot1BlkUp_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_3, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1MechFree_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1MechFree_In_b Failed, s_PSFAS_INP_Mot1MechFree_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_3, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1MechFree_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1MechFree_In_b Failed, s_PSFAS_INP_Mot1MechFree_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_4, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1RefInitErr_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1RefInitErr_In_b Failed, s_PSFAS_INP_Mot1RefInitErr_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_4, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1RefInitErr_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1RefInitErr_In_b Failed, s_PSFAS_INP_Mot1RefInitErr_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_5, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1TempWarn_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1TempWarn_In_b Failed, s_PSFAS_INP_Mot1TempWarn_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_5, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1TempWarn_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1TempWarn_In_b Failed, s_PSFAS_INP_Mot1TempWarn_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_6, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1TempProt_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1TempProt_In_b Failed, s_PSFAS_INP_Mot1TempProt_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_6, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1TempProt_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1TempProt_In_b Failed, s_PSFAS_INP_Mot1TempProt_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_7, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1OverVolt_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1OverVolt_In_b Failed, s_PSFAS_INP_Mot1OverVolt_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_7, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1OverVolt_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1OverVolt_In_b Failed, s_PSFAS_INP_Mot1OverVolt_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_8, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1HighVolt_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1HighVolt_In_b Failed, s_PSFAS_INP_Mot1HighVolt_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_8, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1HighVolt_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1HighVolt_In_b Failed, s_PSFAS_INP_Mot1HighVolt_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_9, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1UnderVolt_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1UnderVolt_In_b Failed, s_PSFAS_INP_Mot1UnderVolt_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_9, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1UnderVolt_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1UnderVolt_In_b Failed, s_PSFAS_INP_Mot1UnderVolt_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_10, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1LowVolt_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1LowVolt_In_b Failed, s_PSFAS_INP_Mot1LowVolt_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_10, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1LowVolt_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1LowVolt_In_b Failed, s_PSFAS_INP_Mot1LowVolt_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_11, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1Err_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1Err_In_b Failed, s_PSFAS_INP_Mot1Err_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_11, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1Err_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1RespErr_In_b Failed, s_PSFAS_INP_Mot1Err_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_12, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1SnsrErr_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1SnsrErr_In_b Failed, s_PSFAS_INP_Mot1SnsrErr_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_12, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1SnsrErr_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1SnsrErr_In_b Failed, s_PSFAS_INP_Mot1SnsrErr_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_13, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1IncSnsrErr_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1IncSnsrErr_In_b  Failed, s_PSFAS_INP_Mot1IncSnsrErr_In_b  = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_13, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1IncSnsrErr_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1IncSnsrErr_In_b  Failed, s_PSFAS_INP_Mot1IncSnsrErr_In_b  = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_14, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1IncErr_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1IncErr_In_b Failed, s_PSFAS_INP_Mot1IncErr_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_14, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1IncErr_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1IncErr_In_b Failed, s_PSFAS_INP_Mot1IncErr_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_15, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1MechPlausErr_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1MechPlausErr_b Failed, s_PSFAS_INP_Mot1MechPlausErr_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_15, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1MechPlausErr_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1MechPlausErr_b Failed, s_PSFAS_INP_Mot1MechPlausErr_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_16, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1E2eCommErr_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1E2eCommErr_In_b Failed, s_PSFAS_INP_Mot1E2eCommErr_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_16, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1E2eCommErr_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1E2eCommErr_In_b Failed, s_PSFAS_INP_Mot1E2eCommErr_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_17, 0)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1DatasetErr_In_b,d"))
    assert eval_value == 0, "1s_PSFAS_INP_Mot1DatasetErr_In_b Failed, s_PSFAS_INP_Mot1DatasetErr_In_b = " + \
                            str(eval_value)

    helper.SetSignalValue(app, P.R_SA1_Fehler_17, 1)
    eval_value = int(tcCtrl.evaluate("s_PSFAS_INP_Mot1DatasetErr_In_b,d"))
    assert eval_value == 1, "2s_PSFAS_INP_Mot1DatasetErr_In_b Failed, s_PSFAS_INP_Mot1DatasetErr_In_b = " + \
                            str(eval_value)
