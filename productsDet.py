from selenium import webdriver
import json
import pickle
from datetime import datetime
from bs4 import BeautifulSoup


driver = webdriver.Chrome('/Users/prasunsarkar/Downloads/chromedrivers')
driver.get("https://aliexpress.com")
cookies = pickle.load(open("cookies.pickle", "rb"))
myArray = ['http://www.aliexpress.com/store/product/Retail-Brand-1-piece-2014-New-Children-s-T-shirt-boys-Tees-Baby-Boy-Clothing-Litle/328777_1635459653.html?sdom=708.123488.111136.0_1635459653', 'http://www.aliexpress.com/store/product/Tri-Poseidon-Brand-Super-Strong-Japan-300m-Multifilament-PE-Braided-Fishing-Line-8-10-20-30/1166220_1692983177.html?sdom=706.123486.111132.0_1692983177', 'http://www.aliexpress.com/store/product/Free-shipping-High-quality-Aluminum-alloy-fishing-line-knotter-Fishing-Hook-Tie-Device-sub-line-tier/1160197_1922205515.html?sdom=706.123486.111132.0_1922205515', 'http://www.aliexpress.com/store/product/2014-R0CKBROS-Tour-de-France-Cycling-Wind-Coat-9-Colors-New/434036_1659437086.html?sdom=706.123486.111132.0_1659437086', 'http://www.aliexpress.com/store/product/Anglers-Choice-Brand-Super-Strong-Japanese-500m-Multifilament-PE-Material-Braided-Fishing-Line-10-20-30/836453_32287525713.html?sdom=706.123486.111132.0_32287525713', 'http://www.aliexpress.com/store/product/54-11CM-Cute-Baby-Kids-Animal-Rabbit-Sleeping-Comfort-Doll-Plush-Toy/1160413_32223165576.html?sdom=708.123488.111136.0_32223165576', 'http://www.aliexpress.com/store/product/Promotion-Casual-Wallets-For-Men-New-Design-Genuine-Leather-Top-Purse-Men-Wallet-With-Coin-Bag/1037875_1594562260.html?sdom=704.123484.111128.0_1594562260', 'http://www.aliexpress.com/store/product/EU-US-Plug-New-RGB-3W-Crystal-Magic-Ball-Laser-Stage-Lighting-For-Party-Disco-DJ/1212310_1950091225.html?sdom=709.123489.111138.0_1950091225', 'http://www.aliexpress.com/store/product/Genuine-Clear-Austrian-Crystal-Jewelry-Set-Women-Jewelry-Set-Necklace-Earrings-Jewelry-Set-Wedding-Party-Accessories/1167544_32221609176.html?sdom=703.123483.111126.0_32221609176', 'http://www.aliexpress.com/store/product/creative-vegetable-slicer-kitchen-gadets/1088854_32318636449.html?sdom=709.123489.111138.0_32318636449', 'http://www.aliexpress.com/store/product/Bamoer-High-Quality-18K-Gold-Plated-Finger-Ring-for-Women-Party-with-AAA-Colorful-Cubic-Zircon/107430_32242377008.html?sdom=703.123483.111126.0_32242377008', 'http://www.aliexpress.com/store/product/1Pcs-Cheap-price-digital-bite-alarm-bite-indicator-banding-on-the-fishing-rod/912949_32262302041.html?sdom=706.123486.111132.0_32262302041', 'http://www.aliexpress.com/store/product/2013-summer-new-arrival-flower-princess-girl-dress-lace-rose-Party-Wedding-Birthday-girls-dresses-Candy/520529_1452219697.html?sdom=708.123488.111136.0_1452219697', 'http://www.aliexpress.com/store/product/Baby-Washable-Reusable-Real-Cloth-Pocket-Nappy-Cover-Wrap-suits-Birth-to-Potty-diaper-cover/1555157_32270975835.html?sdom=708.123488.111136.0_32270975835', 'http://www.aliexpress.com/store/product/2014-summer-running-shoes-male-sport-lazy-network-shoes-men-foot-wrapping-breathable-shoes-free-shipping/1167085_1879139799.html?sdom=704.123484.111128.0_1879139799', 'http://www.aliexpress.com/store/product/flying-butterfly-free-shipping-children-s-room-mirror-wall-sticker-home-decoration-12-pcs-lot-plastic/1581068_32310083954.html?sdom=709.123489.111138.0_32310083954', 'http://www.aliexpress.com/store/product/Retail-2015-New-Girls-Clothing-Sets-Baby-Kids-Clothes-Children-Clothing-Full-Sleeve-T-Shirt-Leopard/1484159_32260679205.html?sdom=708.123488.111136.0_32260679205', 'http://www.aliexpress.com/store/product/New-Candy-Double-Color-ARMOR-Soft-TPU-Silicone-Hybrid-Back-Case-For-iphone-6-Shockproof-Cell/511261_2035992897.html?sdom=705.123485.111130.0_2035992897', 'http://www.aliexpress.com/store/product/Luxury-Fashion-Flip-leather-case-for-apple-Ipad-mini-Multifunctional-protective-Smart-stand-holder-Magnetic-Official/809578_1064632901.html?sdom=705.123485.111130.0_1064632901', 'http://www.aliexpress.com/store/product/Luxury-Bling-Diamond-Crystal-Shiny-Glitter-Flip-Matte-Case-for-iphone-6-Plus-5-5-PU/117073_32245366444.html?sdom=705.123485.111130.0_32245366444', 'http://www.aliexpress.com/store/product/new-For-apple-ipad-2-3-4-ipad2-ipad3-case-table-Smart-Cover-Slim-Magnetic-PU/539712_2037755433.html?sdom=705.123485.111130.0_2037755433', 'http://www.aliexpress.com/store/product/Weight-Lifting-Fitness-Anti-Slip-Gym-Exercise-Body-Building-Training-Workout-Sports-Half-Finger-Gloves/1728291_32294554994.html?sdom=706.123486.111132.0_32294554994', 'http://www.aliexpress.com/store/product/2-30-Months-Breathable-Multifunctional-Front-Facing-Baby-Carrier-Infant-Comfortable-Sling-Backpack-Pouch-Wrap-Baby/103692_32219805277.html?sdom=708.123488.111136.0_32219805277', 'http://www.aliexpress.com/store/product/wholesale-2014-hot-brand-fitted-hat-baseball-cap-Casual-Outdoor-sports-snapback-hats-cap-for-men/628222_32243608596.html?sdom=703.123483.111126.0_32243608596', 'http://www.aliexpress.com/store/product/Summer-Women-Dress-Vestidos-Casual-Clothing-Female-Tropical-Bohemian-Mini-Dress-Beach-Vestidos-De-Renda-Ladies/620009_32282871144.html?sdom=703.123483.111126.0_32282871144', 'http://www.aliexpress.com/store/product/5m-300-LED-SMD3528-non-waterproof-SMD-12V-flexible-light-60-led-m-6-color-LED/1050707_1798828013.html?sdom=709.123489.111138.0_1798828013', 'http://www.aliexpress.com/store/product/VINTAGE-STEAMPUNK-Sunglasses-round-Designer-steam-punk-Metal-OCULOS-de-sol-women-COATING-SUNGLASSES-Men-Retro/1229218_32219828796.html?sdom=703.123483.111126.0_32219828796', 'http://www.aliexpress.com/store/product/Quality-Vintage-Round-Sunglasses-Women-s-Glasses-Shade-Accessories-Free-Shipping/1131150_1673198879.html?sdom=704.123484.111128.0_1673198879', 'http://www.aliexpress.com/store/product/Ultra-Thin-Flexible-Clear-Case-For-Iphone-6-Plus-5-5inch-Soft-Cover-Highly-Transparent-Back/500640_32237203163.html?sdom=705.123485.111130.0_32237203163', 'http://www.aliexpress.com/store/product/Free-dropshipping-Plus-Case-New-Fashion-Flexible-Polarized-Lens-Sunglasses-Brand-Designer-Men-Fishing-Glasses/931552_1540046144.html?sdom=704.123484.111128.0_1540046144', 'http://www.aliexpress.com/store/product/Beauty-Gifts-Zirconia-kitchen-Ceramic-fruit-Knife-Set-Kit-3-4-5-6-inch-with-Blue/635348_1701393883.html?sdom=709.123489.111138.0_1701393883', 'http://www.aliexpress.com/store/product/Hot-sale-best-sell-super-stretch-super-women-hot-shapers-Control-Panties-pant-stretch-neoprene-slimming/731023_32312827679.html?sdom=703.123483.111126.0_32312827679', 'http://www.aliexpress.com/store/product/2015-Hot-NOS-Men-Canvas-Outdoor-Belt-Military-Equipment-Cinturon-Western-Strap-Men-s-Belts-Luxury/1047504_1941745001.html?sdom=704.123484.111128.0_1941745001', 'http://www.aliexpress.com/store/product/Free-shipping-XC8866-29X19cm-4-color-Mini-Water-Drawing-Mat-Aquadoodle-Mat-1-Magic-Pen-Water/432143_1655146871.html?sdom=708.123488.111136.0_1655146871', 'http://www.aliexpress.com/store/product/Free-Shipping-Popular-Ancient-Lamp-Cats-and-Birds-Wall-Sticker-Wall-Mural-Home-Decor-Room-Kids/830136_1338870980.html?sdom=709.123489.111138.0_1338870980', 'http://www.aliexpress.com/store/product/500M-Tri-Poseidon-Brand-Super-Strong-Japan-Multifilament-PE-Braided-Fishing-Line-8-10-20-30/1166220_1688306296.html?sdom=706.123486.111132.0_1688306296', 'http://www.aliexpress.com/store/product/1pc-High-Quality-Fishing-lure-5-8-14-73cm-0-435oz-12-35g-Fishaing-bait-6/901667_32239607051.html?sdom=706.123486.111132.0_32239607051', 'http://www.aliexpress.com/store/product/Free-Shipping-2013-New-Fashion-Baby-Girls-Boys-Hello-Kitty-Tshirt-Minnie-Cotton-Short-Sleeved-Casual/522511_1372610209.html?sdom=708.123488.111136.0_1372610209', 'http://www.aliexpress.com/store/product/Hot-RGB-led-strip-3528-flexible-strip-light-DC12V-5M-300led-24key-IR-remote-controller-power/1495502_32256513375.html?sdom=709.123489.111138.0_32256513375', 'http://www.aliexpress.com/store/product/Candy-Double-Color-ARMOR-Soft-TPU-Hybrid-Back-Case-For-iphone-6-Plus-Shockproof-Cell-Phone/511261_2039616184.html?sdom=705.123485.111130.0_2039616184', 'http://www.aliexpress.com/store/product/3-Pieces-lot-Fantasia-Carter-Baby-Bodysuit-Infant-Jumpsuit-Bebe-Overall-Short-Sleeve-Body-Suit-Baby/521899_1988072399.html?sdom=708.123488.111136.0_1988072399', 'http://www.aliexpress.com/store/product/2015-Fashion-Vintage-Spring-Summer-T-Shirt-Women-Clothing-Tops-Tshirt-Blouse-Animal-Print-T-shirt/114853_32290724057.html?sdom=703.123483.111126.0_32290724057', 'http://www.aliexpress.com/store/product/New-arrival-new-style-artifact-fishing-tool-fishing-net-wire-mesh-hook-free-shipping/116834_1917215533.html?sdom=706.123486.111132.0_1917215533', 'http://www.aliexpress.com/store/product/Free-shipping-DIY-Removable-Wall-Stickers-Cartoon-Cute-Animals-Train-Balloon-Kids-Bedroom-Home-Decor-Mural/1294978_32302493787.html?sdom=709.123489.111138.0_32302493787', 'http://www.aliexpress.com/store/product/Hot-sale-Red-Wine-Cup-Liquid-Transparent-Case-Cover-For-Apple-iPhone-4-4S-5-5S/1304703_32312759573.html?sdom=705.123485.111130.0_32312759573', 'http://www.aliexpress.com/store/product/New-Genuine-Cow-Leather-Baby-Moccasins-Soft-Moccs-Baby-BOW-Shoes-girls-Newborn-Baby-first-walker/1721299_32292571651.html?sdom=708.123488.111136.0_32292571651', 'http://www.aliexpress.com/store/product/CREE-XM-L-XML-T6-LED-1600-Lumens-zoom-Rechargeable-Headlight-LED-Headlamp-CREE-2-x/711739_919845700.html?sdom=709.123489.111138.0_919845700', 'http://www.aliexpress.com/store/product/Fashion-Bracelet-Wholesale-Free-Shipping-VB284/401168_1101450963.html?sdom=704.123484.111128.0_1101450963', 'http://www.aliexpress.com/store/product/2014-new-Verus-Armor-Cases-for-iphone-6-4-7-Card-Slider-Case-with-Card-Storage/230898_32274891058.html?sdom=705.123485.111130.0_32274891058', 'http://www.aliexpress.com/store/product/Free-Shipping-White-Sexy-Pajamas-Lingerie-Lace-Costumes-Bra-Underwear-Clothes-For-Barbie-Doll-Clothes-Hot/1657178_32282054243.html?sdom=708.123488.111136.0_32282054243', 'http://www.aliexpress.com/store/product/Hot-sale-For-iPad-Air-Smart-Case-Cover-Stand-Tablet-Designer-Leather-Cover-For-Apple-iPad/124371_1766586681.html?sdom=705.123485.111130.0_1766586681', 'http://www.aliexpress.com/store/product/Trendy-Indian-Jewelry-Set-Wedding-Accessories-Gold-Silver-Earrings-Pearl-Jewelry-Set-Women-Necklace-Set-SET140024/636066_2019249994.html?sdom=703.123483.111126.0_2019249994', 'http://www.aliexpress.com/store/product/2014-summer-top-short-sleeve-fashion-men-plus-size-t-shirt-or-women-t-shirt-round/1626095_32303326534.html?sdom=704.123484.111128.0_32303326534', 'http://www.aliexpress.com/store/product/Free-Shipping-100-pcs-Green-Fishing-Trace-Lures-Braid-Nylon-fishing-line-Leader-Steel-Wire-Spinner/1303856_32235517648.html?sdom=706.123486.111132.0_32235517648', 'http://www.aliexpress.com/store/product/12pcs-3D-Butterfly-Wall-Stickers-Butterflies-Docors-Art-DIY-Decorations-Paper/1626856_32261078955.html?sdom=709.123489.111138.0_32261078955', 'http://www.aliexpress.com/store/product/New-Arrival-Fashionable-Wedding-Jewelry-Sets-Real-Rose-Gold-Plated-Women-Necklace-Earring-Sets-for-Women/508049_32213924221.html?sdom=703.123483.111126.0_32213924221', 'http://www.aliexpress.com/store/product/Fashion-casual-bag-male-backpack-school-bag-canvas-bag-male-backpack-male-package/219001_1007859333.html?sdom=704.123484.111128.0_1007859333', 'http://www.aliexpress.com/store/product/2015-European-and-American-boys-denim-clothing-sets-boys-handsome-short-sleeved-T-shirt-denim-jeans/927915_32297473767.html?sdom=708.123488.111136.0_32297473767', 'http://www.aliexpress.com/store/product/Free-shipping-wholesale-baseball-men-caps-leisure-snapback-outdoors-unisex-hats-sun-shading/430203_1505933332.html?sdom=703.123483.111126.0_1505933332', 'http://www.aliexpress.com/store/product/2015-New-Summer-girls-split-three-pieces-Swimwear-children-Cute-star-pattern-split-bikini-girls-swimsuit/226113_32317979982.html?sdom=706.123486.111132.0_32317979982', 'http://www.aliexpress.com/store/product/Business-Man-s-Small-Messenger-Bags-Polo-Men-s-Crossbody-Bags-Small-Desigual-Brand-Man-Satchels/1456214_32292116142.html?sdom=704.123484.111128.0_32292116142', 'http://www.aliexpress.com/store/product/Transparent-Fashion-Dynamic-Liquid-Glitter-Colorful-Paillette-Sand-Quicksand-Back-Case-Cover-For-iPhone-5-5S/1398337_2027803414.html?sdom=705.123485.111130.0_2027803414', 'http://www.aliexpress.com/store/product/New-2014-Fashion-Women-Belt-Brand-Designer-Hot-Ladies-Faux-Leather-Metal-Buckle-Straps-Girls-Fashion/602066_1761633635.html?sdom=703.123483.111126.0_1761633635', 'http://www.aliexpress.com/store/product/New-2015-Brand-Sport-Baseball-Cap-Man-Bone-Snapback-Cap-Baseball-caps-Chapeu-Simple-and-Stylish/1359864_32268022924.html?sdom=704.123484.111128.0_32268022924', 'http://www.aliexpress.com/store/product/10-colors-big-Hand-t-shirt-Man-men-clothes-Printing-Hot-3D-visual-creative-personality-spoof/1168434_1846297552.html?sdom=704.123484.111128.0_1846297552', 'http://www.aliexpress.com/store/product/Free-Shipping-Cup-Mold-Silicone-Mold-Cake-Tools-Cookie-Cutter-Ice-Molds-Cake-Mould-Bakeware-Tools/1381906_2021437001.html?sdom=709.123489.111138.0_2021437001', 'http://www.aliexpress.com/store/product/New-arrival-Free-shipping-gentlewoman-wallet-fashion-ladies-wallet-women-s-bowknot-purse-clutch-bags-5COLORS/1037875_1509249275.html?sdom=703.123483.111126.0_1509249275', 'http://www.aliexpress.com/store/product/High-quality-2015-spring-kids-leggings-for-girls-candy-colors-Children-stretch-baby-casual-cotton-pants/333199_32241441127.html?sdom=708.123488.111136.0_32241441127', 'http://www.aliexpress.com/store/product/2015-NEW-OTG-Smartphone-USB-Flash-Drive-Real-capacity-64G-USB2-0-Memory-Stick-8gb-16gb/346773_32273476216.html?sdom=705.123485.111130.0_32273476216', 'http://www.aliexpress.com/store/product/2015-New-Hight-Quality-fashion-tassle-women-messenger-Bags-women-shoulder-bag-pu-leather-woman-bag/1318317_32274606237.html?sdom=703.123483.111126.0_32274606237', 'http://www.aliexpress.com/store/product/High-quality-brand-Paring-Fruit-Utility-3-4-5-6-inch-peeler-Acrylic-Holder-Block-Chef/635348_32252483948.html?sdom=709.123489.111138.0_32252483948', 'http://www.aliexpress.com/store/product/free-shipping-computer-fan-case-cooling-fan-unit-fan-8025-8cm-with-LED-lights-chassis-fan/1358964_32243936360.html?sdom=705.123485.111130.0_32243936360', 'http://www.aliexpress.com/store/product/SeaKnight-2015-New-Quality-CM3000-4000-14BB-5-2-1-Metal-Spinning-Fishing-Reel-Carp-Fishing/1166220_32296344509.html?sdom=706.123486.111132.0_32296344509', 'http://www.aliexpress.com/store/product/2014-New-Fashion-Brand-Casual-Men-s-Long-T-shirt-Simple-fashion-Europe-style-Long-Tee/1361294_32215142339.html?sdom=704.123484.111128.0_32215142339', 'http://www.aliexpress.com/store/product/Brand-New-Polarized-Clip-On-Sunglasses-Driving-Night-Vision-Lens-Sun-Glasses-Anti-UVA-Anti-UVB/1710065_32284936934.html?sdom=706.123486.111132.0_32284936934', 'http://www.aliexpress.com/store/product/2015-New-Big-Boys-Quick-Dry-Shorts-Brand-Kids-Camo-Surf-Beach-Shorts-for-Boys-Trench/236550_32290834624.html?sdom=708.123488.111136.0_32290834624', 'http://www.aliexpress.com/store/product/4-Feet-High-Quality-Nylon-Dog-Pet-Leash-Lead-for-Daily-Walking/404009_1904029157.html?sdom=709.123489.111138.0_1904029157', 'http://www.aliexpress.com/store/product/Universal-LCD-Charger-EU-Plug-USB-Wall-Charger-for-Mobile-Phone-Battery-Power-Converter-with-Retail/701907_32216256792.html?sdom=705.123485.111130.0_32216256792', 'http://www.aliexpress.com/store/product/Free-shipping-wholesale-baseball-men-caps-leisure-snapback-outdoors-unisex-hats-sun-shading/430203_1505933332.html?sdom=704.123484.111128.0_1505933332', 'http://www.aliexpress.com/store/product/IP-68-Waterproof-Heavy-Duty-Hybrid-Swimming-Dive-Case-For-Apple-iPhone-6-4-7-inch/804544_32276245663.html?sdom=705.123485.111130.0_32276245663', 'http://www.aliexpress.com/store/product/1pcs-lot-Retail-Black-Luxury-Genuine-Leather-Case-for-iphone-6-4-7-Original-XD-Nobility/804544_2053087559.html?sdom=705.123485.111130.0_2053087559', 'http://www.aliexpress.com/store/product/FENNEY-100-natural-Pearl-earring-Pearl-with-925-Sterling-Silver-earrings-Birthday-gift-Jewelry-Women-Accessories/1470406_32215551211.html?sdom=703.123483.111126.0_32215551211', 'http://www.aliexpress.com/store/product/New-4-designs-ballons-baby-girl-balloon-milk-bottle-balon-baby-stroller-baloons-baby-foot-balao/1332761_2047951549.html?sdom=709.123489.111138.0_2047951549', 'http://www.aliexpress.com/store/product/Fishing-Lure-Crankbait-Hard-Bait-Fresh-Water-Deep-Water-Bass-Walleye-Crappie-C549-Fishing-Tackle-C549X18/812483_1125086882.html?sdom=706.123486.111132.0_1125086882', 'http://www.aliexpress.com/store/product/2015-Fashion-Baby-Girls-Kids-Children-Summer-My-Little-Pony-T-Shirt-Girl-s-3D-Printer/138048_32261778106.html?sdom=708.123488.111136.0_32261778106', 'http://www.aliexpress.com/store/product/Retail-2014-new-sleeveless-Waist-Chiffon-Dress-Girls-Toddler-3D-Flower-Tutu-Layered-Princess-Party-Bow/1495864_32227157080.html?sdom=708.123488.111136.0_32227157080', 'http://www.aliexpress.com/store/product/VINTAGE-STEAMPUNK-Sunglasses-round-Designer-steam-punk-Metal-OCULOS-de-sol-women-COATING-SUNGLASSES-Men-Retro/1229218_32219828796.html?sdom=704.123484.111128.0_32219828796', 'http://www.aliexpress.com/store/product/DL-Brand-Kinesiology-Kinesio-tape-5cmx5m-Free-Shipping-d-box-with-Usage-Manual-Mix-Colours-Available/112710_575656702.html?sdom=706.123486.111132.0_575656702', 'http://www.aliexpress.com/store/product/Men-s-Exclusive-Pretty-Tops-Deep-V-Neck-Long-Sleeve-T-Shirts-Stunning-Cut-Off-Border/823139_32269511638.html?sdom=704.123484.111128.0_32269511638', 'http://www.aliexpress.com/store/product/Latex-Waist-Trainer-Corset-100-Rubber-Waist-Corset-Chest-Binder-XS-Waist-Training-Corsets-Steel-Boned/1246873_32295633385.html?sdom=703.123483.111126.0_32295633385', 'http://www.aliexpress.com/store/product/2014-TOUR-DE-FRANCE-Breathable-Bike-Bicycle-Cycling-Cycle-Waterproof-Rain-Coat-Raincoat-Wind-Coat-Windcoat/434036_1692400245.html?sdom=706.123486.111132.0_1692400245', 'http://www.aliexpress.com/store/product/2015-New-Arrival-Men-Polarized-Sunlasses-Outdoor-Sport-Goggles-Men-s-Polarizing-Glasses-High-Quality-Lower/1383519_32322714104.html?sdom=704.123484.111128.0_32322714104', 'http://www.aliexpress.com/store/product/New-2014-Girls-Princess-Bow-Belt-dress-Circle-Bubble-Peacock-print-kids-Dress-girl-s-Party/530361_32218569250.html?sdom=708.123488.111136.0_32218569250', 'http://www.aliexpress.com/store/product/wholesale-2014-hot-brand-fitted-hat-baseball-cap-Casual-Outdoor-sports-snapback-hats-cap-for-men/628222_32243608596.html?sdom=704.123484.111128.0_32243608596', 'http://www.aliexpress.com/store/product/7-in-1-For-Samsung-Galaxy-Tab-2-10-1-inch-P5100-Tablet-PU-Leather-Case/630436_1886310477.html?sdom=705.123485.111130.0_1886310477', 'http://www.aliexpress.com/store/product/FINDKING-Brand-top-quality-Mother-day-gift-set-Zirconia-Ceramic-Knife-set-3-4-5-6/635348_32310650309.html?sdom=709.123489.111138.0_32310650309', 'http://www.aliexpress.com/store/product/Women-Beach-Dress-Sexy-Strap-Sheer-Floral-Lace-Embroidered-Crochet-Summer-Dresses-Hippie-Boho-vestidos-Mini/1523118_32303107531.html?sdom=703.123483.111126.0_32303107531', 'http://www.aliexpress.com/store/product/2014-IRON-MAN-3-Matsuda-RAY-TONY-Steampunk-Sunglasses-Men-Mirrored-Designer-Brand-Glasses-Vintage-Sports/817474_1666767360.html?sdom=704.123484.111128.0_1666767360', 'http://www.aliexpress.com/store/product/BABY-BODYSUITS-3PCS-100-Cotton-Infant-Body-Bebes-Short-Sleeve-Clothing-Similar-Carters-Jumpsuit-Printed-Baby/926047_32296213734.html?sdom=708.123488.111136.0_32296213734', 'http://www.aliexpress.com/store/product/Bandage-Rayon-Good-Elastic-Women-Skirts-Mini-Sexy-Slim-Pencil-Clubwear-Suitable-Casual-Formal-Clothing-HL135/400341_869560191.html?sdom=703.123483.111126.0_869560191', 'http://www.aliexpress.com/store/product/new-2014-men-s-messenger-bags-High-quality-canvas-multifunction-shoulder-bag-for-men-travel-business/1248176_1883909957.html?sdom=704.123484.111128.0_1883909957', 'http://www.aliexpress.com/store/product/High-quality-Guard-LCD-Clear-Front-Tempered-Glass-Screen-Protector-Film-For-iPhone-6-4-7/1079451_2045623452.html?sdom=705.123485.111130.0_2045623452', 'http://www.aliexpress.com/store/product/New-Arrival-for-Galaxy-S5-TPU-Soft-Case-S-LINE-Slim-Gel-Back-Cover-for-Samsung/809578_1722759971.html?sdom=705.123485.111130.0_1722759971', 'http://www.aliexpress.com/store/product/Multifunction-Waterproof-Digital-Backlight-Noctilucent-Bicycle-Computer-Odometer-Bike-Speedometer-Clock-Stopwatch/820165_1409844412.html?sdom=706.123486.111132.0_1409844412', 'http://www.aliexpress.com/store/product/Professional-Polarized-Cycling-Glasses-Bike-Casual-Goggles-Outdoor-Sports-Bicycle-Sunglasses-UV-400-With-5-Lens/410258_1820408823.html?sdom=706.123486.111132.0_1820408823', 'http://www.aliexpress.com/store/product/girl-pants-new-arrive-printing-Flower-girls-leggings-Toddler-Classic-Leggings-2-14Ybaby-girls-leggings-kids/333199_32241038992.html?sdom=708.123488.111136.0_32241038992', 'http://www.aliexpress.com/store/product/Elegant-Luxury-Crystal-Clear-Back-Slim-Silk-Leather-Case-For-ipad-mini-1-2-Retina-3/117073_32255369502.html?sdom=705.123485.111130.0_32255369502', 'http://www.aliexpress.com/store/product/Free-Shipping-Cardigan-Women-Lace-Sweet-gray-black-Crochet-Knit-Blouse-Long-sleeve-Tops-Women-long/1293021_2045124844.html?sdom=703.123483.111126.0_2045124844', 'http://www.aliexpress.com/store/product/Real-Genuine-Leather-case-for-Samsung-Galaxy-Note-4-Wallet-Style-Flip-Stand-Phone-Back-Cover/709298_2045064472.html?sdom=705.123485.111130.0_2045064472', 'http://www.aliexpress.com/store/product/2015-vintage-famous-brand-men-wallets-carteras-designer-luxury-genuine-leather-coin-wallet-with-change-pocket/106367_32255957257.html?sdom=704.123484.111128.0_32255957257', 'http://www.aliexpress.com/store/product/5M-5050RGB-LED-strip-150LED-Non-waterproof-44-key-controller-Kit/328535_1759883166.html?sdom=709.123489.111138.0_1759883166', 'http://www.aliexpress.com/store/product/2013-NEW-FPV-5-8G-600mW-32-Channel-Wireless-Audio-Video-A-V-Transmitting-Receiving-System/119062_1239447535.html?sdom=708.123488.111136.0_1239447535', 'http://www.aliexpress.com/store/product/8-color-upgrade-edition-2014-super-warm-winter-parka-jacket-coat-ladies-women-jacket-Slim-Short/526714_32238570601.html?sdom=703.123483.111126.0_32238570601', 'http://www.aliexpress.com/store/product/Teemi-Brand-Christmas-Gift-Mona-Lisa-Multicolour-AAA-Cubic-Zircon-Stud-Earrings-for-Women-18K-Real/1264318_1950358072.html?sdom=703.123483.111126.0_1950358072', 'http://www.aliexpress.com/store/product/Free-shipping-12pcs-6-big-6-small-PVC-3d-Butterfly-Tatoos-Wall-Sticker-Home-Decoration-Decals/1174027_1995535367.html?sdom=709.123489.111138.0_1995535367', 'http://www.aliexpress.com/store/product/New-Bicycle-Light-7-Watt-2000-Lumens-3-Mode-CREE-Q5-LED-Bike-Light-Front-Torch/1452175_32214306594.html?sdom=706.123486.111132.0_32214306594', 'http://www.aliexpress.com/store/product/3M-10-colors-Car-Flexible-EL-Wire-Neon-Light-Dance-Party-Decor-Light-Flexible-Neon-lamps/1213134_2006873690.html?sdom=709.123489.111138.0_2006873690', 'http://www.aliexpress.com/store/product/Beauty-Gifts-Zirconia-kitchen-knife-set-Ceramic-Knife-Set-3-4-5-6-inch-Covers-Free/635348_32231042215.html?sdom=709.123489.111138.0_32231042215', 'http://www.aliexpress.com/store/product/LED-Strip-3528-SMD-300leds-5M-Cool-Warm-White-Flexible-Ribbon-Tape-with-12V-2A-Power/1157502_2042214199.html?sdom=709.123489.111138.0_2042214199', 'http://www.aliexpress.com/store/product/20g-Silver-Fishing-Lure-Spoon-Mustad-Hooks-High-Quality-Surface-Plating-Good-for-Freshwater-Saltwater-Fishing/812483_32217713921.html?sdom=706.123486.111132.0_32217713921']

