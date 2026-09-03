"""Topic-page content for MinnesotaMedicareEnrollment.com.

Each entry in TOPIC_PAGES is one page. Tokens [[PHONE]], [[TEL]], [[EMAIL]],
[[QUOTE]] and [[YEAR]] are filled by generate.py. Links are root-absolute clean
URLs (no .html) to match Vercel's cleanUrls and GitHub Pages' extensionless
resolution.

Every dollar figure on these pages is a verified 2026 CMS figure or a cited
Minnesota figure. Do not "update" a number without the source in hand.
"""

SRC_CMS = ("CMS: 2026 Medicare Parts A &amp; B Premiums and Deductibles (Nov 14, 2025)", "https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-and-deductibles")
SRC_MEDICARE_COSTS = ("Medicare.gov: Medicare costs", "https://www.medicare.gov/basics/costs/medicare-costs")
SRC_MN_STATUTE = ("Minnesota Statutes §62A.31, Medicare supplement benefits; minimum standards", "https://www.revisor.mn.gov/statutes/cite/62A.31")
SRC_MN_COMMERCE_MEDIGAP = ("Minnesota Department of Commerce: Medicare supplement open enrollment", "https://mn.gov/commerce/insurance/health/policy-data-reports/medicare-supplement-open-enrollment.jsp")
SRC_MN_COST_GUIDE = ("Minnesota Department of Commerce: 2026 Medicare Cost plan premium guide (PDF)", "https://mn.gov/commerce-stat/insurance/medicare/2026/cost_012026.pdf")
SRC_MEDICARE_OTHER_PLANS = ("Medicare.gov: Other Medicare health plans (Medicare Cost plans)", "https://www.medicare.gov/health-drug-plans/health-plans/your-coverage-options/other-medicare-health-plans")
SRC_AGING_PATHWAYS = ("Minnesota Aging Pathways (formerly the Senior LinkAge Line), 800-333-2433", "https://mn.gov/aging-pathways/")
SRC_MSHO = ("Minnesota DHS: Minnesota Senior Health Options (MSHO)", "https://mn.gov/dhs/people-we-serve/seniors/health-care/health-care-programs/programs-and-services/msho.jsp")
SRC_MSP = ("LawHelp Minnesota: Medicare Savings Programs fact sheet", "https://www.lawhelpmn.org/self-help-library/fact-sheet/medicare-savings-programs")
SRC_MEDIGAP_GOV = ("Medicare.gov: Medigap (Medicare Supplement Insurance)", "https://www.medicare.gov/health-drug-plans/medigap")
SRC_MA_GOV = ("Medicare.gov: Medicare Advantage plans", "https://www.medicare.gov/health-drug-plans/health-plans")
SRC_PARTD_GOV = ("Medicare.gov: Drug coverage (Part D)", "https://www.medicare.gov/health-drug-plans/part-d")
SRC_TFL = ("TRICARE For Life", "https://www.tricare.mil/tfl")
SRC_VA = ("VA health care and other insurance", "https://www.va.gov/health-care/about-va-health-benefits/va-health-care-and-other-insurance/")
SRC_STAR = ("Star Tribune: Medicare Advantage premiums rising in Minnesota as insurers pull back (2026 plan year)", "https://www.startribune.com/medicare-advantage-minnesota-higher-premiums-fewer-options-unitedhealthcare-healthpartners/601483594")
SRC_CBS = ("CBS Minnesota: UCare and other carriers dropping Medicare Advantage plans for 2026", "https://www.cbsnews.com/minnesota/news/ucare-drops-medicare-advantage-minnesota-seniors-losing-health-insurance/")
SRC_TELOS = ("Telos Actuarial: New Medicare supplement regulations in Minnesota (2026)", "https://www.telosactuarial.com/blog/regulations-tx-mn-2hfy8")
SRC_MYMEDIGAP_MN = ("MyMedigapRate: Minnesota Medigap switching rules, cited to the statute", "https://www.mymedigaprate.com/medigap-rate-history/minnesota")

COST_COUNTIES = ["Aitkin", "Carlton", "Cook", "Goodhue", "Itasca", "Kanabec", "Koochiching", "Lake", "Le Sueur", "McLeod", "Meeker",
                 "Mille Lacs", "Pine", "Pipestone", "Rice", "Rock", "St. Louis", "Sibley", "Stevens", "Traverse", "Yellow Medicine"]
COUNTY_LIST_HTML = '<ul class="county-list">' + "".join(f"<li>{c}</li>" for c in COST_COUNTIES) + "</ul>"

