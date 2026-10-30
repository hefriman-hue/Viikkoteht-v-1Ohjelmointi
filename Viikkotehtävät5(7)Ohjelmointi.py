tuotteet =[
    "PHILIPS_Vedenkeitin_HD4646_2020_09_21_C_1",
    "KENWOOD_Yleiskone_KVL8300S_2015_09_22_C_3",
    "BOCH_Tehosekoitin_MMB65GM_2016_05_07_C_3",
    "WHIRLPOOL_Mikroaaltouuni_MCP345WH_2019_01_15_C_1",
    "ROSENLEW_Pakastin_RPP2330_2017_01_29_C_2",
    "ElEKTROLUX_Jääkaappi_ERF4114AOW_2017_11_07_C_2"
]
kategoriat={
    "1": "Pienlaitteet",
    "2": "Kylmälaitteet",
    "3": "Sekoittimet"
}
for tuote in tuotteet:
    osat =tuote.split("_")
    valmistaja = osat[0]
    nimi = osat[1]
    malli = osat[2]
    vuosi = osat[3]
    kuukausi = osat[4]
    paiva = osat[5]
    kategoria = kategoriat[osat[7]]
    print(f"Valmistaja: {valmistaja}")
    print(f"Nimi ja malli: {nimi}({malli})")
    print(f"Kategoria: {kategoria}")
    print(f"Lisäyspäivämäärä:{int(paiva)}.{int(kuukausi)}.{int(vuosi)}")
    print()
