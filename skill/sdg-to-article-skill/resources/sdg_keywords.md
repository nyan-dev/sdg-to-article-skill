# INTI SDG Keywords

**Source:** INTI International University - SDG Goals Keywords as of 060625.docx  
**INTI revision:** Revised on 06th June 2025  
**Canonical data:** `sdg_keywords.csv` (1634 terms, 17 goals)  
**Rebuilt:** 2026-10-15

## How to use these

Write every keyword wrapped in **curly braces**, regardless of goal:
`{food security}`, `{resource efficiency}`.

The INTI source file is internally inconsistent - Goals 1-12 store
keywords as `{keyword}` but Goals 13-17 store them as `(keyword)`.
This skill normalises everything to curly braces. See SKILL.md for the
rationale and the residual risk if INTI's checker is doing exact
matching against the original delimiters.

**Copy keywords verbatim.**

- A trailing `*` is an INTI stem marker (`coast*` covers coastal). Keep it.
- A `?` inside a word (`fertili?er`, `democrati?ation`) is lost encoding in
  INTI's own file. Reproduce as-is rather than correcting it.
- Do not invent, pluralise, reword, or translate a keyword.

---

## SDG 1 - No poverty

**Official title:** No poverty  
**Keywords:** 27 (INTI stores as curly; write as curly)

```
{financial aid and poverty}, {financial aid and poor}, {financial aid and north-south divide}, {financial development and poverty}, {social protection and access}, {safety net and poor}, {safety net and vulnerable}, {economic resource and access}, {economic resources and access}, {extreme poverty}, {poverty alleviation}, {poverty eradication}, {poverty reduction}, {international poverty line}, {financial empowerment}, {distributional effect}, {distributional effects}, {child labor}, {child labour}, {development aid}, {social protection}, {social protection system}, {resilience of the poor}, {food bank}, {food banks}, {microfinance}, {micro-financ}
```

---

## SDG 2 - Zero hunger

**Official title:** Zero hunger  
**Keywords:** 44 (INTI stores as curly; write as curly)

```
{smallholder and farm}, {smallholder and forestry}, {smallholder and pastoral}, {smallholder and agriculture}, {smallholder and fishery}, {smallholder and food producer}, {smallholder and food producers}, {agriculture and potassium}, {GMO and food}, {food security and genetic diversity}, {food market and restriction}, {food market and tariff}, {food market and access}, {food market and north south divide}, {food market and development governance}, {land tenure rights}, {malnourish}, {malnutrition}, {undernourish}, {undernutrition}, {agricultural production}, {agricultural productivity}, {agricultural practices}, {agricultural management}, {food production}, {food productivity}, {food security}, {food insecurity}, {land right}, {land rights}, {land reform}, {land reforms}, {resilient agricultural practices}, {fertili?er}, {food nutrition improvement}, {hidden hunger}, {genetically modified food}, {agroforestry practices}, {agroforestry management}, {agricultural innovation}, {food governance}, {food supply chain}, {food value chain}, {food commodity market}
```

> Contains `?` where an accented character was lost. Reproduce as-is: `fertili?er`

---

## SDG 3 - Good health and well-being

**Official title:** Good health and well-being  
**Keywords:** 99 (INTI stores as curly; write as curly)

