import datetime

def add_quote_item(existing_list, filters, bearer, product):
    print(bearer)
    new_item = btw_api_body(filters, bearer, product)
    existing_list["quoteItem"].append(new_item)
    return existing_list

def btw_api_body(filters,bearer, product):
  if not filters["btw_bandwidths"] and not filters["btw_bw_type"]:
    bandwidth = bearer
  else:
    bandwidth = filters["btw_bandwidths"] + " " + filters["btw_bw_type"][0]
  body = {"action": "add", "product": {"@type": "WholesaleEthernetElan",
                                                                    "productSpecification": {
                                                                        "id": "WholesaleEthernetElan"},
                                                                    "existingAend": "True",
                                                                    "place": [{"@type": "PostcodeSite",
                                                                               "postcode": filters["postcode"]}], "product": [
                        {"@type": product, "productSpecification":
                            {"id": product}, "bandwidth": bearer, "resilience": "Standard"},
                        {"@type": "EtherflowDynamicService",
                         "productSpecification": {"id": "EtherflowDynamicService"}, "bandwidth": bandwidth ,
                         "cos": "Default CoS (Standard)"}]}}

  return body

def btw_order_api_body(filters):

    body = {
  "externalId": filters["orderReference"],
  "submittedDate": datetime.datetime.now().strftime(' %Y-%m-%d %H:%M:%S'),
  "billingAccount": {
    "id": "0455821502"
  },
  "relatedParty": [
    {
      "role": "KciContact",
      "@referredType": "individualParty",
      "title": "Miss.",
      "givenName": filters["FirstName"],
      "familyName": filters["LastName"],
      "contactMedium": [
        {
          "type": "TelephoneNumber",
          "medium": {
            "type": "business",
            "number": filters["Telephone"]
          }
        },
        {
          "type": "Email",
          "medium": {
            "emailAddress": filters["Email"]
          }
        }
      ]
    }
  ],
  "@baseType": "productOrder",
  "@type": "btProductOrder",
  "orderItem": [
    {
      "id": "MADHUBBB412",
      "action": "add",
      "@baseType": "productOrderItem",
      "@type": "btProductOrderItem",
      "requiredByDate": "2021-08-11T15:42:08.534Z",
      "billingAccount": {
        "id": "0455821502"
      },
      "product": {
        "id": "Etherway",
        "productSpecification": {
          "id": "Etherway"
        },
        "@baseType": "product",
        "@type": "btProduct",
        "btSiteDetails": {
          "HSHazards": filters["siteHazards"],
          "CompanyName": filters["endCustomerCompanyName"],
		  "Room": filters["room"],
		  "floor": filters["floor"],
          "characteristics": [
            {
              "@baseType": "siteCharacteristic",
              "name": "Site Constraint",
              "value": filters["siteConstraint"]
            }
          ]
        },
		"characteristic":[
		{
			"@baseType":"productCharacteristic",
			"@type": "btProductCharacteristic",
			"name": "Bandwidth",
			"value": filters["bandwidth"]
		  },
			{
			"@baseType":"productCharacteristic",
			"@type": "btProductCharacteristic",
			"name": "accessPricingPeriod",
			"value": filters["term"]
			},
			{
			"@baseType":"productCharacteristic",
			"@type": "btProductCharacteristic",
			"name": "InterfaceType",
			"value": filters["interfaceType"]
			},
			{
			"@baseType":"productCharacteristic",
			"@type": "btProductCharacteristic",
			"name": "AutoNegotiateCustomerEnd",
			"value": filters["autonegotiation"]
			},
			{
			"@baseType":"productCharacteristic",
			"@type": "btProductCharacteristic",
			"name": "EtherflowBandwidthRange",
			"value": filters["etherflow"]
			}
		],
        "relatedParty": [
          {
            "role": "ServiceContact",
            "@referredType": "individualParty",
            "title": "Miss.",
            "givenName": filters["firstName"],
            "familyName": filters["lastName"],
            "contactMedium": [
              {
                "type": "TelephoneNumber",
                "medium": {
                  "type": "business",
                  "number": filters["phoneNumber"]
                }
              }
            ]
          }
        ]
      }
    }
  ]
}
    return body