TOPIC_PAGES = [
# ---------------------------------------------------------------- Medicare Advantage
dict(slug="medicare-advantage", nav_title="Medicare Advantage plans in Minnesota", crumb="Medicare Advantage", scene="skyline",
     title="Medicare Advantage Plans in Minnesota [[YEAR]] | ECOS Medicare Solutions",
     desc="Medicare Advantage in Minnesota: networks, $0 premiums, the 2026 carrier exits, and what to do if your plan was discontinued. Free help from a licensed Minnesota agent.",
     llm="Medicare Advantage (Part C) in Minnesota: how networks and bundled benefits work, the 2026 carrier exits, and what a discontinued plan gives you",
     eyebrow="Plans · Part C", h1="Medicare Advantage plans in Minnesota",
     sub="All-in-one plans, often with a $0 premium and extras like dental and vision &mdash; riding on a local network, in a state where the network map was redrawn for 2026.",
     keyfacts=["A Medicare Advantage plan bundles Part A, Part B and usually Part D into one private plan with a network. You keep paying the Part B premium ([[YEAR]]: $202.90) plus any plan premium.",
               "For the 2026 plan year UCare stopped selling Medicare Advantage statewide, and HealthPartners, Humana and UnitedHealthcare left dozens of Minnesota counties, mostly outside the metro.",
               "A discontinued plan gives you a Special Enrollment Period and, in most cases, a guaranteed-issue right to buy a Minnesota Basic or Extended Basic supplement without health questions.",
               "Minnesota&rsquo;s 2027 plan lineups are announced October 1, 2026; the Annual Election Period runs October 15 to December 7."],
     body="""<p>A Medicare Advantage plan (also called Part C) is an all-in-one alternative to Original Medicare, offered by private insurers that Medicare approves and pays. You still have Medicare, but the plan administers your Part A and Part B coverage and almost always folds in Part D drug coverage too. In Minnesota the main carriers are Blue Cross Blue Shield of Minnesota (Blue Plus), HealthPartners, Medica, UnitedHealthcare, Humana and Aetna &mdash; and which of them sells in <em>your</em> county changes every year.</p>
<h2>What&rsquo;s usually included</h2>
<ul>
<li><strong>Hospital and medical coverage</strong> (your Part A and Part B benefits).</li>
<li><strong>Prescription drug coverage</strong> in most plans &mdash; so you don&rsquo;t buy a separate <a href="/part-d">Part D plan</a>.</li>
<li><strong>Extras Original Medicare doesn&rsquo;t cover</strong>, which can include dental, vision, hearing, fitness benefits, and an annual out-of-pocket maximum that caps what you spend on covered care.</li>
</ul>
<h2>The trade-off: networks</h2>
<p>Advantage plans use provider networks (HMO or PPO). That is the single most important thing to check before you enroll: whether your doctors and your hospital are in the plan&rsquo;s network, and whether your medications are on its drug list. Minnesota&rsquo;s health systems &mdash; Allina, M Health Fairview, HealthPartners, Mayo Clinic, Essentia, CentraCare, Sanford &mdash; each contract with some plans and not others, and Mayo Clinic in particular contracts selectively. We confirm your providers and prescriptions are covered before you sign anything.</p>
<div class="warn-box"><p><strong>What changed for 2026, and why it matters this fall.</strong> UCare, long the state&rsquo;s second-largest Advantage carrier, stopped selling Medicare Advantage statewide for the 2026 plan year, affecting roughly 158,000 Minnesotans. HealthPartners, Humana and UnitedHealthcare dropped dozens of counties, mostly outside the Twin Cities, and UnitedHealthcare cut its footprint from 72 counties to 27. Average premiums rose sharply. If you were moved into a new plan, or picked one in a hurry last fall, the Annual Election Period starting October 15 is the time to check it actually fits.</p></div>
<h2>If your plan was discontinued</h2>
<p>A non-renewal notice is not just bad news; it opens doors. You get a Special Enrollment Period that runs past the normal deadlines, and because the plan left you involuntarily, Minnesota and federal rules give most people a <strong>guaranteed-issue right</strong> to buy a <a href="/medicare-supplement">Minnesota Basic or Extended Basic supplement</a> without medical underwriting &mdash; even if you are well past your original six-month Medigap window. The right is time-limited (generally 63 days after your coverage ends), so do not let the notice sit.</p>
<div class="note-box"><p><strong>A Minnesota note.</strong> In 21 counties, mostly in the north and southwest, <a href="/medicare-cost-plans">Medicare Cost plans</a> are a third option that behaves a lot like an Advantage plan at home and like Original Medicare everywhere else. If your county is on that list, compare all three.</p></div>
<h2>Who Medicare Advantage tends to suit</h2>
<p>People who want predictable, lower upfront costs and value bundled extras, and who are comfortable using a plan network and staying mostly in Minnesota. If you winter in Arizona or Florida, see specialists outside the network, or want to use any provider nationwide, compare it against a <a href="/medicare-supplement">supplement</a> &mdash; our <a href="/snowbirds">snowbird guide</a> walks through the difference.</p>
<p>There are also specialized Advantage plans for specific situations: <a href="/chronic-snp">Chronic Special Needs Plans (C-SNPs)</a>, <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a>, and Dual Special Needs Plans, which in Minnesota mostly means <a href="/medicaid">Minnesota Senior Health Options (MSHO)</a> for people with both Medicare and Medical Assistance.</p>""",
     faqs=[("Does Medicare Advantage replace Original Medicare?", "Not exactly. You keep Medicare, but a private Advantage plan administers your benefits and adds extras. You generally use the plan&rsquo;s network and its rules instead of Original Medicare&rsquo;s."),
           ("Is there really a $0 premium?", "Many Advantage plans have a $0 monthly plan premium, but you still pay your Part B premium ($202.90 in [[YEAR]]), and you may have copays, coinsurance and a deductible. We show you the full picture, not just the premium."),
           ("My Minnesota Advantage plan was discontinued. Can I get a Medigap policy now?", "In most cases, yes. Losing your plan through no fault of your own gives you a guaranteed-issue right to buy a Minnesota Basic or Extended Basic supplement without health questions, generally within 63 days of the coverage ending, plus a Special Enrollment Period to pick a new Advantage or Part D plan. Call before the deadline on your notice."),
           ("Can I switch later if it isn&rsquo;t a fit?", "Yes. You can change during the Annual Election Period (Oct 15&ndash;Dec 7), and the Medicare Advantage Open Enrollment Period (Jan 1&ndash;Mar 31) lets current Advantage members switch once or return to Original Medicare. Special circumstances, including moving counties, open other windows.")],
     sources=[SRC_MA_GOV, SRC_CBS, SRC_STAR, SRC_CMS], cta="Let&rsquo;s compare your Advantage options &mdash; and the alternatives.", about="Medicare Advantage in Minnesota"),

# ---------------------------------------------------------------- Medigap (Minnesota)
dict(slug="medicare-supplement", nav_title="Medicare Supplement plans in Minnesota (Basic &amp; Extended Basic)", crumb="Medicare Supplement", scene="northwoods",
     title="Medicare Supplement Plans in Minnesota: Basic vs Extended Basic | ECOS Medicare Solutions",
     desc="Minnesota Medigap explained: Basic vs Extended Basic, riders, the 6-month open enrollment, the new 2026 guaranteed-issue window for ages 65-70, and rate history.",
     llm="Minnesota Medicare Supplement (Medigap): Basic vs Extended Basic plans, riders, open enrollment and guaranteed-issue rules including the August 2026 change, comparing carriers on filed rate history",
     eyebrow="Plans · Medigap, the Minnesota way", h1="Medicare Supplement plans in Minnesota: Basic and Extended Basic",
     sub="Minnesota is one of three states that standardize Medigap its own way. There is no Plan G here &mdash; there is a Basic plan, an Extended Basic plan, and riders. Here is how they work, when you can buy one without health questions, and how to compare carriers.",
     keyfacts=["Minnesota does not use the federal Medigap letters A&ndash;N. Under Minnesota Statutes §62A.31, insurers sell a <strong>Basic</strong> plan and an <strong>Extended Basic</strong> plan, and may add optional riders to Basic.",
               "Both base plans are guaranteed available during your six-month Medigap open enrollment, which starts when you are 65 or older and enrolled in Part B. Minnesota also extends open enrollment to people under 65 on Medicare because of a disability.",
               "New for 2026: beginning August 1, 2026, Minnesotans aged 65&ndash;70 may buy a supplement during the Annual Election Period (Oct 15&ndash;Dec 7), one time, without medical underwriting. Insurers may charge a surcharge that starts at 15% in 2026 and rises 5 points a year to 35%, for the life of the policy.",
               "Because benefits are standardized, the real difference between carriers is price and how fast it rises. Our research site publishes Minnesota carriers&rsquo; filed rate history."],
     body="""<p>Medicare Supplement insurance &mdash; usually called Medigap &mdash; is private coverage that pairs with Original Medicare (Parts A and B). Instead of replacing Medicare, it fills the gaps: the deductibles, copayments and coinsurance you&rsquo;d otherwise pay yourself. You then add a standalone <a href="/part-d">Part D drug plan</a> for prescriptions. What makes Minnesota different is <em>which</em> gaps each plan fills, because the state writes its own plan designs.</p>
<h2>Basic vs Extended Basic</h2>
<table class="ctable">
<caption>The two Minnesota base plans, simplified. The Minnesota Department of Commerce publishes the full benefit chart; we walk through it with you line by line.</caption>
<thead><tr><th scope="col">&nbsp;</th><th scope="col">Basic plan</th><th scope="col">Extended Basic plan</th></tr></thead>
<tbody>
<tr><th scope="row">Part A hospital coinsurance and extra hospital days</th><td>Yes</td><td>Yes</td></tr>
<tr><th scope="row">Part B coinsurance (the 20%)</th><td>Yes</td><td>Yes</td></tr>
<tr><th scope="row">Blood, hospice cost-sharing, skilled-nursing coinsurance</th><td>Yes</td><td>Yes</td></tr>
<tr><th scope="row">Part A hospital deductible ($1,736 in [[YEAR]])</th><td>Optional rider</td><td>Included</td></tr>
<tr><th scope="row">Part B excess charges</th><td>Optional rider</td><td>Included</td></tr>
<tr><th scope="row">Foreign-travel emergency care</th><td>No</td><td>Included</td></tr>
<tr><th scope="row">Part B deductible ($283 in [[YEAR]])</th><td colspan="2">Rider available only to people who were eligible for Medicare before 2020, under the federal rule that ended first-dollar Part B coverage</td></tr>
<tr><th scope="row">Provider access</th><td colspan="2">Any provider in the U.S. that accepts Medicare &mdash; no networks, no referrals, no county lines</td></tr>
</tbody></table>
<p>Insurers can also sell copay versions of Basic (a set copay for office and emergency visits in exchange for a lower premium, in the spirit of a federal Plan N) and a high-deductible version. The names vary by company; the benefits inside each design do not.</p>
<h2>When you can buy one without health questions</h2>
<ul>
<li><strong>Your six-month open enrollment.</strong> It starts the month you are 65 or older <em>and</em> enrolled in Part B. During it, both base plans are guaranteed available regardless of health, and an insurer cannot charge you more for a condition.</li>
<li><strong>Under 65 on disability.</strong> Minnesota extends the same open enrollment to people who qualify for Medicare before 65, something many states do not.</li>
<li><strong>Guaranteed-issue events.</strong> Losing an Advantage, Cost or employer plan through no fault of your own gives you a window (generally 63 days) to buy a supplement without underwriting. The 2026 carrier exits triggered this right for a lot of Minnesotans.</li>
<li><strong>New: the ages 65&ndash;70 annual window.</strong> Beginning August 1, 2026, if you are between 65 and 70 you may buy a supplement during the Annual Election Period, October 15 to December 7, without medical underwriting or pre-existing-condition limits. It can be used once. Insurers may charge a premium surcharge over the standard rate &mdash; 15% for policies bought in 2026, rising 5 percentage points a year to 35% for 2030 and later &mdash; and the surcharge stays with the policy. It is a real second chance for people who chose Advantage at 65 and regret it; it is not free.</li>
</ul>
<div class="note-box"><p><strong>Timing matters.</strong> Outside those windows, insurers can use medical underwriting, and a condition that would be irrelevant at 65 can mean a decline at 72. If you are approaching 65, or your Advantage plan just sent a non-renewal notice, talk to us before the window closes.</p></div>
<h2>Compare the rate history, not just the first-year price</h2>
<p>Because the benefits are standardized, the only real differences between Minnesota Medigap companies are what they charge and how steeply they raise it later. That second part is public: every carrier files its rate increases with the Minnesota Department of Commerce, and a policy that looks cheap at 65 can be the expensive one by 75. We publish that filing history on our research site, <a href="https://www.mymedigaprate.com/medigap-rate-history/minnesota">Minnesota Medigap rate history</a>, with each figure tied to the filing it came from. If your premium has already gone up and you want to know why, <a href="https://www.mymedigaprate.com/why-did-my-medigap-premium-increase">why Medigap premiums increase</a> covers the three causes and how to tell them apart.</p>
<h2>Who Medigap tends to suit</h2>
<p>People who want maximum freedom to choose doctors and hospitals &mdash; Mayo Clinic without a network question, Fargo or Sioux Falls without a border question &mdash; predictable costs, and coverage that travels. That last point is why so many Minnesota <a href="/snowbirds">snowbirds</a> keep a supplement. The cost is a monthly premium that rises with age and with the carrier&rsquo;s filings.</p>""",
     faqs=[("Does Minnesota have Medigap Plan G or Plan N?", "No. Minnesota, Massachusetts and Wisconsin standardize Medicare supplements their own way. Minnesota sells a Basic plan and an Extended Basic plan, with optional riders on Basic. A Basic plan with the Part A deductible and excess-charge riders is the closest thing to a federal Plan G; copay versions of Basic are the closest thing to Plan N."),
           ("Do I need a separate drug plan with a Minnesota supplement?", "Yes. Neither Basic nor Extended Basic includes prescription coverage, so you add a standalone Part D plan. We help you pick one around your specific medications."),
           ("What is the new Minnesota Medigap rule for 2026?", "Beginning August 1, 2026, people aged 65 to 70 can buy a Medicare supplement during the Annual Election Period (October 15 to December 7) without medical underwriting, one time. Insurers may charge a surcharge over the standard premium, starting at 15% in 2026 and rising 5 points each year to a maximum of 35%, and it lasts as long as you keep the policy. Confirm the details with the Minnesota Department of Commerce or Minnesota Aging Pathways before relying on it."),
           ("Can I be turned down for a Minnesota supplement?", "Not during your six-month open enrollment, not during a guaranteed-issue event such as your Advantage plan being discontinued, and not during the new ages 65&ndash;70 annual window. Outside those, insurers can use medical underwriting in Minnesota."),
           ("How much does a Minnesota supplement cost?", "It depends on the plan, the riders, your age, tobacco use and the carrier, and every carrier raises rates on its own schedule. We compare current premiums and each company&rsquo;s filed rate history with you; we do not publish a number here without the filing behind it.")],
     sources=[SRC_MN_STATUTE, SRC_MN_COMMERCE_MEDIGAP, SRC_TELOS, SRC_MEDIGAP_GOV, SRC_MYMEDIGAP_MN, SRC_CMS], cta="Let&rsquo;s see whether Basic or Extended Basic fits you.", about="Minnesota Medicare supplement insurance"),

# ---------------------------------------------------------------- Cost plans
dict(slug="medicare-cost-plans", nav_title="Medicare Cost plans in Minnesota (the 21 counties)", crumb="Medicare Cost plans", scene="lighthouse",
     title="Medicare Cost Plans in Minnesota [[YEAR]]: The 21 Counties | ECOS Medicare Solutions",
     desc="Medicare Cost plans remain in 21 Minnesota counties. What a Cost plan is, how it differs from Advantage, why snowbirds like it, the county list and carriers.",
     llm="Medicare Cost plans in Minnesota: what they are, the 21 counties where they are still sold (2026), carriers, year-round enrollment, and how they compare with Advantage and Medigap",
     eyebrow="Plans · Minnesota&rsquo;s third path", h1="Medicare Cost plans in Minnesota: where they remain and who they fit",
     sub="Almost extinct nationally, Medicare Cost plans are still sold in 21 Minnesota counties. A local network at home, Original Medicare everywhere else, and the freedom to join or leave any month of the year.",
     keyfacts=["A Medicare Cost plan is a Medicare health plan that uses a network at home but lets you get care anywhere under Original Medicare. It can include Part D or be paired with a standalone Part D plan.",
               "Cost plans ended in most of Minnesota (including the entire Twin Cities metro) in 2019 under a federal rule that retires them wherever two or more Medicare Advantage plans compete.",
               "For [[YEAR]] they are still sold in 21 counties, listed below, by Blue Cross Blue Shield of Minnesota and Medica. Premiums and county availability are published each year by the Minnesota Department of Commerce.",
               "You can enroll in or leave a Cost plan any month it is accepting members &mdash; you do not have to wait for the Annual Election Period."],
     body="""<p>Before 2019, Medicare Cost plans covered more Minnesotans than Medicare Advantage did, and most of the state never had to learn the difference. Then a federal rule retired Cost plans in every county with at least two competing Advantage plans, and roughly 300,000 Minnesotans had to choose something else. The plans survived where competition was thin &mdash; the north woods, the Arrowhead, a band of southwestern prairie counties &mdash; and they are still there.</p>
<h2>How a Cost plan works</h2>
<ul>
<li><strong>At home,</strong> you use the plan&rsquo;s network, with plan copays, much like an HMO.</li>
<li><strong>Outside the network,</strong> Original Medicare pays as if you had no plan at all. Care in Rochester, Fargo, Arizona or Florida is covered the way Original Medicare covers it &mdash; you owe Medicare&rsquo;s deductibles and coinsurance, not a denial.</li>
<li><strong>Drug coverage</strong> can be built into the plan or bought as a standalone <a href="/part-d">Part D plan</a>; if you buy it separately, it does not have to come from the same company.</li>
<li><strong>Enrollment is continuous.</strong> You can join whenever the plan is accepting new members and leave any time by switching to Original Medicare, which makes a Cost plan easier to test-drive than an Advantage plan.</li>
<li><strong>Some Cost plans are sold with a supplement-like layer</strong> that covers Original Medicare&rsquo;s cost-sharing when you go out of network. Ask what happens to the Part A deductible out of area &mdash; that is the question that separates the designs.</li>
</ul>
<h2>The [[YEAR]] county list</h2>
<p>According to the Minnesota Department of Commerce&rsquo;s annual Medicare Cost plan guide, Cost plans are offered for [[YEAR]] in these 21 counties:</p>
""" + COUNTY_LIST_HTML + """
<p>The list has been stable since 2019 but is re-published each fall, and a carrier can add or drop a county. Check the current guide, or ask us, before you count on it.</p>
<h2>Cost plan vs Medicare Advantage vs a Minnesota supplement</h2>
<table class="ctable">
<caption>Three ways to fill the gaps in Original Medicare, compared. Details vary by plan and county.</caption>
<thead><tr><th scope="col">&nbsp;</th><th scope="col">Cost plan</th><th scope="col">Medicare Advantage</th><th scope="col">Basic / Extended Basic supplement</th></tr></thead>
<tbody>
<tr><th scope="row">Care at home</th><td>Plan network, plan copays</td><td>Plan network, plan copays</td><td>Any provider that accepts Medicare</td></tr>
<tr><th scope="row">Care out of area</th><td>Original Medicare pays; you owe its cost-sharing</td><td>Emergencies only on most plans</td><td>Fully covered anywhere in the U.S.</td></tr>
<tr><th scope="row">When you can join or leave</th><td>Any month the plan is open</td><td>Enrollment periods only</td><td>Guaranteed during set windows; underwritten otherwise</td></tr>
<tr><th scope="row">Drug coverage</th><td>Built in or add Part D</td><td>Usually built in</td><td>Add a Part D plan</td></tr>
<tr><th scope="row">Where sold</th><td>21 counties</td><td>Varies by county, changing yearly</td><td>Statewide</td></tr>
</tbody></table>
<div class="note-box"><p><strong>Why Minnesota snowbirds keep asking about Cost plans.</strong> A Cost plan is the only network plan that follows you to Arizona through Original Medicare. If your county is on the list and you winter away, it belongs in the comparison &mdash; alongside a supplement, which covers even more out of state. Our <a href="/snowbirds">snowbird guide</a> lays the three side by side.</p></div>
<h2>Who a Cost plan tends to suit</h2>
<p>People in a Cost-plan county who like a local network and low premiums but travel, split the year between states, or get specialty care in Rochester or the metro; and people who want the option of leaving mid-year without waiting for October. People who never leave their county and want the richest extras may prefer an Advantage plan; people who want no network question at all may prefer a supplement.</p>""",
     faqs=[("Are Medicare Cost plans still available in Minnesota?", "Yes, in 21 counties for [[YEAR]]: Aitkin, Carlton, Cook, Goodhue, Itasca, Kanabec, Koochiching, Lake, Le Sueur, McLeod, Meeker, Mille Lacs, Pine, Pipestone, Rice, Rock, St. Louis, Sibley, Stevens, Traverse and Yellow Medicine, per the Minnesota Department of Commerce. They ended in the Twin Cities metro and most other counties in 2019."),
           ("Who sells Medicare Cost plans in Minnesota?", "Blue Cross Blue Shield of Minnesota and Medica. The Minnesota Department of Commerce publishes each company&rsquo;s Cost plan premiums by county every year."),
           ("What is the difference between a Cost plan and Medicare Advantage?", "Both use a network at home. Outside the network, a Cost plan falls back on Original Medicare so your care is still covered (with Medicare&rsquo;s cost-sharing), while most Advantage plans cover only emergencies. Cost plans also let you enroll or leave any month; Advantage plans are tied to enrollment periods."),
           ("Can I join a Cost plan outside the Annual Election Period?", "Yes. Cost plans accept enrollment any month they are open to new members, and you can leave any time by returning to Original Medicare. If the plan includes Part D, the drug portion follows Part D&rsquo;s enrollment rules.")],
     sources=[SRC_MN_COST_GUIDE, SRC_MEDICARE_OTHER_PLANS, SRC_CMS], cta="In a Cost-plan county? Let&rsquo;s compare all three paths.", about="Medicare Cost plans in Minnesota"),

# ---------------------------------------------------------------- Part D
dict(slug="part-d", nav_title="Medicare Part D plans in Minnesota", crumb="Part D", scene="lakes",
     title="Medicare Part D Plans in Minnesota [[YEAR]] | ECOS Medicare Solutions",
     desc="Part D drug plans in Minnesota: the [[YEAR]] $2,100 cap, $615 maximum deductible, choosing by your medications, the late penalty, and pairing with a Cost plan or supplement.",
     llm="Part D drug plans in Minnesota: 2026 $2,100 cap, choosing by your medications, penalties, pairing with Cost plans and supplements",
     eyebrow="Plans · Part D", h1="Medicare Part D drug plans in Minnesota",
     sub="Standalone prescription coverage chosen around your medications and your pharmacy &mdash; whether you pair it with Original Medicare, a Minnesota supplement or a Cost plan.",
     keyfacts=["[[YEAR]] Part D out-of-pocket cap: $2,100. Once your spending on covered drugs reaches it, you pay $0 for covered medications the rest of the year.",
               "[[YEAR]] maximum Part D deductible: $615; many plans set a lower one or none. The national base premium used for penalties is $38.99.",
               "Going 63 or more days without creditable drug coverage after you are first eligible adds a permanent penalty to your premium.",
               "Minnesota Cost plans can include Part D or be paired with a standalone plan from any company; a Basic or Extended Basic supplement always needs a separate Part D plan."],
     body="""<p>Medicare Part D covers prescription drugs through private plans approved by Medicare. You can get it as a standalone plan alongside Original Medicare (and usually a <a href="/medicare-supplement">Minnesota supplement</a>), built into most <a href="/medicare-advantage">Medicare Advantage</a> plans, or built into or paired with a <a href="/medicare-cost-plans">Cost plan</a>.</p>
<h2>What changed for [[YEAR]]</h2>
<ul>
<li><strong>$2,100 out-of-pocket cap.</strong> Once your spending on covered drugs reaches $2,100 in [[YEAR]], you pay $0 for covered medications the rest of the year.</li>
<li><strong>Deductible up to $615.</strong> That is the most a plan can charge as its [[YEAR]] deductible; many plans set a lower one or none at all.</li>
<li><strong>Premiums vary by plan.</strong> The [[YEAR]] national base beneficiary premium &mdash; the figure used to calculate penalties &mdash; is $38.99, but what you actually pay depends on the plan you choose.</li>
<li><strong>The Medicare Prescription Payment Plan</strong> lets you spread out-of-pocket drug costs across the year in monthly instalments instead of paying at the counter. It changes when you pay, not how much.</li>
</ul>
<h2>Choosing a plan is about your drug list</h2>
<p>Every Part D plan has a formulary &mdash; its list of covered drugs and the tier (and cost) for each &mdash; and a pharmacy network with preferred pharmacies that cost less. Two plans with similar premiums can cost very different amounts once your specific prescriptions are run through them, and a plan that is cheap at a Twin Cities chain may be expensive at an independent pharmacy in Grand Marais. We compare plans using your actual medication list and your pharmacy, so the lowest <em>total</em> cost wins, not just the lowest premium.</p>
<div class="note-box"><p><strong>Watch the late-enrollment penalty.</strong> If you go 63 or more days without Part D or other creditable drug coverage after you are first eligible, a permanent penalty can be added to your premium for as long as you have Part D. Employer coverage, the VA pharmacy and TRICARE For Life are all creditable; keep proof. See our <a href="/medicare-costs">[[YEAR]] costs page</a> to estimate a penalty.</p></div>
<h2>Part D and Minnesota&rsquo;s plan types</h2>
<ul>
<li><strong>With a Basic or Extended Basic supplement:</strong> always add a standalone Part D plan; the supplement has no drug coverage.</li>
<li><strong>With a Cost plan:</strong> some Cost plans include Part D, others let you buy any standalone plan. If you are unhappy with a Cost plan&rsquo;s drug coverage you can often keep the medical side and change only the drug plan during the Annual Election Period.</li>
<li><strong>With Medicare Advantage:</strong> usually built in. If you take a Medicare Advantage plan that includes drug coverage, you cannot add a separate Part D plan.</li>
</ul>
<h2>Higher earners and lower incomes</h2>
<p>If your income is above the [[YEAR]] thresholds ($109,000 single / $218,000 joint, based on your 2024 tax return), you pay a Part D income-related surcharge (IRMAA) on top of your plan premium; our <a href="/medicare-costs">costs &amp; IRMAA page</a> lays out the brackets. At the other end, <strong>Extra Help</strong> (the Low-Income Subsidy) cuts Part D premiums and copays substantially for people with limited income and resources; in Minnesota, qualifying for a Medicare Savings Program or Medical Assistance qualifies you for Extra Help automatically. See <a href="/medicaid">Medical Assistance &amp; MSHO</a>.</p>""",
     faqs=[("When should I enroll in Part D?", "Usually when you first become eligible for Medicare, even if you take few or no medications &mdash; that avoids the late-enrollment penalty. Exceptions apply if you have other creditable drug coverage such as an employer plan, TRICARE For Life or VA pharmacy benefits."),
           ("What is the [[YEAR]] Part D out-of-pocket cap?", "$2,100. After your covered-drug spending reaches that amount in [[YEAR]], you pay nothing more for covered medications for the rest of the year."),
           ("Do I need Part D with a Minnesota Cost plan?", "You need creditable drug coverage from somewhere. Some Cost plans include Part D; if yours does not, you can add a standalone Part D plan from any company."),
           ("Can you help me pick a plan around my medications?", "Yes &mdash; that is the most useful thing we do here. Bring your medication list and pharmacy, and we compare plans on your total expected yearly cost.")],
     sources=[SRC_PARTD_GOV, SRC_CMS, SRC_MEDICARE_COSTS], cta="Let&rsquo;s match a drug plan to your prescriptions.", about="Medicare Part D in Minnesota"),

# ---------------------------------------------------------------- Costs
dict(slug="medicare-costs", nav_title="[[YEAR]] Medicare costs, full IRMAA chart, and penalty/IRMAA calculators", crumb="[[YEAR]] Costs", scene="bluffs",
     title="[[YEAR]] Medicare Costs &amp; IRMAA in Minnesota | ECOS Medicare Solutions",
     desc="[[YEAR]] Medicare costs for Minnesota: Part A/B/D premiums and deductibles, the full IRMAA chart, and free calculators for IRMAA and late-enrollment penalties.",
     llm="2026 Medicare costs: Part A/B/D premiums and deductibles, the full IRMAA chart, and calculators for IRMAA and the Part B / Part D late penalties",
     eyebrow="Costs · Verified [[YEAR]] figures", h1="[[YEAR]] Medicare costs and IRMAA, with calculators",
     sub="Every dollar figure on this page comes from the CMS release for [[YEAR]]. The calculators are estimates for planning; Social Security and Medicare set your official amounts.",
     keyfacts=["[[YEAR]] Part B standard premium $202.90/month; Part B deductible $283; Part A hospital deductible $1,736 per benefit period.",
               "[[YEAR]] Part D: out-of-pocket cap $2,100; maximum deductible $615; national base premium $38.99.",
               "IRMAA surcharges begin above $109,000 (single) or $218,000 (joint) of 2024 modified adjusted gross income, and are a cliff: $1 over a threshold moves you to the whole next tier.",
               "Part B late penalty: 10% for each full 12 months without Part B or creditable coverage, for life. Part D late penalty: about 1% of the base premium per month without creditable drug coverage."],
     body="""<p>Medicare&rsquo;s costs change every year, so here are the current <strong>[[YEAR]]</strong> figures, the full income-related surcharge (IRMAA) chart, and a few simple calculators. These are estimates to help you plan &mdash; your official amounts come from Social Security and Medicare. We refresh this page every year when CMS publishes the new numbers, usually in November.</p>
<h2>[[YEAR]] Original Medicare costs</h2>
<table class="ctable">
<caption>Source: CMS [[YEAR]] Medicare Parts A &amp; B Premiums and Deductibles (released Nov 14, 2025) and [[YEAR]] Part D parameters.</caption>
<thead><tr><th scope="col">Item</th><th scope="col">[[YEAR]] amount</th></tr></thead>
<tbody>
<tr><th scope="row">Part B standard premium</th><td>$202.90 / month</td></tr>
<tr><th scope="row">Part B annual deductible</th><td>$283</td></tr>
<tr><th scope="row">Part A hospital deductible</th><td>$1,736 per benefit period</td></tr>
<tr><th scope="row">Part A coinsurance, days 61&ndash;90</th><td>$434 / day</td></tr>
<tr><th scope="row">Part A coinsurance, lifetime reserve days</th><td>$868 / day</td></tr>
<tr><th scope="row">Skilled nursing coinsurance, days 21&ndash;100</th><td>$217 / day</td></tr>
<tr><th scope="row">Part D maximum deductible</th><td>$615</td></tr>
<tr><th scope="row">Part D out-of-pocket cap</th><td>$2,100 / year</td></tr>
<tr><th scope="row">Part D national base beneficiary premium</th><td>$38.99 (used for penalties)</td></tr>
</tbody></table>
<p>Most people pay $0 for Part A because they paid Medicare taxes while working. Part D, Medicare Advantage, Cost plan and supplement premiums vary by plan and carrier. A Minnesota <a href="/medicare-supplement">Extended Basic</a> plan covers the Part A deductible; a Basic plan covers it only with the rider.</p>
<h2>[[YEAR]] IRMAA: what higher earners pay</h2>
<p>If your income is above the thresholds below, you pay an income-related surcharge on top of your Part B and Part D premiums. Your [[YEAR]] IRMAA is based on the income (MAGI) from your <strong>2024</strong> tax return. IRMAA is a cliff: going $1 over a threshold moves you into the whole next tier. A Roth conversion, a farm or cabin sale, or a big capital gain two years ago is the usual surprise.</p>
<table class="ctable">
<caption>[[YEAR]] IRMAA tiers. Part D amounts are added to your plan&rsquo;s premium. Source: CMS / SSA, [[YEAR]].</caption>
<thead><tr><th scope="col">Single filer (2024 MAGI)</th><th scope="col">Married filing jointly</th><th scope="col">Part B total / month</th><th scope="col">Part D surcharge / month</th></tr></thead>
<tbody>
<tr><td>$109,000 or less</td><td>$218,000 or less</td><td>$202.90</td><td>$0.00</td></tr>
<tr><td>$109,001&ndash;$137,000</td><td>$218,001&ndash;$274,000</td><td>$284.10</td><td>+$14.50</td></tr>
<tr><td>$137,001&ndash;$171,000</td><td>$274,001&ndash;$342,000</td><td>$405.80</td><td>+$37.50</td></tr>
<tr><td>$171,001&ndash;$205,000</td><td>$342,001&ndash;$410,000</td><td>$527.50</td><td>+$60.40</td></tr>
<tr><td>$205,001&ndash;$499,999</td><td>$410,001&ndash;$749,999</td><td>$649.20</td><td>+$83.30</td></tr>
<tr><td>$500,000 or more</td><td>$750,000 or more</td><td>$689.90</td><td>+$91.00</td></tr>
</tbody></table>
<p style="font-size:.92rem;color:var(--ink-soft)">Married filing separately uses a compressed two-tier structure with a single threshold at $109,000 &mdash; if that is you, call us and we will walk through it. If your income has dropped since 2024 because you retired, sold a business or lost a spouse, you can ask Social Security to use this year&rsquo;s income instead (Form SSA-44).</p>
<h2>Estimate your numbers</h2>
<p>These calculators are <strong>estimates</strong> using published [[YEAR]] figures. They store nothing. For your official amount, see Medicare.gov or contact Social Security.</p>
<div class="calc">
  <h3>1. IRMAA estimator</h3>
  <div class="field"><label for="fs">Filing status</label>
    <select id="fs"><option value="single">Single / head of household</option><option value="joint">Married filing jointly</option></select></div>
  <div class="field"><label for="magi">Your 2024 income (MAGI)</label>
    <input id="magi" type="number" inputmode="numeric" min="0" step="1000" placeholder="e.g. 95000"></div>
  <button class="btn btn--primary" type="button" onclick="calcIrmaa()">Estimate my premiums</button>
  <div class="calc__result" id="irmaaOut" role="status" aria-live="polite"></div>
</div>
<div class="calc">
  <h3>2. Part B late-enrollment penalty</h3>
  <p style="margin:0 0 .6rem;font-size:.98rem;color:var(--ink-soft)">10% is added for each full 12 months you could have had Part B but didn&rsquo;t (and lacked other qualifying coverage). The penalty generally lasts as long as you have Part B.</p>
  <div class="field"><label for="bmonths">Full months without Part B after you were eligible</label>
    <input id="bmonths" type="number" inputmode="numeric" min="0" step="1" placeholder="e.g. 24"></div>
  <button class="btn btn--primary" type="button" onclick="calcPartB()">Estimate Part B penalty</button>
  <div class="calc__result" id="bOut" role="status" aria-live="polite"></div>
</div>
<div class="calc">
  <h3>3. Part D late-enrollment penalty</h3>
  <p style="margin:0 0 .6rem;font-size:.98rem;color:var(--ink-soft)">Roughly 1% of the national base premium ($38.99 in [[YEAR]]) for each full month you went without creditable drug coverage. It is added to your Part D premium and recalculated each year.</p>
  <div class="field"><label for="dmonths">Full months without creditable drug coverage</label>
    <input id="dmonths" type="number" inputmode="numeric" min="0" step="1" placeholder="e.g. 15"></div>
  <button class="btn btn--primary" type="button" onclick="calcPartD()">Estimate Part D penalty</button>
  <div class="calc__result" id="dOut" role="status" aria-live="polite"></div>
</div>
<div class="note-box"><p>Estimates only, for planning. Your official premiums and any penalty are set by Social Security and Medicare. Want help reading your own numbers or appealing an IRMAA determination (Form SSA-44)? Call <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>.</p></div>
<script>
(function(){
  var fmt=function(n){return '$'+n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});};
  var single=[109000,137000,171000,205000,499999];
  var joint =[218000,274000,342000,410000,749999];
  var partB =[202.90,284.10,405.80,527.50,649.20,689.90];
  var partD =[0,14.50,37.50,60.40,83.30,91.00];
  window.calcIrmaa=function(){
    var st=document.getElementById('fs').value;
    var magi=parseFloat(document.getElementById('magi').value);
    var out=document.getElementById('irmaaOut');
    if(isNaN(magi)||magi<0){out.innerHTML='<p>Please enter your 2024 income to see an estimate.</p>';return;}
    var t=st==='joint'?joint:single, idx=0;
    for(var i=0;i<t.length;i++){if(magi>t[i])idx++;}
    var b=partB[idx], d=partD[idx];
    var msg = idx===0
      ? 'Based on that income, you would pay the <strong>standard</strong> Part B premium of '+fmt(b)+' per month and <strong>no</strong> Part D surcharge.'
      : 'Estimated [[YEAR]] Part B premium: <strong>'+fmt(b)+'/month</strong>. Estimated Part D surcharge: <strong>+'+fmt(d)+'/month</strong> on top of your plan premium.';
    out.innerHTML='<p>'+msg+'</p><p class="calc__fine">Estimate based on 2024 MAGI and [[YEAR]] CMS/SSA figures. Official tier is set by Social Security.</p>';
  };
  window.calcPartB=function(){
    var m=parseInt(document.getElementById('bmonths').value,10);
    var out=document.getElementById('bOut');
    if(isNaN(m)||m<0){out.innerHTML='<p>Enter the number of months to see an estimate.</p>';return;}
    var periods=Math.floor(m/12), pct=periods*10, pen=202.90*0.10*periods, tot=202.90+pen;
    if(periods===0){out.innerHTML='<p>Fewer than 12 full months generally means <strong>no</strong> Part B penalty. Keep proof of any other creditable coverage.</p>';return;}
    out.innerHTML='<p>Estimated penalty: <strong>+'+pct+'%</strong> &rarr; about <strong>'+fmt(pen)+'/month</strong> added to Part B, for an estimated total of <strong>'+fmt(tot)+'/month</strong>.</p><p class="calc__fine">Based on the [[YEAR]] standard premium; the penalty generally continues for as long as you have Part B.</p>';
  };
  window.calcPartD=function(){
    var m=parseInt(document.getElementById('dmonths').value,10);
    var out=document.getElementById('dOut');
    if(isNaN(m)||m<0){out.innerHTML='<p>Enter the number of months to see an estimate.</p>';return;}
    var pen=Math.round((0.01*38.99*m)/0.10)*0.10;
    out.innerHTML='<p>Estimated Part D penalty: about <strong>'+fmt(pen)+'/month</strong>, added to your Part D plan premium.</p><p class="calc__fine">Based on the [[YEAR]] national base premium of $38.99; recalculated each year as that figure changes.</p>';
  };
})();
</script>""",
     faqs=[("What is the standard Medicare Part B premium for [[YEAR]]?", "The standard Part B premium is $202.90 per month in [[YEAR]], with a $283 annual deductible. Higher-income beneficiaries pay more through IRMAA."),
           ("What is IRMAA?", "IRMAA (Income-Related Monthly Adjustment Amount) is a surcharge added to your Part B and Part D premiums if your income is above certain thresholds. For [[YEAR]] it is based on your 2024 tax return and starts above $109,000 (single) or $218,000 (joint)."),
           ("What is the Part D out-of-pocket cap in [[YEAR]]?", "$2,100. Once your spending on covered drugs reaches that amount in [[YEAR]], you pay nothing more for covered medications for the rest of the year."),
           ("Can I get help paying the Part B premium in Minnesota?", "Possibly. Minnesota&rsquo;s Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people with limited income, and Minnesota&rsquo;s asset limits ($10,000 single / $18,000 married) are higher than most states&rsquo;. Apply through your county or tribal human services office; see our Medical Assistance page.")],
     sources=[SRC_CMS, SRC_MEDICARE_COSTS, SRC_MSP], cta="Not sure which costs apply to you? Let&rsquo;s look together.", about="Medicare costs and IRMAA", schema_type="Article"),

# ---------------------------------------------------------------- Turning 65
dict(slug="turning-65", nav_title="Turning 65 in Minnesota guide", crumb="Turning 65", scene="northwoods",
     title="Turning 65 in Minnesota: Medicare Guide [[YEAR]] | ECOS Medicare Solutions",
     desc="Turning 65 in Minnesota: your 7-month window, Basic vs Extended Basic, Cost plans in 21 counties, the deadlines with lifelong penalties, and a checklist.",
     llm="Turning 65 in Minnesota: enrollment windows, the parts of Medicare, Minnesota-specific choices, deadlines with lifelong penalties, and a checklist",
     eyebrow="Guide · New to Medicare", h1="Turning 65 in Minnesota: your Medicare starter guide",
     sub="What to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; written for Minnesota, where the plan choices are not the ones the national websites describe.",
     keyfacts=["Your Initial Enrollment Period is 7 months: the 3 months before your birthday month, the month itself, and the 3 months after. Enroll in the first 3 to avoid a gap.",
               "Your Medigap open enrollment is a separate 6-month window that starts when you are 65 and have Part B. In Minnesota it guarantees you the Basic and Extended Basic plans regardless of health.",
               "Still working with qualifying employer coverage? You can usually delay Part B without penalty and get a Special Enrollment Period later.",
               "Miss Part B or Part D without creditable coverage and the penalty lasts for life: 10% per 12 months for Part B; about 1% per month for Part D."],
     body="""<p>Turning 65 comes with a stack of Medicare mail and a few decisions that matter for the rest of your life. Here is the plain-English version &mdash; what to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; with the Minnesota twists that most guides leave out. When you are ready, we walk through your specific options at no cost.</p>
<h2>1. Your enrollment window: the 7-month Initial Enrollment Period</h2>
<p>Your Initial Enrollment Period (IEP) is seven months long: the three months <em>before</em> the month you turn 65, your birthday month, and the three months <em>after</em>. Signing up in the three months before your birthday means coverage starts the first of your birthday month. You enroll through Social Security (online at ssa.gov, by phone, or at an office); if you already draw Social Security you are enrolled in A and B automatically.</p>
<ul>
<li><strong>Part A</strong> (hospital) is premium-free for most people, so most enroll when first eligible.</li>
<li><strong>Part B</strong> (medical) carries the $202.90 standard monthly premium in [[YEAR]] &mdash; and a timing decision if you are still working (see below).</li>
</ul>
<h2>2. The parts of Medicare, briefly</h2>
<ul>
<li><strong>Part A</strong> &mdash; inpatient hospital, skilled nursing, hospice.</li>
<li><strong>Part B</strong> &mdash; doctors, outpatient care, preventive services.</li>
<li><strong>Part C (Medicare Advantage)</strong> &mdash; a private all-in-one alternative that bundles A, B and usually drug coverage.</li>
<li><strong>Part D</strong> &mdash; prescription drug coverage.</li>
<li><strong>Medicare Cost plans</strong> &mdash; a Minnesota survival: a network plan at home that falls back on Original Medicare elsewhere, sold in <a href="/medicare-cost-plans">21 counties</a>.</li>
</ul>
<h2>3. Your big decision: two paths (three, in 21 counties)</h2>
<table class="ctable">
<caption>The common ways Minnesotans put their coverage together.</caption>
<thead><tr><th scope="col">Path</th><th scope="col">What it looks like</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + extras</th><td>Parts A &amp; B, usually plus a Minnesota <a href="/medicare-supplement">Basic or Extended Basic supplement</a> and a standalone <a href="/part-d">Part D</a> plan. Any provider nationwide that accepts Medicare; predictable costs; monthly premiums.</td></tr>
<tr><th scope="row">Medicare Advantage</th><td>A single <a href="/medicare-advantage">Part C</a> plan that bundles everything, often $0 premium, with extras like dental and vision &mdash; using a local network that changes yearly.</td></tr>
<tr><th scope="row">Medicare Cost plan (21 counties)</th><td>A <a href="/medicare-cost-plans">network plan at home</a> that uses Original Medicare anywhere else; enroll or leave any month. Popular with snowbirds.</td></tr>
</tbody></table>
<p>If you lean toward a supplement, there is a second deadline that is easy to miss: your Medigap open enrollment is its own six-month window, separate from the seven-month one above, and it does not repeat. Our research site sets the two side by side for Minnesota &mdash; <a href="https://www.mymedigaprate.com/turning-65/minnesota">turning 65 in Minnesota</a>.</p>
<h2>4. Deadlines that carry lifelong penalties</h2>
<div class="note-box"><p><strong>Part B late penalty.</strong> If you don&rsquo;t enroll in Part B when first eligible (and don&rsquo;t have qualifying employer coverage), a permanent penalty of 10% per 12 months is added to your premium for life.</p>
<p><strong>Part D late penalty.</strong> Going 63+ days without creditable drug coverage can add a permanent surcharge to your Part D premium.</p>
<p><strong>Medigap open enrollment.</strong> Your six-month Medigap open enrollment begins when you are 65 <em>and</em> enrolled in Part B &mdash; during it Minnesota guarantees you the Basic and Extended Basic plans without medical underwriting. Beginning August 1, 2026, Minnesota also gives people aged 65&ndash;70 a one-time window each fall to buy a supplement without underwriting, with a premium surcharge; it is a safety net, not a substitute for using the first window well.</p></div>
<h2>5. Still working at 65?</h2>
<p>If you (or your spouse) have qualifying employer coverage, you may be able to delay Part B without penalty and get a Special Enrollment Period when that coverage ends. The rules depend on employer size (20 or more employees is the usual line) and whether the drug coverage is creditable. Minnesota&rsquo;s big employers &mdash; the state, the university, the health systems, 3M, Target &mdash; generally qualify; a small business or a retiree plan may not. It is worth a quick conversation before you decide, and a form (CMS-L564) from your employer when you do enroll.</p>
<h2>6. A simple checklist</h2>
<ul>
<li>Mark your 7-month IEP on the calendar (it starts 3 months before your birthday month).</li>
<li>Decide on Part B based on whether you have other creditable coverage.</li>
<li>Find out whether your county is one of the <a href="/medicare-cost-plans">21 Cost-plan counties</a>.</li>
<li>Choose your path: Original Medicare + supplement + Part D, Medicare Advantage, or a Cost plan.</li>
<li>Check that your doctors and prescriptions are covered before you enroll &mdash; especially if Mayo Clinic is in the picture.</li>
<li>If you winter away, read the <a href="/snowbirds">snowbird guide</a> first; if you are a veteran, see how <a href="/veterans">TRICARE or VA benefits</a> coordinate; if you have Medical Assistance, see <a href="/medicaid">MSHO</a>.</li>
<li>Estimate your costs on our <a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA page</a>.</li>
</ul>
<p>None of this has to be done alone. We help Minnesotans sort through it every day &mdash; clearly, patiently, and at no cost to you. Minnesota Aging Pathways (800-333-2433) offers free, unbiased state counseling as well.</p>""",
     faqs=[("When should I sign up for Medicare if I&rsquo;m turning 65?", "During your Initial Enrollment Period &mdash; the seven months that span the three months before your birthday month, your birthday month, and the three months after. Signing up in the first three months means coverage starts on the first of your birthday month."),
           ("Do I have to take Part B at 65 if I&rsquo;m still working?", "Not always. If you have qualifying employer coverage (generally from an employer with 20 or more employees), you may delay Part B without penalty and get a Special Enrollment Period later. The rules depend on the employer&rsquo;s size, so confirm before you decide."),
           ("Is it better to get Medicare Advantage or Original Medicare with a supplement in Minnesota?", "Neither is automatically better &mdash; it depends on your doctors, prescriptions, travel and budget, and in 21 counties a Cost plan is a third choice. We compare them with you so the choice fits your life."),
           ("What is different about turning 65 in Minnesota?", "Your supplement choices are Basic and Extended Basic rather than the lettered plans, Cost plans still exist in 21 counties, and if you later regret an Advantage choice, a new state rule gives people aged 65&ndash;70 a one-time fall window to buy a supplement without health questions, with a surcharge.")],
     sources=[SRC_CMS, SRC_MN_COMMERCE_MEDIGAP, SRC_MN_STATUTE, SRC_AGING_PATHWAYS], cta="Turning 65? Let&rsquo;s talk it through before the window closes.", about="Medicare enrollment for people turning 65 in Minnesota"),

# ---------------------------------------------------------------- Snowbirds
dict(slug="snowbirds", nav_title="Medicare for Minnesota snowbirds (Arizona, Florida, Texas)", crumb="Snowbirds", scene="snow",
     title="Medicare for Minnesota Snowbirds: Plans That Travel | ECOS Medicare Solutions",
     desc="Which Minnesota Medicare plans work in Arizona, Florida or Texas: supplements travel, Cost plans use Original Medicare, most Advantage plans cover emergencies only.",
     llm="Medicare for Minnesota snowbirds: which plans work out of state (supplements, Cost plans, Advantage PPO vs HMO), residency and county rules, Part D away from home, the agency's Arizona offices",
     eyebrow="Guide · Winters away", h1="Medicare for Minnesota snowbirds",
     sub="Which plans follow you to Arizona, Florida or Texas, which ones stop at the state line, and how to keep a Minnesota address without losing coverage in January.",
     keyfacts=["A Minnesota Basic or Extended Basic supplement, with Original Medicare, works with any provider in the U.S. that accepts Medicare &mdash; the simplest snowbird coverage there is.",
               "A Medicare Cost plan (21 counties) covers you out of area through Original Medicare, with Medicare&rsquo;s cost-sharing. That is the main reason Cost plans stayed popular in Minnesota.",
               "Most Medicare Advantage HMOs cover only emergencies and urgent care outside their service area; some PPOs cover routine care out of network at higher cost. Read the Evidence of Coverage, not the brochure.",
               "Your plan is tied to the county of your permanent residence. If you change your legal residence to Arizona, you get a Special Enrollment Period and must pick a plan sold there. Our sister agency has offices in Mesa and Sun City."],
     body="""<p>Minnesota has more snowbirds per capita than almost any state, and the Medicare plan that works beautifully in Edina from May to October can leave you paying cash for a cardiologist in Mesa in February. The rules are not complicated, but they are unforgiving, so here they are plainly.</p>
<h2>Which plans travel</h2>
<table class="ctable">
<caption>How each Minnesota plan type behaves once you are outside its service area. Emergencies are covered by every plan, everywhere in the U.S.</caption>
<thead><tr><th scope="col">Plan type</th><th scope="col">Routine care in Arizona / Florida / Texas</th><th scope="col">What you pay there</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + Basic / Extended Basic supplement</th><td>Any provider that accepts Medicare</td><td>Same as at home &mdash; the supplement pays its share anywhere</td></tr>
<tr><th scope="row">Medicare Cost plan</th><td>Any provider that accepts Medicare, through Original Medicare</td><td>Medicare&rsquo;s deductible and 20% coinsurance, unless the plan adds out-of-area coverage</td></tr>
<tr><th scope="row">Medicare Advantage PPO</th><td>Out-of-network providers, if the plan allows</td><td>Higher out-of-network copays or coinsurance; check the plan&rsquo;s out-of-network maximum</td></tr>
<tr><th scope="row">Medicare Advantage HMO</th><td>Emergencies and urgent care only, on most plans</td><td>Routine care generally not covered out of area</td></tr>
<tr><th scope="row">Part D (standalone or built in)</th><td>National pharmacy networks; mail order</td><td>Preferred-pharmacy pricing may differ; check that a chain near your winter home is preferred</td></tr>
</tbody></table>
<div class="note-box"><p><strong>A few Advantage plans offer a &ldquo;visitor&rdquo; or &ldquo;travel&rdquo; benefit</strong> that extends in-network coverage for up to six or twelve months away from home, and some national carriers let you use their network in other states. It is plan-specific and it changes. If a travel benefit is the reason you are choosing an Advantage plan, we get it in writing from the Evidence of Coverage before you enroll.</p></div>
<h2>Residency: the rule that decides everything</h2>
<p>Medicare Advantage, Part D and Cost plans are sold by county, and you must live in the plan&rsquo;s service area &mdash; meaning your <em>permanent</em> residence. Wintering away for four or five months does not change that; most plans allow up to six months, and some up to twelve, out of area before they disenroll you. What does change it is moving your legal residence: registering to vote, licensing the car, filing as an Arizona resident. That triggers a Special Enrollment Period, ends your Minnesota plan, and means choosing from the plans sold in your new county.</p>
<p>A supplement is different. Once issued, a Minnesota Basic or Extended Basic policy stays in force wherever you live; your premium may be re-rated to the new state&rsquo;s rate area, but the coverage does not end.</p>
<h2>If you become an Arizona (or Florida, or Texas) resident</h2>
<p>Arizona uses the federal Medigap letters, so your Minnesota Extended Basic plan is a different animal from an Arizona Plan G, and the guaranteed-issue rules for switching differ by state. Our agency is licensed in Arizona, Florida and Texas as well as Minnesota, and our Arizona site has offices in Mesa and Sun City. Start with <a href="https://www.medicareenrollmentarizona.com/medicare-supplement-arizona">Medicare supplements in Arizona</a> or the Arizona city pages for <a href="https://www.medicareenrollmentarizona.com/medicare-mesa-az">Mesa</a> and <a href="https://www.medicareenrollmentarizona.com/medicare-sun-city-az">Sun City</a>; for a switch mid-year, the state-by-state rules are on <a href="https://www.mymedigaprate.com/switching-medigap-plans">switching Medigap plans</a>.</p>
<h2>Part D away from home</h2>
<p>Every Part D plan has a national pharmacy network, so filling a prescription in Scottsdale is not a problem. Pricing can be: plans have <em>preferred</em> pharmacies where copays are lowest, and the chain that is preferred at home may not be the chain near your winter place. Mail order at 90-day supplies solves most of it. We check both ZIP codes when we compare plans.</p>
<h2>What we recommend most snowbirds compare</h2>
<ol>
<li>A Minnesota <a href="/medicare-supplement">Extended Basic</a> or Basic-plus-riders supplement with a Part D plan that has preferred pharmacies in both places.</li>
<li>If your county is one of the <a href="/medicare-cost-plans">21 Cost-plan counties</a>, the Cost plan, priced against the supplement.</li>
<li>Only then an Advantage PPO with a documented travel benefit, priced honestly with the out-of-network maximum, not the $0 premium.</li>
</ol>""",
     faqs=[("Does my Minnesota Medicare Advantage plan work in Arizona?", "For emergencies and urgent care, yes &mdash; every plan covers those anywhere in the U.S. For routine care, most HMOs do not; some PPOs cover out-of-network care at higher cost, and a few plans have a travel benefit. Read the Evidence of Coverage, and if travel is why you are choosing the plan, get the benefit in writing."),
           ("Does a Minnesota Medicare supplement work in other states?", "Yes. A Basic or Extended Basic policy pays alongside Original Medicare with any provider in the country that accepts Medicare, with no network and no service area. It is the simplest snowbird coverage."),
           ("How long can I be out of state without losing my plan?", "It depends on the plan; most Medicare Advantage and Cost plans allow up to six months out of the service area, some up to twelve. Changing your legal residence ends the plan regardless of time, and gives you a Special Enrollment Period to pick a plan where you live now."),
           ("Can you help me if I become an Arizona resident?", "Yes. Our agency is licensed in Arizona and has offices in Mesa and Sun City through our Arizona site, and we are licensed in Florida and Texas as well. We help you move your coverage cleanly, including the Medigap switching rules that differ by state.")],
     sources=[SRC_MEDIGAP_GOV, SRC_MA_GOV, SRC_MEDICARE_OTHER_PLANS, ("Medicare Enrollment Arizona (sister site with Mesa and Sun City offices)", "https://www.medicareenrollmentarizona.com")],
     cta="Wintering away? Let&rsquo;s make sure your plan comes with you."),

# ---------------------------------------------------------------- Veterans
dict(slug="veterans", nav_title="Medicare for Minnesota veterans", crumb="Veterans", scene="aurora",
     title="Medicare for Minnesota Veterans: TRICARE &amp; VA | ECOS Medicare Solutions",
     desc="How TRICARE For Life and VA care (Minneapolis, St. Cloud, Fargo VA) work with Medicare in Minnesota, and why Part B timing matters even with VA care.",
     llm="Medicare for Minnesota veterans: TRICARE For Life vs VA coordination, the Part B timing mistake to avoid, Minneapolis / St. Cloud / Fargo VA",
     eyebrow="Your situation · Veterans", h1="Medicare for Minnesota veterans",
     sub="How TRICARE For Life and VA health care each work with Medicare &mdash; explained by a retired Air Force officer who has been through the paperwork himself.",
     keyfacts=["TRICARE For Life requires Medicare Part A and Part B and pays secondary to Medicare. Its pharmacy is creditable, so a separate Part D plan is usually unnecessary.",
               "VA health care does not coordinate with Medicare. VA medical coverage is <strong>not</strong> creditable for Part B, so delaying Part B because you have VA care can trigger a lifelong penalty; VA pharmacy <strong>is</strong> creditable for Part D.",
               "Minnesota&rsquo;s VA care runs through the Minneapolis VA Health Care System, the St. Cloud VA, and the Fargo VA for the northwest, plus community clinics statewide.",
               "With TRICARE For Life, an MA-only plan (Advantage without drug coverage) can add dental or vision without duplicating your prescription benefit."],
     body="""<p>Minnesota has roughly 300,000 veterans, served by the Minneapolis VA Health Care System, the St. Cloud VA, the Fargo VA across the river for the northwest, and community-based outpatient clinics from Rochester to Hibbing. The Guard&rsquo;s Camp Ripley, the 934th Airlift Wing at Minneapolis&ndash;St. Paul and the 148th Fighter Wing in Duluth keep a lot of retirees close by. How your military benefits coordinate with Medicare depends a lot on <em>which</em> benefit you have.</p>
<div class="twocol">
<div class="panel panel--good"><h3>TRICARE For Life (TFL)</h3>
<ul>
<li>Requires you to have Medicare <strong>Part A and Part B</strong>.</li>
<li>Pays <strong>secondary</strong> to Medicare &mdash; it wraps around Medicare like a supplement.</li>
<li>TFL pharmacy is <strong>creditable</strong>, so a separate Part D plan is usually unnecessary.</li>
<li>TFL can pair with a Medicare Advantage plan; because drug coverage already exists, an <strong>MA-only plan</strong> (Advantage without Part D) can add dental or vision without duplicating your Rx.</li>
<li>Because TFL already fills Medicare&rsquo;s gaps, a Minnesota supplement is usually unnecessary too.</li>
</ul></div>
<div class="panel panel--note"><h3>VA health care</h3>
<ul>
<li>Separate from Medicare &mdash; the two <strong>do not coordinate</strong> and don&rsquo;t disrupt each other.</li>
<li>Medicare doesn&rsquo;t pay at VA facilities; the VA doesn&rsquo;t cover Medicare cost-sharing.</li>
<li>VA medical is <strong>not creditable</strong> for Part B &mdash; enroll in Part B on time to avoid a lifelong penalty.</li>
<li>VA pharmacy <strong>is creditable</strong> for Part D, so you can rely on it for drug coverage.</li>
<li>Having both Medicare and VA gives you <strong>more places to get care</strong> &mdash; Mayo or Essentia with Medicare, the VA for service-connected care and prescriptions.</li>
</ul></div>
</div>
<div class="note-box"><p><strong>The mistake we most want you to avoid:</strong> skipping Part B because you have VA care. Because VA medical coverage isn&rsquo;t creditable for Part B, delaying it can trigger a penalty that lasts as long as you have Medicare, and it leaves you with no coverage at a non-VA hospital. If you are approaching 65 with VA benefits, talk to us about timing first.</p></div>
<h2>Which Minnesota plan fits a veteran</h2>
<ul>
<li><strong>VA care plus Original Medicare and a Minnesota supplement</strong> gives the widest choice: any hospital in the state, no network question, VA pharmacy for drugs. Many veterans skip Part D entirely because the VA pharmacy is creditable &mdash; keep the VA&rsquo;s letter as proof.</li>
<li><strong>VA care plus a $0-premium Advantage plan</strong> is common and can work, as long as you understand the network limits and that the VA and the plan will not coordinate a single bill.</li>
<li><strong>In a Cost-plan county,</strong> a <a href="/medicare-cost-plans">Cost plan</a> is worth a look for the same reasons it suits snowbirds.</li>
</ul>
<h2>How we help</h2>
<p>We look at exactly which benefits you carry, confirm your Part B timing, decide whether a separate drug plan adds anything, and &mdash; if it makes sense &mdash; compare an MA-only, Cost plan or supplement option for the gaps. Darin served 22 years in the Air Force and retired as an officer; he has filled out the same forms you are looking at.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not affiliated with or endorsed by the U.S. Department of Veterans Affairs, the Department of Defense, the TRICARE program, the Minnesota Department of Veterans Affairs, or the federal Medicare program.</p>""",
     faqs=[("I have VA health care. Do I need Medicare Part B?", "In most cases, yes &mdash; enroll on time. VA medical coverage is not considered creditable for Part B, so delaying Part B can cause a permanent late penalty. Having both VA and Medicare gives you more options for where to get care."),
           ("With TRICARE For Life, do I need a Part D drug plan or a Minnesota supplement?", "Usually neither. TRICARE For Life pharmacy is creditable drug coverage, and TFL already pays secondary to Medicare, filling the gaps a supplement would. That is also why an MA-only plan can make sense if you want dental or vision."),
           ("Does Medicare work at the Minneapolis or St. Cloud VA?", "No. Medicare does not pay for care at VA facilities, and the VA does not cover Medicare cost-sharing. They operate separately, which is why many veterans keep both."),
           ("Is VA pharmacy coverage enough to avoid the Part D penalty?", "Yes. VA prescription coverage is creditable for Part D, so you can skip a Part D plan without a penalty as long as you keep it. Keep the VA&rsquo;s notice of creditable coverage in case you enroll in Part D later.")],
     sources=[SRC_TFL, SRC_VA, SRC_CMS], cta="Let&rsquo;s sort out your benefits together, veteran to veteran.", about="Medicare for veterans"),

# ---------------------------------------------------------------- Medicaid / MSHO
dict(slug="medicaid", nav_title="Medicare + Minnesota Medical Assistance: MSHO, Medicare Savings Programs, Extra Help", crumb="Medical Assistance &amp; MSHO", scene="lakes",
     title="Medicare &amp; Medical Assistance in Minnesota: MSHO, QMB, SLMB | ECOS Medicare Solutions",
     desc="Medicare with Minnesota Medical Assistance: MSHO, Medicare Savings Programs (QMB, SLMB, QI) with Minnesota's higher asset limits, Extra Help, and where to apply.",
     llm="Medicare and Minnesota Medical Assistance (Medicaid): MSHO, MSC+, Medicare Savings Programs (QMB/SLMB/QI) with Minnesota's $10,000/$18,000 asset limits, Extra Help, county application",
     eyebrow="Your situation · Dual eligible", h1="Medicare and Minnesota Medical Assistance",
     sub="If you qualify for both Medicare and Medical Assistance &mdash; Minnesota&rsquo;s Medicaid &mdash; you may pay far less, and Minnesota Senior Health Options can put both programs under one card. Here is how it works in Minnesota.",
     keyfacts=["Medical Assistance (MA) is Minnesota&rsquo;s Medicaid program, run by the Department of Human Services. For people 65 and over you apply through your county or tribal human services office, not MNsure.",
               "Minnesota Senior Health Options (MSHO) is a voluntary program for people 65+ with Medicare Parts A and B and Medical Assistance: one health plan covers Medicare, Medicaid, Part D drugs and long-term services with a care coordinator.",
               "Medicare Savings Programs (QMB, SLMB, QI) pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles and copays. Minnesota&rsquo;s asset limits are $10,000 (single) and $18,000 (married), higher than most states.",
               "Qualifying for a Medicare Savings Program or Medical Assistance automatically qualifies you for Extra Help with Part D costs. Free counseling: Minnesota Aging Pathways, 800-333-2433."],
     body="""<p>Some Minnesotans qualify for both Medicare and Medical Assistance &mdash; often called being &ldquo;dual eligible.&rdquo; When that happens, <strong>Medicare pays first</strong>, and Medical Assistance may help with costs Medicare leaves behind, like premiums, deductibles and coinsurance, plus services Medicare does not cover at all, such as long-term care at home or in a nursing facility.</p>
<h2>How Medical Assistance works for seniors in Minnesota</h2>
<p>Medical Assistance is administered by the <strong>Minnesota Department of Human Services (DHS)</strong>, with eligibility determined by <strong>county and tribal human services offices</strong>. Eligibility is set by the state and the federal government &mdash; not by an insurance agency &mdash; so we point you to the right place to apply and help you understand how it affects your Medicare choices. People 65 and over apply through their county (or with the DHS application for seniors and people with disabilities), not through MNsure.</p>
<h2>Minnesota Senior Health Options (MSHO)</h2>
<p>MSHO is Minnesota&rsquo;s version of a Dual Special Needs Plan, and it goes further than most states&rsquo;. If you are 65 or older, have Medicare Parts A and B, and qualify for Medical Assistance, you can enroll in MSHO, and one health plan then covers <strong>Medicare, Medical Assistance, Part D drugs, and long-term services and supports</strong>, with a care coordinator who works with you and your doctors. One card, one customer-service number, no coordinating two programs yourself. MSHO plans are offered by Blue Plus (SecureBlue), HealthPartners, Medica, UCare and county-based plans, depending on where you live; UCare&rsquo;s exit from ordinary Medicare Advantage did not end its MSHO plan. People 65+ with Medical Assistance who do not choose MSHO are enrolled in <strong>Minnesota Senior Care Plus (MSC+)</strong>, which covers only the Medical Assistance side.</p>
<h2>Programs that can lower your costs</h2>
<ul>
<li><strong>Medicare Savings Programs (MSPs)</strong> &mdash; QMB, SLMB and QI &mdash; pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles, copays and coinsurance as well. Minnesota&rsquo;s income limits change each July; its asset limits are $10,000 for a single person and $18,000 for a married couple, well above the federal floor most states use. Apply through your county human services office.</li>
<li><strong>Extra Help (Low-Income Subsidy)</strong> lowers what you pay for Part D premiums, deductibles and copays. If you qualify for an MSP or Medical Assistance you get Extra Help automatically; otherwise apply through Social Security.</li>
<li><strong>Medical Assistance with a spenddown</strong> is how Minnesota covers some seniors whose income is slightly too high &mdash; ask the county whether an MSP or a spenddown is the better fit for you.</li>
</ul>
<p style="font-size:.92rem;color:var(--ink-soft)">Free, unbiased state counseling on all of this is available from Minnesota Aging Pathways &mdash; formerly the Senior LinkAge Line, Minnesota&rsquo;s State Health Insurance Assistance Program &mdash; at 800-333-2433, Monday to Friday. When you are ready to talk through the Medicare side, we are here at <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>.</p>
<h2>How we help</h2>
<p>We help you understand whether MSHO is available and a good fit where you live, how a Medicare Savings Program and Extra Help could reduce your costs, and how to keep your Medical Assistance benefits working alongside Medicare. Eligibility decisions rest with the county, the state and CMS; our job is to make the Medicare side clear.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not connected with or endorsed by Minnesota Medical Assistance, the Minnesota Department of Human Services, any county, or the federal Medicare program.</p>""",
     faqs=[("What is Minnesota Senior Health Options (MSHO)?", "A voluntary Minnesota program for people 65 and older who have Medicare Parts A and B and qualify for Medical Assistance. One health plan covers Medicare, Medical Assistance, Part D drugs and long-term services, with a care coordinator. It is Minnesota&rsquo;s version of a Dual Special Needs Plan."),
           ("Who counts as dual eligible in Minnesota?", "People who qualify for both Medicare and Medical Assistance. There are full and partial categories; eligibility is determined by your county or tribal human services office and CMS, based on income and assets."),
           ("Can Medical Assistance pay my Part B premium?", "Possibly. Minnesota&rsquo;s Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people who qualify, with asset limits of $10,000 (single) and $18,000 (married). Apply through your county human services office; Minnesota Aging Pathways (800-333-2433) can help."),
           ("Where do I apply for Medical Assistance if I am over 65?", "Through your county or tribal human services office, using the DHS application for seniors and people with disabilities &mdash; not through MNsure, which handles coverage for people under 65.")],
     sources=[SRC_MSHO, SRC_MSP, SRC_AGING_PATHWAYS, SRC_CMS], cta="Let&rsquo;s check what you qualify for.", about="Medicare and Medical Assistance dual eligibility in Minnesota"),

# ---------------------------------------------------------------- C-SNP
dict(slug="chronic-snp", nav_title="Chronic Special Needs Plans (C-SNP) in Minnesota", crumb="Chronic SNPs", scene="bluffs",
     title="Chronic SNPs (C-SNP) in Minnesota | ECOS Medicare Solutions",
     desc="Chronic Special Needs Plans in Minnesota: which conditions qualify, what a C-SNP offers, and whether one beats a regular Advantage plan or a supplement for you.",
     llm="Chronic Special Needs Plans (C-SNP) in Minnesota for qualifying chronic conditions",
     eyebrow="Your situation · Chronic conditions", h1="Chronic Special Needs Plans (C-SNPs) in Minnesota",
     sub="Medicare Advantage plans built around one chronic condition &mdash; diabetes, heart disease, lung disease, kidney failure &mdash; with care coordination and a drug list to match.",
     keyfacts=["A C-SNP is a Medicare Advantage plan limited to people with a specific qualifying chronic condition, verified by a provider.",
               "It includes Part D, usually a formulary built around the condition, and care coordination; premiums are often $0 or low.",
               "Availability varies by Minnesota county and changed for 2026 with the carrier exits; a regular Advantage plan or a Minnesota supplement may still serve you better.",
               "You can enroll in a C-SNP outside the normal windows when you are first diagnosed or first qualify."],
     body="""<p>A Chronic Special Needs Plan (C-SNP) is a type of Medicare Advantage plan built for people living with a specific severe or disabling chronic condition. Instead of a one-size-fits-all plan, a C-SNP shapes its provider network, drug list and care coordination around that condition.</p>
<h2>Conditions that can qualify</h2>
<p>Medicare defines the chronic conditions a C-SNP can serve. Common examples include:</p>
<ul>
<li>Diabetes mellitus</li>
<li>Chronic heart failure and certain cardiovascular disorders</li>
<li>Chronic lung disorders such as COPD</li>
<li>End-stage renal disease (ESRD) requiring dialysis</li>
<li>Certain other qualifying chronic conditions</li>
</ul>
<p>You generally need a provider to verify that you have the qualifying condition in order to enroll, and a diagnosis gives you a Special Enrollment Period to join one outside the normal windows.</p>
<h2>What a C-SNP usually offers</h2>
<ul>
<li><strong>Care coordination</strong> tailored to your condition, often including a care team or coordinator.</li>
<li><strong>A drug formulary</strong> built with your condition&rsquo;s medications in mind, plus included Part D coverage.</li>
<li><strong>Extra benefits</strong> that vary by plan, and frequently a $0 or low plan premium.</li>
</ul>
<div class="note-box"><p><strong>Is it the right move?</strong> A C-SNP can be a strong fit if your care centers on one chronic condition and you want coordinated support. But it is still a network plan, so the Mayo or Essentia question applies, and a regular Medicare Advantage plan, a Cost plan, or a <a href="/medicare-supplement">Minnesota supplement</a> may serve you better depending on your doctors and other needs. We compare them with you &mdash; no cost, no pressure.</p></div>
<p>Related: <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a> for facility-level care, and <a href="/medicaid">Minnesota Senior Health Options (MSHO)</a> for people with both Medicare and Medical Assistance.</p>""",
     faqs=[("Who can join a Chronic Special Needs Plan in Minnesota?", "People with Medicare Parts A and B who have a qualifying chronic condition, confirmed by a provider, and who live in the plan&rsquo;s service area. Availability varies by county in Minnesota and changes each plan year."),
           ("Does a C-SNP include drug coverage?", "Yes. C-SNPs are Medicare Advantage plans that include Part D prescription coverage, usually with a formulary tailored to the plan&rsquo;s target condition."),
           ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans is free to you.")],
     sources=[SRC_MA_GOV], cta="Let&rsquo;s see whether a C-SNP fits your condition.", about="Chronic Special Needs Plans", priority="0.6"),

# ---------------------------------------------------------------- I-SNP
dict(slug="institutional-snp", nav_title="Institutional Special Needs Plans (I-SNP) in Minnesota", crumb="Institutional SNPs", scene="lakes",
     title="Institutional SNPs (I-SNP) in Minnesota | ECOS Medicare Solutions",
     desc="Institutional Special Needs Plans in Minnesota for people in a nursing facility or needing that level of care at home: who qualifies and how it fits with MSHO.",
     llm="Institutional Special Needs Plans (I-SNP) in Minnesota for facility-level care",
     eyebrow="Your situation · Facility-level care", h1="Institutional Special Needs Plans (I-SNPs) in Minnesota",
     sub="Medicare Advantage plans for people who live in a nursing facility, or need that level of care at home, with care brought to where you live.",
     keyfacts=["An I-SNP is a Medicare Advantage plan for people who live, or are expected to live, 90 days or more in a qualifying facility, or who need that level of care at home per a state assessment.",
               "It brings care coordination on site &mdash; often nurse practitioners working with facility staff &mdash; and includes Part D.",
               "In Minnesota, many people in long-term care also qualify for Medical Assistance; MSHO may then be the better fit, and we compare the two."],
     body="""<p>An Institutional Special Needs Plan (I-SNP) is a Medicare Advantage plan for people who live in &mdash; or are expected to need the level of care provided by &mdash; an institution such as a nursing facility, or who need that level of care while living at home.</p>
<h2>Who an I-SNP is for</h2>
<ul>
<li>People who have lived, or are expected to live, in a qualifying facility (such as a skilled nursing or long-term care facility) for 90 days or more.</li>
<li>People who require an institutional level of care, sometimes provided at home, as confirmed by a state-approved assessment (in Minnesota, the county&rsquo;s long-term care consultation).</li>
</ul>
<h2>How it works</h2>
<ul>
<li><strong>On-site care coordination.</strong> I-SNPs typically bring care management to where the member lives, often with nurse practitioners or care teams who work directly with facility staff, which can mean fewer hospital transfers.</li>
<li><strong>Included Part D coverage</strong> and benefits designed around higher-needs care.</li>
<li><strong>Coordination with families</strong> on care decisions and transitions.</li>
</ul>
<div class="note-box"><p><strong>Helping a parent or loved one?</strong> Choosing or changing a plan for someone in a facility can feel overwhelming. We walk through eligibility, what an I-SNP covers, and how it compares with other options &mdash; including <a href="/medicaid">Minnesota Senior Health Options</a> if Medical Assistance is paying for the care &mdash; patiently, and at no cost.</p></div>
<p>Related: <a href="/chronic-snp">Chronic SNPs (C-SNPs)</a> and <a href="/medicaid">MSHO</a> for people with both Medicare and Medical Assistance.</p>""",
     faqs=[("Who qualifies for an Institutional SNP?", "Generally, people with Medicare who live in (or are expected to need, for 90+ days) a qualifying institutional setting such as a nursing facility, or who need an institutional level of care at home, as determined by an approved assessment."),
           ("Can someone living at home join an I-SNP?", "Sometimes. Certain I-SNPs (institutional-equivalent plans) serve people who need a facility level of care but live at home. Availability depends on the plans offered in your Minnesota county."),
           ("Can you help a family member enroll?", "Yes. We regularly help adult children and caregivers understand the options for a parent or loved one, including how an I-SNP or MSHO coordinates with a facility.")],
     sources=[SRC_MA_GOV, SRC_MSHO], cta="Let&rsquo;s talk through care options for a facility setting.", about="Institutional Special Needs Plans", priority="0.6"),

# ---------------------------------------------------------------- Retirement guide
dict(slug="retirement-guide", nav_title="Retire With Confidence — free 295-page retirement guide", crumb="Free Retirement Guide", scene="northwoods",
     title="Retire With Confidence: Free 2026 Retirement Guide | ECOS Medicare Solutions",
     desc="Retire With Confidence: a free 295-page 2026 guide to Medicare, Social Security and the money decisions of retirement, by a licensed Minnesota agent. Emailed free.",
     llm="Medicare, Social Security, and the money decisions that decide your retirement. Free 295-page 2026 guide, emailed on request by a licensed Minnesota agent",
     eyebrow="Free 295-page guide · 2026 Edition", h1="Retire With Confidence",
     sub="Medicare, Social Security, and the money decisions that decide your retirement &mdash; the ones that come at you between 62 and 75, most with deadlines, several expensive to get wrong in ways nobody tells you about until later. It is free, and there is nothing to buy at the end of it.",
     form_title="Where should we send it?",
     keyfacts=["Forty-seven chapters in six parts: Medicare fundamentals, IRMAA and the income traps, Social Security claiming, retirement income, long-term care and final expense, and a 2026 quick-reference section.",
               "Written by Darin Weidauer, gerontologist, Registered Social Security Analyst and retired Air Force officer &mdash; the licensed agent behind this site.",
               "Emailed on request. Nothing downloads from this page, nothing is for sale, and a phone call is optional."],
     body="""<h2>What&rsquo;s in it: forty-seven chapters, six parts</h2>
<div class="grid grid--3" style="margin:1.4rem 0 2rem">
<article class="card"><h3>Medicare: your foundation</h3><p>The four parts, the seven-month enrollment window, what Medicare covers and the gaps it leaves, Original Medicare against Medicare Advantage, Medigap, and Part D.</p></article>
<article class="card"><h3>IRMAA and the income traps</h3><p>The surcharge nobody warns you about, the late-enrollment penalties that never end, and how selling a house or a cabin, or converting an IRA, can raise your Medicare premium two years later.</p></article>
<article class="card"><h3>Social Security</h3><p>How the benefit is calculated, claiming at 62 against 67 against 70, spousal and survivor benefits, the earnings test, and how much of it is taxed.</p></article>
<article class="card"><h3>Retirement income planning</h3><p>Building the income stack, the tax difference between a 401(k), an IRA and a Roth, life insurance in retirement, and where you live changing what you keep.</p></article>
<article class="card"><h3>Protecting what you have built</h3><p>Long-term care and the hybrid policies that return your money, where you will live, caring for aging parents, and final expense planning.</p></article>
<article class="card"><h3>Future-proofing &amp; reference</h3><p>The annual Medicare review, the decision timeline from 59&frac12; to 75+, a glossary of 60+ terms, a 2026 quick-reference card, and what changed for 2026.</p></article>
</div>
<h2>Who wrote it</h2>
<p>Darin Weidauer &mdash; gerontologist, 22-year U.S. Air Force veteran, independent insurance agent licensed in Minnesota, and Registered Social Security Analyst. He is the licensed agent behind this site, and he is independent &mdash; appointed with a number of carriers rather than employed by one. That is worth knowing before you read anything he has written about insurance.</p>
<p>Why give it away? The rest of this site answers a narrow question: what Medicare plans are available where you live in Minnesota. The book answers the wider one &mdash; the decisions that arrive between 62 and 75.</p>
<div class="note-box"><p>The guide is educational &mdash; it is not a quote, an offer of coverage, or a recommendation to buy, drop or change any policy. Use the form at the top of the page and it will be in your inbox within a few minutes; check your spam folder if not.</p></div>""",
     faqs=[("Is the guide really free?", "Yes. It is emailed to you at no cost, with nothing to buy and no obligation. A licensed agent will call only if you ask for a call on the form."),
           ("Is it specific to Minnesota?", "The book covers Medicare and retirement decisions nationally. For Minnesota specifics &mdash; Basic and Extended Basic supplements, Cost plans, MSHO &mdash; use the guides on this site alongside it."),
           ("Will I be added to a mailing list?", "You will receive the guide and, if you asked for a call, a call. You can opt out of any further contact at any time by replying or telling us.")],
     sources=[], cta="Get Retire With Confidence, free.", about="Retirement planning, Medicare and Social Security", schema_type="WebPage", priority="0.7"),
]

FAQ_PAGE = [
    ("How much does it cost to work with ECOS Medicare Solutions?", "Nothing. Independent Medicare agents are paid by the insurance carriers when you enroll, so comparing plans, answering questions and reviewing your coverage each year is free to you. Your premium is the same whether you enroll through us, another agent or the carrier directly."),
    ("Does Minnesota have Medigap Plan G or Plan N?", "No. Minnesota standardizes Medicare supplements its own way: a Basic plan and an Extended Basic plan, with optional riders on Basic. Basic plus the Part A deductible and excess-charge riders is the closest thing to a federal Plan G. See our Medicare supplement page."),
    ("Are Medicare Cost plans still sold in Minnesota?", "Yes, in 21 counties for [[YEAR]]: Aitkin, Carlton, Cook, Goodhue, Itasca, Kanabec, Koochiching, Lake, Le Sueur, McLeod, Meeker, Mille Lacs, Pine, Pipestone, Rice, Rock, St. Louis, Sibley, Stevens, Traverse and Yellow Medicine. They are sold by Blue Cross Blue Shield of Minnesota and Medica, and they ended in the Twin Cities metro in 2019."),
    ("What is the new Minnesota Medigap rule that started in August 2026?", "People aged 65 to 70 can buy a Medicare supplement during the Annual Election Period (October 15 to December 7), one time, without medical underwriting. Insurers may charge a surcharge over the standard premium, starting at 15% for 2026 and rising 5 points a year to a maximum of 35%, for the life of the policy."),
    ("My Medicare Advantage plan was discontinued. What now?", "You get a Special Enrollment Period to choose a new plan and, because you lost coverage through no fault of your own, generally a guaranteed-issue right to buy a Minnesota Basic or Extended Basic supplement without health questions, usually within 63 days of the coverage ending. Call before the deadline on your notice."),
    ("Which Minnesota plan works when I winter in Arizona or Florida?", "A Minnesota supplement with Original Medicare works anywhere in the U.S. A Cost plan covers you out of area through Original Medicare. Most Medicare Advantage HMOs cover only emergencies out of area; some PPOs and travel benefits go further. See our snowbird guide."),
    ("Does Mayo Clinic take Medicare Advantage?", "Mayo Clinic accepts Original Medicare, and therefore every supplement and Cost plan. It contracts with some Medicare Advantage plans and not others, and the list changes yearly. If Mayo is your care, we confirm the plan&rsquo;s Mayo status in writing before you enroll."),
    ("What is Minnesota Senior Health Options (MSHO)?", "A voluntary program for people 65+ who have Medicare Parts A and B and qualify for Medical Assistance. One health plan covers Medicare, Medical Assistance, Part D and long-term services with a care coordinator. It is Minnesota&rsquo;s version of a Dual Special Needs Plan."),
    ("When can I enroll in or change my Medicare plan in Minnesota?", "Your Initial Enrollment Period is the seven months around your 65th birthday. The Annual Election Period runs October 15 to December 7; Medicare Advantage Open Enrollment runs January 1 to March 31. Cost plans accept enrollment year-round where they are sold, and life events such as moving counties or losing a plan open Special Enrollment Periods."),
    ("What are the [[YEAR]] Medicare costs?", "Part B premium $202.90 a month, Part B deductible $283, Part A hospital deductible $1,736 per benefit period, Part D out-of-pocket cap $2,100. Higher earners pay IRMAA surcharges above $109,000 (single) or $218,000 (joint) of 2024 income. Our costs page has the full chart and calculators."),
    ("Can Minnesota help pay my Part B premium?", "Possibly. Minnesota&rsquo;s Medicare Savings Programs (QMB, SLMB, QI) pay the Part B premium for people with limited income, and Minnesota&rsquo;s asset limits ($10,000 single, $18,000 married) are higher than most states&rsquo;. Apply through your county human services office, or call Minnesota Aging Pathways at 800-333-2433."),
    ("Where can I get free, unbiased Medicare counseling in Minnesota?", "Minnesota Aging Pathways, formerly the Senior LinkAge Line, is Minnesota&rsquo;s State Health Insurance Assistance Program: 800-333-2433, Monday to Friday. You can also call 1-800-MEDICARE or use Medicare.gov. We are an independent agency, not a government program, and we say so on every page."),
    ("Do you offer every plan available in my area?", "No. We represent a number of insurance organizations and products in Minnesota, not all of them, and we will always say so. For the complete list, use Medicare.gov, 1-800-MEDICARE or Minnesota Aging Pathways. For help choosing among the plans we do offer, call [[PHONE]]."),
    ("Do you meet in person?", "We work with Minnesotans statewide by phone and video, which is how most people prefer it. Our sister agency has walk-in offices in Mesa and Sun City, Arizona, for snowbirds."),
]

ABOUT_BODY = """<div class="author" style="margin-bottom:2rem">
<img class="author__photo" src="/darin.jpg" width="600" height="600" alt="Darin Weidauer, independent Medicare insurance agent and credentialed gerontologist" loading="lazy" decoding="async">
<div>
<ul class="creds"><li>NPN 18580338 · licensed in Minnesota</li><li>Credentialed gerontologist (2014)</li><li>Registered Social Security Analyst&reg;</li><li>MBA, Pepperdine</li><li>Master&rsquo;s in Long-Term Care, USC</li><li>22-yr USAF veteran (retired officer)</li></ul>
<p>Darin Weidauer is an independent Medicare insurance agent, credentialed gerontologist, and Registered Social Security Analyst&reg; who helps Minnesota retirees and people approaching 65 make sense of their Medicare options &mdash; clearly, patiently, and with no cost to them.</p>
</div></div>
<h2>Background</h2>
<p>A 22-year U.S. Air Force veteran who retired as an officer, Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine University and a Master&rsquo;s in Long-Term Care from the University of Southern California&rsquo;s Leonard Davis School of Gerontology, where he became a credentialed gerontologist in 2014 &mdash; studying the human side of aging, not just the paperwork.</p>
<p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education: one-on-one reviews, no-cost community workshops, the free 295-page guide <a href="/retirement-guide"><em>Retire With Confidence</em></a>, and the pages on this site, every one of which he wrote or reviewed. He is also the founder of MyECOS360, an agency operating system for independent insurance agents, and the author of its training on <a href="https://www.myecos360.com/insurance-lead-economics">insurance lead economics</a>.</p>
<h2>How he is paid, and what that means for you</h2>
<p>ECOS Medicare Solutions is an independent agency: appointed with a number of Medicare Advantage, Cost plan, supplement and Part D carriers in Minnesota, employed by none of them. When you enroll in a plan through us, the carrier pays us a commission. That commission comes out of the carrier&rsquo;s filed rate &mdash; it is never added to your premium. You pay the same whether you enroll through us, through another agent, or directly with the insurer; going direct does not make a policy cheaper, and using us does not make it dearer.</p>
<p>We do not represent every plan sold in Minnesota, and we say so on every page. For a complete list, use Medicare.gov, 1-800-MEDICARE, or Minnesota Aging Pathways (800-333-2433), the state&rsquo;s free and independent counseling program.</p>
<h2>Licensing</h2>
<p>Darin is a licensed insurance agent in Minnesota and fourteen other states &mdash; Arizona, California, Colorado, Florida, Georgia, Nevada, New Mexico, North Carolina, Ohio, South Carolina, Tennessee, Texas, Utah and Washington &mdash; under National Producer Number 18580338, which you can verify with the Minnesota Department of Commerce or the NIPR. The multi-state licence is what lets us follow Minnesota <a href="/snowbirds">snowbirds</a> to Arizona, Florida and Texas.</p>
<h2>Where else you will find him</h2>
<ul>
<li><a href="https://www.myecos360.com/darin-weidauer" rel="noopener">Author page at MyECOS360</a> &mdash; the canonical profile</li>
<li><a href="https://www.linkedin.com/in/darin-weidauer-3165a816b/" rel="noopener">LinkedIn</a> and <a href="https://www.youtube.com/channel/UCD1XkkknhQ3UT-8AteYD3vQ" rel="noopener">YouTube</a></li>
<li>Sister sites: <a href="https://www.medicareenrollmentarizona.com" rel="noopener">Medicare Enrollment Arizona</a>, <a href="https://georgiamedicareenrollment.com" rel="noopener">Georgia Medicare Enrollment</a>, and <a href="https://www.mymedigaprate.com" rel="noopener">MyMedigapRate</a>, where Medigap rate filings &mdash; Minnesota&rsquo;s included &mdash; are published filing by filing.</li>
</ul>
<h2>How to reach him</h2>
<p>Call <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>, email <a href="mailto:[[EMAIL]]">[[EMAIL]]</a>, or use the form at the top of this page. We work with Minnesotans statewide by phone and video.</p>
"""

PRIVACY_BODY = """<p style="color:var(--ink-soft)"><em>Last updated: September 3, 2026. This policy is provided as a starting template and should be reviewed by your attorney before launch.</em></p>
<p>This Privacy Policy explains how ECOS Medicare Solutions ("we," "us") handles information collected through Minnesotamedicareenrollment.com (the "Site").</p>
<h2>Information we collect</h2>
<p>When you submit a form on the Site, we collect the information you provide: your name, phone number, email address, ZIP code or city, the topic you select, and a record of the consent you give (including the consent language shown and a date/time stamp). We do not ask for, and ask you not to send, health information through the form.</p>
<h2>How we use it</h2>
<p>We use your information to contact you about Medicare plan options and to provide the help you requested &mdash; by phone call, text message and email, consistent with the consent you provide. A licensed insurance agent may contact you. We do not sell your personal information.</p>
<h2>How your form is processed</h2>
<p>Our forms are delivered through a third-party form-processing service (Web3Forms), which transmits your submission to us. The Site loads web fonts from Google Fonts. We aim to limit data sharing to what is needed to operate the Site and respond to you.</p>
<h2>Analytics</h2>
<p>When enabled, we use Google Analytics to understand how visitors find and use this Site &mdash; which pages are read, and whether people call or submit a form. Google Analytics sets cookies and receives your IP address, device and browser type, and the pages you view. We use it in aggregate to improve the Site.</p><p>We do not send Google Analytics your name, phone number, email address or any information you type into a form. You can opt out across all sites using Google&rsquo;s <a href="https://tools.google.com/dlpage/gaoptout" rel="nofollow noopener" target="_blank">browser opt-out add-on</a>, or by using your browser&rsquo;s cookie controls.</p>
<h2>Your choices</h2>
<p>You can opt out of further contact at any time by telling us, replying STOP to texts, or unsubscribing from emails. To request that we delete your information, contact us using the details below. Minnesota residents may also have rights under the Minnesota Consumer Data Privacy Act; contact us to exercise them.</p>
<h2>Data security</h2>
<p>We take reasonable measures to protect the information you share, but no method of transmission over the internet is completely secure.</p>
<h2>Children</h2>
<p>The Site is intended for adults making Medicare decisions and is not directed to children under 13.</p>
<h2>Contact us</h2>
<p>Questions about this policy? Call <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>, email <a href="mailto:[[EMAIL]]">[[EMAIL]]</a>, or use the form on our <a href="/">home page</a>.</p>
<p style="font-size:.85rem;color:var(--ink-soft)">ECOS Medicare Solutions is not connected with or endorsed by the U.S. government or the federal Medicare program. This is a solicitation for insurance.</p>
"""

TERMS_BODY = """<p style="color:var(--ink-soft)"><em>Last updated: September 3, 2026. This document is provided as a starting template and should be reviewed by your attorney before launch.</em></p>
<p>By using Minnesotamedicareenrollment.com (the "Site"), operated by ECOS Medicare Solutions, you agree to these Terms of Use.</p>
<h2>Informational purpose</h2>
<p>The Site provides general information about Medicare to help you make decisions. It is not legal, tax or medical advice, and it is not a substitute for the official Medicare program or for Minnesota&rsquo;s free counseling program, Minnesota Aging Pathways. Medicare plan availability, costs and rules change and vary by county.</p>
<h2>Insurance offered through a licensed agent</h2>
<p>Insurance products referenced on the Site are offered through a licensed insurance agent (Darin Weidauer, NPN 18580338, licensed in Minnesota). Enrollment is subject to plan terms and eligibility. We do not offer every plan available in your area.</p>
<h2>No guarantee of accuracy</h2>
<p>We work to keep figures current and cite the year and source, but we do not warrant that all information is complete, current or error-free. Always confirm details with the official sources noted on the Site.</p>
<h2>External links</h2>
<p>The Site links to third-party websites (such as Medicare.gov and mn.gov) and to other sites operated by ECOS Medicare Solutions. We are not responsible for the content or practices of third-party sites.</p>
<h2>Limitation of liability</h2>
<p>To the fullest extent permitted by law, ECOS Medicare Solutions is not liable for any damages arising from your use of the Site.</p>
<h2>Governing law</h2>
<p>These Terms are governed by the laws of the State of Minnesota.</p>
<h2>Contact us</h2>
<p>Questions? Call <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a> or use the form on our <a href="/">home page</a>.</p>
<p style="font-size:.85rem;color:var(--ink-soft)">ECOS Medicare Solutions is not connected with or endorsed by the U.S. government or the federal Medicare program. This is a solicitation for insurance.</p>
"""
