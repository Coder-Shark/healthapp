from bs4 import BeautifulSoup
import requests



disease = input("first aid for what....")

if disease == "cut" or disease == "scratch":
    aid = """Cut/Scrape: If there is bleeding, press firmly over the site with a clean cloth until it stops, anywhere from three to 15 minutes. Clean with lukewarm running water and gently pat dry. If the skin is broken, apply a thin layer of antibiotic ointment, then cover with a bandage or gauze and adhesive tape. If you can't control the bleeding after several attempts with direct pressure, call your pediatrician or head to an Emergency Room. Continue utilize antibiotic ointment and apply a new bandage daily (or more often if necessary) until the cut heals. If the wound appears to be forming or draining pus or becomes swollen, tender, or red, see a doctor right away to treat the infection."""
    print(aid)

elif disease == "burn":
    aid = """Burn: Immediately hold injury under cold running water or apply a cold, wet towel until the pain subsides. Cover any small blisters with a loose bandage or gauze and tape. Call a doctor as soon as possible if burns are on the face, hands, or genitals, or if they're larger than 1/4 inch anywhere on the body. If the injury looks rooted, go to the Emergency Room. For a burn covering a tenth of the body or more, don't use cold compresses; call 911 and cover up with a clean sheet or a blanket to prevent hypothermia until help arrives. DO NOT pop any blisters yourself. If the skin breaks, apply antibiotic cream and cover the area with a bandage or gauze until it's healed. Watch for any redness, swelling, tenderness, or discharge for these are all signs of infection."""
    print(aid)

elif disease == "insect bite" or disease == "sting":
    aid = """Insect Bite/Sting: If the insect left a stinger, gently scrape the skin with your fingernail to remove it without breaking it. Refrain from using tweezers because that can squeeze more venom out of the stinger, causing further injury. Call 911 if you have trouble breathing, coughing, or develop a hoarse voice, hives, or swollen lips or tongue. To combat itching, apply 1% hydrocortisone cream or a topical antihistamine if the skin isn't broken or scabbed. Contact your doctor if you suspect a tick bite. They may want to test for Lyme disease and other tick-borne diseases."""
    print(aid)

elif disease == "splinter":
    aid = """Use soap and water to wash around the splinter. Clean a pair of tweezers with rubbing alcohol and slowly pull the splinter out. Rewash the skin. If you come across a fragment that is hard to remove, leave it for a day or so to see if it will come out on its own."""
    print(aid)

elif disease == "sunburn":
    aid = """If you feel dizzy, weak, sick to your stomach, or are spiking a high fever—or if the burn is severe (oozing blisters form within 48 hours) and covering a significant portion of your body—go to the Emergency Room. If your only symptoms are discomfort and redness, apply cold compresses and aloe vera lotion and take some ibuprofen. Avoid creams with petroleum, which can cause infection, or anything ending in -Caine. When not administered by a professional, these drugs may be dangerous. """
    print(aid)

elif disease == "nosebleed":
    aid = """Sit upright and don't tilt your head back. Loosen any tight clothing around your neck. Pinch the lower end of the nose close to the nostrils and lean forward while you apply constant pressure for five to ten minutes. Don't release and check the nose; it could prolong the bleeding. If the nosebleed is the result of trauma, you can reduce swelling by holding an ice pack against the bridge of the nose after the bleeding slows down. If it persists for more than ten minutes or returns later, call your doctor or go to the Emergency Room to check for breakage."""
    print(aid)

elif disease == "fractures":
    aid = """Fractures are broken bones, and they can occur as a result of falls or other harsh impacts. When this happens, the affected part should be immobilized, and additional manipulation of the affected area should be avoided. Remember that a fracture could sever a blood vessel or a nerve if it is not immobilized, resulting in a much more severe injury. Immobilize the injured part, and transport the patient to the nearest hospital or medical clinic as soon as possible."""
    print(aid)

elif disease == "drowning":
    aid = """If someone is in difficulty in water, don't enter the water to help unless it's absolutely essential.Once the person is on land, if they're not breathing, open the airway and give five initial rescue breaths before starting CPR. If you're alone, perform CPR for one minute before calling for emergency help.Find out how to give CPR, including rescue breaths.If the person is unconscious but still breathing, put them into the recovery position with their head lower than their body and call an ambulance immediately.Continue to observe the casualty to ensure they don't stop breathing or that their airway becomes obstructed."""
    print(aid)

elif disease == "shock":
    aid = """If someone has had an electric shock, switch off the electrical current at the mains to break the contact between the person and the electrical supply.don't go near or touch the person until you're sure the electrical supply has been switched off .once the power supply has been switched off, and if the person isn't breathing, dial 999 or 112 for an ambulance"""
    print(aid)

elif disease == "heart attack":
    aid = """If you think a person is having, or has had, a heart attack, sit them down and make them as comfortable as possible, and call 999 or 112 for an ambulance.If they're conscious, reassure them and ask them to take a 300mg aspirin tablet to chew slowly (unless you know they shouldn't take aspirin – for example, if they're under 16 or allergic to it).If the person has any medication for angina, such as a spray or tablets, help them to take it. Monitor their vital signs, such as breathing, until help arrives.If the person deteriorates and becomes unconscious, open their airway, check their breathing and, if necessary, start CPR. Re-alert the emergency services that the casualty is now in cardiac arrest."""
    print(aid)

elif disease == "poisoning":
    aid = """Find out what's been swallowed, so you can tell the paramedic or doctor.Do not give the person anything to eat or drink unless a healthcare professional advises you to.Do not try to cause vomiting.Stay with the person, because their condition may get worse and they could become unconscious.Don't leave them if they're unconscious because they may roll onto their back, which could cause them to vomit. The vomit could then enter their lungs and make them choke."""
    print(aid)

elif disease == "stroke":
    aid = """The FAST guide is the most important thing to remember when dealing with people who have had a stroke. The earlier they receive treatment, the better. Call for emergency medical help straight away.Facial weakness – is the person unable to smile evenly, or are their eyes or mouth droopy?Speech problems – is the person unable to speak clearly or understand you?
    Time to call 999 or 112 – for emergency help if a person has any of these symptoms"""
    print(aid)
