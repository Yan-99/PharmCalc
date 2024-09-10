from project import cal_age_points_M, cal_age_points_F
from project import cal_smoke_points_M, cal_smoke_points_F
from project import cal_BP_points_M, cal_BP_points_F
from project import cal_TC_points_M, cal_TC_points_F
from project import cal_HDL_points, cal_ASCVDRiskScore_M, cal_ASCVDRiskScore_F

def test_age_points():
    assert cal_age_points_M(85) == 13
    assert cal_age_points_M(55) == 8
    assert cal_age_points_M(19) == -9
    assert cal_age_points_F(85) == 16
    assert cal_age_points_F(55) == 8
    assert cal_age_points_F(19) == -7

def test_smoke_points():
    assert cal_smoke_points_M("N", 55) == 0
    assert cal_smoke_points_M("Y", 55) == 3
    assert cal_smoke_points_F("N", 55) == 0
    assert cal_smoke_points_F("Y", 55) == 4

def test_BP_points_M():
    assert cal_BP_points_M(119,"Y") == 0
    assert cal_BP_points_M(135,"Y") == 2
    assert cal_BP_points_M(170,"Y") == 3
    assert cal_BP_points_M(135,"N") == 1
    assert cal_BP_points_M(170,"N") == 2

def test_BP_points_F():
    assert cal_BP_points_F(119,"Y") == 0
    assert cal_BP_points_F(135,"Y") == 4
    assert cal_BP_points_F(170,"Y") == 6
    assert cal_BP_points_F(135,"N") == 2
    assert cal_BP_points_F(170,"N") == 4

def test_TC_points():
    assert cal_TC_points_M(3.9, 51) == 0
    assert cal_TC_points_M(5.2, 51) == 3
    assert cal_TC_points_M(11, 51) == 5
    assert cal_TC_points_F(3.9,51) == 0
    assert cal_TC_points_F(5.2,51) == 4
    assert cal_TC_points_F(11,51) == 7

def test_HDL_points():
    assert cal_HDL_points(1.7) == -1
    assert cal_HDL_points(1) == 1
    assert cal_HDL_points(0.9) == 2

def test_ASCVDRiskScore_M():
    assert cal_ASCVDRiskScore_M(-1,"C") == "<1%"
    assert cal_ASCVDRiskScore_M(12,"C") == "4%"
    assert cal_ASCVDRiskScore_M(12,"M") == "7%"
    assert cal_ASCVDRiskScore_M(12,"I") == "10%"

def test_ASCVDRiskScore_F():
    assert cal_ASCVDRiskScore_F(8,"C") == "<1%"
    assert cal_ASCVDRiskScore_F(19,"C") == "3%"
    assert cal_ASCVDRiskScore_F(19,"M") == "5%"
    assert cal_ASCVDRiskScore_F(19,"I") == "7%"
