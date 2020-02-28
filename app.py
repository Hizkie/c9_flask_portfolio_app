from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'kcpgm0ka8vudfq76.chr7pe7iynqr.eu-west-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'kcpqmduod16lyyh2'
app.config['MYSQL_PASSWORD'] = 'dahm3oxh2cakdjm8'
app.config['MYSQL_DB'] = 'vnb273g86ehntst1'

mysql = MySQL(app)



@app.route('/', methods=['GET', 'POST'])

def index():
  if request.method == "POST":
    if 'sentiment' not in request.form:
      cur = mysql.connection.cursor()
      cur.execute('SELECT * FROM tweet')
      data = cur.fetchone()
      cur.close()
      return render_template("index.html", error="አባከዎን አንዱን ምርጫ ይምረጡ", tweet=data)


    else:
      details = request.form 
      ids = details['id']
      response = details['sentiment']

      curr = mysql.connection.cursor()
      curr.execute("INSERT INTO response(tweet_id, ip, country, sentiment) VALUES (%s, %s,%s,%s)", (ids,1,1, response))
      curr.execute("DELETE from tweet WHERE tweet_id = %s" % (ids))
      mysql.connection.commit()
      curr.close()
      cur = mysql.connection.cursor()
      cur.execute('SELECT * FROM tweet')
      data = cur.fetchone()

      cur.close()
      return render_template("index.html", tweet=data)
  else:
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tweet')
    data = cur.fetchone()

    cur.close()
    return render_template("index.html", tweet=data)

@app.route('/tuna')
def tuna():
  return "<h2>Tuna is good</h2>"

@app.route('/met', methods=['GET','POST'])
def met():
  if request.method == 'POST':
    return 'you are using post'
  else:
    return 'you are using get'

@app.route('/profile/<username>')
def profile(username):
  return "hay there %s"  % username

@app.route('/post/<int:post_id>')
def post(post_id):
  return "hay there %s"  % post_id

if __name__ == "__main__":
  app.run(debug=True)