```
{human health*}, {human disease*}, {human illness*}, {human medicine*}, {human mortality}, {battered child syndrome}, {cardiovascular disease}, {cardiovascular diseases}, {chagas}, {child abuse}, {child neglect}, {child well-being index}, {youth well-being index}, {child wellbeing index}, {youth wellbeing index}, {water-borne disease}, {water-borne diseases}, {water borne disease}, {water borne diseases}, {tropical disease}, {tropical diseases}, {chronic respiratory disease}, {chronic respiratory diseases}, {infectious disease}, {infectious diseases}, {sexually-transmitted disease}, {sexually transmitted disease}, {sexually-transmitted diseases}, {sexually transmitted diseases}, {communicable disease}, {communicable diseases}, {AIDS}, {HIV}, {human immunodeficiency virus}, {tuberculosis}, {malaria}, {hepatitis}, {polio*}, {vaccin*}, {cancer*}, {diabet*}, {maternal mortality}, {child mortality}, {childbirth complications}, {neonatal mortality}, {neo-natal mortality}, {premature mortality}, {infant mortality}, {quality adjusted life year}, {maternal health}, {preventable death}, {preventable deaths}, {tobacco control}, {substance abuse}, {drug abuse}, {tobacco use}, {alcohol use}, {substance addiction}, {drug addiction}, {tobacco addiction}, {alcoholism}, {suicid*}, {postnatal depression}, {post-natal depression}, {zika virus}, {dengue}, {schistosomiasis}, {sleeping sickness}, {ebola}, {mental health}, {mental disorder}, {mental illness}, {mental illnesses}, {measles}, {neglected disease}, {neglected diseases}, {diarrhea}, {diarrhoea}, {cholera}, {dysentery}, {typhoid fever}, {traffic accident}, {traffic accidents}, {healthy lifestyle}, {life expectancy}, {life expectancies}, {health policy}, {health system access}, {health system accessible}, {health risk}, {health risks}, {inclusive health}, {obesity}, {social determinants of health}, {psychological harm}, {psychological wellbeing}, {psychological well-being}, {psychological well being}, {public health}
```

---

## SDG 4 - Quality education

**Official title:** Quality education  
**Keywords:** 55 (INTI stores as curly; write as curly)

```
{development aid and teacher training}, {learning opportunities and gender disparities}, {learning opportunities and empowerment}, {learning opportunity and gender disparities}, {learning opportunity and empowerment}, {poverty trap and schooling}, {schooling and gender disparities}, {schooling and ethnic disparities}, {schooling and racial disparities}, {educational reform and developing countries}, {developing countries and school effects}, {teacher training and developing countries}, {school}, {education}, {educational}, {school attendance}, {school enrollment}, {school enrolment}, {inclusive education}, {educational inequality}, {education quality}, {educational enrolment}, {educational enrollment}, {adult literacy}, {numeracy rate}, {educational environment}, {educational access}, {early childhood education}, {basic education}, {affordable education}, {educational financial aid}, {school safety}, {safety in school}, {youth empowerment}, {women empowerment}, {equal opportunities}, {child labour}, {child labor}, {discriminatory}, {educational gap}, {special education needs}, {inclusive education system}, {education exclusion}, {education dropouts}, {global citizenship}, {sustainable development education}, {environmental education}, {education policy}, {educational policies}, {international education}, {education reform}, {educational governance}, {education expenditure}, {foreign aid}, {teacher attrition}
```

---

## SDG 5 - Gender equality

**Official title:** Gender equality  
**Keywords:** 80 (INTI stores as curly; write as curly)

```
{access and family planning services}, {women and violence}, {girl* and violence}, {unpaid work and gender inequality}, {unpaid care work and gender inequality}, {access and reproductive healthcare}, {equality and sexual rights}, {equality and reproductive rights}, {equality and divorce rights}, {foreign aid and women’s empowerment}, {gender inequality}, {gender equality}, {employment equity}, {gender wage gap}, {female labor force participation}, {female labour force participation}, {women labor force participation}, {women labour force participation}, {womens' employment}, {female employment}, {women's unemployment}, {female unemployment}, {forced marriage}, {child marriage}, {forced marriages}, {child marriages}, {occupational segregation}, {women's empowerment}, {girls' empowerment}, {female empowerment}, {female genital mutilation}, {female genital cutting}, {domestic violence}, {sexual violence}, {women's political participation}, {female political participation}, {female managers}, {women in leadership}, {female leadership}, {intra-household allocation}, {honour killing}, {honor killing}, {honour killings}, {honor killings}, {antiwomen}, {anti-women}, {feminism}, {misogyny}, {female infanticide}, {female infanticides}, {human trafficking}, {forced prostitution}, {women's rights}, {gender injustice}, {gender injustices}, {gender discrimination}, {gender disparities}, {gender gap}, {female exploitation}, {household equity}, {women’s underrepresentation}, {female entrepreneurship}, {female ownership}, {women’s economic development}, {women’s power}, {gender-responsive budgeting}, {gender quota}, {gender segregation}, {gender-based violence}, {gender participation}, {female politician}, {female leader}, {contraceptive behaviour}, {women’s autonomy}, {agrarian feminism}, {microfinance}, {women’s livelihood}, {women’s ownership}, {female smallholder}, {gender mainstreaming}
```

