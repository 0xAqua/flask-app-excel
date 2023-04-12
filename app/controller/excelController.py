from openpyxl import load_workbook
import os
import getpass


def document_excel(claim_no: str, claim_day: str, payment_day: str, company: str, post_no: str, address: str,
                   manager: str, note: str, item_1: str, item_2: str, item_3: str, item_4: str, item_5: str,
                   item_6: str, item_7: str, item_8: str, item_9: str, item_10: str, item_11: str, item_12: str,
                   item_13: str, item_14: str,
                   quantity_1: int, quantity_2: int, quantity_3: int, quantity_4: int, quantity_5: int,
                   quantity_6: int, quantity_7: int, quantity_8: int, quantity_9: int, quantity_10: int,
                   quantity_11: int, quantity_12: int, quantity_13: int, quantity_14: int,
                   unit_1: str, unit_2: str, unit_3: str, unit_4: str, unit_5: str, unit_6: str, unit_7: str,
                   unit_8: str, unit_9: str, unit_10: str, unit_11: str, unit_12: str, unit_13: str, unit_14: str,
                   unit_price_1: int, unit_price_2: int, unit_price_3: int,
                   unit_price_4: int, unit_price_5: int, unit_price_6: int, unit_price_7: int, unit_price_8: int,
                   unit_price_9: int, unit_price_10: int, unit_price_11: int, unit_price_12: int, unit_price_13: int,
                   unit_price_14: int,
                   amount_1: int, amount_2: int, amount_3: int, amount_4: int, amount_5: int, amount_6: int,
                   amount_7: int, amount_8: int, amount_9: int, amount_10: int, amount_11: int, amount_12: int,
                   amount_13: int, amount_14: int,
                   sub_total: int, total: int, tax: int):
    filename = "./static/excel/請求書.xlsx"

    workbook = load_workbook(filename=filename)

    worksheet = workbook["Sheet1"]

    claim_no_rename = claim_no[5:9]

    worksheet["N4"] = claim_no_rename
    worksheet["N5"] = claim_day.replace('-', '/')
    worksheet["N6"] = payment_day.replace('-', '/')
    worksheet["B4"] = company
    worksheet["B5"] = post_no
    worksheet["B6"] = address
    worksheet["B10"] = manager
    worksheet["C44"] = note
    worksheet["B17"] = item_1
    worksheet["B18"] = item_2
    worksheet["B19"] = item_3
    worksheet["B20"] = item_4
    worksheet["B21"] = item_5
    worksheet["B22"] = item_6
    worksheet["B23"] = item_7
    worksheet["B24"] = item_8
    worksheet["B25"] = item_9
    worksheet["B26"] = item_10
    worksheet["B27"] = item_11
    worksheet["B28"] = item_12
    worksheet["B29"] = item_13
    worksheet["B30"] = item_14
    worksheet["J17"] = quantity_1
    worksheet["J18"] = quantity_2
    worksheet["J19"] = quantity_3
    worksheet["J20"] = quantity_4
    worksheet["J21"] = quantity_5
    worksheet["J22"] = quantity_6
    worksheet["J23"] = quantity_7
    worksheet["J24"] = quantity_8
    worksheet["J25"] = quantity_9
    worksheet["J26"] = quantity_10
    worksheet["J27"] = quantity_11
    worksheet["J28"] = quantity_12
    worksheet["J29"] = quantity_13
    worksheet["J30"] = quantity_14
    worksheet["K17"] = unit_1
    worksheet["K18"] = unit_2
    worksheet["K19"] = unit_3
    worksheet["K20"] = unit_4
    worksheet["K21"] = unit_5
    worksheet["K22"] = unit_6
    worksheet["K23"] = unit_7
    worksheet["K24"] = unit_8
    worksheet["K25"] = unit_9
    worksheet["K26"] = unit_10
    worksheet["K27"] = unit_11
    worksheet["K28"] = unit_12
    worksheet["K29"] = unit_13
    worksheet["K30"] = unit_14
    worksheet["L17"] = '¥' + '{:,.0f}'.format(int(unit_price_1) if unit_price_1 else 0)
    worksheet["L18"] = '¥' + '{:,.0f}'.format(int(unit_price_2) if unit_price_2 else 0)
    worksheet["L19"] = '¥' + '{:,.0f}'.format(int(unit_price_3) if unit_price_3 else 0)
    worksheet["L20"] = '¥' + '{:,.0f}'.format(int(unit_price_4) if unit_price_4 else 0)
    worksheet["L21"] = '¥' + '{:,.0f}'.format(int(unit_price_5) if unit_price_5 else 0)
    worksheet["L22"] = '¥' + '{:,.0f}'.format(int(unit_price_6) if unit_price_6 else 0)
    worksheet["L23"] = '¥' + '{:,.0f}'.format(int(unit_price_7) if unit_price_7 else 0)
    worksheet["L24"] = '¥' + '{:,.0f}'.format(int(unit_price_8) if unit_price_8 else 0)
    worksheet["L25"] = '¥' + '{:,.0f}'.format(int(unit_price_9) if unit_price_9 else 0)
    worksheet["L26"] = '¥' + '{:,.0f}'.format(int(unit_price_10) if unit_price_10 else 0)
    worksheet["L27"] = '¥' + '{:,.0f}'.format(int(unit_price_11) if unit_price_11 else 0)
    worksheet["L28"] = '¥' + '{:,.0f}'.format(int(unit_price_12) if unit_price_12 else 0)
    worksheet["L29"] = '¥' + '{:,.0f}'.format(int(unit_price_13) if unit_price_13 else 0)
    worksheet["L30"] = '¥' + '{:,.0f}'.format(int(unit_price_14) if unit_price_14 else 0)
    worksheet["O17"] = '¥' + '{:,.0f}'.format(int(amount_1))
    worksheet["O18"] = '¥' + '{:,.0f}'.format(int(amount_2))
    worksheet["O19"] = '¥' + '{:,.0f}'.format(int(amount_3))
    worksheet["O20"] = '¥' + '{:,.0f}'.format(int(amount_4))
    worksheet["O21"] = '¥' + '{:,.0f}'.format(int(amount_5))
    worksheet["O22"] = '¥' + '{:,.0f}'.format(int(amount_6))
    worksheet["O23"] = '¥' + '{:,.0f}'.format(int(amount_7))
    worksheet["O24"] = '¥' + '{:,.0f}'.format(int(amount_8))
    worksheet["O25"] = '¥' + '{:,.0f}'.format(int(amount_9))
    worksheet["O26"] = '¥' + '{:,.0f}'.format(int(amount_10))
    worksheet["O27"] = '¥' + '{:,.0f}'.format(int(amount_11))
    worksheet["O28"] = '¥' + '{:,.0f}'.format(int(amount_12))
    worksheet["O29"] = '¥' + '{:,.0f}'.format(int(amount_13))
    worksheet["O30"] = '¥' + '{:,.0f}'.format(int(amount_14))
    worksheet["L34"] = '¥' + '{:,.0f}'.format(int(sub_total) if sub_total else 0)
    worksheet["L35"] = '¥' + '{:,.0f}'.format(int(tax) if tax else 0)
    worksheet["L36"] = '¥' + '{:,.0f}'.format(int(total) if total else 0)
    worksheet["E12"] = '¥' + '{:,.0f}'.format(int(total) if total else 0)

    dir = claim_day[0:4]
    user = getpass.getuser()
    path = f'/Users/{user}/Desktop'

    path_dir = f"{path}/{dir}"

    if not os.path.exists(path_dir):
        os.makedirs(os.path.join(path, dir))  # ディレクトリ作成
    workbook.save(filename=f"{path}/{dir}/{claim_no_rename + company}.xlsx")
    workbook.close()
