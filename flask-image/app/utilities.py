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
  "externalId": filters["purchaseOrderNumber"],
  "submittedDate": datetime.datetime.now().strftime(' %Y-%m-%d %H:%M:%S'),
  "billingAccount": {
    "id": "0455821113"
  },
  "relatedParty": [
    {
      "role": "Primary Contact",
      "@referredType": "individualParty",
      "title": filters["title"],
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
      "id": "E7W002-Test03",
      "action": "add",
      "@baseType": "productOrderItem",
      "@type": "btProductOrderItem",
      "requiredByDate": "2021-05-24T10:42:08.534Z",
      "billingAccount": {
        "id": "0455821113"
      },
      "productOrderItemRelationship": [
        {
          "id": "ETHA00555666",
          "relationshipType": "reliesOn",
          "@baseType": "OrderItemRelationship",
          "@type": "btServiceRelationship",
          "btType": "FromNode"
        },
        {
          "id": "ETHA00555664",
          "relationshipType": "reliesOn",
          "@baseType": "OrderItemRelationship",
          "@type": "btServiceRelationship",
          "btType": "ToNode"
        },
        {
          "id": "ETHN00555665",
          "relationshipType": "reliesOn",
          "@baseType": "OrderItemRelationship",
          "@type": "btServiceRelationship",
          "btType": "Network"
        }
      ],
      "product": {
        "id": "Etherflow - Connected",
        "productSpecification": {
          "id": "Etherflow - Connected"
        },
        "@baseType": "product",
        "@type": "btProduct",
        "characteristic": [
          {
            "@baseType": "productCharacteristic",
            "@type": "btProductCharacteristic",
            "name": "Bandwidth",
            "value": "1Mbit/s"
          },
          {
            "@baseType": "productCharacteristic",
            "@type": "btProductCharacteristic",
            "name": "Contention",
            "value": "Standard"
          },
          {
            "@baseType": "productCharacteristic",
            "@type": "btProductCharacteristic",
            "name": "FromAccessShared",
            "value": "No"
          },
          {
            "@baseType": "productCharacteristic",
            "@type": "btProductCharacteristic",
            "name": "ToAccessShared",
            "value": "No"
          },
          {
            "@baseType": "productCharacteristic",
            "@type": "btProductCharacteristic",
            "name": "OutageSlot",
            "value": "Not Applicable"
          }
        ],
        "relatedParty": [
          {
            "role": "ServiceContact",
            "title": "Mr.",
            "givenName": "Raj",
            "familyName": "S",
            "contactMedium": [
              {
                "type": "TelephoneNumber",
                "medium": {
                  "type": "business",
                  "number": "9611644499"
                }
              },
              {
                "type": "TelephoneNumber",
                "medium": {
                  "type": "Mobile",
                  "number": "08040417620"
                }
              },
              {
                "type": "Email",
                "medium": {
                  "emailAddress": "ks0064588@techmahindra.com"
                }
              }
            ]
          }
        ]
      },
      "orderItem": [
        {
          "id": "E7W002_1-Test923",
          "action": "add",
          "requiredByDate": "2021-05-24T10:42:08.534Z",
          "billingAccount": {
            "id": "0455821113"
          },
          "product": {
            "id": "Maintenance Category 3",
            "productSpecification": {
              "id": "Maintenance Category 3"
            },
            "baseType": "product",
            "type": "btProduct"
          },
          "@baseType": "productOrderItem",
          "@type": "btProductOrderItem"
        }
      ]
    }
  ]
}
