import requests

url = 'http://127.0.0.1:5000/'

data = {
    'duedate': 'September 1, 2021',
    'from_addr': {
        'addr1': 'Hamilton, New York',
        'addr2': 'Sunnyville, CA 12345',
        'company_name': 'Python Tip'
    },
    'invoice_number': 156,
    'items': [
        {'title': 'Brochure design', 'charge': 500.0},
        {'title': 'Hosting (6 months)', 'charge': 85.0},
        {'title': 'Domain name (1 year)', 'charge': 10.0}
    ],
    'to_addr': {
        'company_name': 'hula hoop',
        'person_email': 'john@example.com',
        'person_name': 'Yasoob Khalid'
    }
}

html = requests.post(url, json=data)
with open('invoice.pdf', 'wb') as f:
    f.write(html.content)
