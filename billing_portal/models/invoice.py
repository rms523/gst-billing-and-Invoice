from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice

doc = SimpleInvoice('invoice.pdf')

# Paid stamp, optional
doc.is_paid = False

doc.invoice_info = InvoiceInfo(1023, datetime.now(), datetime.now())  # Invoice info, optional

# Service Provider Info, optional
doc.service_provider_info = ServiceProviderInfo(
    name='PyInvoice',
    street='My Street',
    city='My City',
    state='My State',
    country='My Country',
    post_code='222222',
    vat_tax_number='Vat/Tax number'
)

# Client info, optional
doc.client_info = ClientInfo(email='client@example.com')

# Add Item
doc.add_item(Item('Item', 'Item desc', 1, '1.1'))
doc.add_item(Item('Item', 'Item desc', 2, '2.2'))
doc.add_item(Item('Item', 'Item desc', 3, '3.3'))

# Tax rate, optional
doc.set_item_tax_rate(20)  # 20%

# Transactions detail, optional
doc.add_transaction(Transaction('Paypal', 111, datetime.now(), 1))
doc.add_transaction(Transaction('Stripe', 222, date.today(), 2))

# Optional
doc.set_bottom_tip("Email: example@example.com<br />Don't hesitate to contact us for any questions.")

doc.finish()
