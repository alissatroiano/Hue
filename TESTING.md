# TESTING.md

## Front-End Tests

### HTML

#### LOGIN PAGE

**- Login Page Test #1:**
	- 1. Copy the contents of `login.html` to clipboard.
	- 2. Visit [W3 Validator](https://validator.w3.org/nu/#textarea).
	- 3. Paste the content from clipboard into the validator and submit the form.
	- 4. Observe several warnings caused by code written in Django's templating language.
	- 5. Observe a few small errors, including:
		- Duplicate id used on 2 fields in the login form.
		- Incorrect placement of the `placeholder` attribute. 


## Back-End Tests

### Heroku

***Build Failed Test #1**
- Date: June 28, 2021 $ 4:38pm
- Issue: 'Build failed after replacing Django model fields'
	- 1. Open `hue-alissa.herokuapp.com` in web browser
	- 2. Navigate to 'hue-alissa.herokuapp.com/admin' and click on 'Orders'
	- 3. Observe an error message in the admin
	- 4. Observe Django application crash message on front-end of web app.
	- 5. Review error logs via `heroku logs -tail`.
	- 6. Visit Git repository on GitHub.
	- 7. Inspect specific commits to determine which changes in the Django app may have led to the Heroku application crashing.
	- 8. Observe that the Heroku hosted app started crashing after the sqlite database was zero’d out and set it up again.

Since then, I have generated 