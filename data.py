# Forwarder 	Tax Invoice 	Invoice date 	
# Customer ID	Shipment	Client GSTN	Client PAN	
# State of Supply	Issue Date 	Terms 	Department 	
# Consol Number 	Shipper	Consignee	
# Order Number/ Order reference 	Goods Description 	
# Country Of Origin	Import Customer Broker 	Weight	Volume 	
# Chargeable	Packages 	Flight / date	MAWB	HAWB	
# Origin	ETA	Destination	ETA	Description 	
# Freight Charges	HSN/SAC	CC Fee	CGST %	
# CGST Amount	SGST %	SGST Amount	Yusen Delivery Order Fee	
# CGST %	CGST Amount	SGST %	SGST Amount	IGM Charge	CGST %	
# CGST Amount	SGST %	SGST Amount	Delivery Order Fee	CGST %	
# CGST Amount	SGST %	SGST Amount	Sub total	Add CGST	
# Add SGST	Total INR

#roi = [y1:y2, x1:x2]
# our data = [x1, y1, x2, y2]
data_page_1 = {'Forwarder': [450, 272, 1255, 335], 
        'Tax Invoice':[470, 420, 987, 500],
        'Invoice date': [1265, 510, 1561, 543],
        'Customer ID': [1264, 551, 1560, 586],
        'Shipment': [1264, 593, 1560, 619],
        'Client GSTN':[1264, 631, 1560, 657],
        'Client PAN':[1264, 668, 1560, 695],
        'State of Supply':[1264, 709, 1560, 728],
        'Issue Date':[1264, 745, 1560, 768],
        'Terms':[1264, 783, 1560, 800],
        'Department':[1264, 829, 1560, 858],
        'Consol Number':[1264, 870, 1560, 895],
        'Shipper':[92, 959, 809, 1005],
        'Consignee':[828, 974, 1549, 1036],
        'Order Number/ Order reference':[91, 1055, 1554, 1111],
        'Goods Description': [90, 1121, 1549, 1169],
        'Country Of Origin': [90, 1190, 570, 1223],
        'Import Customer Broker': [576, 1192, 816, 1224],
        'Weight': [825, 1194, 1062, 1232],
        'Volume': [1069, 1200, 1304, 1233],
        'Chargeable': [1316, 1201, 1545, 1236],
        'Packages': [1314, 1201, 1557, 1238],
        'Flight / date': [84, 1247, 813, 1291],
        'MAWB': [822, 1258, 1181, 1297],
        'HAWB': [1187, 1265, 1549, 1302],
        'Origin': [190, 1282, 638, 1352],
        'ETD': [628, 1329, 812, 1355],
        'Destination': [820, 1328, 1363, 1360],
        'ETA': [1366, 1338, 1547, 1367],
        'Description': [80, 1435, 956, 1497],
        'Freight Charges': [1355, 1450, 1567, 1492],
        'HSN/SAC': [163, 1465, 270, 1501],
        'CC Fee': [1367, 1486, 1551, 1524],
        'CGST %': [997, 1475, 1290, 1525],
        'CGST Amount': [997, 1475, 1290, 1525],
        'SGST %': [1006, 1508, 1276, 1560],
        'SGST Amount': [1006, 1508, 1276, 1560],
        'Yusen Delivery Order Fee': [1367, 1539, 1562, 1598],
        'CGST %_1': [997, 1544, 1371, 1593],
        'CGST Amount_1': [997, 1544, 1371, 1593],
        'SGST %_1': [994, 1573, 1387, 1626],
        'SGST Amount_1': [994, 1573, 1387, 1626],
        'IGM Charge': [1348, 1585, 1576, 1696],
        'CGST %_2': [998, 1614, 1381, 1657],
        'CGST Amount_2': [998, 1614, 1381, 1657],
        'SGST %_2': [985, 1645, 1311, 1697],
        'SGST Amount_2': [985, 1645, 1311, 1697],
        'Delivery Order Fee':[1361, 1647, 1577, 1750],
        'CGST %_3': [976, 1674, 1297, 1727],
        'CGST Amount_3': [976, 1674, 1297, 1727],
        'SGST %_3': [982, 1707, 1268, 1762],
        'SGST Amount_3': [982, 1707, 1268, 1762],
}

data_page_2 = {
        'Sub total':[1178, 1734, 1538, 1756],
        'Add CGST':[1177, 1771, 1541, 1790],
        'Add SGST':[1178, 1805, 1539, 1827],
        'Total INR':[1178, 1840, 1539, 1882],
}