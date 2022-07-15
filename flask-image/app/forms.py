from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Length

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class NewQuote(FlaskForm):
    """Add new quote form."""
    customer_name = StringField(
        'Customer Name',
        [DataRequired()],
        id='net'
    )
    customer_email = StringField(
        'Customer email',
        [DataRequired()],
        id='net'
    )
    net = StringField(
        'NET reference',
        [DataRequired()],
        id='net'
    )
    postcode = StringField(
        'Postcode',
        [DataRequired()],
        id='postcode'
    )
    accessTypes = MultiCheckboxField(
        'AccessTypes',
        choices=
        ['Copper',
         'Fibre',
         'FTTC'],
        id='accessType'
    )
    bandwidths = MultiCheckboxField(
        'Bandwidths',
        choices=
        [('UP_TO_10', 'up to 10Mb'),
         ('FROM_10_TO_100','10Mb to 100Mb'),
         ('FROM_100_TO_1000', '100Mb to 1Gb'),
         ('FROM_1000_TO_10000', '1Gb to 10Gb')],
        id='bandwidths'
    )
    bearers = MultiCheckboxField(
        'Bearers',
        choices=
        [('100', '100Mb'),
         ('1000', '1Gb'),
         ('10000', '10Gb')],
        id='bandwidths'
    )
    productGroups = MultiCheckboxField(
        'ProductGroups',
        choices=
        ['EFM',
          'EoFTTC',
          'Fibre Ethernet'],
        id='productGroups'
    )
    suppliers = MultiCheckboxField(
        'Suppliers',
        choices=
        [('BT Wholesale', 'BT Wholesale'),
         ('Colt', 'Colt'),
         ('Level 3 Communications', 'Level 3'),
         ('SSE Telecoms', 'SSE Telecoms'),
         ('TalkTalk Business', 'TalkTalk Business'),
         ('Virgin Media Business', 'Virgin Media Business'),
         ('Virtual1', 'Virtual1'),
         ('Vodafone', 'Vodafone')],
        id='suppliers'
    )
    terms = MultiCheckboxField(
        'Terms',
        choices=
        ['12 Months',
          '36 Months'],
        id='productGroups'
    )

class RetrieveQuote(FlaskForm):
    """Add new quote form."""
    net = StringField(
        'NET Reference',
        [DataRequired()],
        id='net'
    )

class NewOrder(FlaskForm):
    """Create new order form"""
    quoteReference = StringField(
        'Supplier Quote Reference',
        id='quoteReferenceId'
    )
    pricingRequestAccessProductId = StringField(
        'Pricing Request Product ID',
        id='pricingRequestAccessProductIdId'
    )
    pricingRequestHardwareId = StringField(
        'pricing request hardware ID',
        id='pricingRequestHardwareIdId'
    )
    purchaseOrderNumber = StringField(
        'Purchase Orders Number',
        id='purchaseOrderId'
    )
    orderReference = StringField(
        'Order Reference Number',
        id='orderReference'
    )

    FirstName = StringField(
        'First Name',
        id ='primaryContactFirstNameId'
    )
    LastName = StringField(
        'Last Name',
        id='primaryContactLastNameId'
    )
    Telephone = StringField(
        'Telephone',
        id='primaryContactTelephoneId'
    )
    Email = StringField(
        'Email',
        id='primaryContactEmail'
    )
    endCustomerCompanyName = StringField(
        'End Customer Company Name',
        id='endCustomerCompanyNameId'
    )
    companyRegistration = StringField(
               'Company Registration',
        id='companyRegistration'
    )
    postcode = StringField(
        'Postcode',
        id='postcode'
    )
    buildingName = StringField(
        'Building Name',
        id='buildingName'
    )
    streetNumber = StringField(
        'Street No',
        id='streetNumberId'
    )
    streetName = StringField(
        'Street Name',
        id='streetNameId'
    )
    townCity = StringField(
        'Town/City',
        id='townCityId'
    )
    county = StringField(
        'County',
        id='countyId'
    )
    firstName = StringField(
        'First Name',
        id='firstNameId'
    )
    lastName = StringField(
        'Last Name',
        id='lastNameId'
    )
    phoneNumber = StringField(
        'Phone Number',
        id='phoneNumberId'
    )
    accessAvailableFrom = StringField(
        'Access Available From',
        id='accessAvailableFromId'
    )
    siteConstraint = SelectField(
        'Site Constraint',
        id='siteConstraintId',
        choices=
        ['site-not-ready',
         'new-construction',
         'complex-access-requirements',
         'datacentre',
         'none']
    )
    siteStatus = SelectField(
        'Site Status',
        id='siteStatus',
        choices =
        ['new-site',
         'office-move',
         'current-tenant']
    )
    wasConstructedBefore2000 = SelectField(
        'Constructed before 2000',
        id='wasConstructedBefore2000Id',
        choices=
        ['YES',
         'NO',
         'DONT_KNOW']
    )
    isAsbestosRegisterAvailable = SelectField(
        'Is Asbestos Register Available',
        id='isAsbestosRegisterAvailableId',
        choices=
        ['YES',
         'NO',
         'DONT_KNOW']
    )
    siteHazards = StringField(
        'Site Hazards',
        id='siteHazards'
    )
    areSSRAMSRequired = SelectField(
        'Are SSRAMs required',
        id='areSSRAMSRequired',
        choices=
        ['YES',
         'NO']
    )
    landlordConsentNeeded = SelectField(
        'Is Landlord Consent Required',
        id='landlordConsentRequired',
        choices=['YES',
                 'NO']
    )
    nni = StringField(
        'NNI',
        id='nniId'
    )
    floor = StringField(
        'Floor',
        id='floorId'
    )
    room = StringField(
        'Room',
        id='roomId'
    )
    rack = StringField(
        'Rack',
        id='rackId'
    )
    taggingMethod = SelectField(
        'Tagging Required',
        id='taggingMethodId',
        choices = ['Untagged','Tagged']
    )
    designType = StringField(
        'Design Type',
        id='designTypeId'
    )
    interfaceType = SelectField(
        'Interface Type',
        id='interfaceTypeId',
        choices = [
            '100Base-T Rj45',
        '1000Base-T Rj45',
        'LC-Multi Mode',
        'LC-Single Mode']
    )
    autonegotiation = SelectField(
        'Autonegotion',
        id='autonegotiationId',
        choices = ['Enabled',
                   'Disabled']
    )
    interfaceSpeed = SelectField(
        'Interface Speed',
        id='interfaceSpeedId',
        choices = ['GigE',
                   'FaE']
    )
    duplex = SelectField(
        'Duplex',
        id='duplex',
        choices=['Full',
                 'Half']
    )
    deliveryAddress = StringField(
        'Delivery Address',
        id='deliveryAddressId'
    )
    deliveryContact = StringField(
        'Delivery Contact',
        id='deliveryContactId'
    )
    deliveryContactNumber = StringField(
        'Delivery Contact Number',
        id='deliveryContactNumberId'
    )