---

## SDG 6 - Clean water and sanitation

**Official title:** Clean water and sanitation  
**Keywords:** 60 (INTI stores as curly; write as curly)

```
{Safe and water access}, {Safe and drinking water}, {Clean and drinking water}, {Clean and water source}, {Water and sanitation and hygiene}, {Water and sanitation & hygiene}, {Water and quality}, {Water and resource}, {Water and water availability}, {Water and water-use efficiency}, {Water and water supply}, {Water and water supplies}, {Water and clean water}, {Water and hygienic toilet}, {Water and hygienic toilets}, {Water and antifouling membrane}, {Water and antifouling membranes}, {Water and anti-fouling membrane}, {Water and anti-fouling membranes}, {Water and water management}, {Water and aquatic toxicology}, {Water and water toxicology}, {Water and aquatic ecotoxicology}, {Water and water ecotoxicology}, {Freshwater and water quality}, {Fresh water and water quality}, {Freshwater and pollutant}, {Freshwater and pollution}, {Freshwater and contamina}, {Freshwater and water security}, {Freshwater and water shortage}, {Waste water and treatment}, {Wastewater and treatment}, {Water and water conservation}, {Water and water footprint}, {Water and water infrastructure}, {Water and water pollution}, {Water and water purification}, {Water and water use}, {Water and water uses}, {Water and sanit}, {Water and sewer*}, {Water and ecosystem and protection of}, {Water and ecosystem and endocrine disruptor}, {Water and ecosystem and endocrine disruptors}, {Water and water management and pollution remediation}, {Water and water management and pollutant removal}, {Groundwater and freshwater}, {Ground water and freshwater}, {Ground-water and freshwater}, {Water pollution and waste water and treatment}, {Water pollution and wastewater and treatment}, {Freshwater availability}, {Fresh water availability}, {Water scarcity}, {Open defecation}, {Blue water}, {Green water}, {Grey water}, {Black water}
```

---

## SDG 7 - Affordable and clean energy

**Official title:** Affordable and clean energy  
**Keywords:** 54 (INTI stores as curly; write as curly)

```
{photochemistry and renewable energy}, {foreign development aid and renewable energy}, {official development assistance and electricity}, {energy development and developing countries}, {energy efficiency}, {energy consumption}, {energy transition}, {clean energy technology}, {energy equity}, {energy justice}, {energy poverty}, {energy policy}, {renewable}, {2000 Watt society}, {smart micro-grid}, {smart grid}, {smart microgrid}, {smart micro-grids}, {smart grids}, {smart microgrids}, {smart meter}, {smart meters}, {affordable electricity}, {electricity consumption}, {reliable electricity}, {clean fuel}, {clean cooking fuel}, {fuel poverty}, {life-cycle assessment}, {life cycle assessment}, {life-cycle assessments}, {life cycle assessments}, {photovoltaic}, {photocatalytic water splitting}, {hydrogen production}, {water splitting}, {lithium-ion batteries}, {lithium-ion battery}, {heat network}, {district heat}, {district heating}, {residential energy consumption}, {domestic energy consumption}, {energy security}, {rural electrification}, {energy ladder}, {energy access}, {energy conservation}, {low-carbon society}, {hybrid renewable energy system}, {hybrid renewable energy systems}, {fuel switching}, {energy governance}, {developing countries}
```

---

## SDG 8 - Decent work and economic growth

**Official title:** Decent work and economic growth  
**Keywords:** 90 (INTI stores as curly; write as curly)

