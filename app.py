# from weasyprint import HTML
import os
import io
from flask import Flask, render_template, send_file, request
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from weasyprint import HTML


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    posted_data = request.get_json() or {}
    today = datetime.today().strftime("%B %-d, %Y")
    default_data = {
        'duedate': (datetime.today() + relativedelta(months=1)).strftime("%B %-d, %Y"),
        'from_addr': {
            'company_name': 'Wittel',
            'addr1': 'Av. Francisco Matarazzo, 1500',
            'addr2': 'Barra Funda - São Paulo - SP'
        },
        'invoice_number': 123,
        'items': [
            {'title': 'website design', 'charge': 300.00},
            {'title': 'Hosting (3 months)', 'charge': 75.00},
            {'title': 'Domain name (1 year)', 'charge': 10.00}
        ],
        'to_addr': {
            'company_name': 'Via Varejo',
            'person_name': 'Helio Cavalcante',
            'person_email': 'helio.cavalcante@viavarejo.com'
        }
    }

    duedate = posted_data.get('duedate', default_data['duedate'])
    from_addr = posted_data.get('from_addr', default_data['from_addr'])
    to_addr = posted_data.get('to_addr', default_data['to_addr'])
    invoice_number = posted_data.get('invoice_number', default_data['invoice_number'])
    items = posted_data.get('items', default_data['items'])
    total = sum([i['charge'] for i in items])

    rendered = render_template('invoice.html',
                                date = today,
                                from_addr = from_addr,
                                to_addr = to_addr,
                                items = items,
                                total = total,
                                invoice_number = invoice_number,
                                duedate = duedate)

    html = HTML(string=rendered)
    rendered_pdf = html.write_pdf()
    return send_file(
        io.BytesIO(rendered_pdf),
        download_name='invoice.pdf'
    )


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

