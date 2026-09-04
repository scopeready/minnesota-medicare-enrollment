#!/usr/bin/env python3
"""MinnesotaMedicareEnrollment.com — static site generator.

Run from the repo root:  python3 source/generate.py
Writes every HTML page plus sitemap.xml, robots.txt, llms.txt, llms-full.txt
and the shared assets (site.css, site.js, analytics.js, favicon.svg).

Content lives in source/content.py (topic pages) and in the CITIES / REGIONS
tables below. Site-wide facts live in the CONFIG block. Edit, re-run, commit.
"""
import json, re, html
from pathlib import Path
from datetime import date

from scenes import SCENES
from content import TOPIC_PAGES, ABOUT_BODY, FAQ_PAGE, PRIVACY_BODY, TERMS_BODY

ROOT = Path(__file__).resolve().parent.parent

# ----------------------------------------------------------------------------
# CONFIG — the only block most edits touch
# ----------------------------------------------------------------------------
SITE_URL = "https://minnesotamedicareenrollment.com"
SITE_NAME = "Minnesota Medicare Enrollment"
ORG = "ECOS Medicare Solutions"
# TODO(Darin): swap for a Minnesota (612 / 651 / 507 / 218) tracking number. This
# is the agency's main line, so the site is never live with a dead phone.
PHONE = "(702) 706-6564"
TEL = "+17027066564"
EMAIL = "darinweidauer@ecos.care"
NPN = "18580338"
LIC = "40620754"                      # Minnesota producer licence, shown beside the NPN wherever Darin is named
LIC_TXT = f", MN License #{LIC}"
WEB3FORMS_KEY = "fc793a1c-1dd6-4a2e-9078-e907c4ab0428"   # public by design; same inbox as the sister sites
QUOTE_URL = "https://planenroll.com/?purl=Darin-Weidauer"
TODAY = date(2026, 9, 3)
ISO = TODAY.isoformat()
REVIEWED = TODAY.strftime("%B %-d, %Y")
PLAN_YEAR = 2026

# Verified 2026 Original Medicare figures (CMS, released Nov 14, 2025). Keep in
# sync with llms.txt — the generator writes both from these constants.
FIG = dict(partb="$202.90", partb_ded="$283", parta_ded="$1,736", partd_cap="$2,100",
           partd_ded="$615", partd_base="$38.99", irmaa_single="$109,000", irmaa_joint="$218,000")

# The agency's other web properties. Visible in the footer and declared as
# sameAs on the Organization node so answer engines resolve them to one agency.
NETWORK = [
    ("Medicare Enrollment Arizona", "https://www.medicareenrollmentarizona.com"),
    ("Georgia Medicare Enrollment", "https://georgiamedicareenrollment.com"),
    ("Medicare Enrollment Nevada", "https://medicareenrollmentnevada.com"),
    ("Colorado Medicare Enrollment", "https://coloradomedicareenrollment.com"),
    ("Tennessee Medicare Quotes", "https://www.tennesseemedicarequotes.com"),
    ("Texas Medicare Enrollment", "https://texasmedicareenrollment.com"),
    ("Medicare Enrollment Utah", "https://medicareenrollmentutah.com"),
    ("Medicare Enrollment Florida", "https://medicareenrollmentflorida.com"),
    ("California Medicare Enrollment", "https://www.californiamedicareenrollment.com"),
    ("MyMedigapRate — Medigap rate research", "https://www.mymedigaprate.com"),
    ("MyECOS360 — Darin's author page", "https://www.myecos360.com/darin-weidauer"),
]
SAMEAS_ORG = [u for _, u in NETWORK] + [
    "https://howdoiapplyformedicare.com",
    "https://medicareadvantageanswers.com",
    "https://dentalinsurancetomorrow.com",
]
SAMEAS_DARIN = [
    "https://www.myecos360.com/darin-weidauer",
    "https://www.linkedin.com/in/darin-weidauer-3165a816b/",
    "https://www.youtube.com/channel/UCD1XkkknhQ3UT-8AteYD3vQ",
    "https://www.medicareenrollmentarizona.com/about",
    "https://georgiamedicareenrollment.com/",
    "https://texasmedicareenrollment.com/about",
    "https://medicareenrollmentutah.com/about",
    "https://medicareenrollmentflorida.com/about",
    "https://www.californiamedicareenrollment.com/about",
    "https://www.mymedigaprate.com/about",
]

TPMO = ("We do not offer every plan available in your area. Any information we provide is limited to those "
        "plans we do offer in your area. Please contact Medicare.gov, 1-800-MEDICARE, or Minnesota Aging Pathways "
        "(the Senior LinkAge Line, Minnesota&rsquo;s State Health Insurance Assistance Program, 800-333-2433) "
        "to get information on all of your options.")

