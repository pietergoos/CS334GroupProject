from WhoKnows import app
import os

app.secret_key = os.urandom(24)
app.run(debug = False)
