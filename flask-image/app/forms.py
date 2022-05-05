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
    pricingRequstAccessProductId = StringField(
        'Pricing Request Product ID',
        id='pricingRequstAccessProductIdId'
    )
    pricingRequestHardwareId = StringField(
        'pricing request hardware ID',
        id='pricingRequestHardwareIdId'
    )
    pricingRequestAdditionalHardwareOptionIds = StringField(
        'Additional Hardware Option Ids',
        id='pricingRequestAdditionalHardwareOptionIdsId'
    )
    purchaseOrderNumber = StringField(
        'Purchase Order Number',
        id='purchaseOrderId'
    )
    orderReference = StringField(
        'Order Reference',
        id='orderReferenceId'
    )
    firstName = StringField(
        'First Name',
        id ='primaryContactFirstNameId'
    )
    lastName = StringField(
        'Last Name',
        id='primaryContactLastNameId'
    )
    telephone = StringField(
        'Telephone',
        id='primaryContactTelephoneId'
    )
    email = StringField(
        'Email',
        id='primaryContactEmail'
    )
    endCustomerCompanyName = StringField(
        'End Customer Company Name',
        id='endCustomerCompanyNameId'
    )
    companyRegistration = StringField(
        'Company Registration',
        id='companyRegistrationId'
    )
    postcode = StringField(
        'Postcode',
        id='postcode'
    )
    lastName = StringField(
        'Last Name',
        id='primaryContactLastNameId'
    )
    unitBuildingNo = StringField(
        'Unit Building No',
        id='unitBuildingNoId'
    )
    buildingName = StringField(
        'Building Name',
        id='buildingNameId'
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
    country = StringField(
        'Country',
        id='countryId'
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
    siteConstraint = StringField(
        'Site Constraint',
        id='siteConstraintId'
    )
    siteStatus = StringField(
        'Site Status',
        id='siteStatusId'
    )
    wasConstructedBefore2000 = StringField(
        'Constructed before 2000',
        id='wasConstructedBefore2000Id'
    )
    isAsbestosRegisterAvailable = StringField(
        'Is Asbestos Register Available',
        id='isAsbestosRegisterAvailableId'
    )
    siteNotes = StringField(
        'Site Notes',
        id='siteNotesId'
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
    nni = StringField(
        'NNI',
        id='nniId'
    )
    taggingMethod = StringField(
        'Tagging Method',
        id='taggingMethodId'
    )
    requiredVLAN = StringField(
        'Required VLAN',
        id='requiredVLANId'
    )
    designType = StringField(
        'Design Type',
        id='designTypeId'
    )
    interfaceType = StringField(
        'Interface Type',
        id='interfaceTypeId'
    )
    autonegotiation = StringField(
        'Autonegotion',
        id='autonegotiationId'
    )
    interfaceSpeed = StringField(
        'Interface Speed',
        id='interfaceSpeedId'
    )
    duplex = StringField(
        'Duplex',
        id='duplexId'
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
    secondaryAccess = StringField(
        'Seconday Access',
        id='secondaryAccessId'
    )
    secondaryHardwareId = StringField(
        'Seconday Harware Id',
        id='secondaryHardwareIdId'
    )
    secondaryAdditionalHardwareOptionIds = StringField(
        'Seconday Additional Hardware Option Ids',
        id='secondaryAdditionalHardwareOptionIdsId'
    )
    secondaryNNI = StringField(
        'NNI',
        id='nniId'
    )
    secondaryTaggingMethod = StringField(
        'Tagging Method',
        id='taggingMethodId'
    )
    secondaryRequiredVLAN = StringField(
        'Required VLAN',
        id='requiredVLANId'
    )
    secondaryDesignType = StringField(
        'Design Type',
        id='designTypeId'
    )
    secondaryInterfaceType = StringField(
        'Interface Type',
        id='interfaceTypeId'
    )
    secondaryAutonegotiation = StringField(
        'Autonegotion',
        id='autonegotiationId'
    )
    secondaryInterfaceSpeed = StringField(
        'Interface Speed',
        id='interfaceSpeedId'
    )
    secondaryDuplex = StringField(
        'Duplex',
        id='duplexId'
    )
    secondaryDeliveryAddress = StringField(
        'Delivery Address',
        id='deliveryAddressId'
    )
    secondaryDeliveryContact = StringField(
        'Delivery Contact',
        id='deliveryContactId'
    )
    secondaryDeliveryContactNum = StringField(
        'Delivery Contact Number',
        id='deliveryContactNumId'
    )




