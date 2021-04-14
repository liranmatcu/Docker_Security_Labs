# XSS Attacks Demo based on Flask web framework


# Persistent (Stored) XSS attack
1. Execute `docker-compose up` in the root of this repository.
2. Visit (http://localhost:5000/blog) in your browser.


# Reflection XSS attack
3. Run python3 hacking.py 
4. Visit (http://localhost:5000/pagenotfound) in your browser.
5. Visit (http://127.0.0.1:5000/pagenotfound?page=<img src="http://127.0.0.1:5001/get_image?name=tcu">)