from app.Quote.quote import pricing
import pandas as pd
"""
def test_new_quote():

    filters = {'net': '6666', 'postcode': 'E3 4JW', 'accessTypes': ['Fibre'], 'bandwidths': ['UP_TO_10'],
               'bearers': [], 'productGroups': [], 'suppliers': ['Level 3 Communications'], 'terms': [],
               'csrf_token': 'ImQ1MWE5NTA1NjAzNmY0YTk1OTVmYThjNmI2ZjFiYWI3OTI0OTM4ZGEi.Ykbo2g.zKD3myNGvwOYvbMZjbn9ECTxkkk'}
    test = pricing.run("BT23 8AG", filters, "12345")

    assert test == ((9,)
('<table border="0" class="dataframe table">\n  <thead>\n    <tr style="text-align: right;">\n      <th>Access Type</th>\n '
 '     <th>Bandwidth(Mb)</th>\n      <th>Bearer(Mb)</th>\n      <th>Carrier</th>\n      <th>Install Charges (GDP)</th>\n     '
 ' <th>Lead Time (Days)</th>\n      <th>Monthly fee (GDP)</th>\n      <th>Product</th>\n      <th>Product ref</th>\n      '
 '<th>Term</th>\n      <th>Supplier Reference</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Fibre</td>\n      '
 '<td>10</td>\n      <td>100</td>\n      <td>Level 3 Communications</td>\n      <td>1020.6667</td>\n      <td>55</td>\n      '
 '<td>490.2300</td>\n      <td>Ethernet Everywhere™</td>\n      <td>278201723</td>\n      <td>12</td>\n      <td>278201697</td>\n   '
 ' </tr>\n    <tr>\n      <td>Fibre</td>\n      <td>10</td>\n      <td>100</td>\n      <td>Level 3 Communications</td>\n   '
 '   <td>0.0000</td>\n      <td>55</td>\n      <td>441.7800</td>\n      <td>Ethernet Everywhere™</td>\n      <td>278201722</td>\n   '
 '   <td>36</td>\n      <td>278201697</td>\n    </tr>\n  </tbody>\n</table>', '6666'))
 """