# ----------------------------------------------------------------------------
# Places
# ----------------------------------------------------------------------------
REGIONS = [
    dict(slug="twin-cities", name="Twin Cities Metro", short="Twin Cities", scene="skyline",
         eyebrow="Medicare by region · Minneapolis&ndash;St. Paul",
         h1="Medicare help across the Twin Cities metro",
         sub="Hennepin, Ramsey, Dakota, Anoka, Washington, Scott and Carver counties &mdash; the most plan choices in Minnesota, riding on the most crowded set of provider networks. We check the networks first.",
         counties="Hennepin, Ramsey, Dakota, Anoka, Washington, Scott, Carver",
         cities=["minneapolis", "st-paul", "bloomington", "brooklyn-park", "plymouth", "woodbury", "maple-grove", "eagan", "burnsville"],
         systems=["Allina Health", "M Health Fairview", "HealthPartners &amp; Park Nicollet", "Hennepin Healthcare", "North Memorial Health", "Regions Hospital"],
         cost=[],
         intro=["More than half of Minnesota&rsquo;s Medicare beneficiaries live in the seven-county metro, and it shows in the plan menu: dozens of Medicare Advantage plans, every Medigap carrier in the state, and the full set of Part D plans. Medicare Cost plans, on the other hand, ended in the metro counties in 2019, so metro residents choose between Medicare Advantage and Original Medicare with a supplement.",
                "The metro is also where the big 2026 shake-up landed hardest. UCare left Medicare Advantage statewide, and Humana and UnitedHealthcare pulled out of several counties, so a lot of households were shopping for the first time in years. If that was you, an annual review is worth more than ever &mdash; the plans announced each October 1 are often different from the ones you compared last year."],
         faqs=[("Which Medicare Advantage plans are available in the Twin Cities?", "Availability is set by county and ZIP code, and the lineup changes every plan year. The metro typically has the widest choice in Minnesota &mdash; plans from Blue Cross Blue Shield of Minnesota, HealthPartners, Medica, UnitedHealthcare and others &mdash; but each rides on a different network. We compare what is actually offered at your address."),
               ("Are Medicare Cost plans still sold in the Twin Cities?", "No. Cost plans ended in the seven-county metro at the end of 2018 under a federal rule that retires them wherever two or more Medicare Advantage plans compete. They remain in 21 mostly rural counties. Metro residents choose between Medicare Advantage and Original Medicare with a Medicare supplement."),
               ("Do you meet in person in the Twin Cities?", "We work with Minnesotans by phone and video across the state, which is how most people prefer it. Call and we will set up a time that suits you.")]),
    dict(slug="southeast-minnesota", name="Southeast Minnesota", short="Southeast", scene="bluffs",
         eyebrow="Medicare by region · Rochester &amp; the river bluffs",
         h1="Medicare help across Southeast Minnesota",
         sub="Rochester, Winona, Red Wing, Austin, Albert Lea, Owatonna and Faribault &mdash; Mayo Clinic country, where the network question is really a Mayo question.",
         counties="Olmsted, Winona, Goodhue, Mower, Freeborn, Steele, Rice, Wabasha, Dodge, Fillmore, Houston",
         cities=["rochester"],
         systems=["Mayo Clinic (Rochester)", "Mayo Clinic Health System", "Olmsted Medical Center", "Winona Health", "Allina Health Faribault &amp; Owatonna"],
         cost=["Goodhue", "Rice"],
         intro=["Southeast Minnesota&rsquo;s Medicare decisions revolve around one fact: Mayo Clinic accepts Original Medicare everywhere, but contracts with only some Medicare Advantage plans, and those contracts change. A Medicare supplement or a Cost plan keeps Mayo in reach without a network question; an Advantage plan needs checking every single year.",
                "Goodhue and Rice counties are two of the 21 Minnesota counties where Medicare Cost plans are still sold, which gives Red Wing and Faribault residents a middle path many metro residents no longer have."],
         faqs=[("Does Mayo Clinic take Medicare Advantage?", "Mayo Clinic accepts Original Medicare, which is what a Medicare supplement or a Cost plan builds on. It contracts with some Medicare Advantage plans and not others, and those contracts change year to year. If Mayo is your care, we confirm the plan&rsquo;s Mayo status in writing before you enroll."),
               ("Which Southeast Minnesota counties still have Cost plans?", "Goodhue and Rice, as of the 2026 plan year, per the Minnesota Department of Commerce&rsquo;s Cost plan guide. Olmsted, Winona and the other southeastern counties do not."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")]),
    dict(slug="arrowhead-north-shore", name="Arrowhead &amp; North Shore", short="Arrowhead", scene="lighthouse",
         eyebrow="Medicare by region · Duluth, the Iron Range &amp; the North Shore",
         h1="Medicare help across the Arrowhead and the North Shore",
         sub="Duluth, Two Harbors, Grand Marais, Hibbing, Virginia, Grand Rapids and International Falls &mdash; big distances, two big health systems, and the largest cluster of Cost-plan counties in the state.",
         counties="St. Louis, Lake, Cook, Carlton, Itasca, Koochiching, Aitkin",
         cities=["duluth"],
         systems=["Essentia Health", "Aspirus St. Luke&rsquo;s", "Fairview Range (Hibbing)", "Grand Itasca Clinic &amp; Hospital", "Cook County North Shore Health", "Rainy Lake Medical Center"],
         cost=["St. Louis", "Lake", "Cook", "Carlton", "Itasca", "Koochiching", "Aitkin"],
         intro=["Northeastern Minnesota is where Medicare Cost plans matter most. All seven Arrowhead counties are on the state&rsquo;s list of counties where Cost plans are still sold, so residents from Duluth to the Canadian border can choose a plan that uses a local network at home and falls back on Original Medicare anywhere else &mdash; a fit for people who winter away, or who drive to Rochester or the Twin Cities for specialty care.",
                "The region also saw HealthPartners leave Medicare Advantage in St. Louis County for 2026, so many Duluth-area households were re-shopping. Essentia and Aspirus St. Luke&rsquo;s each contract with different plans; we confirm your system is in-network before anything else."],
         faqs=[("Are Medicare Cost plans available in Duluth and St. Louis County?", "Yes. St. Louis County is one of the 21 Minnesota counties where Cost plans are still offered, along with Lake, Cook, Carlton, Itasca, Koochiching and Aitkin. Cost plans are sold by Blue Cross Blue Shield of Minnesota and Medica; availability and premiums are published each year by the Minnesota Department of Commerce."),
               ("Which plans include Essentia or Aspirus St. Luke&rsquo;s?", "It depends on the plan and the year. Each health system contracts with some plans and not others, and the lists change every October. We check your doctors and hospital against the plan directory before you enroll."),
               ("I spend winters in Arizona. Which plan travels?", "Original Medicare with a Medicare supplement works anywhere in the country. A Cost plan also covers you out of area through Original Medicare. Most Medicare Advantage plans cover only emergencies outside their service area. See our snowbird guide.")]),
    dict(slug="central-minnesota", name="Central Minnesota &amp; Brainerd Lakes", short="Central", scene="lakes",
         eyebrow="Medicare by region · St. Cloud &amp; the lakes",
         h1="Medicare help across Central Minnesota and the Brainerd Lakes",
         sub="St. Cloud, Brainerd, Little Falls, Mora, Pine City and Litchfield &mdash; growing retirement lake country served by CentraCare, Essentia and Cuyuna.",
         counties="Stearns, Benton, Sherburne, Crow Wing, Morrison, Mille Lacs, Kanabec, Pine, Meeker, Cass, Todd, Wright",
         cities=["st-cloud", "brainerd"],
         systems=["CentraCare", "Essentia Health&ndash;St. Joseph&rsquo;s (Brainerd)", "Cuyuna Regional Medical Center", "Lakewood Health System", "Welia Health (Mora)"],
         cost=["Mille Lacs", "Kanabec", "Pine", "Meeker"],
         intro=["Central Minnesota is a mix: the St. Cloud area has metro-style plan choice, while the lakes counties to the north and east lean on a couple of systems and long drives. Mille Lacs, Kanabec, Pine and Meeker counties are still Cost-plan counties; Stearns, Crow Wing and the others are not.",
                "A lot of people retire to a lake place here after a career in the metro. If that is you, note that moving your permanent address across a county line changes the plans available to you and opens a Special Enrollment Period to switch."],
         faqs=[("Which Central Minnesota counties have Medicare Cost plans?", "Mille Lacs, Kanabec, Pine and Meeker, per the Minnesota Department of Commerce&rsquo;s 2026 Cost plan guide. Stearns, Benton, Sherburne, Crow Wing and Wright do not."),
               ("I moved to my lake home full time. Do I need to change plans?", "Possibly. Medicare Advantage, Part D and Cost plans are tied to your county of permanent residence. Moving out of a plan&rsquo;s service area gives you a Special Enrollment Period to pick a plan offered where you live now; a Medicare supplement follows you without a change."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")]),
    dict(slug="northwest-minnesota", name="Northwest Minnesota &amp; the Red River Valley", short="Northwest", scene="prairie",
         eyebrow="Medicare by region · Moorhead, Bemidji &amp; the valley",
         h1="Medicare help across Northwest Minnesota",
         sub="Moorhead, Bemidji, Detroit Lakes, Thief River Falls, Crookston and East Grand Forks &mdash; where your nearest hospital may be across the river in North Dakota.",
         counties="Clay, Beltrami, Becker, Pennington, Polk, Otter Tail (north), Norman, Marshall, Kittson, Roseau, Lake of the Woods",
         cities=["moorhead", "bemidji"],
         systems=["Sanford Health (Fargo, Bemidji, Thief River Falls)", "Essentia Health (Fargo, Detroit Lakes)", "Altru Health System (Grand Forks)", "RiverView Health (Crookston)"],
         cost=[],
         intro=["Northwest Minnesota&rsquo;s Medicare question is often a border question. Fargo and Grand Forks hospitals serve much of the region, so a plan&rsquo;s network has to reach across the state line, and Medicare supplements and Original Medicare do that automatically. Medicare Advantage networks here are thinner than in the metro, and UnitedHealthcare and HealthPartners trimmed their county footprints for 2026.",
                "None of the northwestern counties are on the state&rsquo;s Cost-plan list, so the choice is Medicare Advantage or Original Medicare plus a Minnesota Basic or Extended Basic supplement and a Part D plan."],
         faqs=[("Can I use Sanford or Essentia in Fargo with a Minnesota plan?", "With Original Medicare and a Medicare supplement, yes &mdash; they take Medicare like any other provider. With a Medicare Advantage plan, only if Fargo providers are in that plan&rsquo;s network, which we confirm before you enroll."),
               ("Are there Cost plans in Northwest Minnesota?", "No. None of the northwestern counties are among the 21 where Cost plans are still sold."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")]),
    dict(slug="southwest-minnesota", name="Southwest Minnesota &amp; the Minnesota River Valley", short="Southwest", scene="prairie",
         eyebrow="Medicare by region · Mankato, New Ulm, Marshall &amp; Worthington",
         h1="Medicare help across Southwest Minnesota",
         sub="Mankato, New Ulm, Marshall, Worthington, Hutchinson and Pipestone &mdash; prairie towns with strong local hospitals and several Cost-plan counties.",
         counties="Blue Earth, Nicollet, Brown, Lyon, Nobles, McLeod, Sibley, Le Sueur, Pipestone, Rock, Yellow Medicine, Redwood, Watonwan, Martin",
         cities=["mankato"],
         systems=["Mayo Clinic Health System (Mankato, New Ulm, Fairmont)", "Avera (Marshall, Pipestone, Worthington)", "Sanford Worthington", "Hutchinson Health", "Ridgeview"],
         cost=["McLeod", "Sibley", "Le Sueur", "Pipestone", "Rock", "Yellow Medicine"],
         intro=["Southwest Minnesota has six of the state&rsquo;s 21 Cost-plan counties, and in several of them a Cost plan is the only way to get a local network without giving up Original Medicare elsewhere. HealthPartners left Medicare Advantage in Lyon County for 2026, a reminder that rural Advantage lineups change.",
                "Mayo Clinic Health System and Avera dominate care here, and each contracts differently with each plan. We put your clinic and your pharmacy into the comparison before we talk about premiums."],
         faqs=[("Which Southwest Minnesota counties still have Cost plans?", "McLeod, Sibley, Le Sueur, Pipestone, Rock and Yellow Medicine, per the Minnesota Department of Commerce&rsquo;s 2026 Cost plan guide. Blue Earth, Nicollet, Brown, Lyon and Nobles do not."),
               ("Does Mayo Clinic Health System in Mankato take Medicare Advantage?", "It accepts Original Medicare, and it contracts with some Medicare Advantage plans and not others, changing year to year. We confirm the plan&rsquo;s status with Mayo before you enroll."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")]),
    dict(slug="west-central-minnesota", name="West Central Minnesota", short="West Central", scene="lakes",
         eyebrow="Medicare by region · Alexandria, Fergus Falls, Willmar &amp; Morris",
         h1="Medicare help across West Central Minnesota",
         sub="Alexandria, Fergus Falls, Willmar, Morris and the lakes around them &mdash; a retirement region where Stevens and Traverse counties still carry Cost plans.",
         counties="Douglas, Otter Tail, Kandiyohi, Stevens, Traverse, Pope, Grant, Swift, Chippewa, Wilkin",
         cities=[],
         systems=["Alomere Health (Alexandria)", "Lake Region Healthcare (Fergus Falls)", "CentraCare&ndash;Rice Memorial (Willmar)", "Stevens Community Medical Center (Morris)"],
         cost=["Stevens", "Traverse"],
         intro=["West Central Minnesota is lake-cabin-turned-permanent-home country, and its Medicare picture is rural: a strong local hospital in each town, long drives for specialty care, and Medicare Advantage lineups that shift year to year. HealthPartners dropped Wilkin County for 2026.",
                "Stevens and Traverse counties are still Cost-plan counties. Elsewhere, a Minnesota Basic or Extended Basic supplement remains the simplest way to keep every hospital in the state, and in Fargo, on the table."],
         faqs=[("Which West Central counties still have Cost plans?", "Stevens and Traverse, per the Minnesota Department of Commerce&rsquo;s 2026 Cost plan guide. Douglas, Otter Tail, Kandiyohi and the others do not."),
               ("Can a Medicare supplement be used at any hospital in the region?", "Yes. A Minnesota Basic or Extended Basic policy works with Original Medicare, so any hospital or doctor that accepts Medicare &mdash; in Minnesota, in Fargo, or in Arizona in January &mdash; is covered without a network."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")]),
]
REGION = {r["slug"]: r for r in REGIONS}

CITIES = [
    dict(slug="minneapolis", name="Minneapolis", county="Hennepin County", region="twin-cities", scene="skyline",
         sub="From Uptown to Northeast, Minneapolis has more Medicare plan choices than anywhere in the state &mdash; and more networks to get wrong. A patient, plain-English comparison earns its keep here.",
         intro=["Hennepin County has the deepest Medicare menu in Minnesota: dozens of Medicare Advantage plans, every Medigap carrier, and the full Part D lineup. They ride on different networks &mdash; Allina&rsquo;s Abbott Northwestern, M Health Fairview and the University of Minnesota Medical Center, Hennepin Healthcare, North Memorial &mdash; and the network is what decides whether a $0-premium plan is a bargain or a trap.",
                "Cost plans left Hennepin County in 2019, so the choice is Medicare Advantage or Original Medicare with a Minnesota supplement. UCare&rsquo;s statewide exit and Humana&rsquo;s departure from Hennepin for 2026 sent a lot of Minneapolis households shopping; we help you compare what is actually offered at your ZIP code, check your prescriptions, and weigh Advantage against a Basic or Extended Basic supplement you can use anywhere."],
         systems=["Allina Health / Abbott Northwestern", "M Health Fairview", "Hennepin Healthcare (HCMC)", "North Memorial Health", "University of Minnesota Medical Center"],
         communities="Uptown, Northeast, North Loop, Linden Hills, Longfellow, Nokomis, Kingfield, Camden, Edina, Richfield, St. Louis Park",
         faqs=[("Which Medicare plans are available in Minneapolis?", "Availability changes by ZIP code, but most Minneapolis residents can choose among many Medicare Advantage plans, every Medicare supplement carrier licensed in Minnesota, and the full set of standalone Part D plans. We compare what is offered at your address and what fits your doctors and medications."),
               ("Will my Allina or Fairview doctors take a Medicare Advantage plan?", "It depends on the specific plan&rsquo;s network, and the contracts change every year. Before you enroll we confirm your providers at Allina, M Health Fairview, Hennepin Healthcare or North Memorial are in-network and your prescriptions are on the formulary, so there are no surprises in January."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["st-paul", "bloomington", "brooklyn-park", "plymouth"]),
    dict(slug="st-paul", name="St. Paul", county="Ramsey County", region="twin-cities", scene="capitol",
         sub="Highland Park, Como, the East Side, Roseville, Maplewood &mdash; St. Paul and Ramsey County residents have a full menu of plans and a network question that usually starts with Regions or United.",
         intro=["Ramsey County shares the metro&rsquo;s wide plan choice, and its care is anchored by HealthPartners&rsquo; Regions Hospital, Allina&rsquo;s United Hospital, M Health Fairview and a thick layer of HealthPartners and Allina clinics. Which of those a Medicare Advantage plan includes is the first thing to check, because it varies by carrier and by year.",
                "Cost plans ended in Ramsey County in 2019. St. Paul residents choose between Medicare Advantage and Original Medicare with a Minnesota Basic or Extended Basic supplement, and after the 2026 carrier exits many are choosing again. We compare both paths with your doctors, your pharmacy and your budget in front of us."],
         systems=["Regions Hospital (HealthPartners)", "United Hospital (Allina Health)", "M Health Fairview", "HealthPartners clinics", "Allina Health clinics"],
         communities="Highland Park, Mac-Groveland, Como, Summit Hill, the East Side, West Side, Roseville, Maplewood, White Bear Lake, Shoreview, North St. Paul",
         faqs=[("Which Medicare plans are available in St. Paul?", "Ramsey County residents can typically choose among many Medicare Advantage plans, every Medicare supplement carrier in Minnesota, and the full Part D lineup. Availability is set by ZIP code and changes every plan year; we compare what is actually offered at your address."),
               ("Is Regions Hospital in my plan&rsquo;s network?", "Regions is a HealthPartners hospital and is in HealthPartners&rsquo; own plans; whether it is in another carrier&rsquo;s Medicare Advantage network varies by plan and by year. With Original Medicare and a supplement there is no network to check. We confirm before you enroll."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["minneapolis", "woodbury", "eagan"]),
    dict(slug="rochester", name="Rochester", county="Olmsted County", region="southeast-minnesota", scene="bluffs",
         sub="In Rochester, the Medicare question is a Mayo Clinic question. We make sure whatever you choose keeps Mayo in reach.",
         intro=["Mayo Clinic accepts Original Medicare, full stop &mdash; which is why Original Medicare with a Minnesota supplement is the plan most Rochester retirees start from. Mayo contracts with only some Medicare Advantage plans, and those contracts are renegotiated; UnitedHealthcare left Olmsted County for 2026. If you want an Advantage plan for its extras, we confirm its Mayo status in writing first.",
                "Olmsted Medical Center is the other major system, with its own contracts. Cost plans are not sold in Olmsted County, though neighbouring Goodhue and Rice counties still have them."],
         systems=["Mayo Clinic", "Olmsted Medical Center", "Mayo Clinic Health System"],
         communities="Rochester, Byron, Stewartville, Kasson, Pine Island, Chatfield, Oronoco, Eyota",
         faqs=[("Does Mayo Clinic accept Medicare Advantage plans?", "Mayo Clinic accepts Original Medicare and therefore every Medicare supplement. It contracts with some Medicare Advantage plans and not others, and the list changes from year to year. If Mayo is your care, we confirm the plan&rsquo;s Mayo status before you enroll."),
               ("Which Medicare plans are available in Rochester?", "Olmsted County residents can choose among a number of Medicare Advantage plans, every Medicare supplement carrier in Minnesota, and the full Part D lineup. Cost plans are not sold in Olmsted County."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["mankato", "burnsville"]),
    dict(slug="duluth", name="Duluth", county="St. Louis County", region="arrowhead-north-shore", scene="lighthouse",
         sub="Duluth has something most of Minnesota lost in 2019: Medicare Cost plans. Add Essentia and Aspirus St. Luke&rsquo;s, and the comparison here looks different from the metro.",
         intro=["St. Louis County is one of 21 Minnesota counties where Medicare Cost plans are still sold, so Duluth residents can choose a plan that uses a local network at home and Original Medicare everywhere else &mdash; a fit for winters in Arizona or a Mayo referral. That option sits alongside Medicare Advantage and Original Medicare with a Minnesota supplement.",
                "Duluth&rsquo;s two systems, Essentia Health and Aspirus St. Luke&rsquo;s, contract differently with each plan, and HealthPartners left Medicare Advantage in St. Louis County for 2026. We start by confirming your doctors and hospital are covered, then compare premiums."],
         systems=["Essentia Health&ndash;St. Mary&rsquo;s Medical Center", "Aspirus St. Luke&rsquo;s", "Essentia Health clinics", "Community Memorial (Cloquet)"],
         communities="Duluth, Hermantown, Proctor, Cloquet, Two Harbors, Esko, Rice Lake, Lakeside, Woodland, Superior-area families",
         faqs=[("Are Medicare Cost plans available in Duluth?", "Yes. St. Louis County is one of the 21 Minnesota counties where Cost plans are still offered, sold by Blue Cross Blue Shield of Minnesota and Medica. Premiums and availability are published each year by the Minnesota Department of Commerce, and we compare them against Advantage and supplement options."),
               ("Which plans include Essentia and Aspirus St. Luke&rsquo;s?", "Each system contracts with some plans and not others, and the lists change every October. Original Medicare with a supplement covers both without a network. We confirm your doctors against the plan directory before you enroll."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["brainerd", "st-cloud"]),
    dict(slug="bloomington", name="Bloomington", county="Hennepin County", region="twin-cities", scene="skyline",
         sub="Bloomington, Richfield and Edina retirees sit within reach of Fairview Southdale, Park Nicollet and Allina &mdash; and within the metro&rsquo;s widest plan menu.",
         intro=["South-metro Hennepin County has the full Twin Cities plan lineup, and its care is spread across Fairview Southdale in Edina, Park Nicollet (HealthPartners) in St. Louis Park and Bloomington, and Allina clinics. A Medicare Advantage plan that includes one may exclude another, so we check the network before the premium.",
                "Cost plans left Hennepin County in 2019. The choice is Medicare Advantage or Original Medicare with a Minnesota supplement; we compare both with your doctors and prescriptions in hand."],
         systems=["M Health Fairview Southdale", "Park Nicollet (HealthPartners)", "Allina Health clinics", "Abbott Northwestern"],
         communities="Bloomington, Richfield, Edina, Eden Prairie, Savage, Burnsville border",
         faqs=[("Which Medicare plans are available in Bloomington?", "The full Hennepin County lineup: many Medicare Advantage plans, every Medicare supplement carrier in Minnesota, and all standalone Part D plans. We compare what is offered at your ZIP code."),
               ("Is Fairview Southdale in my Advantage plan&rsquo;s network?", "It depends on the plan and the year. We confirm your hospital and doctors are in-network before you enroll, or steer you to a supplement if you want no network at all."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["minneapolis", "eagan", "burnsville"]),
    dict(slug="brooklyn-park", name="Brooklyn Park", county="Hennepin County", region="twin-cities", scene="skyline",
         sub="Brooklyn Park, Brooklyn Center, Champlin and Crystal &mdash; north-metro households with North Memorial and Maple Grove Hospital close by and the full metro plan menu.",
         intro=["The north metro is North Memorial territory, with Maple Grove Hospital and the Robbinsdale campus, plus Allina and HealthPartners clinics. Medicare Advantage networks split those systems differently, and after UCare&rsquo;s exit and Humana&rsquo;s departure from Hennepin County for 2026 many north-metro residents were re-shopping.",
                "We compare the plans actually offered at your ZIP code, confirm your doctors and pharmacy, and set Advantage beside a Minnesota supplement so you can see the trade-off plainly."],
         systems=["North Memorial Health", "Maple Grove Hospital", "Allina Health clinics", "HealthPartners clinics"],
         communities="Brooklyn Park, Brooklyn Center, Champlin, Crystal, Osseo, New Hope, Robbinsdale",
         faqs=[("Which Medicare plans are available in Brooklyn Park?", "The full Hennepin County lineup of Medicare Advantage, Medicare supplement and Part D plans. Availability is set by ZIP code and changes each plan year."),
               ("Is North Memorial in my plan&rsquo;s network?", "North Memorial contracts with some Medicare Advantage plans and not others. With Original Medicare and a supplement there is no network. We confirm before you enroll."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["maple-grove", "plymouth", "minneapolis"]),
    dict(slug="plymouth", name="Plymouth", county="Hennepin County", region="twin-cities", scene="lakes",
         sub="Plymouth, Wayzata, Minnetonka and Golden Valley &mdash; west-metro retirees with Abbott Northwestern&ndash;WestHealth, North Memorial and Park Nicollet nearby.",
         intro=["The west metro has the full Hennepin County plan lineup and care spread across Allina&rsquo;s WestHealth campus, North Memorial, Park Nicollet and M Health Fairview. Which of them a given Medicare Advantage plan includes is the first thing we check.",
                "Cost plans ended here in 2019. We compare Medicare Advantage against Original Medicare with a Minnesota supplement, with your doctors, prescriptions and travel plans on the table."],
         systems=["Abbott Northwestern&ndash;WestHealth (Allina)", "North Memorial Health", "Park Nicollet (HealthPartners)", "M Health Fairview"],
         communities="Plymouth, Wayzata, Minnetonka, Golden Valley, Medina, Maple Plain, Orono",
         faqs=[("Which Medicare plans are available in Plymouth?", "The full Hennepin County lineup of Medicare Advantage, Medicare supplement and Part D plans, set by ZIP code and changing each plan year."),
               ("I travel a lot. Which plan should I look at?", "A Minnesota Basic or Extended Basic supplement works anywhere in the country with any provider that accepts Medicare. Most Medicare Advantage plans cover only emergencies outside their area, and some PPO plans offer more. We lay both out."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["maple-grove", "brooklyn-park", "minneapolis"]),
    dict(slug="woodbury", name="Woodbury", county="Washington County", region="twin-cities", scene="lakes",
         sub="Woodbury, Oakdale, Cottage Grove, Stillwater and Lake Elmo &mdash; east-metro retirees with Woodwinds, Regions and HealthPartners close by and the St. Croix an easy drive.",
         intro=["Washington County shares the metro plan lineup, and care is anchored by M Health Fairview Woodwinds, HealthPartners&rsquo; Woodbury clinics and Regions Hospital in St. Paul. Some plans reach across the river into Wisconsin and some do not &mdash; worth checking if your doctor is in Hudson.",
                "We compare what is actually offered at your ZIP code, including Medicare Advantage against Original Medicare with a Minnesota supplement, and confirm your providers before you enroll."],
         systems=["M Health Fairview Woodwinds", "HealthPartners Woodbury", "Regions Hospital", "Lakeview Hospital (Stillwater)"],
         communities="Woodbury, Oakdale, Cottage Grove, Lake Elmo, Stillwater, Afton, Bayport",
         faqs=[("Which Medicare plans are available in Woodbury?", "Washington County residents can choose among many Medicare Advantage plans, every Medicare supplement carrier in Minnesota and the full Part D lineup. Availability is set by ZIP code and changes each plan year."),
               ("Can I keep a doctor in Hudson, Wisconsin?", "With Original Medicare and a supplement, yes. With a Medicare Advantage plan, only if that provider is in-network; some east-metro plans include western Wisconsin providers and some do not. We confirm first."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["st-paul", "eagan"]),
    dict(slug="maple-grove", name="Maple Grove", county="Hennepin County", region="twin-cities", scene="lakes",
         sub="Maple Grove, Osseo, Rogers and Champlin &mdash; a fast-growing northwest-metro area with Maple Grove Hospital at its centre and the full metro plan menu.",
         intro=["Maple Grove Hospital and the North Memorial and Fairview clinics around it serve the northwest metro; Allina and HealthPartners have clinics nearby too. Medicare Advantage networks split those systems, so we check the network before the premium.",
                "Cost plans left Hennepin County in 2019. We compare Advantage against Original Medicare with a Minnesota supplement with your doctors and prescriptions in front of us."],
         systems=["Maple Grove Hospital", "North Memorial Health", "M Health Fairview clinics", "Allina Health clinics"],
         communities="Maple Grove, Osseo, Rogers, Champlin, Corcoran, Dayton, Hanover",
         faqs=[("Which Medicare plans are available in Maple Grove?", "The full Hennepin County lineup of Medicare Advantage, Medicare supplement and Part D plans, set by ZIP code and changing each plan year."),
               ("Is Maple Grove Hospital in my Advantage plan&rsquo;s network?", "It depends on the plan and the year. We confirm your hospital and doctors are in-network before you enroll."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["brooklyn-park", "plymouth"]),
    dict(slug="st-cloud", name="St. Cloud", county="Stearns County", region="central-minnesota", scene="lakes",
         sub="St. Cloud, Sartell, Sauk Rapids and Waite Park &mdash; Central Minnesota&rsquo;s hub, where CentraCare is the network question and the plan lineup is broader than most of outstate Minnesota.",
         intro=["CentraCare&rsquo;s St. Cloud Hospital and its clinics dominate care in Stearns, Benton and Sherburne counties, and it contracts differently with each Medicare Advantage carrier. Original Medicare with a Minnesota supplement covers CentraCare without a network question; an Advantage plan needs checking each year.",
                "Stearns County is not a Cost-plan county, so the choice is Advantage or Original Medicare plus a supplement and Part D. The St. Cloud VA is a second consideration for the area&rsquo;s many veterans; see our veterans guide."],
         systems=["CentraCare&ndash;St. Cloud Hospital", "CentraCare clinics", "St. Cloud VA Health Care System"],
         communities="St. Cloud, Sartell, Sauk Rapids, Waite Park, St. Joseph, St. Augusta, Foley, Cold Spring",
         faqs=[("Which Medicare plans are available in St. Cloud?", "Stearns County residents can choose among several Medicare Advantage plans, every Medicare supplement carrier in Minnesota and the full Part D lineup. Cost plans are not sold in Stearns County."),
               ("Does CentraCare take Medicare Advantage?", "CentraCare accepts Original Medicare and contracts with some Medicare Advantage plans and not others, changing year to year. We confirm the plan&rsquo;s CentraCare status before you enroll."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["brainerd", "maple-grove"]),
    dict(slug="eagan", name="Eagan", county="Dakota County", region="twin-cities", scene="skyline",
         sub="Eagan, Apple Valley, Inver Grove Heights and Rosemount &mdash; south-metro Dakota County, with Fairview Ridges, Allina and HealthPartners nearby and the full metro plan menu.",
         intro=["Dakota County has the metro&rsquo;s wide plan lineup, and care is spread across M Health Fairview Ridges in Burnsville, Allina and HealthPartners clinics, and the St. Paul hospitals a short drive north. Medicare Advantage networks include different combinations of those, so we check yours first.",
                "Cost plans ended in Dakota County in 2019. We compare Advantage against Original Medicare with a Minnesota supplement, using your doctors, pharmacy and budget."],
         systems=["M Health Fairview Ridges", "Allina Health clinics", "HealthPartners clinics", "Regions &amp; United (St. Paul)"],
         communities="Eagan, Apple Valley, Inver Grove Heights, Rosemount, Mendota Heights, West St. Paul, South St. Paul",
         faqs=[("Which Medicare plans are available in Eagan?", "The full Dakota County lineup of Medicare Advantage, Medicare supplement and Part D plans, set by ZIP code and changing each plan year."),
               ("Is Fairview Ridges in my plan&rsquo;s network?", "It depends on the plan and the year. We confirm your hospital and doctors are in-network before you enroll."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["burnsville", "st-paul", "bloomington"]),
    dict(slug="burnsville", name="Burnsville", county="Dakota County", region="twin-cities", scene="lakes",
         sub="Burnsville, Savage, Lakeville and Prior Lake &mdash; the southwest metro, home to Fairview Ridges and a growing retiree population with the full metro plan menu.",
         intro=["Fairview Ridges in Burnsville anchors care for the southwest metro, with Allina, HealthPartners and Park Nicollet clinics close by. Medicare Advantage networks here vary by carrier, and the lineup shifted after the 2026 carrier exits.",
                "We compare Advantage against Original Medicare with a Minnesota supplement, with your doctors, prescriptions and travel in the picture."],
         systems=["M Health Fairview Ridges", "Allina Health clinics", "Park Nicollet (HealthPartners)", "Ridgeview (Chaska)"],
         communities="Burnsville, Savage, Lakeville, Prior Lake, Apple Valley, Shakopee",
         faqs=[("Which Medicare plans are available in Burnsville?", "The full Dakota County lineup of Medicare Advantage, Medicare supplement and Part D plans, set by ZIP code and changing each plan year."),
               ("Should I look at Advantage or a supplement?", "Neither is automatically better. Advantage plans bundle extras and often carry a $0 premium but use a network; a Minnesota Basic or Extended Basic supplement costs a monthly premium and works anywhere. We compare both against your doctors and budget."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["eagan", "bloomington", "rochester"]),
    dict(slug="mankato", name="Mankato", county="Blue Earth County", region="southwest-minnesota", scene="bluffs",
         sub="Mankato, North Mankato, St. Peter and the Minnesota River valley &mdash; Mayo Clinic Health System country, with several Cost-plan counties a short drive away.",
         intro=["Mayo Clinic Health System&rsquo;s Mankato hospital and clinics dominate care here, and like Mayo in Rochester they accept Original Medicare and contract selectively with Medicare Advantage plans. A Minnesota supplement keeps Mayo in reach with no network question.",
                "Blue Earth and Nicollet counties are not Cost-plan counties, but neighbouring Le Sueur and Sibley counties are, which changes the comparison for residents just up the road."],
         systems=["Mayo Clinic Health System&ndash;Mankato", "Mayo Clinic Health System clinics", "River&rsquo;s Edge Hospital (St. Peter)"],
         communities="Mankato, North Mankato, St. Peter, Eagle Lake, Lake Crystal, Madison Lake, Le Sueur",
         faqs=[("Does Mayo Clinic Health System in Mankato take Medicare Advantage?", "It accepts Original Medicare and contracts with some Medicare Advantage plans and not others, changing year to year. We confirm the plan&rsquo;s Mayo status before you enroll."),
               ("Are there Cost plans near Mankato?", "Not in Blue Earth or Nicollet counties. Le Sueur and Sibley counties, just north, are on the state&rsquo;s list of 21 Cost-plan counties for 2026."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["rochester", "burnsville"]),
    dict(slug="moorhead", name="Moorhead", county="Clay County", region="northwest-minnesota", scene="prairie",
         sub="Moorhead, Dilworth, Barnesville and Hawley &mdash; where your hospital is probably in Fargo, and your plan needs to know that.",
         intro=["Clay County residents get most of their care across the river at Sanford Health and Essentia Health in Fargo. Original Medicare and a Minnesota supplement cover them without a second thought; a Medicare Advantage plan sold in Clay County has to include Fargo providers in its network, and not all do.",
                "Clay County is not a Cost-plan county. We compare the Advantage plans that actually reach Fargo against a Basic or Extended Basic supplement plus Part D."],
         systems=["Sanford Health (Fargo)", "Essentia Health (Fargo)", "Sanford &amp; Essentia clinics in Moorhead"],
         communities="Moorhead, Dilworth, Barnesville, Hawley, Glyndon, Sabin, Detroit Lakes-area families",
         faqs=[("Can a Minnesota Medicare plan cover Sanford or Essentia in Fargo?", "With Original Medicare and a supplement, yes. With a Medicare Advantage plan, only if Fargo providers are in that plan&rsquo;s network, which we confirm before you enroll."),
               ("Which Medicare plans are available in Moorhead?", "Clay County has a smaller Medicare Advantage lineup than the metro, every Medicare supplement carrier in Minnesota, and the full Part D lineup. Cost plans are not sold in Clay County."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["bemidji", "st-cloud"]),
    dict(slug="brainerd", name="Brainerd", county="Crow Wing County", region="central-minnesota", scene="lakes",
         sub="Brainerd, Baxter, Nisswa, Crosslake and Pequot Lakes &mdash; the Brainerd Lakes, where a lot of Minnesotans retire to the cabin and need a plan that fits life at the lake.",
         intro=["Essentia Health&ndash;St. Joseph&rsquo;s in Brainerd and Cuyuna Regional in Crosby serve the lakes area, and each contracts differently with Medicare Advantage carriers. If you moved here full time from the metro, your old plan may not be sold in Crow Wing County; the move gives you a Special Enrollment Period to switch.",
                "Crow Wing County is not on the Cost-plan list (Aitkin and Mille Lacs, next door, are). We compare Advantage against Original Medicare with a Minnesota supplement, with winters away in mind."],
         systems=["Essentia Health&ndash;St. Joseph&rsquo;s Medical Center", "Cuyuna Regional Medical Center", "Lakewood Health System (Staples)"],
         communities="Brainerd, Baxter, Nisswa, Crosslake, Pequot Lakes, Crosby, Pine River, Little Falls",
         faqs=[("I moved to the lake full time. Do I have to change plans?", "If your Medicare Advantage, Part D or Cost plan is not offered in Crow Wing County, moving gives you a Special Enrollment Period to pick one that is. A Minnesota supplement follows you without a change."),
               ("Are Cost plans available in Brainerd?", "Not in Crow Wing County. Aitkin and Mille Lacs counties, nearby, are on the state&rsquo;s list of 21 Cost-plan counties for 2026."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["st-cloud", "duluth"]),
    dict(slug="bemidji", name="Bemidji", county="Beltrami County", region="northwest-minnesota", scene="aurora",
         sub="Bemidji, Bagley, Blackduck, Cass Lake and Walker &mdash; the first city on the Mississippi, with Sanford Bemidji at its centre and long drives everywhere else.",
         intro=["Sanford Bemidji Medical Center is the region&rsquo;s hospital, with tribal health and small critical-access hospitals filling in across Beltrami, Clearwater, Cass and Hubbard counties. Medicare Advantage networks are thinner up here than in the metro, and the lineup changed for 2026 as carriers trimmed rural counties.",
                "Beltrami County is not a Cost-plan county. For many Bemidji-area retirees, Original Medicare with a Minnesota Basic or Extended Basic supplement is the plan that keeps every hospital in the state on the table."],
         systems=["Sanford Bemidji Medical Center", "Sanford clinics", "Red Lake &amp; Cass Lake IHS facilities"],
         communities="Bemidji, Bagley, Blackduck, Cass Lake, Walker, Park Rapids, Kelliher",
         faqs=[("Which Medicare plans are available in Bemidji?", "Beltrami County has a smaller Medicare Advantage lineup than the metro, every Medicare supplement carrier in Minnesota and the full Part D lineup. Cost plans are not sold in Beltrami County."),
               ("Does Sanford Bemidji take Medicare Advantage?", "Sanford accepts Original Medicare and contracts with some Medicare Advantage plans and not others. We confirm the plan&rsquo;s status with Sanford before you enroll."),
               ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans and reviewing your coverage each year is free to you.")],
         nearby=["moorhead", "brainerd"]),
]
CITY = {c["slug"]: c for c in CITIES}

# ----------------------------------------------------------------------------
# Shared fragments
# ----------------------------------------------------------------------------
def fill(s):
    return (s.replace("[[PHONE]]", PHONE).replace("[[TEL]]", TEL).replace("[[EMAIL]]", EMAIL)
             .replace("[[QUOTE]]", QUOTE_URL).replace("[[YEAR]]", str(PLAN_YEAR)))

LOGO = ('<svg class="brand__mark" width="42" height="42" viewBox="0 0 42 42" aria-hidden="true">'
        '<circle cx="21" cy="21" r="20" fill="#1d4f6e"/>'
        '<path d="M21 6l2.6 9.4L33 18l-9.4 2.6L21 30l-2.6-9.4L9 18l9.4-2.6z" fill="#e7c486"/>'
        '<path d="M6 30c5-3 10-3 15 0s10 3 15 0" stroke="#9fc4d8" stroke-width="2" fill="none" stroke-linecap="round"/>'
        '<path d="M10 30l3-7 3 7zM26 30l3-7 3 7z" fill="#2f5d4a"/></svg>')

NAV = [("/medicare-advantage", "Plans"), ("/medicare-supplement", "Medigap"), ("/medicare-cost-plans", "Cost Plans"),
       ("/medicare-costs", "2026 Costs"), ("/turning-65", "Turning 65"), ("/snowbirds", "Snowbirds"), ("/#areas", "Areas")]

def header():
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f'''<a class="skip" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="brand" href="/" aria-label="{ORG} home">
      {LOGO}
      <span><span class="brand__name">{ORG}</span><br>
      <span class="brand__tag">Plain-English Medicare help in Minnesota</span></span>
    </a>
    <nav class="nav" aria-label="Primary">
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="navLinks"><span class="visually-hidden">Menu</span><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
      <ul class="nav__links" id="navLinks">{links}</ul>
      <a class="header-call" href="tel:{TEL}">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6 19.8 19.8 0 01-3.1-8.7A2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .4 1.9.7 2.8a2 2 0 01-.5 2.1L8.1 9.9a16 16 0 006 6l1.3-1.3a2 2 0 012.1-.4c.9.3 1.8.6 2.8.7a2 2 0 011.7 2z"/></svg>
        {PHONE}
      </a>
    </nav>
  </div>
</header>
'''

def footer():
    cities = "".join(f'<li><a href="/{c["slug"]}">{c["name"]}</a></li>' for c in CITIES)
    regions = "".join(f'<li><a href="/{r["slug"]}">{r["name"]}</a></li>' for r in REGIONS)
    net = " &middot; ".join(f'<a href="{u}" rel="noopener">{n}</a>' for n, u in NETWORK)
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <p class="footer-brand">{ORG}</p>
        <p style="margin-bottom:.6em">Plain-English Medicare guidance for Minnesota retirees and people approaching 65. Independent agency &mdash; we work for you, not a single carrier.</p>
        <p><a href="tel:{TEL}"><strong>{PHONE}</strong></a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p style="font-size:.85rem">Darin Weidauer, licensed insurance agent, NPN {NPN}{LIC_TXT}. Statewide by phone and video.</p>
      </div>
      <div><h4>Plans</h4><ul>
        <li><a href="/medicare-advantage">Medicare Advantage</a></li>
        <li><a href="/medicare-supplement">Medicare Supplement (Basic &amp; Extended Basic)</a></li>
        <li><a href="/medicare-cost-plans">Medicare Cost plans</a></li>
        <li><a href="/part-d">Part D drug plans</a></li>
        <li><a href="/chronic-snp">Chronic SNPs</a></li>
        <li><a href="/institutional-snp">Institutional SNPs</a></li>
      </ul></div>
      <div><h4>Resources</h4><ul>
        <li><a href="/retirement-guide">Free retirement guide</a></li>
        <li><a href="/turning-65">Turning 65 in Minnesota</a></li>
        <li><a href="/medicare-costs">{PLAN_YEAR} costs &amp; IRMAA</a></li>
        <li><a href="/snowbirds">Snowbirds &amp; travel</a></li>
        <li><a href="/veterans">Veterans</a></li>
        <li><a href="/medicaid">Medical Assistance &amp; MSHO</a></li>
        <li><a href="/faq">Questions Minnesotans ask</a></li>
        <li><a href="/about">About Darin</a></li>
        <li><a href="/privacy">Privacy</a> &middot; <a href="/terms">Terms</a></li>
      </ul></div>
      <div><h4>Official &amp; independent</h4><ul>
        <li><a href="https://www.medicare.gov" rel="noopener">Medicare.gov</a></li>
        <li><a href="tel:+18006334227">1-800-MEDICARE</a></li>
        <li><a href="https://mn.gov/aging-pathways/" rel="noopener">Minnesota Aging Pathways (Senior LinkAge Line)</a>, 800-333-2433</li>
        <li><a href="https://mn.gov/commerce/" rel="noopener">Minnesota Department of Commerce</a></li>
      </ul></div>
    </div>
    <nav class="footer-areas" aria-label="Areas we serve">
      <h4>Cities we serve</h4><ul>{cities}</ul>
      <h4>Regions</h4><ul>{regions}</ul>
    </nav>
    <div class="footer-net"><span>Our network of sites:</span> {net}</div>
    <div class="disclaimer">
      <p><strong>Medicare disclaimer.</strong> {TPMO}</p>
      <p>{ORG} is not connected with or endorsed by the U.S. government or the federal Medicare program, and is not affiliated with the State of Minnesota, Minnesota Aging Pathways, Minnesota Medical Assistance, the U.S. Department of Veterans Affairs, the Department of Defense, or the TRICARE program. This is a solicitation for insurance. A licensed insurance agent may contact you.</p>
      <p>Insurance products are offered through {ORG}. Darin Weidauer is a licensed insurance agent in Minnesota (NPN {NPN}{LIC_TXT}) and 14 other states. We may receive compensation from insurance carriers for policies we sell; you pay the same premium whether you enroll through us, another agent, or the carrier directly.</p>
      <p>&copy; <span id="yr">{TODAY.year}</span> {ORG}. Not affiliated with any government agency.</p>
    </div>
  </div>
</footer>
<script src="/site.js" defer></script>
<script src="/analytics.js" defer></script>
'''

CONSENT_TEXT = ("By checking the consent box and submitting this form, I give ECOS Medicare Solutions and a licensed insurance agent "
                "permission to contact me at the phone number and email I provided — including by phone call, text message (SMS), and email, "
                "using automated technology such as an autodialer or prerecorded/artificial voice — about Medicare Advantage, Medicare Supplement, "
                "Medicare Cost, and Part D plan options. I understand consent is not a condition of purchase and that message and data rates may apply, "
                "and that I can opt out at any time.")

def lead_form(form_id, title="Request your free Medicare review", note=None, interest=True):
    note = note or f'Tell us a little about you and Darin will reach out. Prefer to talk now? Call <a href="tel:{TEL}"><strong>{PHONE}</strong></a>.'
    sel = ""
    if interest:
        sel = '''<div class="field"><label for="interest">What can we help with? (optional)</label>
          <select id="interest" name="interest"><option value="">Choose one…</option>
            <option>I'm turning 65 soon</option><option>Review my current plan</option><option>My plan was discontinued</option>
            <option>Medicare Advantage</option><option>Medicare Supplement (Basic / Extended Basic)</option><option>Medicare Cost plan</option>
            <option>Part D drug plan</option><option>I winter in another state</option><option>I have VA / TRICARE</option><option>I have Medical Assistance too</option>
          </select></div>'''
    return f'''<div class="lead-card" id="get-help">
      <h2 class="lead-card__title">{title}</h2>
      <p class="lead-card__note">{note}</p>
      <form id="{form_id}" action="https://api.web3forms.com/submit" method="POST">
        <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
        <input type="hidden" name="subject" value="New Medicare review request — Minnesotamedicareenrollment.com">
        <input type="hidden" name="from_name" value="Minnesota Medicare Enrollment">
        <input type="hidden" name="redirect" value="{SITE_URL}/thank-you">
        <input type="hidden" name="consent_text" value="{html.escape(CONSENT_TEXT, quote=True)}">
        <input type="hidden" name="consent_timestamp" id="consent_timestamp" value="">
        <div class="field"><label for="name">Your name</label><input id="name" name="name" type="text" autocomplete="name" required></div>
        <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required></div>
        <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="zip">ZIP code or city</label><input id="zip" name="zip_or_city" type="text" autocomplete="postal-code" required></div>
        {sel}
        <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="consent"><input id="consent" name="consent" type="checkbox" required>
          <label for="consent">By checking this box and submitting, I give ECOS Medicare Solutions and a licensed agent permission to contact me at the number and email above &mdash; by phone call, text (SMS), and email, including with automated technology &mdash; about Medicare plan options. Consent is not a condition of purchase. Message &amp; data rates may apply; I can opt out anytime.</label>
        </div>
        <button class="btn btn--primary btn--block btn--lg" type="submit">Get my free review</button>
        <p class="form-fineprint">We never ask about your health on this form. See our <a href="/privacy">Privacy Policy</a>. This is a solicitation for insurance. Not connected with or endorsed by the U.S. government or the federal Medicare program.</p>
      </form>
    </div>'''

def crumbs(items):
    """items: list of (name, path) — last has path None"""
    parts = []
    for name, path in items:
        parts.append(f'<a href="{path}">{name}</a>' if path else f'<span>{name}</span>')
    return ('<div class="wrap" style="padding-top:1.1rem"><nav class="eyebrow crumb" aria-label="Breadcrumb">'
            + ' <span aria-hidden="true">/</span> '.join(parts) + '</nav></div>')

def hero(scene, eyebrow, h1, sub, crumb_items, form_id, form_title="Talk it through with Darin", primary_label=None):
    primary = primary_label or f"Call {PHONE}"
    return f'''<section class="hero">
  <div class="hero__scene" aria-hidden="true">{SCENES[scene]}</div>
  {crumbs(crumb_items)}
  <div class="wrap hero__inner" style="padding-top:.5rem">
    <div>
      <p class="eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      <p class="hero__sub">{sub}</p>
      <div class="hero__actions">
        <a class="btn btn--primary btn--lg" href="tel:{TEL}">{primary}</a>
        <a class="btn btn--ghost btn--lg" href="#get-help">Request a free review</a>
      </div>
      <p class="hero__nocost"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> No cost, no obligation, no pressure.</p>
    </div>
    {lead_form(form_id, form_title, f'No cost, no pressure. Prefer to call? <a href="tel:{TEL}"><strong>{PHONE}</strong></a>.')}
  </div>
</section>
'''

def faq_html(faqs, eyebrow="Good to know"):
    items = "".join(f'<details><summary>{q}</summary><div class="faq__a"><p>{a}</p></div></details>' for q, a in faqs)
    return f'''<section class="section section--paper2"><div class="wrap">
<p class="eyebrow center">{eyebrow}</p><h2 class="center">Frequently asked questions</h2>
<div class="faq" style="margin-top:1.6rem">{items}</div></div></section>
'''

def keyfacts(items):
    if not items:
        return ""
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<aside class="keyfacts" aria-label="Key facts"><p class="keyfacts__title">At a glance</p><ul>{lis}</ul></aside>'

def sources(items):
    if not items:
        return ""
    lis = "".join(f'<li><a href="{u}" rel="noopener">{n}</a></li>' for n, u in items)
    return f'<section class="section" style="padding-top:0"><div class="wrap"><div class="sources"><h2>Sources we used on this page</h2><ul>{lis}</ul><p>Figures are checked against the source at the review date in the byline below. If a source has changed since, the source wins.</p></div></div></section>'

def cta(h2, lede="A short, friendly conversation &mdash; no pressure, no cost."):
    return f'''<section class="section section--lake cta-strip"><div class="wrap">
<p class="eyebrow center">Ready when you are</p><h2>{h2}</h2>
<p class="lede" style="color:#dfe8ee;margin-inline:auto">{lede}</p>
<div class="cta-actions">
<a class="btn btn--gold btn--lg" href="tel:{TEL}">Call {PHONE}</a>
<a class="btn btn--ghost btn--lg" href="#get-help" style="color:#fff;border-color:#fff">Request a free review</a>
<a class="btn btn--ghost btn--lg" href="{QUOTE_URL}" target="_blank" rel="noopener" style="color:#fff;border-color:#fff">Get a quote online</a>
</div></div></section>
'''

def byline():
    return f'''<section class="section" style="padding-top:0"><div class="wrap">
<div class="byline">
<img src="/darin.jpg" alt="Darin Weidauer" width="52" height="52" loading="lazy">
<p>Written and reviewed by <a href="/about"><strong>Darin Weidauer</strong></a> &mdash; licensed insurance agent (NPN {NPN}{LIC_TXT}), Gerontologist (USC Leonard Davis School of Gerontology), MBA, Registered Social Security Analyst, and 22-year U.S. Air Force veteran.<span class="rev">Last reviewed {REVIEWED}. Plan availability, benefits and costs change every plan year &mdash; verify current details at <a href="https://www.medicare.gov" rel="noopener">Medicare.gov</a>, 1-800-MEDICARE, or Minnesota Aging Pathways at 800-333-2433.</span></p>
</div></div></section>
'''

# ----------------------------------------------------------------------------
# Structured data
# ----------------------------------------------------------------------------
def org_graph(area=None):
    area = area or {"@type": "State", "name": "Minnesota"}
    return {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "InsuranceAgency", "@id": f"{SITE_URL}/#org", "name": ORG, "alternateName": SITE_NAME,
             "url": f"{SITE_URL}/", "telephone": TEL, "email": EMAIL,
             "description": "Independent Medicare insurance agency helping Minnesota retirees and people approaching 65 compare Medicare Advantage, Medicare Cost plans, Minnesota Basic and Extended Basic supplements, and Part D plans at no cost.",
             "areaServed": area,
             "knowsAbout": ["Medicare Advantage", "Medicare Cost plans", "Medicare Supplement", "Minnesota Basic and Extended Basic Medigap plans",
                            "Medicare Part D", "Special Needs Plans", "Minnesota Senior Health Options (MSHO)", "Medicare and Medical Assistance dual eligibility",
                            "Medicare for snowbirds"],
             "founder": {"@id": f"{SITE_URL}/#darin"}, "sameAs": SAMEAS_ORG,
             "image": f"{SITE_URL}/og-image.png", "logo": f"{SITE_URL}/favicon.svg", "priceRange": "Free consultation"},
            {"@type": "WebSite", "@id": f"{SITE_URL}/#website", "url": f"{SITE_URL}/", "name": SITE_NAME,
             "publisher": {"@id": f"{SITE_URL}/#org"}, "inLanguage": "en-US"},
            {"@type": "Person", "@id": f"{SITE_URL}/#darin", "name": "Darin Weidauer", "honorificSuffix": "MBA, RSSA",
             "image": f"{SITE_URL}/darin.jpg", "url": f"{SITE_URL}/about",
             "jobTitle": "Independent Medicare Insurance Agent & Gerontologist",
             "identifier": [{"@type": "PropertyValue", "propertyID": "NPN", "value": NPN}, {"@type": "PropertyValue", "propertyID": "Minnesota insurance license", "value": LIC}],
             "worksFor": {"@id": f"{SITE_URL}/#org"},
             "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Pepperdine University"},
                          {"@type": "CollegeOrUniversity", "name": "University of Southern California"}],
             "hasCredential": [{"@type": "EducationalOccupationalCredential", "credentialCategory": "Registered Social Security Analyst (RSSA)"},
                               {"@type": "EducationalOccupationalCredential", "credentialCategory": "Credentialed Gerontologist"},
                               {"@type": "EducationalOccupationalCredential", "credentialCategory": "Licensed insurance agent, Minnesota (NPN 18580338, MN License #40620754)"}],
             "knowsAbout": ["Medicare", "Medigap", "Social Security claiming", "Gerontology", "Retirement planning"],
             "sameAs": SAMEAS_DARIN},
        ],
    }

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + '</script>'

def unesc(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))

def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": unesc(q), "acceptedAnswer": {"@type": "Answer", "text": unesc(a)}} for q, a in faqs],
            "datePublished": ISO, "dateModified": ISO, "author": {"@id": f"{SITE_URL}/#darin"}, "reviewedBy": {"@id": f"{SITE_URL}/#darin"}, "inLanguage": "en-US"}

def crumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": unesc(n), "item": SITE_URL + (p if p else "")}
                                for i, (n, p) in enumerate(items)]}

# ----------------------------------------------------------------------------
# Page shell
# ----------------------------------------------------------------------------
def page(path, title, desc, body, schemas, ogtype="website", extra_head="", noindex=False):
    canonical = SITE_URL + ("/" if path == "index" else f"/{path}")
    robots = '<meta name="robots" content="noindex, nofollow">' if noindex else '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">'
    head = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(unesc(desc), quote=True)}">
{robots}
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#1d4f6e">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta name="author" content="Darin Weidauer">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{html.escape(unesc(title), quote=True)}">
<meta property="og:description" content="{html.escape(unesc(desc), quote=True)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/og-image.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Minnesota Medicare Enrollment — ECOS Medicare Solutions">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(unesc(title), quote=True)}">
<meta name="twitter:description" content="{html.escape(unesc(desc), quote=True)}">
<meta name="twitter:image" content="{SITE_URL}/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/site.css">
{extra_head}
{"".join(ld(s) for s in schemas)}
</head>
<body>
'''
    out = head + header() + '<main id="main">\n' + body + '</main>\n' + footer() + '</body>\n</html>\n'
    (ROOT / f"{path}.html").write_text(fill(out), encoding="utf-8")
    return canonical

PAGES = []   # (canonical, lastmod, priority)
def register(canonical, priority="0.6", lastmod=ISO):
    PAGES.append((canonical, lastmod, priority))

# ----------------------------------------------------------------------------
# Builders
# ----------------------------------------------------------------------------
def build_topic(p):
    slug = p["slug"]
    items = [("Home", "/")] + p.get("crumb_parents", []) + [(p["crumb"], None)]
    body = hero(p["scene"], p["eyebrow"], p["h1"], p["sub"], items, slug, p.get("form_title", "Talk it through with Darin"))
    body += f'<section class="section"><div class="wrap prose">{keyfacts(p.get("keyfacts"))}{p["body"]}</div></section>\n'
    body += faq_html(p["faqs"])
    body += cta(p["cta"])
    body += sources(p.get("sources"))
    body += byline()
    schemas = [org_graph(), crumb_ld(items),
               {"@context": "https://schema.org", "@type": p.get("schema_type", "Article"), "headline": unesc(p["h1"]),
                "description": unesc(p["desc"]), "url": f"{SITE_URL}/{slug}", "mainEntityOfPage": f"{SITE_URL}/{slug}",
                "author": {"@id": f"{SITE_URL}/#darin"}, "publisher": {"@id": f"{SITE_URL}/#org"}, "reviewedBy": {"@id": f"{SITE_URL}/#darin"},
                "datePublished": ISO, "dateModified": ISO, "inLanguage": "en-US", "isPartOf": {"@id": f"{SITE_URL}/#website"},
                "about": p.get("about", "Medicare in Minnesota"), "image": f"{SITE_URL}/og-image.png"},
               faq_ld(p["faqs"])]
    canonical = page(slug, p["title"], p["desc"], body, schemas, ogtype="article")
    register(canonical, p.get("priority", "0.8"))

def place_options_grid():
    return '''<div class="grid grid--4" style="margin-top:1.6rem">
      <article class="card"><h3>Medicare Advantage</h3><p>All-in-one Part C plans, often $0 premium, that use a local network &mdash; so your providers and prescriptions matter.</p><a class="card__link" href="/medicare-advantage">How Advantage works <span aria-hidden="true">&rarr;</span></a></article>
      <article class="card"><h3>Minnesota Medigap</h3><p>Basic and Extended Basic supplements pair with Original Medicare and let you see any provider nationwide that accepts Medicare.</p><a class="card__link" href="/medicare-supplement">Basic vs Extended Basic <span aria-hidden="true">&rarr;</span></a></article>
      <article class="card"><h3>Medicare Cost plans</h3><p>Still sold in 21 Minnesota counties: a local network at home, Original Medicare everywhere else.</p><a class="card__link" href="/medicare-cost-plans">Where Cost plans remain <span aria-hidden="true">&rarr;</span></a></article>
      <article class="card"><h3>Part D drug plans</h3><p>Standalone drug coverage chosen around your medications. [[YEAR]] out-of-pocket cap: $2,100.</p><a class="card__link" href="/part-d">How Part D works <span aria-hidden="true">&rarr;</span></a></article>
    </div>'''

def build_city(c):
    r = REGION[c["region"]]
    items = [("Home", "/"), (r["short"], f"/{r['slug']}"), (c["name"], None)]
    sysl = "".join(f"<li>{s}</li>" for s in c["systems"])
    nearby = "".join(f'<a class="loc" href="/{n}">{CITY[n]["name"]} <span aria-hidden="true">&rarr;</span></a>' for n in c["nearby"])
    body = hero(c["scene"], f"Medicare help · {r['name']}", f"Medicare help in {c['name']}, Minnesota", c["sub"], items, c["slug"], "Request your free Medicare review")
    body += f'''<section class="section"><div class="wrap">
    <p class="eyebrow">Medicare in {c['name']}</p>
    <h2>What to know before you compare plans in {c['county']}</h2>
    {"".join(f"<p>{para}</p>" for para in c["intro"])}
    <div class="grid grid--3" style="margin-top:1.8rem">
      <article class="card">
        <svg class="card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 21V8l9-5 9 5v13"/><path d="M9 21v-6h6v6"/><path d="M10 11h4"/></svg>
        <h3>Care close to home</h3><p>Major care in the area includes:</p>
        <ul class="creds" style="margin-top:.2rem">{sysl}</ul>
        <p style="font-size:.95rem;margin-top:.6rem">Plan networks differ &mdash; we check that your doctors and hospital are covered before you enroll.</p>
      </article>
      <article class="card">
        <svg class="card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 21s-7-5.2-7-11a7 7 0 0114 0c0 5.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>
        <h3>Communities we serve</h3><p>{c['communities']}.</p>
      </article>
      <article class="card">
        <svg class="card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
        <h3>When you can enroll</h3><p>Turning 65? Your Initial Enrollment Period is the 7 months around your birthday. Already on Medicare? The Annual Election Period is Oct 15&ndash;Dec 7, and Medicare Advantage Open Enrollment runs Jan 1&ndash;Mar 31. Cost plans, where sold, accept enrollment year-round.</p>
      </article>
    </div></div></section>
<section class="section section--paper2"><div class="wrap">
    <p class="eyebrow">Your options</p><h2>Which kind of plan fits you in {c['name']}?</h2>{place_options_grid()}</div></section>
'''
    body += faq_html(c["faqs"], f"Questions from {c['name']}")
    body += f'''<section class="section"><div class="wrap"><p class="eyebrow">Nearby</p><h2>Medicare help in neighboring areas</h2>
    <div class="loc-grid" style="margin-top:1.4rem">{nearby}<a class="loc" href="/{r['slug']}">All of {r['name']} <span aria-hidden="true">&rarr;</span></a></div></div></section>
'''
    body += cta(f"Let&rsquo;s find your {c['name']} Medicare plan together.")
    body += byline()
    area = {"@type": "City", "name": c["name"], "containedInPlace": {"@type": "State", "name": "Minnesota"}}
    local = {"@context": "https://schema.org", "@type": "InsuranceAgency", "name": f"{ORG} — {c['name']}",
             "url": f"{SITE_URL}/{c['slug']}", "telephone": TEL,
             "description": unesc(f"Free, no-pressure Medicare help in {c['name']} and {c['county']}. Compare Medicare Advantage, Minnesota Medigap, Cost plans & Part D with a licensed independent agent."),
             "areaServed": [{"@type": "City", "name": f"{c['name']}, Minnesota"}, {"@type": "AdministrativeArea", "name": f"{c['county']}, Minnesota"}],
             "parentOrganization": {"@id": f"{SITE_URL}/#org"}, "image": f"{SITE_URL}/og-image.png", "priceRange": "Free consultation"}
    title = f"Medicare Plans in {c['name']}, MN {PLAN_YEAR} | {ORG}"
    desc = f"Free Medicare help in {c['name']} and {c['county']}: compare Medicare Advantage, Minnesota Medigap, Cost plans and Part D with a licensed independent agent."
    canonical = page(c["slug"], title, desc, body, [org_graph(area), local, crumb_ld(items), faq_ld(c["faqs"])])
    register(canonical, "0.6")

def build_region(r):
    items = [("Home", "/"), (r["name"], None)]
    sysl = "".join(f"<li>{s}</li>" for s in r["systems"])
    cities = "".join(f'<a class="loc" href="/{s}">{CITY[s]["name"]} <span aria-hidden="true">&rarr;</span></a>' for s in r["cities"])
    cost = (f'<p><strong>Cost-plan counties in this region ({PLAN_YEAR}):</strong> {", ".join(r["cost"])}. See <a href="/medicare-cost-plans">where Medicare Cost plans remain in Minnesota</a>.</p>'
            if r["cost"] else '<p><strong>Cost plans:</strong> none of the counties in this region are on the state&rsquo;s list of Cost-plan counties; the choice is Medicare Advantage or Original Medicare with a <a href="/medicare-supplement">Minnesota supplement</a>.</p>')
    body = hero(r["scene"], r["eyebrow"], r["h1"], r["sub"], items, r["slug"], "Request your free Medicare review")
    body += f'''<section class="section"><div class="wrap">
    <p class="eyebrow">Medicare in the region</p><h2>{r['name']}: what shapes the choice here</h2>
    {"".join(f"<p>{para}</p>" for para in r["intro"])}
    {cost}
    <p><strong>Counties:</strong> {r['counties']}.</p>
    <div class="grid grid--3" style="margin-top:1.8rem">
      <article class="card"><h3>Health systems</h3><ul class="creds" style="margin-top:.2rem">{sysl}</ul><p style="font-size:.95rem;margin-top:.6rem">Each contracts differently with each plan; we check your doctors first.</p></article>
      <article class="card"><h3>Cities in this region</h3><div class="loc-grid" style="margin-top:.6rem">{cities or '<p>We serve every town in the region by phone and video.</p>'}</div></article>
      <article class="card"><h3>When you can enroll</h3><p>Turning 65? Your Initial Enrollment Period is the 7 months around your birthday. Already on Medicare? Annual Election runs Oct 15&ndash;Dec 7; Medicare Advantage Open Enrollment Jan 1&ndash;Mar 31. Cost plans, where sold, accept enrollment year-round.</p></article>
    </div></div></section>
<section class="section section--paper2"><div class="wrap"><p class="eyebrow">Your options</p><h2>Which kind of plan fits you?</h2>{place_options_grid()}</div></section>
'''
    body += faq_html(r["faqs"], f"Questions from {r['short']} Minnesota")
    body += cta(f"Let&rsquo;s find the right plan for life in {r['short'] if r['short'] != 'Twin Cities' else 'the Twin Cities'}.")
    body += byline()
    area = {"@type": "AdministrativeArea", "name": f"{unesc(r['name'])}, Minnesota", "containedInPlace": {"@type": "State", "name": "Minnesota"}}
    title = f"Medicare Help in {unesc(r['name']).split(' &')[0]}, MN {PLAN_YEAR} | {ORG}"
    desc = f"Free Medicare guidance across {unesc(r['name']).split(' &')[0]}: Medicare Advantage, Minnesota Medigap, Cost plans and Part D, compared by a licensed independent agent."
    canonical = page(r["slug"], title, desc, body, [org_graph(area), crumb_ld(items), faq_ld(r["faqs"])])
    register(canonical, "0.6")

def build_home():
    home_faqs = [
        ("How much does it cost to work with ECOS Medicare Solutions?", "There is no cost to you. Independent Medicare agents are paid by the insurance carriers when you enroll, so our help comparing plans, answering questions, and reviewing your coverage each year is free. Your plan premium is the same whether you enroll with our help or on your own."),
        ("What is different about Medicare in Minnesota?", "Three things. Minnesota standardizes Medicare supplements its own way &mdash; Basic and Extended Basic plans with riders, not the A&ndash;N letters used in most states. Medicare Cost plans, retired almost everywhere else, are still sold in 21 Minnesota counties. And people 65 and over who qualify for Medical Assistance can join Minnesota Senior Health Options, which combines Medicare and Medicaid under one plan."),
        ("When can I enroll in or change my Medicare plan in Minnesota?", "Most people first enroll during their Initial Enrollment Period, the seven months around their 65th birthday. After that, the Annual Election Period runs October 15 to December 7 each year, and the Medicare Advantage Open Enrollment Period runs January 1 to March 31. Medicare Cost plans, where they are sold, accept enrollment year-round, and under a law effective August 1, 2026, Minnesotans aged 65 through 70 can also buy a Medicare supplement without health questions, one time, during the Annual Election Period or the Medicare Advantage Open Enrollment Period, with a lasting premium surcharge of 15% to 35%."),
        ("My Medicare Advantage plan was discontinued. What do I do?", "You are not alone: UCare left Medicare Advantage statewide for 2026, and other carriers dropped dozens of counties. A discontinued plan gives you a Special Enrollment Period and, in many cases, a guaranteed-issue right to buy a Medicare supplement without health questions. Call us before the deadline on your plan&rsquo;s notice and we will lay out the options."),
        ("I spend winters in Arizona or Florida. Which plan works?", "A Minnesota Basic or Extended Basic supplement works anywhere in the country with any provider that accepts Medicare, and a Cost plan covers you out of area through Original Medicare. Most Medicare Advantage plans cover only emergencies outside their service area. Our snowbird guide walks through it, and our sister agency has offices in Mesa and Sun City, Arizona."),
        ("Do you offer every Medicare plan available in my area?", f"No &mdash; and we will always be upfront about that. We represent a number of insurance organizations and products in Minnesota, not all of them. The easiest next step is to call us at {PHONE} and we will walk through what fits you. To compare every option on your own, Medicare.gov, 1-800-MEDICARE, and Minnesota Aging Pathways (800-333-2433) have the complete list."),
    ]
    locs = "".join(f'<a class="loc" href="/{c["slug"]}">{c["name"]} <span aria-hidden="true">&rarr;</span></a>' for c in CITIES)
    regs = "".join(f'<a class="loc" href="/{r["slug"]}">{r["name"]} <span aria-hidden="true">&rarr;</span></a>' for r in REGIONS)
    body = f'''<section class="hero">
  <div class="hero__scene" aria-hidden="true">{SCENES["northwoods"]}</div>
  <div class="wrap hero__inner">
    <div>
      <p class="eyebrow">Medicare made clear · Statewide in Minnesota</p>
      <h1>Medicare in Minnesota, explained by someone who actually teaches it.</h1>
      <p class="hero__sub">Turning 65, retiring, or re-shopping because your plan left the state? Sit down with a credentialed independent agent who will walk you through Medicare Advantage, Minnesota&rsquo;s own Medigap plans, Cost plans and Part D in plain English &mdash; patiently, and at no cost to you.</p>
      <div class="hero__actions">
        <a class="btn btn--primary btn--lg" href="tel:{TEL}">Call {PHONE}</a>
        <a class="btn btn--ghost btn--lg" href="#get-help">Request a free review</a>
      </div>
      <p class="hero__nocost"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> No cost, no obligation, no pressure.</p>
    </div>
    {lead_form("home")}
  </div>
</section>
<div class="trust"><div class="wrap trust__inner">
    <span class="trust__item"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/></svg> Licensed in Minnesota &middot; MN License #{LIC} &middot; NPN {NPN}</span>
    <span class="trust__item"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1 3 3 6 3s6-2 6-3v-5"/></svg> Gerontologist &amp; RSSA&reg;</span>
    <span class="trust__item"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="8" r="5"/><path d="M8 13l-2 9 6-4 6 4-2-9"/></svg> 22-year U.S. Air Force veteran</span>
    <span class="trust__item"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg> Always free to you</span>
</div></div>
<section class="section"><div class="wrap">
    <p class="eyebrow">Minnesota is different</p>
    <h2>Three things about Medicare here that the national websites get wrong</h2>
    <p class="lede">Most Medicare advice is written for the 47 states that use the federal plan letters and retired Cost plans years ago. Minnesota did neither. Start with what is actually for sale here.</p>
    <div class="grid grid--3" style="margin-top:2rem">
      <article class="card help-card"><h3>Medigap is Basic or Extended Basic</h3><p>Minnesota, Massachusetts and Wisconsin standardize supplements their own way. There is no &ldquo;Plan G&rdquo; here &mdash; there is a Basic plan, an Extended Basic plan, and riders that build up from Basic. Comparisons from other states do not describe what you can buy.</p><a class="card__link" href="/medicare-supplement">Basic vs Extended Basic <span aria-hidden="true">&rarr;</span></a></article>
      <article class="card help-card"><h3>Cost plans survive in 21 counties</h3><p>Medicare Cost plans &mdash; a local network at home, Original Medicare anywhere else &mdash; ended in the metro in 2019 but are still sold from Duluth to Pipestone. If your county is on the list, it is a third path worth comparing.</p><a class="card__link" href="/medicare-cost-plans">See the county list <span aria-hidden="true">&rarr;</span></a></article>
      <article class="card help-card"><h3>MSHO combines Medicare and Medicaid</h3><p>Minnesotans 65+ with Medical Assistance can join Minnesota Senior Health Options: one plan, one card, one care coordinator for Medicare, Medicaid, drugs and long-term services.</p><a class="card__link" href="/medicaid">Medical Assistance &amp; MSHO <span aria-hidden="true">&rarr;</span></a></article>
    </div>
</div></section>
<section class="section section--paper2"><div class="wrap center">
    <p class="eyebrow">Medicare in {PLAN_YEAR}, at a glance</p>
    <h2>The numbers that matter this year</h2>
    <p class="lede">Premiums and deductibles change every year. Here are the current {PLAN_YEAR} Original Medicare figures &mdash; we refresh them annually so you are never reading last year&rsquo;s numbers.</p>
  </div>
  <div class="wrap">
    <div class="stats">
      <div class="stat"><div class="stat__num">{FIG['partb']}</div><div class="stat__label">Part B premium</div><div class="stat__sub">Standard monthly, {PLAN_YEAR}</div></div>
      <div class="stat"><div class="stat__num">{FIG['partb_ded']}</div><div class="stat__label">Part B deductible</div><div class="stat__sub">Annual, {PLAN_YEAR}</div></div>
      <div class="stat"><div class="stat__num">{FIG['parta_ded']}</div><div class="stat__label">Part A deductible</div><div class="stat__sub">Per hospital benefit period, {PLAN_YEAR}</div></div>
      <div class="stat"><div class="stat__num">{FIG['partd_cap']}</div><div class="stat__label">Part D drug cap</div><div class="stat__sub">Yearly out-of-pocket max, {PLAN_YEAR}</div></div>
    </div>
    <p class="source-note">Source: Centers for Medicare &amp; Medicaid Services, {PLAN_YEAR} Medicare Parts A &amp; B Premiums and Deductibles (released November 14, 2025) and {PLAN_YEAR} Part D parameters. Higher earners may pay an income-related surcharge (IRMAA) &mdash; see our <a href="/medicare-costs">{PLAN_YEAR} costs &amp; IRMAA page</a>.</p>
</div></section>
<section class="section"><div class="wrap">
    <p class="eyebrow">Where to start</p>
    <h2>Four ways Minnesotans get covered</h2>
    <p class="lede">There is no single &ldquo;best&rdquo; plan &mdash; only the one that fits your doctors, your prescriptions, your county and your winters. Here is the plain-English version of your choices.</p>
    {place_options_grid()}
</div></section>
<section class="section section--paper2"><div class="wrap">
    <p class="eyebrow">Your situation matters</p>
    <h2>Help for specific circumstances</h2>
    <p class="lede">The rules change a lot depending on what else you have and where you spend the year. These are the situations Minnesotans ask us about most.</p>
    <div class="grid grid--4" style="margin-top:2rem">
      <article class="card help-card"><h3>Snowbirds</h3><p>Which plans travel to Arizona, Florida or Texas, and which ones only cover emergencies once you cross the state line.</p><a class="card__link" href="/snowbirds">Medicare for snowbirds <span aria-hidden="true">&rarr;</span></a></article>
      <article class="card help-card"><h3>My plan was discontinued</h3><p>UCare left Medicare Advantage for 2026 and other carriers dropped counties. What a discontinuation notice gives you, and the deadline that comes with it.</p><a class="card__link" href="/medicare-advantage">What to do next <span aria-hidden="true">&rarr;</span></a></article>
      <article class="card help-card"><h3>Veterans</h3><p>How TRICARE For Life and VA care &mdash; Minneapolis, St. Cloud or Fargo VA &mdash; each work with Medicare, and why Part B timing still matters.</p><a class="card__link" href="/veterans">Veterans &amp; Medicare <span aria-hidden="true">&rarr;</span></a></article>
      <article class="card help-card"><h3>Chronic conditions &amp; facility care</h3><p>Chronic Special Needs Plans for diabetes, heart or lung disease, and Institutional SNPs for people in a nursing facility.</p><a class="card__link" href="/chronic-snp">About C-SNPs <span aria-hidden="true">&rarr;</span></a></article>
    </div>
</div></section>
<section class="section"><div class="wrap">
    <div class="callout"><div>
        <p class="eyebrow">Free guide</p>
        <h2 style="margin-bottom:.3em">New to Medicare? Start with Turning 65 in Minnesota.</h2>
        <p>A clear, step-by-step walk-through of your enrollment windows, the Minnesota-specific choices in front of you, and the deadlines that carry a lifelong penalty if you miss them. No sign-up required.</p>
        <a class="btn btn--primary" href="/turning-65">Read the Turning 65 guide</a> <a class="btn btn--ghost" href="/retirement-guide">Get the free 295-page book</a>
      </div>
      <svg width="150" height="150" viewBox="0 0 24 24" fill="none" stroke="#1d4f6e" stroke-width="1.4" aria-hidden="true"><path d="M4 5a2 2 0 012-2h6v18H6a2 2 0 00-2 2z"/><path d="M20 5a2 2 0 00-2-2h-6v18h6a2 2 0 012 2z"/><path d="M8 7h2M8 10h2M14 7h2M14 10h2"/></svg>
    </div>
</div></section>
<section class="section section--paper2"><div class="wrap">
    <p class="eyebrow">Who you&rsquo;ll be working with</p>
    <div class="author">
      <img class="author__photo" src="/darin.jpg" width="600" height="600" alt="Darin Weidauer, independent Medicare insurance agent and credentialed gerontologist" loading="lazy" decoding="async">
      <div>
        <h2 style="margin-bottom:.15em">Darin Weidauer, MBA, RSSA&reg;</h2>
        <p style="font-weight:700;color:var(--lake-dark);margin-bottom:.6em">Gerontologist · Registered Social Security Analyst&reg; · U.S. Air Force Veteran</p>
        <ul class="creds"><li>NPN {NPN}{LIC_TXT} · licensed in Minnesota</li><li>Credentialed gerontologist (2014)</li><li>RSSA&reg;</li><li>22-yr USAF veteran (retired officer)</li><li>Author, <em>Retire With Confidence</em></li></ul>
        <p>Darin Weidauer is an independent Medicare insurance agent, credentialed gerontologist, and Registered Social Security Analyst&reg; who helps Minnesota retirees and people approaching 65 make sense of their options &mdash; clearly, patiently, and with no cost to them. A 22-year U.S. Air Force veteran who retired as an officer, Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine and a Master&rsquo;s in Long-Term Care from USC, and became a credentialed gerontologist in 2014 &mdash; studying the human side of aging, not just the paperwork.</p>
        <p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education through one-on-one reviews, no-cost workshops, and his book <em>Retire With Confidence</em>. <a href="/about">More about Darin &rarr;</a></p>
      </div>
    </div>
</div></section>
<section class="section" id="areas"><div class="wrap">
    <p class="eyebrow">Serving communities across Minnesota</p>
    <h2>Local Medicare help, statewide</h2>
    <p class="lede">We work with Minnesotans by phone and video across the state. Find Medicare guidance for your city:</p>
    <div class="loc-grid">{locs}</div>
    <p class="lede" style="margin-top:2.4rem">Or explore Medicare by region &mdash; the parts of the state we all know by name:</p>
    <div class="loc-grid">{regs}</div>
</div></section>
'''
    body += faq_html(home_faqs, "Questions Minnesotans ask")
    body += cta("Let&rsquo;s find the plan that fits your life.", "A short, friendly conversation &mdash; no pressure, no cost. We&rsquo;ll look at your doctors, your prescriptions, your county and your winters together.")
    body += byline()
    title = f"Medicare Help in Minnesota {PLAN_YEAR} | {ORG}"
    desc = "Free, plain-English Medicare help for Minnesotans: Medicare Advantage, Basic &amp; Extended Basic Medigap, Cost plans and Part D, from a credentialed independent agent."
    canonical = page("index", title, desc, body, [org_graph(), faq_ld(home_faqs)])
    register(canonical, "1.0")

def build_about():
    items = [("Home", "/"), ("About Darin", None)]
    body = hero("northwoods", "About · Who is behind this site", "Darin Weidauer, MBA, RSSA&reg;", "Independent Medicare agent licensed in Minnesota, credentialed gerontologist, Registered Social Security Analyst, and 22-year U.S. Air Force veteran. Here is who you are talking to, what he is paid, and what he is not.", items, "about", "Talk it through with Darin")
    body += f'<section class="section"><div class="wrap prose">{ABOUT_BODY}</div></section>\n'
    body += cta("Have a Medicare question? Ask the person who wrote the page.")
    body += byline()
    profile = {"@context": "https://schema.org", "@type": "ProfilePage", "@id": f"{SITE_URL}/about#profilepage", "url": f"{SITE_URL}/about",
               "name": "About Darin Weidauer — Minnesota Medicare Enrollment", "mainEntity": {"@id": f"{SITE_URL}/#darin"},
               "isPartOf": {"@id": f"{SITE_URL}/#website"}, "dateModified": ISO, "inLanguage": "en-US"}
    canonical = page("about", f"About Darin Weidauer | {ORG}",
                     "Darin Weidauer: independent Medicare agent licensed in Minnesota (NPN 18580338, MN License #40620754), gerontologist, Registered Social Security Analyst and retired Air Force officer. How he is paid.",
                     body, [org_graph(), profile, crumb_ld(items)], ogtype="profile")
    register(canonical, "0.7")

def build_faq_page():
    items = [("Home", "/"), ("FAQ", None)]
    body = hero("lakes", "Questions Minnesotans ask", "Minnesota Medicare questions, answered plainly", "The questions we hear most from Minnesotans &mdash; about Cost plans, Basic and Extended Basic supplements, discontinued Advantage plans, wintering away, and what any of this costs. Short answers, with links to the longer ones.", items, "faq")
    body += faq_html(FAQ_PAGE, "Straight answers")
    body += cta("Didn&rsquo;t see your question? Call and ask it.")
    body += byline()
    canonical = page("faq", f"Minnesota Medicare FAQ {PLAN_YEAR} | {ORG}",
                     "Plain answers to the Medicare questions Minnesotans ask most: Cost plans, Basic vs Extended Basic Medigap, discontinued Advantage plans, snowbird coverage, MSHO and costs.",
                     body, [org_graph(), crumb_ld(items), faq_ld(FAQ_PAGE)])
    register(canonical, "0.7")

def build_legal(slug, name, body_html, desc):
    items = [("Home", "/"), (name, None)]
    body = f'''<section class="hero hero--short"><div class="hero__scene" aria-hidden="true">{SCENES["northwoods"]}</div>{crumbs(items)}
<div class="wrap" style="padding:1rem 0 2.4rem"><p class="eyebrow">{name}</p><h1>{name}</h1></div></section>
<section class="section"><div class="wrap prose">{body_html}</div></section>
'''
    canonical = page(slug, f"{name} | {ORG}", desc, body, [org_graph(), crumb_ld(items)])
    register(canonical, "0.3")

def build_thankyou():
    items = [("Home", "/"), ("Thank you", None)]
    body = f'''<section class="hero hero--short"><div class="hero__scene" aria-hidden="true">{SCENES["lakes"]}</div>{crumbs(items)}
<div class="wrap" style="padding:1rem 0 2.4rem"><p class="eyebrow">Request received</p><h1>Thank you &mdash; your request is on its way.</h1></div></section>
<section class="section"><div class="wrap prose">
<p>Thanks for reaching out. Your request has been received, and Darin or a licensed agent on our team will get back to you shortly to set up your free, no-pressure Medicare review.</p>
<h2>What happens next</h2>
<ul><li>We&rsquo;ll reach out using the contact details you provided.</li><li>We&rsquo;ll listen first &mdash; your doctors, your prescriptions, your county, your winters, your budget.</li><li>Then we&rsquo;ll compare the options that actually fit, with no obligation.</li></ul>
<p>Need to talk sooner? Call us anytime at <a href="tel:{TEL}"><strong>{PHONE}</strong></a>.</p>
<p><a class="btn btn--ghost" href="/">&larr; Back to home</a></p>
</div></section>
'''
    page("thank-you", f"Thank you | {ORG}", "Your request has been received. Darin or a licensed agent will be in touch shortly.", body, [org_graph()], noindex=True)

def build_404():
    body = f'''<section class="section"><div class="wrap prose">
<h1>We couldn&rsquo;t find that page</h1>
<p>The link may be out of date, or the address may have a typo. Here is where most people were heading.</p>
<h2>Popular guides</h2>
<ul>
<li><a href="/#areas">Areas we serve</a> &mdash; a Medicare guide for cities and regions across Minnesota</li>
<li><a href="/medicare-costs">{PLAN_YEAR} Medicare costs</a> &mdash; Part A, B, D and the IRMAA table</li>
<li><a href="/medicare-advantage">Medicare Advantage</a>, <a href="/medicare-supplement">Minnesota Medigap</a> and <a href="/medicare-cost-plans">Cost plans</a></li>
<li><a href="/part-d">Part D drug coverage</a></li>
<li><a href="/turning-65">Turning 65</a> &mdash; your enrollment timeline</li>
<li><a href="/snowbirds">Snowbirds</a> &mdash; which plans travel</li>
<li><a href="/medicaid">Medical Assistance, MSHO and Medicare Savings Programs</a></li>
<li><a href="/veterans">Veterans and Medicare</a></li>
</ul>
<div class="note-box"><p>Still stuck? Call <a href="tel:{TEL}"><strong>{PHONE}</strong></a> and we will point you to the right place &mdash; or just answer the question directly.</p></div>
</div></section>
'''
    page("404", f"Page not found | {ORG}", "That page could not be found. Here are the Minnesota Medicare guides most people were looking for.", body, [org_graph()], noindex=True)

# ----------------------------------------------------------------------------
# Discovery files
# ----------------------------------------------------------------------------
def write_discovery():
    urls = "".join(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{m}</lastmod>\n    <priority>{p}</priority>\n  </url>\n" for u, m, p in PAGES)
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "anthropic-ai", "Google-Extended",
            "PerplexityBot", "Perplexity-User", "Applebot", "Applebot-Extended", "CCBot", "Amazonbot", "meta-externalagent", "cohere-ai", "DuckAssistBot", "YouBot", "Bingbot"]
    (ROOT / "robots.txt").write_text(
        "# Structured summaries for language models: /llms.txt and /llms-full.txt\n"
        f"# {SITE_NAME}\n# Standard search engines and AI / answer-engine crawlers are welcome.\n"
        "User-agent: *\nAllow: /\nDisallow: /thank-you\nDisallow: /source/\n\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n\n# --- AI and answer-engine crawlers: explicitly welcome ---\n"
        + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots))

    topic_lines = "".join(f"- [{unesc(p['nav_title'])}]({SITE_URL}/{p['slug']}): {unesc(p['llm'])}\n" for p in TOPIC_PAGES)
    city_lines = "".join(f"- [Medicare help in {c['name']} ({c['county']})]({SITE_URL}/{c['slug']})\n" for c in CITIES)
    region_lines = "".join(f"- [Medicare help across {unesc(r['name'])}]({SITE_URL}/{r['slug']}): counties {r['counties']}\n" for r in REGIONS)
    net_lines = "".join(f"- [{n}]({u})\n" for n, u in NETWORK)
    (ROOT / "llms.txt").write_text(f"""# {ORG} — Minnesota

> Free, plain-English Medicare guidance for Minnesota retirees and people approaching 65. Compare Medicare Advantage, Minnesota Basic and Extended Basic Medicare supplements, Medicare Cost plans (still sold in 21 Minnesota counties), and Part D drug plans with a credentialed, independent agent at no cost. Statewide service by phone and video.

Contact: {PHONE} · {EMAIL} · {SITE_URL}/

## About
{ORG} is an independent Medicare insurance agency serving the State of Minnesota. Agent: Darin Weidauer, MBA, RSSA — gerontologist, Registered Social Security Analyst, 22-year U.S. Air Force veteran, licensed in Minnesota, NPN {NPN}{LIC_TXT}. Help is free to the consumer; independent agents are paid by carriers at enrollment, and the premium is the same whichever way you buy. Author page: https://www.myecos360.com/darin-weidauer

## What is different about Medicare in Minnesota
- Medicare supplements are state-standardized as a Basic plan and an Extended Basic plan with optional riders (Minn. Stat. §62A.31). Minnesota does not use the federal plan letters A–N.
- Medicare Cost plans are still sold in 21 counties: Aitkin, Carlton, Cook, Goodhue, Itasca, Kanabec, Koochiching, Lake, Le Sueur, McLeod, Meeker, Mille Lacs, Pine, Pipestone, Rice, Rock, St. Louis, Sibley, Stevens, Traverse, Yellow Medicine (Minnesota Aging Pathways, Medicare 101; Minnesota Department of Commerce 2026 Cost plan guide). Sold by Blue Cross Blue Shield of Minnesota and Medica.
- Under Minn. Stat. §62A.31 as amended by Laws 2025, 1st Spec. Sess., ch. 4, art. 5 (effective August 1, 2026), people aged 65 through 70 may, one time, buy a Medicare supplement outside their original six-month window by applying during a qualifying open enrollment period as defined by 42 CFR §422.62(a)(2)-(4) (the Annual Election Period Oct 15–Dec 7, the Medicare Advantage Open Enrollment Period Jan 1–Mar 31), without medical underwriting or pre-existing-condition limits. Surcharge above the community rate, for the life of the policy: 15% (first use in 2026), 20% (2027), 25% (2028), 30% (2029), 35% (2030 and later). August 1, 2026 is the effective date, not an enrollment month.
- Minnesota Senior Health Options (MSHO) combines Medicare and Medical Assistance (Minnesota's Medicaid) for people 65+ under one plan.
- Minnesota's SHIP is Minnesota Aging Pathways, formerly the Senior LinkAge Line: 800-333-2433.
- For the 2026 plan year UCare stopped selling Medicare Advantage statewide and HealthPartners, Humana and UnitedHealthcare left dozens of counties; a discontinued plan creates a Special Enrollment Period and, often, a guaranteed-issue right to a supplement.

## Verified {PLAN_YEAR} figures (CMS)
- Medicare Part B standard premium: {FIG['partb']}/month; annual deductible: {FIG['partb_ded']}
- Part A hospital deductible: {FIG['parta_ded']} per benefit period
- Part D out-of-pocket cap: {FIG['partd_cap']}/year; maximum deductible: {FIG['partd_ded']}; national base premium: {FIG['partd_base']}
- IRMAA (income surcharge) begins above {FIG['irmaa_single']} (single) / {FIG['irmaa_joint']} (joint), based on 2024 MAGI

## Pages
- [Home]({SITE_URL}/): free, plain-English Medicare help across Minnesota
{topic_lines}- [About Darin Weidauer]({SITE_URL}/about): credentials, licensing, compensation disclosure
- [FAQ]({SITE_URL}/faq): the questions Minnesotans ask most
{city_lines}{region_lines}- [Privacy Policy]({SITE_URL}/privacy)
- [Terms of Use]({SITE_URL}/terms)

## Same agency, other sites
{net_lines}
## Compliance
We do not offer every plan available in your area. Any information we provide is limited to those plans we do offer in your area. Beneficiaries can also contact Medicare.gov, 1-800-MEDICARE, or Minnesota Aging Pathways (800-333-2433). Not affiliated with or endorsed by the U.S. government or the federal Medicare program. This is a solicitation for insurance.
""")

    full = [f"# {ORG} — Minnesota (full reference)\n\nWebsite: {SITE_URL}/\nPhone: {PHONE}\nEmail: {EMAIL}\nService area: State of Minnesota (statewide — by phone and video)\nLast reviewed: {ISO}\n"]
    full.append("""
## About
ECOS Medicare Solutions is an independent Medicare insurance agency helping Minnesota retirees and people approaching 65 compare their Medicare options clearly, patiently, and at no cost. Independent agents are paid by the insurance carriers when a client enrolls, so there is no charge to the consumer, and plan premiums are the same whether you enroll with our help or on your own.

## Agent / author
Darin Weidauer, MBA, RSSA — independent Medicare insurance agent licensed in Minnesota (NPN 18580338, MN License #40620754) and 14 other states (AZ, CA, CO, FL, GA, MN, NC, NM, NV, OH, SC, TN, TX, UT, WA), credentialed gerontologist (since 2014), Registered Social Security Analyst, and 22-year U.S. Air Force veteran (retired officer). Author of "Retire With Confidence: Medicare, Social Security, and the Money Decisions That Decide Your Retirement" (2026 Edition, 295 pages). Former Professor of Aerospace Studies at Loyola Marymount University; has lectured at more than 50 colleges and universities. Canonical author profile: https://www.myecos360.com/darin-weidauer
""")
    for p in TOPIC_PAGES:
        full.append(f"\n## {unesc(p['h1'])}\nURL: {SITE_URL}/{p['slug']}\n")
        for k in p.get("keyfacts", []):
            full.append(f"- {unesc(k)}\n")
        for q, a in p["faqs"]:
            full.append(f"- Q: {unesc(q)} A: {unesc(a)}\n")
    full.append("\n## Areas served\nCities: " + ", ".join(c["name"] for c in CITIES) + ".\nRegions: " + ", ".join(unesc(r["name"]) for r in REGIONS) + ".\n")
    full.append("\n## Compliance\nWe do not offer every plan available in your area. Any information we provide is limited to those plans we do offer in your area. Please contact Medicare.gov, 1-800-MEDICARE, or Minnesota Aging Pathways (800-333-2433) to get information on all your options. ECOS Medicare Solutions is not connected with or endorsed by the U.S. government or the federal Medicare program, and is not affiliated with the State of Minnesota, the VA, the Department of Defense, or TRICARE. This is a solicitation for insurance; a licensed agent may contact you.\n")
    (ROOT / "llms-full.txt").write_text("".join(full))

def write_static():
    (ROOT / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42 42"><circle cx="21" cy="21" r="20" fill="#1d4f6e"/><path d="M21 6l2.6 9.4L33 18l-9.4 2.6L21 30l-2.6-9.4L9 18l9.4-2.6z" fill="#e7c486"/><path d="M6 30c5-3 10-3 15 0s10 3 15 0" stroke="#9fc4d8" stroke-width="2" fill="none" stroke-linecap="round"/><path d="M10 30l3-7 3 7zM26 30l3-7 3 7z" fill="#2f5d4a"/></svg>\n')
    (ROOT / "vercel.json").write_text(json.dumps({"cleanUrls": True, "trailingSlash": False,
        "headers": [{"source": "/(.*)", "headers": [{"key": "X-Content-Type-Options", "value": "nosniff"}, {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"}, {"key": "X-Frame-Options", "value": "SAMEORIGIN"}]}]}, indent=2) + "\n")
    (ROOT / "CNAME").write_text("minnesotamedicareenrollment.com\n")
    (ROOT / ".nojekyll").write_text("")
    (ROOT / "site.js").write_text(SITE_JS)
    (ROOT / "analytics.js").write_text(ANALYTICS_JS)
    (ROOT / "site.css").write_text(SITE_CSS)

# ----------------------------------------------------------------------------
# Assets
# ----------------------------------------------------------------------------
SITE_JS = r"""/* ECOS Medicare Solutions — shared site behavior (no dependencies) */
(function () {
  var ct = document.getElementById('consent_timestamp');
  if (ct) ct.value = new Date().toISOString();
  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  // Mobile menu
  var tg = document.querySelector('.nav-toggle'), links = document.getElementById('navLinks');
  if (tg && links) {
    tg.addEventListener('click', function () {
      var open = links.classList.toggle('is-open');
      tg.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && links.classList.contains('is-open')) { links.classList.remove('is-open'); tg.setAttribute('aria-expanded', 'false'); tg.focus(); } });
  }

  // Gentle scroll reveal — skipped when reduced motion is preferred.
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) return;
  var els = document.querySelectorAll('.section, .stat, .card');
  els.forEach(function (el) { el.classList.add('reveal'); });
  if (!('IntersectionObserver' in window)) { els.forEach(function (el) { el.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.12 });
  els.forEach(function (el) { io.observe(el); });
})();
"""

ANALYTICS_JS = r"""/* ECOS Medicare Solutions — site analytics (Google Analytics 4)
 *
 * ONE place to configure. Replace MEASUREMENT_ID below with this site's GA4
 * Measurement ID (Google Analytics -> Admin -> Data Streams -> your web stream).
 * Until a real ID is set this file does nothing at all -- no network requests,
 * no broken hits. A placeholder that silently fails looks installed while
 * collecting zero data, so the placeholder is refused explicitly.
 *
 * Tracks, beyond standard pageviews:
 *   click_to_call  -- every tap on a phone number, labelled by placement
 *   generate_lead  -- every lead form submitted, labelled by page and form
 * Mark BOTH as key events (conversions) in GA4: Admin -> Events -> "Mark as key event".
 */
(function () {
  var MEASUREMENT_ID = 'G-XXXXXXXXXX';
  if (!/^G-[A-Z0-9]{8,12}$/.test(MEASUREMENT_ID) || /^G-X+$/.test(MEASUREMENT_ID)) {
    if (window.console && console.info) console.info('[analytics] No GA4 Measurement ID configured yet — tracking is off. Set MEASUREMENT_ID in analytics.js.');
    return;
  }
  var s = document.createElement('script'); s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + MEASUREMENT_ID; document.head.appendChild(s);
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag; gtag('js', new Date()); gtag('config', MEASUREMENT_ID);
  function placement(el) {
    var map = [['.site-header', 'header'], ['.cta-strip', 'cta strip'], ['.hero', 'hero'], ['.lead-card', 'lead form'],
               ['.faq', 'faq'], ['.site-footer', 'footer'], ['.section', 'body content']];
    for (var i = 0; i < map.length; i++) { try { if (el.closest(map[i][0])) return map[i][1]; } catch (e) {} }
    return 'body';
  }
  function pageInfo() { return { page_path: location.pathname, page_title: (document.title || '').slice(0, 100) }; }
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest && e.target.closest('a[href^="tel:"]'); if (!a) return;
    var info = pageInfo();
    gtag('event', 'click_to_call', { phone_number: a.getAttribute('href').replace('tel:', ''), link_placement: placement(a), page_path: info.page_path, page_title: info.page_title, transport_type: 'beacon' });
  }, true);
  document.addEventListener('submit', function (e) {
    var f = e.target; if (!f || f.tagName !== 'FORM') return;
    var info = pageInfo(); var topic = f.querySelector('select');
    gtag('event', 'generate_lead', { form_id: f.id || f.getAttribute('name') || 'unnamed', form_placement: placement(f), lead_topic: topic ? topic.value : '', page_path: info.page_path, page_title: info.page_title, transport_type: 'beacon' });
  }, true);
})();
"""

SITE_CSS = (Path(__file__).resolve().parent / "site.css").read_text()

# ----------------------------------------------------------------------------
def main():
    write_static()
    build_home()
    for p in TOPIC_PAGES:
        build_topic(p)
    build_about()
    build_faq_page()
    for c in CITIES:
        build_city(c)
    for r in REGIONS:
        build_region(r)
    build_legal("privacy", "Privacy Policy", PRIVACY_BODY, "How Minnesotamedicareenrollment.com collects, uses and protects the information you share with ECOS Medicare Solutions.")
    build_legal("terms", "Terms of Use", TERMS_BODY, "Terms of use for Minnesotamedicareenrollment.com, operated by ECOS Medicare Solutions.")
    build_thankyou()
    build_404()
    write_discovery()
    print(f"built {len(PAGES)} indexable pages + thank-you + 404")

if __name__ == "__main__":
    main()
