# -*- encoding : utf-8 -*-

from .helpers import full_uuid

__all__ = [ 'getAppearance',
            'getCompany', 'getMember'
            'getServiceUUID16', 'getServiceUUID128',
            'getService' ]


# ------------------------------------------------------------------------------
# --- Search ---------------------------------------------------------------------
# ------------------------------------------------------------------------------

def getAppearance(categ, subcateg) :
    apps = Appearances_dict.get(categ, Appearances_dict[0])
    app = apps.get(subcateg, apps[0])
    return app

def getCompany(code) :
    try :
        hexlcode = '0x{:04x}'.format(code)
        hexucode = '0x{:04X}'.format(code)
        idx = COMPANIES.index(hexucode)
        record = COMPANIES[idx:].splitlines()[0].split('\t')
        return hexlcode, record[1]
    except ValueError :
        return hexlcode, None

def getMember(code) :
    try :
        hexlcode = '0x{:04x}'.format(code)
        hexucode = '0x{:04X}'.format(code)
        idx = MEMBERS.index(hexucode)
        record = MEMBERS[idx:].splitlines()[0].split('\t')
        return hexlcode, record[1], record[2]
    except ValueError :
        return hexlcode, 'Unknown', None

def getServiceUUID16(uuid16) :
    return uuid16_dict.get(uuid16, 'Unknown Service')

def getServiceUUID128(uuid128) :
    return uuid128_dict.get(uuid128, 'Unknown Service')

def getService(uuid) :
    uuid128 = str(full_uuid(uuid))
    return services_dict.get(uuid128, 'Unknown Service')
    

Appearances_dict = {
     0 : { 0 : 'Unknown' },
     1 : { 0 : 'Phone' },
     2 : { 0 : 'Computer' },
     3 : { 0 : 'Watch', 1 : 'Watch: Sports Watch' },
     4 : { 0 : 'Clock' },
     5 : { 0 : 'Display' },
     6 : { 0 : 'Remote Control' },
     7 : { 0 : 'Eye-glasses' },
     8 : { 0 : 'Tag' },
     9 : { 0 : 'Keyring' },
    10 : { 0 : 'Media Player' },
    11 : { 0 : 'Barcode Scanner' },
    12 : { 0 : 'Thermometer', 1 : 'Thermometer: Ear' },
    13 : { 0 : 'Heart Rate Sensor', 1 : 'Heart Rate Sensor: Heart Rate Belt' },
    14 : { 0 : 'Blood Pressure', 1 : 'Blood Pressure: Arm', 2 : 'Blood Pressure : Wrist' },
    15 : {
        0 : 'Human Interface Device',
        1 : 'Keyboard',
        2 : 'Mouse',
        3 : 'Joystick',
        4 : 'Gamepad',
        5 : 'Digitizer Tablet',
        6 : 'Card Reader',
        7 : 'Digital Pen',
        8 : 'Barcode Scanner'
    },
    16 : { 0 : 'Glucose Meter' },
    17 : {
        0 : 'Running Walking Sensor',
        1 : 'Running Walking Sensor: In-Shoe',
        2 : 'Running Walking Sensor: On-Shoe',
        3 : 'Running Walking Sensor: On-Hip'
    },
    18 : {
        0 : 'Cycling',
        1 : 'Cycling: Cycling Computer',
        2 : 'Cycling: Speed Sensor',
        3 : 'Cycling: Cadence Sensor',
        4 : 'Cycling: Power Sensor',
        5 : 'Cycling: Speed and Cadence Sensor'
    },
    49 : {
        0 : 'Pulse Oximeter',
        1 : 'Pulse Oximeter: Fingertip',
        2 : 'Pulse Oximeter: Wrist Worn'
    },
    50 : { 0 : 'Weight Scale' },
    51 : {
        0 : 'Personal Mobility Device',
        1 : 'Personal Mobility Device: Powered Wheelchair',
        2 : 'Personal Mobility Device: Mobility Scooter',
    },
    52 : { 0 : 'Continuous Glucose Monitor' },
    53 : {
        0 : 'Insulin Pump',
        1 : 'Insulin Pump: Durable Pump',
        4 : 'Insulin Pump: Patch Pump',
        8 : 'Insulin Pump: Insulin Pen',
    },
    54 : { 0 : 'Medication Delivery' },
    81 : {
        0 : 'Outdoor Sports Activity',
        1 : 'Outdoor Sports Activity: Location Display Device',
        2 : 'Outdoor Sports Activity: Location and Navigation Display Device',
        3 : 'Outdoor Sports Activity: Location Pod',
        4 : 'Outdoor Sports Activity: Location and Navigation Pod',
    },
}
    

