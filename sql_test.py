from flask import Flask , request , jsonify
import mysql.connector as conn
conn.connect(host='localhost',user='root',password='Reset@7830')

app = Flask(__name__)
@app.route("/create" , methods=['GET' , 'POST'])

def test1():
    try:

        _json=request.json
        _name = _json["name"]
        _emailid= _json["emailid"]
        _phone = _json["phone"]
        _address = _json["address"]
        if _name and _emailid and _phone and _address and request.method == 'POST':
            import mysql.connector as conn
            cursor = conn.cursor
            conn.connect(host='localhost', user='root', password='Reset@7830')

            sqlquery = "INSERT INTO emp(name, emailid , phone , address) VALUES (%s , %s , %s , %s)"
            bindData= (_name , _emailid , _phone , _address)
            cursor.execute = (sqlquery , bindData)
            conn.commit()
            respone= jsonify("Employee added successfully")
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print (e)
    finally:
        cursor.close()
        conn.close()

if __name__== "__main__":
    app.run()