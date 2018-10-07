from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice
from billing_portal.models.allfields import Allfields


class GenerateInvoice(object):

    @staticmethod
    def createInvoice(datafields):
        doc = SimpleInvoice('invoice.pdf')

        # Paid stamp, optional
        doc.is_paid = True

        doc.invoice_info = InvoiceInfo(1023, datetime.now(), datetime.now())  # Invoice info, optional

        # Service Provider Info, optional
        doc.service_provider_info = ServiceProviderInfo(
            name='pyInvoice',
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
        itemCount = 0
        for item in range(4):
            doc.add_item(Item(datafields[0]['product'], 'Item Desc', int(datafields[0]['quantity']), str(datafields[0]['rate'])))
            itemCount += 1

        # Tax rate, optional
        doc.set_item_tax_rate(int(datafields[0]['gstrate']))  # 20%

        # Transactions detail, optional
        doc.add_transaction(Transaction('Paypal', 111, datetime.now(), 1))
        doc.add_transaction(Transaction('Stripe', 222, date.today(), 2))

        # Optional
        doc.set_bottom_tip("Email: example@example.com<br />Don't hesitate to contact us for any questions.")

        doc.finish()


if __name__ == '__main__':
        datafields = Allfields.fetchallfields()

        invoiceObj = GenerateInvoice
        print (datafields)
       # invoiceObj.createInvoice(datafields)

