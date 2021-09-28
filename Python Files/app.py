from flask import Flask, request, render_template, jsonify
from hl7 import *
app = Flask(__name__)

@app.route('/process', methods=['POST', ])
def process():
    if request.method == 'POST':

        PID = 'PID|<plname>^<pfname>^<nametype>|<mlname>^<mfname>|<dob>|<gender>|<bgroup>|<streetaddress>^<city>^<pincode>|<phone1>~<phone2>|'        
        MSH = 'MSH|^~\&|HL7SOUP|<Date>|<Time>|ADT|<Random>|2.5.1'
        NK  = 'NK1|1|<klname>^<kfname>|<relation>|<kstreet>^<kcity>|<kphone>'
        PV = 'PV|<pclass>|<admtype>|<priorlocation>|<Random>|<dlname>^<dfname>^<degree>|'
        DG = '|<dsrno>|<diagnosisdesc>|<dateofdiag><timediag>|<diagtype>|<diagclassification>|<nameofdiagl>^<nameofdiagf>|'
        OBX = '|<osrno>|<valuetypeobx>|<obxdesc>|<obxvalue>|<obxunit>|<dateofobx><timeofobx>|'

        Date, Time = get_DateTime()
        Random = random_with_N_digits(6)

        #Extracting Form Data
        #PID
        plname = request.form["plname"]                      #pateintlastname
        pfname = request.form["pfname"]                      #pateintfirstname
        nametype = request.form["nametype"]                 #patientnametype
        mlname = request.form["mlname"]                     #motherlastname
        mfname = request.form["mfname"]                     #motherfirstname
        dob = request.form["dob"]                           #patientdateofbirth
        gender = request.form["gender"]                     #genderofpatient
        bgroup = request.form["bgroup"]                     #bloodgroup ofpatient
        streetaddress = request.form["streetaddress"]       #streetname 
        city = request.form["city"]                         #city
        pincode = request.form["pincode"]
        phone1 = request.form["phone1"]
        phone2 = request.form["phone2"]
        #MSH
        #name = request.form["name"]
        #relation = request.form["relation"]
        #address = request.form["address2"]
        #phone = request.form["phone"]
        #NK
        klname = request.form["klname"]
        kfname = request.form["kfname"]
        relation = request.form["relation"]
        kstreet = request.form["kstreet"]
        kcity = request.form["kcity"]
        kphone = request.form["kphone"]
        #PV
        pclass = request.form["pclass"]
        admtype = request.form["admtype"]
        priorlocation = request.form["priorlocation"]
        dlname = request.form["dlname"]
        dfname = request.form["dfname"]
        degree = request.form["degree"]
        #DG
        dsrno = request.form["dsrno"]
        diagnosisdesc = request.form["diagnosisdesc"]
        dateofdiag  = request.form["dateofdiag"]
        timediag  = request.form["timediag"]
        diagtype = request.form["diagtype"]
        diagclassification = request.form["diagclassification"]
        nameofdiagl = request.form["nameofdiagl"]
        nameofdiagf = request.form["nameofdiagf"]
        #OBX
        osrno = request.form["osrno"]
        valuetypeobx = request.form["valuetypeobx"]
        obxdesc = request.form["obxdesc"]
        obxvalue = request.form["obxvalue"]
        obxunit = request.form["obxunit"]
        dateofobx = request.form["dateofobx"]
        timeofobx = request.form["timeofobx"]

        
        

        #Editing Raw data
       
        dob = dob.replace("-", "")


        

        #Editing Main String
        #PID
        PID = PID.replace("<Random>", Random)
        PID = PID.replace("<plname>", plname)
        PID = PID.replace("<pfname>", pfname)
        PID = PID.replace("<nametype>", nametype)
        PID = PID.replace("<mlname>", mlname)
        PID = PID.replace("<mfname>", mfname)
        PID = PID.replace("<dob>", dob)
        PID = PID.replace("<gender>", gender)
        PID = PID.replace("<bgroup>", bgroup)
        PID = PID.replace("<streetaddress>", streetaddress)
        PID = PID.replace("<city>", city)
        PID = PID.replace("<pincode>", pincode)
        PID = PID.replace("<phone1>", phone1)
        PID = PID.replace("<phone2>", phone2)
        #MSH
        MSH = MSH.replace("<Date>", Date)
        MSH = MSH.replace("<Time>", Time)
        MSH = MSH.replace("<Random>", Random)
        #NK
        NK = NK.replace("<klname>", klname)
        NK = NK.replace("<kfname>", kfname)
        NK = NK.replace("<relation>", relation)
        NK = NK.replace("<kstreet>", kstreet)
        NK = NK.replace("<kcity>", kcity)
        NK = NK.replace("<kphone>", kphone)
        #PV
        PV = PV.replace("<pclass>", pclass)
        PV = PV.replace("<admtype>",admtype)
        PV = PV.replace("<priorlocation>",priorlocation)
        PV = PV.replace("<dlname>",dlname)
        PV = PV.replace("<dfname>",dfname)
        PV = PV.replace("<degree>",degree)
        #DG
        DG = DG.replace("<dsrno>",dsrno)
        DG = DG.replace("<diagnosisdesc>",diagnosisdesc)
        DG = DG.replace("<dateofdiag>",dateofdiag)
        DG = DG.replace("<timediag>",timediag)
        DG = DG.replace("<diagtype>",diagtype)
        DG = DG.replace("<diagclassification>",diagclassification)
        DG = DG.replace("<nameofdiagl>",nameofdiagl)
        DG = DG.replace("<nameofdiagf>",nameofdiagf)
        #OBX
        OBX = OBX.replace("<osrno>",osrno)
        OBX = OBX.replace("<valuetypeobx>",valuetypeobx)
        OBX = OBX.replace("<obxdesc>",obxdesc)
        OBX = OBX.replace("<obxvalue>",obxvalue)
        OBX = OBX.replace("<obxunit>",obxunit)
        OBX = OBX.replace("<dateofobx>",dateofobx)
        OBX = OBX.replace("<timeofobx>",timeofobx)
        


        result = {}
        result["PID"] = PID
        result["MSH"] = MSH
        result["NK"] = NK
        result["PV"] = PV
        result["DG"] = DG
        result["OBX"] = OBX
    return jsonify(result)


@app.route('/', methods=['GET', ])
def index():
    return render_template('fill.html')

if __name__ == '__main__':
    app.run(debug=True)