COMPANIES="""
0	0x0000	Ericsson Technology Licensing
1	0x0001	Nokia Mobile Phones
2	0x0002	Intel Corp.
3	0x0003	IBM Corp.
4	0x0004	Toshiba Corp.
5	0x0005	3Com
6	0x0006	Microsoft
7	0x0007	Lucent
8	0x0008	Motorola
9	0x0009	Infineon Technologies AG
10	0x000A	Qualcomm Technologies International, Ltd. (QTIL)
11	0x000B	Silicon Wave
12	0x000C	Digianswer A/S
13	0x000D	Texas Instruments Inc.
14	0x000E	Parthus Technologies Inc.
15	0x000F	Broadcom Corporation
16	0x0010	Mitel Semiconductor
17	0x0011	Widcomm, Inc.
18	0x0012	Zeevo, Inc.
19	0x0013	Atmel Corporation
20	0x0014	Mitsubishi Electric Corporation
21	0x0015	RTX Telecom A/S
22	0x0016	KC Technology Inc.
23	0x0017	Newlogic
24	0x0018	Transilica, Inc.
25	0x0019	Rohde & Schwarz GmbH & Co. KG
26	0x001A	TTPCom Limited
27	0x001B	Signia Technologies, Inc.
28	0x001C	Conexant Systems Inc.
29	0x001D	Qualcomm
30	0x001E	Inventel
31	0x001F	AVM Berlin
32	0x0020	BandSpeed, Inc.
33	0x0021	Mansella Ltd
34	0x0022	NEC Corporation
35	0x0023	WavePlus Technology Co., Ltd.
36	0x0024	Alcatel
37	0x0025	NXP Semiconductors (formerly Philips Semiconductors)
38	0x0026	C Technologies
39	0x0027	Open Interface
40	0x0028	R F Micro Devices
41	0x0029	Hitachi Ltd
42	0x002A	Symbol Technologies, Inc.
43	0x002B	Tenovis
44	0x002C	Macronix International Co. Ltd.
45	0x002D	GCT Semiconductor
46	0x002E	Norwood Systems
47	0x002F	MewTel Technology Inc.
48	0x0030	ST Microelectronics
49	0x0031	Synopsys, Inc.
50	0x0032	Red-M (Communications) Ltd
51	0x0033	Commil Ltd
52	0x0034	Computer Access Technology Corporation (CATC)
53	0x0035	Eclipse (HQ Espana) S.L.
54	0x0036	Renesas Electronics Corporation
55	0x0037	Mobilian Corporation
56	0x0038	Syntronix Corporation
57	0x0039	Integrated System Solution Corp.
58	0x003A	Matsushita Electric Industrial Co., Ltd.
59	0x003B	Gennum Corporation
60	0x003C	BlackBerry Limited (formerly Research In Motion)
61	0x003D	IPextreme, Inc.
62	0x003E	Systems and Chips, Inc
63	0x003F	Bluetooth SIG, Inc
64	0x0040	Seiko Epson Corporation
65	0x0041	Integrated Silicon Solution Taiwan, Inc.
66	0x0042	CONWISE Technology Corporation Ltd
67	0x0043	PARROT AUTOMOTIVE SAS
68	0x0044	Socket Mobile
69	0x0045	Atheros Communications, Inc.
70	0x0046	MediaTek, Inc.
71	0x0047	Bluegiga
72	0x0048	Marvell Technology Group Ltd.
73	0x0049	3DSP Corporation
74	0x004A	Accel Semiconductor Ltd.
75	0x004B	Continental Automotive Systems
76	0x004C	Apple, Inc.
77	0x004D	Staccato Communications, Inc.
78	0x004E	Avago Technologies
79	0x004F	APT Ltd.
80	0x0050	SiRF Technology, Inc.
81	0x0051	Tzero Technologies, Inc.
82	0x0052	J&M Corporation
83	0x0053	Free2move AB
84	0x0054	3DiJoy Corporation
85	0x0055	Plantronics, Inc.
86	0x0056	Sony Ericsson Mobile Communications
87	0x0057	Harman International Industries, Inc.
88	0x0058	Vizio, Inc.
89	0x0059	Nordic Semiconductor ASA
90	0x005A	EM Microelectronic-Marin SA
91	0x005B	Ralink Technology Corporation
92	0x005C	Belkin International, Inc.
93	0x005D	Realtek Semiconductor Corporation
94	0x005E	Stonestreet One, LLC
95	0x005F	Wicentric, Inc.
96	0x0060	RivieraWaves S.A.S
97	0x0061	RDA Microelectronics
98	0x0062	Gibson Guitars
99	0x0063	MiCommand Inc.
100	0x0064	Band XI International, LLC
101	0x0065	Hewlett-Packard Company
102	0x0066	9Solutions Oy
103	0x0067	GN Netcom A/S
104	0x0068	General Motors
105	0x0069	A&D Engineering, Inc.
106	0x006A	MindTree Ltd.
107	0x006B	Polar Electro OY
108	0x006C	Beautiful Enterprise Co., Ltd.
109	0x006D	BriarTek, Inc
110	0x006E	Summit Data Communications, Inc.
111	0x006F	Sound ID
112	0x0070	Monster, LLC
113	0x0071	connectBlue AB
114	0x0072	ShangHai Super Smart Electronics Co. Ltd.
115	0x0073	Group Sense Ltd.
116	0x0074	Zomm, LLC
117	0x0075	Samsung Electronics Co. Ltd.
118	0x0076	Creative Technology Ltd.
119	0x0077	Laird Technologies
120	0x0078	Nike, Inc.
121	0x0079	lesswire AG
122	0x007A	MStar Semiconductor, Inc.
123	0x007B	Hanlynn Technologies
124	0x007C	A & R Cambridge
125	0x007D	Seers Technology Co., Ltd.
126	0x007E	Sports Tracking Technologies Ltd.
127	0x007F	Autonet Mobile
128	0x0080	DeLorme Publishing Company, Inc.
129	0x0081	WuXi Vimicro
130	0x0082	Sennheiser Communications A/S
131	0x0083	TimeKeeping Systems, Inc.
132	0x0084	Ludus Helsinki Ltd.
133	0x0085	BlueRadios, Inc.
134	0x0086	Equinux AG
135	0x0087	Garmin International, Inc.
136	0x0088	Ecotest
137	0x0089	GN ReSound A/S
138	0x008A	Jawbone
139	0x008B	Topcon Positioning Systems, LLC
140	0x008C	Gimbal Inc. (formerly Qualcomm Labs, Inc. and Qualcomm Retail Solutions, Inc.)
141	0x008D	Zscan Software
142	0x008E	Quintic Corp
143	0x008F	Telit Wireless Solutions GmbH (formerly Stollmann E+V GmbH)
144	0x0090	Funai Electric Co., Ltd.
145	0x0091	Advanced PANMOBIL systems GmbH & Co. KG
146	0x0092	ThinkOptics, Inc.
147	0x0093	Universal Electronics, Inc.
148	0x0094	Airoha Technology Corp.
149	0x0095	NEC Lighting, Ltd.
150	0x0096	ODM Technology, Inc.
151	0x0097	ConnecteDevice Ltd.
152	0x0098	zero1.tv GmbH
153	0x0099	i.Tech Dynamic Global Distribution Ltd.
154	0x009A	Alpwise
155	0x009B	Jiangsu Toppower Automotive Electronics Co., Ltd.
156	0x009C	Colorfy, Inc.
157	0x009D	Geoforce Inc.
158	0x009E	Bose Corporation
159	0x009F	Suunto Oy
160	0x00A0	Kensington Computer Products Group
161	0x00A1	SR-Medizinelektronik
162	0x00A2	Vertu Corporation Limited
163	0x00A3	Meta Watch Ltd.
164	0x00A4	LINAK A/S
165	0x00A5	OTL Dynamics LLC
166	0x00A6	Panda Ocean Inc.
167	0x00A7	Visteon Corporation
168	0x00A8	ARP Devices Limited
169	0x00A9	Magneti Marelli S.p.A
170	0x00AA	CAEN RFID srl
171	0x00AB	Ingenieur-Systemgruppe Zahn GmbH
172	0x00AC	Green Throttle Games
173	0x00AD	Peter Systemtechnik GmbH
174	0x00AE	Omegawave Oy
175	0x00AF	Cinetix
176	0x00B0	Passif Semiconductor Corp
177	0x00B1	Saris Cycling Group, Inc
178	0x00B2	Bekey A/S
179	0x00B3	Clarinox Technologies Pty. Ltd.
180	0x00B4	BDE Technology Co., Ltd.
181	0x00B5	Swirl Networks
182	0x00B6	Meso international
183	0x00B7	TreLab Ltd
184	0x00B8	Qualcomm Innovation Center, Inc. (QuIC)
185	0x00B9	Johnson Controls, Inc.
186	0x00BA	Starkey Laboratories Inc.
187	0x00BB	S-Power Electronics Limited
188	0x00BC	Ace Sensor Inc
189	0x00BD	Aplix Corporation
190	0x00BE	AAMP of America
191	0x00BF	Stalmart Technology Limited
192	0x00C0	AMICCOM Electronics Corporation
193	0x00C1	Shenzhen Excelsecu Data Technology Co.,Ltd
194	0x00C2	Geneq Inc.
195	0x00C3	adidas AG
196	0x00C4	LG Electronics
197	0x00C5	Onset Computer Corporation
198	0x00C6	Selfly BV
199	0x00C7	Quuppa Oy.
200	0x00C8	GeLo Inc
201	0x00C9	Evluma
202	0x00CA	MC10
203	0x00CB	Binauric SE
204	0x00CC	Beats Electronics
205	0x00CD	Microchip Technology Inc.
206	0x00CE	Elgato Systems GmbH
207	0x00CF	ARCHOS SA
208	0x00D0	Dexcom, Inc.
209	0x00D1	Polar Electro Europe B.V.
210	0x00D2	Dialog Semiconductor B.V.
211	0x00D3	Taixingbang Technology (HK) Co,. LTD.
212	0x00D4	Kawantech
213	0x00D5	Austco Communication Systems
214	0x00D6	Timex Group USA, Inc.
215	0x00D7	Qualcomm Technologies, Inc.
216	0x00D8	Qualcomm Connected Experiences, Inc.
217	0x00D9	Voyetra Turtle Beach
218	0x00DA	txtr GmbH
219	0x00DB	Biosentronics
220	0x00DC	Procter & Gamble
221	0x00DD	Hosiden Corporation
222	0x00DE	Muzik LLC
223	0x00DF	Misfit Wearables Corp
224	0x00E0	Google
225	0x00E1	Danlers Ltd
226	0x00E2	Semilink Inc
227	0x00E3	inMusic Brands, Inc
228	0x00E4	L.S. Research Inc.
229	0x00E5	Eden Software Consultants Ltd.
230	0x00E6	Freshtemp
231	0x00E7	KS Technologies
232	0x00E8	ACTS Technologies
233	0x00E9	Vtrack Systems
234	0x00EA	Nielsen-Kellerman Company
235	0x00EB	Server Technology Inc.
236	0x00EC	BioResearch Associates
237	0x00ED	Jolly Logic, LLC
238	0x00EE	Above Average Outcomes, Inc.
239	0x00EF	Bitsplitters GmbH
240	0x00F0	PayPal, Inc.
241	0x00F1	Witron Technology Limited
242	0x00F2	Morse Project Inc.
243	0x00F3	Kent Displays Inc.
244	0x00F4	Nautilus Inc.
245	0x00F5	Smartifier Oy
246	0x00F6	Elcometer Limited
247	0x00F7	VSN Technologies, Inc.
248	0x00F8	AceUni Corp., Ltd.
249	0x00F9	StickNFind
250	0x00FA	Crystal Code AB
251	0x00FB	KOUKAAM a.s.
252	0x00FC	Delphi Corporation
253	0x00FD	ValenceTech Limited
254	0x00FE	Stanley Black and Decker
255	0x00FF	Typo Products, LLC
256	0x0100	TomTom International BV
257	0x0101	Fugoo, Inc.
258	0x0102	Keiser Corporation
259	0x0103	Bang & Olufsen A/S
260	0x0104	PLUS Location Systems Pty Ltd
261	0x0105	Ubiquitous Computing Technology Corporation
262	0x0106	Innovative Yachtter Solutions
263	0x0107	William Demant Holding A/S
264	0x0108	Chicony Electronics Co., Ltd.
265	0x0109	Atus BV
266	0x010A	Codegate Ltd
267	0x010B	ERi, Inc
268	0x010C	Transducers Direct, LLC
269	0x010D	Fujitsu Ten LImited
270	0x010E	Audi AG
271	0x010F	HiSilicon Technologies Col, Ltd.
272	0x0110	Nippon Seiki Co., Ltd.
273	0x0111	Steelseries ApS
274	0x0112	Visybl Inc.
275	0x0113	Openbrain Technologies, Co., Ltd.
276	0x0114	Xensr
277	0x0115	e.solutions
278	0x0116	10AK Technologies
279	0x0117	Wimoto Technologies Inc
280	0x0118	Radius Networks, Inc.
281	0x0119	Wize Technology Co., Ltd.
282	0x011A	Qualcomm Labs, Inc.
283	0x011B	Hewlett Packard Enterprise
284	0x011C	Baidu
285	0x011D	Arendi AG
286	0x011E	Skoda Auto a.s.
287	0x011F	Volkswagen AG
288	0x0120	Porsche AG
289	0x0121	Sino Wealth Electronic Ltd.
290	0x0122	AirTurn, Inc.
291	0x0123	Kinsa, Inc
292	0x0124	HID Global
293	0x0125	SEAT es
294	0x0126	Promethean Ltd.
295	0x0127	Salutica Allied Solutions
296	0x0128	GPSI Group Pty Ltd
297	0x0129	Nimble Devices Oy
298	0x012A	Changzhou Yongse Infotech Co., Ltd.
299	0x012B	SportIQ
300	0x012C	TEMEC Instruments B.V.
301	0x012D	Sony Corporation
302	0x012E	ASSA ABLOY
303	0x012F	Clarion Co. Inc.
304	0x0130	Warehouse Innovations
305	0x0131	Cypress Semiconductor
306	0x0132	MADS Inc
307	0x0133	Blue Maestro Limited
308	0x0134	Resolution Products, Ltd.
309	0x0135	Aireware LLC
310	0x0136	Silvair, Inc.
311	0x0137	Prestigio Plaza Ltd.
312	0x0138	NTEO Inc.
313	0x0139	Focus Systems Corporation
314	0x013A	Tencent Holdings Ltd.
315	0x013B	Allegion
316	0x013C	Murata Manufacturing Co., Ltd.
317	0x013D	WirelessWERX
318	0x013E	Nod, Inc.
319	0x013F	B&B Manufacturing Company
320	0x0140	Alpine Electronics (China) Co., Ltd
321	0x0141	FedEx Services
322	0x0142	Grape Systems Inc.
323	0x0143	Bkon Connect
324	0x0144	Lintech GmbH
325	0x0145	Novatel Wireless
326	0x0146	Ciright
327	0x0147	Mighty Cast, Inc.
328	0x0148	Ambimat Electronics
329	0x0149	Perytons Ltd.
330	0x014A	Tivoli Audio, LLC
331	0x014B	Master Lock
332	0x014C	Mesh-Net Ltd
333	0x014D	HUIZHOU DESAY SV AUTOMOTIVE CO., LTD.
334	0x014E	Tangerine, Inc.
335	0x014F	B&W Group Ltd.
336	0x0150	Pioneer Corporation
337	0x0151	OnBeep
338	0x0152	Vernier Software & Technology
339	0x0153	ROL Ergo
340	0x0154	Pebble Technology
341	0x0155	NETATMO
342	0x0156	Accumulate AB
343	0x0157	Anhui Huami Information Technology Co., Ltd.
344	0x0158	Inmite s.r.o.
345	0x0159	ChefSteps, Inc.
346	0x015A	micas AG
347	0x015B	Biomedical Research Ltd.
348	0x015C	Pitius Tec S.L.
349	0x015D	Estimote, Inc.
350	0x015E	Unikey Technologies, Inc.
351	0x015F	Timer Cap Co.
352	0x0160	AwoX
353	0x0161	yikes
354	0x0162	MADSGlobalNZ Ltd.
355	0x0163	PCH International
356	0x0164	Qingdao Yeelink Information Technology Co., Ltd.
357	0x0165	Milwaukee Tool (Formally Milwaukee Electric Tools)
358	0x0166	MISHIK Pte Ltd
359	0x0167	Ascensia Diabetes Care US Inc.
360	0x0168	Spicebox LLC
361	0x0169	emberlight
362	0x016A	Cooper-Atkins Corporation
363	0x016B	Qblinks
364	0x016C	MYSPHERA
365	0x016D	LifeScan Inc
366	0x016E	Volantic AB
367	0x016F	Podo Labs, Inc
368	0x0170	Roche Diabetes Care AG
369	0x0171	Amazon Fulfillment Service
370	0x0172	Connovate Technology Private Limited
371	0x0173	Kocomojo, LLC
372	0x0174	Everykey Inc.
373	0x0175	Dynamic Controls
374	0x0176	SentriLock
375	0x0177	I-SYST inc.
376	0x0178	CASIO COMPUTER CO., LTD.
377	0x0179	LAPIS Semiconductor Co., Ltd.
378	0x017A	Telemonitor, Inc.
379	0x017B	taskit GmbH
380	0x017C	Daimler AG
381	0x017D	BatAndCat
382	0x017E	BluDotz Ltd
383	0x017F	XTel Wireless ApS
384	0x0180	Gigaset Communications GmbH
385	0x0181	Gecko Health Innovations, Inc.
386	0x0182	HOP Ubiquitous
387	0x0183	Walt Disney
388	0x0184	Nectar
389	0x0185	bel'apps LLC
390	0x0186	CORE Lighting Ltd
391	0x0187	Seraphim Sense Ltd
392	0x0188	Unico RBC
393	0x0189	Physical Enterprises Inc.
394	0x018A	Able Trend Technology Limited
395	0x018B	Konica Minolta, Inc.
396	0x018C	Wilo SE
397	0x018D	Extron Design Services
398	0x018E	Fitbit, Inc.
399	0x018F	Fireflies Systems
400	0x0190	Intelletto Technologies Inc.
401	0x0191	FDK CORPORATION
402	0x0192	Cloudleaf, Inc
403	0x0193	Maveric Automation LLC
404	0x0194	Acoustic Stream Corporation
405	0x0195	Zuli
406	0x0196	Paxton Access Ltd
407	0x0197	WiSilica Inc.
408	0x0198	VENGIT Korlatolt Felelossegu Tarsasag
409	0x0199	SALTO SYSTEMS S.L.
410	0x019A	TRON Forum (formerly T-Engine Forum)
411	0x019B	CUBETECH s.r.o.
412	0x019C	Cokiya Incorporated
413	0x019D	CVS Health
414	0x019E	Ceruus
415	0x019F	Strainstall Ltd
416	0x01A0	Channel Enterprises (HK) Ltd.
417	0x01A1	FIAMM
418	0x01A2	GIGALANE.CO.,LTD
419	0x01A3	EROAD
420	0x01A4	Mine Safety Appliances
421	0x01A5	Icon Health and Fitness
422	0x01A6	Wille Engineering (formely as Asandoo GmbH)
423	0x01A7	ENERGOUS CORPORATION
424	0x01A8	Taobao
425	0x01A9	Canon Inc.
426	0x01AA	Geophysical Technology Inc.
427	0x01AB	Facebook, Inc.
428	0x01AC	Trividia Health, Inc.
429	0x01AD	FlightSafety International
430	0x01AE	Earlens Corporation
431	0x01AF	Sunrise Micro Devices, Inc.
432	0x01B0	Star Micronics Co., Ltd.
433	0x01B1	Netizens Sp. z o.o.
434	0x01B2	Nymi Inc.
435	0x01B3	Nytec, Inc.
436	0x01B4	Trineo Sp. z o.o.
437	0x01B5	Nest Labs Inc.
438	0x01B6	LM Technologies Ltd
439	0x01B7	General Electric Company
440	0x01B8	i+D3 S.L.
441	0x01B9	HANA Micron
442	0x01BA	Stages Cycling LLC
443	0x01BB	Cochlear Bone Anchored Solutions AB
444	0x01BC	SenionLab AB
445	0x01BD	Syszone Co., Ltd
446	0x01BE	Pulsate Mobile Ltd.
447	0x01BF	Hong Kong HunterSun Electronic Limited
448	0x01C0	pironex GmbH
449	0x01C1	BRADATECH Corp.
450	0x01C2	Transenergooil AG
451	0x01C3	Bunch
452	0x01C4	DME Microelectronics
453	0x01C5	Bitcraze AB
454	0x01C6	HASWARE Inc.
455	0x01C7	Abiogenix Inc.
456	0x01C8	Poly-Control ApS
457	0x01C9	Avi-on
458	0x01CA	Laerdal Medical AS
459	0x01CB	Fetch My Pet
460	0x01CC	Sam Labs Ltd.
461	0x01CD	Chengdu Synwing Technology Ltd
462	0x01CE	HOUWA SYSTEM DESIGN, k.k.
463	0x01CF	BSH
464	0x01D0	Primus Inter Pares Ltd
465	0x01D1	August Home, Inc
466	0x01D2	Gill Electronics
467	0x01D3	Sky Wave Design
468	0x01D4	Newlab S.r.l.
469	0x01D5	ELAD srl
470	0x01D6	G-wearables inc.
471	0x01D7	Squadrone Systems Inc.
472	0x01D8	Code Corporation
473	0x01D9	Savant Systems LLC
474	0x01DA	Logitech International SA
475	0x01DB	Innblue Consulting
476	0x01DC	iParking Ltd.
477	0x01DD	Koninklijke Philips Electronics N.V.
478	0x01DE	Minelab Electronics Pty Limited
479	0x01DF	Bison Group Ltd.
480	0x01E0	Widex A/S
481	0x01E1	Jolla Ltd
482	0x01E2	Lectronix, Inc.
483	0x01E3	Caterpillar Inc
484	0x01E4	Freedom Innovations
485	0x01E5	Dynamic Devices Ltd
486	0x01E6	Technology Solutions (UK) Ltd
487	0x01E7	IPS Group Inc.
488	0x01E8	STIR
489	0x01E9	Sano, Inc.
490	0x01EA	Advanced Application Design, Inc.
491	0x01EB	AutoMap LLC
492	0x01EC	Spreadtrum Communications Shanghai Ltd
493	0x01ED	CuteCircuit LTD
494	0x01EE	Valeo Service
495	0x01EF	Fullpower Technologies, Inc.
496	0x01F0	KloudNation
497	0x01F1	Zebra Technologies Corporation
498	0x01F2	Itron, Inc.
499	0x01F3	The University of Tokyo
500	0x01F4	UTC Fire and Security
501	0x01F5	Cool Webthings Limited
502	0x01F6	DJO Global
503	0x01F7	Gelliner Limited
504	0x01F8	Anyka (Guangzhou) Microelectronics Technology Co, LTD
505	0x01F9	Medtronic Inc.
506	0x01FA	Gozio Inc.
507	0x01FB	Form Lifting, LLC
508	0x01FC	Wahoo Fitness, LLC
509	0x01FD	Kontakt Micro-Location Sp. z o.o.
510	0x01FE	Radio Systems Corporation
511	0x01FF	Freescale Semiconductor, Inc.
512	0x0200	Verifone Systems Pte Ltd. Taiwan Branch
513	0x0201	AR Timing
514	0x0202	Rigado LLC
515	0x0203	Kemppi Oy
516	0x0204	Tapcentive Inc.
517	0x0205	Smartbotics Inc.
518	0x0206	Otter Products, LLC
519	0x0207	STEMP Inc.
520	0x0208	LumiGeek LLC
521	0x0209	InvisionHeart Inc.
522	0x020A	Macnica Inc.
523	0x020B	Jaguar Land Rover Limited
524	0x020C	CoroWare Technologies, Inc
525	0x020D	Simplo Technology Co., LTD
526	0x020E	Omron Healthcare Co., LTD
527	0x020F	Comodule GMBH
528	0x0210	ikeGPS
529	0x0211	Telink Semiconductor Co. Ltd
530	0x0212	Interplan Co., Ltd
531	0x0213	Wyler AG
532	0x0214	IK Multimedia Production srl
533	0x0215	Lukoton Experience Oy
534	0x0216	MTI Ltd
535	0x0217	Tech4home, Lda
536	0x0218	Hiotech AB
537	0x0219	DOTT Limited
538	0x021A	Blue Speck Labs, LLC
539	0x021B	Cisco Systems, Inc
540	0x021C	Mobicomm Inc
541	0x021D	Edamic
542	0x021E	Goodnet, Ltd
543	0x021F	Luster Leaf Products Inc
544	0x0220	Manus Machina BV
545	0x0221	Mobiquity Networks Inc
546	0x0222	Praxis Dynamics
547	0x0223	Philip Morris Products S.A.
548	0x0224	Comarch SA
549	0x0225	Nestl Nespresso S.A.
550	0x0226	Merlinia A/S
551	0x0227	LifeBEAM Technologies
552	0x0228	Twocanoes Labs, LLC
553	0x0229	Muoverti Limited
554	0x022A	Stamer Musikanlagen GMBH
555	0x022B	Tesla Motors
556	0x022C	Pharynks Corporation
557	0x022D	Lupine
558	0x022E	Siemens AG
559	0x022F	Huami (Shanghai) Culture Communication CO., LTD
560	0x0230	Foster Electric Company, Ltd
561	0x0231	ETA SA
562	0x0232	x-Senso Solutions Kft
563	0x0233	Shenzhen SuLong Communication Ltd
564	0x0234	FengFan (BeiJing) Technology Co, Ltd
565	0x0235	Qrio Inc
566	0x0236	Pitpatpet Ltd
567	0x0237	MSHeli s.r.l.
568	0x0238	Trakm8 Ltd
569	0x0239	JIN CO, Ltd
570	0x023A	Alatech Tehnology
571	0x023B	Beijing CarePulse Electronic Technology Co, Ltd
572	0x023C	Awarepoint
573	0x023D	ViCentra B.V.
574	0x023E	Raven Industries
575	0x023F	WaveWare Technologies Inc.
576	0x0240	Argenox Technologies
577	0x0241	Bragi GmbH
578	0x0242	16Lab Inc
579	0x0243	Masimo Corp
580	0x0244	Iotera Inc
581	0x0245	Endress+Hauser
582	0x0246	ACKme Networks, Inc.
583	0x0247	FiftyThree Inc.
584	0x0248	Parker Hannifin Corp
585	0x0249	Transcranial Ltd
586	0x024A	Uwatec AG
587	0x024B	Orlan LLC
588	0x024C	Blue Clover Devices
589	0x024D	M-Way Solutions GmbH
590	0x024E	Microtronics Engineering GmbH
591	0x024F	Schneider Schreibgerte GmbH
592	0x0250	Sapphire Circuits LLC
593	0x0251	Lumo Bodytech Inc.
594	0x0252	UKC Technosolution
595	0x0253	Xicato Inc.
596	0x0254	Playbrush
597	0x0255	Dai Nippon Printing Co., Ltd.
598	0x0256	G24 Power Limited
599	0x0257	AdBabble Local Commerce Inc.
600	0x0258	Devialet SA
601	0x0259	ALTYOR
602	0x025A	University of Applied Sciences Valais/Haute Ecole Valaisanne
603	0x025B	Five Interactive, LLC dba Zendo
604	0x025C	NetEaseHangzhouNetwork co.Ltd.
605	0x025D	Lexmark International Inc.
606	0x025E	Fluke Corporation
607	0x025F	Yardarm Technologies
608	0x0260	SensaRx
609	0x0261	SECVRE GmbH
610	0x0262	Glacial Ridge Technologies
611	0x0263	Identiv, Inc.
612	0x0264	DDS, Inc.
613	0x0265	SMK Corporation
614	0x0266	Schawbel Technologies LLC
615	0x0267	XMI Systems SA
616	0x0268	Cerevo
617	0x0269	Torrox GmbH & Co KG
618	0x026A	Gemalto
619	0x026B	DEKA Research & Development Corp.
620	0x026C	Domster Tadeusz Szydlowski
621	0x026D	Technogym SPA
622	0x026E	FLEURBAEY BVBA
623	0x026F	Aptcode Solutions
624	0x0270	LSI ADL Technology
625	0x0271	Animas Corp
626	0x0272	Alps Electric Co., Ltd.
627	0x0273	OCEASOFT
628	0x0274	Motsai Research
629	0x0275	Geotab
630	0x0276	E.G.O. Elektro-Gertebau GmbH
631	0x0277	bewhere inc
632	0x0278	Johnson Outdoors Inc
633	0x0279	steute Schaltgerate GmbH & Co. KG
634	0x027A	Ekomini inc.
635	0x027B	DEFA AS
636	0x027C	Aseptika Ltd
637	0x027D	HUAWEI Technologies Co., Ltd. ( )
638	0x027E	HabitAware, LLC
639	0x027F	ruwido austria gmbh
640	0x0280	ITEC corporation
641	0x0281	StoneL
642	0x0282	Sonova AG
643	0x0283	Maven Machines, Inc.
644	0x0284	Synapse Electronics
645	0x0285	Standard Innovation Inc.
646	0x0286	RF Code, Inc.
647	0x0287	Wally Ventures S.L.
648	0x0288	Willowbank Electronics Ltd
649	0x0289	SK Telecom
650	0x028A	Jetro AS
651	0x028B	Code Gears LTD
652	0x028C	NANOLINK APS
653	0x028D	IF, LLC
654	0x028E	RF Digital Corp
655	0x028F	Church & Dwight Co., Inc
656	0x0290	Multibit Oy
657	0x0291	CliniCloud Inc
658	0x0292	SwiftSensors
659	0x0293	Blue Bite
660	0x0294	ELIAS GmbH
661	0x0295	Sivantos GmbH
662	0x0296	Petzl
663	0x0297	storm power ltd
664	0x0298	EISST Ltd
665	0x0299	Inexess Technology Simma KG
666	0x029A	Currant, Inc.
667	0x029B	C2 Development, Inc.
668	0x029C	Blue Sky Scientific, LLC
669	0x029D	ALOTTAZS LABS, LLC
670	0x029E	Kupson spol. s r.o.
671	0x029F	Areus Engineering GmbH
672	0x02A0	Impossible Camera GmbH
673	0x02A1	InventureTrack Systems
674	0x02A2	LockedUp
675	0x02A3	Itude
676	0x02A4	Pacific Lock Company
677	0x02A5	Tendyron Corporation ( )
678	0x02A6	Robert Bosch GmbH
679	0x02A7	Illuxtron international B.V.
680	0x02A8	miSport Ltd.
681	0x02A9	Chargelib
682	0x02AA	Doppler Lab
683	0x02AB	BBPOS Limited
684	0x02AC	RTB Elektronik GmbH & Co. KG
685	0x02AD	Rx Networks, Inc.
686	0x02AE	WeatherFlow, Inc.
687	0x02AF	Technicolor USA Inc.
688	0x02B0	Bestechnic(Shanghai),Ltd
689	0x02B1	Raden Inc
690	0x02B2	JouZen Oy
691	0x02B3	CLABER S.P.A.
692	0x02B4	Hyginex, Inc.
693	0x02B5	HANSHIN ELECTRIC RAILWAY CO.,LTD.
694	0x02B6	Schneider Electric
695	0x02B7	Oort Technologies LLC
696	0x02B8	Chrono Therapeutics
697	0x02B9	Rinnai Corporation
698	0x02BA	Swissprime Technologies AG
699	0x02BB	Koha.,Co.Ltd
700	0x02BC	Genevac Ltd
701	0x02BD	Chemtronics
702	0x02BE	Seguro Technology Sp. z o.o.
703	0x02BF	Redbird Flight Simulations
704	0x02C0	Dash Robotics
705	0x02C1	LINE Corporation
706	0x02C2	Guillemot Corporation
707	0x02C3	Techtronic Power Tools Technology Limited
708	0x02C4	Wilson Sporting Goods
709	0x02C5	Lenovo (Singapore) Pte Ltd. ( )
710	0x02C6	Ayatan Sensors
711	0x02C7	Electronics Tomorrow Limited
712	0x02C8	VASCO Data Security International, Inc.
713	0x02C9	PayRange Inc.
714	0x02CA	ABOV Semiconductor
715	0x02CB	AINA-Wireless Inc.
716	0x02CC	Eijkelkamp Soil & Water
717	0x02CD	BMA ergonomics b.v.
718	0x02CE	Teva Branded Pharmaceutical Products R&D, Inc.
719	0x02CF	Anima
720	0x02D0	3M
721	0x02D1	Empatica Srl
722	0x02D2	Afero, Inc.
723	0x02D3	Powercast Corporation
724	0x02D4	Secuyou ApS
725	0x02D5	OMRON Corporation
726	0x02D6	Send Solutions
727	0x02D7	NIPPON SYSTEMWARE CO.,LTD.
728	0x02D8	Neosfar
729	0x02D9	Fliegl Agrartechnik GmbH
730	0x02DA	Gilvader
731	0x02DB	Digi International Inc (R)
732	0x02DC	DeWalch Technologies, Inc.
733	0x02DD	Flint Rehabilitation Devices, LLC
734	0x02DE	Samsung SDS Co., Ltd.
735	0x02DF	Blur Product Development
736	0x02E0	University of Michigan
737	0x02E1	Victron Energy BV
738	0x02E2	NTT docomo
739	0x02E3	Carmanah Technologies Corp.
740	0x02E4	Bytestorm Ltd.
741	0x02E5	Espressif Incorporated ( () )
742	0x02E6	Unwire
743	0x02E7	Connected Yard, Inc.
744	0x02E8	American Music Environments
745	0x02E9	Sensogram Technologies, Inc.
746	0x02EA	Fujitsu Limited
747	0x02EB	Ardic Technology
748	0x02EC	Delta Systems, Inc
749	0x02ED	HTC Corporation
750	0x02EE	Citizen Holdings Co., Ltd.
751	0x02EF	SMART-INNOVATION.inc
752	0x02F0	Blackrat Software
753	0x02F1	The Idea Cave, LLC
754	0x02F2	GoPro, Inc.
755	0x02F3	AuthAir, Inc
756	0x02F4	Vensi, Inc.
757	0x02F5	Indagem Tech LLC
758	0x02F6	Intemo Technologies
759	0x02F7	DreamVisions co., Ltd.
760	0x02F8	Runteq Oy Ltd
761	0x02F9	IMAGINATION TECHNOLOGIES LTD
762	0x02FA	CoSTAR TEchnologies
763	0x02FB	Clarius Mobile Health Corp.
764	0x02FC	Shanghai Frequen Microelectronics Co., Ltd.
765	0x02FD	Uwanna, Inc.
766	0x02FE	Lierda Science & Technology Group Co., Ltd.
767	0x02FF	Silicon Laboratories
768	0x0300	World Moto Inc.
769	0x0301	Giatec Scientific Inc.
770	0x0302	Loop Devices, Inc
771	0x0303	IACA electronique
772	0x0304	Proxy Technologies, Inc.
773	0x0305	Swipp ApS
774	0x0306	Life Laboratory Inc.
775	0x0307	FUJI INDUSTRIAL CO.,LTD.
776	0x0308	Surefire, LLC
777	0x0309	Dolby Labs
778	0x030A	Ellisys
779	0x030B	Magnitude Lighting Converters
780	0x030C	Hilti AG
781	0x030D	Devdata S.r.l.
782	0x030E	Deviceworx
783	0x030F	Shortcut Labs
784	0x0310	SGL Italia S.r.l.
785	0x0311	PEEQ DATA
786	0x0312	Ducere Technologies Pvt Ltd
787	0x0313	DiveNav, Inc.
788	0x0314	RIIG AI Sp. z o.o.
789	0x0315	Thermo Fisher Scientific
790	0x0316	AG Measurematics Pvt. Ltd.
791	0x0317	CHUO Electronics CO., LTD.
792	0x0318	Aspenta International
793	0x0319	Eugster Frismag AG
794	0x031A	Amber wireless GmbH
795	0x031B	HQ Inc
796	0x031C	Lab Sensor Solutions
797	0x031D	Enterlab ApS
798	0x031E	Eyefi, Inc.
799	0x031F	MetaSystem S.p.A.
800	0x0320	SONO ELECTRONICS. CO., LTD
801	0x0321	Jewelbots
802	0x0322	Compumedics Limited
803	0x0323	Rotor Bike Components
804	0x0324	Astro, Inc.
805	0x0325	Amotus Solutions
806	0x0326	Healthwear Technologies (Changzhou)Ltd
807	0x0327	Essex Electronics
808	0x0328	Grundfos A/S
809	0x0329	Eargo, Inc.
810	0x032A	Electronic Design Lab
811	0x032B	ESYLUX
812	0x032C	NIPPON SMT.CO.,Ltd
813	0x032D	BM innovations GmbH
814	0x032E	indoormap
815	0x032F	OttoQ Inc
816	0x0330	North Pole Engineering
817	0x0331	3flares Technologies Inc.
818	0x0332	Electrocompaniet A.S.
819	0x0333	Mul-T-Lock
820	0x0334	Corentium AS
821	0x0335	Enlighted Inc
822	0x0336	GISTIC
823	0x0337	AJP2 Holdings, LLC
824	0x0338	COBI GmbH
825	0x0339	Blue Sky Scientific, LLC
826	0x033A	Appception, Inc.
827	0x033B	Courtney Thorne Limited
828	0x033C	Virtuosys
829	0x033D	TPV Technology Limited
830	0x033E	Monitra SA
831	0x033F	Automation Components, Inc.
832	0x0340	Letsense s.r.l.
833	0x0341	Etesian Technologies LLC
834	0x0342	GERTEC BRASIL LTDA.
835	0x0343	Drekker Development Pty. Ltd.
836	0x0344	Whirl Inc
837	0x0345	Locus Positioning
838	0x0346	Acuity Brands Lighting, Inc
839	0x0347	Prevent Biometrics
840	0x0348	Arioneo
841	0x0349	VersaMe
842	0x034A	Vaddio
843	0x034B	Libratone A/S
844	0x034C	HM Electronics, Inc.
845	0x034D	TASER International, Inc.
846	0x034E	SafeTrust Inc.
847	0x034F	Heartland Payment Systems
848	0x0350	Bitstrata Systems Inc.
849	0x0351	Pieps GmbH
850	0x0352	iRiding(Xiamen)Technology Co.,Ltd.
851	0x0353	Alpha Audiotronics, Inc.
852	0x0354	TOPPAN FORMS CO.,LTD.
853	0x0355	Sigma Designs, Inc.
854	0x0356	Spectrum Brands, Inc.
855	0x0357	Polymap Wireless
856	0x0358	MagniWare Ltd.
857	0x0359	Novotec Medical GmbH
858	0x035A	Medicom Innovation Partner a/s
859	0x035B	Matrix Inc.
860	0x035C	Eaton Corporation
861	0x035D	KYS
862	0x035E	Naya Health, Inc.
863	0x035F	Acromag
864	0x0360	Insulet Corporation
865	0x0361	Wellinks Inc.
866	0x0362	ON Semiconductor
867	0x0363	FREELAP SA
868	0x0364	Favero Electronics Srl
869	0x0365	BioMech Sensor LLC
870	0x0366	BOLTT Sports technologies Private limited
871	0x0367	Saphe International
872	0x0368	Metormote AB
873	0x0369	littleBits
874	0x036A	SetPoint Medical
875	0x036B	BRControls Products BV
876	0x036C	Zipcar
877	0x036D	AirBolt Pty Ltd
878	0x036E	KeepTruckin Inc
879	0x036F	Motiv, Inc.
880	0x0370	Wazombi Labs O
881	0x0371	ORBCOMM
882	0x0372	Nixie Labs, Inc.
883	0x0373	AppNearMe Ltd
884	0x0374	Holman Industries
885	0x0375	Expain AS
886	0x0376	Electronic Temperature Instruments Ltd
887	0x0377	Plejd AB
888	0x0378	Propeller Health
889	0x0379	Shenzhen iMCO Electronic Technology Co.,Ltd
890	0x037A	Algoria
891	0x037B	Apption Labs Inc.
892	0x037C	Cronologics Corporation
893	0x037D	MICRODIA Ltd.
894	0x037E	lulabytes S.L.
895	0x037F	Nestec S.A.
896	0x0380	LLC "MEGA-F service"
897	0x0381	Sharp Corporation
898	0x0382	Precision Outcomes Ltd
899	0x0383	Kronos Incorporated
900	0x0384	OCOSMOS Co., Ltd.
901	0x0385	Embedded Electronic Solutions Ltd. dba e2Solutions
902	0x0386	Aterica Inc.
903	0x0387	BluStor PMC, Inc.
904	0x0388	Kapsch TrafficCom AB
905	0x0389	ActiveBlu Corporation
906	0x038A	Kohler Mira Limited
907	0x038B	Noke
908	0x038C	Appion Inc.
909	0x038D	Resmed Ltd
910	0x038E	Crownstone B.V.
911	0x038F	Xiaomi Inc.
912	0x0390	INFOTECH s.r.o.
913	0x0391	Thingsquare AB
914	0x0392	T&D
915	0x0393	LAVAZZA S.p.A.
916	0x0394	Netclearance Systems, Inc.
917	0x0395	SDATAWAY
918	0x0396	BLOKS GmbH
919	0x0397	LEGO System A/S
920	0x0398	Thetatronics Ltd
921	0x0399	Nikon Corporation
922	0x039A	NeST
923	0x039B	South Silicon Valley Microelectronics
924	0x039C	ALE International
925	0x039D	CareView Communications, Inc.
926	0x039E	SchoolBoard Limited
927	0x039F	Molex Corporation
928	0x03A0	IVT Wireless Limited
929	0x03A1	Alpine Labs LLC
930	0x03A2	Candura Instruments
931	0x03A3	SmartMovt Technology Co., Ltd
932	0x03A4	Token Zero Ltd
933	0x03A5	ACE CAD Enterprise Co., Ltd. (ACECAD)
934	0x03A6	Medela, Inc
935	0x03A7	AeroScout
936	0x03A8	Esrille Inc.
937	0x03A9	THINKERLY SRL
938	0x03AA	Exon Sp. z o.o.
939	0x03AB	Meizu Technology Co., Ltd.
940	0x03AC	Smablo LTD
941	0x03AD	XiQ
942	0x03AE	Allswell Inc.
943	0x03AF	Comm-N-Sense Corp DBA Verigo
944	0x03B0	VIBRADORM GmbH
945	0x03B1	Otodata Wireless Network Inc.
946	0x03B2	Propagation Systems Limited
947	0x03B3	Midwest Instruments & Controls
948	0x03B4	Alpha Nodus, inc.
949	0x03B5	petPOMM, Inc
950	0x03B6	Mattel
951	0x03B7	Airbly Inc.
952	0x03B8	A-Safe Limited
953	0x03B9	FREDERIQUE CONSTANT SA
954	0x03BA	Maxscend Microelectronics Company Limited
955	0x03BB	Abbott Diabetes Care
956	0x03BC	ASB Bank Ltd
957	0x03BD	amadas
958	0x03BE	Applied Science, Inc.
959	0x03BF	iLumi Solutions Inc.
960	0x03C0	Arch Systems Inc.
961	0x03C1	Ember Technologies, Inc.
962	0x03C2	Snapchat Inc
963	0x03C3	Casambi Technologies Oy
964	0x03C4	Pico Technology Inc.
965	0x03C5	St. Jude Medical, Inc.
966	0x03C6	Intricon
967	0x03C7	Structural Health Systems, Inc.
968	0x03C8	Avvel International
969	0x03C9	Gallagher Group
970	0x03CA	In2things Automation Pvt. Ltd.
971	0x03CB	SYSDEV Srl
972	0x03CC	Vonkil Technologies Ltd
973	0x03CD	Wynd Technologies, Inc.
974	0x03CE	CONTRINEX S.A.
975	0x03CF	MIRA, Inc.
976	0x03D0	Watteam Ltd
977	0x03D1	Density Inc.
978	0x03D2	IOT Pot India Private Limited
979	0x03D3	Sigma Connectivity AB
980	0x03D4	PEG PEREGO SPA
981	0x03D5	Wyzelink Systems Inc.
982	0x03D6	Yota Devices LTD
983	0x03D7	FINSECUR
984	0x03D8	Zen-Me Labs Ltd
985	0x03D9	3IWare Co., Ltd.
986	0x03DA	EnOcean GmbH
987	0x03DB	Instabeat, Inc
988	0x03DC	Nima Labs
989	0x03DD	Andreas Stihl AG & Co. KG
990	0x03DE	Nathan Rhoades LLC
991	0x03DF	Grob Technologies, LLC
992	0x03E0	Actions (Zhuhai) Technology Co., Limited
993	0x03E1	SPD Development Company Ltd
994	0x03E2	Sensoan Oy
995	0x03E3	Qualcomm Life Inc
996	0x03E4	Chip-ing AG
997	0x03E5	ffly4u
998	0x03E6	IoT Instruments Oy
999	0x03E7	TRUE Fitness Technology
1000	0x03E8	Reiner Kartengeraete GmbH & Co. KG.
1001	0x03E9	SHENZHEN LEMONJOY TECHNOLOGY CO., LTD.
1002	0x03EA	Hello Inc.
1003	0x03EB	Evollve Inc.
1004	0x03EC	Jigowatts Inc.
1005	0x03ED	BASIC MICRO.COM,INC.
1006	0x03EE	CUBE TECHNOLOGIES
1007	0x03EF	foolography GmbH
1008	0x03F0	CLINK
1009	0x03F1	Hestan Smart Cooking Inc.
1010	0x03F2	WindowMaster A/S
1011	0x03F3	Flowscape AB
1012	0x03F4	PAL Technologies Ltd
1013	0x03F5	WHERE, Inc.
1014	0x03F6	Iton Technology Corp.
1015	0x03F7	Owl Labs Inc.
1016	0x03F8	Rockford Corp.
1017	0x03F9	Becon Technologies Co.,Ltd.
1018	0x03FA	Vyassoft Technologies Inc
1019	0x03FB	Nox Medical
1020	0x03FC	Kimberly-Clark
1021	0x03FD	Trimble Navigation Ltd.
1022	0x03FE	Littelfuse
1023	0x03FF	Withings
1024	0x0400	i-developer IT Beratung UG
1025	0x0401	
1026	0x0402	Sears Holdings Corporation
1027	0x0403	Gantner Electronic GmbH
1028	0x0404	Authomate Inc
1029	0x0405	Vertex International, Inc.
1030	0x0406	Airtago
1031	0x0407	Swiss Audio SA
1032	0x0408	ToGetHome Inc.
1033	0x0409	AXIS
1034	0x040A	Openmatics
1035	0x040B	Jana Care Inc.
1036	0x040C	Senix Corporation
1037	0x040D	NorthStar Battery Company, LLC
1038	0x040E	SKF (U.K.) Limited
1039	0x040F	CO-AX Technology, Inc.
1040	0x0410	Fender Musical Instruments
1041	0x0411	Luidia Inc
1042	0x0412	SEFAM
1043	0x0413	Wireless Cables Inc
1044	0x0414	Lightning Protection International Pty Ltd
1045	0x0415	Uber Technologies Inc
1046	0x0416	SODA GmbH
1047	0x0417	Fatigue Science
1048	0x0418	Alpine Electronics Inc.
1049	0x0419	Novalogy LTD
1050	0x041A	Friday Labs Limited
1051	0x041B	OrthoAccel Technologies
1052	0x041C	WaterGuru, Inc.
1053	0x041D	Benning Elektrotechnik und Elektronik GmbH & Co. KG
1054	0x041E	Dell Computer Corporation
1055	0x041F	Kopin Corporation
1056	0x0420	TecBakery GmbH
1057	0x0421	Backbone Labs, Inc.
1058	0x0422	DELSEY SA
1059	0x0423	Chargifi Limited
1060	0x0424	Trainesense Ltd.
1061	0x0425	Unify Software and Solutions GmbH & Co. KG
1062	0x0426	Husqvarna AB
1063	0x0427	Focus fleet and fuel management inc
1064	0x0428	SmallLoop, LLC
1065	0x0429	Prolon Inc.
1066	0x042A	BD Medical
1067	0x042B	iMicroMed Incorporated
1068	0x042C	Ticto N.V.
1069	0x042D	Meshtech AS
1070	0x042E	MemCachier Inc.
1071	0x042F	Danfoss A/S
1072	0x0430	SnapStyk Inc.
1073	0x0431	Amway Corporation
1074	0x0432	Silk Labs, Inc.
1075	0x0433	Pillsy Inc.
1076	0x0434	Hatch Baby, Inc.
1077	0x0435	Blocks Wearables Ltd.
1078	0x0436	Drayson Technologies (Europe) Limited
1079	0x0437	eBest IOT Inc.
1080	0x0438	Helvar Ltd
1081	0x0439	Radiance Technologies
1082	0x043A	Nuheara Limited
1083	0x043B	Appside co., ltd.
1084	0x043C	DeLaval
1085	0x043D	Coiler Corporation
1086	0x043E	Thermomedics, Inc.
1087	0x043F	Tentacle Sync GmbH
1088	0x0440	Valencell, Inc.
1089	0x0441	iProtoXi Oy
1090	0x0442	SECOM CO., LTD.
1091	0x0443	Tucker International LLC
1092	0x0444	Metanate Limited
1093	0x0445	Kobian Canada Inc.
1094	0x0446	NETGEAR, Inc.
1095	0x0447	Fabtronics Australia Pty Ltd
1096	0x0448	Grand Centrix GmbH
1097	0x0449	1UP USA.com llc
1098	0x044A	SHIMANO INC.
1099	0x044B	Nain Inc.
1100	0x044C	LifeStyle Lock, LLC
1101	0x044D	VEGA Grieshaber KG
1102	0x044E	Xtrava Inc.
1103	0x044F	TTS Tooltechnic Systems AG & Co. KG
1104	0x0450	Teenage Engineering AB
1105	0x0451	Tunstall Nordic AB
1106	0x0452	Svep Design Center AB
1107	0x0453	GreenPeak Technologies BV
1108	0x0454	Sphinx Electronics GmbH & Co KG
1109	0x0455	Atomation
1110	0x0456	Nemik Consulting Inc
1111	0x0457	RF INNOVATION
1112	0x0458	Mini Solution Co., Ltd.
1113	0x0459	Lumenetix, Inc
1114	0x045A	2048450 Ontario Inc
1115	0x045B	SPACEEK LTD
1116	0x045C	Delta T Corporation
1117	0x045D	Boston Scientific Corporation
1118	0x045E	Nuviz, Inc.
1119	0x045F	Real Time Automation, Inc.
1120	0x0460	Kolibree
1121	0x0461	vhf elektronik GmbH
1122	0x0462	Bonsai Systems GmbH
1123	0x0463	Fathom Systems Inc.
1124	0x0464	Bellman & Symfon
1125	0x0465	International Forte Group LLC
1126	0x0466	CycleLabs Solutions inc.
1127	0x0467	Codenex Oy
1128	0x0468	Kynesim Ltd
1129	0x0469	Palago AB
1130	0x046A	INSIGMA INC.
1131	0x046B	PMD Solutions
1132	0x046C	Qingdao Realtime Technology Co., Ltd.
1133	0x046D	BEGA Gantenbrink-Leuchten KG
1134	0x046E	Pambor Ltd.
1135	0x046F	Develco Products A/S
1136	0x0470	iDesign s.r.l.
1137	0x0471	TiVo Corp
1138	0x0472	Control-J Pty Ltd
1139	0x0473	Steelcase, Inc.
1140	0x0474	iApartment co., ltd.
1141	0x0475	Icom inc.
1142	0x0476	Oxstren Wearable Technologies Private Limited
1143	0x0477	Blue Spark Technologies
1144	0x0478	FarSite Communications Limited
1145	0x0479	mywerk system GmbH
1146	0x047A	Sinosun Technology Co., Ltd.
1147	0x047B	MIYOSHI ELECTRONICS CORPORATION
1148	0x047C	POWERMAT LTD
1149	0x047D	Occly LLC
1150	0x047E	OurHub Dev IvS
1151	0x047F	Pro-Mark, Inc.
1152	0x0480	Dynometrics Inc.
1153	0x0481	Quintrax Limited
1154	0x0482	POS Tuning Udo Vosshenrich GmbH & Co. KG
1155	0x0483	Multi Care Systems B.V.
1156	0x0484	Revol Technologies Inc
1157	0x0485	SKIDATA AG
1158	0x0486	DEV TECNOLOGIA INDUSTRIA, COMERCIO E MANUTENCAO DE EQUIPAMENTOS LTDA. - ME
1159	0x0487	Centrica Connected Home
1160	0x0488	Automotive Data Solutions Inc
1161	0x0489	Igarashi Engineering
1162	0x048A	Taelek Oy
1163	0x048B	CP Electronics Limited
1164	0x048C	Vectronix AG
1165	0x048D	S-Labs Sp. z o.o.
1166	0x048E	Companion Medical, Inc.
1167	0x048F	BlueKitchen GmbH
1168	0x0490	Matting AB
1169	0x0491	SOREX - Wireless Solutions GmbH
1170	0x0492	ADC Technology, Inc.
1171	0x0493	Lynxemi Pte Ltd
1172	0x0494	SENNHEISER electronic GmbH & Co. KG
1173	0x0495	LMT Mercer Group, Inc
1174	0x0496	Polymorphic Labs LLC
1175	0x0497	Cochlear Limited
1176	0x0498	METER Group, Inc. USA
1177	0x0499	Ruuvi Innovations Ltd.
1178	0x049A	Situne AS
1179	0x049B	nVisti, LLC
1180	0x049C	DyOcean
1181	0x049D	Uhlmann & Zacher GmbH
1182	0x049E	AND!XOR LLC
1183	0x049F	tictote AB
1184	0x04A0	Vypin, LLC
1185	0x04A1	PNI Sensor Corporation
1186	0x04A2	ovrEngineered, LLC
1187	0x04A3	GT-tronics HK Ltd
1188	0x04A4	Herbert Waldmann GmbH & Co. KG
1189	0x04A5	Guangzhou FiiO Electronics Technology Co.,Ltd
1190	0x04A6	Vinetech Co., Ltd
1191	0x04A7	Dallas Logic Corporation
1192	0x04A8	BioTex, Inc.
1193	0x04A9	DISCOVERY SOUND TECHNOLOGY, LLC
1194	0x04AA	LINKIO SAS
1195	0x04AB	Harbortronics, Inc.
1196	0x04AC	Undagrid B.V.
1197	0x04AD	Shure Inc
1198	0x04AE	ERM Electronic Systems LTD
1199	0x04AF	BIOROWER Handelsagentur GmbH
1200	0x04B0	Weba Sport und Med. Artikel GmbH
1201	0x04B1	Kartographers Technologies Pvt. Ltd.
1202	0x04B2	The Shadow on the Moon
1203	0x04B3	mobike (Hong Kong) Limited
1204	0x04B4	Inuheat Group AB
1205	0x04B5	Swiftronix AB
1206	0x04B6	Diagnoptics Technologies
1207	0x04B7	Analog Devices, Inc.
1208	0x04B8	Soraa Inc.
1209	0x04B9	CSR Building Products Limited
1210	0x04BA	Crestron Electronics, Inc.
1211	0x04BB	Neatebox Ltd
1212	0x04BC	Draegerwerk AG & Co. KGaA
1213	0x04BD	AlbynMedical
1214	0x04BE	Averos FZCO
1215	0x04BF	VIT Initiative, LLC
1216	0x04C0	Statsports International
1217	0x04C1	Sospitas, s.r.o.
1218	0x04C2	Dmet Products Corp.
1219	0x04C3	Mantracourt Electronics Limited
1220	0x04C4	TeAM Hutchins AB
1221	0x04C5	Seibert Williams Glass, LLC
1222	0x04C6	Insta GmbH
1223	0x04C7	Svantek Sp. z o.o.
1224	0x04C8	Shanghai Flyco Electrical Appliance Co., Ltd.
1225	0x04C9	Thornwave Labs Inc
1226	0x04CA	Steiner-Optik GmbH
1227	0x04CB	Novo Nordisk A/S
1228	0x04CC	Enflux Inc.
1229	0x04CD	Safetech Products LLC
1230	0x04CE	GOOOLED S.R.L.
1231	0x04CF	DOM Sicherheitstechnik GmbH & Co. KG
1232	0x04D0	Olympus Corporation
1233	0x04D1	KTS GmbH
1234	0x04D2	Anloq Technologies Inc.
1235	0x04D3	Queercon, Inc
1236	0x04D4	5th Element Ltd
1237	0x04D5	Gooee Limited
1238	0x04D6	LUGLOC LLC
1239	0x04D7	Blincam, Inc.
1240	0x04D8	FUJIFILM Corporation
1241	0x04D9	RandMcNally
1242	0x04DA	Franceschi Marina snc
1243	0x04DB	Engineered Audio, LLC.
1244	0x04DC	IOTTIVE (OPC) PRIVATE LIMITED
1245	0x04DD	4MOD Technology
1246	0x04DE	Lutron Electronics Co., Inc.
1247	0x04DF	Emerson
1248	0x04E0	Guardtec, Inc.
1249	0x04E1	REACTEC LIMITED
1250	0x04E2	EllieGrid
1251	0x04E3	Under Armour
1252	0x04E4	Woodenshark
1253	0x04E5	Avack Oy
1254	0x04E6	Smart Solution Technology, Inc.
1255	0x04E7	REHABTRONICS INC.
1256	0x04E8	STABILO International
1257	0x04E9	Busch Jaeger Elektro GmbH
1258	0x04EA	Pacific Bioscience Laboratories, Inc
1259	0x04EB	Bird Home Automation GmbH
1260	0x04EC	Motorola Solutions
1261	0x04ED	R9 Technology, Inc.
1262	0x04EE	Auxivia
1263	0x04EF	DaisyWorks, Inc
1264	0x04F0	Kosi Limited
1265	0x04F1	Theben AG
1266	0x04F2	InDreamer Techsol Private Limited
1267	0x04F3	Cerevast Medical
1268	0x04F4	ZanCompute Inc.
1269	0x04F5	Pirelli Tyre S.P.A.
1270	0x04F6	McLear Limited
1271	0x04F7	Shenzhen Huiding Technology Co.,Ltd.
1272	0x04F8	Convergence Systems Limited
1273	0x04F9	Interactio
1274	0x04FA	Androtec GmbH
1275	0x04FB	Benchmark Drives GmbH & Co. KG
1276	0x04FC	SwingLync L. L. C.
1277	0x04FD	Tapkey GmbH
1278	0x04FE	Woosim Systems Inc.
1279	0x04FF	Microsemi Corporation
1280	0x0500	Wiliot LTD.
1281	0x0501	Polaris IND
1282	0x0502	Specifi-Kali LLC
1283	0x0503	Locoroll, Inc
1284	0x0504	PHYPLUS Inc
1285	0x0505	Inplay Technologies LLC
1286	0x0506	Hager
1287	0x0507	Yellowcog
1288	0x0508	Axes System sp. z o. o.
1289	0x0509	myLIFTER Inc.
1290	0x050A	Shake-on B.V.
1291	0x050B	Vibrissa Inc.
1292	0x050C	OSRAM GmbH
1293	0x050D	TRSystems GmbH
1294	0x050E	Yichip Microelectronics (Hangzhou) Co.,Ltd.
1295	0x050F	Foundation Engineering LLC
1296	0x0510	UNI-ELECTRONICS, INC.
1297	0x0511	Brookfield Equinox LLC
1298	0x0512	Soprod SA
1299	0x0513	9974091 Canada Inc.
1300	0x0514	FIBRO GmbH
1301	0x0515	RB Controls Co., Ltd.
1302	0x0516	Footmarks
1303	0x0517	Amtronic Sverige AB (formerly Amcore AB)
1304	0x0518	MAMORIO.inc
1305	0x0519	Tyto Life LLC
1306	0x051A	Leica Camera AG
1307	0x051B	Angee Technologies Ltd.
1308	0x051C	EDPS
1309	0x051D	OFF Line Co., Ltd.
1310	0x051E	Detect Blue Limited
1311	0x051F	Setec Pty Ltd
1312	0x0520	Target Corporation
1313	0x0521	IAI Corporation
1314	0x0522	NS Tech, Inc.
1315	0x0523	MTG Co., Ltd.
1316	0x0524	Hangzhou iMagic Technology Co., Ltd
1317	0x0525	HONGKONG NANO IC TECHNOLOGIES CO., LIMITED
1318	0x0526	Honeywell International Inc.
1319	0x0527	Albrecht JUNG
1320	0x0528	Lunera Lighting Inc.
1321	0x0529	Lumen UAB
1322	0x052A	Keynes Controls Ltd
1323	0x052B	Novartis AG
1324	0x052C	Geosatis SA
1325	0x052D	EXFO, Inc.
1326	0x052E	LEDVANCE GmbH
1327	0x052F	Center ID Corp.
1328	0x0530	Adolene, Inc.
1329	0x0531	D&M Holdings Inc.
1330	0x0532	CRESCO Wireless, Inc.
1331	0x0533	Nura Operations Pty Ltd
1332	0x0534	Frontiergadget, Inc.
1333	0x0535	Smart Component Technologies Limited
1334	0x0536	ZTR Control Systems LLC
1335	0x0537	MetaLogics Corporation
1336	0x0538	Medela AG
1337	0x0539	OPPLE Lighting Co., Ltd
1338	0x053A	Savitech Corp.,
1339	0x053B	prodigy
1340	0x053C	Screenovate Technologies Ltd
1341	0x053D	TESA SA
1342	0x053E	CLIM8 LIMITED
1343	0x053F	Silergy Corp
1344	0x0540	SilverPlus, Inc
1345	0x0541	Sharknet srl
1346	0x0542	Mist Systems, Inc.
1347	0x0543	MIWA LOCK CO.,Ltd
1348	0x0544	OrthoSensor, Inc.
1349	0x0545	Candy Hoover Group s.r.l
1350	0x0546	Apexar Technologies S.A.
1351	0x0547	LOGICDATA d.o.o.
1352	0x0548	Knick Elektronische Messgeraete GmbH & Co. KG
1353	0x0549	Smart Technologies and Investment Limited
1354	0x054A	Linough Inc.
1355	0x054B	Advanced Electronic Designs, Inc.
1356	0x054C	Carefree Scott Fetzer Co Inc
1357	0x054D	Sensome
1358	0x054E	FORTRONIK storitve d.o.o.
1359	0x054F	Sinnoz
1360	0x0550	Versa Networks, Inc.
1361	0x0551	Sylero
1362	0x0552	Avempace SARL
1363	0x0553	Nintendo Co., Ltd.
1364	0x0554	National Instruments
1365	0x0555	KROHNE Messtechnik GmbH
1366	0x0556	Otodynamics Ltd
1367	0x0557	Arwin Technology Limited
1368	0x0558	benegear, inc.
1369	0x0559	Newcon Optik
1370	0x055A	CANDY HOUSE, Inc.
1371	0x055B	FRANKLIN TECHNOLOGY INC
1372	0x055C	Lely
1373	0x055D	Valve Corporation
1374	0x055E	Hekatron Vertriebs GmbH
1375	0x055F	PROTECH S.A.S. DI GIRARDI ANDREA & C.
1376	0x0560	Sarita CareTech APS (formerly Sarita CareTech IVS)
1377	0x0561	Finder S.p.A.
1378	0x0562	Thalmic Labs Inc.
1379	0x0563	Steinel Vertrieb GmbH
1380	0x0564	Beghelli Spa
1381	0x0565	Beijing Smartspace Technologies Inc.
1382	0x0566	CORE TRANSPORT TECHNOLOGIES NZ LIMITED
1383	0x0567	Xiamen Everesports Goods Co., Ltd
1384	0x0568	Bodyport Inc.
1385	0x0569	Audionics System, INC.
1386	0x056A	Flipnavi Co.,Ltd.
1387	0x056B	Rion Co., Ltd.
1388	0x056C	Long Range Systems, LLC
1389	0x056D	Redmond Industrial Group LLC
1390	0x056E	VIZPIN INC.
1391	0x056F	BikeFinder AS
1392	0x0570	Consumer Sleep Solutions LLC
1393	0x0571	PSIKICK, INC.
1394	0x0572	AntTail.com
1395	0x0573	Lighting Science Group Corp.
1396	0x0574	AFFORDABLE ELECTRONICS INC
1397	0x0575	Integral Memroy Plc
1398	0x0576	Globalstar, Inc.
1399	0x0577	True Wearables, Inc.
1400	0x0578	Wellington Drive Technologies Ltd
1401	0x0579	Ensemble Tech Private Limited
1402	0x057A	OMNI Remotes
1403	0x057B	Duracell U.S. Operations Inc.
1404	0x057C	Toor Technologies LLC
1405	0x057D	Instinct Performance
1406	0x057E	Beco, Inc
1407	0x057F	Scuf Gaming International, LLC
1408	0x0580	ARANZ Medical Limited
1409	0x0581	LYS TECHNOLOGIES LTD
1410	0x0582	Breakwall Analytics, LLC
1411	0x0583	Code Blue Communications
1412	0x0584	Gira Giersiepen GmbH & Co. KG
1413	0x0585	Hearing Lab Technology
1414	0x0586	LEGRAND
1415	0x0587	Derichs GmbH
1416	0x0588	ALT-TEKNIK LLC
1417	0x0589	Star Technologies
1418	0x058A	START TODAY CO.,LTD.
1419	0x058B	Maxim Integrated Products
1420	0x058C	MERCK Kommanditgesellschaft auf Aktien
1421	0x058D	Jungheinrich Aktiengesellschaft
1422	0x058E	Oculus VR, LLC
1423	0x058F	HENDON SEMICONDUCTORS PTY LTD
1424	0x0590	Pur3 Ltd
1425	0x0591	Viasat Group S.p.A.
1426	0x0592	IZITHERM
1427	0x0593	Spaulding Clinical Research
1428	0x0594	Kohler Company
1429	0x0595	Inor Process AB
1430	0x0596	My Smart Blinds
1431	0x0597	RadioPulse Inc
1432	0x0598	rapitag GmbH
1433	0x0599	Lazlo326, LLC.
1434	0x059A	Teledyne Lecroy, Inc.
1435	0x059B	Dataflow Systems Limited
1436	0x059C	Macrogiga Electronics
1437	0x059D	Tandem Diabetes Care
1438	0x059E	Polycom, Inc.
1439	0x059F	Fisher & Paykel Healthcare
1440	0x05A0	RCP Software Oy
1441	0x05A1	Shanghai Xiaoyi Technology Co.,Ltd.
1442	0x05A2	ADHERIUM(NZ) LIMITED
1443	0x05A3	Axiomware Systems Incorporated
1444	0x05A4	O. E. M. Controls, Inc.
1445	0x05A5	Kiiroo BV
1446	0x05A6	Telecon Mobile Limited
1447	0x05A7	Sonos Inc
1448	0x05A8	Tom Allebrandi Consulting
1449	0x05A9	Monidor
1450	0x05AA	Tramex Limited
1451	0x05AB	Nofence AS
1452	0x05AC	GoerTek Dynaudio Co., Ltd.
1453	0x05AD	INIA
1454	0x05AE	CARMATE MFG.CO.,LTD
1455	0x05AF	ONvocal
1456	0x05B0	NewTec GmbH
1457	0x05B1	Medallion Instrumentation Systems
1458	0x05B2	CAREL INDUSTRIES S.P.A.
1459	0x05B3	Parabit Systems, Inc.
1460	0x05B4	White Horse Scientific ltd
1461	0x05B5	verisilicon
1462	0x05B6	Elecs Industry Co.,Ltd.
1463	0x05B7	Beijing Pinecone Electronics Co.,Ltd.
1464	0x05B8	Ambystoma Labs Inc.
1465	0x05B9	Suzhou Pairlink Network Technology
1466	0x05BA	igloohome
1467	0x05BB	Oxford Metrics plc
1468	0x05BC	Leviton Mfg. Co., Inc.
1469	0x05BD	ULC Robotics Inc.
1470	0x05BE	RFID Global by Softwork SrL
1471	0x05BF	Real-World-Systems Corporation
1472	0x05C0	Nalu Medical, Inc.
1473	0x05C1	P.I.Engineering
1474	0x05C2	Grote Industries
1475	0x05C3	Runtime, Inc.
1476	0x05C4	Codecoup sp. z o.o. sp. k.
1477	0x05C5	SELVE GmbH & Co. KG
1478	0x05C6	Smart Animal Training Systems, LLC
1479	0x05C7	Lippert Components, INC
1480	0x05C8	SOMFY SAS
1481	0x05C9	TBS Electronics B.V.
1482	0x05CA	MHL Custom Inc
1483	0x05CB	LucentWear LLC
1484	0x05CC	WATTS ELECTRONICS
1485	0x05CD	RJ Brands LLC
1486	0x05CE	V-ZUG Ltd
1487	0x05CF	Biowatch SA
1488	0x05D0	Anova Applied Electronics
1489	0x05D1	Lindab AB
1490	0x05D2	frogblue TECHNOLOGY GmbH
1491	0x05D3	Acurable Limited
1492	0x05D4	LAMPLIGHT Co., Ltd.
1493	0x05D5	TEGAM, Inc.
1494	0x05D6	Zhuhai Jieli technology Co.,Ltd
1495	0x05D7	modum.io AG
1496	0x05D8	Farm Jenny LLC
1497	0x05D9	Toyo Electronics Corporation
1498	0x05DA	Applied Neural Research Corp
1499	0x05DB	Avid Identification Systems, Inc.
1500	0x05DC	Petronics Inc.
1501	0x05DD	essentim GmbH
1502	0x05DE	QT Medical INC.
1503	0x05DF	VIRTUALCLINIC.DIRECT LIMITED
1504	0x05E0	Viper Design LLC
1505	0x05E1	Human, Incorporated
1506	0x05E2	stAPPtronics GmbH
1507	0x05E3	Elemental Machines, Inc.
1508	0x05E4	Taiyo Yuden Co., Ltd
1509	0x05E5	INEO ENERGY& SYSTEMS
1510	0x05E6	Motion Instruments Inc.
1511	0x05E7	PressurePro
1512	0x05E8	COWBOY
1513	0x05E9	iconmobile GmbH
1514	0x05EA	ACS-Control-System GmbH
1515	0x05EB	Bayerische Motoren Werke AG
1516	0x05EC	Gycom Svenska AB
1517	0x05ED	Fuji Xerox Co., Ltd
1518	0x05EE	Glide Inc.
1519	0x05EF	SIKOM AS
1520	0x05F0	beken
1521	0x05F1	The Linux Foundation
1522	0x05F2	Try and E CO.,LTD.
1523	0x05F3	SeeScan
1524	0x05F4	Clearity, LLC
1525	0x05F5	GS TAG
1526	0x05F6	DPTechnics
1527	0x05F7	TRACMO, INC.
1528	0x05F8	Anki Inc.
1529	0x05F9	Hagleitner Hygiene International GmbH
1530	0x05FA	Konami Sports Life Co., Ltd.
1531	0x05FB	Arblet Inc.
1532	0x05FC	Masbando GmbH
1533	0x05FD	Innoseis
1534	0x05FE	Niko
1535	0x05FF	Wellnomics Ltd
1536	0x0600	iRobot Corporation
1537	0x0601	Schrader Electronics
1538	0x0602	Geberit International AG
1539	0x0603	Fourth Evolution Inc
1540	0x0604	Cell2Jack LLC
1541	0x0605	FMW electronic Futterer u. Maier-Wolf OHG
1542	0x0606	John Deere
1543	0x0607	Rookery Technology Ltd
1544	0x0608	KeySafe-Cloud
1545	0x0609	BUCHI Labortechnik AG
1546	0x060A	IQAir AG
1547	0x060B	Triax Technologies Inc
1548	0x060C	Vuzix Corporation
1549	0x060D	TDK Corporation
1550	0x060E	Blueair AB
1551	0x060F	Signify Netherlands
1552	0x0610	ADH GUARDIAN USA LLC
1553	0x0611	Beurer GmbH
1554	0x0612	Playfinity AS
1555	0x0613	Hans Dinslage GmbH
1556	0x0614	OnAsset Intelligence, Inc.
1557	0x0615	INTER ACTION Corporation
1558	0x0616	OS42 UG (haftungsbeschraenkt)
1559	0x0617	WIZCONNECTED COMPANY LIMITED
1560	0x0618	Audio-Technica Corporation
1561	0x0619	Six Guys Labs, s.r.o.
1562	0x061A	R.W. Beckett Corporation
1563	0x061B	silex technology, inc.
1564	0x061C	Univations Limited
1565	0x061D	SENS Innovation ApS
1566	0x061E	Diamond Kinetics, Inc.
1567	0x061F	Phrame Inc.
1568	0x0620	Forciot Oy
1569	0x0621	Noordung d.o.o.
1570	0x0622	Beam Labs, LLC
1571	0x0623	Philadelphia Scientific (U.K.) Limited
1572	0x0624	Biovotion AG
1573	0x0625	Square Panda, Inc.
1574	0x0626	Amplifico
1575	0x0627	WEG S.A.
1576	0x0628	Ensto Oy
1577	0x0629	PHONEPE PVT LTD
1578	0x062A	Lunatico Astronomia SL
1579	0x062B	MinebeaMitsumi Inc.
1580	0x062C	ASPion GmbH
1581	0x062D	Vossloh-Schwabe Deutschland GmbH
1582	0x062E	Procept
1583	0x062F	ONKYO Corporation
1584	0x0630	Asthrea D.O.O.
1585	0x0631	Fortiori Design LLC
1586	0x0632	Hugo Muller GmbH & Co KG
1587	0x0633	Wangi Lai PLT
1588	0x0634	Fanstel Corp
1589	0x0635	Crookwood
1590	0x0636	ELECTRONICA INTEGRAL DE SONIDO S.A.
1591	0x0637	GiP Innovation Tools GmbH
1592	0x0638	LX SOLUTIONS PTY LIMITED
1593	0x0639	Shenzhen Minew Technologies Co., Ltd.
1594	0x063A	Prolojik Limited
1595	0x063B	Kromek Group Plc
1596	0x063C	Contec Medical Systems Co., Ltd.
1597	0x063D	Xradio Technology Co.,Ltd.
1598	0x063E	The Indoor Lab, LLC
1599	0x063F	LDL TECHNOLOGY
1600	0x0640	Parkifi
1601	0x0641	Revenue Collection Systems FRANCE SAS
1602	0x0642	Bluetrum Technology Co.,Ltd
1603	0x0643	makita corporation
1604	0x0644	Apogee Instruments
1605	0x0645	BM3
1606	0x0646	SGV Group Holding GmbH & Co. KG
1607	0x0647	MED-EL
1608	0x0648	Ultune Technologies
1609	0x0649	Ryeex Technology Co.,Ltd.
1610	0x064A	Open Research Institute, Inc.
1611	0x064B	Scale-Tec, Ltd
1612	0x064C	Zumtobel Group AG
1613	0x064D	iLOQ Oy
1614	0x064E	KRUXWorks Technologies Private Limited
1615	0x064F	Digital Matter Pty Ltd
1616	0x0650	Coravin, Inc.
1617	0x0651	Stasis Labs, Inc.
1618	0x0652	ITZ Innovations- und Technologiezentrum GmbH
1619	0x0653	Meggitt SA
1620	0x0654	Ledlenser GmbH & Co. KG
1621	0x0655	Renishaw PLC
1622	0x0656	ZhuHai AdvanPro Technology Company Limited
1623	0x0657	Meshtronix Limited
1624	0x0658	Payex Norge AS
1625	0x0659	UnSeen Technologies Oy
1626	0x065A	Zound Industries International AB
1627	0x065B	Sesam Solutions BV
1628	0x065C	PixArt Imaging Inc.
1629	0x065D	Panduit Corp.
1630	0x065E	Alo AB
1631	0x065F	Ricoh Company Ltd
1632	0x0660	RTC Industries, Inc.
1633	0x0661	Mode Lighting Limited
1634	0x0662	Particle Industries, Inc.
1635	0x0663	Advanced Telemetry Systems, Inc.
1636	0x0664	RHA TECHNOLOGIES LTD
1637	0x0665	Pure International Limited
1638	0x0666	WTO Werkzeug-Einrichtungen GmbH
1639	0x0667	Spark Technology Labs Inc.
1640	0x0668	Bleb Technology srl
1641	0x0669	Livanova USA, Inc.
1642	0x066A	Brady Worldwide Inc.
1643	0x066B	DewertOkin GmbH
1644	0x066C	Ztove ApS
1645	0x066D	Venso EcoSolutions AB
1646	0x066E	Eurotronik Kranj d.o.o.
1647	0x066F	Hug Technology Ltd
1648	0x0670	Gema Switzerland GmbH
1649	0x0671	Buzz Products Ltd.
1650	0x0672	Kopi
1651	0x0673	Innova Ideas Limited
1652	0x0674	BeSpoon
1653	0x0675	Deco Enterprises, Inc.
1654	0x0676	Expai Solutions Private Limited
1655	0x0677	Innovation First, Inc.
1656	0x0678	SABIK Offshore GmbH
1657	0x0679	4iiii Innovations Inc.
1658	0x067A	The Energy Conservatory, Inc.
1659	0x067B	I.FARM, INC.
1660	0x067C	Tile, Inc.
1661	0x067D	Form Athletica Inc.
1662	0x067E	MbientLab Inc
1663	0x067F	NETGRID S.N.C. DI BISSOLI MATTEO, CAMPOREALE SIMONE, TOGNETTI FEDERICO
1664	0x0680	Mannkind Corporation
1665	0x0681	Trade FIDES a.s.
1666	0x0682	Photron Limited
1667	0x0683	Eltako GmbH
1668	0x0684	Dermalapps, LLC
1669	0x0685	Greenwald Industries
1670	0x0686	inQs Co., Ltd.
1671	0x0687	Cherry GmbH
1672	0x0688	Amsted Digital Solutions Inc.
1673	0x0689	Tacx b.v.
1674	0x068A	Raytac Corporation
1675	0x068B	Jiangsu Teranovo Tech Co., Ltd.
1676	0x068C	Changzhou Sound Dragon Electronics and Acoustics Co., Ltd
1677	0x068D	JetBeep Inc.
1678	0x068E	Razer Inc.
1679	0x068F	JRM Group Limited
1680	0x0690	Eccrine Systems, Inc.
1681	0x0691	Curie Point AB
1682	0x0692	Georg Fischer AG
1683	0x0693	Hach - Danaher
1684	0x0694	T&A Laboratories LLC
1685	0x0695	Koki Holdings Co., Ltd.
1686	0x0696	Gunakar Private Limited
1687	0x0697	Stemco Products Inc
1688	0x0698	Wood IT Security, LLC
1689	0x0699	RandomLab SAS
1690	0x069A	Adero, Inc. (formerly as TrackR, Inc.)
1691	0x069B	Dragonchip Limited
1692	0x069C	Noomi AB
1693	0x069D	Vakaros LLC
1694	0x069E	Delta Electronics, Inc.
1695	0x069F	FlowMotion Technologies AS
1696	0x06A0	OBIQ Location Technology Inc.
1697	0x06A1	Cardo Systems, Ltd
1698	0x06A2	Globalworx GmbH
1699	0x06A3	Nymbus, LLC
1700	0x06A4	Sanyo Techno Solutions Tottori Co., Ltd.
1701	0x06A5	TEKZITEL PTY LTD
1702	0x06A6	Roambee Corporation
1703	0x06A7	Chipsea Technologies (ShenZhen) Corp.
1704	0x06A8	GD Midea Air-Conditioning Equipment Co., Ltd.
1705	0x06A9	Soundmax Electronics Limited
1706	0x06AA	Produal Oy
1707	0x06AB	HMS Industrial Networks AB
1708	0x06AC	Ingchips Technology Co., Ltd.
1709	0x06AD	InnovaSea Systems Inc.
1710	0x06AE	SenseQ Inc.
1711	0x06AF	Shoof Technologies
1712	0x06B0	BRK Brands, Inc.
1713	0x06B1	SimpliSafe, Inc.
1714	0x06B2	Tussock Innovation 2013 Limited
1715	0x06B3	The Hablab ApS
1716	0x06B4	Sencilion Oy
1717	0x06B5	Wabilogic Ltd.
1718	0x06B6	Sociometric Solutions, Inc.
1719	0x06B7	iCOGNIZE GmbH
1720	0x06B8	ShadeCraft, Inc
1721	0x06B9	Beflex Inc.
1722	0x06BA	Beaconzone Ltd
1723	0x06BB	Leaftronix Analogic Solutions Private Limited
1724	0x06BC	TWS Srl
1725	0x06BD	ABB Oy
1726	0x06BE	HitSeed Oy
1727	0x06BF	Delcom Products Inc.
1728	0x06C0	CAME S.p.A.
1729	0x06C1	Alarm.com Holdings, Inc
1730	0x06C2	Measurlogic Inc.
1731	0x06C3	King I Electronics.Co.,Ltd
1732	0x06C4	Dream Labs GmbH
1733	0x06C5	Urban Compass, Inc
1734	0x06C6	Simm Tronic Limited
1735	0x06C7	Somatix Inc
1736	0x06C8	Storz & Bickel GmbH & Co. KG
1737	0x06C9	MYLAPS B.V.
1738	0x06CA	Shenzhen Zhongguang Infotech Technology Development Co., Ltd
1739	0x06CB	Dyeware, LLC
1740	0x06CC	Dongguan SmartAction Technology Co.,Ltd.
1741	0x06CD	DIG Corporation
1742	0x06CE	FIOR & GENTZ
1743	0x06CF	Belparts N.V.
1744	0x06D0	Etekcity Corporation
1745	0x06D1	Meyer Sound Laboratories, Incorporated
1746	0x06D2	CeoTronics AG
1747	0x06D3	TriTeq Lock and Security, LLC
1748	0x06D4	DYNAKODE TECHNOLOGY PRIVATE LIMITED
1749	0x06D5	Sensirion AG
1750	0x06D6	JCT Healthcare Pty Ltd
1751	0x06D7	FUBA Automotive Electronics GmbH
1752	0x06D8	AW Company
1753	0x06D9	Shanghai Mountain View Silicon Co.,Ltd.
1754	0x06DA	Zliide Technologies ApS
1755	0x06DB	Automatic Labs, Inc.
1756	0x06DC	Industrial Network Controls, LLC
1757	0x06DD	Intellithings Ltd.
1758	0x06DE	Navcast, Inc.
1759	0x06DF	Hubbell Lighting, Inc.
1760	0x06E0	Avaya
1761	0x06E1	Milestone AV Technologies LLC
1762	0x06E2	Alango Technologies Ltd
1763	0x06E3	Spinlock Ltd
1764	0x06E4	Aluna
1765	0x06E5	OPTEX CO.,LTD.
1766	0x06E6	NIHON DENGYO KOUSAKU
1767	0x06E7	VELUX A/S
1768	0x06E8	Almendo Technologies GmbH
1769	0x06E9	Zmartfun Electronics, Inc.
1770	0x06EA	SafeLine Sweden AB
1771	0x06EB	Houston Radar LLC
1772	0x06EC	Sigur
1773	0x06ED	J Neades Ltd
1774	0x06EE	Avantis Systems Limited
1775	0x06EF	ALCARE Co., Ltd.
1776	0x06F0	Chargy Technologies, SL
1777	0x06F1	Shibutani Co., Ltd.
1778	0x06F2	Trapper Data AB
1779	0x06F3	Alfred International Inc.
1780	0x06F4	Near Field Solutions Ltd
1781	0x06F5	Vigil Technologies Inc.
1782	0x06F6	Vitulo Plus BV
1783	0x06F7	WILKA Schliesstechnik GmbH
1784	0x06F8	BodyPlus Technology Co.,Ltd
1785	0x06F9	happybrush GmbH
1786	0x06FA	Enequi AB
1787	0x06FB	Sartorius AG
1788	0x06FC	Tom Communication Industrial Co.,Ltd.
1789	0x06FD	ESS Embedded System Solutions Inc.
1790	0x06FE	Mahr GmbH
1791	0x06FF	Redpine Signals Inc
1792	0x0700	TraqFreq LLC
1793	0x0701	PAFERS TECH
1794	0x0702	Akciju sabiedriba "SAF TEHNIKA"
1795	0x0703	Beijing Jingdong Century Trading Co., Ltd.
1796	0x0704	JBX Designs Inc.
1797	0x0705	AB Electrolux
1798	0x0706	Wernher von Braun Center for ASdvanced Research
1799	0x0707	Essity Hygiene and Health Aktiebolag
1800	0x0708	Be Interactive Co., Ltd
1801	0x0709	Carewear Corp.
1802	0x070A	Huf Hlsbeck & Frst GmbH & Co. KG
1803	0x070B	Element Products, Inc.
1804	0x070C	Beijing Winner Microelectronics Co.,Ltd
1805	0x070D	SmartSnugg Pty Ltd
1806	0x070E	FiveCo Sarl
1807	0x070F	California Things Inc.
1808	0x0710	Audiodo AB
1809	0x0711	ABAX AS
1810	0x0712	Bull Group Company Limited
1811	0x0713	Respiri Limited
1812	0x0714	MindPeace Safety LLC
1813	0x0715	Vgyan Solutions
1814	0x0716	Altonics
1815	0x0717	iQsquare BV
1816	0x0718	IDIBAIX enginneering
1817	0x0719	ECSG
1818	0x071A	REVSMART WEARABLE HK CO LTD
1819	0x071B	Precor
1820	0x071C	F5 Sports, Inc
1821	0x071D	exoTIC Systems
1822	0x071E	DONGGUAN HELE ELECTRONICS CO., LTD
1823	0x071F	Dongguan Liesheng Electronic Co.Ltd
1824	0x0720	Oculeve, Inc.
1825	0x0721	Clover Network, Inc.
1826	0x0722	Xiamen Eholder Electronics Co.Ltd
1827	0x0723	Ford Motor Company
1828	0x0724	Guangzhou SuperSound Information Technology Co.,Ltd
1829	0x0725	Tedee Sp. z o.o.
1830	0x0726	PHC Corporation
1831	0x0727	STALKIT AS
1832	0x0728	Eli Lilly and Company
1833	0x0729	SwaraLink Technologies
1834	0x072A	JMR embedded systems GmbH
1835	0x072B	Bitkey Inc.
1836	0x072C	GWA Hygiene GmbH
1837	0x072D	Safera Oy
1838	0x072E	Open Platform Systems LLC
1839	0x072F	OnePlus Electronics (Shenzhen) Co., Ltd.
65535	0xFFFF	This value has special meaning depending on the context in which it used. Link Manager Protocol (LMP): This value may be used in the internal and interoperability tests before a Company ID has been assigned. This value shall not be used in shipping end products. Device ID Profile: This value is reserved as the default vendor ID when no Device ID service record is present in a remote device.
"""