```
{economic growth}, {economic development policy}, {employment policy}, {inclusive economic growth}, {sustainable growth}, {economic development}, {economic globalization}, {economic globalisation}, {economic productivity}, {low-carbon economy}, {inclusive growth}, {microfinanc}, {micro-financ}, {micro-credit*}, {microcredit*}, {equal income}, {equal wages}, {decent job}, {decent jobs}, {quality job}, {quality jobs}, {job creation}, {full employment}, {employment protection}, {informal employment}, {precarious employment}, {unemployment}, {precarious job}, {precarious jobs}, {microenterprise*}, {micro-enterprise*}, {small enterprise}, {medium enterprise}, {small enterprises}, {medium enterprises}, {small entrepreneur}, {starting entrepreneur}, {medium entrepreneur}, {small entrepreneurs}, {medium entrepreneurs}, {starting entrepreneurs}, {social entrepreneurship}, {safe working environment}, {labor market institution}, {labor market institutions}, {labour market institution}, {labour market institutions}, {forced labour}, {forced labor}, {child labour}, {child labor}, {labour right}, {labor right}, {labour rights}, {labor rights}, {modern slavery}, {human trafficking}, {child soldier}, {child soldiers}, {global jobs}, {living wage}, {minimum wage}, {circular economy}, {inclusive economy}, {rural economy}, {Foreign Development Investment}, {Aid for Trade}, {trade unions}, {trade union}, {working poor}, {Not in Education, Employment, or Training}, {carbon offset}, {carbon offsetting}, {carbon offsets}, {offset project}, {offset projects}, {economic diversification}, {material footprint}, {resource efficiency}, {cradle to cradle and economy}, {economic decoupling}, {labour market disparities}, {sustainable tourism}, {ecotourism}, {community-based tourism}, {tourism employment}, {sustainable tourism policy}, {financial access}, {financial inclusion}, {access to banking}
```

---

## SDG 9 - Industry, innovation and infrastructure

**Official title:** Industry, innovation and infrastructure  
**Keywords:** 43 (INTI stores as curly; write as curly)

```
{industrial growth}, {industrial diversification}, {infrastructural development}, {infrastructural investment}, {infrastructure investment}, {public infrastructure}, {resilient infrastructure}, {transborder infrastructure}, {public infrastructures}, {resilient infrastructures}, {transborder infrastructures}, {industrial emissions and mitigation}, {industrial waste management}, {industrial waste treatment}, {traffic congestion}, {microenterprise}, {micro-enterprise}, {small enterprise}, {medium enterprise}, {small enterprises}, {medium enterprises}, {small entrepreneur}, {medium entrepreneur}, {small entrepreneurs}, {medium entrepreneurs}, {value chain management}, {broadband access and developing countries}, {manufacturing innovation}, {manufacturing investment}, {sustainable transportation}, {accessible transportation}, {transportation services}, {inclusive transportation}, {R&D investment}, {green product}, {green products}, {sustainable manufacturing}, {cradle to cradle and industry}, {closed loop supply chain}, {industrial and innovation}, {process innovation}, {product innovation}, {inclusive innovation}
```

---

## SDG 10 - Reduced inequalities

**Official title:** Reduced inequalities  
**Keywords:** 34 (INTI stores as curly; write as curly)

```
{equality and economic}, {equality and financial}, {equality and socio-economic}, {inequality and economic}, {inequality and financial}, {inequality and socio-economic}, {economic reform policy}, {economic reform policies}, {political inclusion}, {social protection policy}, {social protection policies}, {immigration}, {emigration}, {foreign direct investment}, {development gap}, {development gaps}, {migrant remittance}, {responsible migration}, {migration policy}, {migration policies}, {north-south divide}, {developing and tariffs}, {developing and tariff}, {developing and zero-tariff}, {developing and duty-free access}, {social exclusion}, {economic marginalization}, {income inequality}, {discriminatory law}, {discriminatory policies}, {discriminatory policy}, {economic empowerment}, {economic transformation}, {global market and empowerment}
```

---

## SDG 11 - Sustainable cities and communities

**Official title:** Sustainable cities and communities  
**Keywords:** 55 (INTI stores as curly; write as curly)

