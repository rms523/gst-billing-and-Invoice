from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice


class GenerateInvoice(object):

    @staticmethod
    def createInvoice(datafields):
        doc = SimpleInvoice('invoice.pdf')

        # Paid stamp, optional
        doc.is_paid = False

        doc.invoice_info = InvoiceInfo(1023, datetime.now(), datetime.now())  # Invoice info, optional

        # Service Provider Info, optional
        doc.service_provider_info = ServiceProviderInfo(
            name='pyInvoice Rahulshamrjdjjkjjk',
            street='My Street lsjfklsdjljfkldjskljslkdjfklsd',
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
        for item in range(len(datafields)):
            doc.add_item(Item(datafields[itemCount][0], datafields[itemCount][1], itemCount+1, datafields[itemCount][6]))
            itemCount += 1

        # Tax rate, optional
        doc.set_item_tax_rate(datafields[4])  # 20%

        # Transactions detail, optional
        doc.add_transaction(Transaction('Paypal', 111, datetime.now(), 1))
        doc.add_transaction(Transaction('Stripe', 222, date.today(), 2))

        # Optional
        doc.set_bottom_tip("Email: example@example.com<br />Don't hesitate to contact us for any questions.")

        doc.finish()


if __name__ == '__main__':

        invoiceObj = GenerateInvoice
        invoiceObj.createInvoice()