MEMBERS = """
64948	0xFDB4	HP Inc	24-Jan-2019
64949	0xFDB5	ECSG	18-Jan-2019
64950	0xFDB6	GWA Hygiene GmbH	18-Jan-2019
64951	0xFDB7	LivaNova USA Inc.	11-Jan-2019
64952	0xFDB8	LivaNova USA Inc.	11-Jan-2019
64953	0xFDB9	Comcast Cable Corporation	11-Jan-2019
64954	0xFDBA	Comcast Cable Corporation	11-Jan-2019
64955	0xFDBB	Profoto	11-Jan-2019
64956	0xFDBC	Emerson	11-Jan-2019
64957	0xFDBD	Clover Network, Inc.	8-Jan-2019
64958	0xFDBE	California Things Inc.	8-Jan-2019
64959	0xFDBF	California Things Inc.	8-Jan-2019
64960	0xFDC0	Hunter Douglas	8-Jan-2019
64961	0xFDC1	Hunter Douglas	8-Jan-2019
64962	0xFDC2	Baidu Online Network Technology (Beijing) Co., Ltd	7-Jan-2019
64963	0xFDC3	Baidu Online Network Technology (Beijing) Co., Ltd	7-Jan-2019
64964	0xFDC4	Simavita (Aust) Pty Ltd	11-Dec-2018
64965	0xFDC5	Automatic Labs	11-Dec-2018
64966	0xFDC6	Eli Lilly and Company	11-Dec-2018
64967	0xFDC7	Eli Lilly and Company	11-Dec-2018
64968	0xFDC8	Hach Danaher	21-Nov-2018
64969	0xFDC9	Busch-Jaeger Elektro GmbH	26-Oct-2018
64970	0xFDCA	Fortin Electronic Systems 	16-Oct-2018
64971	0xFDCB	Meggitt SA	16-Oct-2018
64972	0xFDCC	Shoof Technologies	16-Oct-2018
64973	0xFDCD	Qingping Technology (Beijing) Co., Ltd.	16-Oct-2018
64974	0xFDCE	SENNHEISER electronic GmbH & Co. KG	16-Oct-2018
64975	0xFDCF	Nalu Medical, Inc	18-Sep-2018
64976	0xFDD0	Huawei Technologies Co., Ltd 	6-Sep-2018
64977	0xFDD1	Huawei Technologies Co., Ltd 	6-Sep-2018
64978	0xFDD2	Bose Corporation	6-Sep-2018
64979	0xFDD3	FUBA Automotive Electronics GmbH	23-Aug-2018
64980	0xFDD4	LX Solutions Pty Limited	23-Aug-2018
64981	0xFDD5	Brompton Bicycle Ltd	23-Aug-2018
64982	0xFDD6	Ministry of Supply	14-Aug-2018
64983	0xFDD7	Emerson	9-Aug-2018
64984	0xFDD8	Jiangsu Teranovo Tech Co., Ltd.	9-Aug-2018
64985	0xFDD9	Jiangsu Teranovo Tech Co., Ltd.	9-Aug-2018
64986	0xFDDA	MHCS	23-Jul-2018
64987	0xFDDB	Samsung Electronics Co., Ltd. 	19-Jul-2018
64988	0xFDDC	4iiii Innovations Inc.	11-Jul-2018
64989	0xFDDD	Arch Systems Inc	2-Jul-2018
64990	0xFDDE	Noodle Technology Inc.	27-Jun-2018
64991	0xFDDF	Harman International	11-Jun-2018
64992	0xFDE0	John Deere	23-May-2018
64993	0xFDE1	Fortin Electronic Systems 	15-May-2018
64994	0xFDE2	Google Inc.	14-May-2018
64995	0xFDE3	Abbott Diabetes Care	9-May-2018
64996	0xFDE4	JUUL Labs, Inc.	8-May-2018
64997	0xFDE5	SMK Corporation 	27-Apr-2018
64998	0xFDE6	Intelletto Technologies Inc	6-Apr-2018
64999	0xFDE7	SECOM Co., LTD	3-Apr-2018
65000	0xFDE8	Robert Bosch GmbH	27-Mar-2018
65001	0xFDE9	Spacesaver Corporation	22-Mar-2018
65002	0xFDEA	SeeScan, Inc	22-Mar-2018
65003	0xFDEB	Syntronix Corporation	21-Mar-2018
65004	0xFDEC	Mannkind Corporation	20-Mar-2018
65005	0xFDED	Pole Star	19-Mar-2018
65006	0xFDEE	Huawei Technologies Co., Ltd.	15-Mar-2018
65007	0xFDEF	ART AND PROGRAM, INC.	15-Mar-2018
65008	0xFDF0	Google Inc.	20-Feb-2018
65009	0xFDF1	LAMPLIGHT Co.,Ltd	7-Feb-2018
65010	0xFDF2	AMICCOM Electronics Corporation	31-Jan-2018
65011	0xFDF3	Amersports	4-Feb-2018
65012	0xFDF4	O. E. M. Controls, Inc.	
65013	0xFDF5	Milwaukee Electric Tools	11-Jan-2018
65014	0xFDF6	AIAIAI ApS	11-Jan-2018
65015	0xFDF7	HP Inc.	3-Jan-2018
65016	0xFDF8	Onvocal	28-Dec-2017
65017	0xFDF9	INIA	27-Dec-2017
65018	0xFDFA	Tandem Diabetes Care	22-Dec-2017
65019	0xFDFB	Tandem Diabetes Care	22-Dec-2017
65020	0xFDFC	Optrel AG	19-Dec-2017
65021	0xFDFD	RecursiveSoft Inc.	19-Dec-2017
65022	0xFDFE	ADHERIUM(NZ) LIMITED	6-Dec-2017
65023	0xFDFF	OSRAM GmbH	4-Dec-2017
65024	0xFE00	Amazon.com Services, Inc.	22-Nov-2017
65025	0xFE01	Duracell U.S. Operations Inc.	14-Nov-2017
65026	0xFE02	Robert Bosch GmbH	31-Oct-2017
65027	0xFE03	Amazon.com Services, Inc.	23-Oct-2017
65028	0xFE04	OpenPath Security Inc	20-Oct-2017
65029	0xFE05	CORE Transport Technologies NZ Limited	11-Oct-2017
65030	0xFE06	Qualcomm Technologies, Inc.	9-Oct-2017
65031	0xFE07	Sonos, Inc.	3-Oct-2017
65032	0xFE08	Microsoft	26-Sep-2017
65033	0xFE09	Pillsy, Inc.	21-Sep-2017
65034	0xFE0A	ruwido austria gmbh	19-Sep-2017
65035	0xFE0B	ruwido austria gmbh	19-Sep-2017
65036	0xFE0C	Procter & Gamble	31-Aug-2017
65037	0xFE0D	Procter & Gamble	31-Aug-2017
65038	0xFE0E	Setec Pty Ltd	23-Aug-2017
65039	0xFE0F	Philips Lighting B.V.	17-Aug-2017
65040	0xFE10	Lapis Semiconductor Co., Ltd.	3-Aug-2017
65041	0xFE11	GMC-I Messtechnik GmbH	31-Jul-2017
65042	0xFE12	M-Way Solutions GmbH	27-Jul-2017
65043	0xFE13	Apple Inc.	27-Jul-2017
65044	0xFE14	Flextronics International USA Inc.	20-Jul-2017
65045	0xFE15	Amazon.com Services, Inc..	18-Jul-2017
65046	0xFE16	Footmarks, Inc.	5-Jul-2017
65047	0xFE17	Telit Wireless Solutions GmbH	5-Jul-2017
65048	0xFE18	Runtime, Inc.	5-Jul-2017
65049	0xFE19	Google, Inc	5-Jul-2017
65050	0xFE1A	Tyto Life LLC	5-Jul-2017
65051	0xFE1B	Tyto Life LLC	5-Jul-2017
65052	0xFE1C	NetMedia, Inc.	20-Jun-2017
65053	0xFE1D	Illuminati Instrument Corporation	16-Jun-2017
65054	0xFE1E	Smart Innovations Co., Ltd	13-Jun-2017
65055	0xFE1F	Garmin International, Inc.	30-May-2017
65056	0xFE20	Emerson	24-May-2017
65057	0xFE21	Bose Corporation	22-May-2017
65058	0xFE22	Zoll Medical Corporation	2-May-2017
65059	0xFE23	Zoll Medical Corporation	2-May-2017
65060	0xFE24	August Home Inc	17-Apr-2017
65061	0xFE25	Apple, Inc. 	6-Apr-2017
65062	0xFE26	Google	6-Apr-2017
65063	0xFE27	Google	31-Mar-2017
65064	0xFE28	Ayla Networks	28-Mar-2017
65065	0xFE29	Gibson Innovations	13-Mar-2017
65066	0xFE2A	DaisyWorks, Inc.	6-Mar-2017
65067	0xFE2B	ITT Industries	24-Feb-2017
65068	0xFE2C	Google	22-Feb-2017
65069	0xFE2D	SMART INNOVATION Co.,Ltd	13-Feb-2017
65070	0xFE2E	ERi,Inc.	13-Feb-2017
65071	0xFE2F	CRESCO Wireless, Inc	26-Jan-2017
65072	0xFE30	Volkswagen AG	24-Jan-2017
65073	0xFE31	Volkswagen AG	24-Jan-2017
65074	0xFE32	Pro-Mark, Inc.	24-Jan-2017
65075	0xFE33	CHIPOLO d.o.o.	16-Jan-2017
65076	0xFE34	SmallLoop LLC	9-Jan-2017
65077	0xFE35	HUAWEI Technologies Co., Ltd	5-Jan-2017
65078	0xFE36	HUAWEI Technologies Co., Ltd	5-Jan-2017
65079	0xFE37	Spaceek LTD	27-Dec-2016
65080	0xFE38	Spaceek LTD	27-Dec-2016
65081	0xFE39	TTS Tooltechnic Systems AG & Co. KG	22-Dec-2016
65082	0xFE3A	TTS Tooltechnic Systems AG & Co. KG	22-Dec-2016
65083	0xFE3B	Dobly Laboratories	9-Dec-2016
65084	0xFE3C	alibaba	1-Dec-2016
65085	0xFE3D	BD Medical	16-Nov-2016
65086	0xFE3E	BD Medical	16-Nov-2016
65087	0xFE3F	Friday Labs Limited	10-Nov-2016
65088	0xFE40	Inugo Systems Limited	28-Oct-2016
65089	0xFE41	Inugo Systems Limited	28-Oct-2016
65090	0xFE42	Nets A/S	25-Oct-2016
65091	0xFE43	Andreas Stihl AG & Co. KG	25-Oct-2016
65092	0xFE44	SK Telecom	17-Oct-2016
65093	0xFE45	Snapchat Inc	4-Oct-2016
65094	0xFE46	B&O Play A/S	29-Sep-2016
65095	0xFE47	General Motors	16-Sep-2016
65096	0xFE48	General Motors	16-Sep-2016
65097	0xFE49	SenionLab AB	16-Sep-2016
65098	0xFE4A	OMRON HEALTHCARE Co., Ltd.	2-Sep-2016
65099	0xFE4B	Philips Lighting B.V.	22-Aug-2016
65100	0xFE4C	Volkswagen AG	19-Aug-2016
65101	0xFE4D	Casambi Technologies Oy	5-Aug-2016
65102	0xFE4E	NTT docomo	5-Aug-2016
65103	0xFE4F	Molekule, Inc.	5-Aug-2016
65104	0xFE50	Google Inc.	5-Aug-2016
65105	0xFE51	SRAM	3-Aug-2016
65106	0xFE52	SetPoint Medical	3-Aug-2016
65107	0xFE53	3M	15-Jul-2016
65108	0xFE54	Motiv, Inc.	7-Jul-2016
65109	0xFE55	Google Inc.	5-Jul-2016
65110	0xFE56	Google Inc.	24-Jun-2016
65111	0xFE57	Dotted Labs	20-Jun-2016
65112	0xFE58	Nordic Semiconductor ASA	7-Jun-2016
65113	0xFE59	Nordic Semiconductor ASA	7-Jun-2016
65114	0xFE5A	Cronologics Corporation	26-May-2016
65115	0xFE5B	GT-tronics HK Ltd	11-May-2016
65116	0xFE5C	million hunters GmbH	27-Apr-2016
65117	0xFE5D	Grundfos A/S	20-Apr-2016
65118	0xFE5E	Plastc Corporation	19-Apr-2016
65119	0xFE5F	Eyefi, Inc.	19-Apr-2016
65120	0xFE60	Lierda Science & Technology Group Co., Ltd.	8-Apr-2016
65121	0xFE61	Logitech International SA	8-Apr-2016
65122	0xFE62	Indagem Tech LLC	5-Apr-2016
65123	0xFE63	Connected Yard, Inc.	5-Apr-2016
65124	0xFE64	Siemens AG	24-Mar-2016
65125	0xFE65	CHIPOLO d.o.o.	24-Mar-2016
65126	0xFE66	Intel Corporation	7-Mar-2016
65127	0xFE67	Lab Sensor Solutions	7-Mar-2016
65128	0xFE68	Qualcomm Life Inc	29-Feb-2016
65129	0xFE69	Qualcomm Life Inc	29-Feb-2016
65130	0xFE6A	Kontakt Micro-Location Sp. z o.o.	23-Feb-2016
65131	0xFE6B	TASER International, Inc.	19-Feb-2016
65132	0xFE6C	TASER International, Inc.	19-Feb-2016
65133	0xFE6D	The University of Tokyo	11-Feb-2016
65134	0xFE6E	The University of Tokyo	11-Feb-2016
65135	0xFE6F	LINE Corporation	9-Feb-2016
65136	0xFE70	Beijing Jingdong Century Trading Co., Ltd.	9-Feb-2016
65137	0xFE71	Plume Design Inc	25-Jan-2016
65138	0xFE72	St. Jude Medical, Inc.	25-Jan-2016
65139	0xFE73	St. Jude Medical, Inc.	25-Jan-2016
65140	0xFE74	unwire	15-Jan-2016
65141	0xFE75	TangoMe	15-Jan-2016
65142	0xFE76	TangoMe	15-Jan-2016
65143	0xFE77	Hewlett-Packard Company	7-Jan-2016
65144	0xFE78	Hewlett-Packard Company	7-Jan-2016
65145	0xFE79	Zebra Technologies	22-Dec-2015
65146	0xFE7A	Bragi GmbH	21-Dec-2015
65147	0xFE7B	Orion Labs, Inc.	11-Dec-2015
65148	0xFE7C	Telit Wireless Solutions (Formerly Stollmann E+V GmbH)	7-Dec-2015
65149	0xFE7D	Aterica Health Inc.	3-Nov-2015
65150	0xFE7E	Awear Solutions Ltd	2-Nov-2015
65151	0xFE7F	Doppler Lab	28-Oct-2015
65152	0xFE80	Doppler Lab	28-Oct-2015
65153	0xFE81	Medtronic Inc.	22-Oct-2015
65154	0xFE82	Medtronic Inc.	22-Oct-2015
65155	0xFE83	Blue Bite	25-Sep-2015
65156	0xFE84	RF Digital Corp	21-Sep-2015
65157	0xFE85	RF Digital Corp	21-Sep-2015
65158	0xFE86	HUAWEI Technologies Co., Ltd. ( )	16-Sep-2015
65159	0xFE87	Qingdao Yeelink Information Technology Co., Ltd. ( )	8-Sep-2015
65160	0xFE88	SALTO SYSTEMS S.L.	31-Aug-2015
65161	0xFE89	B&O Play A/S	17-Aug-2015
65162	0xFE8A	Apple, Inc.	31-Jul-2015
65163	0xFE8B	Apple, Inc.	31-Jul-2015
65164	0xFE8C	TRON Forum	31-Jul-2015
65165	0xFE8D	Interaxon Inc.	29-Jul-2015
65166	0xFE8E	ARM Ltd	15-Jun-2015
65167	0xFE8F	CSR	15-Jun-2015
65168	0xFE90	JUMA	13-Jun-2015
65169	0xFE91	Shanghai Imilab Technology Co.,Ltd	23-Jun-2015
65170	0xFE92	Jarden Safety & Security	19-Jun-2015
65171	0xFE93	OttoQ In	18-Jun-2015
65172	0xFE94	OttoQ In	18-Jun-2015
65173	0xFE95	Xiaomi Inc.	15-Jun-2015
65174	0xFE96	Tesla Motors Inc.	12-Jun-2015
65175	0xFE97	Tesla Motors Inc.	12-Jun-2015
65176	0xFE98	Currant Inc	8-Jun-2015
65177	0xFE99	Currant Inc	8-Jun-2015
65178	0xFE9A	Estimote	3-Jun-2015
65179	0xFE9B	Samsara Networks, Inc	27-May-2015
65180	0xFE9C	GSI Laboratories, Inc.	20-May-2015
65181	0xFE9D	Mobiquity Networks Inc	19-May-2015
65182	0xFE9E	Dialog Semiconductor B.V.	13-May-2015
65183	0xFE9F	Google	12-May-2015
65184	0xFEA0	Google	12-May-2015
65185	0xFEA1	Intrepid Control Systems, Inc.	12-May-2015
65186	0xFEA2	Intrepid Control Systems, Inc.	12-May-2015
65187	0xFEA3	ITT Industries	20-Apr-2015
65188	0xFEA4	Paxton Access Ltd	9-Apr-2015
65189	0xFEA5	GoPro, Inc.	19-Mar-2015
65190	0xFEA6	GoPro, Inc.	19-Mar-2015
65191	0xFEA7	UTC Fire and Security	16-Mar-2015
65192	0xFEA8	Savant Systems LLC	16-Mar-2015
65193	0xFEA9	Savant Systems LLC	16-Mar-2015
65194	0xFEAA	Google	12-Mar-2015
65195	0xFEAB	Nokia	12-Feb-2015
65196	0xFEAC	Nokia	12-Feb-2015
65197	0xFEAD	Nokia	12-Feb-2015
65198	0xFEAE	Nokia	12-Feb-2015
65199	0xFEAF	Nest Labs Inc	10-Feb-2015
65200	0xFEB0	Nest Labs Inc	10-Feb-2015
65201	0xFEB1	Electronics Tomorrow Limited	30-Jan-2015
65202	0xFEB2	Microsoft Corporation	27-Jan-2015
65203	0xFEB3	Taobao	13-Jan-2015
65204	0xFEB4	WiSilica Inc.	2-Jan-2015
65205	0xFEB5	WiSilica Inc.	2-Jan-2015
65206	0xFEB6	Vencer Co., Ltd	12-Dec-2014
65207	0xFEB7	Facebook, Inc.	6-Dec-2014
65208	0xFEB8	Facebook, Inc.	6-Dec-2014
65209	0xFEB9	LG Electronics	4-Dec-2014
65210	0xFEBA	Tencent Holdings Limited	4-Dec-2014
65211	0xFEBB	adafruit industries	30-Oct-2014
65212	0xFEBC	Dexcom Inc	23-Oct-2014
65213	0xFEBD	Clover Network, Inc	12-Oct-2014
65214	0xFEBE	Bose Corporation	6-Oct-2014
65215	0xFEBF	Nod, Inc.	23-Sep-2014
65216	0xFEC0	KDDI Corporation	23-Sep-2014
65217	0xFEC1	KDDI Corporation	23-Sep-2014
65218	0xFEC2	Blue Spark Technologies, Inc.	16-Sep-2014
65219	0xFEC3	360fly, Inc.	16-Sep-2014
65220	0xFEC4	PLUS Location Systems	10-Sep-2014
65221	0xFEC5	Realtek Semiconductor Corp.	10-Sep-2014
65222	0xFEC6	Kocomojo, LLC	8-Aug-2014
65223	0xFEC7	Apple, Inc.	4-Aug-2014
65224	0xFEC8	Apple, Inc.	4-Aug-2014
65225	0xFEC9	Apple, Inc.	4-Aug-2014
65226	0xFECA	Apple, Inc.	4-Aug-2014
65227	0xFECB	Apple, Inc.	4-Aug-2014
65228	0xFECC	Apple, Inc.	4-Aug-2014
65229	0xFECD	Apple, Inc.	4-Aug-2014
65230	0xFECE	Apple, Inc.	4-Aug-2014
65231	0xFECF	Apple, Inc.	4-Aug-2014
65232	0xFED0	Apple, Inc.	4-Aug-2014
65233	0xFED1	Apple, Inc.	4-Aug-2014
65234	0xFED2	Apple, Inc.	4-Aug-2014
65235	0xFED3	Apple, Inc.	4-Aug-2014
65236	0xFED4	Apple, Inc.	4-Aug-2014
65237	0xFED5	Plantronics Inc.	1-Aug-2014
65238	0xFED6	Broadcom	1-Aug-2014
65239	0xFED7	Broadcom	1-Aug-2014
65240	0xFED8	Google	22-Jul-2014
65241	0xFED9	Pebble Technology Corporation	16-Jul-2014
65242	0xFEDA	ISSC Technologies Corp. 	14-Jul-2014
65243	0xFEDB	Perka, Inc.	1-Jul-2014
65244	0xFEDC	Jawbone	26-Jun-2014
65245	0xFEDD	Jawbone	26-Jun-2014
65246	0xFEDE	Coin, Inc.	24-Jun-2014
65247	0xFEDF	Design SHIFT	23-Jun-2014
65248	0xFEE0	Anhui Huami Information Technology Co., Ltd. 	9-Jun-2014
65249	0xFEE1	Anhui Huami Information Technology Co., Ltd. 	9-Jun-2014
65250	0xFEE2	Anki, Inc.	8-May-2014
65251	0xFEE3	Anki, Inc.	8-May-2014
65252	0xFEE4	Nordic Semiconductor ASA	5-May-2014
65253	0xFEE5	Nordic Semiconductor ASA	5-May-2014
65254	0xFEE6	Silvair, Inc.	25-Apr-2014
65255	0xFEE7	Tencent Holdings Limited.	24-Apr-2014
65256	0xFEE8	Quintic Corp.	24-Apr-2014
65257	0xFEE9	Quintic Corp.	24-Apr-2014
65258	0xFEEA	Swirl Networks, Inc.	8-Apr-2014
65259	0xFEEB	Swirl Networks, Inc.	8-Apr-2014
65260	0xFEEC	Tile, Inc.	27-Mar-2014
65261	0xFEED	Tile, Inc.	17-Mar-2014
65262	0xFEEE	Polar Electro Oy 	6-Mar-2014
65263	0xFEEF	Polar Electro Oy 	6-Mar-2014
65264	0xFEF0	Intel	6-Mar-2014
65265	0xFEF1	CSR	13-Feb-2014
65266	0xFEF2	CSR	13-Feb-2014
65267	0xFEF3	Google	13-Feb-2014
65268	0xFEF4	Google	13-Feb-2014
65269	0xFEF5	Dialog Semiconductor GmbH	13-Feb-2014
65270	0xFEF6	Wicentric, Inc.	13-Feb-2014
65271	0xFEF7	Aplix Corporation	13-Feb-2014
65272	0xFEF8	Aplix Corporation	13-Feb-2014
65273	0xFEF9	PayPal, Inc.	13-Jan-2014
65274	0xFEFA	PayPal, Inc.	13-Jan-2014
65275	0xFEFB	Telit Wireless Solutions (Formerly Stollmann E+V GmbH)	6-Jan-2013
65276	0xFEFC	Gimbal, Inc.	20-Dec-2013
65277	0xFEFD	Gimbal, Inc.	20-Dec-2013
65278	0xFEFE	GN ReSound A/S	17-Dec-2013
65279	0xFEFF	GN Netcom	12-Dec-2013
"""