```
{city}, {cities}, {human settlement}, {human settlements}, {urban}, {metropolis}, {town}, {municipal*}, {gentrification}, {congestion}, {transportation}, {public transport}, {housing}, {slum*}, {Sendai Framework}, {Disaster Risk Reduction}, {DRR}, {smart city}, {smart cities}, {resilient building}, {resilient buildings}, {sustainable building}, {sustainable buildings}, {building design}, {buildings design}, {urbanization}, {zero energy building}, {zero energy buildings}, {zero-energy building}, {zero-energy buildings}, {basic service}, {basic services}, {governance}, {citizen participation}, {collaborative planning}, {participatory planning}, {inclusiveness}, {cultural heritage}, {natural heritage}, {UNESCO}, {disaster}, {ecological footprint}, {environmental footprint}, {waste}, {pollution}, {pollutant*}, {waste water}, {recycling}, {circular economy}, {air quality}, {green space}, {green spaces}, {nature inclusive}, {nature inclusive building}, {nature inclusive buildings}
```

---

## SDG 12 - Responsible consumption and production

**Official title:** Responsible consumption and production  
**Keywords:** 53 (INTI stores as curly; write as curly)

```
{environmental pollution}, {hazardous waste}, {hazardous chemical}, {hazardous chemicals}, {toxic chemical}, {toxic chemicals}, {chemical pollution}, {ozone depletion}, {pesticide pollution}, {pesticide stress}, {pesticide reduction}, {life cycle assessment}, {life cycle analysis}, {life cycle analyses}, {life-cycle analysis}, {life-cycle analyses}, {low carbon economy}, {low-carbon economy}, {environmental footprint}, {material footprint}, {harvest efficiency}, {solid waste}, {waste generation}, {corporate social responsibility}, {corporate sustainability}, {consumer behavior}, {consumer behaviors}, {consumer behaviour}, {consumer behaviours}, {waste recycling}, {resource recycling}, {resource reuse}, {biobased economy}, {zero waste}, {sustainability label}, {sustainability labelling}, {global resource extraction}, {material flow accounting}, {societal metabolism}, {food spill}, {resource spill}, {resource efficiency}, {sustainable food consumption}, {green consumption}, {sustainable supply chain}, {circular economy}, {cradle to cradle}, {sustainable procurement}, {sustainable tourism}, {fossil-fuel subsidies}, {fossil-fuel expenditure}, {consumption (resource use or spill)}, {production (resource use or spill)}
```

---

## SDG 13 - Climate action

**Official title:** Climate action  
**Keywords:** 80 (INTI stores as paren; write as curly)

```
{climate action}, {climate adaptation}, {climate change}, {climate capitalism}, {ipcc}, {climate effect}, {climate equity}, {climate feedback}, {climate finance}, {climate change financing}, {climate forcing}, {climate governance}, {climate impact}, {climate investment}, {climate justice}, {climate mitigation}, {climate model}, {climate models}, {climate modeling}, {climate modelling}, {climate policy}, {climate policies}, {climate risk}, {climate risks}, {climate services}, {climate service}, {climate prediction}, {climate predictions}, {climate signal}, {climate signals}, {climate tipping point}, {climate variation}, {climate variations}, {ecoclimatology}, {eco-climatology}, {Green Climate Fund}, {regional climate}, {regional climates}, {urban climate}, {urban climates}, {climate}, {adaptive management}, {awareness}, {bioeconomy}, {carbon}, {decision-making}, {disaster risk reduction}, {environmental education}, {sustainable development education}, {energy conservation}, {emission*}, {extreme}, {food chain}, {food chains}, {framework}, {hazard*}, {island*}, {land use}, {megacit*}, {consumption}, {production}, {small island developing states}, {anthropocene}, {atmospher*}, {clean development mechanism}, {glacier retreat}, {warming}, {greenhouse}, {ice-ocean interaction}, {ice-ocean interactions}, {nitrogen cycle}, {nitrogen cycles}, {ocean acidification}, {radiative forcing}, {sea ice}, {sea level}, {sea levels}, {thermal expansion}, {unfccc}, {ozone}
```

---

## SDG 14 - Life below water

**Official title:** Life below water  
**Keywords:** 294 (INTI stores as paren; write as curly)

> Generated cross-product: 294 listed terms = 7 prefixes x 42 concepts (100% coverage). A valid keyword is any prefix + `and` + any concept.

**Prefixes:** coast* | mangrove | marine | ocean | oceans | sea | seas