for cookie in cookies:
    driver.add_cookie(cookie)

def extract_product_info(product_url):
    driver.get(product_url)
    content = driver.page_source

    soup = BeautifulSoup(content, "html.parser")

    product_id = soup.find('input', {'id': 'hid-product-id'})['value']
    title = soup.find('h1', {'class': 'product-name'}).text
    price = float(soup.find('span', {'id': 'j-sku-price'}).text.split('-')[0])

    if soup.find('span', {'id': 'j-sku-discount-price'}):
        discount_price = float(soup.find('span', {'id': 'j-sku-discount-price'}).text.split('-')[0])
    else:
        discount_price = None

    properties = soup.findAll('li', {'class': 'property-item'})
    attrs_dict = {}
    for item in properties:
        name = item.find('span', {'class': 'propery-title'}).text[:-1]
        val = item.find('span', {'class': 'propery-des'}).text
        attrs_dict[name] = val
    description = json.dumps(attrs_dict)

   # stars = float(soup.find('span', {'class': 'percent-num'}).text)
   # votes = int(soup.find('span', {'itemprop': 'reviewCount'}).text)
   # orders = int(soup.find('span', {'id': 'j-order-num'}).text.split()[0].replace(',', ''))
   # wishlists = 0  # int(soup.find('span', {'id': 'j-wishlist-num'}).text.strip()[1:-1].split()[0])

    try:
     shipping_cost = soup.find('span', {'class': 'logistics-cost'}).text
       # shipping_company = soup.find('span', {'id': 'j-shipping-company'}).text
    except Exception:
        shipping_cost = ''
        shipping_company = ''
   # is_free_shipping = shipping_cost == 'Free Shipping'
   # is_epacket = shipping_company == 'ePacket'

    primary_image_url = soup.find('div', {'id': 'magnifier'}).find('img')['src']

   # store_id = soup.find('span', {'class': 'store-number'}).text.split('.')[-1]
   # store_name = soup.find('span', {'class': 'shop-name'}).find('a').text
   # #store_start_date = soup.find('span', {'class': 'store-time'}).find('em').text
   # store_start_date = datetime.strptime(store_start_date, '%b %d, %Y')

    if soup.find('span', {'class': 'rank-num'}):
        store_feedback_score = int(soup.find('span', {'class': 'rank-num'}).text)
        store_positive_feedback_rate = float(soup.find('span', {'class': 'positive-percent'}).text[:-1]) * 0.01
    else:
        driver.refresh()
        try:
            store_feedback_score = int(soup.find('span', {'class': 'rank-num'}).text)
            store_positive_feedback_rate = float(soup.find('span', {'class': 'positive-percent'}).text[:-1]) * 0.01
        except Exception:
            store_feedback_score = -1
            store_positive_feedback_rate = -1

    try:
        cats = [item.text for item in soup.find('div', {'class': 'ui-breadcrumb'}).findAll('a')]
        category = '||'.join(cats)
    except Exception:
        category = ''

    row = {
        #'product_id': product_id,
        'title': title,
        #'description': description,
        'price': price,
       # 'discount_price': discount_price,
       # 'stars': stars,
        #'votes': votes,
        #'orders': orders,
        #'wishlists': wishlists,
        #'is_free_shipping': is_free_shipping,
        #'is_epacket': is_epacket,
        'primary_image_url': primary_image_url,
        #'store_id': store_id,
        #'store_name': store_name,
        #'store_start_date': store_start_date,
        #'store_feedback_score': store_feedback_score,
        #'store_positive_feedback_rate': store_positive_feedback_rate,
        #'category': category,
        'product_url': product_url
    }
    print(row)
    return row

if __name__ == '__main__':
    for linkie in myArray:
        extract_product_info(linkie)