uuid16_dict = {
    0x0001: "SDP",
    0x0003: "RFCOMM",
    0x0005: "TCS-BIN",
    0x0007: "ATT",
    0x0008: "OBEX",
    0x000f: "BNEP",
    0x0010: "UPNP",
    0x0011: "HIDP",
    0x0012: "Hardcopy Control Channel",
    0x0014: "Hardcopy Data Channel",
    0x0016: "Hardcopy Notification",
    0x0017: "AVCTP",
    0x0019: "AVDTP",
    0x001b: "CMTP",
    0x001e: "MCAP Control Channel",
    0x001f: "MCAP Data Channel",
    0x0100: "L2CAP",
    # 0x0101 to 0x0fff undefined */
    0x1000: "Service Discovery Server Service Class",
    0x1001: "Browse Group Descriptor Service Class",
    0x1002: "Public Browse Root",
    # 0x1003 to 0x1100 undefined */
    0x1101: "Serial Port",
    0x1102: "LAN Access Using PPP",
    0x1103: "Dialup Networking",
    0x1104: "IrMC Sync",
    0x1105: "OBEX Object Push",
    0x1106: "OBEX File Transfer",
    0x1107: "IrMC Sync Command",
    0x1108: "Headset",
    0x1109: "Cordless Telephony",
    0x110a: "Audio Source",
    0x110b: "Audio Sink",
    0x110c: "A/V Remote Control Target",
    0x110d: "Advanced Audio Distribution",
    0x110e: "A/V Remote Control",
    0x110f: "A/V Remote Control Controller",
    0x1110: "Intercom",
    0x1111: "Fax",
    0x1112: "Headset AG",
    0x1113: "WAP",
    0x1114: "WAP Client",
    0x1115: "PANU",
    0x1116: "NAP",
    0x1117: "GN",
    0x1118: "Direct Printing",
    0x1119: "Reference Printing",
    0x111a: "Basic Imaging Profile",
    0x111b: "Imaging Responder",
    0x111c: "Imaging Automatic Archive",
    0x111d: "Imaging Referenced Objects",
    0x111e: "Handsfree",
    0x111f: "Handsfree Audio Gateway",
    0x1120: "Direct Printing Refrence Objects Service",
    0x1121: "Reflected UI",
    0x1122: "Basic Printing",
    0x1123: "Printing Status",
    0x1124: "Human Interface Device Service",
    0x1125: "Hardcopy Cable Replacement",
    0x1126: "HCR Print",
    0x1127: "HCR Scan",
    0x1128: "Common ISDN Access",
    # 0x1129 and 0x112a undefined */
    0x112d: "SIM Access",
    0x112e: "Phonebook Access Client",
    0x112f: "Phonebook Access Server",
    0x1130: "Phonebook Access",
    0x1131: "Headset HS",
    0x1132: "Message Access Server",
    0x1133: "Message Notification Server",
    0x1134: "Message Access Profile",
    0x1135: "GNSS",
    0x1136: "GNSS Server",
    0x1137: "3D Display",
    0x1138: "3D Glasses",
    0x1139: "3D Synchronization",
    0x113a: "MPS Profile",
    0x113b: "MPS Service",
    # 0x113c to 0x11ff undefined */
    0x1200: "PnP Information",
    0x1201: "Generic Networking",
    0x1202: "Generic File Transfer",
    0x1203: "Generic Audio",
    0x1204: "Generic Telephony",
    0x1205: "UPNP Service",
    0x1206: "UPNP IP Service",
    0x1300: "UPNP IP PAN",
    0x1301: "UPNP IP LAP",
    0x1302: "UPNP IP L2CAP",
    0x1303: "Video Source",
    0x1304: "Video Sink",
    0x1305: "Video Distribution",
    # 0x1306 to 0x13ff undefined */
    0x1400: "HDP",
    0x1401: "HDP Source",
    0x1402: "HDP Sink",
    # 0x1403 to 0x17ff undefined */
    0x1800: "Generic Access Profile",
    0x1801: "Generic Attribute Profile",
    0x1802: "Immediate Alert",
    0x1803: "Link Loss",
    0x1804: "Tx Power",
    0x1805: "Current Time Service",
    0x1806: "Reference Time Update Service",
    0x1807: "Next DST Change Service",
    0x1808: "Glucose",
    0x1809: "Health Thermometer",
    0x180a: "Device Information",
    # 0x180b and 0x180c undefined */
    0x180d: "Heart Rate",
    0x180e: "Phone Alert Status Service",
    0x180f: "Battery Service",
    0x1810: "Blood Pressure",
    0x1811: "Alert Notification Service",
    0x1812: "Human Interface Device",
    0x1813: "Scan Parameters",
    0x1814: "Running Speed and Cadence",
    0x1815: "Automation IO",
    0x1816: "Cycling Speed and Cadence",
    # 0x1817 undefined */
    0x1818: "Cycling Power",
    0x1819: "Location and Navigation",
    0x181a: "Environmental Sensing",
    0x181b: "Body Composition",
    0x181c: "User Data",
    0x181d: "Weight Scale",
    0x181e: "Bond Management",
    0x181f: "Continuous Glucose Monitoring",
    0x1820: "Internet Protocol Support",
    0x1821: "Indoor Positioning",
    0x1822: "Pulse Oximeter",
    0x1823: "HTTP Proxy",
    0x1824: "Transport Discovery",
    0x1825: "Object Transfer",
    0x1826: "Fitness Machine",
    0x1827: "Mesh Provisioning",
    0x1828: "Mesh Proxy",
    # 0x1829 to 0x27ff undefined */
    0x2800: "Primary Service",
    0x2801: "Secondary Service",
    0x2802: "Include",
    0x2803: "Characteristic",
    # 0x2804 to 0x28ff undefined */
    0x2900: "Characteristic Extended Properties",
    0x2901: "Characteristic User Description",
    0x2902: "Client Characteristic Configuration",
    0x2903: "Server Characteristic Configuration",
    0x2904: "Characteristic Format",
    0x2905: "Characteristic Aggregate Formate",
    0x2906: "Valid Range",
    0x2907: "External Report Reference",
    0x2908: "Report Reference",
    0x2909: "Number of Digitals",
    0x290a: "Value Trigger Setting",
    0x290b: "Environmental Sensing Configuration",
    0x290c: "Environmental Sensing Measurement",
    0x290d: "Environmental Sensing Trigger Setting",
    0x290e: "Time Trigger Setting",
    # 0x290f to 0x29ff undefined */
    0x2a00: "Device Name",
    0x2a01: "Appearance",
    0x2a02: "Peripheral Privacy Flag",
    0x2a03: "Reconnection Address",
    0x2a04: "Peripheral Preferred Connection Parameters",
    0x2a05: "Service Changed",
    0x2a06: "Alert Level",
    0x2a07: "Tx Power Level",
    0x2a08: "Date Time",
    0x2a09: "Day of Week",
    0x2a0a: "Day Date Time",
    # 0x2a0b undefined */
    0x2a0c: "Exact Time 256",
    0x2a0d: "DST Offset",
    0x2a0e: "Time Zone",
    0x2a0f: "Local Time Information",
    # 0x2a10 undefined */
    0x2a11: "Time with DST",
    0x2a12: "Time Accuracy",
    0x2a13: "Time Source",
    0x2a14: "Reference Time Information",
    # 0x2a15 undefined */
    0x2a16: "Time Update Control Point",
    0x2a17: "Time Update State",
    0x2a18: "Glucose Measurement",
    0x2a19: "Battery Level",
    # 0x2a1a and 0x2a1b undefined */
    0x2a1c: "Temperature Measurement",
    0x2a1d: "Temperature Type",
    0x2a1e: "Intermediate Temperature",
    # 0x2a1f and 0x2a20 undefined */
    0x2a21: "Measurement Interval",
    0x2a22: "Boot Keyboard Input Report",
    0x2a23: "System ID",
    0x2a24: "Model Number String",
    0x2a25: "Serial Number String",
    0x2a26: "Firmware Revision String",
    0x2a27: "Hardware Revision String",
    0x2a28: "Software Revision String",
    0x2a29: "Manufacturer Name String",
    0x2a2a: "IEEE 11073-20601 Regulatory Cert. Data List",
    0x2a2b: "Current Time",
    0x2a2c: "Magnetic Declination",
    # 0x2a2d to 0x2a30 undefined */
    0x2a31: "Scan Refresh",
    0x2a32: "Boot Keyboard Output Report",
    0x2a33: "Boot Mouse Input Report",
    0x2a34: "Glucose Measurement Context",
    0x2a35: "Blood Pressure Measurement",
    0x2a36: "Intermediate Cuff Pressure",
    0x2a37: "Heart Rate Measurement",
    0x2a38: "Body Sensor Location",
    0x2a39: "Heart Rate Control Point",
    # 0x2a3a to 0x2a3e undefined */
    0x2a3f: "Alert Status",
    0x2a40: "Ringer Control Point",
    0x2a41: "Ringer Setting",
    0x2a42: "Alert Category ID Bit Mask",
    0x2a43: "Alert Category ID",
    0x2a44: "Alert Notification Control Point",
    0x2a45: "Unread Alert Status",
    0x2a46: "New Alert",
    0x2a47: "Supported New Alert Category",
    0x2a48: "Supported Unread Alert Category",
    0x2a49: "Blood Pressure Feature",
    0x2a4a: "HID Information",
    0x2a4b: "Report Map",
    0x2a4c: "HID Control Point",
    0x2a4d: "Report",
    0x2a4e: "Protocol Mode",
    0x2a4f: "Scan Interval Window",
    0x2a50: "PnP ID",
    0x2a51: "Glucose Feature",
    0x2a52: "Record Access Control Point",
    0x2a53: "RSC Measurement",
    0x2a54: "RSC Feature",
    0x2a55: "SC Control Point",
    0x2a56: "Digital",
    # 0x2a57 undefined */
    0x2a58: "Analog",
    # 0x2a59 undefined */
    0x2a5a: "Aggregate",
    0x2a5b: "CSC Measurement",
    0x2a5c: "CSC Feature",
    0x2a5d: "Sensor Location",
    # 0x2a5e to 0x2a62 undefined */
    0x2a63: "Cycling Power Measurement",
    0x2a64: "Cycling Power Vector",
    0x2a65: "Cycling Power Feature",
    0x2a66: "Cycling Power Control Point",
    0x2a67: "Location and Speed",
    0x2a68: "Navigation",
    0x2a69: "Position Quality",
    0x2a6a: "LN Feature",
    0x2a6b: "LN Control Point",
    0x2a6c: "Elevation",
    0x2a6d: "Pressure",
    0x2a6e: "Temperature",
    0x2a6f: "Humidity",
    0x2a70: "True Wind Speed",
    0x2a71: "True Wind Direction",
    0x2a72: "Apparent Wind Speed",
    0x2a73: "Apparent Wind Direction",
    0x2a74: "Gust Factor",
    0x2a75: "Pollen Concentration",
    0x2a76: "UV Index",
    0x2a77: "Irradiance",
    0x2a78: "Rainfall",
    0x2a79: "Wind Chill",
    0x2a7a: "Heat Index",
    0x2a7b: "Dew Point",
    0x2a7c: "Trend",
    0x2a7d: "Descriptor Value Changed",
    0x2a7e: "Aerobic Heart Rate Lower Limit",
    0x2a7f: "Aerobic Threshold",
    0x2a80: "Age",
    0x2a81: "Anaerobic Heart Rate Lower Limit",
    0x2a82: "Anaerobic Heart Rate Upper Limit",
    0x2a83: "Anaerobic Threshold",
    0x2a84: "Aerobic Heart Rate Upper Limit",
    0x2a85: "Date of Birth",
    0x2a86: "Date of Threshold Assessment",
    0x2a87: "Email Address",
    0x2a88: "Fat Burn Heart Rate Lower Limit",
    0x2a89: "Fat Burn Heart Rate Upper Limit",
    0x2a8a: "First Name",
    0x2a8b: "Five Zone Heart Rate Limits",
    0x2a8c: "Gender",
    0x2a8d: "Heart Rate Max",
    0x2a8e: "Height",
    0x2a8f: "Hip Circumference",
    0x2a90: "Last Name",
    0x2a91: "Maximum Recommended Heart Rate",
    0x2a92: "Resting Heart Rate",
    0x2a93: "Sport Type for Aerobic/Anaerobic Thresholds",
    0x2a94: "Three Zone Heart Rate Limits",
    0x2a95: "Two Zone Heart Rate Limit",
    0x2a96: "VO2 Max",
    0x2a97: "Waist Circumference",
    0x2a98: "Weight",
    0x2a99: "Database Change Increment",
    0x2a9a: "User Index",
    0x2a9b: "Body Composition Feature",
    0x2a9c: "Body Composition Measurement",
    0x2a9d: "Weight Measurement",
    0x2a9e: "Weight Scale Feature",
    0x2a9f: "User Control Point",
    0x2aa0: "Magnetic Flux Density - 2D",
    0x2aa1: "Magnetic Flux Density - 3D",
    0x2aa2: "Language",
    0x2aa3: "Barometric Pressure Trend",
    0x2aa4: "Bond Management Control Point",
    0x2aa5: "Bond Management Feature",
    0x2aa6: "Central Address Resolution",
    0x2aa7: "CGM Measurement",
    0x2aa8: "CGM Feature",
    0x2aa9: "CGM Status",
    0x2aaa: "CGM Session Start Time",
    0x2aab: "CGM Session Run Time",
    0x2aac: "CGM Specific Ops Control Point",
    0x2aad: "Indoor Positioning Configuration",
    0x2aae: "Latitude",
    0x2aaf: "Longitude",
    0x2ab0: "Local North Coordinate",
    0x2ab1: "Local East Coordinate",
    0x2ab2: "Floor Number",
    0x2ab3: "Altitude",
    0x2ab4: "Uncertainty",
    0x2ab5: "Location Name",
    0x2ab6: "URI",
    0x2ab7: "HTTP Headers",
    0x2ab8: "HTTP Status Code",
    0x2ab9: "HTTP Entity Body",
    0x2aba: "HTTP Control Point",
    0x2abb: "HTTPS Security",
    0x2abc: "TDS Control Point",
    0x2abd: "OTS Feature",
    0x2abe: "Object Name",
    0x2abf: "Object Type",
    0x2ac0: "Object Size",
    0x2ac1: "Object First-Created",
    0x2ac2: "Object Last-Modified",
    0x2ac3: "Object ID",
    0x2ac4: "Object Properties",
    0x2ac5: "Object Action Control Point",
    0x2ac6: "Object List Control Point",
    0x2ac7: "Object List Filter",
    0x2ac8: "Object Changed",
    0x2ac9: "Resolvable Private Address Only",
    # 0x2aca and 0x2acb undefined */
    0x2acc: "Fitness Machine Feature",
    0x2acd: "Treadmill Data",
    0x2ace: "Cross Trainer Data",
    0x2acf: "Step Climber Data",
    0x2ad0: "Stair Climber Data",
    0x2ad1: "Rower Data",
    0x2ad2: "Indoor Bike Data",
    0x2ad3: "Training Status",
    0x2ad4: "Supported Speed Range",
    0x2ad5: "Supported Inclination Range",
    0x2ad6: "Supported Resistance Level Range",
    0x2ad7: "Supported Heart Rate Range",
    0x2ad8: "Supported Power Range",
    0x2ad9: "Fitness Machine Control Point",
    0x2ada: "Fitness Machine Status",
    0x2adb: "Mesh Provisioning Data In",
    0x2adc: "Mesh Provisioning Data Out",
    0x2add: "Mesh Proxy Data In",
    0x2ade: "Mesh Proxy Data Out",
    # vendor defined */
    0xfeff: "GN Netcom",
    0xfefe: "GN ReSound A/S",
    0xfefd: "Gimbal: Inc.",
    0xfefc: "Gimbal: Inc.",
    0xfefb: "Stollmann E+V GmbH",
    0xfefa: "PayPal: Inc.",
    0xfef9: "PayPal: Inc.",
    0xfef8: "Aplix Corporation",
    0xfef7: "Aplix Corporation",
    0xfef6: "Wicentric: Inc.",
    0xfef5: "Dialog Semiconductor GmbH",
    0xfef4: "Google",
    0xfef3: "Google",
    0xfef2: "CSR",
    0xfef1: "CSR",
    0xfef0: "Intel",
    0xfeef: "Polar Electro Oy",
    0xfeee: "Polar Electro Oy",
    0xfeed: "Tile: Inc.",
    0xfeec: "Tile: Inc.",
    0xfeeb: "Swirl Networks: Inc.",
    0xfeea: "Swirl Networks: Inc.",
    0xfee9: "Quintic Corp.",
    0xfee8: "Quintic Corp.",
    0xfee7: "Tencent Holdings Limited",
    0xfee6: "Seed Labs: Inc.",
    0xfee5: "Nordic Semiconductor ASA",
    0xfee4: "Nordic Semiconductor ASA",
    0xfee3: "Anki: Inc.",
    0xfee2: "Anki: Inc.",
    0xfee1: "Anhui Huami Information Technology Co.",
    0xfee0: "Anhui Huami Information Technology Co.",
    0xfedf: "Design SHIFT",
    0xfede: "Coin: Inc.",
    0xfedd: "Jawbone",
    0xfedc: "Jawbone",
    0xfedb: "Perka: Inc.",
    0xfeda: "ISSC Technologies Corporation",
    0xfed9: "Pebble Technology Corporation",
    0xfed8: "Google",
    0xfed7: "Broadcom Corporation",
    0xfed6: "Broadcom Corporation",
    0xfed5: "Plantronics Inc.",
    0xfed4: "Apple: Inc.",
    0xfed3: "Apple: Inc.",
    0xfed2: "Apple: Inc.",
    0xfed1: "Apple: Inc.",
    0xfed0: "Apple: Inc.",
    0xfecf: "Apple: Inc.",
    0xfece: "Apple: Inc.",
    0xfecd: "Apple: Inc.",
    0xfecc: "Apple: Inc.",
    0xfecb: "Apple: Inc.",
    0xfeca: "Apple: Inc.",
    0xfec9: "Apple: Inc.",
    0xfec8: "Apple: Inc.",
    0xfec7: "Apple: Inc.",
    0xfec6: "Kocomojo: LLC",
    0xfec5: "Realtek Semiconductor Corp.",
    0xfec4: "PLUS Location Systems",
    0xfec3: "360fly: Inc.",
    0xfec2: "Blue Spark Technologies: Inc.",
    0xfec1: "KDDI Corporation",
    0xfec0: "KDDI Corporation",
    0xfebf: "Nod: Inc.",
    0xfebe: "Bose Corporation",
    0xfebd: "Clover Network: Inc.",
    0xfebc: "Dexcom: Inc.",
    0xfebb: "adafruit industries",
    0xfeba: "Tencent Holdings Limited",
    0xfeb9: "LG Electronics",
    0xfeb8: "Facebook: Inc.",
    0xfeb7: "Facebook: Inc.",
    0xfeb6: "Vencer Co: Ltd",
    0xfeb5: "WiSilica Inc.",
    0xfeb4: "WiSilica Inc.",
    0xfeb3: "Taobao",
    0xfeb2: "Microsoft Corporation",
    0xfeb1: "Electronics Tomorrow Limited",
    0xfeb0: "Nest Labs Inc.",
    0xfeaf: "Nest Labs Inc.",
    0xfeae: "Nokia Corporation",
    0xfead: "Nokia Corporation",
    0xfeac: "Nokia Corporation",
    0xfeab: "Nokia Corporation",
    0xfeaa: "Google",
    0xfea9: "Savant Systems LLC",
    0xfea8: "Savant Systems LLC",
    0xfea7: "UTC Fire and Security",
    0xfea6: "GoPro: Inc.",
    0xfea5: "GoPro: Inc.",
    0xfea4: "Paxton Access Ltd",
    0xfea3: "ITT Industries",
    0xfea2: "Intrepid Control Systems: Inc.",
    0xfea1: "Intrepid Control Systems: Inc.",
    0xfea0: "Google",
    0xfe9f: "Google",
    0xfe9e: "Dialog Semiconductor B.V.",
    0xfe9d: "Mobiquity Networks Inc",
    0xfe9c: "GSI Laboratories: Inc.",
    0xfe9b: "Samsara Networks: Inc",
    0xfe9a: "Estimote",
    0xfe99: "Currant: Inc.",
    0xfe98: "Currant: Inc.",
    0xfe97: "Tesla Motor Inc.",
    0xfe96: "Tesla Motor Inc.",
    0xfe95: "Xiaomi Inc.",
    0xfe94: "OttoQ Inc.",
    0xfe93: "OttoQ Inc.",
    0xfe92: "Jarden Safety & Security",
    0xfe91: "Shanghai Imilab Technology Co.,Ltd",
    0xfe90: "JUMA",
    0xfe8f: "CSR",
    0xfe8e: "ARM Ltd",
    0xfe8d: "Interaxon Inc.",
    0xfe8c: "TRON Forum",
    0xfe8b: "Apple: Inc.",
    0xfe8a: "Apple: Inc.",
    0xfe89: "B&O Play A/S",
    0xfe88: "SALTO SYSTEMS S.L.",
    0xfe87: "Qingdao Yeelink Information Technology Co.: Ltd. ( 青岛亿联客信息技术有限公司 )",
    0xfe86: "HUAWEI Technologies Co.: Ltd. ( 华为技术有限公司 )",
    0xfe85: "RF Digital Corp",
    0xfe84: "RF Digital Corp",
    0xfe83: "Blue Bite",
    0xfe82: "Medtronic Inc.",
    0xfe81: "Medtronic Inc.",
    0xfe80: "Doppler Lab",
    0xfe7f: "Doppler Lab",
    0xfe7e: "Awear Solutions Ltd",
    0xfe7d: "Aterica Health Inc.",
    0xfe7c: "Stollmann E+V GmbH",
    0xfe7b: "Orion Labs: Inc.",
    0xfe7a: "Bragi GmbH",
    0xfe79: "Zebra Technologies",
    0xfe78: "Hewlett-Packard Company",
    0xfe77: "Hewlett-Packard Company",
    0xfe76: "TangoMe",
    0xfe75: "TangoMe",
    0xfe74: "unwire",
    0xfe73: "St. Jude Medical: Inc.",
    0xfe72: "St. Jude Medical: Inc.",
    0xfe71: "Plume Design Inc",
    0xfe70: "Beijing Jingdong Century Trading Co.: Ltd.",
    0xfe6f: "LINE Corporation",
    0xfe6e: "The University of Tokyo",
    0xfe6d: "The University of Tokyo",
    0xfe6c: "TASER International: Inc.",
    0xfe6b: "TASER International: Inc.",
    0xfe6a: "Kontakt Micro-Location Sp. z o.o.",
    0xfe69: "Qualcomm Life Inc",
    0xfe68: "Qualcomm Life Inc",
    0xfe67: "Lab Sensor Solutions",
    0xfe66: "Intel Corporation",
    0xfe65: "CHIPOLO d.o.o.",
    0xfe64: "Siemens AG",
    0xfe63: "Connected Yard: Inc.",
    0xfe62: "Indagem Tech LLC",
    0xfe61: "Logitech International SA",
    0xfe60: "Lierda Science & Technology Group Co.: Ltd.",
    0xfe5F: "Eyefi: Inc.",
    0xfe5E: "Plastc Corporation",
    0xfe5D: "Grundfos A/S",
    0xfe5C: "million hunters GmbH",
    0xfe5B: "GT-tronics HK Ltd",
    0xfe5A: "Chronologics Corporation",
    0xfe59: "Nordic Semiconductor ASA",
    0xfe58: "Nordic Semiconductor ASA",
    0xfe57: "Dotted Labs",
    0xfe56: "Google Inc.",
    0xfe55: "Google Inc.",
    0xfe54: "Motiv: Inc.",
    0xfe53: "3M",
    0xfe52: "SetPoint Medical",
    0xfe51: "SRAM",
    0xfe50: "Google Inc.",
    0xfe4F: "Molekule: Inc.",
    0xfe4E: "NTT docomo",
    0xfe4D: "Casambi Technologies Oy",
    0xfe4C: "Volkswagen AG",
    0xfe4B: "Koninklijke Philips N.V.",
    0xfe4A: "OMRON HEALTHCARE Co.: Ltd.",
    0xfe49: "SenionLab AB",
    0xfe48: "General Motors",
    0xfe47: "General Motors",
    0xfe46: "B&O Play A/S",
    0xfe45: "Snapchat Inc",
    0xfe44: "SK Telecom",
    0xfe43: "Andreas Stihl AG & Co. KG",
    0xfe42: "Nets A/S",
    0xfe41: "Inugo Systems Limited",
    0xfe40: "Inugo Systems Limited",
    0xfe3F: "Friday Labs Limited",
    0xfe3E: "BD Medical",
    0xfe3D: "BD Medical",
    0xfe3C: "Alibaba",
    0xfe3B: "Dolby Laboratories",
    0xfe3A: "TTS Tooltechnic Systems AG & Co. KG",
    0xfe39: "TTS Tooltechnic Systems AG & Co. KG",
    0xfe38: "Spaceek LTD",
    0xfe37: "Spaceek LTD",
    0xfe36: "HUAWEI Technologies Co.: Ltd",
    0xfe35: "HUAWEI Technologies Co.: Ltd",
    0xfe34: "SmallLoop LLC",
    0xfe33: "CHIPOLO d.o.o.",
    0xfe32: "Pro-Mark: Inc.",
    0xfe31: "Volkswagen AG",
    0xfe30: "Volkswagen AG",
    0xfe2F: "CRESCO Wireless: Inc",
    0xfe2E: "ERi,Inc.",
    0xfe2D: "SMART INNOVATION Co.,Ltd",
    0xfe2C: "Google Inc.",
    0xfe2B: "ITT Industries",
    0xfe2A: "DaisyWorks: Inc.",
    0xfe29: "Gibson Innovations",
    0xfe28: "Ayla Network",
    0xfe27: "Google Inc.",
    0xfe26: "Google Inc.",
    0xfe25: "Apple: Inc.",
    0xfe24: "August Home Inc",
    0xfe23: "Zoll Medical Corporation",
    0xfe22: "Zoll Medical Corporation",
    0xfe21: "Bose Corporation",
    0xfe20: "Emerson",
    0xfe1F: "Garmin International: Inc.",
    0xfe1E: "Smart Innovations Co.: Ltd",
    0xfe1D: "Illuminati Instrument Corporation",
    0xfe1C: "NetMedia: Inc.",
    # SDO defined */
    0xfffc: "AirFuel Alliance",
    0xfffe: "Alliance for Wireless Power (A4WP)",
    0xfffd: "Fast IDentity Online Alliance (FIDO)",
}

