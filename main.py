import webapp2

form="""
<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text" 
               style="height: 100px; width: 400px;">%(text)s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>

</html>
"""

def escape_html(s):
	for(i,o)in(("&","&amp;"),
				(">","&gt;"),
				("<","&lt;"),
				('"',"&quote;")):
		s=s.replace(i,o)			
	return s	

class MainPage(webapp2.RequestHandler):
    def write_form(self, text=""):
		self.response.out.write(form % {"text": text})

    def get(self):
	    self.write_form()

    def post(self):
	    user_text=self.request.get('text')
	    text=escape_html(user_text)
	    encodedText=text.encode("rot13")
	    self.write_form(encodedText)


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)