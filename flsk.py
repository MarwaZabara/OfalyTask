from flask import Flask, jsonify,Response
from flask_restful import Api, Resource
import json
import twitter
from flask.ext.mysql import MySQL


app = Flask(__name__)
api=Api(app)


mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'marwa'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'Ofalytask'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()


Consumer_Key ="ElojnzGtxRndpzPFtk2iLy5bz"
Consumer_Secret="6hkvl4OZWhcXkGpbDPN75dVsY3DYsT4Y7ZkdsWlv1JSK0v62jt"
Access_Token="981492937484849152-CLso4ME3NQ7kqkjYtKe1SZGxKzsGOAy"
Access_Secret="w3bhReIraIg0P2evgb6yXgb686FTB3BUD1KVusZ847PeY"

twitter_api = twitter.Api(Consumer_Key,
                  Consumer_Secret,
                  Access_Token,
                 Access_Secret)

class users(Resource):
 	def get(self,id):
 		tweets=twitter_api.GetUserTimeline(id)
 		cursor = mysql.connect().cursor()
		sql = "INSERT INTO `my_table` (`uid`,`tid`,`txt`) VALUES (%s, %s, %s)"
		for x in xrange(1,25):
			obj
			cursor.execute(sql, (id, tweets[s].id,tweets[s].text))
			
 		return jsonify({tweets})
api.add_resource(users,'/users/<int:id>/posts',methods = ['GET'])


class data(Resource):
 	def get(self,id):
 		if local:
 			sql = "SELECT * from  `my_table2` WHERE `id` = (%s) "
			cursor.execute(sql, (id))	
 		else:	
	 		data=twitter_api.GetUser(id)
	 		cursor = mysql.connect().cursor()
			sql = "INSERT INTO `my_table2` (`uid`,`username`) VALUES (%s, %s)"
			cursor.execute(sql, (id,tweets[s].username))	
	 		return jsonify({data})
api.add_resource(data,'/users/<int:id>/<bool:local?>')
		#route to return last 25 posts and put in database



api.add_resource(users,'/users')						#route to return user data and update if needed (reads from database and dfisplay them)

# data=twitter_api.GetUser("784965303646158848")
# print data