uuid128_dict = {
    "a3c87500-8ed3-4bdf-8a39-a01bebede295": "Eddystone Configuration Service",
    "a3c87501-8ed3-4bdf-8a39-a01bebede295": "Capabilities",
    "a3c87502-8ed3-4bdf-8a39-a01bebede295": "Active Slot",
    "a3c87503-8ed3-4bdf-8a39-a01bebede295": "Advertising Interval",
    "a3c87504-8ed3-4bdf-8a39-a01bebede295": "Radio Tx Power",
    "a3c87505-8ed3-4bdf-8a39-a01bebede295": "(Advanced) Advertised Tx Power",
    "a3c87506-8ed3-4bdf-8a39-a01bebede295": "Lock State",
    "a3c87507-8ed3-4bdf-8a39-a01bebede295": "Unlock",
    "a3c87508-8ed3-4bdf-8a39-a01bebede295": "Public ECDH Key",
    "a3c87509-8ed3-4bdf-8a39-a01bebede295": "EID Identity Key",
    "a3c8750a-8ed3-4bdf-8a39-a01bebede295": "ADV Slot Data",
    "a3c8750b-8ed3-4bdf-8a39-a01bebede295": "(Advanced) Factory reset",
    "a3c8750c-8ed3-4bdf-8a39-a01bebede295": "(Advanced) Remain Connectable",
    # BBC micro:bit Bluetooth Profiles */
    "e95d0753-251d-470a-a062-fa1922dfa9a8": "MicroBit Accelerometer Service",
    "e95dca4b-251d-470a-a062-fa1922dfa9a8": "MicroBit Accelerometer Data",
    "e95dfb24-251d-470a-a062-fa1922dfa9a8": "MicroBit Accelerometer Period",
    "e95df2d8-251d-470a-a062-fa1922dfa9a8": "MicroBit Magnetometer Service",
    "e95dfb11-251d-470a-a062-fa1922dfa9a8": "MicroBit Magnetometer Data",
    "e95d386c-251d-470a-a062-fa1922dfa9a8": "MicroBit Magnetometer Period",
    "e95d9715-251d-470a-a062-fa1922dfa9a8": "MicroBit Magnetometer Bearing",
    "e95d9882-251d-470a-a062-fa1922dfa9a8": "MicroBit Button Service",
    "e95dda90-251d-470a-a062-fa1922dfa9a8": "MicroBit Button A State",
    "e95dda91-251d-470a-a062-fa1922dfa9a8": "MicroBit Button B State",
    "e95d127b-251d-470a-a062-fa1922dfa9a8": "MicroBit IO PIN Service",
    "e95d8d00-251d-470a-a062-fa1922dfa9a8": "MicroBit PIN Data",
    "e95d5899-251d-470a-a062-fa1922dfa9a8": "MicroBit PIN AD Configuration",
    "e95dd822-251d-470a-a062-fa1922dfa9a8": "MicroBit PWM Control",
    "e95dd91d-251d-470a-a062-fa1922dfa9a8": "MicroBit LED Service",
    "e95d7b77-251d-470a-a062-fa1922dfa9a8": "MicroBit LED Matrix state",
    "e95d93ee-251d-470a-a062-fa1922dfa9a8": "MicroBit LED Text",
    "e95d0d2d-251d-470a-a062-fa1922dfa9a8": "MicroBit Scrolling Delay",
    "e95d93af-251d-470a-a062-fa1922dfa9a8": "MicroBit Event Service",
    "e95db84c-251d-470a-a062-fa1922dfa9a8": "MicroBit Requirements",
    "e95d9775-251d-470a-a062-fa1922dfa9a8": "MicroBit Event Data",
    "e95d23c4-251d-470a-a062-fa1922dfa9a8": "MicroBit Client Requirements",
    "e95d5404-251d-470a-a062-fa1922dfa9a8": "MicroBit Client Events",
    "e95d93b0-251d-470a-a062-fa1922dfa9a8": "MicroBit DFU Control Service" "",
    "e95d93b1-251d-470a-a062-fa1922dfa9a8": "MicroBit DFU Control",
    "e95d6100-251d-470a-a062-fa1922dfa9a8": "MicroBit Temperature Service",
    "e95d1b25-251d-470a-a062-fa1922dfa9a8": "MicroBit Temperature Period",
    # Nordic UART Port Emulation */
    "6e400001-b5a3-f393-e0a9-e50e24dcca9e": "Nordic UART Service",
    "6e400002-b5a3-f393-e0a9-e50e24dcca9e": "Nordic UART TX",
    "6e400003-b5a3-f393-e0a9-e50e24dcca9e": "Nordic UART RX",
}

