#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for
# each county.

import openpyxl
import pprint

main_sheet = openpyxl.load_workbook('censuspopdata.xlsx').get_sheet_by_name(
    'Population by Census Tract')
countyData = {}

print("Reading rows...")

for each_tuple in main_sheet['A2':'D72865']:
    state = each_tuple[1].value
    county = each_tuple[2].value
    pop = each_tuple[3].value

    # 为避免多余元素出现，从外到内定义嵌套字典。
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += pop

print("Writing results...")
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
