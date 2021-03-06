# -*- encoding: utf-8 -*-
JSONLOC = "C:\\opengeo\\webapps\\DiplomacyExplorer2\\jsonFile\\jsonLayerFile.txt"

jsoninfo = {
			"keyTP":{
				'categoryName': "Trade Promotion",
				'categoryDescription': "<div><h7 class='lorem'>The Department of State’s Bureau of Economic, Energy and Business Affairs is devoted to providing technical expertise in regional and bilateral trade negotiations including labor, environment, services, government procurement, trade remedies, and trade capacity building. This bureau helps to oversee programs such as AGOA.</h7></div>",
				'layers':{
					'geoJsonLayerTPAPEC': {
						'subject': "APEC Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
										weight: 1,
										opacity: 1,
										color: 'white',
										fillOpacity: 0.7,
										fillColor: getColorTPMember(feature.properties.APEC)
									}
									}})""",
						'ptsLayer': "",
						'description':"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam aliquet fermentum ipsum, id commodo orci dignissim non. Mauris vulputate ultricies leo, et porta orci pretium in. Duis pulvinar iaculis augue, sit amet mollis quam tristique.",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerTPASEAN':{
						'subject': "ASEAN Membership",
						'jsonLayer': """new L.geoJson(data, {style:  function(feature){ return {
										weight: 1,
										opacity: 1,
										color: 'white',
										fillOpacity: 0.7,
										fillColor: getColorTPMember(feature.properties.ASEAN)
									}
									}})""",
						'ptsLayer': "",
						'description': "ASEAN Membership stuffASEAN Membership stuffASEAN Membership stuffASEAN Membership stuffASEAN Membership stuffASEAN Membership stuffASEAN Membership stuff",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerTPCAFTA':{
						'subject': "CAFTA Membership",
						'jsonLayer': "",
						'jsonStyle': {		"weight": 1,
											"opacity": 1,
											"color": 'white',
											"fillOpacity": 0.7,
											"fillColorMainKey": "TPMember",
											"fillColorSubKey": "CAFTA"
									},
						'ptsLayer': "",
						'description': "CAFTA MembershipCAFTA MembershipCAFTA MembershipCAFTA Membership",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerTPCBERA':{
						'subject': "CBERA Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
											weight: 1,
											opacity: 1,
											color: 'white',
											fillOpacity: 0.7,
											fillColor: getColorTPMember(feature.properties.CBERA)
										}
										}})""",
						'ptsLayer': "",
						'description': "CBERA MembershipCBERA MembershipCBERA MembershipCBERA MembershipCBERA Membership",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerTPNAFTA':{
						'subject': "NAFTA Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
											weight: 1,
											opacity: 1,
											color: 'white',
											fillOpacity: 0.7,
											fillColor: getColorTPMember(feature.properties.NAFTA)
										}
										}})""",
						'ptsLayer': "",
						'description': "NAFTA MembershipNAFTA MembershipNAFTA MembershipNAFTA MembershipNAFTA Membership",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerTPWTO':{
						'subject': "WTO Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
										weight: 1,
										opacity: 1,
										color: 'white',
										fillOpacity: 0.7,
										fillColor: getColorTPMember(feature.properties.WTO)
									}
									}})""",
						'ptsLayer': "",
						'description': "WTO MembershipWTO MembershipWTO MembershipWTO MembershipWTO MembershipWTO MembershipWTO Membership",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					}

				}
			},
			"keyMLO":{
				'categoryName': "Multi-Lateral Organizations",
				'categoryDescription': "<div><h7 class='lorem'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam aliquet fermentum ipsum, id commodo orci dignissim non. Mauris vulputate ultricies leo, et porta orci pretium in. Duis pulvinar iaculis augue, sit amet mollis quam tristique.</h7></div>",
				'layers':{
					'geoJsonLayerMLOAU':{
						'subject': "African Union Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
											weight: 1,
											opacity: 1,
											color: 'white',
											fillOpacity: 0.7,
											fillColor: getColorMLOMember(feature.properties.AU)
										}
										}})""",
						'ptsLayer': "",
						'description': "African Union MembershipAfrican Union MembershipAfrican Union MembershipAfrican Union Membership",
						'labels': {'grades': ['Member', 'Suspended', 'null'], 'from': ['Member', 'Suspended', 'Not a member']}
					},
					'geoJsonLayerMLOEU':{
						'subject': "European Union Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
											weight: 1,
											opacity: 1,
											color: 'white',
											fillOpacity: 0.7,
											fillColor: getColorMLOMember(feature.properties.FAO)
										}
										}})""",
						'ptsLayer': "",
						'description': "European Union MembershipEuropean Union MembershipEuropean Union MembershipEuropean Union MembershipEuropean Union MembershipEuropean Union MembershipEuropean Union Membership",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerMLOFAO':{
						'subject': "Food and Agriculture Organization Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
												weight: 1,
												opacity: 1,
												color: 'white',
												fillOpacity: 0.7,
												fillColor: getColorMLOMember(feature.properties.FAO)
											}
											}})""",
						'ptsLayer': "",
						'description': "Food and Agriculture Organization MembershipFood and Agriculture Organization MembershipFood and Agriculture Organization MembershipFood and Agriculture Organization MembershipFood and Agriculture Organization MembershipFood and Agriculture Organization Membership",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerMLOICAO':{
						'subject': "International Civil Aviation Organization Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
												weight: 1,
												opacity: 1,
												color: 'white',
												fillOpacity: 0.7,
												fillColor: getColorMLOMember(feature.properties.ICAO)
											}
											}})""",
						'ptsLayer': "",
						'description': "International Civil Aviation Organization MembershipInternational Civil Aviation Organization MembershipInternational Civil Aviation Organization MembershipInternational Civil Aviation Organization MembershipInternational Civil Aviation Organization Membership",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerMLONATO':{
						'subject': "North American Treaty Organization Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
													weight: 1,
													opacity: 1,
													color: 'white',
													fillOpacity: 0.7,
													fillColor: getColorMLOMember(feature.properties.NATO)
												}
												}})""",
						'ptsLayer': "",
						'description': "North American Treaty Organization MembershipNorth American Treaty Organization MembershipNorth American Treaty Organization Membership",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerMLOOAS':{
						'subject': "Organization of American States Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
												weight: 1,
												opacity: 1,
												color: 'white',
												fillOpacity: 0.7,
												fillColor: getColorMLOMember(feature.properties.OAS)
											}
											}})""",
						'ptsLayer': "",
						'description': "North American Treaty Organization MembershipNorth American Treaty Organization MembershipNorth American Treaty Organization Membership",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerMLOOECD':{
						'subject': "OECD Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
											weight: 1,
											opacity: 1,
											color: 'white',
											fillOpacity: 0.7,
											fillColor: getColorMLOMember(feature.properties.OECD)
										}
										}})""",
						'ptsLayer': "",
						'description': "OECD MembershipOECD MembershipOECD MembershipOECD MembershipOECD MembershipOECD MembershipOECD MembershipOECD Membership",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerMLOOSCE':{
						'subject': "OSCE Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
											weight: 1,
											opacity: 1,
											color: 'white',
											fillOpacity: 0.7,
											fillColor: getColorMLOMember(feature.properties.OSCE)
										}
										}})""",
						'ptsLayer': "",
						'description': "OSCE MembershipOSCE MembershipOSCE MembershipOSCE MembershipOSCE MembershipOSCE Membership",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerMLOUNESCO':{
						'subject': "UNESCO Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
											weight: 1,
											opacity: 1,
											color: 'white',
											fillOpacity: 0.7,
											fillColor: getColorMLOMember(feature.properties.UNESCO)
										}
										}})""",
						'ptsLayer': "",
						'description': "UNESCO MembershipUNESCO MembershipUNESCO MembershipUNESCO MembershipUNESCO Membership",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerMLOUNHCR':{
						'subject': "UNHCR Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
											weight: 1,
											opacity: 1,
											color: 'white',
											fillOpacity: 0.7,
											fillColor: getColorMLOMember(feature.properties.UNHCR)
										}
										}})""",
						'ptsLayer': "",
						'description': "UNHCR MembershipUNHCR MembershipUNHCR MembershipUNHCR MembershipUNHCR MembershipUNHCR Membershipp",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerMLOUNGA':{
						'subject': "UNGA Membership",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
										weight: 1,
										opacity: 1,
										color: 'white',
										fillOpacity: 0.7,
										fillColor: getColorMLOMember(feature.properties.UNGA)
									}
									}})""",
						'ptsLayer': "",
						'description': "UNGA MembershipUNGA MembershipUNGA MembershipUNGA MembershipUNGA MembershipUNGA MembershipUNGA Membership",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					}
				}
			},
			"keyHI":{
				'categoryName': "Health Issues",
				'categoryDescription': "<div><h7 class='lorem'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam aliquet fermentum ipsum, id commodo orci dignissim non. Mauris vulputate ultricies leo, et porta orci pretium in. Duis pulvinar iaculis augue, sit amet mollis quam tristique.</h7></div>",
				'layers':{
					'geoJsonLayerHIGH':{
						'subject': "Global Health",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
											weight: 1,
											opacity: 1,
											color: 'white',
											fillOpacity: 0.7,
											fillColor: getColorHIGH(feature.properties.Global_Health)
										}
										}})""",
						'ptsLayer': "",
						'description': "Global HealthGlobal HealthGlobal HealthGlobal HealthGlobal HealthGlobal HealthGlobal Health",
						'labels': {'grades': ['1'], 'from': ['Programs']}
					},
					'geoJsonLayerHIAV':{
						'subject': "Avian Flu (tk)",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
											weight: 1,
											opacity: 1,
											color: 'white',
											fillOpacity: 0.7,
											fillColor: getColorHIAV(feature.properties.Avian_Flu)
										}
										}})""",
						'ptsLayer': "",
						'description': "Avian Flu (tk)Avian Flu (tk)Avian Flu (tk)Avian Flu (tk)Avian Flu (tk)Avian Flu (tk)",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerHIHIVAIDS':{
						'subject': "HIV / AIDS (tk)",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
											weight: 1,
											opacity: 1,
											color: 'white',
											fillOpacity: 0.7,
											fillColor: getColorHIHIVAIDS(feature.properties.HIVAIDS)
										}
										}})""",
						'ptsLayer': "",
						'description': "HIV / AIDS (tk)HIV / AIDS (tk)HIV / AIDS (tk)HIV / AIDS (tk)HIV / AIDS (tk)HIV / AIDS (tk)",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerHIM':{
						'subject': "Malaria (tk)",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
															weight: 1,
															opacity: 1,
															color: 'white',
															fillOpacity: 0.7,
															fillColor: getColorHIM(feature.properties.Malaria)
														}
														}})""",
						'ptsLayer': "",
						'description': "Malaria (tk)Malaria (tk)Malaria (tk)Malaria (tk)Malaria (tk)Malaria (tk)Malaria (tk)Malaria (tk)",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerHIMHAC':{
						'subject': "Maternal Health - Access to Care",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
													weight: 1,
													opacity: 1,
													color: 'white',
													fillOpacity: 0.7,
													fillColor: getColorHIMHAC(feature.properties.Maternity_Health_Access_to_Care)
												}
												}})""",
						'ptsLayer': "",
						'description': "Maternal Health - Access to CareMaternal Health - Access to CareMaternal Health - Access to CareMaternal Health - Access to CareMaternal Health - Access to Care",
						'labels': {'grades': ['Excellent', 'Good', 'Fair', 'Poor', 'Unsuitable', 'No data'], 'from': ['Excellent', 'Good', 'Fair', 'Poor', 'Unsuitable', 'No data']}
					},
					'geoJsonLayerHIPEPFAR':{
						'subject': "PEPFAR",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
										weight: 1,
										opacity: 1,
										color: 'white',
										fillOpacity: 0.7,
										fillColor: getColorHIPEPFAR(feature.properties.PEPFAR)
									}
									}})""",
						'ptsLayer': "geoJsonLayerHIPEPFARpts",
						'description': "PEPFARPEPFARPEPFARPEPFARPEPFARPEPFARPEPFARPEPFARPEPFARPEPFARPEPFAR",
						'labels': {'grades': ['1', '2', '3', 'No Data'], 'from': ['1', '2', '3', 'No data']}
					},
					'geoJsonLayerHIP':{
						'subject': "Polio (tk)",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
										weight: 1,
										opacity: 1,
										color: 'white',
										fillOpacity: 0.7,
										fillColor: getColorHIP(feature.properties.Polio)
									}
									}})""",
						'ptsLayer': "",
						'description': "Polio (tk)Polio (tk)Polio (tk)Polio (tk)Polio (tk)Polio (tk)",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					},
					'geoJsonLayerHIT':{
						'subject': "Tuberculosis (tk)",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
										weight: 1,
										opacity: 1,
										color: 'white',
										fillOpacity: 0.7,
										fillColor: getColorHIT(feature.properties.Tuberculosis)
									}
									}})""",
						'ptsLayer': "",
						'description': "Tuberculosis (tk)Tuberculosis (tk)Tuberculosis (tk)Tuberculosis (tk)Tuberculosis (tk)",
						'labels': {'grades': ['Member','null'], 'from': ['Member', 'Not a member']}
					}
				}

			},
			"keyNuc":{
				'categoryName': "Nuclear Arms Control",
				'categoryDescription': "<div><h7 class='lorem'>A key element in the effort to control arms around the world has been the Treaty on the Non-Proliferation of Nuclear Weapons (NPT) which entered into force in 1970. The Treaty is regarded as the legal and political cornerstone of the nuclear nonproliferation regime, which establishes three “pillars” – nuclear nonproliferation, disarmament, and the peaceful use of nuclear energy.</h7><br><br><h7 class='lorem'>In Prague on April 5, 2009 President Obama said that the basic bargain at the core of the NPT Treaty is sound: “countries with nuclear weapons will move towards disarmament; countries without nuclear weapons will not acquire them; and all countries can access peaceful nuclear energy.” Although nine countries are acknowledged to possess nuclear weapons, not all of them are among the nearly190 nations that are party to the treaty.</h7><br><br><h7 class='lorem'>The Bureau of Arms Control, Verification and Compliance, coordinating with other national security institutions, develops strategies for the negotiation of arms control and disarmament treaties and creates strong relationships with other countries to implement the treaties. The work of the bureau serves to improve the security of the United States and all nations of the world.</h7><br><br><h7 class='lorem'>Links:</h7><ul><li><a href='http://www.un.org/disarmament/WMD/Nuclear/NPT.shtml'>Treaty on the Non-Proliferation of Nuclear Weapons</a></li><li><a href='http://www.state.gov/t/index.htm'>Under Secretary for Arms Control and International Security</a></li><a href='http://www.state.gov/t/avc/index.htm'>Bureau of Arms Control, Verification and Compliance</a></li><a href='http://www.state.gov/t/isn/index.htm'>Bureau of International Security and Nonproliferation</a></li><a href='http://www.state.gov/t/pm/index.htm'>Bureau of Political-Military Affairs</a></li></ul></div>",
				'layers':{
					'geoJsonLayerNucSign':{
						'subject': "Nuclear Arms Control - Signed",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
											weight: 1,
											opacity: 1,
											color: 'white',
											fillOpacity: 0.7,
											fillColor: getColorNucSign(feature.properties.Signed)
										}
										}})""",
						'ptsLayer': "geoJsonLayerNucpts",
						'description': "The Bureau of Arms Control, Verification and Compliance, coordinating with other national security institutions, develops strategies for the negotiation of arms control and disarmament treaties and creates strong relationships with other nations to cooperate in the implementation of the treaties. Ultimately, the work of the bureau serves to improve the security of the United States and all the nations of the world.",
						'labels': {'grades': ['X'], 'from': ['Signed']}
					},
					'geoJsonLayerNucDepo':{
						'subject': "Nuclear Arms Control - Deposited",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
										weight: 1,
										opacity: 1,
										color: 'white',
										fillOpacity: 0.7,
										fillColor: getColorNucDepo(feature.properties.Deposited)
									}
									}})""",
						'ptsLayer': "geoJsonLayerNucpts",
						'description': "The Bureau of Arms Control, Verification and Compliance, coordinating with other national security institutions, develops strategies for the negotiation of arms control and disarmament treaties and creates strong relationships with other nations to cooperate in the implementation of the treaties. Ultimately, the work of the bureau serves to improve the security of the United States and all the nations of the world.",
						'labels': {'grades': ['X'], 'from': ['Deposited']}
					}
				}
			},
			'keyHT':{
				'categoryName': "Human Trafficking",
				'categoryDescription': "<div><h7 class='lorem'>NOT ACTUAL CONTENTA key element in the effort to control arms around the world has been the Treaty on the Non-Proliferation of Nuclear Weapons (NPT) which entered into force in 1970. The Treaty is regarded as the legal and political cornerstone of the nuclear nonproliferation regime, which establishes three “pillars” – nuclear nonproliferation, disarmament, and the peaceful use of nuclear energy.</h7><br><br><h7 class='lorem'>In Prague on April 5, 2009 President Obama said that the basic bargain at the core of the NPT Treaty is sound: “countries with nuclear weapons will move towards disarmament; countries without nuclear weapons will not acquire them; and all countries can access peaceful nuclear energy.” Although nine countries are acknowledged to possess nuclear weapons, not all of them are among the nearly190 nations that are party to the treaty.</h7><br><br><h7 class='lorem'>The Bureau of Arms Control, Verification and Compliance, coordinating with other national security institutions, develops strategies for the negotiation of arms control and disarmament treaties and creates strong relationships with other countries to implement the treaties. The work of the bureau serves to improve the security of the United States and all nations of the world.</h7><br><br><h7 class='lorem'>Links:</h7><ul><li><a href='http://www.un.org/disarmament/WMD/Nuclear/NPT.shtml'>Treaty on the Non-Proliferation of Nuclear Weapons</a></li><li><a href='http://www.state.gov/t/index.htm'>Under Secretary for Arms Control and International Security</a></li><a href='http://www.state.gov/t/avc/index.htm'>Bureau of Arms Control, Verification and Compliance</a></li><a href='http://www.state.gov/t/isn/index.htm'>Bureau of International Security and Nonproliferation</a></li><a href='http://www.state.gov/t/pm/index.htm'>Bureau of Political-Military Affairs</a></li></ul></div>",
				'layers':{
					'geoJsonLayerHT':{
						'subject': "Human Trafficking",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
											weight: 1,
											opacity: 1,
											color: 'white',
											fillOpacity: 0.7,
											fillColor: getColorHT(feature.properties.Human_Trafficking)
										}
										}})""",
						'ptsLayer': "geoJsonLayerHTpts",
						'description': "Human TraffickingHuman TraffickingHuman TraffickingHuman TraffickingHuman TraffickingHuman Trafficking",
						'labels': {'grades': ['Tier 1', 'Tier 2', 'Tier 2 Watch List', 'Tier 3 Auto-Downgrade', 'Tier 3', 'Special Case'], 'from': ['Tier 1', 'Tier 2', 'Tier 2 Watch List', 'Tier 3 Auto-Downgrade', 'Tier 3', 'Special Case']}
					}
				}
			},
			'keyWatSan':{
				'categoryName': "Water & Sanitation",
				'categoryDescription': " sit amet, consectetur adipiscing elit. Aliquam aliquet fermentum ipsum, id commodo orci dignissim n",
				'layers':{
					'geoJsonLayerWatSan':{
						'subject': "Water & Sanitation",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
										weight: 1,
										opacity: 1,
										color: 'white',
										fillOpacity: 0.7,
										fillColor: getColorWatSan(feature.properties.Wat_San)
									}
									}})""",
						'ptsLayer': "",
						'description': "Water & SanitationWater & SanitationWater & SanitationWater & SanitationWater & SanitationWater & Sanitation",
						'labels': {'grades': ['1'], 'from': ['Programs']}
					}
				}
			},
			'keyDHRA':{
				'categoryName': "Democracy & Human Rights",
				'categoryDescription': "Democracy & Human RightsDemocracy & Human RightsDemocracy & Human RightsDemocracy & Human RightsDemocracy & Human RightsDemocracy & Human Rights",
				'layers':{
					'geoJsonLayerDHRA':{
						'subject': "Democracy & Human Rights",
						'jsonLayer': """new L.geoJson(data, {style: function(feature){ return {
										weight: 1,
										opacity: 1,
										color: 'white',
										fillOpacity: 0.7,
										fillColor: getColorDHRA(feature.properties.DHRA)
									}
									}})""",
						'ptsLayer': "",
						'description': "Democracy & Human RightsDemocracy & Human RightsDemocracy & Human RightsDemocracy & Human RightsDemocracy & Human Rights",
						'labels': {'grades': ['1'], 'from': ['Programs']}
					}
				}
			}
}

OUTPUT = "C:\\opengeo\\webapps\\DiplomacyExplorer2\\jsonFile\\splitoutput\\"

import json

for mainkey,mainkeyobj in jsoninfo.iteritems():
    with open(OUTPUT + mainkey + ".json", 'w') as mainkeyfile:
        newobj = {'categoryName': mainkeyobj['categoryName'], 'categoryDescription': mainkeyobj['categoryDescription']}
        json.dump(newobj, mainkeyfile)

    for subkey, subkeyobj in mainkeyobj['layers'].iteritems():
        with open(OUTPUT + mainkey + "_" + subkey + ".json", 'w') as subkeyfile:
            json.dump(subkeyobj, subkeyfile)







#split into different main keys and subkeys
#write each to file with underscore name