services_dict = {
        # BLUETOOTH CLASSIC PROFILES
        "00001000-0000-1000-8000-00805f9b34fb" : "Service Discovery Server",
        "00001101-0000-1000-8000-00805f9b34fb" : "Serial Port",
        "00001103-0000-1000-8000-00805f9b34fb" : "Dialup Networking",
        "00001104-0000-1000-8000-00805f9b34fb" : "IrMC Sync",
        "00001105-0000-1000-8000-00805f9b34fb" : "OBEX Object Push",
        "00001106-0000-1000-8000-00805f9b34fb" : "OBEX File Transfer",
        "00001108-0000-1000-8000-00805f9b34fb" : "Headset",
        "0000110a-0000-1000-8000-00805f9b34fb" : "A2DP Source",
        "0000110b-0000-1000-8000-00805f9b34fb" : "A2DP Sink",
        "0000110c-0000-1000-8000-00805f9b34fb" : "A/V Remote Control Target",
        "0000110d-0000-1000-8000-00805f9b34fb" : "Advanced Audio Distribution Profile",
        "0000110e-0000-1000-8000-00805f9b34fb" : "A/V Remote Control",
        "00001112-0000-1000-8000-00805f9b34fb" : "Headset AG",
        "00001115-0000-1000-8000-00805f9b34fb" : "PANU",
        "00001116-0000-1000-8000-00805f9b34fb" : "NAP",
        "0000111b-0000-1000-8000-00805f9b34fb" : "Imaging Responder",
        "0000111e-0000-1000-8000-00805f9b34fb" : "Handsfree",
        "0000111f-0000-1000-8000-00805f9b34fb" : "Handsfree Audio Gateway",
        "00001124-0000-1000-8000-00805f9b34fb" : "Human Interface Device",
        "0000112f-0000-1000-8000-00805f9b34fb" : "Phonebook Access Server",
        "00001132-0000-1000-8000-00805f9b34fb" : "Message Access Server",
        "00001133-0000-1000-8000-00805f9b34fb" : "Message Notification Server",
        "00001200-0000-1000-8000-00805f9b34fb" : "PnP Information",
        "00001203-0000-1000-8000-00805f9b34fb" : "Generic Audio",

        # GATT Services
        "00001800-0000-1000-8000-00805f9b34fb" : "Generic Access",
        "00001801-0000-1000-8000-00805f9b34fb" : "Generic Attribute",
        "00001802-0000-1000-8000-00805f9b34fb" : "Immediate Alert",
        "00001803-0000-1000-8000-00805f9b34fb" : "Link Loss",
        "00001804-0000-1000-8000-00805f9b34fb" : "Tx Power",
        "00001805-0000-1000-8000-00805f9b34fb" : "Current Time Service",
        "00001806-0000-1000-8000-00805f9b34fb" : "Reference Time Update Service",
        "00001807-0000-1000-8000-00805f9b34fb" : "Next DST Change Service",
        "00001808-0000-1000-8000-00805f9b34fb" : "Glucose",
        "00001809-0000-1000-8000-00805f9b34fb" : "Health Thermometer",
        "0000180a-0000-1000-8000-00805f9b34fb" : "Device Information",
        "0000180b-0000-1000-8000-00805f9b34fb" : "Network Availability",
        "0000180c-0000-1000-8000-00805f9b34fb" : "Watchdog",
        "0000180d-0000-1000-8000-00805f9b34fb" : "Heart Rate",
        "0000180e-0000-1000-8000-00805f9b34fb" : "Phone Alert Status Service",
        "0000180f-0000-1000-8000-00805f9b34fb" : "Battery Service",
        "00001810-0000-1000-8000-00805f9b34fb" : "Blood Pressure",
        "00001811-0000-1000-8000-00805f9b34fb" : "Alert Notification Service",
        "00001812-0000-1000-8000-00805f9b34fb" : "Human Interface Device",
        "00001813-0000-1000-8000-00805f9b34fb" : "Scan Parameters",
        "00001814-0000-1000-8000-00805f9b34fb" : "Running Speed and Cadence",
        "00001815-0000-1000-8000-00805f9b34fb" : "Automation IO",
        "00001816-0000-1000-8000-00805f9b34fb" : "Cycling Speed and Cadence",
        "00001818-0000-1000-8000-00805f9b34fb" : "Cycling Power",
        "00001819-0000-1000-8000-00805f9b34fb" : "Location and Navigation",
        "0000181a-0000-1000-8000-00805f9b34fb" : "Environmental Sensing",
        "0000181b-0000-1000-8000-00805f9b34fb" : "Body Composition",
        "0000181c-0000-1000-8000-00805f9b34fb" : "User Data",
        "0000181d-0000-1000-8000-00805f9b34fb" : "Weight Scale",
        "0000181e-0000-1000-8000-00805f9b34fb" : "Bond Management",
        "0000181f-0000-1000-8000-00805f9b34fb" : "Continuous Glucose Monitoring",
        "00001820-0000-1000-8000-00805f9b34fb" : "Internet Protocol Support",
        "00002700-0000-1000-8000-00805f9b34fb" : "unitless",
        "00002701-0000-1000-8000-00805f9b34fb" : "length (metre)",
        "00002702-0000-1000-8000-00805f9b34fb" : "mass (kilogram)",
        "00002703-0000-1000-8000-00805f9b34fb" : "time (second)",
        "00002704-0000-1000-8000-00805f9b34fb" : "electric current (ampere)",
        "00002705-0000-1000-8000-00805f9b34fb" : "thermodynamic temperature (kelvin)",
        "00002706-0000-1000-8000-00805f9b34fb" : "amount of substance (mole)",
        "00002707-0000-1000-8000-00805f9b34fb" : "luminous intensity (candela)",
        "00002710-0000-1000-8000-00805f9b34fb" : "area (square metres)",
        "00002711-0000-1000-8000-00805f9b34fb" : "volume (cubic metres)",
        "00002712-0000-1000-8000-00805f9b34fb" : "velocity (metres per second)",
        "00002713-0000-1000-8000-00805f9b34fb" : "acceleration (metres per second squared)",
        "00002714-0000-1000-8000-00805f9b34fb" : "wavenumber (reciprocal metre)",
        "00002715-0000-1000-8000-00805f9b34fb" : "density (kilogram per cubic metre)",
        "00002716-0000-1000-8000-00805f9b34fb" : "surface density (kilogram per square metre)",
        "00002717-0000-1000-8000-00805f9b34fb" : "specific volume (cubic metre per kilogram)",
        "00002718-0000-1000-8000-00805f9b34fb" : "current density (ampere per square metre)",
        "00002719-0000-1000-8000-00805f9b34fb" : "magnetic field strength (ampere per metre)",
        "0000271a-0000-1000-8000-00805f9b34fb" : "amount concentration (mole per cubic metre)",
        "0000271b-0000-1000-8000-00805f9b34fb" : "mass concentration (kilogram per cubic metre)",
        "0000271c-0000-1000-8000-00805f9b34fb" : "luminance (candela per square metre)",
        "0000271d-0000-1000-8000-00805f9b34fb" : "refractive index",
        "0000271e-0000-1000-8000-00805f9b34fb" : "relative permeability",
        "00002720-0000-1000-8000-00805f9b34fb" : "plane angle (radian)",
        "00002721-0000-1000-8000-00805f9b34fb" : "solid angle (steradian)",
        "00002722-0000-1000-8000-00805f9b34fb" : "frequency (hertz)",
        "00002723-0000-1000-8000-00805f9b34fb" : "force (newton)",
        "00002724-0000-1000-8000-00805f9b34fb" : "pressure (pascal)",
        "00002725-0000-1000-8000-00805f9b34fb" : "energy (joule)",
        "00002726-0000-1000-8000-00805f9b34fb" : "power (watt)",
        "00002727-0000-1000-8000-00805f9b34fb" : "electric charge (coulomb)",
        "00002728-0000-1000-8000-00805f9b34fb" : "electric potential difference (volt)",
        "00002729-0000-1000-8000-00805f9b34fb" : "capacitance (farad)",
        "0000272a-0000-1000-8000-00805f9b34fb" : "electric resistance (ohm)",
        "0000272b-0000-1000-8000-00805f9b34fb" : "electric conductance (siemens)",
        "0000272c-0000-1000-8000-00805f9b34fb" : "magnetic flux (weber)",
        "0000272d-0000-1000-8000-00805f9b34fb" : "magnetic flux density (tesla)",
        "0000272e-0000-1000-8000-00805f9b34fb" : "inductance (henry)",
        "0000272f-0000-1000-8000-00805f9b34fb" : "Celsius temperature (degree Celsius)",
        "00002730-0000-1000-8000-00805f9b34fb" : "luminous flux (lumen)",
        "00002731-0000-1000-8000-00805f9b34fb" : "illuminance (lux)",
        "00002732-0000-1000-8000-00805f9b34fb" : "activity referred to a radionuclide (becquerel)",
        "00002733-0000-1000-8000-00805f9b34fb" : "absorbed dose (gray)",
        "00002734-0000-1000-8000-00805f9b34fb" : "dose equivalent (sievert)",
        "00002735-0000-1000-8000-00805f9b34fb" : "catalytic activity (katal)",
        "00002740-0000-1000-8000-00805f9b34fb" : "dynamic viscosity (pascal second)",
        "00002741-0000-1000-8000-00805f9b34fb" : "moment of force (newton metre)",
        "00002742-0000-1000-8000-00805f9b34fb" : "surface tension (newton per metre)",
        "00002743-0000-1000-8000-00805f9b34fb" : "angular velocity (radian per second)",
        "00002744-0000-1000-8000-00805f9b34fb" : "angular acceleration (radian per second squared)",
        "00002745-0000-1000-8000-00805f9b34fb" : "heat flux density (watt per square metre)",
        "00002746-0000-1000-8000-00805f9b34fb" : "heat capacity (joule per kelvin)",
        "00002747-0000-1000-8000-00805f9b34fb" : "specific heat capacity (joule per kilogram kelvin)",
        "00002748-0000-1000-8000-00805f9b34fb" : "specific energy (joule per kilogram)",
        "00002749-0000-1000-8000-00805f9b34fb" : "thermal conductivity (watt per metre kelvin)",
        "0000274a-0000-1000-8000-00805f9b34fb" : "energy density (joule per cubic metre)",
        "0000274b-0000-1000-8000-00805f9b34fb" : "electric field strength (volt per metre)",
        "0000274c-0000-1000-8000-00805f9b34fb" : "electric charge density (coulomb per cubic metre)",
        "0000274d-0000-1000-8000-00805f9b34fb" : "surface charge density (coulomb per square metre)",
        "0000274e-0000-1000-8000-00805f9b34fb" : "electric flux density (coulomb per square metre)",
        "0000274f-0000-1000-8000-00805f9b34fb" : "permittivity (farad per metre)",
        "00002750-0000-1000-8000-00805f9b34fb" : "permeability (henry per metre)",
        "00002751-0000-1000-8000-00805f9b34fb" : "molar energy (joule per mole)",
        "00002752-0000-1000-8000-00805f9b34fb" : "molar entropy (joule per mole kelvin)",
        "00002753-0000-1000-8000-00805f9b34fb" : "exposure (coulomb per kilogram)",
        "00002754-0000-1000-8000-00805f9b34fb" : "absorbed dose rate (gray per second)",
        "00002755-0000-1000-8000-00805f9b34fb" : "radiant intensity (watt per steradian)",
        "00002756-0000-1000-8000-00805f9b34fb" : "radiance (watt per square metre steradian)",
        "00002757-0000-1000-8000-00805f9b34fb" : "catalytic activity concentration (katal per cubic metre)",
        "00002760-0000-1000-8000-00805f9b34fb" : "time (minute)",
        "00002761-0000-1000-8000-00805f9b34fb" : "time (hour)",
        "00002762-0000-1000-8000-00805f9b34fb" : "time (day)",
        "00002763-0000-1000-8000-00805f9b34fb" : "plane angle (degree)",
        "00002764-0000-1000-8000-00805f9b34fb" : "plane angle (minute)",
        "00002765-0000-1000-8000-00805f9b34fb" : "plane angle (second)",
        "00002766-0000-1000-8000-00805f9b34fb" : "area (hectare)",
        "00002767-0000-1000-8000-00805f9b34fb" : "volume (litre)",
        "00002768-0000-1000-8000-00805f9b34fb" : "mass (tonne)",
        "00002780-0000-1000-8000-00805f9b34fb" : "pressure (bar)",
        "00002781-0000-1000-8000-00805f9b34fb" : "pressure (millimetre of mercury)",
        "00002782-0000-1000-8000-00805f9b34fb" : "length (angstrom)",
        "00002783-0000-1000-8000-00805f9b34fb" : "length (nautical mile)",
        "00002784-0000-1000-8000-00805f9b34fb" : "area (barn)",
        "00002785-0000-1000-8000-00805f9b34fb" : "velocity (knot)",
        "00002786-0000-1000-8000-00805f9b34fb" : "logarithmic radio quantity (neper)",
        "00002787-0000-1000-8000-00805f9b34fb" : "logarithmic radio quantity (bel)",
        "000027a0-0000-1000-8000-00805f9b34fb" : "length (yard)",
        "000027a1-0000-1000-8000-00805f9b34fb" : "length (parsec)",
        "000027a2-0000-1000-8000-00805f9b34fb" : "length (inch)",
        "000027a3-0000-1000-8000-00805f9b34fb" : "length (foot)",
        "000027a4-0000-1000-8000-00805f9b34fb" : "length (mile)",
        "000027a5-0000-1000-8000-00805f9b34fb" : "pressure (pound-force per square inch)",
        "000027a6-0000-1000-8000-00805f9b34fb" : "velocity (kilometre per hour)",
        "000027a7-0000-1000-8000-00805f9b34fb" : "velocity (mile per hour)",
        "000027a8-0000-1000-8000-00805f9b34fb" : "angular velocity (revolution per minute)",
        "000027a9-0000-1000-8000-00805f9b34fb" : "energy (gram calorie)",
        "000027aa-0000-1000-8000-00805f9b34fb" : "energy (kilogram calorie)",
        "000027ab-0000-1000-8000-00805f9b34fb" : "energy (kilowatt hour)",
        "000027ac-0000-1000-8000-00805f9b34fb" : "thermodynamic temperature (degree Fahrenheit)",
        "000027ad-0000-1000-8000-00805f9b34fb" : "percentage",
        "000027ae-0000-1000-8000-00805f9b34fb" : "per mille",
        "000027af-0000-1000-8000-00805f9b34fb" : "period (beats per minute)",
        "000027b0-0000-1000-8000-00805f9b34fb" : "electric charge (ampere hours)",
        "000027b1-0000-1000-8000-00805f9b34fb" : "mass density (milligram per decilitre)",
        "000027b2-0000-1000-8000-00805f9b34fb" : "mass density (millimole per litre)",
        "000027b3-0000-1000-8000-00805f9b34fb" : "time (year)",
        "000027b4-0000-1000-8000-00805f9b34fb" : "time (month)",
        "000027b5-0000-1000-8000-00805f9b34fb" : "concentration (count per cubic metre)",
        "000027b6-0000-1000-8000-00805f9b34fb" : "irradiance (watt per square metre)",
        "000027b7-0000-1000-8000-00805f9b34fb" : "milliliter (per kilogram per minute)",
        "000027b8-0000-1000-8000-00805f9b34fb" : "mass (pound)",
        "00002800-0000-1000-8000-00805f9b34fb" : "GATT Primary Service Declaration",
        "00002801-0000-1000-8000-00805f9b34fb" : "GATT Secondary Service Declaration",
        "00002802-0000-1000-8000-00805f9b34fb" : "GATT Include Declaration",
        "00002803-0000-1000-8000-00805f9b34fb" : "GATT Characteristic Declaration",
        "00002900-0000-1000-8000-00805f9b34fb" : "Characteristic Extended Properties",
        "00002901-0000-1000-8000-00805f9b34fb" : "Characteristic User Description",
        "00002902-0000-1000-8000-00805f9b34fb" : "Client Characteristic Configuration",
        "00002903-0000-1000-8000-00805f9b34fb" : "Server Characteristic Configuration",
        "00002904-0000-1000-8000-00805f9b34fb" : "Characteristic Presentation Format",
        "00002905-0000-1000-8000-00805f9b34fb" : "Characteristic Aggregate Format",
        "00002906-0000-1000-8000-00805f9b34fb" : "Valid Range",
        "00002907-0000-1000-8000-00805f9b34fb" : "External Report Reference",
        "00002908-0000-1000-8000-00805f9b34fb" : "Report Reference",
        "00002909-0000-1000-8000-00805f9b34fb" : "Number of Digits",
        "0000290a-0000-1000-8000-00805f9b34fb" : "Trigger Setting",
        "0000290b-0000-1000-8000-00805f9b34fb" : "Environmental Sensing Configuration",
        "0000290c-0000-1000-8000-00805f9b34fb" : "Environmental Sensing Measurement",
        "0000290d-0000-1000-8000-00805f9b34fb" : "Environmental Sensing Trigger Setting",
        "00002a00-0000-1000-8000-00805f9b34fb" : "Device Name",
        "00002a01-0000-1000-8000-00805f9b34fb" : "Appearance",
        "00002a02-0000-1000-8000-00805f9b34fb" : "Peripheral Privacy Flag",
        "00002a03-0000-1000-8000-00805f9b34fb" : "Reconnection Address",
        "00002a04-0000-1000-8000-00805f9b34fb" : "Peripheral Preferred Connection Parameters",
        "00002a05-0000-1000-8000-00805f9b34fb" : "Service Changed",
        "00002a06-0000-1000-8000-00805f9b34fb" : "Alert Level",
        "00002a07-0000-1000-8000-00805f9b34fb" : "Tx Power Level",
        "00002a08-0000-1000-8000-00805f9b34fb" : "Date Time",
        "00002a09-0000-1000-8000-00805f9b34fb" : "Day of Week",
        "00002a0a-0000-1000-8000-00805f9b34fb" : "Day Date Time",
        "00002a0b-0000-1000-8000-00805f9b34fb" : "Exact Time 100",
        "00002a0c-0000-1000-8000-00805f9b34fb" : "Exact Time 256",
        "00002a0d-0000-1000-8000-00805f9b34fb" : "DST Offset",
        "00002a0e-0000-1000-8000-00805f9b34fb" : "Time Zone",
        "00002a0f-0000-1000-8000-00805f9b34fb" : "Local Time Information",
        "00002a10-0000-1000-8000-00805f9b34fb" : "Secondary Time Zone",
        "00002a11-0000-1000-8000-00805f9b34fb" : "Time with DST",
        "00002a12-0000-1000-8000-00805f9b34fb" : "Time Accuracy",
        "00002a13-0000-1000-8000-00805f9b34fb" : "Time Source",
        "00002a14-0000-1000-8000-00805f9b34fb" : "Reference Time Information",
        "00002a15-0000-1000-8000-00805f9b34fb" : "Time Broadcast",
        "00002a16-0000-1000-8000-00805f9b34fb" : "Time Update Control Point",
        "00002a17-0000-1000-8000-00805f9b34fb" : "Time Update State",
        "00002a18-0000-1000-8000-00805f9b34fb" : "Glucose Measurement",
        "00002a19-0000-1000-8000-00805f9b34fb" : "Battery Level",
        "00002a1a-0000-1000-8000-00805f9b34fb" : "Battery Power State",
        "00002a1b-0000-1000-8000-00805f9b34fb" : "Battery Level State",
        "00002a1c-0000-1000-8000-00805f9b34fb" : "Temperature Measurement",
        "00002a1d-0000-1000-8000-00805f9b34fb" : "Temperature Type",
        "00002a1e-0000-1000-8000-00805f9b34fb" : "Intermediate Temperature",
        "00002a1f-0000-1000-8000-00805f9b34fb" : "Temperature Celsius",
        "00002a20-0000-1000-8000-00805f9b34fb" : "Temperature Fahrenheit",
        "00002a21-0000-1000-8000-00805f9b34fb" : "Measurement Interval",
        "00002a22-0000-1000-8000-00805f9b34fb" : "Boot Keyboard Input Report",
        "00002a23-0000-1000-8000-00805f9b34fb" : "System ID",
        "00002a24-0000-1000-8000-00805f9b34fb" : "Model Number String",
        "00002a25-0000-1000-8000-00805f9b34fb" : "Serial Number String",
        "00002a26-0000-1000-8000-00805f9b34fb" : "Firmware Revision String",
        "00002a27-0000-1000-8000-00805f9b34fb" : "Hardware Revision String",
        "00002a28-0000-1000-8000-00805f9b34fb" : "Software Revision String",
        "00002a29-0000-1000-8000-00805f9b34fb" : "Manufacturer Name String",
        "00002a2a-0000-1000-8000-00805f9b34fb" : "IEEE 11073-20601 Regulatory Certification Data List",
        "00002a2b-0000-1000-8000-00805f9b34fb" : "Current Time",
        "00002a2c-0000-1000-8000-00805f9b34fb" : "Elevation",
        "00002a2d-0000-1000-8000-00805f9b34fb" : "Latitude",
        "00002a2e-0000-1000-8000-00805f9b34fb" : "Longitude",
        "00002a2f-0000-1000-8000-00805f9b34fb" : "Position 2D",
        "00002a30-0000-1000-8000-00805f9b34fb" : "Position 3D",
        "00002a31-0000-1000-8000-00805f9b34fb" : "Scan Refresh",
        "00002a32-0000-1000-8000-00805f9b34fb" : "Boot Keyboard Output Report",
        "00002a33-0000-1000-8000-00805f9b34fb" : "Boot Mouse Input Report",
        "00002a34-0000-1000-8000-00805f9b34fb" : "Glucose Measurement Context",
        "00002a35-0000-1000-8000-00805f9b34fb" : "Blood Pressure Measurement",
        "00002a36-0000-1000-8000-00805f9b34fb" : "Intermediate Cuff Pressure",
        "00002a37-0000-1000-8000-00805f9b34fb" : "Heart Rate Measurement",
        "00002a38-0000-1000-8000-00805f9b34fb" : "Body Sensor Location",
        "00002a39-0000-1000-8000-00805f9b34fb" : "Heart Rate Control Point",
        "00002a3a-0000-1000-8000-00805f9b34fb" : "Removable",
        "00002a3b-0000-1000-8000-00805f9b34fb" : "Service Required",
        "00002a3c-0000-1000-8000-00805f9b34fb" : "Scientific Temperature Celsius",
        "00002a3d-0000-1000-8000-00805f9b34fb" : "String",
        "00002a3e-0000-1000-8000-00805f9b34fb" : "Network Availability",
        "00002a3f-0000-1000-8000-00805f9b34fb" : "Alert Status",
        "00002a40-0000-1000-8000-00805f9b34fb" : "Ringer Control Point",
        "00002a41-0000-1000-8000-00805f9b34fb" : "Ringer Setting",
        "00002a42-0000-1000-8000-00805f9b34fb" : "Alert Category ID Bit Mask",
        "00002a43-0000-1000-8000-00805f9b34fb" : "Alert Category ID",
        "00002a44-0000-1000-8000-00805f9b34fb" : "Alert Notification Control Point",
        "00002a45-0000-1000-8000-00805f9b34fb" : "Unread Alert Status",
        "00002a46-0000-1000-8000-00805f9b34fb" : "New Alert",
        "00002a47-0000-1000-8000-00805f9b34fb" : "Supported New Alert Category",
        "00002a48-0000-1000-8000-00805f9b34fb" : "Supported Unread Alert Category",
        "00002a49-0000-1000-8000-00805f9b34fb" : "Blood Pressure Feature",
        "00002a4a-0000-1000-8000-00805f9b34fb" : "HID Information",
        "00002a4b-0000-1000-8000-00805f9b34fb" : "HID Report Map",
        "00002a4c-0000-1000-8000-00805f9b34fb" : "HID Control Point",
        "00002a4e-0000-1000-8000-00805f9b34fb" : "Protocol Mode",
        "00002a4f-0000-1000-8000-00805f9b34fb" : "Scan Interval Windows",
        "00002a50-0000-1000-8000-00805f9b34fb" : "PnP ID",
        "00002a51-0000-1000-8000-00805f9b34fb" : "Glucose Feature",
        "00002a52-0000-1000-8000-00805f9b34fb" : "Glucose RACP",
        "00002a53-0000-1000-8000-00805f9b34fb" : "RSC Measurement",
        "00002a54-0000-1000-8000-00805f9b34fb" : "RSC Feature",
        "00002a55-0000-1000-8000-00805f9b34fb" : "RSC/CSC Control Point",
        "00002a56-0000-1000-8000-00805f9b34fb" : "Digital Input",
        "00002a57-0000-1000-8000-00805f9b34fb" : "Digital Output",
        "00002a58-0000-1000-8000-00805f9b34fb" : "Analog Input",
        "00002a59-0000-1000-8000-00805f9b34fb" : "Analog Output",
        "00002a5A-0000-1000-8000-00805f9b34fb" : "Aggregate Input",
        "00002a5b-0000-1000-8000-00805f9b34fb" : "CSC Measurement",
        "00002a5c-0000-1000-8000-00805f9b34fb" : "CSC Feature",
        "00002a5d-0000-1000-8000-00805f9b34fb" : "Sensor Location",
        "00002a5f-0000-1000-8000-00805f9b34fb" : "Oximetry Continuous Measure Temp",
        "00002a60-0000-1000-8000-00805f9b34fb" : "Oximetry Pulsatile Event Temp",
        "00002a61-0000-1000-8000-00805f9b34fb" : "Oximetry Feature Temp",
        "00002a62-0000-1000-8000-00805f9b34fb" : "Oximetry Control Point Temp",
        "00002a63-0000-1000-8000-00805f9b34fb" : "Cycling Power Measurement",
        "00002a64-0000-1000-8000-00805f9b34fb" : "Cycling Power Vector",
        "00002a65-0000-1000-8000-00805f9b34fb" : "Cycling Power Feature",
        "00002a66-0000-1000-8000-00805f9b34fb" : "Cycling Power Control Point",
        "00002a67-0000-1000-8000-00805f9b34fb" : "Location and Speed",
        "00002a68-0000-1000-8000-00805f9b34fb" : "Navigation",
        "00002a69-0000-1000-8000-00805f9b34fb" : "Position Quality",
        "00002a6a-0000-1000-8000-00805f9b34fb" : "LN Feature",
        "00002a6b-0000-1000-8000-00805f9b34fb" : "LN Control Point",
        "00002a6c-0000-1000-8000-00805f9b34fb" : "Elevation",
        "00002a6d-0000-1000-8000-00805f9b34fb" : "Pressure",
        "00002a6f-0000-1000-8000-00805f9b34fb" : "Humidity",
        "00002a72-0000-1000-8000-00805f9b34fb" : "Apparent Wind Speed",
        "00002a73-0000-1000-8000-00805f9b34fb" : "Apparent Wind Direction?",
        "00002a74-0000-1000-8000-00805f9b34fb" : "Gust Factor",
        "00002a75-0000-1000-8000-00805f9b34fb" : "Pollen Concentration",
        "00002a77-0000-1000-8000-00805f9b34fb" : "Irradiance",
        "00002a7a-0000-1000-8000-00805f9b34fb" : "Heat Index",
        "00002a7b-0000-1000-8000-00805f9b34fb" : "Dew Point",
        "00002a7d-0000-1000-8000-00805f9b34fb" : "Descriptor Value Changed",
        "00002a7e-0000-1000-8000-00805f9b34fb" : "Aerobic Heart Rate Lower Limit",
        "00002a7f-0000-1000-8000-00805f9b34fb" : "Aerobic Threshold",
        "00002a80-0000-1000-8000-00805f9b34fb" : "Age",
        "00002a81-0000-1000-8000-00805f9b34fb" : "Anaerobic Heart Rate Lower Limit",
        "00002a82-0000-1000-8000-00805f9b34fb" : "Anaerobic Heart Rate Upper Limit",
        "00002a83-0000-1000-8000-00805f9b34fb" : "Anaerobic Threshold",
        "00002a84-0000-1000-8000-00805f9b34fb" : "Aerobic Heart Rate Upper Limit",
        "00002a85-0000-1000-8000-00805f9b34fb" : "Date of Birth",
        "00002a86-0000-1000-8000-00805f9b34fb" : "Date of Threshold Assessment",
        "00002a87-0000-1000-8000-00805f9b34fb" : "Email Address",
        "00002a88-0000-1000-8000-00805f9b34fb" : "Fat Burn Heart Rate Lower Limit",
        "00002a89-0000-1000-8000-00805f9b34fb" : "Fat Burn Heart Rate Upper Limit",
        "00002a8a-0000-1000-8000-00805f9b34fb" : "First Name",
        "00002a8b-0000-1000-8000-00805f9b34fb" : "Five Zone Heart Rate Limits",
        "00002a8c-0000-1000-8000-00805f9b34fb" : "Gender",
        "00002a8d-0000-1000-8000-00805f9b34fb" : "Heart Rate Max",
        "00002a8e-0000-1000-8000-00805f9b34fb" : "Height",
        "00002a8f-0000-1000-8000-00805f9b34fb" : "Hip Circumference",
        "00002a90-0000-1000-8000-00805f9b34fb" : "Last Name",
        "00002a91-0000-1000-8000-00805f9b34fb" : "Maximum Recommended Heart Rate",
        "00002a99-0000-1000-8000-00805f9b34fb" : "Database Change Increment",
        "00002a9b-0000-1000-8000-00805f9b34fb" : "Body Composition Feature",
        "00002a9c-0000-1000-8000-00805f9b34fb" : "Body Composition Measurement",
        "00002aa0-0000-1000-8000-00805f9b34fb" : "Magnetic Flux Density - 2D",
        "00002aa1-0000-1000-8000-00805f9b34fb" : "Magnetic Flux Density - 3D",
        "00002aa2-0000-1000-8000-00805f9b34fb" : "Language",
        "00002aa3-0000-1000-8000-00805f9b34fb" : "Barometric Pressure Trend",
        "00002aa4-0000-1000-8000-00805f9b34fb" : "Bond Management Control Point",
        "00002aa5-0000-1000-8000-00805f9b34fb" : "Bond Management Feature",
        "00002aa6-0000-1000-8000-00805f9b34fb" : "Central Address Resolution",
        "00002aa7-0000-1000-8000-00805f9b34fb" : "CGM Measurement",
        "00002aa8-0000-1000-8000-00805f9b34fb" : "CGM Feature",
        "00002aa9-0000-1000-8000-00805f9b34fb" : "CGM Status",
        "00002aaa-0000-1000-8000-00805f9b34fb" : "CGM Session Start Time",
        "00002aab-0000-1000-8000-00805f9b34fb" : "CGM Session Run Time",
        "00002aac-0000-1000-8000-00805f9b34fb" : "CGM Specific Ops Control Point",

        "0000b000-0000-1000-8000-00805f9b34fb" : "Weight Scale",
        "0000b001-0000-1000-8000-00805f9b34fb" : "Weight Scale Measurement",
        "0000c000-0000-1000-8000-00805f9b34fb" : "Continuout Gluecose Measurement",
        "0000c001-0000-1000-8000-00805f9b34fb" : "Continuous Glucose Measurement",
        "0000c002-0000-1000-8000-00805f9b34fb" : "Continuous Glucose Features",
        "0000c003-0000-1000-8000-00805f9b34fb" : "Continuous Glucose Status",
        "0000c004-0000-1000-8000-00805f9b34fb" : "Continuous Glucose Session",
        "0000c005-0000-1000-8000-00805f9b34fb" : "Continuous Glucose Runtime",
        "0000c006-0000-1000-8000-00805f9b34fb" : "Continuous Glucose RACP",
        "0000c007-0000-1000-8000-00805f9b34fb" : "Continuous Glucose ASCP",
        "0000c008-0000-1000-8000-00805f9b34fb" : "Continuous Glucose CGMCP",
        "0000d000-0000-1000-8000-00805f9b34fb" : "Pedometer",
        "0000d001-0000-1000-8000-00805f9b34fb" : "Pedometer Measurement",
        "0000e000-0000-1000-8000-00805f9b34fb" : "Audio Temp",
        "0000e001-0000-1000-8000-00805f9b34fb" : "Audio Battery Level Temp",
        "0000e002-0000-1000-8000-00805f9b34fb" : "Audio LeftRight Temp",
        "0000e003-0000-1000-8000-00805f9b34fb" : "Audio Hi ID Temp",
        "0000e004-0000-1000-8000-00805f9b34fb" : "Audio Other Hi ID Temp",
        "0000e005-0000-1000-8000-00805f9b34fb" : "Audio Mic Attenuation Temp",
        "0000e006-0000-1000-8000-00805f9b34fb" : "Audio 2nd Stream Attenuation Temp",
        "0000e007-0000-1000-8000-00805f9b34fb" : "Audio Available Programs Bitmap Temp",
        "0000e008-0000-1000-8000-00805f9b34fb" : "Audio Stream Programs Bitmap Temp",
        "0000e009-0000-1000-8000-00805f9b34fb" : "Audio Current Active Program Temp",
        "0000e00a-0000-1000-8000-00805f9b34fb" : "Audio Program Data Version Temp",
        "0000e00b-0000-1000-8000-00805f9b34fb" : "Audio Program ID Name Selector Temp",
        "0000e00c-0000-1000-8000-00805f9b34fb" : "Audio Program Name Temp",
        "0000e00d-0000-1000-8000-00805f9b34fb" : "Audio Program Catogory Temp",

        # 16-bit UUIDs for Members, ordered by UUID ----------------------------------------------------------------------
        "0000fe1c-0000-1000-8000-00805f9b34fb" : "Custom UUID of NetMedia, Inc.",
        "0000fe1d-0000-1000-8000-00805f9b34fb" : "Custom UUID of Illuminati Instrument Corporation",
        "0000fe1e-0000-1000-8000-00805f9b34fb" : "Custom UUID of Smart Innovations Co., Ltd",
        "0000fe1f-0000-1000-8000-00805f9b34fb" : "Custom UUID of Garmin International, Inc.",
        "0000fe20-0000-1000-8000-00805f9b34fb" : "Custom UUID of Emerson",
        "0000fe21-0000-1000-8000-00805f9b34fb" : "Custom UUID of Bose Corporation",
        "0000fe22-0000-1000-8000-00805f9b34fb" : "Custom UUID of Zoll Medical Corporation",
        "0000fe23-0000-1000-8000-00805f9b34fb" : "Custom UUID of Zoll Medical Corporation",
        "0000fe24-0000-1000-8000-00805f9b34fb" : "Custom UUID of August Home Inc",
        "0000fe25-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fe26-0000-1000-8000-00805f9b34fb" : "Custom UUID of Google Inc.",
        "0000fe27-0000-1000-8000-00805f9b34fb" : "Custom UUID of Google Inc.",
        "0000fe28-0000-1000-8000-00805f9b34fb" : "Custom UUID of Ayla Networks",
        "0000fe29-0000-1000-8000-00805f9b34fb" : "Custom UUID of Gibson Innovations",
        "0000fe2a-0000-1000-8000-00805f9b34fb" : "Custom UUID of DaisyWorks, Inc.",
        "0000fe2b-0000-1000-8000-00805f9b34fb" : "Custom UUID of ITT Industries",
        "0000fe2c-0000-1000-8000-00805f9b34fb" : "Custom UUID of Google Inc.",
        "0000fe2d-0000-1000-8000-00805f9b34fb" : "Custom UUID of SMART INNOVATION Co.,Ltd",
        "0000fe2e-0000-1000-8000-00805f9b34fb" : "Custom UUID of ERi,Inc.",
        "0000fe2f-0000-1000-8000-00805f9b34fb" : "Custom UUID of CRESCO Wireless, Inc",
        "0000fe30-0000-1000-8000-00805f9b34fb" : "Custom UUID of Volkswagen AG",
        "0000fe31-0000-1000-8000-00805f9b34fb" : "Custom UUID of Volkswagen AG",
        "0000fe32-0000-1000-8000-00805f9b34fb" : "Custom UUID of Pro-Mark, Inc.",
        "0000fe33-0000-1000-8000-00805f9b34fb" : "Custom UUID of CHIPOLO d.o.o.",
        "0000fe34-0000-1000-8000-00805f9b34fb" : "Custom UUID of SmallLoop LLC",
        "0000fe35-0000-1000-8000-00805f9b34fb" : "Custom UUID of HUAWEI Technologies Co., Ltd",
        "0000fe36-0000-1000-8000-00805f9b34fb" : "Custom UUID of HUAWEI Technologies Co., Ltd",
        "0000fe37-0000-1000-8000-00805f9b34fb" : "Custom UUID of Spaceek LTD",
        "0000fe38-0000-1000-8000-00805f9b34fb" : "Custom UUID of Spaceek LTD",
        "0000fe39-0000-1000-8000-00805f9b34fb" : "Custom UUID of TTS Tooltechnic Systems AG & Co. KG",
        "0000fe3a-0000-1000-8000-00805f9b34fb" : "Custom UUID of TTS Tooltechnic Systems AG & Co. KG",
        "0000fe3b-0000-1000-8000-00805f9b34fb" : "Custom UUID of Dolby Laboratories",
        "0000fe3c-0000-1000-8000-00805f9b34fb" : "Custom UUID of Alibaba",
        "0000fe3d-0000-1000-8000-00805f9b34fb" : "Custom UUID of BD Medical",
        "0000fe3e-0000-1000-8000-00805f9b34fb" : "Custom UUID of BD Medical",
        "0000fe3f-0000-1000-8000-00805f9b34fb" : "Custom UUID of Friday Labs Limited",
        "0000fe40-0000-1000-8000-00805f9b34fb" : "Custom UUID of Inugo Systems Limited",
        "0000fe41-0000-1000-8000-00805f9b34fb" : "Custom UUID of Inugo Systems Limited",
        "0000fe42-0000-1000-8000-00805f9b34fb" : "Custom UUID of Nets A/S",
        "0000fe43-0000-1000-8000-00805f9b34fb" : "Custom UUID of Andreas Stihl AG & Co. KG",
        "0000fe44-0000-1000-8000-00805f9b34fb" : "Custom UUID of SK Telecom",
        "0000fe45-0000-1000-8000-00805f9b34fb" : "Custom UUID of Snapchat Inc",
        "0000fe46-0000-1000-8000-00805f9b34fb" : "Custom UUID of B&O Play A/S",
        "0000fe47-0000-1000-8000-00805f9b34fb" : "Custom UUID of General Motors",
        "0000fe48-0000-1000-8000-00805f9b34fb" : "Custom UUID of General Motors",
        "0000fe49-0000-1000-8000-00805f9b34fb" : "Custom UUID of SenionLab AB",
        "0000fe4a-0000-1000-8000-00805f9b34fb" : "Custom UUID of OMRON HEALTHCARE Co., Ltd.",
        "0000fe4b-0000-1000-8000-00805f9b34fb" : "Custom UUID of Koninklijke Philips N.V.",
        "0000fe4c-0000-1000-8000-00805f9b34fb" : "Custom UUID of Volkswagen AG",
        "0000fe4d-0000-1000-8000-00805f9b34fb" : "Custom UUID of Casambi Technologies Oy",
        "0000fe4e-0000-1000-8000-00805f9b34fb" : "Custom UUID of NTT docomo",
        "0000fe4f-0000-1000-8000-00805f9b34fb" : "Custom UUID of Molekule, Inc.",
        "0000fe50-0000-1000-8000-00805f9b34fb" : "Custom UUID of Google Inc.",
        "0000fe51-0000-1000-8000-00805f9b34fb" : "Custom UUID of SRAM",
        "0000fe52-0000-1000-8000-00805f9b34fb" : "Custom UUID of SetPoint Medical",
        "0000fe53-0000-1000-8000-00805f9b34fb" : "Custom UUID of 3M",
        "0000fe54-0000-1000-8000-00805f9b34fb" : "Custom UUID of Motiv, Inc.",
        "0000fe55-0000-1000-8000-00805f9b34fb" : "Custom UUID of Google Inc.",
        "0000fe56-0000-1000-8000-00805f9b34fb" : "Custom UUID of Google Inc.",
        "0000fe57-0000-1000-8000-00805f9b34fb" : "Custom UUID of Dotted Labs",
        "0000fe58-0000-1000-8000-00805f9b34fb" : "Custom UUID of Nordic Semiconductor ASA",
        "0000fe59-0000-1000-8000-00805f9b34fb" : "Custom UUID of Nordic Semiconductor ASA",
        "0000fe5a-0000-1000-8000-00805f9b34fb" : "Custom UUID of Chronologics Corporation",
        "0000fe5b-0000-1000-8000-00805f9b34fb" : "Custom UUID of GT-tronics HK Ltd",
        "0000fe5c-0000-1000-8000-00805f9b34fb" : "Custom UUID of million hunters GmbH",
        "0000fe5d-0000-1000-8000-00805f9b34fb" : "Custom UUID of Grundfos A/S",
        "0000fe5e-0000-1000-8000-00805f9b34fb" : "Custom UUID of Plastc Corporation",
        "0000fe5f-0000-1000-8000-00805f9b34fb" : "Custom UUID of Eyefi, Inc.",
        "0000fe60-0000-1000-8000-00805f9b34fb" : "Custom UUID of Lierda Science & Technology Group Co., Ltd.",
        "0000fe61-0000-1000-8000-00805f9b34fb" : "Custom UUID of Logitech International SA",
        "0000fe62-0000-1000-8000-00805f9b34fb" : "Custom UUID of Indagem Tech LLC",
        "0000fe63-0000-1000-8000-00805f9b34fb" : "Custom UUID of Connected Yard, Inc.",
        "0000fe64-0000-1000-8000-00805f9b34fb" : "Custom UUID of Siemens AG",
        "0000fe65-0000-1000-8000-00805f9b34fb" : "Custom UUID of CHIPOLO d.o.o.",
        "0000fe66-0000-1000-8000-00805f9b34fb" : "Custom UUID of Intel Corporation",
        "0000fe67-0000-1000-8000-00805f9b34fb" : "Custom UUID of Lab Sensor Solutions",
        "0000fe68-0000-1000-8000-00805f9b34fb" : "Custom UUID of Qualcomm Life Inc",
        "0000fe69-0000-1000-8000-00805f9b34fb" : "Custom UUID of Qualcomm Life Inc",
        "0000fe6a-0000-1000-8000-00805f9b34fb" : "Custom UUID of Kontakt Micro-Location Sp. z o.o.",
        "0000fe6b-0000-1000-8000-00805f9b34fb" : "Custom UUID of TASER International, Inc.",
        "0000fe6c-0000-1000-8000-00805f9b34fb" : "Custom UUID of TASER International, Inc.",
        "0000fe6d-0000-1000-8000-00805f9b34fb" : "Custom UUID of The University of Tokyo",
        "0000fe6e-0000-1000-8000-00805f9b34fb" : "Custom UUID of The University of Tokyo",
        "0000fe6f-0000-1000-8000-00805f9b34fb" : "Custom UUID of LINE Corporation",
        "0000fe70-0000-1000-8000-00805f9b34fb" : "Custom UUID of Beijing Jingdong Century Trading Co., Ltd.",
        "0000fe71-0000-1000-8000-00805f9b34fb" : "Custom UUID of Plume Design Inc",
        "0000fe72-0000-1000-8000-00805f9b34fb" : "Custom UUID of St. Jude Medical, Inc.",
        "0000fe73-0000-1000-8000-00805f9b34fb" : "Custom UUID of St. Jude Medical, Inc.",
        "0000fe74-0000-1000-8000-00805f9b34fb" : "Custom UUID of unwire",
        "0000fe75-0000-1000-8000-00805f9b34fb" : "Custom UUID of TangoMe",
        "0000fe76-0000-1000-8000-00805f9b34fb" : "Custom UUID of TangoMe",
        "0000fe77-0000-1000-8000-00805f9b34fb" : "Custom UUID of Hewlett-Packard Company",
        "0000fe78-0000-1000-8000-00805f9b34fb" : "Custom UUID of Hewlett-Packard Company",
        "0000fe79-0000-1000-8000-00805f9b34fb" : "Custom UUID of Zebra Technologies",
        "0000fe7a-0000-1000-8000-00805f9b34fb" : "Custom UUID of Bragi GmbH",
        "0000fe7b-0000-1000-8000-00805f9b34fb" : "Custom UUID of Orion Labs, Inc.",
        "0000fe7c-0000-1000-8000-00805f9b34fb" : "Custom UUID of Telit Wireless Solutions (Formerly Stollmann E+V GmbH)",
        "0000fe7d-0000-1000-8000-00805f9b34fb" : "Custom UUID of Aterica Health Inc.",
        "0000fe7e-0000-1000-8000-00805f9b34fb" : "Custom UUID of Awear Solutions Ltd",
        "0000fe7f-0000-1000-8000-00805f9b34fb" : "Custom UUID of Doppler Lab",
        "0000fe80-0000-1000-8000-00805f9b34fb" : "Custom UUID of Doppler Lab",
        "0000fe81-0000-1000-8000-00805f9b34fb" : "Custom UUID of Medtronic Inc.",
        "0000fe82-0000-1000-8000-00805f9b34fb" : "Custom UUID of Medtronic Inc.",
        "0000fe83-0000-1000-8000-00805f9b34fb" : "Custom UUID of Blue Bite",
        "0000fe84-0000-1000-8000-00805f9b34fb" : "Custom UUID of RF Digital Corp",
        "0000fe85-0000-1000-8000-00805f9b34fb" : "Custom UUID of RF Digital Corp",
        "0000fe86-0000-1000-8000-00805f9b34fb" : "Custom UUID of HUAWEI Technologies Co., Ltd. ( )",
        "0000fe87-0000-1000-8000-00805f9b34fb" : "Custom UUID of Qingdao Yeelink Information Technology Co., Ltd. ( )",
        "0000fe88-0000-1000-8000-00805f9b34fb" : "Custom UUID of SALTO SYSTEMS S.L.",
        "0000fe89-0000-1000-8000-00805f9b34fb" : "Custom UUID of B&O Play A/S",
        "0000fe8a-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fe8b-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fe8c-0000-1000-8000-00805f9b34fb" : "Custom UUID of TRON Forum",
        "0000fe8d-0000-1000-8000-00805f9b34fb" : "Custom UUID of Interaxon Inc.",
        "0000fe8e-0000-1000-8000-00805f9b34fb" : "Custom UUID of ARM Ltd",
        "0000fe8f-0000-1000-8000-00805f9b34fb" : "Custom UUID of CSR",
        "0000fe90-0000-1000-8000-00805f9b34fb" : "Custom UUID of JUMA",
        "0000fe91-0000-1000-8000-00805f9b34fb" : "Custom UUID of Shanghai Imilab Technology Co.,Ltd",
        "0000fe92-0000-1000-8000-00805f9b34fb" : "Custom UUID of Jarden Safety & Security",
        "0000fe93-0000-1000-8000-00805f9b34fb" : "Custom UUID of OttoQ Inc.",
        "0000fe94-0000-1000-8000-00805f9b34fb" : "Custom UUID of OttoQ Inc.",
        "0000fe95-0000-1000-8000-00805f9b34fb" : "Custom UUID of Xiaomi Inc.",
        "0000fe96-0000-1000-8000-00805f9b34fb" : "Custom UUID of Tesla Motor Inc.",
        "0000fe97-0000-1000-8000-00805f9b34fb" : "Custom UUID of Tesla Motor Inc.",
        "0000fe98-0000-1000-8000-00805f9b34fb" : "Custom UUID of Currant, Inc.",
        "0000fe99-0000-1000-8000-00805f9b34fb" : "Custom UUID of Currant, Inc.",
        "0000fe9a-0000-1000-8000-00805f9b34fb" : "Custom UUID of Estimote",
        "0000fe9b-0000-1000-8000-00805f9b34fb" : "Custom UUID of Samsara Networks, Inc",
        "0000fe9c-0000-1000-8000-00805f9b34fb" : "Custom UUID of GSI Laboratories, Inc.",
        "0000fe9d-0000-1000-8000-00805f9b34fb" : "Custom UUID of Mobiquity Networks Inc",
        "0000fe9e-0000-1000-8000-00805f9b34fb" : "Custom UUID of Dialog Semiconductor B.V.",
        "0000fe9f-0000-1000-8000-00805f9b34fb" : "Custom UUID of Google Inc.",
        "0000fea0-0000-1000-8000-00805f9b34fb" : "Custom UUID of Google Inc.",
        "0000fea1-0000-1000-8000-00805f9b34fb" : "Custom UUID of Intrepid Control Systems, Inc.",
        "0000fea2-0000-1000-8000-00805f9b34fb" : "Custom UUID of Intrepid Control Systems, Inc.",
        "0000fea3-0000-1000-8000-00805f9b34fb" : "Custom UUID of ITT Industries",
        "0000fea4-0000-1000-8000-00805f9b34fb" : "Custom UUID of Paxton Access Ltd",
        "0000fea5-0000-1000-8000-00805f9b34fb" : "Custom UUID of GoPro, Inc.",
        "0000fea6-0000-1000-8000-00805f9b34fb" : "Custom UUID of GoPro, Inc.",
        "0000fea7-0000-1000-8000-00805f9b34fb" : "Custom UUID of UTC Fire and Security",
        "0000fea8-0000-1000-8000-00805f9b34fb" : "Custom UUID of Savant Systems LLC",
        "0000fea9-0000-1000-8000-00805f9b34fb" : "Custom UUID of Savant Systems LLC",
        "0000feaa-0000-1000-8000-00805f9b34fb" : "Custom UUID of Google Inc.",
        "0000feab-0000-1000-8000-00805f9b34fb" : "Custom UUID of Nokia Corporation",
        "0000feac-0000-1000-8000-00805f9b34fb" : "Custom UUID of Nokia Corporation",
        "0000fead-0000-1000-8000-00805f9b34fb" : "Custom UUID of Nokia Corporation",
        "0000feae-0000-1000-8000-00805f9b34fb" : "Custom UUID of Nokia Corporation",
        "0000feaf-0000-1000-8000-00805f9b34fb" : "Custom UUID of Nest Labs Inc.",
        "0000feb0-0000-1000-8000-00805f9b34fb" : "Custom UUID of Nest Labs Inc.",
        "0000feb1-0000-1000-8000-00805f9b34fb" : "Custom UUID of Electronics Tomorrow Limited",
        "0000feb2-0000-1000-8000-00805f9b34fb" : "Custom UUID of Microsoft Corporation",
        "0000feb3-0000-1000-8000-00805f9b34fb" : "Custom UUID of Taobao",
        "0000feb4-0000-1000-8000-00805f9b34fb" : "Custom UUID of WiSilica Inc.",
        "0000feb5-0000-1000-8000-00805f9b34fb" : "Custom UUID of WiSilica Inc.",
        "0000feb6-0000-1000-8000-00805f9b34fb" : "Custom UUID of Vencer Co, Ltd",
        "0000feb7-0000-1000-8000-00805f9b34fb" : "Custom UUID of Facebook, Inc.",
        "0000feb8-0000-1000-8000-00805f9b34fb" : "Custom UUID of Facebook, Inc.",
        "0000feb9-0000-1000-8000-00805f9b34fb" : "Custom UUID of LG Electronics",
        "0000feba-0000-1000-8000-00805f9b34fb" : "Custom UUID of Tencent Holdings Limited",
        "0000febb-0000-1000-8000-00805f9b34fb" : "Custom UUID of adafruit industries",
        "0000febc-0000-1000-8000-00805f9b34fb" : "Custom UUID of Dexcom, Inc.",
        "0000febd-0000-1000-8000-00805f9b34fb" : "Custom UUID of Clover Network, Inc.",
        "0000febe-0000-1000-8000-00805f9b34fb" : "Custom UUID of Bose Corporation",
        "0000febf-0000-1000-8000-00805f9b34fb" : "Custom UUID of Nod, Inc.",
        "0000fec0-0000-1000-8000-00805f9b34fb" : "Custom UUID of KDDI Corporation",
        "0000fec1-0000-1000-8000-00805f9b34fb" : "Custom UUID of KDDI Corporation",
        "0000fec2-0000-1000-8000-00805f9b34fb" : "Custom UUID of Blue Spark Technologies, Inc.",
        "0000fec3-0000-1000-8000-00805f9b34fb" : "Custom UUID of 360fly, Inc.",
        "0000fec4-0000-1000-8000-00805f9b34fb" : "Custom UUID of PLUS Location Systems",
        "0000fec5-0000-1000-8000-00805f9b34fb" : "Custom UUID of Realtek Semiconductor Corp.",
        "0000fec6-0000-1000-8000-00805f9b34fb" : "Custom UUID of Kocomojo, LLC",
        "0000fec7-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fec8-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fec9-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000feca-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fecb-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fecc-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fecd-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fece-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fecf-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fed0-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fed1-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fed2-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fed3-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fed4-0000-1000-8000-00805f9b34fb" : "Custom UUID of Apple, Inc.",
        "0000fed5-0000-1000-8000-00805f9b34fb" : "Custom UUID of Plantronics Inc.",
        "0000fed6-0000-1000-8000-00805f9b34fb" : "Custom UUID of Broadcom Corporation",
        "0000fed7-0000-1000-8000-00805f9b34fb" : "Custom UUID of Broadcom Corporation",
        "0000fed8-0000-1000-8000-00805f9b34fb" : "Custom UUID of Google Inc.",
        "0000fed9-0000-1000-8000-00805f9b34fb" : "Custom UUID of Pebble Technology Corporation",
        "0000feda-0000-1000-8000-00805f9b34fb" : "Custom UUID of ISSC Technologies Corporation",
        "0000fedb-0000-1000-8000-00805f9b34fb" : "Custom UUID of Perka, Inc.",
        "0000fedc-0000-1000-8000-00805f9b34fb" : "Custom UUID of Jawbone",
        "0000fedd-0000-1000-8000-00805f9b34fb" : "Custom UUID of Jawbone",
        "0000fede-0000-1000-8000-00805f9b34fb" : "Custom UUID of Coin, Inc.",
        "0000fedf-0000-1000-8000-00805f9b34fb" : "Custom UUID of Design SHIFT",
        "0000fee0-0000-1000-8000-00805f9b34fb" : "Custom UUID of Anhui Huami Information Technology Co.",
        "0000fee1-0000-1000-8000-00805f9b34fb" : "Custom UUID of Anhui Huami Information Technology Co.",
        "0000fee2-0000-1000-8000-00805f9b34fb" : "Custom UUID of Anki, Inc.",
        "0000fee3-0000-1000-8000-00805f9b34fb" : "Custom UUID of Anki, Inc.",
        "0000fee4-0000-1000-8000-00805f9b34fb" : "Custom UUID of Nordic Semiconductor ASA",
        "0000fee5-0000-1000-8000-00805f9b34fb" : "Custom UUID of Nordic Semiconductor ASA",
        "0000fee6-0000-1000-8000-00805f9b34fb" : "Custom UUID of Silvair, Inc.",
        "0000fee7-0000-1000-8000-00805f9b34fb" : "Custom UUID of Tencent Holdings Limited",
        "0000fee8-0000-1000-8000-00805f9b34fb" : "Custom UUID of Quintic Corp.",
        "0000fee9-0000-1000-8000-00805f9b34fb" : "Custom UUID of Quintic Corp.",
        "0000feea-0000-1000-8000-00805f9b34fb" : "Custom UUID of Swirl Networks, Inc.",
        "0000feeb-0000-1000-8000-00805f9b34fb" : "Custom UUID of Swirl Networks, Inc.",
        "0000feec-0000-1000-8000-00805f9b34fb" : "Custom UUID of Tile, Inc.",
        "0000feed-0000-1000-8000-00805f9b34fb" : "Custom UUID of Tile, Inc.",
        "0000feee-0000-1000-8000-00805f9b34fb" : "Custom UUID of Polar Electro Oy",
        "0000feef-0000-1000-8000-00805f9b34fb" : "Custom UUID of Polar Electro Oy",
        "0000fef0-0000-1000-8000-00805f9b34fb" : "Custom UUID of Intel",
        "0000fef1-0000-1000-8000-00805f9b34fb" : "Custom UUID of CSR",
        "0000fef2-0000-1000-8000-00805f9b34fb" : "Custom UUID of CSR",
        "0000fef3-0000-1000-8000-00805f9b34fb" : "Custom UUID of Google Inc.",
        "0000fef4-0000-1000-8000-00805f9b34fb" : "Custom UUID of Google Inc.",
        "0000fef5-0000-1000-8000-00805f9b34fb" : "Custom UUID of Dialog Semiconductor GmbH",
        "0000fef6-0000-1000-8000-00805f9b34fb" : "Custom UUID of Wicentric, Inc.",
        "0000fef7-0000-1000-8000-00805f9b34fb" : "Custom UUID of Aplix Corporation",
        "0000fef8-0000-1000-8000-00805f9b34fb" : "Custom UUID of Aplix Corporation",
        "0000fef9-0000-1000-8000-00805f9b34fb" : "Custom UUID of PayPal, Inc.",
        "0000fefa-0000-1000-8000-00805f9b34fb" : "Custom UUID of PayPal, Inc.",
        "0000fefb-0000-1000-8000-00805f9b34fb" : "Custom UUID of Telit Wireless Solutions (Formerly Stollmann E+V GmbH)",
        "0000fefc-0000-1000-8000-00805f9b34fb" : "Custom UUID of Gimbal, Inc.",
        "0000fefd-0000-1000-8000-00805f9b34fb" : "Custom UUID of Gimbal, Inc.",
        "0000fefe-0000-1000-8000-00805f9b34fb" : "Custom UUID of GN ReSound A/S",
        "0000feff-0000-1000-8000-00805f9b34fb" : "Custom UUID of GN Netcom",

        # Non-Standard public, ordered by UUID ------------------------------------------------------------------------

        "0000ffe0-0000-1000-8000-00805f9b34fb" : "HM-10 UART Service",
        "0000ffe1-0000-1000-8000-00805f9b34fb" : "HM-10 UART RX/TX",

        # Posture Sensing Service
        # "0000ffe0-0000-1000-8000-00805f9b34fb" : "Posture Sensing Service", # collision with HM-10
        "0000ffe5-0000-1000-8000-00805f9b34fb" : "Control Service",
        "0000ffe9-0000-1000-8000-00805f9b34fb" : "UART TX",

        "0000fff0-0000-1000-8000-00805f9b34fb" : "ISSC Transparent Service",
        "0000fff1-0000-1000-8000-00805f9b34fb" : "ISSC Transparent RX",
        "0000fff2-0000-1000-8000-00805f9b34fb" : "ISSC Transparent TX",

        "0000fff6-0000-1000-8000-00805f9b34fb" : "RX",
        "0000fff7-0000-1000-8000-00805f9b34fb" : "TX",

        # 16 Bit UUIDs For SDOs, ordered by UUID ----------------------------------------------------------------------
        "0000fffc-0000-1000-8000-00805f9b34fb" : "AirFuel Alliance Wireless Power Transfer Service",
        "0000fffd-0000-1000-8000-00805f9b34fb" : "Fast IDentity Online Alliance Universal Second Factor Authenticator Service",
        "0000fffe-0000-1000-8000-00805f9b34fb" : "AirFuel Alliance Wireless Power Transfer Service",

        # Nodric Service
        "6e400001-b5a3-f393-e0a9-e50e24dcca9e" : "Nodric UART Service",
        "6e400002-b5a3-f393-e0a9-e50e24dcca9e" : "Nodric UART Rx Char",
        "6e400003-b5a3-f393-e0a9-e50e24dcca9e" : "Nodric UART Tx Char",
        "00001530-1212-efde-1523-785feabcd123" : "Nodric DFU Service",
        "00001531-1212-efde-1523-785feabcd123" : "Nodric DFU Control Point",
        "00001532-1212-efde-1523-785feabcd123" : "Nodric DFU Packet",

        # Read Bear
        "713d0000-503e-4c75-ba94-3148f18d941e" : "RedBearLab Service",
        "713d0002-503e-4c75-ba94-3148f18d941e" : "RedBearLab RX Service",
        "713d0003-503e-4c75-ba94-3148f18d941e" : "RedBearLab TX Service",

        # RedBear Beacon B1
        "b0702881-a295-a8ab-f734-031a98a512d" : "RedBear B1 iBeacon",
        "b0702882-a295-a8ab-f734-031a98a512d" : "RedBear B1 Major ID",
        "b0702883-a295-a8ab-f734-031a98a512d" : "RedBear B1 Minor ID",
        "b0702884-a295-a8ab-f734-031a98a512d" : "RedBear B1 Measured Power",
        "b0702885-a295-a8ab-f734-031a98a512d" : "RedBear B1 LED Switch ",
        "b0702886-a295-a8ab-f734-031a98a512d" : "RedBear B1 Advertising Interval",
        "b0702887-a295-a8ab-f734-031a98a512d" : "RedBear B1 Output Power",
        "b0702888-a295-a8ab-f734-031a98a512d" : "RedBear B1 Firmware Version",

        # ISSC dual mode
        "49535343-fe7d-4ae5-8fa9-9fafd205e455" : "ISSC Proprietary Service",
        "49535343-1e4d-4bd9-ba61-23c647249616" : "ISSC Transparent TX",
        "49535343-8841-43f4-a8d4-ecbe34729bb3" : "ISSC Transparent RX",
        "49535343-6daa-4d02-abf6-19569aca69fe" : "ISSC Update Connection Parameter",
        "49535343-6daa-4d02-abf6-19569aca69fe" : "ISSC Update Connection Parameter",
        "49535343-aca3-481c-91ec-d85e28a60318" : "ISSC Air Patch",

        # Stollmann Terminal IO
        "0000fefb-0000-1000-8000-00805f9b34fb" : "Stollmann Terminal IO Service",
        "00000001-0000-1000-8000-008025000000" : "Stollmann UART RX",
        "00000002-0000-1000-8000-008025000000" : "Stollmann UART TX",
        "00000004-0000-1000-8000-008025000000" : "Stollmann Credits UART RX",

        # Apple Notification Center Service
        "7905f431-b5ce-4e99-a40f-4b1e122d00d0" : "Apple Notification Center Service",
        "9fbf120d-6301-42d9-8c58-25e699a21dbd" : "Notification Source",
        "69d1d8f3-45e1-49a8-9821-9bbdfdaad9d9" : "Control Point UUID",
        "22eac6e9-24d6-4bb5-be44-b36ace7c7bfb" : "Data Source",

        # Laird BL600 Virtual Serial Port Service
        "569a1101-b87f-490c-92cb-11ba5ea5167c" : "BL600 vSP Service",
        "569a2000-b87f-490c-92cb-11ba5ea5167c" : "TX FIFO",
        "569a2001-b87f-490c-92cb-11ba5ea5167c" : "RX FIFO",
        "569a2002-b87f-490c-92cb-11ba5ea5167c" : "Modem Out",
        "569a2003-b87f-490c-92cb-11ba5ea5167c" : "Modem In",

        # Oregon Scientific IDT EM221
        "905e180a-81e9-4796-9b75-b95cf5e30c0b" : "Device Information",
        "905e2a24-81e9-4796-9b75-b95cf5e30c0b" : "Model Number String",
        "905e2a26-81e9-4796-9b75-b95cf5e30c0b" : "Firmware Revision String",
        "905e2a27-81e9-4796-9b75-b95cf5e30c0b" : "Hardware Revision String",
        "905e2a29-81e9-4796-9b75-b95cf5e30c0b" : "Manufacturer Name String",
        "905e180f-81e9-4796-9b75-b95cf5e30c0b" : "Battery Service",
        "905e2a19-81e9-4796-9b75-b95cf5e30c0b" : "Battery Level",
        "905efe00-81e9-4796-9b75-b95cf5e30c0b" : "Oregon Scientific Service",
        "905e8e01-81e9-4796-9b75-b95cf5e30c0b" : "Oregon Scientific Characteristic",
        "905e8e02-81e9-4796-9b75-b95cf5e30c0b" : "Oregon Scientific Characteristic",
        "905e8e03-81e9-4796-9b75-b95cf5e30c0b" : "Oregon Scientific Characteristic",
        "905e8e30-81e9-4796-9b75-b95cf5e30c0b" : "Oregon Scientific Characteristic",
        "905e8e34-81e9-4796-9b75-b95cf5e30c0b" : "Oregon Scientific Characteristic",
        "905e8e40-81e9-4796-9b75-b95cf5e30c0b" : "Oregon Scientific Characteristic",
}