**Concepts:** acidification and seawater | artisanal fishers | biogeochemical cycle | biogeochemical cycles | coastal ecotourism | coastal habitat | coastal habitats | coastal management | community based conservation | community-based conservation | coral bleach | coral bleaching | destructive fishing | ecotourism | eutrophicat* | fisheries | fisheries rights | fishery | ice-ocean | local fisheries | marine conservation | marine debris | marine economy | marine land slide | marine policy | marine pollution | marine protected area | marine protected areas | marine quota | nutrient runoff | ocean acidification | oceanic circulation model | oceanic circulation modeling | oceanic circulation modelling | oceanic circulation models | overfishing | small Island development states | species richness | sustainable yield | traditional ecological knowledge | water cycle | water cycles

---

## SDG 15 - Life on land

**Official title:** Life on land  
**Keywords:** 288 (INTI stores as paren; write as curly)

> Generated cross-product: 288 listed terms = 4 prefixes x 71 concepts (100% coverage). A valid keyword is any prefix + `and` + any concept.

**Prefixes:** freshwater | inland | land | terrestrial

**Concepts:** LULUCF | Nagoya Protocol on Access to Genetic Resources | REDD | Red List Index | Red List species | alien species | bio-econom* | biodivers* | biodiversity-inclusive | bioeconom* | biological invasion | biological production | community based conservation | community-based conservation | deforest* | desertif* | drought | dryland* | earth system | eco-system* | ecological resilience | ecosystem* | ecotourism | endangered species | extinction risk | extinction risks | extinction wave | fire-fallow cultivation | forest | forest auditing | forest certification | forest management | forest stewardship council | genetic resources | habitat fragmentation | habitat loss | habitat restoration | human-wildlife conflict | illegal logging | invasive species | land conservation | land degradation | land restoration | land use | land uses | mountain vegetation | mountain* | mountainous cover | poach* | protected area | protected areas | rainforest alliance | silviculture | slash-and-burn | soil degradation | soil restoration | species richness | sustainable land management | threatened species | timber harvest | tree cover | trophic cascade | trophic level | trophic web | wetland* | wildlife market | wildlife markets | wildlife product | wildlife products | wildlife traffic | wildlife trafficking

---

## SDG 16 - Peace, justice and strong institutions

**Official title:** Peace, justice and strong institutions  
**Keywords:** 96 (INTI stores as paren; write as curly)

```
{actual innocence}, {false confession}, {armed conflict}, {armed conflicts}, {civil conflict}, {civil conflicts}, {war conflict}, {war warfare}, {war democracy}, {war Geneva Convention}, {war treaty}, {war peace}, {peacekeeping}, {corruption institution}, {corruption public official}, {corruption government}, {corruption bribery}, {corruption conflict}, {crime}, {crimes}, {criminal}, {democratic deficit}, {democrati?ation institutional}, {democrati?ation conflict}, {democrati?ation decision-making}, {democrati?ation society}, {democrati?ation politics}, {democrati?ation financial aid}, {ethnic conflict}, {ethnic conflicts}, {exoneration}, {genocid*}, {homicid*}, {murder*}, {human trafficking}, {criminal justice system}, {justice system}, {arbitrary justice}, {refugee*}, {terroris*}, {violence}, {torture}, {effective rule of law}, {arms flow}, {transparent institution}, {transparent institutions}, {good governance}, {legal identity for all}, {freedom of information}, {human rights institution}, {human rights activists}, {fundamental freedom}, {fundamental freedoms}, {violent conflict}, {violent conflicts}, {peaceful society}, {effective institution}, {effective institutions}, {accountable institution}, {accountable institutions}, {inclusive institution}, {inclusive institutions}, {child abuse}, {arbitrary detention}, {unsentenced detention}, {judicial system}, {criminal tribunal}, {inclusive society}, {inclusive societies}, {responsive institution}, {responsive institutions}, {fair society}, {fair societies}, {legal remedy}, {legal remedies}, {independence of judiciary}, {independent judiciary}, {separation of powers}, {extremism}, {war crime}, {peaceful society}, {organized crime}, {illicit transfer}, {illicit money}, {arms trafficking}, {cybercrime}, {insurgence}, {democratic institution}, {political instability}, {political decision-making responsive}, {political decision-making inclusive}, {political decision-making participatory}, {political decision-making representative}, {Aarhus Convention}, {press freedom}, {freedom of speech}
```

