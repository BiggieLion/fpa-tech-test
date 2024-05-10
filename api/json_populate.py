def populate_family_object(pre_json, json_response):
    for field in pre_json.values():
        for element in field:
            familyArray = element["familyRelationships"]
            for member in familyArray:
                if (
                    member["relationship"] == "Spouse"
                    and member["name"] not in json_response["family"]["spouse"]
                ):
                    json_response["family"]["spouse"].append(member["name"])
                elif (
                    member["relationship"] == "Child"
                    and member["name"] not in json_response["family"]["children"]
                ):
                    json_response["family"]["children"].append(member["name"])
                elif (
                    member["relationship"] == "Family member"
                    and member["name"] not in json_response["family"]["other_family"]
                ):
                    json_response["family"]["other_family"].append(member["name"])
                elif (
                    member["relationship"] == "Self"
                    and member["name"] not in json_response["family"]["self"]
                ):
                    json_response["family"]["self"].append(member["name"])

    return json_response


def populate_assets_array(pre_assets_array):
    assets_array = []
    for asset in pre_assets_array:
        asset_object = {
            "assetName": asset["assetName"],
            "assetType": asset["assetType"],
            "primaryBeneficiaries": populate_primary_beneficiaries_assets_array(
                asset["primaryBeneficiaries"]
            ),
        }
        assets_array.append(asset_object)

    return assets_array


def populate_primary_beneficiaries_assets_array(primary_beneficiaries_array):
    primary_beneficiaries = []
    for primary_beneficiary in primary_beneficiaries_array:
        primary_beneficiary_object = {
            "whenWillTransfer": primary_beneficiary["whenWillTransfer"],
            "isItFirstDeathOrSecondDeath": primary_beneficiary[
                "isItFirstDeathOrSecondDeath"
            ],
            "beneficiaries": populate_beneficiaries_primary_array(
                primary_beneficiary["beneficiaries"]
            ),
        }
        primary_beneficiaries.append(primary_beneficiary_object)

    return primary_beneficiaries


def populate_beneficiaries_primary_array(beneficiaries_array):
    beneficiaries = []
    for beneficiary in beneficiaries_array:
        beneficiary_object = {
            "name": beneficiary["name"],
            "value": beneficiary["value"],
            "amount": beneficiary["amount"],
            "comment": beneficiary["comment"],
        }
        beneficiaries.append(beneficiary_object)

    return beneficiaries


def populate_material_info_array(material_info_array):
    material_info = []
    for material in material_info_array:
        material_object = {
            "value": material["value"],
            "page": material["page"],
            "paragraph": material["paragraph"],
        }
        material_info.append(material_object)

    return material_info


def populate_will_array_objects(will_array):
    wills = []
    for will in will_array:
        will_object = {
            "title": will["title"],
            "executor": will["executor"],
            "replacement_executor": will["replacement_executor"],
            "guardian": will["guardian"],
            "state": will["state"],
            "willOwner": will["willOwner"],
            "dateOfWill": will["dateOfWill"],
            "assets": populate_assets_array(will["assets"]),
            "materialInformation": populate_material_info_array(
                will["materialInformation"]
            ),
        }
        wills.append(will_object)

    return wills


def populate_trusts_array(trusts_array):
    trusts = []
    for trust in trusts_array:
        trust_object = {
            "title": trust["title"],
            "dateOfTrust": trust["dateOfTrust"],
            "grantor": trust["grantor"],
            "trustee": populate_trustee_array(trust["trustee"]),
            "type": trust["type"],
            "state": trust["state"],
            "assets": populate_assets_array(trust["assets"]),
            "trustees": populate_trustees_array(trust["trustees"]),
            "subtype": trust["subtype"],
            "jointOrSingle": trust["jointOrSingle"],
            "grantorOrNonGrantorTrust": trust["grantorOrNonGrantorTrust"],
            "resultingTrusts": trust["resultingTrusts"],
            "listsAssets": trust["listsAssets"],
            "materialInformation": populate_material_info_array(
                trust["materialInformation"]
            ),
        }
        trusts.append(trust_object)

    return trusts


def populate_trustee_array(trustee_array):
    trustees = []
    for trustee in trustee_array:
        trustee_object = {
            "name": trustee["name"],
            "relation": trustee["relation"],
            "trusteeType": trustee["trusteeType"],
            "trusteeTrusteeOrCoTrustee": trustee["trusteeTrusteeOrCoTrustee"],
            "trusteeCanAnyCoTrusteeContinueAsSoleTrustee": trustee[
                "trusteeCanAnyCoTrusteeContinueAsSoleTrustee"
            ],
            "page": trustee["page"],
            "paragraph": trustee["paragraph"],
        }
        trustees.append(trustee_object)

    return trustees


def populate_trustees_array(trustees_array):
    trustees = []
    for trustee in trustees_array:
        trustee_object = {
            "name": trustee["name"],
            "relation": trustee["relation"],
            "trusteeType": trustee["trusteeType"],
            "trusteeTrusteeOrCoTrustee": trustee["trusteeTrusteeOrCoTrustee"],
            "trusteeCanTrusteesActIndividually": trustee[
                "trusteeCanTrusteesActIndividually"
            ],
            "trusteeCanAnyCoTrusteeContinueAsSoleTrustee": trustee[
                "trusteeCanAnyCoTrusteeContinueAsSoleTrustee"
            ],
            "page": trustee["page"],
            "paragraph": trustee["paragraph"],
        }
        trustees.append(trustee_object)

    return trustees


def populate_json_response(pre_json):
    json_response = {
        "family": {"spouse": [], "children": [], "other_family": [], "self": []},
        "will": [],
        "trusts": [],
    }

    json_response = populate_family_object(pre_json, json_response)

    if "will" in pre_json.keys():
        json_response["will"] = populate_will_array_objects(pre_json["will"])

    if "trusts" in pre_json.keys():
        json_response["trusts"] = populate_trusts_array(pre_json["trusts"])

    return json_response
