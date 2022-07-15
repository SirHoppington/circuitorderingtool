# circuitorderingtool

Flask application that requests quotations from Virtual 1 Layer 2 Quotation API and BT Wholesale Layer 2 Quotation API.

Pricing from both suppliers are stored with a unique "NET" references and can be added to a customer quotation.

Customer quotations can be sent to orders, whereby order status is updated and an order can be placed directly via the Suppliers Order
API.

WTForms used for New Quote and New Order forms.

Bootstrap basic stylings.

SQLAlchemy ORM and Postgres databases.