> Contains `?` where an accented character was lost. Reproduce as-is: `democrati?ation institutional`, `democrati?ation conflict`, `democrati?ation decision-making`, `democrati?ation society`, `democrati?ation politics`, `democrati?ation financial aid`

---

## SDG 17 - Partnerships for the Goals

**Official title:** Partnerships for the goals  
**Keywords:** 182 (INTI stores as paren; write as curly)

```
{tax transition}, {tax system}, {tax policy}, {tax policies}, {excise duty}, {excise duties}, {excise tax}, {excise taxes}, {revenue collection}, {cycle of money}, {slippery slope framework}, {tax morale}, {tax administration}, {tax avoidance}, {business tax}, {corporate tax}, {inheritance tax}, {international tax}, {shadow economy}, {tax behaviour}, {tax efficiency}, {value added tax}, {fiscal policy}, {monetary policy}, {informal economy}, {informal sector}, {envelope wage}, {underground economy}, {underground sector}, {informal employment}, {undeclared work}, {underdeclared employment}, {hidden economy}, {black economy}, {money laundering}, {tax evasion}, {VAT gap}, {VAT fraud}, {currency demand approach}, {base erosion and profit shifting}, {BEPS}, {transfer pricing}, {tax treaty}, {tax treaties}, {taxation of capital}, {endogenous growth}, {public capital}, {official development assistance}, {ODA}, {development assistance}, {foreign aid}, {development aid}, {development cooperation}, {international development cooperation}, {global civil society}, {international cooperation}, {international public finance}, {shared prosperity}, {bilateral aid}, {foreign direct investment}, {foreign investment}, {developing}, {belt and road initiative}, {cross border cooperation}, {cross border collaboration}, {non government development organization}, {NGDO}, {north-south cooperation}, {north-south partnerships}, {north-south collaboration}, {north-south research partnerships}, {developing country}, {poor country}, {emerging country}, {developing world}, {developing nation}, {developing state}, {developing states}, {low income country}, {middle income country}, {low income nation}, {middle income nation}, {low income state}, {middle income state}, {least developed country}, {least developed nation}, {least developed state}, {promotion regime}, {investment regime}, {foreign investment}, {foreign trade}, {trade relations}, {trade regime}, {trade promotion}, {international investment}, {international investment agreement}, {trade and investment}, {trade}, {investment}, {capital flight}, {FDI}, {WTO}, {WTO accession}, {FDI inflow}, {trade rule}, {international trade}, {international trade law}, {trade openness}, {trade shock}, {ISDS}, {RCEP}, {bilateral investment treaty}, {investment treaty}, {economic statecraft}, {world trade organisation}, {economic integration}, {economic development board}, {economic cooperation}, {EDB}, {trade liberalisation}, {import competition}, {cross-border e-commerce}, {free trade agreement}, {regional integration}, {NAFTA}, {north american free trade agreement}, {debt sustainability}, {debt relief}, {debt restructuring}, {debt structuring}, {sovereign default}, {sovereign debt restructuring}, {sovereign debt structuring}, {Paris Club}, {Highly Indebted Poor Countries Initiative}, {HIPC Initiative}, {HIPC}, {debt}, {public debt}, {external debt}, {foreign debt}, {vulture fund}, {Collective Action Clause}, {Debt Collection}, {Relief Provision}, {fiscal sustainability}, {insolvency}, {financial distress}, {debt maturity}, {fiscal rule}, {debt crisis}, {fiscal space}, {fiscal recovery}, {sovereign bond}, {government debt}, {debt overhang}, {Fiscal Reaction Function}, {Sovereign credit risk}, {primary balance}, {debt management}, {domestic debt}, {debt dynamic}, {international debt}, {scheme of arrangement}, {exit consent}, {borrower}, {sovereign risk}, {pari passu}, {debt service}, {debt reduction}, {public finance}, {global health}, {international cooperation}, {international collaboration}, {international partnership}, {regional cooperation}, {regional collaboration}, {regional partnership}, {climate change}, {global warming}, {ecology}, {green development}
```

---
