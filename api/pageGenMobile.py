initial = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Powerscore on VRC Tracker</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Teko:wght@300..700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link rel="icon" type="image/x-icon" href="https://www.dropbox.com/scl/fi/jgpvl6s9otkgc6uqg5pmt/favicon.ico?rlkey=nb39qqv34ppoyk6k3b2qd1yl0&st=lgn1ldkn&raw=1">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #084d5a;
            color: #ffffff;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 108px;
        }
        title {
            font-family: 'Inter', sans-serif;
            background-color: #084d5a;
            color: #ffffff;
            margin: 0;
            padding: 0;
            display: flex;
            width: 300px;
            align-items: center;
            text-align: center;
            font-size: 24px;
            font-weight: 900;
        }
        img {
            width: 100%;
            height: 100%;
        }
        .total-parent-container {
            display: flex;
            flex-direction: column;
            height: 108px;
            align-items: center;
        }
        .input-parent-container {
            text-align: center;
            width: 100%;
            display: flex;
            flex-direction: column;
        }
        .input-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .input-container input {
            width: 250px;
            height: 20px;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px 0 0 5px;
            border: 1px solid #ffffff;
            font-family: 'Inter', sans-serif;
            letter-spacing: -0.3px;
            text-align: center;
            background-color: #084d5a;
            color: #ffffff;
        }
        .input-container button {
            width: 42px;
            height: 42px;
            border: 1px solid #ffffff;
            border-left: none;
            background-color: #084d5a;
            border-radius: 0 5px 5px 0;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .input-container button i {
            color: #ffffff;
            font-size: 15px;
        }
        .gap {
            width: 10px;
            height: 30px;
            display: block;
        }
        .gap-2 {
            width: 10px;
            height: 10px;
            display: block;
        }
        a {
            text-decoration: none;
            color: white;
        }
        .banner {
            background-color: black;
            width: 100%;
            position: fixed; /* Keeps it at the top even when scrolling */
            top: 0;
            left: 0;
            font-weight: 500;
            letter-spacing: -1px;
            font-size: 30px;
            padding-top: 20px;
            padding-bottom: 20px;
            text-align: center;
        }
        .home-button {
            background-color: black;
            position: fixed; /* Keeps it at the top even when scrolling */
            top: 22px;
            left: 22px;
            justify-content: left;
            font-weight: 500;
            font-size: 15px;
            padding: 5px 8px 5px 8px;
            border: 1px solid #ffffff;
            border-radius: 5px;
        }
        .body-parent-container {
            display: flex;
            flex-direction: column;
            width: 300px;
            height: 150px;
            border: 1px transparent;
            justify-content: center;
            align-self: center;
        }
        .body-container {
            display: flex;
            width: 300px;
            flex-direction: row;
            border: 1px solid #ffffff;
            border-radius: 5px;
            padding: 10px;
            justify-content: center;
            align-self: center;
            
        }
        .body-contained-2 {
            display: flex;
            border: 1px transparent #ffffff;
            border-radius: 5px;
            padding: 5px;
            align-self: center;
            font-size: 16px;
            width: 70px;
        }
        .body-contained-3 {
            display: flex;
            border: 1px transparent #ffffff;
            border-radius: 5px;
            padding: 5px;
            align-self: center;
            font-size: 16px;
            width: 54px;
        }
        .body-contained-4 {
            display: flex;
            border: 1px transparent #ffffff;
            border-radius: 5px;
            padding: 5px;
            align-self: center;
            font-size: 16px;
            width: 30px;
        }
        .body-contained-5 {
            display: flex;
            border: 1px transparent #ffffff;
            border-radius: 5px;
            padding: 5px 10px 5px 10px;
            align-self: center;
            font-size: 14px;
        }
        .body-contained-1 {
            display: flex;
            border: 1px transparent #ffffff;
            border-radius: 5px;
            padding: 5px;
            align-self: center;
            font-size: 12px;
        }
        .dropdown {
            font-family: 'Inter', sans-serif;
            display: flex;
            color: #ffffff;
            border: 1px solid #ffffff;
            background-color: #084d5a;
            border-radius: 5px;
            padding: 5px;
            font-size: 20px;
        }
        .download-button {
            display: flex;
            width: 140px;
            font-size: 16px;
            padding: 5px;
            border-radius: 5px;
            border: 1px solid #ffffff;
            font-family: 'Inter', sans-serif;
            letter-spacing: -0.3px;
            text-align: center;
            background-color: #095d6a;
            color: #ffffff;
            justify-content: center;
            align-items: center;
        }
        .download-text {
            font-size: 16px;
            font-family: 'Inter', sans-serif;
            letter-spacing: -0.3px;
            color: #ffffff;
            border: 0px transparent;
            background-color: #095d6a;
            cursor: pointer;
        }
        .container {
            display: flex;
            align-items: center;
            flex-direction: column;
        }
    </style>
</head>
<body>
    <div class="banner">VRC-Tracker</div>
    <div class="home-button"><a href="https://powerscore.vercel.app"> ◀ Home </a></div>
    <div class="total-parent-container">
        <div class="gap">
            <div class="gap"></div>
        </div>
        <div class="imageOverlay">
        </div>
        <div class="gap">
            <div class="gap"></div>
        </div>
        <div class="gap">
            <div class="gap"></div>
        </div>
        <div class="input-parent-container">
            <div class="input-container">
                <form action="/competitions" method="GET" class="input-container">
                    <input type="text" name="query" placeholder="Enter a Competition SKU (ex: RE-VRC-XX-XXXX)">
                    <button type="submit" id="overlayButton">
                        <i id="overlayButton" class="fas fa-search"></i>
                    </button>
                    <input type="hidden" name="division" value="1">
                </form>
            </div>
        </div>
        <div class="gap">
            <div class="gap"></div>
        </div>'''

ending = '''        <div class="gap-2"><div class="gap-2"></div></div><form action="/download" method="GET" class="download-button"><button type="submit" class="download-text">Download XLSX</button></form>
        <div class="gap">
            <div class="gap"></div>
        </div><div class="gap">
            <div class="gap"></div>
        </div></div>
    </div>
</body>
</html>'''

def generateFrom(info, sku, division = "1", excelFile = None):
    #comp = open("templates/comp.html", "w")
    name = info[0]
    powerscores = info[1]
    offensive = info[2]
    defensive = info[3]
    divisions = info[4]

    title = f'''<title>{name} Powerscore</title><div class="gap">
            <div class="gap-2"></div>
        </div>
        <div class="gap-2"><div class="gap-2"></div></div>
        '''

    dropdown = f'''<div class="container"><form id="myForm" action="/competitions" method="GET">
    <input type="hidden" id="sku" name="query" value="{sku}">
    <label for="division">Division</label>
<select name="division" id="divs" class="dropdown">'''
    
    for divID, divName in enumerate(divisions):
        if int(division) - 1 == divID:
            dropdown = dropdown + f'''<option value="{divID + 1}" selected>{divName}</option>
            '''
        else:
            dropdown = dropdown + f'''<option value="{divID + 1}">{divName}</option>
            '''

    dropdown = dropdown + '''</select></form><script>
        const selectElement = document.getElementById('divs');
        const formElement = document.getElementById('myForm');

        selectElement.addEventListener('change', () => {
            formElement.submit();
        });
    </script><div class="gap">
            <div class="gap"></div>
        </div>
        ''' + '''
        <div class="body-container">
    <div class="body-contained-5">Rank</div>
    <div class="body-contained-5">Team Name</div>
    <div class="body-contained-5">Powerscore</div>
    <div class="body-contained-5">OPS</div>
    <div class="body-contained-5">DPS</div>
</div>'''

    bodyList = ""
    for team in range(len(powerscores)):
        bodyList = bodyList + f'''
        <div class="body-container">
        <div class="body-contained-4"><b>{str(team + 1) + ". "}</b></div>
    <div class="body-contained-2"><b>{powerscores[team][0]}</b></div>
    <div class="body-contained-3">{powerscores[team][1]}</div>
    <div class="body-contained-3">{offensive[team][1]}</div>
    <div class="body-contained-4">{defensive[team][1]}</div>
</div>
'''
    
    total = initial + title + dropdown + bodyList + ending
    return total
    #comp.write(total)
    #comp.close()