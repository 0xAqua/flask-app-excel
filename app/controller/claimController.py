from flask import Flask, render_template, request, redirect, url_for

import settings
from app.models.db import DataBase
from app.controller.excelController import document_excel

app = Flask(__name__, template_folder="../../templates", static_folder="../../static")
invoice_db = DataBase("invoice")


class WebServer(object):
    @staticmethod
    def start(debug=False):
        sql = '''
            "invoice_ID" INTEGER PRIMARY KEY AUTOINCREMENT,
            "claim_no"	INTEGER,
            "claim_day" TEXT,
            "payment_day" TEXT,
            "company" TEXT,
            "post_no" TEXT,
            "address" TEXT,
            "manager" TEXT,
            "note" TEXT,
            "tax" INTEGER,
            "total" INTEGER,
            "create_at" TEXT
        '''
        invoice_db.create_db(sql)
        app.run(host='0.0.0.0', port=settings.PORT, debug=debug)


server = WebServer()


@app.route('/')
def index() -> str:
    return render_template('index.html')


@app.route('/process_form', methods=['POST'])
def process_form():
    process = request.form['submit-action']

    claim_no = request.form["claim__no"]
    claim_day = request.form["claim__day"]
    payment_day = request.form["payment__day"]
    company = request.form["company"]
    post_no = request.form["post__no"]
    address = request.form["address"]
    manager = request.form["manager"]
    note = request.form["note"]
    item_1 = request.form["item__1"]
    item_2 = request.form["item__2"]
    item_3 = request.form["item__3"]
    item_4 = request.form["item__4"]
    item_5 = request.form["item__5"]
    item_6 = request.form["item__6"]
    item_7 = request.form["item__7"]
    item_8 = request.form["item__8"]
    item_9 = request.form["item__9"]
    item_10 = request.form["item__10"]
    item_11 = request.form["item__11"]
    item_12 = request.form["item__12"]
    item_13 = request.form["item__13"]
    item_14 = request.form["item__14"]
    unit_price_1 = request.form["unit__price__1"]
    unit_price_2 = request.form["unit__price__2"]
    unit_price_3 = request.form["unit__price__3"]
    unit_price_4 = request.form["unit__price__4"]
    unit_price_5 = request.form["unit__price__5"]
    unit_price_6 = request.form["unit__price__6"]
    unit_price_7 = request.form["unit__price__7"]
    unit_price_8 = request.form["unit__price__8"]
    unit_price_9 = request.form["unit__price__9"]
    unit_price_10 = request.form["unit__price__10"]
    unit_price_11 = request.form["unit__price__11"]
    unit_price_12 = request.form["unit__price__12"]
    unit_price_13 = request.form["unit__price__13"]
    unit_price_14 = request.form["unit__price__14"]
    unit_1 = request.form["unit_1"]
    unit_2 = request.form["unit_2"]
    unit_3 = request.form["unit_3"]
    unit_4 = request.form["unit_4"]
    unit_5 = request.form["unit_5"]
    unit_6 = request.form["unit_6"]
    unit_7 = request.form["unit_7"]
    unit_8 = request.form["unit_8"]
    unit_9 = request.form["unit_9"]
    unit_10 = request.form["unit_10"]
    unit_11 = request.form["unit_11"]
    unit_12 = request.form["unit_12"]
    unit_13 = request.form["unit_13"]
    unit_14 = request.form["unit_14"]
    quantity_1 = request.form["quantity__1"]
    quantity_2 = request.form["quantity__2"]
    quantity_3 = request.form["quantity__3"]
    quantity_4 = request.form["quantity__4"]
    quantity_5 = request.form["quantity__5"]
    quantity_6 = request.form["quantity__6"]
    quantity_7 = request.form["quantity__7"]
    quantity_8 = request.form["quantity__8"]
    quantity_9 = request.form["quantity__9"]
    quantity_10 = request.form["quantity__10"]
    quantity_11 = request.form["quantity__11"]
    quantity_12 = request.form["quantity__12"]
    quantity_13 = request.form["quantity__13"]
    quantity_14 = request.form["quantity__14"]
    amount_1 = request.form["amount__1"]
    amount_2 = request.form["amount__2"]
    amount_3 = request.form["amount__3"]
    amount_4 = request.form["amount__4"]
    amount_5 = request.form["amount__5"]
    amount_6 = request.form["amount__6"]
    amount_7 = request.form["amount__7"]
    amount_8 = request.form["amount__8"]
    amount_9 = request.form["amount__9"]
    amount_10 = request.form["amount__10"]
    amount_11 = request.form["amount__11"]
    amount_12 = request.form["amount__12"]
    amount_13 = request.form["amount__13"]
    amount_14 = request.form["amount__14"]
    sub_total = request.form["sub_total"]
    tax = request.form["tax"]
    total = request.form["total"]

    if process == 'PDF 保存':
        print("PDF")
    else:
        print("Excel")

        document_excel(claim_no, claim_day, payment_day, company, post_no, address, manager, note,
                       item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11,
                       item_12, item_13, item_14,
                       quantity_1, quantity_2, quantity_3, quantity_4, quantity_5, quantity_6, quantity_7, quantity_8,
                       quantity_9, quantity_10, quantity_11, quantity_12, quantity_13, quantity_14,
                       unit_1, unit_2, unit_3, unit_4, unit_5, unit_6, unit_7, unit_8, unit_9, unit_10, unit_11,
                       unit_12, unit_13, unit_14,
                       unit_price_1, unit_price_2, unit_price_3, unit_price_4, unit_price_5, unit_price_6,
                       unit_price_7, unit_price_8, unit_price_9, unit_price_10, unit_price_11, unit_price_12,
                       unit_price_13, unit_price_14,
                       amount_1, amount_2, amount_3, amount_4, amount_5, amount_6, amount_7, amount_8, amount_9,
                       amount_10, amount_11, amount_12, amount_13, amount_14,
                       sub_total, total, tax)

        print("完了")

    return redirect(url_for('index'))
